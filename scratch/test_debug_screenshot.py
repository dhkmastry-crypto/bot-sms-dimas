import requests
import time
import json
import os

session = requests.Session()
r = session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
print("Login status:", r.status_code)

idx = 1
print(f"1. Navigating tab #{idx} to /Switchfy/api/webhooks...")
r_eval = session.post(f"http://localhost:5000/api/augestel/pool/eval/{idx}", json={"script": "window.location.href = '/Switchfy/api/webhooks'; 'navigating';"})
print("Eval response:", r_eval.status_code, r_eval.json())

print("2. Waiting 3 seconds for page to load...")
time.sleep(3)

print(f"3. Calling debug endpoint to take full-page screenshot...")
r_debug = session.get(f"http://localhost:5000/api/augestel/pool/debug/{idx}")
print("Debug response:", r_debug.status_code)
data = r_debug.json()
print("URL:", data.get("data", {}).get("url"))
print("Title:", data.get("data", {}).get("title"))
print("Screenshot path:", data.get("data", {}).get("form_info", {}).get("screenshot"))
