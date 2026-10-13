#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
#  🤖 IVASMS OTP TELEGRAM BOT
#  ─────────────────────────────────────────────────────────────
#  Bot Telegram yang memonitor IVASMS dan mengirim OTP
#  secara real-time ke grup Telegram
#
#  Format pesan seperti di gambar:
#  🇲🇱 ML | 🟢 | +2237🫣4077
#  WhatsApp                    16:30
#  ┌─────────────────┐
#  │     577732       │
#  └─────────────────┘
#  [📁 File]  [✈️ Grup OTP]
# ═══════════════════════════════════════════════════════════════

import asyncio
import logging
import signal
import sys
import os
import json
import time
from datetime import datetime

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

from telegram import Bot, CopyTextButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

# Local imports
import re
from config import (
    BOT_TOKEN,
    GROUP_CHAT_ID,
    GROUP_LINK,
    NUMBER_LINK,
    OWNER_LINK,
    BOT_NAME,
    IVASMS_URL,
    IVASMS_SMS_ENDPOINT,
    POLL_INTERVAL,
    COOKIES,
    COOKIES_2,
    IVASMS_EMAIL,
    IVASMS_PASSWORD,
    IVASMS_EMAIL_2,
    IVASMS_PASSWORD_2,
    ELITE_SMS_ENABLED,
    ELITE_SMS_URL,
    ELITE_SMS_API_KEY,
)

try:
    from config import (
        AUGESTEL_ENABLED,
        AUGESTEL_URL,
        AUGESTEL_API_KEY,
        AUGESTEL_EMAIL,
    )
except ImportError:
    AUGESTEL_ENABLED = False
    AUGESTEL_URL = "https://augestel.com/api/v1/iprn"
    AUGESTEL_API_KEY = ""
    AUGESTEL_EMAIL = ""

try:
    from config import COOKIES_2, IVASMS_EMAIL_2, IVASMS_PASSWORD_2
except ImportError:
    COOKIES_2 = {}
    IVASMS_EMAIL_2 = ""
    IVASMS_PASSWORD_2 = ""

try:
    from config import FILE_LINK, CHANNEL_LINK, SENSOR_TEXT
except ImportError:
    FILE_LINK = NUMBER_LINK
    CHANNEL_LINK = GROUP_LINK
    SENSOR_TEXT = "••••"
from ivasms_scraper import IVASMSClient
from elite_sms_client import EliteSMSClient
from augestel_client import AugestelClient
from cookie_sync import get_fresh_cookies_from_browser

# ────────────────────────────────────────────
#  LOGGING SETUP
# ────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log', encoding='utf-8'),
    ]
)
logger = logging.getLogger("OTPBot")

# Reduce noise from libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("cloudscraper").setLevel(logging.WARNING)


# ────────────────────────────────────────────
#  MESSAGE FORMATTER
# ────────────────────────────────────────────
def format_otp_message(sms_data: dict) -> str:
    """
    Format pesan OTP:

    🇿🇼 ZW | 🟢 2637 •••• 4006 #EN
    🔢 Prefix: 263788
    """
    flag = sms_data.get("flag", "🏳️")
    country = sms_data.get("country_code", "??")
    platform = sms_data.get("platform", "SMS")

    # Platform icon
    p_lower = platform.lower()
    if "whatsapp" in p_lower or "wa " in p_lower:
        platform_icon = "🟢"
    elif "telegram" in p_lower:
        platform_icon = "🔵"
    else:
        platform_icon = sms_data.get("platform_emoji", "💬")

    # Ambil angka murni nomor telepon
    phone = str(sms_data.get("phone", "")).strip()
    digits = re.sub(r'\D', '', phone)

    # Prefix = 6 nomer pertama
    prefix_6 = digits[:6] if len(digits) >= 6 else digits

    # Mask nomor telepon (4 angka depan & 4 angka belakang)
    sensor = SENSOR_TEXT or "••••"
    if len(digits) >= 8:
        phone_masked = f"{digits[:4]} {sensor} {digits[-4:]}"
    elif len(digits) > 4:
        phone_masked = f"{digits[:4]} {sensor}"
    else:
        phone_masked = digits or "???"

    # Tag bahasa (#EN / #ID / dsb)
    msg_text = sms_data.get("message", "").lower()
    if any(w in msg_text for w in ["kode", "adalah", "jangan", "rahasia"]):
        lang_tag = "#ID"
    elif any(w in msg_text for w in ["codigo", "código", "es tu", "clave"]):
        lang_tag = "#ES"
    else:
        lang_tag = "#EN"

    # Baris 1: 🇿🇼 ZW | 🟢 2637 •••• 4006 #EN
    line1 = f"{flag} {country} | {platform_icon} {phone_masked} {lang_tag}"

    # Baris 2: 🔢 Prefix: 263788
    line2 = f"🔢 Prefix: {prefix_6}"

    return f"{line1}\n{line2}"


