# ═══════════════════════════════════════════════════════════════
#  SUPERVISOR / WATCHDOG 24/7 - OTP IVA SMS
#  ─────────────────────────────────────────────────────────────
#  Menjaga seluruh layanan tetap hidup 24 jam nonstop:
#  1. Bot Telegram (bot.py)
#  2. Web Admin Dashboard (admin_server.py)
#  3. Ngrok Tunnel (static domain - link tetap)
#  4. Auto-heal: Deteksi crash, restart otomatis, & sinkronisasi sesi
# ═══════════════════════════════════════════════════════════════

import os
import sys
import time
import subprocess
import logging
from datetime import datetime

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ [WATCHDOG] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("watchdog")

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = sys.executable
CLOUDFLARED_EXE = os.path.join(DIR_PATH, "cloudflared", "cloudflared.exe")
CLOUDFLARE_TOKEN = "eyJhIjoiYjhkNTZjN2NlYTYyZTc4YzdkN2YzOWM1YTg3Y2M2ZWEiLCJ0IjoiOWY4YjkyNzYtZmY1MC00MzgyLWI0NmQtMWY1NzUxM2JlNDEzIiwicyI6Ik5XTTRPRFEyWkdJdE5UQmpPQzAwWWpRMUxXSTJOVGN0TURGbVlUWmxaVEJpWkRrMyJ9"
CUSTOM_DOMAIN = "https://dimsong.online"
NGROK_EXE = os.path.join(DIR_PATH, "ngrok", "ngrok.exe")
NGROK_DOMAIN = "bonnet-grinning-naming.ngrok-free.dev"

processes = {
    "bot": None,
    "admin": None,
    "tunnel": None,
    "autopush": None,
}

# ── Anti-spam restart tracking ──────────────────────────────────
import json as _json

_last_restart_time = {
    "bot": 0,
    "admin": 0,
    "tunnel": 0,
    "autopush": 0,
}
_restart_fail_count = {
    "bot": 0,
    "admin": 0,
    "tunnel": 0,
    "autopush": 0,
}
MIN_RESTART_COOLDOWN = 60        # Minimum detik antar restart per service
MAX_BACKOFF          = 600       # Max 10 menit backoff
HEARTBEAT_GRACE      = 300      # 5 menit grace period setelah restart
_bot_restarted_by_health = False # Flag koordinasi: jangan double-restart


def _get_cooldown(service_name):
    """Hitung cooldown dengan exponential backoff berdasarkan jumlah gagal berturut."""
    fails = _restart_fail_count.get(service_name, 0)
    backoff = min(MIN_RESTART_COOLDOWN * (2 ** fails), MAX_BACKOFF)
    return backoff


def _can_restart(service_name):
    """Cek apakah service boleh di-restart (sudah lewat cooldown)."""
    elapsed = time.time() - _last_restart_time.get(service_name, 0)
    cooldown = _get_cooldown(service_name)
    if elapsed < cooldown:
        return False, cooldown - elapsed
    return True, 0


def _record_restart(service_name):
    """Catat waktu restart & increment fail counter."""
    _last_restart_time[service_name] = time.time()
    _restart_fail_count[service_name] = _restart_fail_count.get(service_name, 0) + 1


def _reset_fail_count(service_name):
    """Reset fail counter ketika service berhasil berjalan lama (sehat)."""
    _restart_fail_count[service_name] = 0


