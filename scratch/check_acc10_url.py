import urllib.request
import json

req = urllib.request.Request(
    "http://localhost:5000/api/status",
    headers={"X-Internal-Token": "bot-internal-secret"}
)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        accs = data.get('augestel_accounts_status', [])
        for a in accs:
            if a.get('index') >= 10:
                print(f"Acc #{a.get('index')} ({a.get('email')}): active={a.get('is_pool_active')}, status={a.get('cookie_status')}, last_check={a.get('last_check')}")
except Exception as e:
    print("Error:", e)