def create_keyboard(sms_data: dict, file_link: str = "", channel_link: str = "", otp_text: str = "") -> InlineKeyboardMarkup:
    """
    Buat inline keyboard persis screenshot:
    [           🔑 758-347            ]  <-- copy button (highlighted)
    [ 📁 FILE ↗ ]   [ 🔔 CHANNEL ↗ ]
    """
    f_link = (file_link or FILE_LINK or NUMBER_LINK or "").strip()
    c_link = (channel_link or CHANNEL_LINK or GROUP_LINK or "").strip()

    def ensure_url(url: str) -> str:
        if not url:
            return ""
        if not url.startswith("http://") and not url.startswith("https://"):
            return "https://" + url
        return url

    f_url = ensure_url(f_link)
    c_url = ensure_url(c_link)

    # Ambil OTP angka murni & formatted
    raw_otp = otp_text or sms_data.get("otp", "") or ""
    clean_otp = str(raw_otp).strip()
    if len(clean_otp) == 6 and clean_otp.isdigit():
        otp_display = f"{clean_otp[:3]}-{clean_otp[3:]}"
    else:
        otp_display = clean_otp

    # Row 1: Tombol Salin OTP persis screenshot: 🔑 758-347
    copy_btn = InlineKeyboardButton(
        f"🔑 {otp_display}",
        copy_text=CopyTextButton(text=clean_otp),
    )

    # Row 2: FILE & CHANNEL (tanpa panah)
    file_btn = (
        InlineKeyboardButton("📁 FILE", url=f_url)
        if f_url
        else InlineKeyboardButton("📁 FILE", callback_data="btn_file")
    )

    channel_btn = (
        InlineKeyboardButton("🔔 CHANNEL", url=c_url)
        if c_url
        else InlineKeyboardButton("🔔 CHANNEL", callback_data="btn_channel")
    )

    buttons = [
        [copy_btn],              # Row 1: Copy OTP
        [file_btn, channel_btn], # Row 2: File & Channel
    ]

    return InlineKeyboardMarkup(buttons)


