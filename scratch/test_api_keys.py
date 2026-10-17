import json

with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
    accs = json.load(f)

print('Total accounts:', len(accs))
with_keys = [a for a in accs if a.get('api_key') and a.get('api_key').startswith('sk_live_')]
print('Accounts with valid api_key:', len(with_keys))
for i, a in enumerate(accs, 1):
    k = a.get('api_key') or ''
    masked_k = (k[:10] + '...') if k else 'NO_KEY'
    print(f"#{i}: {a.get('email')}: {masked_k}")
