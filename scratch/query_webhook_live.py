import requests
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

session = requests.Session()
login_res = session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
print("Login status:", login_res.status_code)

res = session.get("http://localhost:5000/api/augestel/webhooks/status")
print("Overview status:", res.status_code)
if res.status_code == 200:
    data = res.json()
    print("Target Webhook URL:", data.get("webhook_url"))
    print("Tunnel URL:", data.get("tunnel_url"))
    guardian_accs = data.get("guardian_accounts", {})
    print(f"Total Guardian Accounts Tracked: {len(guardian_accs)}")
    
    matches = 0
    mismatches = 0
    not_checked = 0
    target_wh = data.get("webhook_url")

    for k, v in sorted(guardian_accs.items(), key=lambda x: int(x[0])):
        idx = int(k)
        email = v.get("email", "")
        url = v.get("url", "")
        is_active = v.get("is_active", False)
        status = v.get("status", "")
        is_match = (url == target_wh)
        if is_match:
            matches += 1
            icon = "✅"
        elif not url:
            not_checked += 1
            icon = "⏳"
        else:
            mismatches += 1
            icon = "🔄"
        print(f"{icon} Akun #{idx:02d} ({email}) | active={is_active} | status={status} | url={url}")

    print("=" * 60)
    print(f"Ringkasan: {matches} cocok dengan dimsong.online, {mismatches} sedang diupdate, {not_checked} pending antrean")
else:
    print("Response text:", res.text[:300])
