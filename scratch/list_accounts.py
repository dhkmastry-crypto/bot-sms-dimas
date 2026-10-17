import json
accs = json.load(open('augestel_accounts.json', encoding='utf-8'))
print(f"Total accounts in file: {len(accs)}")
for i, a in enumerate(accs, 1):
    print(f"#{i:02d}: {a.get('email')}")
