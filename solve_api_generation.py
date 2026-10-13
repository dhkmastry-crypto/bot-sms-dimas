import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
m = re.search(r'name="_token" value="([^"]+)"', r.text)
csrf = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': csrf, 'email': 'Ekiprijipratama03@gmail.com', 'password': 'Ciparay024'})
print('Login status:', resp.status_code, 'URL:', resp.url)

if resp.status_code == 200 and '/login' not in resp.url:
    doc = scraper.get('https://augestel.com/Switchfy/api/documentation')
    print('Doc status:', doc.status_code, 'Len:', len(doc.text))
    with open('doc_eki.html', 'w', encoding='utf-8') as f:
        f.write(doc.text)
    print('Successfully saved doc_eki.html!')
    
    # Check if sk_live is already there
    keys = re.findall(r'sk_live_[a-zA-Z0-9_\-]+', doc.text)
    print('Keys already in doc:', keys)
    
    # Find all occurrences of generate or apiKey
    for m in re.finditer(r'generateApiKey', doc.text):
        idx = m.start()
        print('generateApiKey at', idx)
        print(doc.text[max(0, idx-300):min(len(doc.text), idx+500)])
else:
    print('Login failed! Status:', resp.status_code)
