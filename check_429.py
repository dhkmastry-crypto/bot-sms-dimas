import cloudscraper
import re

scraper = cloudscraper.create_scraper()
res = scraper.get("https://augestel.com/Switchfy")
csrf = re.search(r'name="_token" value="([^"]+)"', res.text).group(1)
post = scraper.post("https://augestel.com/Switchfy/login", data={"_token": csrf, "email": "saputradimas0878@gmail.com", "password": "dimas098."})
print("Status code:", post.status_code)
print("Headers:", dict(post.headers))
print("Snippet:", post.text[:300])
