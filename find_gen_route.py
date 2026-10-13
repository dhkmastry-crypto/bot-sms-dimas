import cloudscraper
import re

scraper = cloudscraper.create_scraper()
# Let's inspect the HTML of /Switchfy/api/documentation
# Wait, does /Switchfy/api/documentation need authentication or is it public?
doc = scraper.get('https://augestel.com/Switchfy/api/documentation')
print("Status:", doc.status_code, "Length:", len(doc.text))
idx = doc.text.find('generateApiKey')
print("idx of generateApiKey:", idx)
if idx != -1:
    # Print 2000 chars after this
    print("=== 2000 chars around generateApiKey ===")
    print(doc.text[idx:idx+3000])
else:
    print("Not found without login. Is it behind login?")
