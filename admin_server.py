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
import hashlib
import hmac
import json
import logging
import re
import subprocess
import threading
import time
from datetime import datetime, timedelta
from functools import wraps

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from flask import Flask, render_template, jsonify, request, redirect, url_for, session, send_file, Response

from augestel_earnings_service import (
    load_augestel_earnings,
    load_api_earnings,
    load_webhook_earnings,
    save_augestel_earnings,
    trigger_background_api_sync,
    get_sync_state,
    record_incremental_webhook_sms,
    record_webhook_daily_summary,
    USD_TO_IDR_RATE,
)

# ────────────────────────────────────────────
#  APP SETUP
# ────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = "otp-iva-sms-admin-secret-2026"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)
app.config["TEMPLATES_AUTO_RELOAD"] = True

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

# Auto-add Augestel state
auto_add_augestel_state = {
    "running": False,
    "account_index": "1",
    "account_email": "",
    "workers": 2,
    "range_name": "",
    "number_prefix": "",
    "max_add": 0,
    "delay": 15,
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
    "accounts": [],
}

# Augestel connection state
augestel_status = {
    "connected": False,
    "last_check": None,
    "accounts": [],
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
        # Allow internal localhost calls from local CLI or background services
        if request.remote_addr in ("127.0.0.1", "::1", "localhost") and request.headers.get("X-Internal-Token") == "bot-internal-secret":
            return f(*args, **kwargs)
        if not session.get("logged_in"):
            if request.path.startswith("/api/"):
                return jsonify({
                    "success": False,
                    "error": "Unauthorized",
                    "message": "Sesi login Anda telah berakhir. Silakan login kembali.",
                    "need_login": True
                }), 401
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function



# ────────────────────────────────────────────
#  HELPER FUNCTIONS
# ────────────────────────────────────────────

def load_config():
    """Load current config from config.py"""
    config = {}
    config_path = os.path.join(BASE_DIR, "config.py")
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
            "OWNER_CHAT_ID": r'OWNER_CHAT_ID\s*=\s*"([^"]*)"',
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
    config_path = os.path.join(BASE_DIR, "config.py")
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
            "OWNER_CHAT_ID": (r'(OWNER_CHAT_ID\s*=\s*)"[^"]*"', r'\1"{}"'),
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
    log_path = os.path.join(BASE_DIR, "bot.log")
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
    log_path = os.path.join(BASE_DIR, "bot.log")
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
    status_file = os.path.join(BASE_DIR, "status.json")
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
    """Stub kompatibilitas untuk cek IVASMS (Platform dinonaktifkan)."""
    global ivasms_status
    ivasms_status = {
        "connected": False,
        "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accounts": []
    }
    return ivasms_status


def check_augestel_browser_cookie(account_idx: int) -> dict:
    """
    Memeriksa status browser profile & cookies untuk akun Augestel.
    Memeriksa file SQLite Cookies di browser_profile_augestel_{account_idx}.
    """
    import shutil
    import sqlite3
    import tempfile
    import time

    user_data_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{account_idx}")
    if not os.path.exists(user_data_dir):
        return {
            "profile_exists": False,
            "cookie_connected": False,
            "status_text": "Profil Browser Belum Dibuat",
            "has_remember": False,
            "has_session": False,
            "cookie_count": 0,
        }

    db_path = os.path.join(user_data_dir, "Default", "Network", "Cookies")
    if not os.path.exists(db_path):
        return {
            "profile_exists": True,
            "cookie_connected": False,
            "status_text": "Belum Ada Sesi (Silakan Login)",
            "has_remember": False,
            "has_session": False,
            "cookie_count": 0,
        }

    # Chromium epoch time in microseconds (1601-01-01)
    now_chrome_time = int((time.time() + 11644473600) * 1000000)
    tmp_path = None
    try:
        tmp_dir = tempfile.gettempdir()
        tmp_path = os.path.join(tmp_dir, f"chk_aug_cookie_{account_idx}_{time.time()}.sqlite")
        shutil.copyfile(db_path, tmp_path)

        conn = sqlite3.connect(tmp_path)
        cur = conn.cursor()
        cur.execute("SELECT name, expires_utc FROM cookies WHERE host_key LIKE '%augestel.com%'")
        rows = cur.fetchall()
        conn.close()

        has_remember = False
        has_session = False

        for name, expires_utc in rows:
            if "remember_client" in name:
                if expires_utc == 0 or expires_utc > now_chrome_time:
                    has_remember = True
            elif "augestel-session" in name:
                if expires_utc == 0 or expires_utc > now_chrome_time:
                    has_session = True

        cookie_connected = has_remember or has_session
        if has_remember:
            status_text = "Sesi Aktif (Remember Me)"
        elif has_session:
            status_text = "Sesi Aktif (Session Cookie)"
        elif len(rows) > 0:
            status_text = "Sesi Kadaluarsa (Expired)"
        else:
            status_text = "Belum Ada Cookie Login"

        return {
            "profile_exists": True,
            "cookie_connected": cookie_connected,
            "status_text": status_text,
            "has_remember": has_remember,
            "has_session": has_session,
            "cookie_count": len(rows),
        }
    except Exception as e:
        return {
            "profile_exists": True,
            "cookie_connected": False,
            "status_text": f"Error Cookie: {e}",
            "has_remember": False,
            "has_session": False,
            "cookie_count": 0,
        }
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


def check_augestel_multi_connection(target_index: int = None):
    """Check Augestel connection for each registered account, checking BOTH REST API & Browser Profile Cookies"""
    global augestel_status
    acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        cfg = load_config()
        if cfg.get("AUGESTEL_EMAIL") and cfg.get("AUGESTEL_API_KEY"):
            accounts.append({"email": cfg["AUGESTEL_EMAIL"], "api_key": cfg["AUGESTEL_API_KEY"]})

    pool_dict = {}
    try:
        from augestel_browser_pool import get_browser_pool
        pool_inst = get_browser_pool()
        if pool_inst and pool_inst.is_running:
            if target_index is not None:
                try:
                    pool_inst.check_account_sync(target_index)
                except Exception:
                    pass
            pool_dict = pool_inst.get_status_dict()
    except Exception:
        pass

    existing_results = {r.get("index"): r for r in augestel_status.get("accounts", []) if isinstance(r, dict)}
    results = []
    any_connected = False
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    from augestel_client import AugestelClient

    for idx, acc in enumerate(accounts, start=1):
        email = acc.get("email", "")
        api_key = acc.get("api_key", "")
        if not email:
            continue

        # If checking a single account, preserve others
        if target_index is not None and idx != target_index:
            prev = existing_results.get(idx, {
                "index": idx,
                "email": email,
                "api_connected": bool(api_key),
                "cookie_connected": False,
                "connected": False,
                "balance": acc.get("balance", "0.00"),
                "last_check": "-"
            })
            if prev.get("connected") or prev.get("api_connected"):
                any_connected = True
            results.append(prev)
            continue

        api_connected = False
        balance = "0.00"

        # 1. Cek REST API Key
        if api_key:
            try:
                rem_cd = AugestelClient.get_remaining_cooldown()
                if rem_cd > 0:
                    api_connected = True
                    balance = acc.get("balance", "0.00")
                else:
                    client = AugestelClient(api_key=api_key, email=email)
                    api_connected = client.check_connection()
                    if api_connected and AugestelClient.get_remaining_cooldown() == 0:
                        stats = client.get_statistics()
                        balance = stats.get("data", {}).get("balance", "0.00") if isinstance(stats, dict) else "0.00"
            except Exception as e:
                logger.error(f"Error checking Augestel acc {idx}: {e}")
                api_connected = False

        # 2. Cek Browser Profile & Keep-Alive Browser Pool di RAM
        p_item = pool_dict.get(idx) or pool_dict.get(str(idx)) or {}
        pool_logged_in = p_item.get("logged_in", False)
        pool_message = p_item.get("message", "")

        if pool_logged_in:
            cookie_connected = True
            has_remember = True
            has_session = True
            cookie_status = "Standby di RAM (24/7)"
            is_pool_active = True
        elif pool_inst and pool_inst.is_running:
            # Pool is managing the browser, do NOT touch SQLite Cookies file directly
            cookie_connected = False
            has_remember = False
            has_session = False
            cookie_status = pool_message if pool_message else "Browser Standby / Belum Login"
            is_pool_active = False
        else:
            cookie_info = check_augestel_browser_cookie(idx)
            cookie_connected = cookie_info.get("cookie_connected", False)
            has_remember = cookie_info.get("has_remember", False)
            has_session = cookie_info.get("has_session", False)
            cookie_status = pool_message if pool_message else cookie_info.get("status_text", "-")
            is_pool_active = False

        overall_connected = api_connected and cookie_connected
        if overall_connected or api_connected or cookie_connected:
            any_connected = True

        results.append({
            "index": idx,
            "email": email,
            "api_connected": api_connected,
            "cookie_connected": cookie_connected,
            "cookie_status": cookie_status,
            "has_remember": has_remember,
            "has_session": has_session,
            "cookie_count": 3 if pool_logged_in else 0,
            "is_pool_active": is_pool_active,
            "connected": overall_connected,
            "balance": balance,
            "last_check": now_str
        })

    augestel_status["connected"] = any_connected
    augestel_status["last_check"] = now_str
    augestel_status["accounts"] = results

    # Sync to status.json
    try:
        status_file = os.path.join(BASE_DIR, "status.json")
        s_data = {}
        if os.path.exists(status_file):
            with open(status_file, "r", encoding="utf-8") as f:
                s_data = json.load(f)
        s_data["augestel_connected"] = any_connected
        s_data["augestel_accounts_status"] = results
        with open(status_file, "w", encoding="utf-8") as f:
            json.dump(s_data, f, indent=2)
    except Exception:
        pass

    return augestel_status


# ────────────────────────────────────────────
#  ROUTES - AUTH
# ────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == ADMIN_USER and password == ADMIN_PASS:
            session.permanent = True
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
@app.route("/augestel-accounts")
@login_required
def accounts_page():
    return render_template("admin.html", page="accounts-augestel")


@app.route("/auto-add")
@app.route("/auto-add-augestel")
@login_required
def auto_add_page():
    return render_template("admin.html", page="auto-add-augestel")


@app.route("/numbers")
@app.route("/numbers-augestel")
@login_required
def numbers_page():
    return render_template("admin.html", page="numbers-augestel")


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
            "ivasms_connected": False,
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
        "ivasms_status": {"connected": False, "accounts": []},
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
            cwd=BASE_DIR,
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
        log_path = os.path.join(BASE_DIR, "bot.log")
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


# ────────────────────────────────────────────
#  AUGESTEL WEBHOOK RECEIVER (NO RATE LIMIT)
# ────────────────────────────────────────────
#  AUGESTEL EARNINGS & REVENUE ENGINE (FITUR 2)
# ────────────────────────────────────────────
EARNINGS_FILE = os.path.join(BASE_DIR, "augestel_earnings.json")

# ────────────────────────────────────────────
#  ULTRA-FAST TELEGRAM ENGINE & RAM PHONE MAP
# ────────────────────────────────────────────
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor

# Pre-warmed persistent HTTPS session with Keep-Alive to api.telegram.org
_fast_tg_session = requests.Session()
_tg_retries = Retry(
    total=3,
    backoff_factor=0.2,
    status_forcelist=[500, 502, 503, 504],
    raise_on_status=False
)
_tg_adapter = HTTPAdapter(pool_connections=25, pool_maxsize=50, max_retries=_tg_retries)
_fast_tg_session.mount("https://", _tg_adapter)

# Pre-allocated ThreadPool for Webhook (0 thread startup overhead)
_webhook_executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="FastWebhook")

