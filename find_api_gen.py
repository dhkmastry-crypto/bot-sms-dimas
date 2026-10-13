import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/Switchfy')
print('Get Switchfy status:', r.status_code, 'URL:', r.url)
m = re.search(r'name="_token" value="([^"]+)"', r.text)
token = m.group(1) if m else ''
print('Token:', token[:20])

resp = scraper.post('https://augestel.com/Switchfy/login', data={'_token': token, 'email': 'Ekiprijipratama03@gmail.com', 'password': 'Ciparay024'})
print('Login status:', resp.status_code, 'URL:', resp.url)
if '/login' in resp.url:
    # check error in html
    err = re.findall(r'<(?:div|span|p)[^>]*class="[^"]*(?:error|alert|invalid)[^"]*"[^>]*>(.*?)</', resp.text, re.IGNORECASE)
    print('Errors found:', err)
    # Check if there is captcha
    if 'turnstile' in resp.text.lower() or 'hcaptcha' in resp.text.lower() or 'recaptcha' in resp.text.lower():
        print('Captcha detected in login form!')
    if 'iprn-cap' in resp.text.lower():
        print('iprn-cap proof-of-work detected!')
