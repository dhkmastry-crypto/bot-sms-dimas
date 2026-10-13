import time
import cloudscraper
import re

print("Waiting 55 seconds for Cloudflare rate limit to completely expire...")
time.sleep(55)

scraper = cloudscraper.create_scraper()
print("1. Fetching login page...")
r = scraper.get("https://augestel.com/Switchfy")
print("GET status:", r.status_code)
csrf = re.search(r'name="_token" value="([^"]+)"', r.text).group(1)
print("CSRF:", csrf)

print("2. Submitting login request...")
post = scraper.post("https://augestel.com/Switchfy/login", data={"_token": csrf, "email": "saputradimas0878@gmail.com", "password": "dimas098."})
print("Login status:", post.status_code, "Final URL:", post.url)

print("3. Fetching /Switchfy/api/documentation ...")
doc = scraper.get("https://augestel.com/Switchfy/api/documentation")
print("Doc status:", doc.status_code, "Final URL:", doc.url)

keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc.text)
print("Keys found in doc:", set(keys))

if keys:
    print("SUCCESS! API Key:", keys[0])
else:
    with open("doc_after_wait.html", "w", encoding="utf-8") as f:
        f.write(doc.text)
    print("Saved doc_after_wait.html, size:", len(doc.text))
