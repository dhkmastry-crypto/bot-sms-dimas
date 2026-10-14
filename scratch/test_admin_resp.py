import urllib.request
import json

req = urllib.request.Request(
    'http://localhost:5000/api/augestel/accounts',
    headers={'X-Internal-Token': 'bot-internal-secret'}
)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        accs = data.get('accounts', [])
        print(f"Total accounts in admin server: {len(accs)}")
        for i, a in enumerate(accs, 1):
            if i >= 10:
                print(f"Acc #{i}: {a.get('email')} | pwd: {a.get('password')}")
except Exception as e:
    print('Error:', e)
