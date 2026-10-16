import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from augestel_client import AugestelClient

with open("augestel_accounts.json", "r", encoding="utf-8") as f:
    accs = json.load(f)

print(f"Total akun di json: {len(accs)}")
for idx, acc in enumerate(accs, 1):
    email = acc.get("email", "")
    api_key = acc.get("api_key", "")
    client = AugestelClient(api_key=api_key, email=email)
    res = client.get_numbers(page=1, per_page=1)
    if res.get("success"):
        total = res.get("pagination", {}).get("total", len(res.get("data", [])))
        print(f"Akun #{idx:02d} ({email:<28}): {total:>5} nomor di portal")
    else:
        err = res.get("message", "Unknown error")
        print(f"Akun #{idx:02d} ({email:<28}): GAGAL ({err})")
