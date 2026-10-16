# ═══════════════════════════════════════════════════════════════
#  TELEGRAM FILE SENDER - AUTO EXPORT & SEND NUMBERS TXT
#  ─────────────────────────────────────────────────────────────
#  Otomatis mengekspor seluruh nomor akun Augestel ke file .txt
#  dan mengirimkannya langsung ke chat pribadi Pemilik Bot Telegram.
# ═══════════════════════════════════════════════════════════════

import os
import sys

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

import re
import json
import time
import logging
import requests
from datetime import datetime

logger = logging.getLogger("telegram_file_sender")
if not logger.handlers:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("%(asctime)s │ %(levelname)-8s │ [FileSender] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
os.makedirs(EXPORTS_DIR, exist_ok=True)

# Cache debounce pengiriman agar tidak spam
_LAST_SENT_INFO = {
    "timestamp": 0.0,
    "total_numbers": -1,
}


def get_config_val(key: str, default: str = "") -> str:
    """Ambil nilai konfigurasi langsung dari config.py tanpa cache."""
    cfg_file = os.path.join(BASE_DIR, "config.py")
    if not os.path.exists(cfg_file):
        return default
    try:
        with open(cfg_file, "r", encoding="utf-8") as f:
            content = f.read()
        m = re.search(rf'^{key}\s*=\s*["\'](.*?)["\']', content, re.MULTILINE)
        if m:
            return m.group(1).strip()
    except Exception as e:
        logger.error(f"Error reading {key} from config.py: {e}")
    return default


def set_owner_chat_id(chat_id: str) -> bool:
    """Simpan Chat ID Pemilik ke config.py secara aman."""
    clean_id = str(chat_id).strip()
    if not clean_id:
        return False

    cfg_file = os.path.join(BASE_DIR, "config.py")
    try:
        with open(cfg_file, "r", encoding="utf-8") as f:
            content = f.read()

        if re.search(r'OWNER_CHAT_ID\s*=\s*["\'].*?["\']', content):
            new_content = re.sub(
                r'OWNER_CHAT_ID\s*=\s*["\'].*?["\']',
                f'OWNER_CHAT_ID = "{clean_id}"',
                content
            )
        else:
            # Sisipkan setelah GROUP_CHAT_ID
            new_content = re.sub(
                r'(GROUP_CHAT_ID\s*=\s*["\'].*?["\'])',
                r'\1\n\n# Chat ID Pribadi Pemilik Bot (Penerima file nomor .txt otomatis)\nOWNER_CHAT_ID = "' + clean_id + '"',
                content
            )

        with open(cfg_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info(f"✅ OWNER_CHAT_ID berhasil disimpan ke config.py: {clean_id}")
        return True
    except Exception as e:
        logger.error(f"❌ Gagal menyimpan OWNER_CHAT_ID ke config.py: {e}")
        return False


def get_owner_chat_id() -> str:
    """Dapatkan Chat ID Pemilik saat ini."""
    val = get_config_val("OWNER_CHAT_ID")
    if val:
        return val
    try:
        import config
        return getattr(config, "OWNER_CHAT_ID", "").strip()
    except Exception:
        return ""


def get_bot_token() -> str:
    val = get_config_val("BOT_TOKEN")
    if val:
        return val
    try:
        import config
        return getattr(config, "BOT_TOKEN", "").strip()
    except Exception:
        return ""


def get_fallback_chat_id() -> str:
    val = get_config_val("GROUP_CHAT_ID")
    if val:
        return val
    try:
        import config
        return getattr(config, "GROUP_CHAT_ID", "").strip()
    except Exception:
        return ""


def send_telegram_document(chat_id: str, file_path: str, caption: str = "") -> dict:
    """Mengirim file dokumen ke chat Telegram via HTTP API resmi."""
    token = get_bot_token()
    if not token:
        logger.error("❌ BOT_TOKEN tidak ditemukan!")
        return {"success": False, "message": "BOT_TOKEN belum diatur!"}

    if not os.path.exists(file_path):
        logger.error(f"❌ File tidak ditemukan: {file_path}")
        return {"success": False, "message": "File dokumen tidak ditemukan!"}

    url = f"https://api.telegram.org/bot{token}/sendDocument"

    try:
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as doc_file:
            files = {
                "document": (filename, doc_file, "text/plain")
            }
            data = {
                "chat_id": str(chat_id),
                "caption": caption,
                "parse_mode": "HTML",
            }
            res = requests.post(url, data=data, files=files, timeout=45)

        res_json = res.json()
        if res_json.get("ok"):
            logger.info(f"🚀 Dokumen {filename} berhasil terkirim ke Telegram Chat ID: {chat_id}")
            return {"success": True, "message": "Dokumen berhasil terkirim ke Telegram!", "result": res_json.get("result")}
        else:
            err_desc = res_json.get("description", "Unknown Telegram API Error")
            logger.error(f"❌ Gagal mengirim dokumen ke Telegram ({chat_id}): {err_desc}")
            return {"success": False, "message": f"Telegram error: {err_desc}"}
    except Exception as e:
        logger.error(f"❌ Exception saat kirim dokumen ke Telegram: {e}")
        return {"success": False, "message": f"Koneksi gagal: {e}"}


def export_and_send_augestel_numbers_txt(
    target_chat_id: str = None,
    force: bool = False,
    trigger_reason: str = "Deteksi Otomatis"
) -> dict:
    """
    Ekspor seluruh nomor Augestel ke file .txt (1 nomor per baris)
    dan kirimkan langsung ke Pemilik Bot Telegram.
    """
    global _LAST_SENT_INFO

    now = time.time()
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    disp_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # 1. Tentukan Chat ID penerima (Prioritas: Argumen > OWNER_CHAT_ID > GROUP_CHAT_ID)
    owner_id = (target_chat_id or get_owner_chat_id() or "").strip()
    is_owner_target = bool(owner_id)

    if not owner_id:
        # Fallback ke group jika owner belum set
        owner_id = get_fallback_chat_id().strip()
        logger.warning(f"⚠️ OWNER_CHAT_ID belum diisi. Menggunakan fallback GROUP_CHAT_ID: {owner_id}")

    if not owner_id:
        msg = "Chat ID Telegram belum diatur! Buka bot Telegram dan kirim pesan /start atau /setowner di chat pribadi."
        logger.warning(f"⚠️ {msg}")
        return {"success": False, "message": msg}

    # 2. Ambil data nomor dari cache agregasi Augestel
    cache_file = os.path.join(BASE_DIR, "augestel_numbers_cache.json")
    numbers_list = []
    total_from_portal = 0
    accounts_breakdown = []

    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                c_data = json.load(f)
                numbers_list = c_data.get("numbers", [])
                total_from_portal = c_data.get("total", len(numbers_list))
                accounts_breakdown = c_data.get("accounts_breakdown", [])
        except Exception as e:
            logger.warning(f"Gagal membaca augestel_numbers_cache.json: {e}")

    # Jika cache agregasi kosong, coba baca cache per akun (1..16)
    if not numbers_list:
        logger.info("Mengumpulkan nomor dari file cache per akun (1..16)...")
        seen_nums = set()
        for i in range(1, 17):
            indiv_file = os.path.join(BASE_DIR, f"augestel_numbers_cache_{i}.json")
            if os.path.exists(indiv_file):
                try:
                    with open(indiv_file, "r", encoding="utf-8") as f:
                        indiv_data = json.load(f)
                        sub_items = indiv_data.get("numbers", [])
                        for item in sub_items:
                            n = str(item.get("number", "")).strip()
                            if n and n not in seen_nums:
                                seen_nums.add(n)
                                numbers_list.append(item)
                except Exception:
                    pass

    total_count = len(numbers_list)
    if total_count == 0:
        logger.warning("⚠️ Tidak ada nomor Augestel yang terdeteksi untuk diekspor.")
        return {"success": False, "message": "Belum ada nomor yang terdeteksi pada seluruh akun Augestel."}

    # 3. Debounce check: Jika tidak dipaksa (force=False), hindari kirim ulang jika nomor sama persis dalam 90 detik
    if not force:
        time_diff = now - _LAST_SENT_INFO["timestamp"]
        if time_diff < 90 and _LAST_SENT_INFO["total_numbers"] == total_count:
            logger.info(f"⏳ Lewati kirim file TXT (Debounce: baru dikirim {int(time_diff)}s lalu dengan jumlah nomor sama).")
            return {"success": True, "message": "Debounce: file sudah terkirim baru-baru ini.", "skipped": True}

    # 4. Buat isi TXT: Deretan nomor bersih per baris (1 nomor per baris)
    lines = []
    for item in numbers_list:
        num = str(item.get("number", "")).strip()
        if num:
            lines.append(num)

    txt_content = "\n".join(lines)

    # 5. Simpan file TXT ke folder exports/
    file_name = f"augestel_numbers_ALL_ACCOUNTS_{date_str}.txt"
    file_path = os.path.join(EXPORTS_DIR, file_name)

    latest_file_name = "augestel_numbers_latest.txt"
    latest_file_path = os.path.join(EXPORTS_DIR, latest_file_name)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(txt_content)
        with open(latest_file_path, "w", encoding="utf-8") as f:
            f.write(txt_content)
        logger.info(f"💾 File TXT berhasil disimpan di: {file_path} ({len(lines)} baris nomor)")
    except Exception as e:
        logger.error(f"❌ Gagal menyimpan file TXT: {e}")
        return {"success": False, "message": f"Gagal simpan file TXT: {e}"}

    # 6. Hitung statistik akun
    active_accounts = len([b for b in accounts_breakdown if b.get("total", 0) > 0]) or 16
    total_accounts = len(accounts_breakdown) or 16

    # 7. Susun caption Telegram yang informatif & elegan
    target_label = "👑 Pemilik Bot (Chat Pribadi)" if is_owner_target else "👥 Grup Telegram"
    caption = (
        f"📁 <b>File Nomor Augestel Otomatis</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 <b>Pemicu:</b> {trigger_reason}\n"
        f"👥 <b>Total Akun:</b> {total_accounts} Akun Terdaftar\n"
        f"📊 <b>Akun Terisi:</b> {active_accounts} Akun Aktif\n"
        f"🔢 <b>Total Nomor:</b> {len(lines):,} Nomor\n"
        f"📅 <b>Waktu:</b> {disp_time} WIB\n"
        f"🎯 <b>Tujuan:</b> {target_label}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"<i>💡 File .txt terlampir berisi 1 nomor per baris, siap di-copy atau dimasukkan ke software lain.</i>"
    )

    # 8. Kirim dokumen ke Telegram
    send_res = send_telegram_document(owner_id, file_path, caption=caption)

    if send_res.get("success"):
        _LAST_SENT_INFO["timestamp"] = now
        _LAST_SENT_INFO["total_numbers"] = total_count

    return {
        "success": send_res.get("success", False),
        "message": send_res.get("message", ""),
        "file_path": file_path,
        "total_numbers": len(lines),
        "target_chat_id": owner_id,
    }


if __name__ == "__main__":
    print("Testing export_and_send_augestel_numbers_txt...")
    res = export_and_send_augestel_numbers_txt(force=True, trigger_reason="Uji Coba Langsung CLI")
    print("Result:", res)
