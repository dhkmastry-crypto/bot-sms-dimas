import asyncio
import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

session = requests.Session()
login_res = session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
print("Admin login:", login_res.status_code)

# Check pool status
res = session.get("http://localhost:5000/api/augestel/status")
if res.status_code == 200:
    st = res.json().get("pool_status", {})
    print(f"Pool status tracking {len(st)} accounts.")
    active_pages = [k for k, v in st.items() if v.get("logged_in")]
    print(f"Logged in accounts: {len(active_pages)}")
else:
    print("Failed to get pool status:", res.status_code)