# ────────────────────────────────────────────
#  STATISTICS TRACKER & REVENUE COUNTER
# ────────────────────────────────────────────
class StatsTracker:
    """Track statistik OTP, estimasi cuan/revenue, dan tren jam sibuk."""

    def __init__(self):
        self.total_sent = 0
        self.total_revenue = 0.0
        self.start_time = datetime.now()
        self.platform_counts = {}
        self.country_counts = {}
        self.hourly_counts = {f"{h:02d}:00": 0 for h in range(24)}

    def record(self, sms_data: dict):
        self.total_sent += 1
        platform = sms_data.get("platform", "Unknown")
        country = sms_data.get("country_code", "??")
        self.platform_counts[platform] = self.platform_counts.get(platform, 0) + 1
        self.country_counts[country] = self.country_counts.get(country, 0) + 1

        # Hitung revenue ($0.05 default jika tidak tertera)
        rev_str = str(sms_data.get("revenue", "$0.00")).replace("$", "").replace("€", "").strip()
        try:
            val = float(rev_str)
            if val <= 0:
                val = 0.05  # Estimasi rata-rata rate per OTP IVASMS
            self.total_revenue += val
        except Exception:
            self.total_revenue += 0.05

        # Catat jam pengiriman (tren jam sibuk)
        hour_key = datetime.now().strftime("%H:00")
        self.hourly_counts[hour_key] = self.hourly_counts.get(hour_key, 0) + 1

    def get_summary(self) -> str:
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        top_platforms = sorted(self.platform_counts.items(), key=lambda x: -x[1])[:5]
        top_countries = sorted(self.country_counts.items(), key=lambda x: -x[1])[:5]

        platform_text = "\n".join(
            f"  • {name}: *{count}*" for name, count in top_platforms
        ) or "  _Belum ada data_"

        country_text = "\n".join(
            f"  • {code}: *{count}*" for code, count in top_countries
        ) or "  _Belum ada data_"

        return (
            f"📊 *STATISTIK OTP BOT*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"⏱ Uptime: `{hours}h {minutes}m {seconds}s`\n"
            f"📨 Total OTP: *{self.total_sent}*\n"
            f"💰 Est. Revenue: *${self.total_revenue:.2f}*\n"
            f"\n"
            f"📱 *Platform:*\n{platform_text}\n"
            f"\n"
            f"🌍 *Negara:*\n{country_text}\n"
            f"━━━━━━━━━━━━━━━━━━━━"
        )


# ────────────────────────────────────────────
#  FULL MESSAGE STORAGE (untuk tombol File)
# ────────────────────────────────────────────
# Store last N full messages for callback queries
full_messages = {}
MAX_STORED_MESSAGES = 500


def store_full_message(sms_id: str, message: str):
    """Simpan full message untuk callback query."""
    full_messages[sms_id[:40]] = message
    # Cleanup old messages
    if len(full_messages) > MAX_STORED_MESSAGES:
        oldest_keys = list(full_messages.keys())[:-MAX_STORED_MESSAGES]
        for key in oldest_keys:
            del full_messages[key]


# ────────────────────────────────────────────
#  BOT COMMANDS
# ────────────────────────────────────────────
stats = StatsTracker()


bot_accounts_status = {}

