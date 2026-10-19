import requests

s = requests.Session()
s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
res = s.get("http://localhost:5000/api/augestel/webhooks/status")
data = res.json()
print("Guardian accounts:", len(data.get("guardian_accounts", {})))
for k, v in list(data.get("guardian_accounts", {}).items())[:5]:
    print(k, v)
