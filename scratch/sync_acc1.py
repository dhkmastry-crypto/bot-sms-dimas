import time
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from augestel_client import AugestelClient
from numbers_service import get_augestel_accounts, _format_augestel_number_item

accounts = get_augestel_accounts()
acc1 = accounts[0]
client = AugestelClient(api_key=acc1['api_key'], email=acc1['email'])

cache_file = os.path.join(os.path.dirname(__file__), '..', 'augestel_numbers_cache_1.json')
all_items = []

res1 = client.get_numbers(page=1, per_page=100, auto_retry=True)
if not res1.get('success'):
    print('Failed page 1:', res1)
    sys.exit(1)

total = res1.get('pagination', {}).get('total', 2010)
last_page = res1.get('pagination', {}).get('last_page', 21)
all_items.extend(res1.get('data', []))
print(f'Page 1/{last_page} ok ({len(res1.get("data", []))} items). Total: {total}')

for p in range(2, last_page + 1):
    for attempt in range(5):
        res = client.get_numbers(page=p, per_page=100, auto_retry=True)
        if res.get('success'):
            data = res.get('data', [])
            all_items.extend(data)
            print(f'Page {p}/{last_page} ok (+{len(data)} items). Total collected: {len(all_items)}/{total}')
            break
        else:
            print(f'Page {p} attempt {attempt+1} failed: {res.get("message")}. Waiting 15s...')
            time.sleep(15)
    time.sleep(3)

formatted = [_format_augestel_number_item(it, idx, 1, acc1['email']) for idx, it in enumerate(all_items, 1)]

result = {
    'success': True,
    'account_index': 'aug_1',
    'email': f"Augestel #1 ({acc1['email']})",
    'total': total,
    'count': len(formatted),
    'numbers': formatted,
    'cached_at': time.strftime('%Y-%m-%d %H:%M:%S')
}

with open(cache_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2)

print('Done writing cache 1! Total numbers in cache:', len(formatted))