def update_bot_status(ivasms_ok: bool = None, elite_ok: bool = None, augestel_ok: bool = None, accounts_status: list = None, acc_idx: int = None, acc_connected: bool = None):
    """Simpan status bot & setiap akun IVASMS & Augestel real-time ke status.json agar dashboard web sinkron 100%."""
    global bot_accounts_status
    try:
        status_file = os.path.join(os.path.dirname(__file__), "status.json")
        data = {}
        if os.path.exists(status_file):
            try:
                with open(status_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                pass
        data["bot_running"] = True
        data["pid"] = os.getpid()
        data["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if ivasms_ok is not None:
            data["ivasms_connected"] = bool(ivasms_ok)
        if elite_ok is not None:
            data["elite_connected"] = bool(elite_ok)
        if augestel_ok is not None:
            data["augestel_connected"] = bool(augestel_ok)

        # Update status per akun
        if accounts_status is not None:
            for item in accounts_status:
                if isinstance(item, dict) and "index" in item:
                    bot_accounts_status[item["index"]] = item
        elif acc_idx is not None and acc_connected is not None:
            if acc_idx in bot_accounts_status:
                bot_accounts_status[acc_idx]["connected"] = bool(acc_connected)
                bot_accounts_status[acc_idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                bot_accounts_status[acc_idx] = {
                    "index": acc_idx,
                    "connected": bool(acc_connected),
                    "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

        if bot_accounts_status:
            data["accounts_status"] = list(bot_accounts_status.values())

        data["total_sent"] = getattr(stats, "total_sent", 0)
        data["total_revenue"] = round(getattr(stats, "total_revenue", 0.0), 2)
        data["platform_counts"] = getattr(stats, "platform_counts", {})
        data["country_counts"] = getattr(stats, "country_counts", {})
        data["hourly_counts"] = getattr(stats, "hourly_counts", {})
        temp_file = status_file + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        if os.path.exists(temp_file):
            os.replace(temp_file, status_file)
    except Exception as e:
        logger.debug(f"Status file update error: {e}")


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /start command."""
    welcome_msg = (
        f"🤖 *{BOT_NAME} - OTP Monitor Bot*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"\n"
        f"Bot ini memonitor IVASMS dan mengirim\n"
        f"kode OTP secara *real-time* ke grup.\n"
        f"\n"
        f"📋 *Perintah:*\n"
        f"  /start — Menu utama\n"
        f"  /status — Status koneksi\n"
        f"  /stats — Statistik OTP\n"
        f"  /ping — Cek bot hidup\n"
        f"\n"
        f"⚡ Polling interval: `{POLL_INTERVAL}` detik\n"
        f"🌐 Source: `{IVASMS_URL}`\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    await update.message.reply_text(welcome_msg, parse_mode=ParseMode.MARKDOWN)


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /status command."""
    global active_clients, active_elite_client
    await update.message.reply_text("🔄 Checking providers connection...", parse_mode=ParseMode.MARKDOWN)

    # Cek status semua akun IVASMS aktif
    ivasms_any_ok = False
    status_lines = [
        f"🤖 *Bot Status: RUNNING*",
        f"━━━━━━━━━━━━━━━━━━━━",
    ]

    accounts = load_ivasms_accounts()
    for idx, acc in enumerate(accounts, start=1):
        email_disp = acc.get("email", f"Akun {idx}")
        # Cek jika ada client terdaftar
        is_ok = False
        if idx - 1 < len(active_clients):
            cl = active_clients[idx - 1]
            is_ok = cl.check_connection()
            if not is_ok:
                fresh_c = await get_fresh_cookies_from_browser(account_index=idx, email=acc.get("email"), password=acc.get("password"))
                if fresh_c:
                    cl.update_cookies(fresh_c)
                    is_ok = cl.check_connection()
        if is_ok:
            ivasms_any_ok = True
        status_lines.append(f"🌐 IVASMS (Akun {idx}): {'✅ Connected' if is_ok else '❌ Disconnected'} - `{email_disp}`")

    # Cek Elite-SMS
    is_elite_ok = False
    if ELITE_SMS_ENABLED and ELITE_SMS_API_KEY:
        if not active_elite_client:
            active_elite_client = EliteSMSClient(ELITE_SMS_API_KEY, ELITE_SMS_URL)
        is_elite_ok = active_elite_client.check_connection()

    # Sinkronisasi status ke status.json agar dashboard web langsung update
    update_bot_status(ivasms_ok=ivasms_any_ok, elite_ok=is_elite_ok)

    status_lines.extend([
        f"🌐 Elite-SMS: {'✅ Connected' if is_elite_ok else '❌ Offline/Disabled' if ELITE_SMS_ENABLED else '⚪ Disabled'}",
        f"⚡ Interval: `{POLL_INTERVAL}s`",
        f"📨 Total OTP sent: *{stats.total_sent}*",
        f"━━━━━━━━━━━━━━━━━━━━",
    ])
    await update.message.reply_text("\n".join(status_lines), parse_mode=ParseMode.MARKDOWN)


async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /stats command."""
    await update.message.reply_text(stats.get_summary(), parse_mode=ParseMode.MARKDOWN)


async def cmd_ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /ping command."""
    await update.message.reply_text(
        f"🏓 *Pong!*\n⏰ `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`",
        parse_mode=ParseMode.MARKDOWN
    )


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk callback dari inline keyboard."""
    query = update.callback_query
    data = query.data or ""
    await query.answer()

    if data in ("btn_file", "btn_number"):
        await query.answer("Link FILE belum diisi di config.py.", show_alert=True)
        return

    if data in ("btn_channel", "btn_owner"):
        await query.answer("Link CHANNEL belum diisi di config.py.", show_alert=True)
        return

    if data.startswith("file_"):
        sms_id = data[5:]
        full_msg = full_messages.get(sms_id, "⚠️ Pesan sudah tidak tersedia (expired)")

        # Truncate jika terlalu panjang
        if len(full_msg) > 3000:
            full_msg = full_msg[:3000] + "\n\n... _(truncated)_"

        await query.message.reply_text(
            f"📁 *Full SMS Content:*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"```\n{full_msg}\n```",
            parse_mode=ParseMode.MARKDOWN,
        )


# ────────────────────────────────────────────
#  OTP POLLING LOOP
# ────────────────────────────────────────────
async def poll_otp(bot: Bot, client: IVASMSClient, chat_id: str, account_idx: int = 1):
    """Loop utama untuk polling OTP dari IVASMS (bisa akun 1 atau akun 2)."""
    logger.info(f"🚀 OTP polling started (IVASMS Akun {account_idx})")

    consecutive_errors = 0
    max_errors = 10

    while True:
        try:
            # Ambil SMS baru
            new_sms_list = client.get_new_sms()
            update_bot_status(ivasms_ok=True, acc_idx=account_idx, acc_connected=True)

            for sms_data in new_sms_list:
                try:
                    # Format pesan (sama persis tanpa pembeda notifikasi)
                    message = format_otp_message(sms_data)
                    keyboard = create_keyboard(sms_data, FILE_LINK, CHANNEL_LINK)

                    # Simpan full message untuk callback
                    store_full_message(
                        sms_data.get("id", "unknown"),
                        sms_data.get("message", "No message")
                    )

                    # Kirim ke Telegram
                    await bot.send_message(
                        chat_id=chat_id,
                        text=message,
                        parse_mode=ParseMode.HTML,
                        reply_markup=keyboard,
                    )

                    # Record stats
                    stats.record(sms_data)
                    update_bot_status(ivasms_ok=True, acc_idx=account_idx, acc_connected=True)

                    logger.info(
                        f"📤 Sent OTP [Akun {account_idx}]: {sms_data.get('country_code', '??')} | "
                        f"{sms_data.get('platform', 'SMS')} | "
                        f"{sms_data.get('otp', 'N/A')}"
                    )

                    # Delay antar pesan untuk menghindari rate limit
                    await asyncio.sleep(0.5)

                except Exception as e:
                    logger.error(f"❌ Failed to send message [Akun {account_idx}]: {e}")

            consecutive_errors = 0  # Reset error counter on success

        except Exception as e:
            consecutive_errors += 1
            logger.error(f"❌ Polling error Akun {account_idx} ({consecutive_errors}/{max_errors}): {e}")
            update_bot_status(acc_idx=account_idx, acc_connected=False)

            # Otomatis refresh cookie dari browser jika ada error sesi
            if consecutive_errors >= 1:
                logger.info(f"🔄 Auto-refreshing cookies Akun {account_idx} from background browser...")
                try:
                    fresh_c = await get_fresh_cookies_from_browser(account_index=account_idx)
                    if fresh_c:
                        client.update_cookies(fresh_c)
                        logger.info(f"✅ Cookies Akun {account_idx} successfully auto-refreshed!")
                        consecutive_errors = 0
                        update_bot_status(ivasms_ok=True, acc_idx=account_idx, acc_connected=True)
                except Exception as sync_e:
                    logger.error(f"Failed auto-refresh Akun {account_idx}: {sync_e}")

            if consecutive_errors >= max_errors:
                logger.critical(f"🔴 Too many consecutive errors Akun {account_idx}! Pausing for 60s...")
                await asyncio.sleep(60)
                consecutive_errors = 0

        # Wait before next poll
        await asyncio.sleep(POLL_INTERVAL)


async def poll_otp_elite(bot: Bot, client: EliteSMSClient, chat_id: str):
    """Loop polling OTP dari Elite-SMS API."""
    logger.info("🚀 Elite-SMS polling started")
    while True:
        try:
            new_sms_list = client.get_new_sms(limit=50)
            update_bot_status(elite_ok=True)
            for sms_data in new_sms_list:
                try:
                    message = format_otp_message(sms_data)
                    keyboard = create_keyboard(sms_data, FILE_LINK, CHANNEL_LINK)

                    store_full_message(
                        sms_data.get("id", "unknown"),
                        sms_data.get("message", "No message")
                    )

                    await bot.send_message(
                        chat_id=chat_id,
                        text=message,
                        parse_mode=ParseMode.HTML,
                        reply_markup=keyboard,
                    )

                    stats.record(sms_data)
                    update_bot_status(elite_ok=True)
                    logger.info(
                        f"📤 [Elite-SMS] Sent OTP: {sms_data.get('country_code', '??')} | "
                        f"{sms_data.get('platform', 'SMS')} | "
                        f"{sms_data.get('otp', 'N/A')}"
                    )
                    await asyncio.sleep(0.5)
                except Exception as e:
                    logger.error(f"❌ [Elite-SMS] Failed to send message: {e}")
        except Exception as e:
            logger.error(f"❌ [Elite-SMS] Polling error: {e}")
            update_bot_status(elite_ok=False)

        await asyncio.sleep(POLL_INTERVAL)


async def poll_otp_augestel(bot: Bot, client: AugestelClient, chat_id: str, account_idx: int = 1):
    """Loop polling OTP dari Augestel API (https://augestel.com)."""
    email_label = getattr(client, "email", f"Akun #{account_idx}")
    logger.info(f"🚀 Augestel polling started (Akun #{account_idx}: {email_label})")
    poll_gap = max(14, POLL_INTERVAL)  # 14s agar aman dari rate limit 5 req/menit
    while True:
        try:
            # Jika sedang dalam masa cooldown rate limit
            now_t = time.time()
            limit_until = getattr(client, "rate_limit_until", 0)
            if limit_until > now_t:
                wait_time = int(limit_until - now_t) + 1
                logger.info(f"⏳ [Augestel #{account_idx}] Menunggu cooldown 429 ({wait_time}s)...")
                await asyncio.sleep(wait_time)

            new_sms_list = client.get_new_sms(per_page=100)
            update_bot_status(augestel_ok=True)
            for sms_data in new_sms_list:
                try:
                    message = format_otp_message(sms_data)
                    keyboard = create_keyboard(sms_data, FILE_LINK, CHANNEL_LINK)

                    store_full_message(
                        sms_data.get("id", "unknown"),
                        sms_data.get("message", "No message")
                    )

                    await bot.send_message(
                        chat_id=chat_id,
                        text=message,
                        parse_mode=ParseMode.HTML,
                        reply_markup=keyboard,
                    )

                    stats.record(sms_data)
                    update_bot_status(augestel_ok=True)
                    logger.info(
                        f"📤 [Augestel #{account_idx}] Sent OTP: {sms_data.get('country_code', '??')} | "
                        f"{sms_data.get('platform', 'SMS')} | "
                        f"{sms_data.get('otp', 'N/A')}"
                    )
                    await asyncio.sleep(0.5)
                except Exception as e:
                    logger.error(f"❌ [Augestel #{account_idx}] Failed to send message: {e}")
        except Exception as e:
            logger.error(f"❌ [Augestel #{account_idx}] Polling error: {e}")
            update_bot_status(augestel_ok=False)

        await asyncio.sleep(poll_gap)


def load_augestel_accounts() -> list:
    """Muat semua akun Augestel dari augestel_accounts.json (fallback ke config.py)."""
    accs_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    if os.path.exists(accs_file):
        try:
            with open(accs_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception as e:
            logger.warning(f"Gagal membaca augestel_accounts.json: {e}")

    accs = []
    if AUGESTEL_API_KEY:
        accs.append({
            "email": AUGESTEL_EMAIL or "saputradimas0878@gmail.com",
            "api_key": AUGESTEL_API_KEY
        })
    return accs


def load_ivasms_accounts() -> list:
    """Muat semua akun IVASMS dari ivasms_accounts.json (fallback ke config.py)."""
    accs_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    if os.path.exists(accs_file):
        try:
            with open(accs_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception as e:
            logger.warning(f"Gagal membaca ivasms_accounts.json: {e}")

    # Fallback ke konfigurasi statis
    accs = []
    if IVASMS_EMAIL and IVASMS_PASSWORD:
        accs.append({"email": IVASMS_EMAIL, "password": IVASMS_PASSWORD, "cookies": COOKIES})
    if IVASMS_EMAIL_2 and IVASMS_PASSWORD_2:
        accs.append({"email": IVASMS_EMAIL_2, "password": IVASMS_PASSWORD_2, "cookies": COOKIES_2})
    return accs


# Global client instances
active_clients = []
active_elite_client = None
active_augestel_client = None

# ────────────────────────────────────────────
#  MAIN APPLICATION
# ────────────────────────────────────────────
async def post_init(application: Application):
    """Called after bot initialization."""
    global active_clients, active_elite_client
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    logger.info(f"🤖 {BOT_NAME} is starting up...")
    logger.info(f"🌐 IVASMS URL: {IVASMS_URL}")
    if ELITE_SMS_ENABLED:
        logger.info(f"🌐 Elite-SMS URL: {ELITE_SMS_URL}")
    logger.info(f"⚡ Poll interval: {POLL_INTERVAL}s")
    logger.info(f"📤 Target chat: {GROUP_CHAT_ID}")
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    accounts = load_ivasms_accounts()
    logger.info(f"📋 Terdeteksi {len(accounts)} akun IVASMS terdaftar.")

    active_clients = []
    for idx, acc in enumerate(accounts, start=1):
        email = acc.get("email", "").strip()
        pwd = acc.get("password", "").strip()
        cookies = acc.get("cookies") or (COOKIES if idx == 1 else COOKIES_2 if idx == 2 else {})

        if not email or not pwd:
            continue

        try:
            client = IVASMSClient(cookies, IVASMS_URL)
            conn_ok = client.check_connection()
            if not conn_ok:
                logger.info(f"🔄 Checking fresh cookies from browser profile (Akun {idx}: {email})...")
                try:
                    fresh_c = await get_fresh_cookies_from_browser(account_index=idx, email=email, password=pwd)
                    if fresh_c:
                        client.update_cookies(fresh_c)
                        conn_ok = client.check_connection()
                except Exception as e:
                    logger.warning(f"Browser sync Akun {idx} skipped: {e}")

            if conn_ok:
                logger.info(f"✅ IVASMS connection (Akun {idx}: {email}) verified!")
                try:
                    existing_count = client.mark_initial_as_seen()
                    logger.info(f"📌 [IVASMS Akun {idx}] Skipping {existing_count} existing SMS")
                except Exception as ex:
                    logger.warning(f"Could not fetch initial SMS Akun {idx}: {ex}")
            else:
                logger.warning(f"⚠️ IVASMS Akun {idx} ({email}) session expired. Bot tetap berjalan & auto-sync!")

            active_clients.append(client)
            asyncio.create_task(poll_otp(application.bot, client, GROUP_CHAT_ID, account_idx=idx))
            update_bot_status(acc_idx=idx, acc_connected=conn_ok)
            if conn_ok:
                update_bot_status(ivasms_ok=True)
        except Exception as acc_err:
            logger.error(f"⚠️ Gagal inisialisasi IVASMS poller Akun {idx}: {acc_err}")
            update_bot_status(acc_idx=idx, acc_connected=False)

    # Inisialisasi Elite-SMS Client (Multi-Provider)
    if ELITE_SMS_ENABLED and ELITE_SMS_API_KEY:
        try:
            active_elite_client = EliteSMSClient(ELITE_SMS_API_KEY, ELITE_SMS_URL)
            if active_elite_client.check_connection():
                logger.info("✅ Elite-SMS connection verified!")
            else:
                logger.warning("⚠️ Elite-SMS connection status not online, will still poll...")
            
            existing_elite = active_elite_client.mark_initial_as_seen()
            logger.info(f"📌 [Elite-SMS] Skipping {existing_elite} existing SMS")
            asyncio.create_task(poll_otp_elite(application.bot, active_elite_client, GROUP_CHAT_ID))
        except Exception as e_err:
            logger.error(f"❌ Failed to init Elite-SMS client: {e_err}")

    # Inisialisasi Augestel Client (Multi-Provider & Multi-Account)
    if AUGESTEL_ENABLED:
        aug_accounts = load_augestel_accounts()
        logger.info(f"📋 Terdeteksi {len(aug_accounts)} akun Augestel terdaftar.")
        for a_idx, a_acc in enumerate(aug_accounts, 1):
            a_key = a_acc.get("api_key", "").strip()
            a_email = a_acc.get("email", "").strip()
            if not a_key:
                continue
            try:
                cl = AugestelClient(api_key=a_key, base_url=AUGESTEL_URL, email=a_email)
                if a_idx == 1:
                    active_augestel_client = cl
                    if cl.check_connection():
                        logger.info(f"✅ Augestel (Akun #{a_idx}: {a_email}) connection verified!")
                        update_bot_status(augestel_ok=True)
                existing_aug = cl.mark_initial_as_seen()
                logger.info(f"📌 [Augestel Akun #{a_idx}: {a_email}] Skipping {existing_aug} existing SMS")
                asyncio.create_task(poll_otp_augestel(application.bot, cl, GROUP_CHAT_ID, account_idx=a_idx))
                await asyncio.sleep(1.5)
            except Exception as aug_err:
                logger.error(f"❌ Failed to init Augestel client Akun #{a_idx}: {aug_err}")

    # Startup message to Telegram group disabled per user request
    logger.info("Bot startup complete (silent startup mode)")


def main():
    """Entry point utama."""
    # ──── Validasi konfigurasi ────
    if not BOT_TOKEN:
        print("=" * 50)
        print("❌ ERROR: BOT_TOKEN belum diisi!")
        print("")
        print("Cara mendapatkan Bot Token:")
        print("1. Buka Telegram, cari @BotFather")
        print("2. Kirim /newbot")
        print("3. Ikuti instruksi")
        print("4. Copy token ke config.py")
        print("=" * 50)
        sys.exit(1)

    if not GROUP_CHAT_ID:
        print("=" * 50)
        print("❌ ERROR: GROUP_CHAT_ID belum diisi!")
        print("")
        print("Cara mendapatkan Chat ID:")
        print("1. Tambahkan @userinfobot ke grup")
        print("2. Atau gunakan @getidsbot")
        print("3. Copy chat ID ke config.py")
        print("   (Grup biasanya dimulai dengan -100)")
        print("=" * 50)
        sys.exit(1)

    if not COOKIES:
        print("=" * 50)
        print("❌ ERROR: COOKIES IVASMS belum diisi!")
        print("")
        print("Cara mendapatkan cookies:")
        print("1. Buka https://www.ivasms.com")
        print("2. Login ke akun Anda")
        print("3. Tekan F12 → Application → Cookies")
        print("4. Copy semua cookies ke config.py")
        print("=" * 50)
        sys.exit(1)

    # ──── Build & Run Application ────
    logger.info("🔧 Building application...")

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Register command handlers
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("ping", cmd_ping))

    # Register callback handler untuk inline buttons
    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Run the bot with infinite auto-recovery loop
    logger.info("🚀 Starting bot (24/7 auto-recovery mode)...")
    retry_delay = 5
    while True:
        try:
            try:
                asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            app.run_polling(
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True,
            )
            break
        except (KeyboardInterrupt, SystemExit):
            logger.info("Bot stopped by user.")
            break
        except Exception as crash_err:
            logger.critical(f"💥 Unhandled polling crash: {crash_err}. Auto-restarting in {retry_delay}s...")
            import time
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)


if __name__ == "__main__":
    main()
