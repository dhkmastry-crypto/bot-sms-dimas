import cloudscraper

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
import re
m = re.search(r'name="_token" value="([^"]+)"', r.text)
token = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': token, 'email': 'Ekiprijipratama03@gmail.com', 'password': 'Ciparay024'})
print('Status:', resp.status_code)
for k, v in resp.headers.items():
    if any(x in k.lower() for x in ['retry', 'rate', 'limit', 'cf']):
        print(f'{k}: {v}')
