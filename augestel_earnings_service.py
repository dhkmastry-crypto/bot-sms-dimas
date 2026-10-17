# ═══════════════════════════════════════════════════════════════
#  AUGESTEL REVENUE & DAILY EARNINGS ANALYTICS SERVICE
#  ─────────────────────────────────────────────────────────────
#  Mengambil dan mengagregasi data analitik pendapatan (Revenue),
#  Traffic SMS harian, dan Nomor Ter-Cuan langsung dari REST API
#  resmi Augestel (GET /api/v1/iprn/statistics) untuk seluruh akun.
# ═══════════════════════════════════════════════════════════════

import os
import sys

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

import json
import time
import logging
import threading
import requests
from datetime import datetime

logger = logging.getLogger("augestel_earnings")
if not logger.handlers:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("%(asctime)s │ %(levelname)-8s │ [AugestelEarnings] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EARNINGS_FILE = os.path.join(BASE_DIR, "augestel_earnings.json")
EARNINGS_API_FILE = os.path.join(BASE_DIR, "augestel_earnings_api.json")
EARNINGS_WEBHOOK_FILE = os.path.join(BASE_DIR, "augestel_earnings_webhook.json")
ACCOUNTS_FILE = os.path.join(BASE_DIR, "augestel_accounts.json")
USD_TO_IDR_RATE = 16250.0

# State sinkronisasi API Augestel
_sync_lock = threading.Lock()
_sync_state = {
    "is_syncing": False,
    "current_account": 0,
    "total_accounts": 0,
    "progress_pct": 0,
    "current_email": "",
    "started_at": None,
    "finished_at": None,
    "last_error": None,
    "total_synced": 0,
}


def get_sync_state() -> dict:
    """Mengembalikan status live sinkronisasi API ke frontend."""
    return dict(_sync_state)


def fetch_account_statistics_api(api_key: str, timeout: int = 12) -> dict:
    """
    Memanggil endpoint resmi Augestel GET /api/v1/iprn/statistics
    untuk satu akun dengan bearer token api_key.
    """
    clean_key = (api_key or "").strip()
    if not clean_key:
        return {}

    url = "https://augestel.com/api/v1/iprn/statistics"
    headers = {
        "Authorization": f"Bearer {clean_key}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    params = {"group_by": "day"}

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=timeout)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("success"):
                return data
        elif resp.status_code == 429:
            logger.warning("⚠️ [Augestel API] Rate limit (429) hit, slowing down...")
            time.sleep(2.5)
        else:
            logger.debug(f"Augestel stats returned HTTP {resp.status_code}")
    except Exception as e:
        logger.error(f"Error calling Augestel /statistics: {e}")

    return {}


def _get_default_structure(source_name: str = "Augestel Official REST API") -> dict:
    return {
        "total_revenue_usd": 0.0,
        "total_revenue_idr": 0,
        "total_sms": 0,
        "today_date": datetime.now().strftime("%Y-%m-%d"),
        "today_revenue_usd": 0.0,
        "today_sms": 0,
        "yesterday_revenue_usd": 0.0,
        "yesterday_sms": 0,
        "by_account": {},
        "by_country": {},
        "by_platform": {},
        "daily_breakdown": [],
        "top_numbers": [],
        "last_api_sync": None,
        "last_event_time": None,
        "sync_source": source_name,
        "recent_transactions": []
    }


def load_api_earnings() -> dict:
    """Membaca data analitik pendapatan Versi REST API resmi."""
    target_f = EARNINGS_API_FILE if os.path.exists(EARNINGS_API_FILE) else EARNINGS_FILE
    default_d = _get_default_structure("Augestel Official REST API (v1/iprn/statistics)")
    if not os.path.exists(target_f):
        return default_d
    try:
        with open(target_f, "r", encoding="utf-8") as f:
            d = json.load(f)
            for k, v in default_d.items():
                if k not in d:
                    d[k] = v
            return d
    except Exception as e:
        logger.error(f"Error reading {target_f}: {e}")
        return default_d


def save_api_earnings(data: dict) -> bool:
    """Menyimpan data analitik pendapatan Versi REST API."""
    try:
        for fpath in (EARNINGS_API_FILE, EARNINGS_FILE):
            temp_file = fpath + ".tmp"
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            if os.path.exists(temp_file):
                os.replace(temp_file, fpath)
        return True
    except Exception as e:
        logger.error(f"Error saving api earnings: {e}")
        return False


def load_webhook_earnings() -> dict:
    """Membaca data analitik pendapatan Versi Real-Time Webhook."""
    default_d = _get_default_structure("Augestel Real-Time Webhook Engine (https://dimsong.online)")
    if not os.path.exists(EARNINGS_WEBHOOK_FILE):
        return default_d
    try:
        with open(EARNINGS_WEBHOOK_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
            for k, v in default_d.items():
                if k not in d:
                    d[k] = v
            return d
    except Exception as e:
        logger.error(f"Error reading {EARNINGS_WEBHOOK_FILE}: {e}")
        return default_d


def save_webhook_earnings(data: dict) -> bool:
    """Menyimpan data analitik pendapatan Versi Real-Time Webhook."""
    try:
        temp_file = EARNINGS_WEBHOOK_FILE + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        if os.path.exists(temp_file):
            os.replace(temp_file, EARNINGS_WEBHOOK_FILE)
        return True
    except Exception as e:
        logger.error(f"Error saving webhook earnings: {e}")
        return False


def load_augestel_earnings(mode: str = "api") -> dict:
    """
    Fungsi universal: Membaca data analitik Augestel berdasarkan mode pilihan:
    - 'api'     : Versi REST API resmi (default)
    - 'webhook' : Versi Real-Time Webhook
    """
    if str(mode).lower() == "webhook":
        return load_webhook_earnings()
    return load_api_earnings()


def save_augestel_earnings(data: dict, mode: str = "api") -> bool:
    """Menyimpan data analitik pendapatan ke target mode yang sesuai."""
    if str(mode).lower() == "webhook":
        return save_webhook_earnings(data)
    return save_api_earnings(data)


def sync_all_accounts_from_api(delay: float = 0.35) -> dict:
    """
    Menyinkronkan seluruh akun Augestel (1..32) langsung dari API resmi Augestel.
    Mengagregasi total cuan, traffic SMS harian, rincian akun, dan nomor ter-cuan.
    """
    global _sync_state

    if not os.path.exists(ACCOUNTS_FILE):
        return {"success": False, "message": "augestel_accounts.json tidak ditemukan"}

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            accounts = json.load(f)
    except Exception as e:
        return {"success": False, "message": f"Gagal membaca akun: {e}"}

    total_accs = len(accounts)
    if total_accs == 0:
        return {"success": False, "message": "Tidak ada akun Augestel yang terdaftar"}

    _sync_state["is_syncing"] = True
    _sync_state["total_accounts"] = total_accs
    _sync_state["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _sync_state["last_error"] = None
    _sync_state["total_synced"] = 0

    logger.info(f"🚀 [API Sync] Memulai sinkronisasi pendapatan dari Augestel API untuk {total_accs} akun...")

    # Struktur agregasi
    total_revenue_usd = 0.0
    total_sms = 0
    by_account = {}
    daily_map = {}
    merged_numbers_map = {}

    # Ambil data lama sebagai dasar fallback jika ada akun yang API-nya timeout
    old_data = load_augestel_earnings()
    old_by_acc = old_data.get("by_account", {})

    synced_count = 0
    for idx, acc in enumerate(accounts, 1):
        api_key = acc.get("api_key", "").strip()
        email = acc.get("email", f"Akun #{idx}").strip()

        _sync_state["current_account"] = idx
        _sync_state["current_email"] = email
        _sync_state["progress_pct"] = int((idx / total_accs) * 100)

        if not api_key:
            # Fallback jika akun belum ada key
            prev = old_by_acc.get(str(idx), {})
            by_account[str(idx)] = {
                "email": email,
                "sms": prev.get("sms", 0),
                "usd": prev.get("usd", 0.0),
                "idr": int(prev.get("usd", 0.0) * USD_TO_IDR_RATE),
                "api_connected": False,
                "top_numbers": prev.get("top_numbers", [])
            }
            continue

        stats_res = fetch_account_statistics_api(api_key)
        if stats_res and stats_res.get("success"):
            synced_count += 1
            summ = stats_res.get("summary", {})
            acc_sms = int(summ.get("total_messages", 0) or 0)
            acc_usd = round(float(summ.get("total_earnings", 0.0) or 0.0), 4)

            total_revenue_usd += acc_usd
            total_sms += acc_sms

            # Daily breakdown per akun
            for db in stats_res.get("daily_breakdown", []):
                p = str(db.get("period", "")).strip()
                if not p:
                    continue
                if p not in daily_map:
                    daily_map[p] = {"messages": 0, "earnings": 0.0, "delivered": 0}
                daily_map[p]["messages"] += int(db.get("messages", 0) or 0)
                daily_map[p]["delivered"] += int(db.get("delivered", 0) or 0)
                daily_map[p]["earnings"] = round(daily_map[p]["earnings"] + float(db.get("earnings", 0.0) or 0.0), 4)

            # Top numbers per akun
            top_nums = stats_res.get("top_numbers", [])
            for tn in top_nums:
                num = tn.get("number", "")
                if not num:
                    continue
                if num not in merged_numbers_map:
                    merged_numbers_map[num] = {
                        "number": num,
                        "range_name": tn.get("range_name", "Augestel IPRN"),
                        "messages": 0,
                        "earnings": 0.0,
                        "account": email
                    }
                merged_numbers_map[num]["messages"] += int(tn.get("messages", 0) or 0)
                merged_numbers_map[num]["earnings"] = round(merged_numbers_map[num]["earnings"] + float(tn.get("earnings", 0.0) or 0.0), 4)

            by_account[str(idx)] = {
                "email": email,
                "sms": acc_sms,
                "usd": acc_usd,
                "idr": int(acc_usd * USD_TO_IDR_RATE),
                "api_connected": True,
                "top_numbers": top_nums[:5]
            }
        else:
            # Jika panggilan API gagal atau 429, pertahankan nilai cache lama
            prev = old_by_acc.get(str(idx), {})
            prev_usd = float(prev.get("usd", 0.0) or 0.0)
            prev_sms = int(prev.get("sms", 0) or 0)
            total_revenue_usd += prev_usd
            total_sms += prev_sms
            by_account[str(idx)] = {
                "email": email,
                "sms": prev_sms,
                "usd": prev_usd,
                "idr": int(prev_usd * USD_TO_IDR_RATE),
                "api_connected": False,
                "top_numbers": prev.get("top_numbers", [])
            }

        # Jeda halus antar-akun agar Cloudflare/Augestel API aman
        time.sleep(delay)

    # Susun riwayat harian berurutan tanggal terbaru ke terlama
    daily_history = []
    for date_key in sorted(daily_map.keys(), reverse=True):
        entry = daily_map[date_key]
        entry["period"] = date_key
        entry["earnings_idr"] = int(entry["earnings"] * USD_TO_IDR_RATE)
        daily_history.append(entry)

    # Tentukan Today & Yesterday dari daily_history API
    today_revenue_usd = 0.0
    today_sms = 0
    yesterday_revenue_usd = 0.0
    yesterday_sms = 0

    if len(daily_history) >= 1:
        today_revenue_usd = daily_history[0].get("earnings", 0.0)
        today_sms = daily_history[0].get("messages", 0)
    if len(daily_history) >= 2:
        yesterday_revenue_usd = daily_history[1].get("earnings", 0.0)
        yesterday_sms = daily_history[1].get("messages", 0)

    # Top 20 nomor paling cuan across all accounts
    top_numbers = sorted(merged_numbers_map.values(), key=lambda x: -x["earnings"])[:20]

    final_data = {
        "total_revenue_usd": round(total_revenue_usd, 4),
        "total_revenue_idr": int(total_revenue_usd * USD_TO_IDR_RATE),
        "total_sms": total_sms,
        "today_date": datetime.now().strftime("%Y-%m-%d"),
        "today_revenue_usd": round(today_revenue_usd, 4),
        "today_sms": today_sms,
        "yesterday_revenue_usd": round(yesterday_revenue_usd, 4),
        "yesterday_sms": yesterday_sms,
        "by_account": by_account,
        "daily_breakdown": daily_history,
        "top_numbers": top_numbers,
        "by_country": old_data.get("by_country", {}),
        "by_platform": old_data.get("by_platform", {}),
        "recent_transactions": old_data.get("recent_transactions", []),
        "last_api_sync": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sync_source": "Augestel Official REST API (v1/iprn/statistics)",
        "total_accounts_synced": synced_count
    }

    save_augestel_earnings(final_data)

    _sync_state["is_syncing"] = False
    _sync_state["finished_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _sync_state["progress_pct"] = 100
    _sync_state["total_synced"] = synced_count

    logger.info(f"✅ [API Sync Selesai] Total Cuan: ${total_revenue_usd:.4f} (Rp {int(total_revenue_usd * USD_TO_IDR_RATE):,}) dari {synced_count}/{total_accs} Akun Augestel.")
    return {
        "success": True,
        "data": final_data,
        "synced_accounts": synced_count,
        "total_accounts": total_accs
    }


def trigger_background_api_sync() -> bool:
    """Memulai proses sinkronisasi API di thread latar belakang jika belum berjalan."""
    global _sync_state
    if _sync_state.get("is_syncing"):
        return False

    t = threading.Thread(target=sync_all_accounts_from_api, daemon=True)
    t.start()
    return True


def record_incremental_webhook_sms(account_idx=1, account_email="", rate_val=0.016, country_cc="ZW", country_flag="🇿🇼", platform="WhatsApp", phone=""):
    """
    Mencatat pertambahan cuan langsung saat ada event Webhook SMS masuk (real-time increment).
    Memperbarui store Versi Webhook dan store Versi API secara sinkron.
    """
    rate = float(rate_val or 0.016)
    if rate <= 0:
        rate = 0.016

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 1. Update Versi Webhook
    w = None
    try:
        w = load_webhook_earnings()
        w["total_sms"] = int(w.get("total_sms", 0)) + 1
        w["total_revenue_usd"] = round(float(w.get("total_revenue_usd", 0.0)) + rate, 4)
        w["total_revenue_idr"] = int(w["total_revenue_usd"] * USD_TO_IDR_RATE)

        if w.get("today_date") != today_str:
            w["yesterday_revenue_usd"] = w.get("today_revenue_usd", 0.0)
            w["yesterday_sms"] = w.get("today_sms", 0)
            w["today_date"] = today_str
            w["today_revenue_usd"] = 0.0
            w["today_sms"] = 0

        w["today_sms"] = int(w.get("today_sms", 0)) + 1
        w["today_revenue_usd"] = round(float(w.get("today_revenue_usd", 0.0)) + rate, 4)

        acc_key = str(account_email or f"Akun #{account_idx}")
        if acc_key not in w["by_account"]:
            w["by_account"][acc_key] = {"email": acc_key, "sms": 0, "usd": 0.0, "idr": 0}
        w["by_account"][acc_key]["sms"] += 1
        w["by_account"][acc_key]["usd"] = round(w["by_account"][acc_key]["usd"] + rate, 4)
        w["by_account"][acc_key]["idr"] = int(w["by_account"][acc_key]["usd"] * USD_TO_IDR_RATE)

        if "recent_transactions" not in w:
            w["recent_transactions"] = []
        w["recent_transactions"].insert(0, {
            "time": now_str,
            "account": acc_key,
            "phone": phone,
            "platform": platform,
            "flag": country_flag,
            "rate_usd": rate
        })
        w["recent_transactions"] = w["recent_transactions"][:30]
        w["last_event_time"] = now_str
        save_webhook_earnings(w)
    except Exception as e_w:
        logger.error(f"Error updating webhook earnings: {e_w}")

    # 2. Update Versi API (Inkremental agar real-time saat webhook tiba)
    try:
        a = load_api_earnings()
        a["total_sms"] = int(a.get("total_sms", 0)) + 1
        a["total_revenue_usd"] = round(float(a.get("total_revenue_usd", 0.0)) + rate, 4)
        a["total_revenue_idr"] = int(a["total_revenue_usd"] * USD_TO_IDR_RATE)
        a["today_sms"] = int(a.get("today_sms", 0)) + 1
        a["today_revenue_usd"] = round(float(a.get("today_revenue_usd", 0.0)) + rate, 4)

        acc_k = str(account_idx)
        if acc_k not in a["by_account"]:
            a["by_account"][acc_k] = {"email": account_email or f"Akun #{account_idx}", "sms": 0, "usd": 0.0, "idr": 0, "api_connected": True, "top_numbers": []}
        a["by_account"][acc_k]["sms"] += 1
        a["by_account"][acc_k]["usd"] = round(a["by_account"][acc_k]["usd"] + rate, 4)
        a["by_account"][acc_k]["idr"] = int(a["by_account"][acc_k]["usd"] * USD_TO_IDR_RATE)

        if "recent_transactions" not in a:
            a["recent_transactions"] = []
        a["recent_transactions"].insert(0, {
            "time": now_str,
            "account": f"Akun #{account_idx}",
            "phone": phone,
            "platform": platform,
            "flag": country_flag,
            "rate_usd": rate
        })
        a["recent_transactions"] = a["recent_transactions"][:30]
        save_api_earnings(a)
    except Exception as e_a:
        logger.error(f"Error updating api earnings: {e_a}")

    return w


def record_webhook_daily_summary(daily_usd: float, daily_sms: int):
    """Mencatat summary harian dari event webhook earnings.daily."""
    try:
        w = load_webhook_earnings()
        w["yesterday_revenue_usd"] = round(float(daily_usd or 0.0), 4)
        if daily_sms > 0:
            w["yesterday_sms"] = int(daily_sms)
        save_webhook_earnings(w)
    except Exception as e:
        logger.error(f"Error in record_webhook_daily_summary: {e}")

