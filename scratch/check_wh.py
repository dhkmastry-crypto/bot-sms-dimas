import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

s = requests.Session()
s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"}, timeout=10)

res = s.get("http://localhost:5000/api/augestel/internal-guardian-status", timeout=15)
data = res.json()
guardian = data.get("guardian", {})

print(f"{'No':<4} | {'Email':<34} | {'Active':<7} | {'Delivering':<11} | {'Paused':<7} | {'Status'}")
print("-" * 85)

all_ready = True
for k in sorted(guardian.keys(), key=lambda x: int(x)):
    v = guardian[k]
    email = v.get("email", "-")
    is_act = v.get("is_active", False)
    is_del = v.get("is_delivering", False)
    is_pau = v.get("is_paused", False)
    status = v.get("status", "-")
    url = v.get("url", "-")
    
    if not is_act or not is_del or is_pau:
        all_ready = False

    print(f"#{int(k):<3} | {email:<34} | {str(is_act):<7} | {str(is_del):<11} | {str(is_pau):<7} | {status}")

print("-" * 85)
print(f"Total Accounts Monitored: {len(guardian)}")
print(f"All Active & Delivering (Ready for OTP): {all_ready}")
