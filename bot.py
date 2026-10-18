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

from functools import wraps
from telegram import Bot, CopyTextButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode

# Local imports
import re
from config import (
    BOT_TOKEN,
    GROUP_CHAT_ID,
    GROUP_LINK,
    NUMBER_LINK,
    OWNER_LINK,
    OWNER_CHAT_ID,
    BOT_NAME,
    POLL_INTERVAL,
)

try:
    from config import (
        AUGESTEL_ENABLED,
        AUGESTEL_URL,
        AUGESTEL_API_KEY,
        AUGESTEL_EMAIL,
        AUGESTEL_POLLING_ENABLED,
    )
except ImportError:
    AUGESTEL_ENABLED = False
    AUGESTEL_URL = "https://augestel.com/api/v1/iprn"
    AUGESTEL_API_KEY = ""
    AUGESTEL_EMAIL = ""
    AUGESTEL_POLLING_ENABLED = False

try:
    from config import FILE_LINK, CHANNEL_LINK, SENSOR_TEXT
except ImportError:
    FILE_LINK = NUMBER_LINK
    CHANNEL_LINK = GROUP_LINK
    SENSOR_TEXT = "••••"
from otp_utils import (
    get_country_from_phone,
    mask_phone_number,
    detect_platform,
    extract_otp,
    COUNTRY_FLAGS,
)
from augestel_client import AugestelClient
from otp_dedup import is_duplicate_and_claim

