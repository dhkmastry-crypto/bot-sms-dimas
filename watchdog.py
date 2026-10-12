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
NGROK_EXE = os.path.join(DIR_PATH, "ngrok", "ngrok.exe")
NGROK_DOMAIN = "bonnet-grinning-naming.ngrok-free.dev"

processes = {
    "bot": None,
    "admin": None,
    "tunnel": None,
}


def start_bot():
    logger.info("🤖 Starting Telegram Bot (bot.py)...")
    try:
        proc = subprocess.Popen(
            [PYTHON_EXE, "bot.py"],
            cwd=DIR_PATH,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        processes["bot"] = proc
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
        logger.info(f"✅ Admin Server started with PID: {proc.pid}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start admin server: {e}")
        return None


def start_tunnel():
    if not os.path.exists(NGROK_EXE):
        logger.warning("⚠️ ngrok.exe not found, skipping tunnel auto-start")
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
        logger.info(f"✅ Ngrok Tunnel started with PID: {proc.pid}")
        logger.info(f"🌐 Dashboard URL: https://{NGROK_DOMAIN}")
        return proc
    except Exception as e:
        logger.error(f"❌ Failed to start tunnel: {e}")
        return None


def check_and_heal():
    """Periksa status setiap proses, auto-restart jika mati."""
    # 1. Check Bot
    if processes["bot"] is None or processes["bot"].poll() is not None:
        exit_code = processes["bot"].poll() if processes["bot"] else "None"
        logger.warning(f"⚠️ Bot is DOWN (Exit Code: {exit_code}). Auto-restarting...")
        start_bot()

    # 2. Check Admin Server
    if processes["admin"] is None or processes["admin"].poll() is not None:
        exit_code = processes["admin"].poll() if processes["admin"] else "None"
        logger.warning(f"⚠️ Admin Server is DOWN (Exit Code: {exit_code}). Auto-restarting...")
        start_admin()

    # 3. Check Ngrok Tunnel
    if os.path.exists(NGROK_EXE):
        if processes["tunnel"] is None or processes["tunnel"].poll() is not None:
            exit_code = processes["tunnel"].poll() if processes["tunnel"] else "None"
            logger.warning(f"⚠️ Tunnel is DOWN (Exit Code: {exit_code}). Auto-restarting...")
            start_tunnel()


def check_session_health():
    """Cek status.json untuk memastikan bot tidak macet."""
    status_file = os.path.join(DIR_PATH, "status.json")
    if not os.path.exists(status_file):
        return

    try:
        import json
        with open(status_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        last_str = data.get("last_update")
        if last_str:
            last_dt = datetime.strptime(last_str, "%Y-%m-%d %H:%M:%S")
            diff = (datetime.now() - last_dt).total_seconds()
            # Jika bot tidak memberi heartbeat > 3 menit, restart bot
            if diff > 180:
                logger.warning(f"⚠️ Bot heartbeat stagnant for {int(diff)}s. Restarting bot to auto-fix...")
                if processes["bot"] and processes["bot"].poll() is None:
                    processes["bot"].terminate()
                    time.sleep(2)
                start_bot()
    except Exception as e:
        logger.debug(f"Health check parse note: {e}")


def main():
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

