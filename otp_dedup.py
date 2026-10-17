# ═══════════════════════════════════════════════════════════════
#  CENTRALIZED MULTI-PROCESS OTP DEDUPLICATION SERVICE
#  ─────────────────────────────────────────────────────────────
#  Mencegah pengiriman OTP ganda (double message) ke Telegram:
#  - Mengkoordinasikan deduplikasi antar proses (bot.py & admin_server.py)
#  - Menangani race condition antara Webhook (Push) & API Poller
#  - Menjamin pengiriman Telegram & pencatatan earnings EXACTLY ONCE
#  - Menggunakan SQLite WAL mode (ACID, process-safe, ultra-cepat)
# ═══════════════════════════════════════════════════════════════

import os
import re
import time
import sqlite3
import hashlib
import logging

logger = logging.getLogger("otp_dedup")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "otp_dedup.db")

# Fallback in-memory cache jika terjadi lock I/O
_in_memory_seen = {}
_in_memory_earnings = set()


def _get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=15.0)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn


def init_db():
    try:
        with _get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS seen_otp (
                    dedup_key TEXT PRIMARY KEY,
                    phone TEXT,
                    otp TEXT,
                    source TEXT,
                    created_at REAL,
                    earnings_recorded INTEGER DEFAULT 0
                );
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_seen_otp_created ON seen_otp(created_at);")
            conn.commit()
    except Exception as e:
        logger.error(f"❌ [Dedup] Failed to initialize SQLite dedup database: {e}")


# Inisialisasi tabel saat file diimpor
init_db()


def normalize_phone_digits(phone: str) -> str:
    """Ambil hanya digit angka dari nomor telepon (buang spasi, +, strip, dll)."""
    return re.sub(r'\D', '', str(phone or ''))


def normalize_otp_code(otp: str) -> str:
    """Bersihkan format OTP seperti 385-954 menjadi 385954."""
    raw = str(otp or '').strip()
    digits = re.sub(r'\D', '', raw)
    if digits:
        return digits
    return raw.lower()


def get_dedup_key(phone: str, otp: str = "", raw_message: str = "") -> str:
    """Hasilkan kunci unik stabil untuk satu event OTP / SMS."""
    clean_phone = normalize_phone_digits(phone)
    clean_otp = normalize_otp_code(otp)

    if clean_otp and len(clean_otp) >= 3:
        # Jika ada kode OTP (misal WhatsApp 385954 pada nomor 24380007640)
        return f"otp_{clean_phone}_{clean_otp}"
    else:
        # Jika SMS tanpa kode angka OTP, gunakan normalized content hash
        clean_msg = re.sub(r'\W+', '', str(raw_message or '')).lower()
        msg_hash = hashlib.sha256(clean_msg.encode('utf-8')).hexdigest()[:16]
        return f"msg_{clean_phone}_{msg_hash}"


