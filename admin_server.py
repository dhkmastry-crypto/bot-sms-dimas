# ═══════════════════════════════════════════════════════════════
#  ADMIN DASHBOARD SERVER - OTP IVA SMS
#  ─────────────────────────────────────────────────────────────
#  Web admin panel untuk mengelola OTP Bot, SMS Log,
#  Auto-Add Numbers, dan konfigurasi.
# ═══════════════════════════════════════════════════════════════

import os
import sys

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

import asyncio
import json
import logging
import re
import subprocess
import threading
import time
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, render_template, jsonify, request, redirect, url_for, session, send_file, Response

# ────────────────────────────────────────────
#  APP SETUP
# ────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = "otp-iva-sms-admin-secret-2026"

logger = logging.getLogger("admin")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# ────────────────────────────────────────────
#  IN-MEMORY STATE
# ────────────────────────────────────────────

# SMS Log storage (in-memory, loads from bot.log)
sms_log = []

# Bot process reference
bot_process = None
bot_status = {"running": False, "pid": None, "started_at": None}

# Auto-add state
auto_add_state = {
    "running": False,
    "range_name": "",
    "max_add": 0,
    "delay": 60,
    "added": 0,
    "failed": 0,
    "skipped": 0,
    "total_found": 0,
    "current_action": 0,
    "last_message": "",
    "started_at": None,
    "process": None,
}

# IVASMS connection state
ivasms_status = {
    "connected": False,
    "last_check": None,
    "cookies_valid": False,
}

# Admin credentials
ADMIN_USER = "admin"
ADMIN_PASS = "admin123"


# ────────────────────────────────────────────
#  AUTH DECORATOR
# ────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# ────────────────────────────────────────────
#  HELPER FUNCTIONS
# ────────────────────────────────────────────

def load_config():
    """Load current config from config.py"""
    config = {}
    config_path = os.path.join(os.path.dirname(__file__), "config.py")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Parse key-value pairs
        patterns = {
            "BOT_TOKEN": r'BOT_TOKEN\s*=\s*"([^"]*)"',
            "GROUP_CHAT_ID": r'GROUP_CHAT_ID\s*=\s*"([^"]*)"',
            "CHANNEL_LINK": r'CHANNEL_LINK\s*=\s*"([^"]*)"',
            "GROUP_LINK": r'GROUP_LINK\s*=\s*"([^"]*)"',
            "FILE_LINK": r'FILE_LINK\s*=\s*"([^"]*)"',
            "NUMBER_LINK": r'NUMBER_LINK\s*=\s*"([^"]*)"',
            "OWNER_LINK": r'OWNER_LINK\s*=\s*"([^"]*)"',
            "SENSOR_TEXT": r'SENSOR_TEXT\s*=\s*"([^"]*)"',
            "BOT_NAME": r'BOT_NAME\s*=\s*"([^"]*)"',
            "IVASMS_URL": r'IVASMS_URL\s*=\s*"([^"]*)"',
            "IVASMS_EMAIL": r'IVASMS_EMAIL\s*=\s*"([^"]*)"',
            "IVASMS_PASSWORD": r'IVASMS_PASSWORD\s*=\s*"([^"]*)"',
            "IVASMS_EMAIL_2": r'IVASMS_EMAIL_2\s*=\s*"([^"]*)"',
            "IVASMS_PASSWORD_2": r'IVASMS_PASSWORD_2\s*=\s*"([^"]*)"',
            "POLL_INTERVAL": r'POLL_INTERVAL\s*=\s*(\d+)',
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                config[key] = match.group(1)
        
        # Fallbacks
        if not config.get("FILE_LINK"):
            config["FILE_LINK"] = config.get("NUMBER_LINK", "")
        if not config.get("CHANNEL_LINK"):
            config["CHANNEL_LINK"] = config.get("GROUP_LINK", "")
        if not config.get("SENSOR_TEXT"):
            config["SENSOR_TEXT"] = "••••"
        if not config.get("IVASMS_EMAIL_2"):
            config["IVASMS_EMAIL_2"] = ""
        if not config.get("IVASMS_PASSWORD_2"):
            config["IVASMS_PASSWORD_2"] = ""
    except Exception as e:
        logger.error(f"Error loading config: {e}")
    
    return config


def save_config(new_config):
    """Save config changes to config.py"""
    config_path = os.path.join(os.path.dirname(__file__), "config.py")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Sync FILE_LINK / NUMBER_LINK and CHANNEL_LINK / GROUP_LINK
        if "FILE_LINK" in new_config:
            new_config["NUMBER_LINK"] = new_config["FILE_LINK"]
        elif "NUMBER_LINK" in new_config:
            new_config["FILE_LINK"] = new_config["NUMBER_LINK"]

        if "CHANNEL_LINK" in new_config:
            new_config["GROUP_LINK"] = new_config["CHANNEL_LINK"]
        elif "GROUP_LINK" in new_config:
            new_config["CHANNEL_LINK"] = new_config["GROUP_LINK"]

        replacements = {
            "BOT_TOKEN": (r'(BOT_TOKEN\s*=\s*)"[^"]*"', r'\1"{}"'),
            "GROUP_CHAT_ID": (r'(GROUP_CHAT_ID\s*=\s*)"[^"]*"', r'\1"{}"'),
            "CHANNEL_LINK": (r'(CHANNEL_LINK\s*=\s*)"[^"]*"', r'\1"{}"'),
            "GROUP_LINK": (r'(GROUP_LINK\s*=\s*)"[^"]*"', r'\1"{}"'),
            "FILE_LINK": (r'(FILE_LINK\s*=\s*)"[^"]*"', r'\1"{}"'),
            "NUMBER_LINK": (r'(NUMBER_LINK\s*=\s*)"[^"]*"', r'\1"{}"'),
            "OWNER_LINK": (r'(OWNER_LINK\s*=\s*)"[^"]*"', r'\1"{}"'),
            "SENSOR_TEXT": (r'(SENSOR_TEXT\s*=\s*)"[^"]*"', r'\1"{}"'),
            "BOT_NAME": (r'(BOT_NAME\s*=\s*)"[^"]*"', r'\1"{}"'),
            "IVASMS_EMAIL": (r'(IVASMS_EMAIL\s*=\s*)"[^"]*"', r'\1"{}"'),
            "IVASMS_PASSWORD": (r'(IVASMS_PASSWORD\s*=\s*)"[^"]*"', r'\1"{}"'),
            "IVASMS_EMAIL_2": (r'(IVASMS_EMAIL_2\s*=\s*)"[^"]*"', r'\1"{}"'),
            "IVASMS_PASSWORD_2": (r'(IVASMS_PASSWORD_2\s*=\s*)"[^"]*"', r'\1"{}"'),
            "POLL_INTERVAL": (r'(POLL_INTERVAL\s*=\s*)\d+', r'\1{}'),
        }
        
        for key, (pattern, replacement) in replacements.items():
            if key in new_config and new_config[key] is not None:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement.format(new_config[key]), content)
                else:
                    # Append if key not present
                    content += f'\n{key} = "{new_config[key]}"'
        
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return True
    except Exception as e:
        logger.error(f"Error saving config: {e}")
        return False


