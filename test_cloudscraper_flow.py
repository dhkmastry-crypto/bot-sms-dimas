import cloudscraper
import re

scraper = cloudscraper.create_scraper()

# 1. GET /Switchfy to get CSRF token and session cookie
print("1. Loading login page...")
r = scraper.get("https://augestel.com/Switchfy")
match = re.search(r'name="_token" value="([^"]+)"', r.text)
csrf_token = match.group(1) if match else ""
print("CSRF token:", csrf_token)

# 2. POST /Switchfy/login
print("2. Submitting login...")
post_data = {
    "_token": csrf_token,
    "email": "saputradimas0878@gmail.com",
    "password": "dimas098."
}
headers = {
    "Referer": "https://augestel.com/Switchfy",
    "Origin": "https://augestel.com",
}
resp = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers)
print("Login status code:", resp.status_code)
print("Final URL after login:", resp.url)

# 3. Request SMS API documentation
print("3. Fetching /Switchfy/api/documentation ...")
doc_resp = scraper.get("https://augestel.com/Switchfy/api/documentation", headers={"Referer": resp.url})
print("Doc status code:", doc_resp.status_code)
print("Doc final URL:", doc_resp.url)

keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc_resp.text)
print("Keys found in doc:", set(keys))

with open("debug_real_api_doc_success.html", "w", encoding="utf-8") as f:
    f.write(doc_resp.text)
print("Saved debug_real_api_doc_success.html, length:", len(doc_resp.text))