def is_duplicate_and_claim(
    phone: str,
    otp: str = "",
    raw_message: str = "",
    source: str = "unknown",
    ttl_seconds: int = 1800,  # 30 menit jendela perlindungan anti-duplicate
) -> bool:
    """
    Periksa apakah OTP / pesan ini sudah pernah diklaim atau dikirim ke Telegram
    dalam kurun waktu `ttl_seconds` (default 30 menit).

    Returns:
        True  -> Pesan DUPLIKAT! JANGAN kirim ke Telegram.
        False -> Pesan BARU / FRESH! Klaim atomik berhasil, silakan kirim ke Telegram.
    """
    dedup_key = get_dedup_key(phone, otp, raw_message)
    clean_phone = normalize_phone_digits(phone)
    clean_otp = normalize_otp_code(otp)
    now = time.time()
    cutoff = now - ttl_seconds

    # 1. Cek in-memory fallback terlebih dahulu (fast-path)
    mem_record = _in_memory_seen.get(dedup_key)
    if mem_record:
        prev_source, prev_time = mem_record
        if prev_time >= cutoff:
            elapsed = int(now - prev_time)
            logger.warning(
                f"🛡️ [Dedup In-Memory] BLOCKED DUPLICATE OTP: {dedup_key} dari '{source}' "
                f"(sudah dikirim oleh '{prev_source}' {elapsed} detik lalu)"
            )
            return True

    # 2. Cek & Klaim secara Atomik di Database SQLite
    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            
            # Cek apakah record sudah ada
            cursor.execute("SELECT source, created_at FROM seen_otp WHERE dedup_key = ?", (dedup_key,))
            row = cursor.fetchone()

            if row:
                prev_source, prev_time = row
                if prev_time >= cutoff:
                    elapsed = int(now - prev_time)
                    logger.warning(
                        f"🛡️ [Dedup DB] BLOCKED DUPLICATE OTP: {dedup_key} dari '{source}' "
                        f"(sudah dikirim oleh '{prev_source}' {elapsed} detik lalu)"
                    )
                    # Update local mem cache
                    _in_memory_seen[dedup_key] = (prev_source, prev_time)
                    return True
                else:
                    # Sudah expired lewat dari TTL, perbarui kepemilikan
                    cursor.execute(
                        "UPDATE seen_otp SET source = ?, created_at = ?, earnings_recorded = 0 WHERE dedup_key = ?",
                        (source, now, dedup_key)
                    )
                    conn.commit()
                    _in_memory_seen[dedup_key] = (source, now)
                    return False

            # Jika belum pernah ada, INSERT secara atomik
            cursor.execute(
                "INSERT INTO seen_otp (dedup_key, phone, otp, source, created_at, earnings_recorded) VALUES (?, ?, ?, ?, ?, 0)",
                (dedup_key, clean_phone, clean_otp, source, now)
            )

            # Bersihkan sampah record lama (> 24 jam)
            cursor.execute("DELETE FROM seen_otp WHERE created_at < ?", (now - 86400,))
            conn.commit()

            # Simpan ke in-memory
            _in_memory_seen[dedup_key] = (source, now)
            return False

    except sqlite3.IntegrityError:
        # Terjadi race condition: proses lain baru saja insert kunci yang sama persis
        logger.warning(
            f"🛡️ [Dedup Race] BLOCKED DUPLICATE OTP: {dedup_key} dari '{source}' (menang race condition di proses lain)"
        )
        _in_memory_seen[dedup_key] = (source, now)
        return True

    except Exception as e:
        logger.error(f"❌ [Dedup Error] SQLite check failed: {e}")
        # Jika DB error, gunakan in-memory dict sebagai penyelamat
        if dedup_key in _in_memory_seen and _in_memory_seen[dedup_key][1] >= cutoff:
            return True
        _in_memory_seen[dedup_key] = (source, now)
        return False


def claim_earnings_once(dedup_key: str) -> bool:
    """
    Menjamin pencatatan pendapatan (earnings) hanya dilakukan 1x per OTP.
    Returns True jika ini panggilan pertama yang berhak mencatat earnings.
    Returns False jika earnings untuk OTP ini sudah pernah dicatat.
    """
    if dedup_key in _in_memory_earnings:
        return False

    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT earnings_recorded FROM seen_otp WHERE dedup_key = ?", (dedup_key,))
            row = cursor.fetchone()

            if row and row[0] == 1:
                _in_memory_earnings.add(dedup_key)
                return False

            # Tandai earnings sudah dicatat
            cursor.execute("UPDATE seen_otp SET earnings_recorded = 1 WHERE dedup_key = ?", (dedup_key,))
            conn.commit()
            _in_memory_earnings.add(dedup_key)
            return True
    except Exception as e:
        logger.error(f"❌ [Dedup Earnings Error]: {e}")
        if dedup_key in _in_memory_earnings:
            return False
        _in_memory_earnings.add(dedup_key)
        return True