def _keep_telegram_session_alive():
    """Background keeper: menjaga koneksi TCP & TLS 1.3 ke api.telegram.org selalu standby panas 24/7."""
    from config import BOT_TOKEN
    while True:
        try:
            if BOT_TOKEN:
                _fast_tg_session.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe", timeout=5)
        except Exception:
            pass
        time.sleep(35)

threading.Thread(target=_keep_telegram_session_alive, daemon=True).start()

# In-Memory RAM Map: nomor telepon -> (account_idx, account_email)
_phone_account_map = {}
_phone_map_lock = threading.Lock()
_phone_map_last_refresh = 0

def refresh_phone_account_map(force=False):
    """Memetakan seluruh nomor telepon dari 32 akun ke RAM agar lookup 0.0001ms (tanpa baca disk)."""
    global _phone_account_map, _phone_map_last_refresh
    now = time.time()
    if not force and (now - _phone_map_last_refresh < 300) and _phone_account_map:
        return

    with _phone_map_lock:
        try:
            acc_emails = {}
            acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
            if os.path.exists(acc_file):
                with open(acc_file, "r", encoding="utf-8") as af:
                    accs = json.load(af)
                    for i, a in enumerate(accs, 1):
                        acc_emails[i] = a.get("email", f"Akun #{i}")

            new_map = {}
            for idx in range(1, 33):
                c_path = os.path.join(BASE_DIR, f"augestel_numbers_cache_{idx}.json")
                if os.path.exists(c_path):
                    try:
                        with open(c_path, "r", encoding="utf-8") as cf:
                            c_data = json.load(cf)
                            for n in c_data.get("numbers", []):
                                cp = re.sub(r'[\s\+\-]', '', str(n))
                                if cp:
                                    new_map[cp] = (idx, acc_emails.get(idx, f"Akun #{idx}"))
                    except Exception:
                        pass
            _phone_account_map = new_map
            _phone_map_last_refresh = now
            logger.info(f"⚡ [Turbo Engine] Pre-cached {len(new_map)} nomor Augestel di RAM (Lookup akun instant 0ms).")
        except Exception as e:
            logger.error(f"Error refreshing phone account map: {e}")

# Pre-cache saat server start
threading.Thread(target=refresh_phone_account_map, args=(True,), daemon=True).start()

def find_account_by_phone(phone_number: str) -> tuple:
    """Lookup akun pemilik nomor telepon dari RAM dalam 0.0001ms."""
    clean_p = re.sub(r'[\s\+\-]', '', str(phone_number))
    if not clean_p:
        return 1, "Akun #1"

    found = _phone_account_map.get(clean_p)
    if found:
        return found

    for k, v in _phone_account_map.items():
        if len(k) >= 8 and (clean_p.endswith(k) or k.endswith(clean_p)):
            _phone_account_map[clean_p] = v
            return v

    return 1, "Akun #1"

def record_earnings_sms(account_idx=1, account_email="", rate_val=0.015, country_cc="ZW", country_flag="🇿🇼", platform="WhatsApp", phone=""):
    """Catat pertambahan cuan SMS real-time melalui service analitik API."""
    return record_incremental_webhook_sms(account_idx, account_email, rate_val, country_cc, country_flag, platform, phone)

# ────────────────────────────────────────────
#  AUGESTEL WEBHOOK RECEIVER (NO RATE LIMIT)
# ────────────────────────────────────────────
def get_current_tunnel_url():
    """Mengambil link publik aktif saat ini (Cloudflare Tunnel atau Ngrok)"""
    tf = os.path.join(BASE_DIR, "tunnel_url.txt")
    if os.path.exists(tf):
        try:
            with open(tf, "r", encoding="utf-8") as f:
                u = f.read().strip()
                if u.startswith("http"):
                    return u
        except Exception:
            pass
    return "https://bonnet-grinning-naming.ngrok-free.dev"

augestel_webhook_seen_ids = set()
augestel_webhook_history = []
augestel_webhook_status = {
    "url": "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook",
    "total_received": 0,
    "last_received": None,
    "last_event": None,
    "last_sms": None,
}


