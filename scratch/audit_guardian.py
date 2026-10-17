import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

session = requests.Session()
session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

# Let's inspect status from admin_server
res = session.get("http://localhost:5000/api/augestel/webhooks/status")
if res.status_code == 200:
    data = res.json()
    ga = data.get("guardian_accounts", {})
    print(f"Guardian is tracking {len(ga)} accounts:")
    for k, v in sorted(ga.items(), key=lambda x: int(x[0])):
        idx = int(k)
        print(f"#{idx:02d} ({v.get('email')}): status={v.get('status')}, active={v.get('is_active')}, url={v.get('url')}")
else:
    print("Error:", res.status_code, res.text)
