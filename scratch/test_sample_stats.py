import json, requests, time

with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
    accs = json.load(f)

for i in range(5):
    a = accs[i]
    headers = {'Authorization': f"Bearer {a['api_key']}", 'Accept': 'application/json'}
    try:
        r = requests.get('https://augestel.com/api/v1/iprn/statistics', headers=headers, timeout=10)
        if r.status_code == 200:
            d = r.json()
            summ = d.get('summary', {})
            print(f"#{i+1} ({a['email']}): messages={summ.get('total_messages')} earnings=${summ.get('total_earnings')}")
        else:
            print(f"#{i+1} ({a['email']}): status {r.status_code}")
    except Exception as e:
        print(f"#{i+1}: error {e}")
    time.sleep(1)