@app.route("/api/augestel/webhook", methods=["GET", "POST"])
def augestel_webhook():
    """
    Webhook endpoint untuk menerima event SMS/Numbers secara real-time dari Augestel Switchfy.
    Menghilangkan limit polling 1 menit sepenuhnya (0 API call consumed).
    """
    if request.method == "GET":
        return jsonify({
            "status": "active",
            "service": "Augestel Webhook Receiver",
            "time": datetime.now().isoformat(),
            "total_received": augestel_webhook_status["total_received"],
            "last_received": augestel_webhook_status["last_received"],
        }), 200

    raw_data = request.get_data()
    signature = request.headers.get("X-Augestel-Signature", "")
    event_header = request.headers.get("X-Augestel-Event", "")

    try:
        payload = request.get_json(force=True, silent=True) or {}
    except Exception:
        payload = {}

    event_type = payload.get("event") or event_header or "unknown"
    data = payload.get("data") or {}

    augestel_webhook_status["total_received"] += 1
    augestel_webhook_status["last_received"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    augestel_webhook_status["last_event"] = event_type

    # Fast dispatch: Jalankan di thread pool terdedikasi tanpa latency thread creation
    def dispatch_webhook_event(ev_type, ev_data, full_payload):
        t_start = time.time()
        try:
            if ev_type == "message.received":
                phone = str(ev_data.get("number", "")).strip()
                raw_message = str(ev_data.get("message", "")).strip()
                source_sender = str(ev_data.get("source", "")).strip()
                received_at = str(ev_data.get("received_at", "")).strip()
                rate_val = ev_data.get("rate", 0.0)

                from otp_utils import get_country_from_phone, mask_phone_number, detect_platform, extract_otp
                from bot import format_otp_message, create_keyboard
                from config import BOT_TOKEN, GROUP_CHAT_ID, FILE_LINK, CHANNEL_LINK
                from otp_dedup import is_duplicate_and_claim, get_dedup_key, claim_earnings_once

                phone_cc, phone_flag = get_country_from_phone(phone)
                otp = extract_otp(raw_message)
                platform, p_emoji = detect_platform(source_sender)
                if platform == "SMS":
                    platform, p_emoji = detect_platform(raw_message)

                # 1. Deduplikasi Multi-Proses Super Cepat
                dedup_k = get_dedup_key(phone, otp, raw_message)
                is_duplicate = is_duplicate_and_claim(phone, otp, raw_message, source="Augestel Webhook")
                if is_duplicate:
                    logger.info(f"🛡️ [Augestel Webhook] Duplicate OTP skipped for {phone} (otp={otp})")
                    return

                # 2. Cari akun pemilik nomor secara instan dari RAM (0.001 ms)
                matched_acc_idx, matched_acc_email = find_account_by_phone(phone)

                try:
                    rev_str = f"${float(rate_val):.4f}" if float(rate_val) > 0 else "$0.0120"
                except Exception:
                    rev_str = "$0.0120"

                unique_hash = hashlib.sha256(
                    f"{phone}|{received_at}|{source_sender}|{raw_message}".encode("utf-8")
                ).hexdigest()[:16]
                sms_id = f"aug_{unique_hash}"

                sms_entry = {
                    "id": sms_id,
                    "phone": phone,
                    "phone_masked": mask_phone_number(phone),
                    "sender": source_sender or "Augestel",
                    "message": raw_message,
                    "otp": otp,
                    "platform": platform,
                    "platform_emoji": p_emoji,
                    "country_code": phone_cc,
                    "flag": phone_flag,
                    "timestamp": received_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "revenue": rev_str,
                    "rate": rate_val,
                    "range_name": ev_data.get("range_name", "Augestel IPRN"),
                    "source": f"Augestel ({matched_acc_email})",
                }

                augestel_webhook_status["last_sms"] = sms_entry

                # 3. Format pesan teks & Inline Keyboard
                msg_text = format_otp_message(sms_entry)
                keyboard = create_keyboard(sms_entry, FILE_LINK, CHANNEL_LINK, otp_text=otp)

                # 4. 🚀 PRIORITAS #1 (SUPER NGEBUT): TEMBAK LANGSUNG KE TELEGRAM MENGGUNAKAN PERSISTENT KEEP-ALIVE HTTP
                tg_payload = {
                    "chat_id": GROUP_CHAT_ID,
                    "text": msg_text,
                    "parse_mode": "HTML",
                    "reply_markup": keyboard.to_dict()
                }

                sent_ok = False
                msg_id = None
                for attempt in range(1, 4):
                    try:
                        r = _fast_tg_session.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json=tg_payload,
                            timeout=5.0
                        )
                        if r.status_code == 200:
                            sent_ok = True
                            resp_json = r.json()
                            msg_id = resp_json.get("result", {}).get("message_id")
                            break
                        else:
                            logger.warning(f"⚠️ [Telegram Turbo Push] Attempt #{attempt} status {r.status_code}: {r.text}")
                            time.sleep(0.3)
                    except Exception as tg_err:
                        logger.warning(f"⚠️ [Telegram Turbo Push] Attempt #{attempt} error: {tg_err}")
                        time.sleep(0.3)

                t_tg = (time.time() - t_start) * 1000
                if sent_ok:
                    logger.info(f"⚡ [TURBO NOTIFIKASI] OTP {otp} ({platform}) berhasil terkirim ke Telegram dalam {t_tg:.1f}ms! (msg_id={msg_id})")
                else:
                    logger.error(f"❌ [Telegram Turbo Push] Gagal mengirim OTP {otp} setelah 3 percobaan ({t_tg:.1f}ms)")

                # 5. CATAT PENDAPATAN & LOG KE FILE DI LATAR BELAKANG (ASYNCHRONOUS - 0ms blocking Telegram)
                def save_records_async():
                    try:
                        if claim_earnings_once(dedup_k):
                            record_earnings_sms(
                                account_idx=matched_acc_idx,
                                account_email=matched_acc_email,
                                rate_val=rate_val,
                                country_cc=phone_cc,
                                country_flag=phone_flag,
                                platform=platform,
                                phone=phone
                            )
                        log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ 📤 [Augestel Webhook] Sent OTP: {phone_cc} | {platform} | {otp} ({matched_acc_email})\n"
                        with open(os.path.join(BASE_DIR, "bot.log"), "a", encoding="utf-8") as f:
                            f.write(log_line)
                    except Exception as err_rec:
                        logger.error(f"Error saving earnings records async: {err_rec}")

                _webhook_executor.submit(save_records_async)

            elif ev_type == "earnings.daily":
                daily_usd = float(ev_data.get("earnings", 0.0) or ev_data.get("amount", 0.0) or 0.0)
                daily_sms = int(ev_data.get("sms_count", 0) or 0)
                logger.info(f"💰 [Augestel Webhook] Daily Earnings Summary received: ${daily_usd:.4f} ({daily_sms} SMS)")
                record_webhook_daily_summary(daily_usd, daily_sms)
                log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ 💰 [Augestel Webhook] Daily Earnings Summary: ${daily_usd:.4f} ({daily_sms} SMS)\n"
                log_path = os.path.join(BASE_DIR, "bot.log")
                try:
                    with open(log_path, "a", encoding="utf-8") as f:
                        f.write(log_line)
                except Exception:
                    pass

            elif ev_type in ["number.assigned", "number.removed"]:
                num = ev_data.get("number")
                rng = ev_data.get("range_name")
                log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ ℹ️ [Augestel Webhook] {ev_type}: {num} ({rng})\n"
                log_path = os.path.join(BASE_DIR, "bot.log")
                try:
                    with open(log_path, "a", encoding="utf-8") as f:
                        f.write(log_line)
                except Exception:
                    pass
                # Trigger refresh RAM cache bila ada nomor baru
                refresh_phone_account_map(force=True)

        except Exception as e:
            logger.error(f"❌ Error processing Augestel webhook in background: {e}", exc_info=True)

    _webhook_executor.submit(dispatch_webhook_event, event_type, data, payload)

    augestel_webhook_history.insert(0, {
        "event": event_type,
        "received_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data,
        "signature_present": bool(signature),
    })
    if len(augestel_webhook_history) > 50:
        augestel_webhook_history.pop()

    return jsonify({"success": True, "message": "Event received"}), 200


@app.route("/api/augestel/earnings")
@login_required
def api_augestel_earnings():
    """Mengembalikan data analitik pendapatan Augestel (Mendukung Versi REST API & Versi Webhook)"""
    mode = request.args.get("mode", "api").strip().lower()
    api_data = load_api_earnings()
    webhook_data = load_webhook_earnings()
    sync_status = get_sync_state()

    active_data = webhook_data if mode == "webhook" else api_data

    return jsonify({
        "success": True,
        "mode": mode,
        "data": active_data,
        "api_data": api_data,
        "webhook_data": webhook_data,
        "sync_status": sync_status,
        "exchange_rate": USD_TO_IDR_RATE
    })


@app.route("/api/augestel/earnings/sync", methods=["POST"])
@login_required
def api_augestel_earnings_sync():
    """Memicu sinkronisasi manual ke REST API resmi Augestel untuk seluruh 32 akun"""
    started = trigger_background_api_sync()
    return jsonify({
        "success": True,
        "started": started,
        "message": "Sinkronisasi analitik pendapatan dari API Augestel sedang berjalan di latar belakang..." if started else "Sinkronisasi sedang berlangsung, mohon tunggu sebentar.",
        "is_syncing": True
    })


@app.route("/api/augestel/earnings/sync-status")
@login_required
def api_augestel_earnings_sync_status():
    """Cek progress live sinkronisasi API Augestel"""
    return jsonify({
        "success": True,
        "sync_status": get_sync_state()
    })


@app.route("/api/augestel/webhook/simulate", methods=["POST"])
@login_required
def api_augestel_webhook_simulate():
    """
    Fitur 6: Live SMS Simulator & Webhook Tester
    Mensimulasikan pesan OTP masuk pada akun dan nomor tertentu,
    mengirimkan kartu OTP interaktif ke Telegram, dan mencatat earnings.
    """
    req_data = request.json or {}
    acc_idx = int(req_data.get("account_index", 1) or 1)
    phone = str(req_data.get("phone", "+263788124006")).strip()
    platform = str(req_data.get("platform", "WhatsApp")).strip()
    otp = str(req_data.get("otp", "884762")).strip()
    try:
        rate_val = float(req_data.get("rate", 0.0150) or 0.0150)
    except Exception:
        rate_val = 0.0150
    range_name = str(req_data.get("range_name", "Augestel Test Range")).strip()
    custom_msg = str(req_data.get("message", "")).strip()

    if not custom_msg:
        custom_msg = f"Kode verifikasi {platform} Anda adalah: {otp[:3]}-{otp[3:] if len(otp)>3 else otp}. Jangan bagikan kode ini kepada siapapun."

    from otp_utils import get_country_from_phone, mask_phone_number, detect_platform
    from bot import format_otp_message, create_keyboard
    from config import BOT_TOKEN, GROUP_CHAT_ID, FILE_LINK, CHANNEL_LINK
    from telegram import Bot
    from telegram.constants import ParseMode

    phone_cc, phone_flag = get_country_from_phone(phone)
    _, p_emoji = detect_platform(platform)

    acc_email = f"Akun #{acc_idx}"
    try:
        with open(os.path.join(BASE_DIR, "augestel_accounts.json"), "r", encoding="utf-8") as af:
            accs = json.load(af)
            if 0 < acc_idx <= len(accs):
                acc_email = accs[acc_idx - 1].get("email", acc_email)
    except Exception:
        pass

    sms_entry = {
        "id": f"sim_{int(time.time())}",
        "phone": phone,
        "phone_masked": mask_phone_number(phone),
        "sender": platform,
        "message": custom_msg,
        "otp": otp,
        "platform": platform,
        "platform_emoji": p_emoji,
        "country_code": phone_cc,
        "flag": phone_flag,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "revenue": f"${rate_val:.4f}",
        "rate": rate_val,
        "range_name": range_name,
        "source": f"Augestel ({acc_email})",
    }

    msg_text = format_otp_message(sms_entry)
    keyboard = create_keyboard(sms_entry, FILE_LINK, CHANNEL_LINK, otp_text=otp)

    msg_id = None
    try:
        async def send_tg():
            bot = Bot(token=BOT_TOKEN)
            return await bot.send_message(
                chat_id=GROUP_CHAT_ID,
                text=msg_text,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard,
            )

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res = loop.run_until_complete(send_tg())
        loop.close()
        msg_id = res.message_id
    except Exception as e:
        logger.error(f"Gagal kirim simulated OTP ke TG: {e}")

    updated_earnings = record_earnings_sms(
        account_idx=acc_idx,
        account_email=acc_email,
        rate_val=rate_val,
        country_cc=phone_cc,
        country_flag=phone_flag,
        platform=platform,
        phone=phone
    )

    log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ 🧪 [Live Simulator] Akun #{acc_idx} ({acc_email}) Sent {platform} OTP {otp} for {phone} (Rate: ${rate_val:.4f})\n"
    log_path = os.path.join(BASE_DIR, "bot.log")
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception:
        pass

    return jsonify({
        "success": True,
        "message": f"Simulasi Webhook berhasil! OTP {otp} terkirim ke Telegram & pendapatan tercatat (${rate_val:.4f}).",
        "telegram_sent": bool(msg_id),
        "telegram_message_id": msg_id,
        "account": acc_email,
        "phone": phone,
        "otp": otp,
        "rate": rate_val,
        "earnings": updated_earnings
    })


