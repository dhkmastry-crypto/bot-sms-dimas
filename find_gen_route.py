import cloudscraper
import re

scraper = cloudscraper.create_scraper()
r = scraper.get('https://augestel.com/build/manifest.json')
print('manifest.json status:', r.status_code)
if r.status_code == 200:
    print(r.text)
else:
    # Check if there are other asset files in app JS
    js = scraper.get('https://augestel.com/build/assets/app-BmR76E4K.js').text
    chunks = re.findall(r'assets/[a-zA-Z0-9_\-]+\.js', js)
    print('Chunks in app js:', set(chunks))