def _reset_heartbeat():
    """Update last_update di status.json ke sekarang agar tidak langsung trigger restart lagi."""
    status_file = os.path.join(DIR_PATH, "status.json")
    try:
        data = {}
        if os.path.exists(status_file):
            with open(status_file, "r", encoding="utf-8") as f:
                data = _json.load(f)
        data["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(status_file, "w", encoding="utf-8") as f:
            _json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.debug(f"Reset heartbeat note: {e}")


def start_bot():
    logger.info("🤖 Starting Telegram Bot (bot.py)...")
    try:
        # Pastikan proses lama benar-benar mati dulu
        if processes["bot"] and processes["bot"].poll() is None:
            logger.info("🔪 Terminating old bot process first...")
            processes["bot"].terminate()
            try:
                processes["bot"].wait(timeout=5)
            except subprocess.TimeoutExpired:
                processes["bot"].kill()
            time.sleep(2)

        proc = subprocess.Popen(
            [PYTHON_EXE, "bot.py"],
            cwd=DIR_PATH,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        processes["bot"] = proc
        _record_restart("bot")
        _reset_heartbeat()  # Reset heartbeat agar tidak langsung trigger health check
        logger.info(f"✅ Bot started with PID: {proc.pid}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        return None


def start_admin():
    logger.info("🌐 Starting Admin Server (admin_server.py)...")
    try:
        proc = subprocess.Popen(
            [PYTHON_EXE, "admin_server.py"],
            cwd=DIR_PATH,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        processes["admin"] = proc
        _record_restart("admin")
        logger.info(f"✅ Admin Server started with PID: {proc.pid}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start admin server: {e}")
        return None


def start_tunnel():
    if os.path.exists(CLOUDFLARED_EXE):
        log_path = os.path.join(DIR_PATH, "tunnel.log")
        log_file = open(log_path, "w", encoding="utf-8")

        if CLOUDFLARE_TOKEN:
            logger.info(f"🚇 Starting Permanent Cloudflare Tunnel for {CUSTOM_DOMAIN}...")
            try:
                proc = subprocess.Popen(
                    [
                        CLOUDFLARED_EXE, "tunnel", "run",
                        "--token", CLOUDFLARE_TOKEN,
                        "--protocol", "quic",
                        "--edge-ip-version", "auto",
                        "--proxy-tcp-keepalive", "60s",
                        "--proxy-keepalive-timeout", "120s",
                        "--no-chunked-encoding"
                    ],
                    cwd=DIR_PATH,
                    stdout=log_file,
                    stderr=subprocess.STDOUT,
                    creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
                )
                processes["tunnel"] = proc
                _record_restart("tunnel")
                logger.info(f"✅ Permanent Cloudflare Tunnel started with PID: {proc.pid}")
                logger.info("=" * 60)
                logger.info(f"🌐 PERMANENT DOMAIN LIVE: {CUSTOM_DOMAIN}")
                logger.info("=" * 60)

                with open(os.path.join(DIR_PATH, "tunnel_url.txt"), "w", encoding="utf-8") as uf:
                    uf.write(CUSTOM_DOMAIN)
                st_path = os.path.join(DIR_PATH, "status.json")
                if os.path.exists(st_path):
                    try:
                        with open(st_path, "r", encoding="utf-8") as sf:
                            s_d = _json.load(sf)
                        s_d["tunnel_url"] = CUSTOM_DOMAIN
                        with open(st_path, "w", encoding="utf-8") as sf:
                            _json.dump(s_d, sf, indent=2)
                    except Exception:
                        pass
                return proc
            except Exception as e:
                logger.error(f"❌ Failed to start Cloudflare Tunnel with token: {e}")
                return None

        logger.info("🚇 Starting Cloudflare Quick Tunnel (cloudflared)...")
        try:
            proc = subprocess.Popen(
                [CLOUDFLARED_EXE, "tunnel", "--url", "http://localhost:5000"],
                cwd=DIR_PATH,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
            )
            processes["tunnel"] = proc
            _record_restart("tunnel")
            logger.info(f"✅ Cloudflare Tunnel started with PID: {proc.pid}")

            def _track_cf_url():
                import re as _re
                import threading as _th
                time.sleep(2)
                for _ in range(30):
                    if os.path.exists(log_path):
                        try:
                            with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
                                txt = f.read()
                            m = _re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", txt)
                            if m:
                                cf_url = m.group(0).strip()
                                logger.info("=" * 60)
                                logger.info(f"🌐 CLOUDFLARE TUNNEL LIVE: {cf_url}")
                                logger.info("=" * 60)
                                with open(os.path.join(DIR_PATH, "tunnel_url.txt"), "w", encoding="utf-8") as uf:
                                    uf.write(cf_url)
                                st_path = os.path.join(DIR_PATH, "status.json")
                                if os.path.exists(st_path):
                                    try:
                                        with open(st_path, "r", encoding="utf-8") as sf:
                                            s_d = _json.load(sf)
                                        s_d["tunnel_url"] = cf_url
                                        with open(st_path, "w", encoding="utf-8") as sf:
                                            _json.dump(s_d, sf, indent=2)
                                    except Exception:
                                        pass
                                break
                        except Exception:
                            pass
                    time.sleep(1)

            import threading
            threading.Thread(target=_track_cf_url, daemon=True).start()
            return proc
        except Exception as e:
            logger.error(f"❌ Failed to start Cloudflare tunnel: {e}")
            return None

    if not os.path.exists(NGROK_EXE):
        logger.warning("⚠️ Neither cloudflared.exe nor ngrok.exe found, skipping tunnel auto-start")
        return None

    logger.info(f"🚇 Starting Ngrok Tunnel (domain: {NGROK_DOMAIN})...")
    try:
        log_file = open(os.path.join(DIR_PATH, "tunnel.log"), "w", encoding="utf-8")
        proc = subprocess.Popen(
            [NGROK_EXE, "http", "--domain", NGROK_DOMAIN, "5000", "--log", "stdout"],
            cwd=DIR_PATH,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        processes["tunnel"] = proc
        _record_restart("tunnel")
        logger.info(f"✅ Ngrok Tunnel started with PID: {proc.pid}")
        logger.info(f"🌐 Dashboard URL: https://{NGROK_DOMAIN}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start tunnel: {e}")
        return None


def start_autopush():
    logger.info("🐙 Starting Git Auto-Push Daemon (git_autopush.py)...")
    try:
        proc = subprocess.Popen(
            [PYTHON_EXE, "git_autopush.py"],
            cwd=DIR_PATH,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        processes["autopush"] = proc
        _record_restart("autopush")
        logger.info(f"✅ Git Auto-Push started with PID: {proc.pid}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start git autopush: {e}")
        return None


def _restart_service_if_needed(name, start_fn, extra_condition=True):
    """Helper: restart service jika mati, dengan cooldown & backoff."""
    if not extra_condition:
        return
    proc = processes.get(name)
    if proc is not None and proc.poll() is None:
        # Masih hidup, cek apakah sudah cukup lama → reset fail counter
        elapsed_since_start = time.time() - _last_restart_time.get(name, 0)
        if elapsed_since_start > 120:  # Hidup > 2 menit = dianggap sehat
            _reset_fail_count(name)
        return  # Masih jalan, skip

    exit_code = proc.poll() if proc else "None"
    can, remaining = _can_restart(name)
    if not can:
        # Masih dalam cooldown, skip (tidak log spam)
        return
    logger.warning(f"⚠️ {name.upper()} is DOWN (Exit Code: {exit_code}). Auto-restarting... "
                   f"(attempt #{_restart_fail_count.get(name, 0) + 1}, "
                   f"next cooldown: {int(_get_cooldown(name))}s)")
    start_fn()


def check_and_heal():
    """Periksa status setiap proses, auto-restart jika mati (dengan cooldown)."""
    global _bot_restarted_by_health

    # Jika bot sudah di-restart oleh health check cycle ini, skip
    if not _bot_restarted_by_health:
        _restart_service_if_needed("bot", start_bot)
    _bot_restarted_by_health = False  # Reset flag untuk cycle berikutnya

    _restart_service_if_needed("admin", start_admin)
    _restart_service_if_needed("tunnel", start_tunnel, extra_condition=(os.path.exists(CLOUDFLARED_EXE) or os.path.exists(NGROK_EXE)))
    _restart_service_if_needed("autopush", start_autopush)


def check_session_health():
    """Cek status.json untuk memastikan bot tidak macet."""
    global _bot_restarted_by_health

    status_file = os.path.join(DIR_PATH, "status.json")
    if not os.path.exists(status_file):
        return

    try:
        with open(status_file, "r", encoding="utf-8") as f:
            data = _json.load(f)

        last_str = data.get("last_update")
        if last_str:
            last_dt = datetime.strptime(last_str, "%Y-%m-%d %H:%M:%S")
            diff = (datetime.now() - last_dt).total_seconds()

            # Jika baru saja restart, beri grace period
            time_since_last_restart = time.time() - _last_restart_time.get("bot", 0)
            if time_since_last_restart < HEARTBEAT_GRACE:
                return  # Bot baru start, belum sempat update heartbeat

            # Jika bot tidak memberi heartbeat > 3 menit, restart bot
            if diff > 180:
                can, remaining = _can_restart("bot")
                if not can:
                    return  # Masih cooldown

                logger.warning(f"⚠️ Bot heartbeat stagnant for {int(diff)}s. Restarting bot to auto-fix...")
                start_bot()
                _bot_restarted_by_health = True  # Tandai agar check_and_heal tidak restart lagi
    except Exception as e:
        logger.debug(f"Health check parse note: {e}")


_singleton_socket = None


def acquire_singleton_lock(port=54321):
    """Pastikan hanya 1 instance Watchdog yang berjalan di sistem."""
    global _singleton_socket
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        s.listen(1)
        _singleton_socket = s
        return True
    except socket.error:
        return False


def main():
    if not acquire_singleton_lock():
        logger.warning("⚠️ Watchdog sudah berjalan di proses lain (Instance aktif terdeteksi).")
        logger.warning("Keluar untuk mencegah konflik proses duplikat.")
        sys.exit(99)

    logger.info("=" * 60)
    logger.info("🛡️ OTP IVA SMS - 24/7 AUTO-HEAL WATCHDOG ACTIVE")
    logger.info(f"🌐 Static URL: https://{NGROK_DOMAIN}")
    logger.info("=" * 60)

    # Start all services
    start_admin()
    time.sleep(2)
    start_bot()
    time.sleep(2)
    start_tunnel()
    time.sleep(1)
    start_autopush()

    logger.info("🚀 All services started. Entering 24/7 monitoring loop...")

    try:
        while True:
            time.sleep(10)
            check_and_heal()
            check_session_health()
    except KeyboardInterrupt:
        logger.info("🛑 Watchdog stopped by user. Terminating child services...")
        for name, proc in processes.items():
            if proc and proc.poll() is None:
                try:
                    proc.terminate()
                except Exception:
                    pass
        logger.info("Bye!")


if __name__ == "__main__":
    main()