@app.route("/api/augestel/webhooks/status")
@login_required
def api_augestel_webhooks_status():
    """Get current status of Augestel webhooks and recent events"""
    guardian_status = {}
    guardian_active = False
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            guardian_status = pool.get_webhook_guardian_status()
            guardian_active = pool.webhook_guardian_enabled
    except Exception:
        pass

    curr_tunnel = get_current_tunnel_url()
    return jsonify({
        "success": True,
        "webhook_url": f"{curr_tunnel}/api/augestel/webhook",
        "tunnel_url": curr_tunnel,
        "total_received": augestel_webhook_status["total_received"],
        "last_received": augestel_webhook_status["last_received"],
        "last_event": augestel_webhook_status["last_event"],
        "last_sms": augestel_webhook_status["last_sms"],
        "recent_history": augestel_webhook_history[:10],
        "guardian_enabled": guardian_active,
        "guardian_accounts": guardian_status,
    })


@app.route("/api/tunnel/info", methods=["GET"])
def api_tunnel_info():
    """Mengembalikan URL terowongan publik (Cloudflare Tunnel atau Ngrok) saat ini"""
    curr_tunnel = get_current_tunnel_url()
    is_cf = "trycloudflare.com" in curr_tunnel or "cloudflare" in curr_tunnel
    return jsonify({
        "success": True,
        "tunnel_url": curr_tunnel,
        "provider": "Cloudflare Tunnel (Unlimited 24/7)" if is_cf else "Ngrok",
        "webhook_url": f"{curr_tunnel}/api/augestel/webhook"
    })


