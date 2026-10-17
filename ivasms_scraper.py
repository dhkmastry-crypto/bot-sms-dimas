# ═══════════════════════════════════════════════════════════════
#  IVASMS SCRAPER (DEPRECATED & RE-EXPORT COMPATIBILITY LAYER)
#  Platform IVASMS telah dinonaktifkan/dihapus per permintaan user.
#  Semua utilitas OTP, kode negara, platform & regex diekspor dari otp_utils.
# ═══════════════════════════════════════════════════════════════

import logging
from otp_utils import (
    COUNTRY_FLAGS,
    PHONE_PREFIX_TO_COUNTRY,
    COUNTRY_NAME_TO_CODE,
    get_country_from_phone,
    get_country_from_range_name,
    mask_phone_number,
    detect_platform,
    extract_otp,
)

logger = logging.getLogger(__name__)


class IVASMSClient:
    """
    Stub kompatibilitas untuk IVASMSClient (Platform IVASMS telah dinonaktifkan).
    Semua method mengembalikan nilai aman (no-op) agar tidak merusak import lama.
    """

    def __init__(self, cookies=None, base_url="https://www.ivasms.com"):
        self.base_url = base_url
        self.seen_ids = set()

    def update_cookies(self, cookies):
        pass

    def check_connection(self) -> bool:
        return False

    def mark_initial_as_seen(self) -> int:
        return 0

    def get_latest_sms(self) -> list:
        return []
