import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

session = requests.Session()
login_res = session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
print("Login status:", login_res.status_code)

target_url = "https://dimsong.online/api/augestel/webhook"

for idx in [31, 32]:
    print(f"\n--- Setting up Account #{idx} ---")
    res = session.post("http://localhost:5000/api/augestel/webhooks/setup-single", json={"index": idx, "webhook_url": target_url}, timeout=120)
    print("Response status:", res.status_code)
    try:
        print("Response body:", res.json())
    except Exception:
        print("Raw body:", res.text[:300])

print("\n--- Verifying Guardian Status ---")
res2 = session.get("http://localhost:5000/api/augestel/webhooks/status")
if res2.status_code == 200:
    ga = res2.json().get("guardian_accounts", {})
    for idx in [31, 32]:
        info = ga.get(str(idx), {})
        print(f"Account #{idx}: delivering={info.get('is_delivering')}, active={info.get('is_active')}, url={info.get('url')}, status={info.get('status')}")
