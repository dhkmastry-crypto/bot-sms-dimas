import json, requests, time
from datetime import datetime

with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
    accs = json.load(f)

print(f"Starting test sync for {len(accs)} accounts...")
start_t = time.time()

total_revenue = 0.0
total_sms = 0
by_account = {}
daily_totals = {}

for idx, acc in enumerate(accs, 1):
    api_key = acc.get('api_key')
    email = acc.get('email', f'Akun #{idx}')
    if not api_key:
        continue
    
    headers = {'Authorization': f'Bearer {api_key}', 'Accept': 'application/json'}
    try:
        r = requests.get('https://augestel.com/api/v1/iprn/statistics', headers=headers, timeout=10)
        if r.status_code == 200:
            d = r.json()
            summ = d.get('summary', {})
            t_msg = summ.get('total_messages', 0)
            t_earn = float(summ.get('total_earnings', 0.0))
            total_revenue += t_earn
            total_sms += t_msg
            
            # daily
            for db in d.get('daily_breakdown', []):
                p = db.get('period')
                if p not in daily_totals:
                    daily_totals[p] = {'messages': 0, 'usd': 0.0}
                daily_totals[p]['messages'] += db.get('messages', 0)
                daily_totals[p]['usd'] = round(daily_totals[p]['usd'] + float(db.get('earnings', 0.0)), 4)
                
            by_account[str(idx)] = {
                'email': email,
                'sms': t_msg,
                'usd': round(t_earn, 4),
                'top_numbers': d.get('top_numbers', [])[:3]
            }
            print(f"[{idx}/32] {email}: {t_msg} SMS, ${t_earn:.4f}")
        elif r.status_code == 429:
            print(f"[{idx}/32] ⚠️ 429 Rate limit on {email}")
            time.sleep(3)
        else:
            print(f"[{idx}/32] Status {r.status_code} on {email}")
    except Exception as e:
        print(f"[{idx}/32] Error on {email}: {e}")
    time.sleep(0.4)

duration = time.time() - start_t
print(f"\nDone in {duration:.1f}s!")
print(f"Total Revenue USD: ${total_revenue:.4f} (≈ Rp {int(total_revenue * 16250):,})")
print(f"Total SMS: {total_sms}")
print("Daily Totals:", json.dumps(daily_totals, indent=2))
