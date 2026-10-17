# ═══════════════════════════════════════════════════════════════
#  COOKIE SYNC (DEPRECATED - IVASMS PLATFORM TELAH DINONAKTIFKAN)
# ═══════════════════════════════════════════════════════════════

import logging

logger = logging.getLogger(__name__)


async def get_fresh_cookies_from_browser(account_index: int = 1, email: str = "", password: str = "") -> dict:
    """Stub kompatibilitas: IVASMS dinonaktifkan."""
    return {}


def sync_cookies_to_config(cookies: dict) -> bool:
    """Stub kompatibilitas: IVASMS dinonaktifkan."""
    return True
