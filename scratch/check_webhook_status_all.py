import os
import sys

BASE_DIR = r"c:\Users\ADMIN\Downloads\OTP IVA SMS"
sys.path.insert(0, BASE_DIR)

from augestel_browser_pool import get_browser_pool

pool = get_browser_pool()
print(f"Pool running: {pool.is_running}")
print(f"Total accounts in pool: {len(pool.accounts)}")
print(f"Target Webhook URL: {pool.webhook_url}")

# Ambil status guardian
status_map = pool.get_webhook_guardian_status()
print(f"Total tracked in guardian: {len(status_map)}")

for idx, data in sorted(status_map.items()):
    email = data.get("email", "")
    url = data.get("url", "")
    is_active = data.get("is_active", False)
    is_paused = data.get("is_paused", False)
    stat = data.get("status", "")
    print(f"Account #{idx:02d} ({email}): is_active={is_active}, is_paused={is_paused}, status={stat}, url={url}")
