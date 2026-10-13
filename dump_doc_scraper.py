import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
m = re.search(r'name="_token" value="([^"]+)"', r.text)
csrf = m.group(1) if m else ''

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': csrf, 'email': 'saputradimas0878@gmail.com', 'password': 'dimas098.'})
print('Login status:', resp.status_code, 'URL:', resp.url)

if resp.status_code == 200 and '/login' not in resp.url:
    doc = scraper.get('https://augestel.com/Switchfy/api/documentation')
    print('Doc status:', doc.status_code, 'Len:', len(doc.text))
    
    # Save full text
    with open('full_doc.html', 'w', encoding='utf-8') as f:
        f.write(doc.text)
    print('Saved full_doc.html')

    # Search for all occurrences of "regenerate", "delete", "apiKey", "api-key"
    for word in ['regenerateApiKey', 'deleteApiKey', 'generateApiKey', 'copyApiKey']:
        for m in re.finditer(re.escape(word), doc.text):
            idx = m.start()
            print(f'=== Found {word} at {idx} ===')
            print(doc.text[max(0, idx-100):min(len(doc.text), idx+400)])
else:
    print('Login failed! Headers:', resp.headers.get('Retry-After'))
