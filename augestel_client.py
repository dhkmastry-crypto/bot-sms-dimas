# ═══════════════════════════════════════════════════════════════
#  AUGESTEL CLIENT - Monitor OTP & Numbers dari https://augestel.com
# ═══════════════════════════════════════════════════════════════

import logging
import requests
import re
import hashlib
import time
import datetime
from ivasms_scraper import (
    get_country_from_phone,
    mask_phone_number,
    detect_platform,
    extract_otp,
    COUNTRY_FLAGS
)

logger = logging.getLogger(__name__)


class AugestelClient:
    """
    Client resmi untuk konsumsi REST API Augestel (https://augestel.com/api/v1/iprn)
    Endpoints:
      - GET /messages (EDR - Event Detail Records / SMS Masuk)
      - GET /numbers (Assigned premium rate numbers)
      - GET /statistics (Earnings & summary stats)
    """

    def __init__(
        self,
        api_key: str = "sk_live_FacL1Nd9nZLCYUK317e456JPVEZaNnAGlwWXY8fS",
        base_url: str = "https://augestel.com/api/v1/iprn",
        email: str = "saputradimas0878@gmail.com",
    ):
        self.api_key = api_key.strip()
        self.base_url = base_url.rstrip("/")
        self.email = email
        self.seen_ids = set()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
        })
        if self.api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {self.api_key}",
            })

    def check_connection(self) -> bool:
        """Cek apakah API Augestel dapat diakses dan API Key valid."""
        try:
            url = f"{self.base_url}/numbers"
            params = {"per_page": 1}
            r = self.session.get(url, params=params, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return data.get("success") is True
            elif r.status_code == 429:
                # Rate limited but key is valid
                return True
            return False
        except Exception as e:
            logger.error(f"Augestel check connection failed: {e}")
            return False

    def get_all_sms(self, per_page: int = 100) -> list:
        """
        Ambil pesan dari endpoint /messages dan format agar kompatibel 100%
        dengan Telegram bot dan dashboard.
        """
        all_sms = []
        try:
            url = f"{self.base_url}/messages"
            # Sertakan start_date kemarin agar mencakup seluruh pesan aktif
            yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
            params = {
                "start_date": yesterday,
                "per_page": per_page,
                "page": 1,
            }
            r = self.session.get(url, params=params, timeout=15)
            if r.status_code == 429:
                retry_after = r.json().get("error", {}).get("retry_after", 15)
                logger.warning(f"Augestel rate limit (429), retry after {retry_after}s")
                return []
            if r.status_code != 200:
                logger.error(f"Augestel /messages returned HTTP {r.status_code}: {r.text[:200]}")
                return []

            res_json = r.json()
            items = res_json.get("data", [])
            for item in items:
                phone_num = str(item.get("number", "")).strip()
                source_sender = str(item.get("source", "")).strip()
                message = str(item.get("message", "")).strip()
                received_at = str(item.get("received_at", "")).strip()
                rate_val = item.get("rate", 0.0)
                try:
                    rev_str = f"${float(rate_val):.4f}" if float(rate_val) > 0 else "$0.00"
                except Exception:
                    rev_str = "$0.00"

                phone_cc, phone_flag = get_country_from_phone(phone_num)

                otp = extract_otp(message)
                platform, p_emoji = detect_platform(source_sender)
                if platform == "SMS":
                    platform, p_emoji = detect_platform(message)

                # Generate ID unik stabil menggunakan SHA256 / format gabungan
                sms_id = "aug_" + hashlib.sha256(
                    f"{phone_num}|{received_at}|{source_sender}|{message}".encode("utf-8")
                ).hexdigest()[:16]

                all_sms.append({
                    "id": sms_id,
                    "phone": phone_num,
                    "phone_masked": mask_phone_number(phone_num),
                    "sender": source_sender or "Augestel",
                    "message": message,
                    "otp": otp,
                    "platform": platform,
                    "platform_emoji": p_emoji,
                    "country_code": phone_cc,
                    "flag": phone_flag,
                    "timestamp": received_at,
                    "revenue": rev_str,
                    "rate": rate_val,
                    "range_name": item.get("range_name", "Augestel IPRN"),
                    "source": "Augestel",
                })
        except Exception as e:
            logger.error(f"Error fetching Augestel data: {e}")

        return all_sms

    def get_new_sms(self, per_page: int = 100) -> list:
        """Ambil hanya SMS baru yang belum pernah dikirim."""
        all_sms = self.get_all_sms(per_page=per_page)
        new_sms = []
        for sms in all_sms:
            if sms["id"] not in self.seen_ids:
                self.seen_ids.add(sms["id"])
                new_sms.append(sms)

        if new_sms:
            logger.info(f"Augestel: Found {len(new_sms)} new SMS")
        return new_sms

    def mark_initial_as_seen(self) -> int:
        """Tandai SMS yang ada saat startup agar tidak membanjiri notifikasi awal."""
        all_sms = self.get_all_sms(per_page=100)
        for sms in all_sms:
            self.seen_ids.add(sms["id"])
        logger.info(f"Augestel: Marked {len(all_sms)} initial SMS as seen")
        return len(all_sms)

    def get_numbers(self, page: int = 1, per_page: int = 100) -> dict:
        """Ambil daftar nomor aktif dari Augestel dengan auto-retry jika 429."""
        url = f"{self.base_url}/numbers"
        params = {"page": page, "per_page": min(per_page, 100)}
        for attempt in range(4):
            try:
                r = self.session.get(url, params=params, timeout=15)
                if r.status_code == 200:
                    return r.json()
                elif r.status_code == 429:
                    retry_sec = 13
                    try:
                        hdr = r.headers.get("Retry-After")
                        if hdr and hdr.isdigit():
                            retry_sec = max(int(hdr), 13)
                    except Exception:
                        pass
                    logger.info(f"Augestel API rate limited (429). Menunggu {retry_sec} detik...")
                    time.sleep(retry_sec)
                    continue
                return {"success": False, "message": f"HTTP {r.status_code}"}
            except Exception as e:
                logger.error(f"Error fetching Augestel numbers: {e}")
                return {"success": False, "message": str(e)}
        return {"success": False, "message": "Rate limited after retries"}

    def get_all_numbers_list(self, max_records: int = 50000) -> list:
        """Ambil seluruh daftar nomor Augestel dengan auto-paging hingga tuntas (tanpa batas 200)."""
        all_numbers = []
        page = 1
        per_page = 100
        while len(all_numbers) < max_records:
            res = self.get_numbers(page=page, per_page=per_page)
            if not res.get("success"):
                break
            items = res.get("data", [])
            if not items:
                break
            for item in items:
                num_str = str(item.get("number", "")).strip()
                rate_val = item.get("a2p_rate", 0.0)
                all_numbers.append({
                    "Number": num_str,
                    "range": item.get("range_name", "Augestel"),
                    "A2P": f"${rate_val:.4f}" if isinstance(rate_val, (int, float)) else str(rate_val),
                    "a2p_rate": rate_val,
                    "P2P": "$0.0000",
                    "Voice": "-",
                    "limit_a2p": item.get("portal_limit_a2p", 0),
                    "last_message": item.get("last_message_at") or "-",
                    "provider": "Augestel",
                })
            pagination = res.get("pagination", {})
            last_page = pagination.get("last_page", 1)
            if page >= last_page:
                break
            page += 1
            time.sleep(1)

        return all_numbers


    def get_statistics(self) -> dict:
        """Ambil ringkasan statistik dan earning dari Augestel."""
        try:
            url = f"{self.base_url}/statistics"
            r = self.session.get(url, timeout=15)
            if r.status_code == 200:
                return r.json()
            return {}
        except Exception as e:
            logger.error(f"Error fetching Augestel statistics: {e}")
            return {}

    @classmethod
    def login_and_extract_api_key(cls, email: str, password: str) -> dict:
        """
        Login otomatis ke portal Augestel (Switchfy) menggunakan email & password,
        lalu mengekstrak API Key (sk_live_...) secara otomatis tanpa input manual.
        """
        import cloudscraper
        scraper = cloudscraper.create_scraper()
        email = (email or "").strip()
        password = (password or "").strip()

        if not email or not password:
            return {"success": False, "message": "Email dan password Augestel wajib diisi!"}

        # Optimasi 1: Cek apakah akun ini sudah pernah memiliki API Key yang valid di config / json
        try:
            import json, os
            acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
            if os.path.exists(acc_file):
                with open(acc_file, "r", encoding="utf-8") as f:
                    saved_accs = json.load(f)
                    for a in saved_accs:
                        if a.get("email", "").lower() == email.lower() and a.get("api_key"):
                            # Verifikasi cepat apakah key masih aktif (hanya ~300ms)
                            test_client = cls(api_key=a["api_key"])
                            if test_client.check_connection():
                                return {
                                    "success": True,
                                    "api_key": a["api_key"],
                                    "email": email,
                                    "message": "API Key valid terverifikasi secara instan!"
                                }
        except Exception:
            pass

        for attempt in range(2):
            try:
                # 1. Buka halaman login untuk mengambil CSRF token (cepat: ~1s)
                login_page = scraper.get("https://augestel.com/Switchfy", timeout=12)
                if login_page.status_code != 200:
                    return {"success": False, "message": f"Gagal mengakses portal Augestel (HTTP {login_page.status_code})"}

                match = re.search(r'name="_token" value="([^"]+)"', login_page.text)
                csrf_token = match.group(1) if match else ""
                if not csrf_token:
                    return {"success": False, "message": "CSRF Token portal Augestel tidak ditemukan."}

                # 2. Kirim kredensial login
                post_data = {
                    "_token": csrf_token,
                    "email": email,
                    "password": password
                }
                headers = {
                    "Referer": "https://augestel.com/Switchfy",
                    "Origin": "https://augestel.com",
                }
                login_resp = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers, timeout=12)

                # Jika terkena Cloudflare rate-limit pada form login (tunggu minimal tanpa delay berlebih)
                if login_resp.status_code == 429:
                    retry_sec = 10
                    try:
                        hdr = login_resp.headers.get("Retry-After")
                        if hdr and hdr.isdigit():
                            retry_sec = min(int(hdr), 20)
                    except Exception:
                        pass
                    logger.warning(f"Login rate limited (429), menunggu {retry_sec} detik...")
                    time.sleep(retry_sec)
                    continue

                # Cek jika login gagal (terlempar kembali ke login atau pesan error kredensial)
                if "invalid" in login_resp.text.lower() or "credentials" in login_resp.text.lower() or "login" in login_resp.url.lower():
                    # Jika URL tetap di login
                    if "/login" in login_resp.url and login_resp.status_code == 200:
                        return {"success": False, "message": "Email atau password Augestel salah! Silakan periksa kembali."}

                # 3. Kunjungi halaman Developer -> SMS API (https://augestel.com/Switchfy/api/documentation)
                doc_resp = scraper.get("https://augestel.com/Switchfy/api/documentation", headers={"Referer": login_resp.url}, timeout=20)
                if doc_resp.status_code == 200:
                    keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc_resp.text)
                    if keys:
                        api_key = keys[0]
                        logger.info(f"Berhasil mendeteksi API Key Augestel untuk {email}: {api_key[:12]}...")
                        return {
                            "success": True,
                            "api_key": api_key,
                            "email": email,
                            "message": "Login berhasil & API Key otomatis terdeteksi!"
                        }

                # Fallback: Cari di halaman Webhooks atau EDR history jika ada
                wh_resp = scraper.get("https://augestel.com/Switchfy/api/webhooks", headers={"Referer": login_resp.url}, timeout=15)
                if wh_resp.status_code == 200:
                    keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", wh_resp.text)
                    if keys:
                        api_key = keys[0]
                        return {
                            "success": True,
                            "api_key": api_key,
                            "email": email,
                            "message": "Login berhasil & API Key otomatis terdeteksi!"
                        }

                return {
                    "success": True,
                    "api_key": "",
                    "email": email,
                    "login_ok": True,
                    "message": "Login berhasil! Namun API Key (sk_live_...) belum di-generate di portal https://augestel.com/Switchfy/api/documentation."
                }

            except Exception as e:
                logger.error(f"Error login & extract API key Augestel: {e}")
                return {"success": False, "message": f"Terjadi kesalahan saat login: {e}"}

        return {"success": False, "message": "Gagal login ke Augestel setelah beberapa percobaan."}

