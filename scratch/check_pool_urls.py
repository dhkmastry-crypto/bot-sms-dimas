import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

s = requests.Session()
s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

for idx in [1, 2, 3]:
    res = s.post(f"http://localhost:5000/api/augestel/pool/eval/{idx}", json={"script": "window.location.href"})
    print(f"Account #{idx} current URL:", res.json())
