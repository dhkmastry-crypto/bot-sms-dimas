import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
m = re.search(r'name="_token" value="([^"]+)"', r.text)
token = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': token, 'email': 'saputradimas0878@gmail.com', 'password': 'dimas098.'})
print('Login status:', resp.status_code, 'URL:', resp.url)

if resp.status_code == 200 and '/login' not in resp.url:
    doc = scraper.get('https://augestel.com/Switchfy/api/documentation')
    print('Doc status:', doc.status_code, 'Length:', len(doc.text))
    with open('real_doc_page.html', 'w', encoding='utf-8') as f:
        f.write(doc.text)
    print('Saved real_doc_page.html!')
else:
    print('Failed to log in:', resp.status_code)
    if 'Retry-After' in resp.headers:
        print('Retry-After:', resp.headers['Retry-After'])
