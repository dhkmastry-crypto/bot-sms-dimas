import cloudscraper
import re
import json

with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
    accs = json.load(f)

acc = accs[0]
email = acc['email']
pwd = acc['password']
print(f"Testing login for {email}...")

scraper = cloudscraper.create_scraper()
login_page = scraper.get('https://augestel.com/Switchfy', timeout=15)
match = re.search(r'name="_token" value="([^"]+)"', login_page.text)
csrf_token = match.group(1) if match else ''

post_data = {'_token': csrf_token, 'email': email, 'password': pwd}
headers = {'Referer': 'https://augestel.com/Switchfy', 'Origin': 'https://augestel.com'}
login_resp = scraper.post('https://augestel.com/Switchfy/login', data=post_data, headers=headers, timeout=15)
print('Login URL:', login_resp.url, 'Status:', login_resp.status_code)

test_resp = scraper.get('https://augestel.com/Switchfy/test/numbers', timeout=20)
print('Numbers page status:', test_resp.status_code, 'Final URL:', test_resp.url)
print('Title:', re.findall(r'<title>(.*?)</title>', test_resp.text, re.IGNORECASE))
print('Length of HTML:', len(test_resp.text))

with open('debug_switchfy_numbers.html', 'w', encoding='utf-8') as f:
    f.write(test_resp.text)
print('Saved to debug_switchfy_numbers.html')