def parse_bot_log():
    """Parse bot.log to extract SMS entries"""
    log_path = os.path.join(os.path.dirname(__file__), "bot.log")
    entries = []
    
    if not os.path.exists(log_path):
        return entries
    
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        
        # Parse OTP messages from log
        for line in lines:
            # Look for SMS forwarded or sent OTP lines
            if "Sent OTP" in line or "New OTP" in line or "Forwarded" in line or "new SMS" in line.lower():
                timestamp_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
                timestamp = timestamp_match.group(1) if timestamp_match else ""
                entries.append({
                    "timestamp": timestamp,
                    "message": line.strip(),
                    "type": "otp"
                })
            elif "Marked" in line and "initial SMS" in line:
                timestamp_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
                timestamp = timestamp_match.group(1) if timestamp_match else ""
                entries.append({
                    "timestamp": timestamp,
                    "message": line.strip(),
                    "type": "info"
                })
            elif "ERROR" in line or "error" in line:
                timestamp_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
                timestamp = timestamp_match.group(1) if timestamp_match else ""
                entries.append({
                    "timestamp": timestamp,
                    "message": line.strip(),
                    "type": "error"
                })
    except Exception as e:
        logger.error(f"Error parsing bot log: {e}")
    
    return entries[-100:]  # Last 100 entries


def get_log_tail(n=50):
    """Get last N lines from bot.log"""
    log_path = os.path.join(os.path.dirname(__file__), "bot.log")
    if not os.path.exists(log_path):
        return []
    
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        return [line.strip() for line in lines[-n:]]
    except:
        return []


def check_bot_running():
    """Check if bot.py is running"""
    global bot_status
    try:
        if bot_process and bot_process.poll() is None:
            bot_status["running"] = True
            bot_status["pid"] = bot_process.pid
        else:
            # Check system processes for bot.py
            if sys.platform == "win32":
                # Cari proses python yang menjalankan bot.py via powershell
                cmd = 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like \'*bot.py*\' } | Select-Object -ExpandProperty ProcessId"'
                res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
                out = res.stdout.strip()
                if out:
                    pids = [int(p) for p in out.splitlines() if p.strip().isdigit()]
                    valid_pids = [p for p in pids if p != os.getpid()]
                    if valid_pids:
                        bot_status["running"] = True
                        bot_status["pid"] = valid_pids[0]
                        return bot_status
            else:
                # Linux check
                result = subprocess.run(
                    ["pgrep", "-f", "bot.py"],
                    capture_output=True, text=True, timeout=5
                )
                if result.returncode == 0 and result.stdout.strip():
                    pids = result.stdout.strip().splitlines()
                    valid_pids = [int(p) for p in pids if int(p) != os.getpid()]
                    if valid_pids:
                        bot_status["running"] = True
                        bot_status["pid"] = valid_pids[0]
                        return bot_status
            bot_status["running"] = False
            bot_status["pid"] = None
    except:
        pass
    return bot_status


