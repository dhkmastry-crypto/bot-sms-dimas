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
        """Ambil daftar nomor aktif dari Augestel."""
        try:
            url = f"{self.base_url}/numbers"
            params = {"page": page, "per_page": min(per_page, 100)}
            r = self.session.get(url, params=params, timeout=15)
            if r.status_code == 200:
                return r.json()
            return {"success": False, "message": f"HTTP {r.status_code}"}
        except Exception as e:
            logger.error(f"Error fetching Augestel numbers: {e}")
            return {"success": False, "message": str(e)}

    def get_all_numbers_list(self, max_records: int = 1000) -> list:
        """Ambil seluruh daftar nomor Augestel dengan auto-paging."""
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
            if page >= pagination.get("last_page", 1):
                break
            page += 1
            time.sleep(0.5)  # Beri jeda kecil antar page

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
