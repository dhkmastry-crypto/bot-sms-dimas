import os
import sys
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from augestel_client import AugestelClient

with open("augestel_accounts.json", "r", encoding="utf-8") as f:
    accs = json.load(f)

for i, a in enumerate(accs, 1):
    email = a.get("email", "")
    key = a.get("api_key", "")
    if key:
        c = AugestelClient(api_key=key, email=email)
        res = c.get_numbers(page=1, per_page=1)
        tot = res.get("pagination", {}).get("total", 0) if res.get("success") else f"Err: {res.get('message')}"
        print(f"Akun #{i:02d} ({email}): {tot} nomor")
    else:
        print(f"Akun #{i:02d} ({email}): Belum ada API Key")