@app.route("/api/augestel/webhooks/guardian/check-now", methods=["POST"])
@login_required
def api_augestel_webhooks_guardian_check_now():
    """Trigger Webhook Guardian auto-heal check immediately across all accounts"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.trigger_guardian_auto_heal_sync()
            return jsonify({
                "success": True,
                "results": res,
                "guardian_status": pool.get_webhook_guardian_status()
            })
        return jsonify({"success": False, "message": "Browser pool tidak berjalan"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
@app.route("/api/augestel/accounts/auto-setup", methods=["POST"])
@login_required
def api_augestel_accounts_auto_setup():
    """Trigger auto-setup (Login check, API Key generate/retrieve, Webhook install) for an Augestel account"""
    data = request.get_json(silent=True) or {}
    idx = int(data.get("index", 1))
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.ensure_account_setup_sync(idx)
            return jsonify(res)
        return jsonify({"success": False, "message": "Browser pool tidak berjalan"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})



@app.route("/api/augestel/webhooks/setup-single", methods=["POST"])
@login_required
def api_augestel_webhooks_setup_single():
    """Setup or refresh webhook for a single Augestel account synchronously"""
    data = request.get_json(silent=True) or {}
    idx = int(data.get("index", 1))
    webhook_url = data.get("webhook_url") or augestel_webhook_status["url"]
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.setup_account_webhook_sync(idx, webhook_url)
            return jsonify(res)
        return jsonify({"success": False, "message": "Browser pool tidak berjalan"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/webhooks/setup-all", methods=["POST"])
@login_required
def api_augestel_webhooks_setup_all():
    """
    Secara otomatis memasang webhook endpoint ke seluruh akun Augestel (1-7)
    menggunakan profil browser Playwright yang sudah login.
    """
    body = request.get_json(silent=True) or {}
    webhook_url = body.get("webhook_url") if isinstance(body, dict) else ""
    if not webhook_url:
        webhook_url = augestel_webhook_status["url"]

    def run_setup_worker():
        logger.info(f"🚀 Memulai auto-setup Webhook untuk semua akun Augestel ({webhook_url})...")
        try:
            from augestel_browser_pool import get_browser_pool
            pool = get_browser_pool()
            if pool and pool.is_running:
                res = pool.setup_all_webhooks_sync(webhook_url)
                logger.info(f"🎉 Selesai pasang webhook ke semua akun via Live Pool: {res}")
                return
        except Exception as e_pool:
            logger.warning(f"Fallback setup webhook: {e_pool}")

        from playwright.sync_api import sync_playwright
        profiles = []
        for i in range(1, 20):
            pdir = os.path.join(BASE_DIR, f"browser_profile_augestel_{i}")
            if os.path.exists(pdir):
                profiles.append(i)
                
        results = []
        with sync_playwright() as p:
            for idx in profiles:
                pdir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")
                logger.info(f"Mengonfigurasi webhook pada profil #{idx}...")
                try:
                    ctx = p.chromium.launch_persistent_context(
                        user_data_dir=pdir,
                        channel="msedge",
                        headless=False,
                        args=["--window-position=-2000,-2000"]
                    )
                    page = ctx.pages[0] if ctx.pages else ctx.new_page()
                    page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=30000)
                    
                    if "/login" in page.url.lower() or "login" in (page.title() or "").lower():
                        logger.warning(f"Akun #{idx} belum login, melewati webhook setup")
                        ctx.close()
                        results.append({"account_idx": idx, "success": False, "error": "Not logged in"})
                        continue
                    
                    url_input = page.wait_for_selector("#webhookUrl", timeout=10000)
                    url_input.fill(webhook_url)
                    
                    active_cb = page.query_selector('input[type="checkbox"][name="is_active"]')
                    if active_cb and not active_cb.is_checked():
                        active_cb.check()
                        
                    msg_cb = page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
                    if msg_cb and not msg_cb.is_checked():
                        msg_cb.check()
                        
                    submit_btn = page.query_selector('form[action*="webhook"] button[type="submit"]')
                    if submit_btn:
                        submit_btn.click()
                        page.wait_for_timeout(3000)
                        
                    saved_val = page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
                    ctx.close()
                    results.append({"account_idx": idx, "success": bool(saved_val == webhook_url), "saved_url": saved_val})
                    logger.info(f"✅ Akun #{idx} webhook terpasang: {saved_val}")
                except Exception as e:
                    logger.error(f"❌ Akun #{idx} gagal pasang webhook: {e}")
                    results.append({"account_idx": idx, "success": False, "error": str(e)})
                    
        logger.info(f"🎉 Selesai pasang webhook ke semua akun: {results}")

    threading.Thread(target=run_setup_worker, daemon=True).start()
    return jsonify({
        "success": True,
        "message": "Proses pemasangan webhook ke seluruh akun Augestel sedang berjalan di background!",
        "webhook_url": webhook_url
    })


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
    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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

    # Pastikan status akun Augestel tersinkron dengan Augestel Browser Pool (Keep-Alive RAM)
    pool_dict = {}
    try:
        from augestel_browser_pool import get_browser_pool
        pool_inst = get_browser_pool()
        if pool_inst and pool_inst.is_running:
            pool_dict = pool_inst.get_status_dict()
    except Exception:
        pass

    aug_file = os.path.join(BASE_DIR, "augestel_accounts.json")
    aug_accounts_db = []
    if os.path.exists(aug_file):
        try:
            with open(aug_file, "r", encoding="utf-8") as f:
                aug_accounts_db = json.load(f)
        except Exception:
            pass

    merged_aug_status = []
    for idx, a in enumerate(aug_accounts_db, start=1):
        email = a.get("email", "")
        api_ok = bool(a.get("api_key"))

        # Cek status browser keep-alive (RAM daemon)
        p_item = pool_dict.get(idx) or pool_dict.get(str(idx)) or {}
        pool_logged_in = p_item.get("logged_in", False)
        pool_message = p_item.get("message", "")

        if pool_logged_in:
            cookie_connected = True
            has_remember = True
            has_session = True
            cookie_status = "Standby di RAM (24/7)"
            is_pool_active = True
            last_check = p_item.get("last_check") or "Standby 24/7"
        elif pool_inst and pool_inst.is_running:
            # Pool is managing the browser, do NOT touch SQLite Cookies file directly
            cookie_connected = False
            has_remember = False
            has_session = False
            cookie_status = pool_message if pool_message else "Browser Standby / Belum Login"
            is_pool_active = False
            last_check = p_item.get("last_check") or ("Status Terpantau (Aktif)" if api_ok else "Belum ada API Key")
        else:
            c_info = check_augestel_browser_cookie(idx)
            cookie_connected = c_info.get("cookie_connected", False)
            has_remember = c_info.get("has_remember", False)
            has_session = c_info.get("has_session", False)
            cookie_status = pool_message if pool_message else c_info.get("status_text", "-")
            is_pool_active = False
            last_check = p_item.get("last_check") or ("Status Terpantau (Aktif)" if api_ok else "Belum ada API Key")

        merged_aug_status.append({
            "index": idx,
            "email": email or f"Akun #{idx}",
            "api_connected": api_ok,
            "cookie_connected": cookie_connected,
            "cookie_status": cookie_status,
            "has_remember": has_remember,
            "has_session": has_session,
            "cookie_count": 3 if pool_logged_in else 0,
            "is_pool_active": is_pool_active,
            "connected": api_ok and cookie_connected,
            "balance": a.get("balance", "0.00"),
            "last_check": last_check
        })

    augestel_status["accounts"] = merged_aug_status
    augestel_status["connected"] = any(acc["connected"] for acc in merged_aug_status) if merged_aug_status else False


    res = dict(bot_status)
    res["ivasms_status"] = ivasms_status
    res["accounts_status"] = merged_status
    res["augestel_status"] = augestel_status
    res["augestel_accounts_status"] = merged_aug_status
    return jsonify(res)


@app.route("/api/ivasms/check", methods=["POST"])
@login_required
def api_ivasms_check():
    """Check IVASMS connection (Platform dinonaktifkan)"""
    return jsonify({"success": True, "status": {"connected": False, "accounts": []}})


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

    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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
            cwd=BASE_DIR,
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


# ────────────────────────────────────────────
#  API ROUTES - AUTO-ADD AUGESTEL
# ────────────────────────────────────────────

@app.route("/api/augestel/auto-add/start", methods=["POST"])
@login_required
def api_augestel_auto_add_start():
    """Start auto-add numbers for Augestel"""
    global auto_add_augestel_state
    
    if auto_add_augestel_state["running"]:
        return jsonify({"success": False, "message": "Auto-add Augestel sudah berjalan!"})
    
    data = request.json or {}
    range_name = data.get("range_name", "").strip()
    number_prefix = data.get("number_prefix", "").strip()
    batch_count = int(data.get("batch_count", 250) or 250)
    batch_count = max(1, min(batch_count, 1000))
    max_add = int(data.get("max_add", 0) or 0)
    delay = int(data.get("delay", 15) or 15)
    raw_acc_val = data.get("account_index", "1")
    if isinstance(raw_acc_val, list):
        raw_acc = ",".join(str(x) for x in raw_acc_val)
    else:
        raw_acc = str(raw_acc_val).strip().lower()
    workers = int(data.get("workers", 2) or 2)
    workers = max(1, min(workers, 12))
    
    acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
    accounts_db = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts_db = json.load(f)
        except Exception:
            pass

    target_indices = []
    if raw_acc == "all":
        account_arg = "all"
        target_indices = list(range(1, len(accounts_db) + 1)) if accounts_db else [1]
        account_email = f"Semua Akun ({len(target_indices)} Akun Terdaftar)"
    elif "," in raw_acc:
        parts = [p.strip() for p in raw_acc.split(",") if p.strip().isdigit()]
        if not parts:
            parts = ["1"]
        target_indices = [int(p) for p in parts if 1 <= int(p) <= (len(accounts_db) or 10)]
        if not target_indices:
            target_indices = [1]
        account_arg = ",".join(str(x) for x in target_indices)
        account_email = f"{len(target_indices)} Akun Terpilih (" + ", ".join([f"#{p}" for p in target_indices]) + ")"
    else:
        try:
            acc_num = int(raw_acc)
        except Exception:
            acc_num = 1
        target_indices = [acc_num]
        account_arg = str(acc_num)
        account_email = f"Akun #{acc_num}"
        if 1 <= acc_num <= len(accounts_db):
            account_email = accounts_db[acc_num - 1].get("email", account_email)
    
    # ── Prioritaskan Live Browser Pool yang aktif di RAM ──
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
    except Exception:
        pool = None

    if pool and pool.is_running:
        auto_add_augestel_state = {
            "running": True,
            "account_index": account_arg,
            "account_email": account_email,
            "workers": workers,
            "range_name": range_name,
            "number_prefix": number_prefix,
            "batch_count": batch_count,
            "max_add": max_add,
            "delay": delay,
            "added": 0,
            "failed": 0,
            "skipped": 0,
            "total_found": 0,
            "current_action": 0,
            "last_message": f"Memulai Auto-Add via Live Browser Profile ({workers} worker) untuk {account_email}...",
            "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "process": None,
        }

        def on_pool_status_update(data):
            global auto_add_augestel_state
            if isinstance(data, dict):
                for k, v in data.items():
                    auto_add_augestel_state[k] = v

        def run_pool_auto_add_thread():
            global auto_add_augestel_state
            try:
                pool.run_coro(
                    pool.run_auto_add_multi(
                        account_indices=target_indices,
                        range_filter=range_name,
                        max_add=max_add,
                        delay=delay,
                        workers_count=workers,
                        batch_count=batch_count,
                        number_prefix=number_prefix,
                        status_callback=on_pool_status_update,
                        max_concurrent_accounts=len(target_indices)
                    ),
                    timeout=86400
                )
            except Exception as e:
                logger.error(f"Error Auto-Add Live Pool: {e}")
                auto_add_augestel_state["last_message"] = f"Error: {e}"
            finally:
                auto_add_augestel_state["running"] = False
                if auto_add_augestel_state.get("added", 0) > 0:
                    try:
                        from numbers_service import get_all_numbers
                        get_all_numbers(force_refresh=True, provider="augestel")
                    except Exception:
                        pass
                    try:
                        from telegram_file_sender import export_and_send_augestel_numbers_txt
                        export_and_send_augestel_numbers_txt(force=True, trigger_reason="Auto-Add Selesai (Nomor Baru Ditambahkan)")
                    except Exception as ex_send:
                        logger.error(f"Auto-send TXT error after pool auto-add: {ex_send}")

        th = threading.Thread(target=run_pool_auto_add_thread, daemon=True)
        th.start()

        desc_parts = []
        if range_name:
            desc_parts.append(f"Range: '{range_name}'")
        if number_prefix:
            desc_parts.append(f"Prefix: '{number_prefix}'")
        target_name = " & ".join(desc_parts) if desc_parts else "Semua Range & Nomor"
        return jsonify({"success": True, "message": f"Auto-add Augestel via Live Browser Pool dimulai untuk {target_name}!"})

    # ── Fallback Subprocess (Hanya jika Pool tidak aktif) ──
    try:
        proc = subprocess.Popen(
            [sys.executable, "-u", "auto_add_augestel.py", range_name, str(max_add), str(delay), account_arg, str(workers), str(batch_count), number_prefix],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        
        auto_add_augestel_state = {
            "running": True,
            "account_index": account_arg,
            "account_email": account_email,
            "workers": workers,
            "range_name": range_name,
            "number_prefix": number_prefix,
            "batch_count": batch_count,
            "max_add": max_add,
            "delay": delay,
            "added": 0,
            "failed": 0,
            "skipped": 0,
            "total_found": 0,
            "current_action": 0,
            "last_message": f"Memulai {workers} worker ({batch_count} nomor/request) untuk {account_email}...",
            "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "process": proc,
        }
        
        # Monitor in background thread
        def monitor_augestel_auto_add():
            global auto_add_augestel_state
            try:
                for line in iter(proc.stdout.readline, b''):
                    decoded = line.decode("utf-8", errors="replace").strip()
                    if decoded:
                        auto_add_augestel_state["last_message"] = decoded

                        if "Memulai Auto-Add Augestel untuk Akun #" in decoded:
                            m_acc = re.search(r"Akun #(\d+):?\s*(.*)", decoded)
                            if m_acc:
                                auto_add_augestel_state["account_email"] = f"Akun #{m_acc.group(1)} ({m_acc.group(2).strip()})"
                        
                        # Parse stats
                        if "Added=" in decoded:
                            m = re.search(r"Added=(\d+).*Failed=(\d+).*Skipped=(\d+)", decoded)
                            if m:
                                auto_add_augestel_state["added"] = int(m.group(1))
                                auto_add_augestel_state["failed"] = int(m.group(2))
                                auto_add_augestel_state["skipped"] = int(m.group(3))
                        
                        if "Action #" in decoded:
                            m = re.search(r"Action #(\d+)", decoded)
                            if m:
                                auto_add_augestel_state["current_action"] = int(m.group(1))
                        
                        if "total records" in decoded:
                            m = re.search(r"(\d+) total records", decoded)
                            if m:
                                auto_add_augestel_state["total_found"] = int(m.group(1))
                
                proc.wait()
            except Exception:
                pass
            finally:
                auto_add_augestel_state["running"] = False
                auto_add_augestel_state["process"] = None
                if auto_add_augestel_state.get("added", 0) > 0:
                    try:
                        from numbers_service import get_all_numbers
                        get_all_numbers(force_refresh=True, provider="augestel")
                    except Exception:
                        pass
                    try:
                        from telegram_file_sender import export_and_send_augestel_numbers_txt
                        export_and_send_augestel_numbers_txt(force=True, trigger_reason="Auto-Add Selesai (Nomor Baru Ditambahkan)")
                    except Exception as ex_send:
                        logger.error(f"Auto-send TXT error after fallback auto-add: {ex_send}")
        
        thread = threading.Thread(target=monitor_augestel_auto_add, daemon=True)
        thread.start()
        
        desc_parts = []
        if range_name:
            desc_parts.append(f"Range: '{range_name}'")
        if number_prefix:
            desc_parts.append(f"Prefix: '{number_prefix}'")
        target_name = " & ".join(desc_parts) if desc_parts else "Semua Range & Nomor"
        return jsonify({"success": True, "message": f"Auto-add Augestel dimulai untuk {target_name}!"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal: {e}"})


@app.route("/api/augestel/auto-add/stop", methods=["POST"])
@login_required
def api_augestel_auto_add_stop():
    """Stop auto-add Augestel"""
    global auto_add_augestel_state
    
    # 1. Hentikan auto-add di live pool jika sedang berjalan
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool:
            pool.stop_auto_add()
    except Exception:
        pass

    # 2. Hentikan subprocess jika fallback yang berjalan
    proc = auto_add_augestel_state.get("process")
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
    
    auto_add_augestel_state["running"] = False
    auto_add_augestel_state["process"] = None
    return jsonify({"success": True, "message": "Auto-add Augestel dihentikan."})


@app.route("/api/augestel/auto-add/status")
@login_required
def api_augestel_auto_add_status():
    """Get auto-add Augestel status"""
    safe_state = {k: v for k, v in auto_add_augestel_state.items() if k != "process"}
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
    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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

    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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

    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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
    acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
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
    """Add or update an Augestel account with automatic login, API Key generation & Webhook setup via Browser Pool"""
    data = request.json or {}
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()
    api_key = data.get("api_key", "").strip()
    index = data.get("index")

    if not email:
        return jsonify({"success": False, "message": "Email akun Augestel wajib diisi!"})

    if not password and not api_key:
        return jsonify({"success": False, "message": "Password portal Augestel wajib diisi untuk login!"})

    acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    new_entry = {
        "email": email,
        "password": password,
        "api_key": api_key
    }

    target_idx = 1
    if index is not None and isinstance(index, int) and 0 <= index < len(accounts):
        accounts[index] = new_entry
        target_idx = index + 1
    else:
        found = False
        for i, a in enumerate(accounts):
            if a.get("email", "").lower() == email.lower():
                accounts[i] = new_entry
                target_idx = i + 1
                found = True
                break
        if not found:
            accounts.append(new_entry)
            target_idx = len(accounts)

    try:
        with open(acc_file, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=2)

        # Update primary account to config.py if it's the first account and has key
        if len(accounts) >= 1 and accounts[0].get("api_key"):
            save_config({
                "AUGESTEL_EMAIL": accounts[0]["email"],
                "AUGESTEL_API_KEY": accounts[0].get("api_key", "")
            })

        # Memicu sinkronisasi pool browser di RAM secara real-time
        # Pool akan otomatis: 1) Login akun baru, 2) Ambil/Generate API Key, 3) Pasang Webhook
        try:
            from augestel_browser_pool import get_browser_pool
            pool = get_browser_pool()
            if pool and pool.is_running:
                threading.Thread(target=pool.sync_accounts_sync, daemon=True, name=f"PoolSyncAcc{target_idx}").start()
        except Exception as e_sync:
            logger.warning(f"Gagal memicu sinkronisasi browser pool: {e_sync}")

        msg = f"✅ Akun Augestel #{target_idx} ({email}) berhasil disimpan! Sistem Browser Pool di RAM otomatis melakukan login, mengambil/men-generate API Key, dan memasang Webhook."

        return jsonify({
            "success": True,
            "message": msg,
            "api_key": api_key,
            "accounts": accounts
        })
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal menyimpan akun Augestel: {e}"})


@app.route("/api/augestel/accounts/delete", methods=["POST"])
@login_required
def api_augestel_accounts_delete():
    """Delete an Augestel account by index or email"""
    data = request.json or {}
    index = data.get("index")
    email = data.get("email", "").strip()

    acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
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

            # Sinkronkan pool browser di RAM setelah akun dihapus
            try:
                from augestel_browser_pool import get_browser_pool
                pool = get_browser_pool()
                if pool and pool.is_running:
                    threading.Thread(target=pool.sync_accounts_sync, daemon=True, name="PoolSyncOnDelete").start()
            except Exception as e_sync:
                logger.warning(f"Gagal memicu sinkronisasi browser pool: {e_sync}")

            return jsonify({"success": True, "message": "Akun Augestel berhasil dihapus!", "accounts": accounts})
        except Exception as e:
            return jsonify({"success": False, "message": f"Gagal menyimpan: {e}"})

    return jsonify({"success": False, "message": "Akun Augestel tidak ditemukan."})


@app.route("/api/augestel/batch-login", methods=["POST"])
@login_required
def api_augestel_batch_login():
    """Trigger background batch login for all Augestel accounts via live pool in RAM"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            def _relogin_all_worker():
                for idx in range(1, len(pool.accounts) + 1):
                    try:
                        pool.relogin_account_sync(idx)
                    except Exception as ex:
                        logger.error(f"Error relogin account #{idx}: {ex}")
            threading.Thread(target=_relogin_all_worker, daemon=True, name="PoolBatchReloginWorker").start()
            return jsonify({"success": True, "message": "Proses refresh & login pool browser di RAM untuk semua akun telah dimulai!"})

        subprocess.Popen(
            [sys.executable, "batch_login_augestel.py"],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        return jsonify({"success": True, "message": "Proses batch login & warmup untuk semua akun Augestel telah dimulai di background!"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal memulai batch login: {e}"})


@app.route("/api/augestel/login-single", methods=["POST"])
@login_required
def api_augestel_login_single():
    """Trigger background browser login for a single Augestel account via live pool in RAM"""
    data = request.json or {}
    idx = data.get("index")
    if not idx:
        return jsonify({"success": False, "message": "Index akun tidak valid!"})
    try:
        idx_int = int(idx)
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.relogin_account_sync(idx_int)
            if res.get("success"):
                check_augestel_multi_connection(target_index=idx_int)
                return jsonify({"success": True, "message": f"Login browser Akun #{idx} di RAM berhasil diperbarui!"})
            else:
                return jsonify({"success": False, "message": f"Gagal login Akun #{idx} di RAM: {res.get('message')}"})

        subprocess.Popen(
            [sys.executable, "batch_login_augestel.py", "--account", str(idx)],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
        )
        return jsonify({"success": True, "message": f"Login browser profil Akun #{idx} sedang diproses di background!"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Gagal memulai login browser: {e}"})


def open_augestel_desktop_window(idx: int) -> dict:
    """
    Membuka jendela browser Microsoft Edge asli di layar desktop VPS
    untuk Akun Augestel #{idx} secara interaktif (100% tampak di monitor).
    """
    import os
    import json
    import subprocess
    import time

    base_dir = BASE_DIR
    accounts_file = os.path.join(base_dir, "augestel_accounts.json")
    accounts = []
    if os.path.exists(accounts_file):
        try:
            with open(accounts_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    email = ""
    pwd = ""
    masked_key = ""
    if 0 < idx <= len(accounts):
        acc = accounts[idx - 1]
        email = acc.get("email", "")
        pwd = acc.get("password", "")
        key = acc.get("api_key", "")
        if key:
            masked_key = f"{key[:8]}...{key[-4:]}" if len(key) > 12 else key

    user_data_dir = os.path.join(base_dir, f"browser_profile_augestel_{idx}")
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_exe):
        edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_exe):
        edge_exe = "msedge.exe"

    # 1. Inform the browser pool to release the context and mark this account in desktop mode
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool:
            pool.mark_desktop_mode(idx, active=True)
            if pool.is_running:
                pool.close_context_sync(idx)
    except Exception as e_pool:
        logger.debug(f"Pool release notice error: {e_pool}")

    # 2. Check if a visible Edge window for this profile is already running
    # If so, restore and focus it
    ps_find_focus = f'''
    $procs = Get-CimInstance Win32_Process | Where-Object {{ $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel_{idx}*" }}
    $found = $false
    foreach ($p in $procs) {{
        $gp = Get-Process -Id $p.ProcessId -ErrorAction SilentlyContinue
        if ($gp -and $gp.MainWindowHandle -ne 0) {{
            Add-Type @"
              using System;
              using System.Runtime.InteropServices;
              public class WinFocus {{
                [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
                [DllImport("user32.dll")] public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
              }}
"@ -ErrorAction SilentlyContinue
            [WinFocus]::ShowWindowAsync($gp.MainWindowHandle, 9)
            [WinFocus]::SetForegroundWindow($gp.MainWindowHandle)
            $found = $true
            break
        }}
    }}
    if ($found) {{ "FOCUSED" }} else {{ "NOT_FOUND" }}
    '''
    try:
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_find_focus], capture_output=True, text=True, timeout=8)
        if "FOCUSED" in res.stdout:
            return {
                "success": True,
                "message": f"Jendela Microsoft Edge Akun #{idx} ({email}) sudah terbuka di layar dan berhasil difokuskan ke depan!",
                "idx": idx,
                "email": email,
                "password": pwd,
                "masked_key": masked_key
            }
    except Exception:
        pass

    # 3. Kill any zombie/offscreen background processes locking this profile
    cmd_kill = (
        f'Get-CimInstance Win32_Process | '
        f'Where-Object {{ $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel_{idx}*" }} | '
        f'ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}'
    )
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", cmd_kill], capture_output=True, timeout=10)
    except Exception:
        pass

    # 4. Clean lock files in user_data_dir
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        lk_path = os.path.join(user_data_dir, lk)
        if os.path.exists(lk_path):
            try:
                os.remove(lk_path)
            except Exception:
                pass

    # 5. Launch native Edge directly on screen (coordinates 100, 80, size 1280x850)
    target_url = "https://augestel.com/Switchfy/client/numbers"
    cmd = [
        "powershell", "-NoProfile", "-Command",
        f'Start-Process "{edge_exe}" -ArgumentList @('
        f'\'--user-data-dir="{user_data_dir}"\','
        f'\'--window-position=100,80\','
        f'\'--window-size=1280,850\','
        f'\'--no-first-run\','
        f'\'--no-default-browser-check\','
        f'\'{target_url}\''
        f')'
    ]
    try:
        subprocess.run(cmd, capture_output=True, timeout=10)
    except Exception as e_launch:
        return {"success": False, "message": f"Gagal meluncurkan Edge: {e_launch}"}

    # 6. Wait a moment and bring it to foreground
    time.sleep(2)
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_find_focus], capture_output=True, text=True, timeout=6)
    except Exception:
        pass

    return {
        "success": True,
        "message": f"Jendela Microsoft Edge Akun #{idx} ({email}) BERHASIL DIBUKA di layar desktop VPS! Silakan klik puzzle / isi password di monitor.",
        "idx": idx,
        "email": email,
        "password": pwd,
        "masked_key": masked_key
    }


