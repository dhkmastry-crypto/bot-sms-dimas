import urllib.request
import json
import sys

idx = int(sys.argv[1]) if len(sys.argv) > 1 else 10

req = urllib.request.Request(
    f"http://localhost:5000/api/augestel/pool/show/{idx}",
    headers={"X-Internal-Token": "bot-internal-secret"},
    data=b"{}",
    method="POST"
)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Show Window Result for Acc #{idx}:", json.dumps(res, indent=2))
except Exception as e:
    print("Error:", e)
