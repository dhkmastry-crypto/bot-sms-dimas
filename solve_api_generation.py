import cloudscraper
import re
import time

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
m = re.search(r'name="_token" value="([^"]+)"', r.text)
csrf = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': csrf, 'email': 'Ekiprijipratama03@gmail.com', 'password': 'Ciparay024'})
print('Login status:', resp.status_code, 'URL:', resp.url)
print('Retry-After:', resp.headers.get('Retry-After'))