def close_augestel_desktop_window(idx: int) -> dict:
    """Menutup jendela Microsoft Edge desktop untuk Akun #{idx}."""
    import subprocess
    cmd_kill = (
        f'Get-CimInstance Win32_Process | '
        f'Where-Object {{ $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel_{idx}*" }} | '
        f'ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}'
    )
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", cmd_kill], capture_output=True, timeout=10)
    except Exception:
        pass

    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool:
            pool.mark_desktop_mode(idx, active=False)
    except Exception:
        pass

    return {"success": True, "message": f"Jendela desktop browser Akun #{idx} telah ditutup."}


def sync_augestel_desktop_session(idx: int) -> dict:
    """Memeriksa status cookies login Akun #{idx} setelah user berinteraksi di layar."""
    prof_stat = check_augestel_profile_status(idx)
    conn_res = check_augestel_multi_connection(target_index=idx)
    is_logged_in = prof_stat.get("cookie_connected", False)

    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool:
            pool.mark_desktop_mode(idx, active=False)
    except Exception:
        pass

    msg = "Sesi berhasil disinkronkan! " + ("Login AKTIF & valid." if is_logged_in else "Belum terdeteksi login aktif (Silakan login di Edge dan centang Remember Me).")
    return {
        "success": True,
        "logged_in": is_logged_in,
        "profile_status": prof_stat,
        "connection": conn_res,
        "message": msg
    }


