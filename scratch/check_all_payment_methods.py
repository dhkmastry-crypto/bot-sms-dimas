import requests
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

s = requests.Session()
login_res = s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
if login_res.status_code != 200:
    print("Failed to login to admin server!")
    sys.exit(1)

with open("augestel_accounts.json", "r", encoding="utf-8") as f:
    accounts = json.load(f)

print(f"Checking all {len(accounts)} accounts in pool...")

status_report = []

for idx in range(1, len(accounts) + 1):
    acc = accounts[idx - 1]
    email = acc["email"]

    # Check current URL
    res = s.post(f"http://localhost:5000/api/augestel/pool/eval/{idx}", json={"script": "window.location.href"})
    data = res.json()
    if not data.get("success"):
        print(f"[#{idx:02d}] {email} -> Error: {data.get('message') or data.get('error')}")
        status_report.append({"idx": idx, "email": email, "state": "error", "error": data.get("error") or data.get("message")})
        continue

    curr_url = data.get("result", "")
    print(f"[#{idx:02d}] {email} -> URL: {curr_url}")
    status_report.append({"idx": idx, "email": email, "state": "ok", "url": curr_url})

print("\nSummary:")
ok_count = sum(1 for x in status_report if x["state"] == "ok")
err_count = len(status_report) - ok_count
print(f"Total: {len(status_report)} | Active Pages in Pool: {ok_count} | Errored/Closed: {err_count}")