# ────────────────────────────────────────────
#  LOGGING SETUP
# ────────────────────────────────────────────
logger = logging.getLogger("OTPBot")
if not logger.handlers:
    _sh = logging.StreamHandler(sys.stdout)
    _fh = logging.FileHandler('bot.log', encoding='utf-8')
    _fmt = logging.Formatter('%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    _sh.setFormatter(_fmt)
    _fh.setFormatter(_fmt)
    logger.addHandler(_sh)
    logger.addHandler(_fh)
    logger.setLevel(logging.INFO)
    logger.propagate = False

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


_cfg_file_cache = ""
_cfg_channel_cache = ""
_cfg_mtime_cache = 0

def _get_dynamic_links(file_link: str = "", channel_link: str = "") -> tuple:
    global _cfg_file_cache, _cfg_channel_cache, _cfg_mtime_cache
    try:
        cfg_path = os.path.join(DIR_PATH, "config.py")
        if os.path.exists(cfg_path):
            mt = os.path.getmtime(cfg_path)
            if mt != _cfg_mtime_cache:
                import importlib
                import config as _cfg
                importlib.reload(_cfg)
                _cfg_file_cache = getattr(_cfg, "FILE_LINK", "") or getattr(_cfg, "NUMBER_LINK", "")
                _cfg_channel_cache = getattr(_cfg, "CHANNEL_LINK", "") or getattr(_cfg, "GROUP_LINK", "")
                _cfg_mtime_cache = mt
    except Exception:
        pass
    f_link = (_cfg_file_cache or file_link or FILE_LINK or NUMBER_LINK or "").strip()
    c_link = (_cfg_channel_cache or channel_link or CHANNEL_LINK or GROUP_LINK or "").strip()
    return f_link, c_link


def create_keyboard(sms_data: dict, file_link: str = "", channel_link: str = "", otp_text: str = "") -> InlineKeyboardMarkup:
    """
    Buat inline keyboard persis screenshot:
    [           🔑 758-347            ]  <-- copy button (highlighted)
    [ 📁 FILE ↗ ]   [ 🔔 CHANNEL ↗ ]
    """
    f_link, c_link = _get_dynamic_links(file_link, channel_link)

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

        # Muat data revenue resmi dari API Augestel (augestel_earnings.json)
        api_rev_text = ""
        try:
            efile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "augestel_earnings.json")
            if os.path.exists(efile):
                with open(efile, "r", encoding="utf-8") as f:
                    ed = json.load(f)
                tot_usd = float(ed.get("total_revenue_usd", 0.0) or 0.0)
                tot_idr = int(ed.get("total_revenue_idr", 0) or (tot_usd * 16250))
                tot_sms = int(ed.get("total_sms", 0) or 0)
                today_usd = float(ed.get("today_revenue_usd", 0.0) or 0.0)
                today_sms = int(ed.get("today_sms", 0) or 0)
                yest_usd = float(ed.get("yesterday_revenue_usd", 0.0) or 0.0)
                yest_sms = int(ed.get("yesterday_sms", 0) or 0)
                last_sync = ed.get("last_api_sync", "-")

                api_rev_text = (
                    f"💰 *AUGESTEL OFFICIAL REVENUE (API)*\n"
                    f"• Total Payout: *${tot_usd:.4f}* (≈ Rp {tot_idr:,})\n"
                    f"• Hari Ini: *${today_usd:.4f}* ({today_sms} OTP)\n"
                    f"• Kemarin: *${yest_usd:.4f}* ({yest_sms} OTP)\n"
                    f"• Total Trafik API: *{tot_sms} SMS*\n"
                    f"• Terakhir Sync: `{last_sync}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                )
        except Exception:
            pass

        top_platforms = sorted(self.platform_counts.items(), key=lambda x: -x[1])[:5]
        top_countries = sorted(self.country_counts.items(), key=lambda x: -x[1])[:5]

        platform_text = "\n".join(
            f"  • {name}: *{count}*" for name, count in top_platforms
        ) or "  _Belum ada data_"

        country_text = "\n".join(
            f"  • {code}: *{count}*" for code, count in top_countries
        ) or "  _Belum ada data_"

        return (
            f"📊 *STATISTIK OTP BOT & CUAN*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"{api_rev_text}"
            f"🤖 *STATUS RUNTIME BOT*\n"
            f"• Uptime: `{hours}h {minutes}m {seconds}s`\n"
            f"• OTP Sesi Ini: *{self.total_sent}*\n"
            f"\n"
            f"📱 *Platform (Sesi):*\n{platform_text}\n"
            f"\n"
            f"🌍 *Negara (Sesi):*\n{country_text}\n"
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

def update_bot_status(ivasms_ok: bool = None, augestel_ok: bool = None, accounts_status: list = None, acc_idx: int = None, acc_connected: bool = None):
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


# ────────────────────────────────────────────
#  OWNER AUTHORIZATION (KHUSUS PEMILIK BOT)
# ────────────────────────────────────────────
def is_owner(update: Update) -> bool:
    """Cek apakah pengirim pesan / command adalah Pemilik Bot (Owner Tunggal: 8584584698)."""
    try:
        from telegram_file_sender import get_owner_chat_id
        owner_id = str(get_owner_chat_id() or "").strip()
    except Exception:
        owner_id = ""

    if not owner_id:
        try:
            from config import OWNER_CHAT_ID
            owner_id = str(OWNER_CHAT_ID or "").strip()
        except Exception:
            owner_id = ""

    if not owner_id:
        owner_id = "8584584698"

    user = update.effective_user
    chat = update.effective_chat

    user_id = str(user.id) if user else ""
    chat_id = str(chat.id) if chat else ""

    allowed_ids = [x.strip() for x in re.split(r'[,;\s]+', owner_id) if x.strip()]
    return (user_id in allowed_ids or chat_id in allowed_ids)



def owner_only(func):
    """Decorator: Hanya izinkan Pemilik Bot (Owner) yang bisa menjalankan perintah/input."""
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        if not is_owner(update):
            user = update.effective_user
            user_id = str(user.id) if user else "Unknown"
            user_name = user.full_name if user else "Unknown"
            logger.warning(f"🚫 [Akses Ditolak] User {user_name} (ID: {user_id}) mencoba menjalankan /{func.__name__}")
            if update.message:
                await update.message.reply_text(
                    f"⛔ *Akses Ditolak*\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"Maaf, bot ini disetting *khusus Pemilik Bot (Owner)*.\n"
                    f"Anda tidak memiliki izin untuk memberikan input atau perintah ke bot ini.\n\n"
                    f"🆔 *ID Telegram Anda:* `{user_id}`",
                    parse_mode=ParseMode.MARKDOWN
                )
            return
        return await func(update, context, *args, **kwargs)
    return wrapper


async def handle_private_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menolak semua pesan non-command dari non-owner di chat pribadi."""
    if not update.message:
        return
    if not is_owner(update):
        user = update.effective_user
        user_id = str(user.id) if user else "Unknown"
        user_name = user.full_name if user else "Unknown"
        logger.warning(f"🚫 [Input Ditolak] Non-owner {user_name} (ID: {user_id}) mengirim pesan pribadi: {update.message.text or ''}")
        await update.message.reply_text(
            f"⛔ *Akses Ditolak*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"Maaf, bot ini disetting *khusus Pemilik Bot (Owner)*.\n"
            f"Hanya Pemilik Bot yang diizinkan untuk berinteraksi dengan bot ini.\n\n"
            f"🆔 *ID Telegram Anda:* `{user_id}`",
            parse_mode=ParseMode.MARKDOWN
        )


@owner_only
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /start command dengan auto-detection Pemilik Bot."""
    chat = update.effective_chat
    user = update.effective_user

    owner_info = ""
    if chat and chat.type == "private":
        try:
            from telegram_file_sender import get_owner_chat_id, set_owner_chat_id
            curr_owner = get_owner_chat_id()
            if not curr_owner:
                set_owner_chat_id(str(chat.id))
                owner_info = (
                    f"\n\n👑 *Status Pemilik Bot:*\n"
                    f"Chat ID Anda (`{chat.id}`) telah *otomatis tersimpan* sebagai Pemilik Bot!\n"
                    f"File nomor TXT akan otomatis dikirimkan ke chat pribadi ini setiap kali seluruh nomor akun Augestel selesai terdeteksi."
                )
            elif curr_owner == str(chat.id):
                owner_info = (
                    f"\n\n👑 *Status Pemilik Bot:*\n"
                    f"Anda terdaftar sebagai Pemilik Bot (`{chat.id}`).\n"
                    f"Ketik /filenomor untuk meminta file TXT nomor terbaru kapan saja."
                )
        except Exception:
            pass

    welcome_msg = (
        f"🤖 *{BOT_NAME} - OTP Monitor Bot*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"\n"
        f"Bot ini memonitor Augestel dan mengirim\n"
        f"kode OTP secara *real-time* ke grup.\n"
        f"\n"
        f"📋 *Perintah:*\n"
        f"  /start — Menu utama\n"
        f"  /status — Status koneksi provider\n"
        f"  /stats — Statistik OTP & cuan\n"
        f"  /filenomor — Minta file TXT seluruh nomor Augestel\n"
        f"  /myid — Cek Chat ID Telegram Anda\n"
        f"  /setowner — Daftarkan chat ini sebagai Pemilik\n"
        f"  /ping — Cek bot hidup\n"
        f"\n"
        f"⚡ Provider: `Augestel`\n"
        f"⚡ Polling interval: `{POLL_INTERVAL}` detik\n"
        f"{owner_info}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    await update.message.reply_text(welcome_msg, parse_mode=ParseMode.MARKDOWN)


@owner_only
async def cmd_myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk melihat Chat ID Telegram."""
    chat = update.effective_chat
    user = update.effective_user
    await update.message.reply_text(
        f"🆔 *Info Telegram Anda:*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"• Chat ID: `{chat.id}`\n"
        f"• Tipe: `{chat.type}`\n"
        f"• Nama: {user.full_name or 'N/A'}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"Status: Anda terdaftar sebagai Pemilik Bot Telegram.",
        parse_mode=ParseMode.MARKDOWN
    )


@owner_only
async def cmd_setowner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk mendaftarkan chat pribadi sebagai Pemilik Bot."""
    chat = update.effective_chat
    if not chat or chat.type != "private":
        await update.message.reply_text("⚠️ Perintah `/setowner` harus dikirim melalui Chat Pribadi dengan bot (bukan di dalam grup)!", parse_mode=ParseMode.MARKDOWN)
        return

    try:
        from telegram_file_sender import set_owner_chat_id
        set_owner_chat_id(str(chat.id))
        await update.message.reply_text(
            f"👑 *Sukses Terdaftar!*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"Chat ID `{chat.id}` kini resmi terdaftar sebagai *Pemilik Bot Telegram*.\n\n"
            f"Setiap kali seluruh nomor akun Augestel selesai terdeteksi/disinkronkan, file `.txt` (1 nomor per baris) akan otomatis dikirimkan ke chat pribadi ini!\n\n"
            f"Ketik `/filenomor` kapan saja untuk meminta file terbaru saat ini.",
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Gagal menyimpan: {e}", parse_mode=ParseMode.MARKDOWN)


@owner_only
async def cmd_filenomor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk meminta file TXT seluruh nomor Augestel secara on-demand."""
    chat = update.effective_chat
    status_msg = await update.message.reply_text("⏳ Sedang menyiapkan file TXT seluruh nomor Augestel...", parse_mode=ParseMode.MARKDOWN)
    try:
        from telegram_file_sender import export_and_send_augestel_numbers_txt
        res = export_and_send_augestel_numbers_txt(target_chat_id=str(chat.id), force=True, trigger_reason="Permintaan On-Demand /filenomor")
        if res.get("success"):
            try:
                await status_msg.delete()
            except Exception:
                pass
        else:
            await status_msg.edit_text(f"❌ Gagal mengirim file nomor: {res.get('message')}")
    except Exception as e:
        await status_msg.edit_text(f"❌ Terjadi kesalahan: {e}")



@owner_only
async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /status command."""
    global active_clients
    await update.message.reply_text("🔄 Checking providers connection...", parse_mode=ParseMode.MARKDOWN)

    aug_accounts = load_augestel_accounts()
    status_lines = [
        f"🤖 *Bot Status: RUNNING*",
        f"━━━━━━━━━━━━━━━━━━━━",
        f"🌐 Augestel: {'✅ Webhook Mode (Real-Time Push)' if AUGESTEL_ENABLED and not AUGESTEL_POLLING_ENABLED else '✅ Polling Mode' if AUGESTEL_ENABLED else '⚪ Disabled'}",
        f"📋 Akun Augestel: *{len(aug_accounts)} Akun Terdaftar*",
        f"⚡ Polling Interval: `{POLL_INTERVAL}s`",
        f"📨 Total OTP sent: *{stats.total_sent}*",
        f"━━━━━━━━━━━━━━━━━━━━",
    ]
    update_bot_status(augestel_ok=True)
    await update.message.reply_text("\n".join(status_lines), parse_mode=ParseMode.MARKDOWN)


@owner_only
async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk /stats command."""
    await update.message.reply_text(stats.get_summary(), parse_mode=ParseMode.MARKDOWN)


@owner_only
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





async def poll_otp_augestel_multi(bot: Bot, clients_with_idx: list, chat_id: str):
    """
    Loop polling OTP Augestel Multi-Account terkoordinasi (Round-Robin Sequential).
    Menghindari tabrakan request paralel antar akun sehingga terbebas dari
    Cloudflare 1015 IP Rate Limit dan Laravel 429 Too Many Requests.
    """
    total_accs = len(clients_with_idx)
    logger.info(f"🚀 Augestel Multi-Account Poller aktif untuk {total_accs} akun (Sequential Safe Mode).")

    while True:
        try:
            # 1. Cek apakah ada cooldown global (misal setelah 429)
            rem_cd = AugestelClient.get_remaining_cooldown()
            if rem_cd > 0:
                logger.info(f"⏳ [Augestel] Menunggu cooldown rate limit ({rem_cd}s tersisa)...")
                await asyncio.sleep(rem_cd)
                continue

            # 2. Polling setiap akun secara bergiliran dengan jeda aman
            for account_idx, client in clients_with_idx:
                # Jika di tengah jalan terkena cooldown, segera istirahat
                if AugestelClient.get_remaining_cooldown() > 0:
                    break

                try:
                    new_sms_list = client.get_new_sms(per_page=100)
                    update_bot_status(augestel_ok=True)
                    for sms_data in new_sms_list:
                        try:
                            phone = sms_data.get("phone", "")
                            otp = sms_data.get("otp", "")
                            raw_msg = sms_data.get("message", "")

                            # Cegah pengiriman duplikat (termasuk jika Webhook sudah kirim duluan)
                            if is_duplicate_and_claim(phone, otp, raw_msg, source=f"Augestel #{account_idx}"):
                                logger.info(
                                    f"🛡️ [Augestel #{account_idx}] Duplicate OTP skipped for {phone} (otp={otp})"
                                )
                                continue

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

                # Jeda optimal antar akun (4.5 detik sesuai enforce_rate_gap Augestel)
                await asyncio.sleep(4.5)

            # Jeda antar putaran penuh seluruh akun (5.0 detik)
            await asyncio.sleep(5.0)

        except Exception as loop_err:
            logger.error(f"❌ [Augestel Poller] Unexpected loop error: {loop_err}")
            await asyncio.sleep(10)


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
    """Stub kompatibilitas akun IVASMS (dinonaktifkan)."""
    return []


# Global client instances
active_clients = []
active_augestel_client = None

# ────────────────────────────────────────────
#  MAIN APPLICATION
# ────────────────────────────────────────────
async def post_init(application: Application):
    """Called after bot initialization."""
    global active_clients, active_augestel_client
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    logger.info(f"🤖 {BOT_NAME} is starting up...")
    logger.info(f"⚡ Provider: Augestel")
    logger.info(f"⚡ Poll interval: {POLL_INTERVAL}s")
    logger.info(f"📤 Target chat: {GROUP_CHAT_ID}")
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Inisialisasi Augestel (Multi-Provider & Multi-Account)
    if AUGESTEL_ENABLED:
        update_bot_status(augestel_ok=True)
        if not AUGESTEL_POLLING_ENABLED:
            logger.info("📡 [Augestel] Mode Webhook Murni AKTIF (Jalur Polling dimatikan per permintaan, 0 API Rate Limit, Anti-Double OTP).")
        else:
            aug_accounts = load_augestel_accounts()
            logger.info(f"📋 Terdeteksi {len(aug_accounts)} akun Augestel terdaftar untuk polling.")
            aug_clients_list = []
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
                    aug_clients_list.append((a_idx, cl))
                except Exception as aug_err:
                    logger.error(f"❌ Failed to init Augestel client Akun #{a_idx}: {aug_err}")

            if aug_clients_list:
                # Luncurkan 1 task orchestrator tunggal terkoordinasi untuk seluruh akun
                asyncio.create_task(poll_otp_augestel_multi(application.bot, aug_clients_list, GROUP_CHAT_ID))

    async def _bot_heartbeat_loop():
        """Mengirim sinyal detak jantung rutin ke status.json agar watchdog tahu bot sehat walafiat (terutama dalam mode webhook)."""
        while True:
            try:
                update_bot_status(augestel_ok=True)
            except Exception:
                pass
            await asyncio.sleep(45)

    asyncio.create_task(_bot_heartbeat_loop())

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

    # ──── Build & Run Application ────
    logger.info("🔧 Building application...")

    from telegram.request import HTTPXRequest
    from telegram.error import NetworkError, TimedOut, RetryAfter

    custom_request = HTTPXRequest(
        connection_pool_size=16,
        connect_timeout=20.0,
        read_timeout=30.0,
        write_timeout=20.0,
        pool_timeout=15.0,
    )

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .request(custom_request)
        .post_init(post_init)
        .build()
    )

    async def on_telegram_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Menangani gangguan jaringan sementara dari server Telegram tanpa crash / log berlebih."""
        err = context.error
        if isinstance(err, (NetworkError, TimedOut)):
            logger.warning(f"⚠️ [Telegram Network] Gangguan sementara ke api.telegram.org ({err}). Bot otomatis melakukan auto-retry...")
            return
        if isinstance(err, RetryAfter):
            logger.warning(f"⏳ [Telegram Rate Limit] Flood control: Menunggu {err.retry_after}s...")
            return
        logger.error(f"Telegram Exception: {err}", exc_info=err)

    app.add_error_handler(on_telegram_error)

    # Register command handlers (khusus owner)
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("ping", cmd_ping))
    app.add_handler(CommandHandler("myid", cmd_myid))
    app.add_handler(CommandHandler("setowner", cmd_setowner))
    app.add_handler(CommandHandler("filenomor", cmd_filenomor))
    app.add_handler(CommandHandler("getnumbers", cmd_filenomor))
    app.add_handler(CommandHandler("numbers", cmd_filenomor))

    # Register message handler untuk private chat (tolak input dari non-owner)
    app.add_handler(MessageHandler(filters.ChatType.PRIVATE & ~filters.COMMAND, handle_private_messages))

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
