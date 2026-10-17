import requests

s = requests.Session()
# Login
r_log = s.post('http://localhost:5000/login', data={'username': 'admin', 'password': 'password123'})
print('Login status:', r_log.status_code)

# Test earnings API
r_earn = s.get('http://localhost:5000/api/augestel/earnings')
print('Earnings API status:', r_earn.status_code)
if r_earn.status_code == 200:
    data = r_earn.json()
    d = data.get('data', {})
    print('SUCCESS:', data.get('success'))
    print('TOTAL USD:', d.get('total_revenue_usd'))
    print('TOTAL IDR:', d.get('total_revenue_idr'))
    print('TOTAL SMS:', d.get('total_sms'))
    print('TODAY USD:', d.get('today_revenue_usd'))
    print('ACCOUNTS COUNT:', len(d.get('by_account', {})))
    print('DAILY BREAKDOWN COUNT:', len(d.get('daily_breakdown', [])))
    print('TOP NUMBERS COUNT:', len(d.get('top_numbers', [])))
    print('LAST API SYNC:', d.get('last_api_sync'))
    print('SYNC SOURCE:', d.get('sync_source'))
else:
    print('Response:', r_earn.text[:400])