@app.route("/api/augestel/pool/show/<int:idx>", methods=["GET", "POST"])
@login_required
def api_augestel_pool_show(idx):
    """Bring the Edge browser window for account idx to the VPS screen so user can interact with captcha/login"""
    try:
        res = open_augestel_desktop_window(idx)
        return jsonify(res)
    except Exception as e:
        logger.error(f"Error api_augestel_pool_show: {e}")
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/hide/<int:idx>", methods=["GET", "POST"])
@app.route("/api/augestel/pool/close-desktop/<int:idx>", methods=["GET", "POST"])
@login_required
def api_augestel_pool_hide(idx):
    """Move or close the Edge browser window for account idx"""
    try:
        res = close_augestel_desktop_window(idx)
        return jsonify(res)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/sync-session/<int:idx>", methods=["GET", "POST"])
@login_required
def api_augestel_pool_sync_session(idx):
    """Check and sync the login session for account idx after user finished on desktop"""
    try:
        res = sync_augestel_desktop_session(idx)
        return jsonify(res)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/close-context/<int:idx>", methods=["GET", "POST"])
@login_required
def api_augestel_close_context(idx):
    """Release profile lock by closing the background context for account idx"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.close_context_sync(idx)
            return jsonify(res)
        return jsonify({"success": False, "message": "Browser pool Augestel tidak aktif di RAM"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/reinit/<int:idx>", methods=["GET", "POST"])
@login_required
def api_augestel_reinit_context(idx):
    """Reload account idx from disk into RAM pool 24/7 after successful interactive login"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if pool and pool.is_running:
            res = pool.reinit_account_sync(idx)
            return jsonify(res)
        return jsonify({"success": False, "message": "Browser pool Augestel tidak aktif di RAM"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/check", methods=["POST"])
@login_required
def api_augestel_check():
    """Check Augestel connection for all accounts or single account"""
    try:
        data = request.json or {}
        target_idx = data.get("index")
        if target_idx is not None:
            try:
                target_idx = int(target_idx)
            except Exception:
                target_idx = None

        result = check_augestel_multi_connection(target_index=target_idx)
        return jsonify({
            "success": True,
            "status": {
                "connected": result.get("connected", False),
                "accounts": result.get("accounts", []),
                "total_accounts": len(result.get("accounts", [])),
                "last_check": result.get("last_check")
            }
        })
    except Exception as e:
        logger.error(f"Error in api_augestel_check: {e}")
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


@app.route("/api/numbers/delete-selected", methods=["POST"])
@login_required
def api_numbers_delete_selected():
    """Hapus / return daftar nomor yang dipilih user dari cache & database lokal."""
    data = request.json or {}
    raw_acc = str(data.get("account_index", "augestel_all")).strip().lower()
    selected_numbers = data.get("numbers", [])
    if not selected_numbers:
        return jsonify({"success": False, "message": "Tidak ada nomor yang dipilih."}), 400

    target_set = set(str(n).strip() for n in selected_numbers if str(n).strip())
    if not target_set:
        return jsonify({"success": False, "message": "Daftar nomor terpilih kosong."}), 400

    try:
        deleted_count = 0
        from numbers_service import get_augestel_accounts, _NUMBERS_CACHE
        aug_accounts = get_augestel_accounts()
        total_accounts = len(aug_accounts)

        # Loop update file cache per akun (1..total)
        for i in range(1, total_accounts + 1):
            cache_file = os.path.join(BASE_DIR, f"augestel_numbers_cache_{i}.json")
            if os.path.exists(cache_file):
                try:
                    with open(cache_file, "r", encoding="utf-8") as f:
                        c_data = json.load(f)
                    nums = c_data.get("numbers", [])
                    new_nums = [item for item in nums if str(item.get("number", "")).strip() not in target_set]
                    diff = len(nums) - len(new_nums)
                    if diff > 0:
                        deleted_count += diff
                        c_data["numbers"] = new_nums
                        c_data["count"] = len(new_nums)
                        c_data["total"] = len(new_nums)
                        c_data["cached_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open(cache_file, "w", encoding="utf-8") as f:
                            json.dump(c_data, f, indent=2)
                        _NUMBERS_CACHE.pop(f"augestel_{i}", None)
                except Exception as ex:
                    logger.warning(f"Error update cache {cache_file}: {ex}")

        # Update cache agregasi gabungan jika ada
        all_cache = os.path.join(BASE_DIR, "augestel_numbers_cache.json")
        if os.path.exists(all_cache):
            try:
                with open(all_cache, "r", encoding="utf-8") as f:
                    c_all = json.load(f)
                nums = c_all.get("numbers", [])
                new_nums = [item for item in nums if str(item.get("number", "")).strip() not in target_set]
                c_all["numbers"] = new_nums
                c_all["count"] = len(new_nums)
                c_all["total"] = len(new_nums)
                c_all["cached_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(all_cache, "w", encoding="utf-8") as f:
                    json.dump(c_all, f, indent=2)
                _NUMBERS_CACHE.pop("augestel_all", None)
            except Exception as ex:
                logger.warning(f"Error update all_cache: {ex}")

        logger.info(f"🗑️ Berhasil menghapus {len(target_set)} nomor terpilih dari cache Augestel.")
        return jsonify({
            "success": True,
            "message": f"Berhasil menghapus/return {len(target_set)} nomor terpilih dari daftar!",
            "deleted_count": len(target_set)
        })
    except Exception as e:
        logger.error(f"Error in api_numbers_delete_selected: {e}")
        return jsonify({"success": False, "message": f"Gagal menghapus nomor terpilih: {e}"}), 500



@app.route("/api/augestel/pool/status", methods=["GET"])
@login_required
def api_augestel_pool_status():
    """Get live status of Augestel 24/7 browser pool"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        return jsonify({
            "success": True,
            "is_running": pool.is_running,
            "status": pool.get_status_dict()
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/debug/<int:idx>", methods=["GET"])
@login_required
def api_augestel_pool_debug(idx):
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if idx not in pool.pages:
            return jsonify({"success": False, "message": f"No page for account #{idx}"})
        page = pool.pages[idx]

        async def get_debug():
            url = page.url
            title = await page.title()
            form_info = await page.evaluate('''() => {
                const f = document.querySelector('#loginForm, form');
                return {
                    formOuterHtml: f ? f.outerHTML : 'no form',
                    bodyText: document.body.innerText
                };
            }''')
            try:
                import os
                scr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scratch", f"login_acc{idx}.png")
                await page.screenshot(path=scr_path, full_page=True)
                form_info["screenshot"] = scr_path
            except Exception as e_scr:
                form_info["screenshot_err"] = str(e_scr)
            return {"url": url, "title": title, "form_info": form_info}

        res = pool.run_coro(get_debug(), timeout=15)
        return jsonify({"success": True, "data": res})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/eval/<int:idx>", methods=["POST"])
@login_required
def api_augestel_pool_eval(idx):
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if idx not in pool.pages:
            return jsonify({"success": False, "message": f"No page for {idx}"})
        data = request.json or {}
        js_code = data.get("script", "")
        page = pool.pages[idx]
        res = pool.run_coro(page.evaluate(js_code), timeout=15)
        return jsonify({"success": True, "result": res})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/augestel/pool/test-login/<int:idx>", methods=["POST"])
@login_required
def api_augestel_pool_test_login(idx):
    try:
        import asyncio
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        if idx not in pool.pages:
            return jsonify({"success": False, "message": f"No page for account #{idx}"})
        page = pool.pages[idx]
        acc = pool.accounts[idx - 1] if 0 < idx <= len(pool.accounts) else {}
        email = acc.get("email", "")
        password = acc.get("password", "")

        async def do_test():
            await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            
            email_el = await page.query_selector("#loginEmail, input[name='email']")
            pass_el = await page.query_selector("#loginPassword, input[name='password']")
            if not email_el or not pass_el:
                return {"error": "Input fields not found", "url": page.url}
                
            await email_el.fill(email)
            await pass_el.fill(password)
            
            cb = await page.query_selector("input[name='remember']")
            if cb:
                try: await cb.check()
                except Exception: pass
                
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
                
            await asyncio.sleep(4)
            
            final_url = page.url
            final_title = await page.title()
            
            error_info = await page.evaluate('''() => {
                const alerts = Array.from(document.querySelectorAll('.alert, .error, .invalid-feedback, .text-danger, .swal2-html-container, .swal2-title, .wait, #loginError, .login-error, span[role="alert"]')).map(e => e.innerText.trim()).filter(t => t.length > 0);
                const bodyText = document.body.innerText;
                const matchErr = bodyText.match(/(?:invalid|incorrect|credentials|match|blocked|suspended|verify|too many|cooldown|password)[^\\n\\.]*/gi);
                return { alerts, matchErr, url: window.location.href };
            }''')
            
            return {
                "email": email,
                "password_used": password,
                "final_url": final_url,
                "final_title": final_title,
                "error_info": error_info
            }

        res = pool.run_coro(do_test(), timeout=40)
        return jsonify({"success": True, "data": res})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/augestel/pool/start", methods=["POST"])
@login_required
def api_augestel_pool_start():
    """Start or re-initialize the 24/7 browser pool"""
    try:
        from augestel_browser_pool import get_browser_pool
        pool = get_browser_pool()
        import threading
        threading.Thread(target=pool.start_pool_sync, daemon=True).start()
        return jsonify({"success": True, "message": "Augestel Browser Pool sedang diinisialisasi di latar belakang!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route("/api/accounts/bulk-import", methods=["POST"])
@login_required
def api_accounts_bulk_import():
    """Bulk import IVASMS accounts in format email:password per line"""
    data = request.json or {}
    raw_text = data.get("text", "").strip()
    if not raw_text:
        return jsonify({"success": False, "message": "Teks akun tidak boleh kosong!"})

    acc_file = os.path.join(BASE_DIR, "ivasms_accounts.json")
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
    raw_idx = str(request.args.get("account_index", "augestel_all")).strip().lower()
    force_refresh = request.args.get("refresh", "0") in ["1", "true", "True"]
    if raw_idx in ["all", "1", ""] or not raw_idx.startswith("aug"):
        acc_arg = "augestel_all"
    else:
        acc_arg = raw_idx

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
    raw_idx = str(request.args.get("account_index", "augestel_all")).strip().lower()
    if raw_idx in ["all", "1", ""] or not raw_idx.startswith("aug"):
        acc_arg = "augestel_all"
    else:
        acc_arg = raw_idx

    try:
        from numbers_service import fetch_account_numbers, generate_numbers_excel
        res = asyncio.run(fetch_account_numbers(account_index=acc_arg, force_refresh=False))
        if not res.get("success"):
            return jsonify({"success": False, "message": res.get("message", "Gagal mengambil data")}), 400

        numbers_list = res.get("numbers", [])
        email = res.get("email", "all" if acc_arg == "all" else f"acc{acc_arg}")

        excel_buf = generate_numbers_excel(numbers_list, email=email)

        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        if acc_arg in ["augestel", "augestel_all", "aug_all", "all"]:
            filename = f"augestel_numbers_ALL_ACCOUNTS_{date_str}.xlsx"
        elif str(acc_arg).startswith("aug"):
            clean_email_tag = re.sub(r'[^a-zA-Z0-9]', '_', email.split('@')[0]) if '@' in email else str(acc_arg)
            filename = f"augestel_numbers_{clean_email_tag}_{date_str}.xlsx"
        else:
            filename = f"augestel_numbers_ALL_ACCOUNTS_{date_str}.xlsx"

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
    raw_idx = str(request.args.get("account_index", "augestel_all")).strip().lower()
    if raw_idx in ["all", "1", ""] or not raw_idx.startswith("aug"):
        acc_arg = "augestel_all"
    else:
        acc_arg = raw_idx

    try:
        from numbers_service import fetch_account_numbers, generate_numbers_txt
        res = asyncio.run(fetch_account_numbers(account_index=acc_arg, force_refresh=False))
        if not res.get("success"):
            return jsonify({"success": False, "message": res.get("message", "Gagal mengambil data")}), 400

        numbers_list = res.get("numbers", [])
        email = res.get("email", "all" if acc_arg == "all" else f"acc{acc_arg}")

        txt_content = generate_numbers_txt(numbers_list)

        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        if acc_arg in ["augestel", "augestel_all", "aug_all", "all"]:
            filename = f"augestel_numbers_ALL_ACCOUNTS_{date_str}.txt"
        elif str(acc_arg).startswith("aug"):
            clean_email_tag = re.sub(r'[^a-zA-Z0-9]', '_', email.split('@')[0]) if '@' in email else str(acc_arg)
            filename = f"augestel_numbers_{clean_email_tag}_{date_str}.txt"
        else:
            filename = f"augestel_numbers_ALL_ACCOUNTS_{date_str}.txt"

        return Response(
            txt_content,
            mimetype="text/plain; charset=utf-8",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        logger.error(f"Error in api_numbers_export_txt: {e}")
        return jsonify({"success": False, "message": f"Gagal export TXT: {e}"}), 500


@app.route("/api/numbers/send-telegram", methods=["POST"])
@login_required
def api_numbers_send_telegram():
    """Mengirim file TXT nomor Augestel ke Pemilik Bot Telegram secara manual dari dashboard"""
    data = request.json or {}
    raw_acc = str(data.get("account_index", "")).strip().lower()
    try:
        from telegram_file_sender import export_and_send_augestel_numbers_txt, send_telegram_document, get_owner_chat_id, get_fallback_chat_id
        if not raw_acc or raw_acc in ["augestel_all", "aug_all", "all"]:
            res = export_and_send_augestel_numbers_txt(force=True, trigger_reason="Manual dari Web Dashboard")
            return jsonify(res)

        from numbers_service import fetch_account_numbers
        res_data = asyncio.run(fetch_account_numbers(account_index=raw_acc, force_refresh=False))
        numbers = res_data.get("numbers", [])
        if not numbers:
            return jsonify({"success": False, "message": "Tidak ada nomor pada akun terpilih untuk dikirim!"}), 400

        lines = [str(it.get("number", "")).strip() for it in numbers if str(it.get("number", "")).strip()]
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_dir = os.path.join(BASE_DIR, "exports")
        os.makedirs(export_dir, exist_ok=True)
        acc_tag = res_data.get("email", raw_acc).replace(" ", "_")
        acc_tag = re.sub(r'[^a-zA-Z0-9_#]', '', acc_tag)
        file_name = f"augestel_numbers_{acc_tag}_{date_str}.txt"
        file_path = os.path.join(export_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        owner_id = (get_owner_chat_id() or get_fallback_chat_id() or "").strip()
        if not owner_id:
            return jsonify({"success": False, "message": "Chat ID Telegram belum diatur!"}), 400

        caption = (
            f"📱 <b>FILE NOMOR AUGESTEL ({res_data.get('email', raw_acc)})</b>\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🔢 <b>Total Nomor:</b> {len(lines):,} nomor\n"
            f"🕒 <b>Waktu Ekspor:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} WIB\n"
            f"ℹ️ <i>Dikirim manual dari Web Dashboard</i>"
        )
        send_res = send_telegram_document(owner_id, file_path, caption)
        send_res["total_numbers"] = len(lines)
        return jsonify(send_res)
    except Exception as e:
        logger.error(f"Error in api_numbers_send_telegram: {e}")
        return jsonify({"success": False, "message": f"Gagal kirim ke Telegram: {e}"}), 500


@app.route("/api/numbers/export-selected/excel", methods=["POST"])
@login_required
def api_numbers_export_selected_excel():
    """Export daftar nomor terpilih (selected) ke Excel (.xlsx)"""
    data = request.json or {}
    numbers_list = data.get("numbers", [])
    if not numbers_list:
        return jsonify({"success": False, "message": "Tidak ada nomor terpilih untuk diekspor"}), 400

    try:
        from numbers_service import generate_numbers_excel
        excel_buf = generate_numbers_excel(numbers_list, email="Pilihan Terpilih (Selected)")
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"augestel_selected_{len(numbers_list)}_nomor_{date_str}.xlsx"

        return send_file(
            excel_buf,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        logger.error(f"Error in api_numbers_export_selected_excel: {e}")
        return jsonify({"success": False, "message": f"Gagal export Excel nomor terpilih: {e}"}), 500


@app.route("/api/numbers/send-telegram-selected", methods=["POST"])
@login_required
def api_numbers_send_telegram_selected():
    """Kirim file .txt berisi nomor-nomor terpilih langsung ke chat Telegram Pemilik"""
    data = request.json or {}
    numbers_list = data.get("numbers", [])
    if not numbers_list:
        return jsonify({"success": False, "message": "Tidak ada nomor terpilih untuk dikirim"}), 400

    try:
        import config as _cfg
        owner_id = str(getattr(_cfg, "OWNER_CHAT_ID", "")).strip() or str(getattr(_cfg, "GROUP_CHAT_ID", "")).strip()
        if not owner_id:
            return jsonify({"success": False, "message": "OWNER_CHAT_ID belum diatur pada config.py!"}), 400

        lines = []
        for it in numbers_list:
            if isinstance(it, dict):
                n = str(it.get("number", "")).strip()
            else:
                n = str(it).strip()
            if n:
                lines.append(n)

        if not lines:
            return jsonify({"success": False, "message": "Daftar nomor terpilih kosong."}), 400

        txt_content = "\n".join(lines)
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_dir = os.path.join(BASE_DIR, "exports")
        os.makedirs(export_dir, exist_ok=True)
        file_path = os.path.join(export_dir, f"augestel_selected_{len(lines)}_nomor_{date_str}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(txt_content)

        caption = (
            f"📱 <b>Augestel Numbers (Pilihan Manual)</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"✨ <b>Jumlah Nomor:</b> <code>{len(lines):,}</code> nomor terpilih\n"
            f"📅 <b>Waktu Export:</b> <code>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
            f"🎯 <b>Format:</b> Text File (.txt - 1 nomor per baris)\n"
            f"━━━━━━━━━━━━━━━━━━"
        )

        from telegram_file_sender import send_telegram_document
        res = send_telegram_document(owner_id, file_path, caption=caption)
        if res.get("success"):
            return jsonify({
                "success": True,
                "message": f"File TXT berisi {len(lines)} nomor terpilih berhasil dikirim ke Telegram!",
                "total_numbers": len(lines)
            })
        else:
            return jsonify({
                "success": False,
                "message": f"Gagal kirim ke Telegram: {res.get('message', 'Unknown error')}"
            }), 500

    except Exception as e:
        logger.error(f"Error in api_numbers_send_telegram_selected: {e}")
        return jsonify({"success": False, "message": f"Gagal mengirim ke Telegram: {e}"}), 500



# ────────────────────────────────────────────
#  RUN
# ────────────────────────────────────────────


if __name__ == "__main__":
    print("=" * 55)
    print("  🌐 OTP IVA SMS - Admin Dashboard")
    print("  📍 http://localhost:5000")
    print(f"  👤 Login: {ADMIN_USER} / {ADMIN_PASS}")
    print("=" * 55)

    # Inisialisasi Augestel Browser Pool (Standby 24/7 di RAM)
    try:
        from augestel_browser_pool import get_browser_pool
        import threading
        pool = get_browser_pool()
        threading.Thread(target=pool.start_pool_sync, daemon=True, name="AugestelPoolStarter").start()
    except Exception as e_pool:
        logger.warning(f"Gagal auto-start browser pool: {e_pool}")

    # Periodic API Revenue Sync (Setiap 20 menit sync otomatis ke API Augestel)
    def _periodic_api_sync_worker():
        time.sleep(15)
        while True:
            try:
                trigger_background_api_sync()
            except Exception as e_sync:
                logger.debug(f"Periodic API sync error: {e_sync}")
            time.sleep(1200)

    threading.Thread(target=_periodic_api_sync_worker, daemon=True, name="AugestelApiSyncWorker").start()

    app.run(host="0.0.0.0", port=5000, debug=False)

