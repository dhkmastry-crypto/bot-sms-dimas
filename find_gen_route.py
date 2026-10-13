import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
m = re.search(r'name="_token" value="([^"]+)"', r.text)
token = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': token, 'email': 'Ekiprijipratama03@gmail.com', 'password': 'Ciparay024'})
print('Login status:', resp.status_code, 'URL:', resp.url)

if resp.status_code == 200 and '/login' not in resp.url:
    doc = scraper.get('https://augestel.com/Switchfy/api/documentation')
    print('Doc status:', doc.status_code, 'Len:', len(doc.text))
    with open('doc_dump.html', 'w', encoding='utf-8') as f:
        f.write(doc.text)
    print('Saved doc_dump.html!')
    
    # Search for all scripts and functions
    for match in re.finditer(r'generateApiKey', doc.text):
        idx = match.start()
        print('--- generateApiKey match ---')
        print(doc.text[max(0, idx-200):min(len(doc.text), idx+400)])
else:
    print('Failed to log in.')