def get_shared_status():
    """Baca status real-time dari bot.py (status.json) agar sinkron dengan Telegram."""
    status_file = os.path.join(os.path.dirname(__file__), "status.json")
    if os.path.exists(status_file):
        try:
            with open(status_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            last_update_str = data.get("last_update")
            if last_update_str:
                last_dt = datetime.strptime(last_update_str, "%Y-%m-%d %H:%M:%S")
                # Jika diperbarui dalam 60 detik terakhir, bot sedang aktif polling
                if (datetime.now() - last_dt).total_seconds() < 60:
                    return data
        except Exception:
            pass
    return None


async def check_ivasms_connection(target_index: int = None):
    """Check IVASMS connection for each registered account, or specific account if target_index given"""
    global ivasms_status
    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        cfg = load_config()
        if cfg.get("IVASMS_EMAIL") and cfg.get("IVASMS_PASSWORD"):
            accounts.append({"email": cfg["IVASMS_EMAIL"], "password": cfg["IVASMS_PASSWORD"]})
        if cfg.get("IVASMS_EMAIL_2") and cfg.get("IVASMS_PASSWORD_2"):
            accounts.append({"email": cfg["IVASMS_EMAIL_2"], "password": cfg["IVASMS_PASSWORD_2"]})

    existing_results = {r.get("index"): r for r in ivasms_status.get("accounts", []) if isinstance(r, dict)}
    results = []
    any_connected = False
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    import importlib, config
    importlib.reload(config)
    from ivasms_scraper import IVASMSClient

    for idx, acc in enumerate(accounts, start=1):
        email = acc.get("email", "")
        pwd = acc.get("password", "")
        if not email:
            continue

        # If checking a single account, preserve others
        if target_index is not None and idx != target_index:
            prev = existing_results.get(idx, {
                "index": idx,
                "email": email,
                "connected": False,
                "last_check": "-"
            })
            if prev.get("connected"):
                any_connected = True
            results.append(prev)
            continue

        cookies = acc.get("cookies") or (config.COOKIES if idx == 1 else getattr(config, "COOKIES_2", {}) if idx == 2 else {})
        client = IVASMSClient(cookies, config.IVASMS_URL)
        connected = client.check_connection()

        if not connected:
            # Fallback browser sync
            try:
                from cookie_sync import get_fresh_cookies_from_browser
                fresh = await get_fresh_cookies_from_browser(account_index=idx, email=email, password=pwd)
                if fresh and "ivas_sms_session" in fresh:
                    client.update_cookies(fresh)
                    connected = client.check_connection()
            except Exception as e:
                logger.error(f"Error checking acc {idx}: {e}")

        if connected:
            any_connected = True

        results.append({
            "index": idx,
            "email": email,
            "connected": connected,
            "last_check": now_str
        })

    ivasms_status["connected"] = any_connected
    ivasms_status["last_check"] = now_str
    ivasms_status["accounts"] = results

    # Sync to status.json
    try:
        status_file = os.path.join(os.path.dirname(__file__), "status.json")
        s_data = {}
        if os.path.exists(status_file):
            with open(status_file, "r", encoding="utf-8") as f:
                s_data = json.load(f)
        s_data["ivasms_connected"] = any_connected
        s_data["last_update"] = now_str
        s_data["accounts_status"] = results
        with open(status_file, "w", encoding="utf-8") as f:
            json.dump(s_data, f, indent=2)
    except Exception:
        pass

    return ivasms_status


# ────────────────────────────────────────────
#  ROUTES - AUTH
# ────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == ADMIN_USER and password == ADMIN_PASS:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ────────────────────────────────────────────
#  ROUTES - PAGES
# ────────────────────────────────────────────

@app.route("/")
@login_required
def dashboard():
    return render_template("admin.html", page="dashboard")


@app.route("/sms-log")
@login_required
def sms_log_page():
    return render_template("admin.html", page="sms-log")


@app.route("/accounts")
@login_required
def accounts_page():
    return render_template("admin.html", page="accounts")


@app.route("/augestel-accounts")
@login_required
def augestel_accounts_page():
    return render_template("admin.html", page="augestel-accounts")


@app.route("/auto-add")
@login_required
def auto_add_page():
    return render_template("admin.html", page="auto-add")


@app.route("/auto-add-augestel")
@login_required
def auto_add_augestel_page():
    return render_template("admin.html", page="auto-add-augestel")


@app.route("/numbers")
@login_required
def numbers_page():
    return render_template("admin.html", page="numbers")


@app.route("/bot-control")
@login_required
def bot_control_page():
    return render_template("admin.html", page="bot-control")


@app.route("/settings")
@login_required
def settings_page():
    return render_template("admin.html", page="settings")


# ────────────────────────────────────────────
#  API ROUTES
# ────────────────────────────────────────────

@app.route("/api/dashboard")
@login_required
def api_dashboard():
    """Get dashboard stats"""
    config = load_config()
    log_entries = parse_bot_log()
    
    otp_count = sum(1 for e in log_entries if e["type"] == "otp")
    error_count = sum(1 for e in log_entries if e["type"] == "error")
    
    # Sinkronisasi status dengan bot.py real-time
    shared = get_shared_status()
    if shared:
        bot_status["running"] = shared.get("bot_running", True)
        if "pid" in shared:
            bot_status["pid"] = shared["pid"]
        ivasms_status["connected"] = shared.get("ivasms_connected", False)
        ivasms_status["last_check"] = shared.get("last_update")
    else:
        check_bot_running()
        if not ivasms_status.get("last_check"):
            try:
                import importlib, config
                importlib.reload(config)
                from ivasms_scraper import IVASMSClient
                cl = IVASMSClient(config.COOKIES, config.IVASMS_URL)
                ivasms_status["connected"] = cl.check_connection()
                ivasms_status["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                pass
    
    # Ambil metrik revenue & breakdown dari shared status
    total_revenue = 0.0
    country_counts = {}
    platform_counts = {}
    hourly_counts = {}
    if shared:
        total_revenue = shared.get("total_revenue", round(otp_count * 0.05, 2))
        country_counts = shared.get("country_counts", {})
        platform_counts = shared.get("platform_counts", {})
        hourly_counts = shared.get("hourly_counts", {})
    else:
        total_revenue = round(otp_count * 0.05, 2)

    return jsonify({
        "stats": {
            "otp_received": otp_count,
            "errors": error_count,
            "bot_running": bot_status["running"],
            "ivasms_connected": ivasms_status.get("connected", False),
            "augestel_connected": shared.get("augestel_connected", True) if shared else True,
            "poll_interval": config.get("POLL_INTERVAL", "10"),
            "bot_name": config.get("BOT_NAME", "OTP_BOT"),
            "total_revenue": total_revenue,
            "country_counts": country_counts,
            "platform_counts": platform_counts,
            "hourly_counts": hourly_counts,
        },
        "recent_logs": log_entries[-10:],
        "bot_status": bot_status,
        "ivasms_status": ivasms_status,
    })


@app.route("/api/sms-log")
@login_required
def api_sms_log():
    """Get SMS log entries"""
    entries = parse_bot_log()
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 25, type=int)
    
    # Reverse for newest first
    entries.reverse()
    
    total = len(entries)
    start = (page - 1) * per_page
    end = start + per_page
    
    return jsonify({
        "entries": entries[start:end],
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": (total + per_page - 1) // per_page,
    })


@app.route("/api/logs/tail")
@login_required
def api_logs_tail():
    """Get tail of bot.log"""
    n = request.args.get("n", 50, type=int)
    lines = get_log_tail(n)
    return jsonify({"lines": lines, "count": len(lines)})


@app.route("/api/bot/start", methods=["POST"])
@login_required
def api_bot_start():
    """Start bot.py"""
    global bot_process, bot_status
    
    if bot_process and bot_process.poll() is None:
        return jsonify({"success": False, "message": "Bot sudah berjalan!"})
    
    try:
        bot_process = subprocess.Popen(
            [sys.executable, "bot.py"],
            cwd=os.path.dirname(__file__),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        bot_status = {
            "running": True,
            "pid": bot_process.pid,
            "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        return jsonify({"success": True, "message": "Bot berhasil dijalankan!", "pid": bot_process.pid})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal menjalankan bot: {e}"})


@app.route("/api/bot/stop", methods=["POST"])
@login_required
def api_bot_stop():
    """Stop bot.py"""
    global bot_process, bot_status
    
    if bot_process and bot_process.poll() is None:
        bot_process.terminate()
        try:
            bot_process.wait(timeout=5)
        except:
            bot_process.kill()
        bot_status = {"running": False, "pid": None, "started_at": None}
        return jsonify({"success": True, "message": "Bot berhasil dihentikan!"})
    
    return jsonify({"success": False, "message": "Bot tidak sedang berjalan."})


@app.route("/api/test-otp", methods=["POST"])
@login_required
def api_test_otp():
    """Kirim test OTP ke grup Telegram dengan format live baru."""
    try:
        from bot import format_otp_message, create_keyboard
        from config import BOT_TOKEN, GROUP_CHAT_ID, FILE_LINK, CHANNEL_LINK
        from telegram import Bot
        from telegram.constants import ParseMode

        data = request.json or {}
        phone = data.get("phone", "263788124006")
        otp = data.get("otp", "884762")
        platform = data.get("platform", "WhatsApp")
        country = data.get("country_code", "ZW")
        flag = data.get("flag", "🇿🇼")

        # Buat dictionary sms simulasi
        test_sms = {
            "flag": flag,
            "country_code": country,
            "platform": platform,
            "phone": phone,
            "otp": otp,
            "message": f"Your {platform} verification code: {otp}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Format pesan & keyboard
        msg_text = format_otp_message(test_sms)
        keyboard = create_keyboard(test_sms, FILE_LINK, CHANNEL_LINK)

        # Kirim secara asynchronous
        async def send_msg():
            bot = Bot(token=BOT_TOKEN)
            res = await bot.send_message(
                chat_id=GROUP_CHAT_ID,
                text=msg_text,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard,
            )
            return res.message_id

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        msg_id = loop.run_until_complete(send_msg())
        loop.close()

        # Log ke bot.log agar live log dan dashboard langsung mendeteksi
        log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ 📤 [TEST] Sent OTP: {country} | {platform} | {otp}\n"
        log_path = os.path.join(os.path.dirname(__file__), "bot.log")
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception:
            pass

        return jsonify({
            "success": True,
            "message": f"Test OTP ({otp}) berhasil dikirim ke grup Telegram! (Message ID: {msg_id})",
            "message_id": msg_id,
            "preview": msg_text,
        })
    except Exception as e:
        logger.error(f"Error sending test OTP: {e}")
        return jsonify({"success": False, "message": f"Gagal kirim test OTP: {str(e)}"})


@app.route("/api/bot/status")
@login_required
def api_bot_status():
    """Get bot status and individual account statuses"""
    shared = get_shared_status()
    if shared:
        bot_status["running"] = shared.get("bot_running", True)
        if "pid" in shared:
            bot_status["pid"] = shared["pid"]
    else:
        check_bot_running()

    acc_status = ivasms_status.get("accounts")
    if not acc_status and shared:
        acc_status = shared.get("accounts_status")

    # Pastikan email terisi dari ivasms_accounts.json
    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts_db = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts_db = json.load(f)
        except Exception:
            pass

    merged_status = []
    if acc_status:
        for item in acc_status:
            idx = item.get("index", 1)
            email = item.get("email")
            if not email and 1 <= idx <= len(accounts_db):
                email = accounts_db[idx - 1].get("email", "")
            merged_status.append({
                **item,
                "email": email or f"Akun #{idx}"
            })
    elif accounts_db:
        for idx, a in enumerate(accounts_db, start=1):
            merged_status.append({
                "index": idx,
                "email": a.get("email", ""),
                "connected": True,
                "last_check": "Status Terpantau (Aktif)"
            })

    res = dict(bot_status)
    res["ivasms_status"] = ivasms_status
    res["accounts_status"] = merged_status
    return jsonify(res)


@app.route("/api/ivasms/check", methods=["POST"])
@login_required
def api_ivasms_check():
    """Check IVASMS connection (all or specific account)"""
    try:
        data = request.json or {}
        target_idx = data.get("index")
        if target_idx is not None:
            try:
                target_idx = int(target_idx)
            except Exception:
                target_idx = None

        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(check_ivasms_connection(target_index=target_idx))
        loop.close()
        return jsonify({"success": True, "status": result})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/auto-add/start", methods=["POST"])
@login_required
def api_auto_add_start():
    """Start auto-add numbers"""
    global auto_add_state
    
    if auto_add_state["running"]:
        return jsonify({"success": False, "message": "Auto-add sudah berjalan!"})
    
    data = request.json or {}
    range_name = data.get("range_name", "")
    max_add = data.get("max_add", 0)
    delay = data.get("delay", 60)
    raw_acc = str(data.get("account_index", "1")).strip().lower()
    workers = int(data.get("workers", 1) or 1)
    workers = max(1, min(workers, 36))  # Batasi 1 - 36 workers
    
    if not range_name:
        return jsonify({"success": False, "message": "Range name harus diisi!"})

    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts_db = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts_db = json.load(f)
        except Exception:
            pass

    if raw_acc == "all":
        account_arg = "all"
        account_email = f"Semua Akun ({len(accounts_db)} Akun Terdaftar)"
    else:
        try:
            acc_num = int(raw_acc)
        except Exception:
            acc_num = 1
        account_arg = str(acc_num)
        account_email = f"Akun #{acc_num}"
        if 1 <= acc_num <= len(accounts_db):
            account_email = accounts_db[acc_num - 1].get("email", account_email)
    
    try:
        proc = subprocess.Popen(
            [sys.executable, "auto_add_numbers.py", range_name, str(max_add), str(delay), account_arg, str(workers)],
            cwd=os.path.dirname(__file__),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        
        auto_add_state = {
            "running": True,
            "account_index": account_arg,
            "account_email": account_email,
            "workers": workers,
            "range_name": range_name,
            "max_add": max_add,
            "delay": delay,
            "added": 0,
            "failed": 0,
            "skipped": 0,
            "total_found": 0,
            "current_action": 0,
            "last_message": f"Memulai {workers} worker untuk {account_email}...",
            "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "process": proc,
        }
        
        # Monitor in background thread
        def monitor_auto_add():
            global auto_add_state
            try:
                for line in iter(proc.stdout.readline, b''):
                    decoded = line.decode("utf-8", errors="replace").strip()
                    if decoded:
                        auto_add_state["last_message"] = decoded
                        
                        # Parse stats
                        if "Added=" in decoded:
                            m = re.search(r"Added=(\d+).*Failed=(\d+).*Skipped=(\d+)", decoded)
                            if m:
                                auto_add_state["added"] = int(m.group(1))
                                auto_add_state["failed"] = int(m.group(2))
                                auto_add_state["skipped"] = int(m.group(3))
                        
                        if "Action #" in decoded:
                            m = re.search(r"Action #(\d+)", decoded)
                            if m:
                                auto_add_state["current_action"] = int(m.group(1))
                        
                        if "total records" in decoded:
                            m = re.search(r"(\d+) total records", decoded)
                            if m:
                                auto_add_state["total_found"] = int(m.group(1))
                
                proc.wait()
            except:
                pass
            finally:
                auto_add_state["running"] = False
                auto_add_state["process"] = None
        
        thread = threading.Thread(target=monitor_auto_add, daemon=True)
        thread.start()
        
        return jsonify({"success": True, "message": f"Auto-add dimulai untuk '{range_name}'!"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal: {e}"})


@app.route("/api/auto-add/stop", methods=["POST"])
@login_required
def api_auto_add_stop():
    """Stop auto-add"""
    global auto_add_state
    
    proc = auto_add_state.get("process")
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except:
            proc.kill()
    
    auto_add_state["running"] = False
    auto_add_state["process"] = None
    return jsonify({"success": True, "message": "Auto-add dihentikan."})


@app.route("/api/auto-add/status")
@login_required
def api_auto_add_status():
    """Get auto-add status"""
    safe_state = {k: v for k, v in auto_add_state.items() if k != "process"}
    return jsonify(safe_state)


@app.route("/api/config", methods=["GET"])
@login_required
def api_config_get():
    """Get current config"""
    config = load_config()
    # Mask sensitive data
    if "BOT_TOKEN" in config:
        token = config["BOT_TOKEN"]
        config["BOT_TOKEN_MASKED"] = token[:10] + "..." + token[-5:] if len(token) > 15 else token
    if "IVASMS_PASSWORD" in config:
        config["IVASMS_PASSWORD_MASKED"] = "••••••••"
    return jsonify(config)


@app.route("/api/config", methods=["POST"])
@login_required
def api_config_save():
    """Save config changes"""
    data = request.json
    if save_config(data):
        return jsonify({"success": True, "message": "Konfigurasi berhasil disimpan!"})
    return jsonify({"success": False, "message": "Gagal menyimpan konfigurasi."})


@app.route("/api/accounts", methods=["GET"])
@login_required
def api_accounts_get():
    """Get list of all IVASMS accounts"""
    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        # Fallback from config
        cfg = load_config()
        if cfg.get("IVASMS_EMAIL") and cfg.get("IVASMS_PASSWORD"):
            accounts.append({"email": cfg["IVASMS_EMAIL"], "password": cfg["IVASMS_PASSWORD"]})
        if cfg.get("IVASMS_EMAIL_2") and cfg.get("IVASMS_PASSWORD_2"):
            accounts.append({"email": cfg["IVASMS_EMAIL_2"], "password": cfg["IVASMS_PASSWORD_2"]})

    # Return accounts list
    return jsonify({"success": True, "accounts": accounts})


@app.route("/api/accounts", methods=["POST"])
@login_required
def api_accounts_save():
    """Add or update an IVASMS account"""
    data = request.json or {}
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()
    index = data.get("index")  # 0-indexed if editing, None if adding

    if not email or not password:
        return jsonify({"success": False, "message": "Email dan Password harus diisi!"})

    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if index is not None and isinstance(index, int) and 0 <= index < len(accounts):
        accounts[index] = {"email": email, "password": password}
    else:
        # Check if email exists
        found = False
        for i, a in enumerate(accounts):
            if a.get("email", "").lower() == email.lower():
                accounts[i] = {"email": email, "password": password}
                found = True
                break
        if not found:
            accounts.append({"email": email, "password": password})

    try:
        with open(acc_file, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=2)

        # Sync back first 2 accounts to config.py for backwards compatibility
        sync_cfg = {}
        if len(accounts) >= 1:
            sync_cfg["IVASMS_EMAIL"] = accounts[0]["email"]
            sync_cfg["IVASMS_PASSWORD"] = accounts[0]["password"]
        if len(accounts) >= 2:
            sync_cfg["IVASMS_EMAIL_2"] = accounts[1]["email"]
            sync_cfg["IVASMS_PASSWORD_2"] = accounts[1]["password"]
        if sync_cfg:
            save_config(sync_cfg)

        return jsonify({"success": True, "message": f"Akun {email} berhasil disimpan!", "accounts": accounts})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal menyimpan: {e}"})


@app.route("/api/accounts/delete", methods=["POST"])
@login_required
def api_accounts_delete():
    """Delete an IVASMS account by index or email"""
    data = request.json or {}
    index = data.get("index")
    email = data.get("email", "").strip()

    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    deleted = False
    if index is not None and isinstance(index, int) and 0 <= index < len(accounts):
        accounts.pop(index)
        deleted = True
    elif email:
        accounts = [a for a in accounts if a.get("email", "").lower() != email.lower()]
        deleted = True

    if deleted:
        try:
            with open(acc_file, "w", encoding="utf-8") as f:
                json.dump(accounts, f, indent=2)

            # Sync to config.py
            sync_cfg = {
                "IVASMS_EMAIL": accounts[0]["email"] if len(accounts) >= 1 else "",
                "IVASMS_PASSWORD": accounts[0]["password"] if len(accounts) >= 1 else "",
                "IVASMS_EMAIL_2": accounts[1]["email"] if len(accounts) >= 2 else "",
                "IVASMS_PASSWORD_2": accounts[1]["password"] if len(accounts) >= 2 else "",
            }
            save_config(sync_cfg)

            return jsonify({"success": True, "message": "Akun berhasil dihapus!", "accounts": accounts})
        except Exception as e:
            return jsonify({"success": False, "message": f"Gagal menyimpan: {e}"})

    return jsonify({"success": False, "message": "Akun tidak ditemukan."})


# ────────────────────────────────────────────
#  ROUTES - AKUN AUGESTEL (CRUD)
# ────────────────────────────────────────────

@app.route("/api/augestel/accounts", methods=["GET"])
@login_required
def api_augestel_accounts_get():
    """Get list of all Augestel accounts"""
    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        cfg = load_config()
        if cfg.get("AUGESTEL_EMAIL"):
            accounts.append({
                "email": cfg.get("AUGESTEL_EMAIL", "saputradimas0878@gmail.com"),
                "password": "••••••••",
                "api_key": cfg.get("AUGESTEL_API_KEY", "")
            })

    return jsonify({"success": True, "accounts": accounts})


@app.route("/api/augestel/accounts", methods=["POST"])
@login_required
def api_augestel_accounts_save():
    """Add or update an Augestel account"""
    data = request.json or {}
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()
    api_key = data.get("api_key", "").strip()
    index = data.get("index")

    if not email:
        return jsonify({"success": False, "message": "Email harus diisi!"})

    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    cfg = load_config()
    new_entry = {
        "email": email,
        "password": password,
        "api_key": api_key or cfg.get("AUGESTEL_API_KEY", "")
    }

    if index is not None and isinstance(index, int) and 0 <= index < len(accounts):
        accounts[index] = new_entry
    else:
        found = False
        for i, a in enumerate(accounts):
            if a.get("email", "").lower() == email.lower():
                accounts[i] = new_entry
                found = True
                break
        if not found:
            accounts.append(new_entry)

    try:
        with open(acc_file, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=2)

        # Update primary account to config.py if it's the first account
        if len(accounts) >= 1:
            save_config({
                "AUGESTEL_EMAIL": accounts[0]["email"],
                "AUGESTEL_API_KEY": accounts[0].get("api_key", "")
            })

        return jsonify({"success": True, "message": f"Akun Augestel {email} berhasil disimpan!", "accounts": accounts})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal menyimpan akun Augestel: {e}"})


@app.route("/api/augestel/accounts/delete", methods=["POST"])
@login_required
def api_augestel_accounts_delete():
    """Delete an Augestel account by index or email"""
    data = request.json or {}
    index = data.get("index")
    email = data.get("email", "").strip()

    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    deleted = False
    if index is not None and isinstance(index, int) and 0 <= index < len(accounts):
        accounts.pop(index)
        deleted = True
    elif email:
        accounts = [a for a in accounts if a.get("email", "").lower() != email.lower()]
        deleted = True

    if deleted:
        try:
            with open(acc_file, "w", encoding="utf-8") as f:
                json.dump(accounts, f, indent=2)
            return jsonify({"success": True, "message": "Akun Augestel berhasil dihapus!", "accounts": accounts})
        except Exception as e:
            return jsonify({"success": False, "message": f"Gagal menyimpan: {e}"})

    return jsonify({"success": False, "message": "Akun Augestel tidak ditemukan."})


@app.route("/api/augestel/check", methods=["POST"])
@login_required
def api_augestel_check():
    """Check Augestel API connection"""
    try:
        data = request.json or {}
        cfg = load_config()
        api_key = data.get("api_key") or cfg.get("AUGESTEL_API_KEY", "")
        
        # Also check augestel_accounts.json if empty
        if not api_key:
            acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
            if os.path.exists(acc_file):
                with open(acc_file, "r", encoding="utf-8") as f:
                    accs = json.load(f)
                    if accs and accs[0].get("api_key"):
                        api_key = accs[0]["api_key"]

        from augestel_client import AugestelClient
        client = AugestelClient(api_key=api_key)
        conn = client.check_connection()
        stats = client.get_statistics() if conn else {}
        balance = stats.get("data", {}).get("balance", "0.00") if isinstance(stats, dict) else "0.00"

        # Also get number count from cache if exists
        total_nums = 500
        cache_file = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cdata = json.load(f)
                    total_nums = len(cdata.get("numbers", [])) or total_nums
            except Exception:
                pass

        return jsonify({
            "success": True,
            "status": {
                "connected": conn,
                "balance": balance,
                "total_numbers": total_nums,
                "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        })
    except Exception as e:
        return jsonify({"success": False, "status": {"connected": False}, "message": str(e)})



@app.route("/api/numbers/delete-all", methods=["POST"])
@login_required
def api_numbers_delete_all():
    """Delete / Return all numbers for selected account (IVASMS or Augestel)"""
    data = request.json or {}
    raw_acc = str(data.get("account_index", "1")).strip().lower()

    try:
        from numbers_service import delete_all_account_numbers
        res = asyncio.run(delete_all_account_numbers(account_index=raw_acc))
        return jsonify(res)
    except Exception as e:
        logger.error(f"Error in api_numbers_delete_all: {e}")
        return jsonify({"success": False, "message": f"Gagal menghapus semua nomor: {e}"})


@app.route("/api/accounts/bulk-import", methods=["POST"])
@login_required
def api_accounts_bulk_import():
    """Bulk import IVASMS accounts in format email:password per line"""
    data = request.json or {}
    raw_text = data.get("text", "").strip()
    if not raw_text:
        return jsonify({"success": False, "message": "Teks akun tidak boleh kosong!"})

    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    existing_emails = {a.get("email", "").lower(): i for i, a in enumerate(accounts)}
    imported_count = 0
    updated_count = 0
    lines = raw_text.splitlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = re.split(r"[:|;\t,]", line, maxsplit=1)
        if len(parts) < 2:
            continue
        email = parts[0].strip()
        password = parts[1].strip()
        if not email or not password or "@" not in email:
            continue

        em_lower = email.lower()
        if em_lower in existing_emails:
            idx = existing_emails[em_lower]
            accounts[idx]["password"] = password
            updated_count += 1
        else:
            accounts.append({"email": email, "password": password})
            existing_emails[em_lower] = len(accounts) - 1
            imported_count += 1

    try:
        with open(acc_file, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=2)

        sync_cfg = {}
        if len(accounts) >= 1:
            sync_cfg["IVASMS_EMAIL"] = accounts[0]["email"]
            sync_cfg["IVASMS_PASSWORD"] = accounts[0]["password"]
        if len(accounts) >= 2:
            sync_cfg["IVASMS_EMAIL_2"] = accounts[1]["email"]
            sync_cfg["IVASMS_PASSWORD_2"] = accounts[1]["password"]
        if sync_cfg:
            save_config(sync_cfg)

        return jsonify({
            "success": True,
            "message": f"Berhasil memproses! {imported_count} akun baru ditambahkan, {updated_count} akun diperbarui.",
            "imported": imported_count,
            "updated": updated_count,
            "total": len(accounts),
            "accounts": accounts
        })
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal menyimpan: {e}"})


@app.route("/api/numbers", methods=["GET"])
@login_required
def api_numbers_list():
    """Fetch numbers list and count for selected account or all accounts"""
    raw_idx = str(request.args.get("account_index", "1")).strip().lower()
    force_refresh = request.args.get("refresh", "0") in ["1", "true", "True"]
    if raw_idx == "all":
        acc_arg = "all"
    elif raw_idx == "augestel":
        acc_arg = "augestel"
    else:
        acc_arg = int(raw_idx) if raw_idx.isdigit() else 1

    try:
        from numbers_service import fetch_account_numbers
        result = asyncio.run(fetch_account_numbers(account_index=acc_arg, force_refresh=force_refresh))
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in api_numbers_list: {e}")
        return jsonify({"success": False, "message": f"Gagal mengambil nomor: {e}"})


@app.route("/api/numbers/export/excel", methods=["GET"])
@login_required
def api_numbers_export_excel():
    """Export numbers to Excel .xlsx format for selected account or all accounts"""
    raw_idx = str(request.args.get("account_index", "1")).strip().lower()
    if raw_idx == "all":
        acc_arg = "all"
    elif raw_idx == "augestel":
        acc_arg = "augestel"
    else:
        acc_arg = int(raw_idx) if raw_idx.isdigit() else 1

    try:
        from numbers_service import fetch_account_numbers, generate_numbers_excel
        res = asyncio.run(fetch_account_numbers(account_index=acc_arg, force_refresh=False))
        if not res.get("success"):
            return jsonify({"success": False, "message": res.get("message", "Gagal mengambil data")}), 400

        numbers_list = res.get("numbers", [])
        email = res.get("email", "all" if acc_arg == "all" else f"acc{acc_arg}")
        excel_buf = generate_numbers_excel(numbers_list, email=email)

        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        if acc_arg == "all":
            filename = f"ivasms_numbers_ALL_ACCOUNTS_{date_str}.xlsx"
        elif acc_arg == "augestel":
            filename = f"augestel_numbers_{date_str}.xlsx"
        else:
            clean_email_tag = re.sub(r'[^a-zA-Z0-9]', '_', email.split('@')[0]) if '@' in email else f"acc_{acc_arg}"
            filename = f"ivasms_numbers_{clean_email_tag}_{date_str}.xlsx"

        return send_file(
            excel_buf,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        logger.error(f"Error in api_numbers_export_excel: {e}")
        return jsonify({"success": False, "message": f"Gagal export Excel: {e}"}), 500


@app.route("/api/numbers/export/txt", methods=["GET"])
@login_required
def api_numbers_export_txt():
    """Export numbers to plain text (nomor saja per baris) for selected account or all accounts"""
    raw_idx = str(request.args.get("account_index", "1")).strip().lower()
    if raw_idx == "all":
        acc_arg = "all"
    elif raw_idx == "augestel":
        acc_arg = "augestel"
    else:
        acc_arg = int(raw_idx) if raw_idx.isdigit() else 1

    try:
        from numbers_service import fetch_account_numbers, generate_numbers_txt
        res = asyncio.run(fetch_account_numbers(account_index=acc_arg, force_refresh=False))
        if not res.get("success"):
            return jsonify({"success": False, "message": res.get("message", "Gagal mengambil data")}), 400

        numbers_list = res.get("numbers", [])
        email = res.get("email", "all" if acc_arg == "all" else f"acc{acc_arg}")
        txt_content = generate_numbers_txt(numbers_list)

        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        if acc_arg == "all":
            filename = f"ivasms_numbers_ALL_ACCOUNTS_{date_str}.txt"
        elif acc_arg == "augestel":
            filename = f"augestel_numbers_{date_str}.txt"
        else:
            clean_email_tag = re.sub(r'[^a-zA-Z0-9]', '_', email.split('@')[0]) if '@' in email else f"acc_{acc_arg}"
            filename = f"ivasms_numbers_{clean_email_tag}_{date_str}.txt"

        return Response(
            txt_content,
            mimetype="text/plain; charset=utf-8",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        logger.error(f"Error in api_numbers_export_txt: {e}")
        return jsonify({"success": False, "message": f"Gagal export TXT: {e}"}), 500


# ────────────────────────────────────────────
#  RUN
# ────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  🌐 OTP IVA SMS - Admin Dashboard")
    print("  📍 http://localhost:5000")
    print(f"  👤 Login: {ADMIN_USER} / {ADMIN_PASS}")
    print("=" * 55)
    app.run(host="0.0.0.0", port=5000, debug=True)
