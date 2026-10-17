import requests
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

session = requests.Session()
session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

# Let's inspect what pool has for account 32
# In admin_server.py:
# There is an endpoint /api/augestel/webhooks/setup-single or similar?
# Let's check admin_server.py routes for augestel webhooks
res = session.get("http://localhost:5000/api/augestel/webhooks/status")
data = res.json()
acc32 = data.get("guardian_accounts", {}).get("32", {})
print("Guardian data for #32:", acc32)
