import requests
import re
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

r = s.get("https://augestel.com/Switchfy")
print("GET /Switchfy status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
csrf_input = soup.find("input", {"name": "_token"})
csrf_token = csrf_input.get("value") if csrf_input else ""
print("CSRF Token:", csrf_token)

post_data = {
    "_token": csrf_token,
    "email": "saputradimas0878@gmail.com",
    "password": "dimas098."
}

res = s.post(
    "https://augestel.com/Switchfy/login",
    data=post_data,
    headers={"Referer": "https://augestel.com/Switchfy"}
)
print("POST status:", res.status_code, "Final URL:", res.url)

doc_res = s.get("https://augestel.com/Switchfy/api/documentation")
print("GET doc status:", doc_res.status_code, "Final URL:", doc_res.url)

keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc_res.text)
print("Keys found in doc:", set(keys))

with open("debug_requests_doc_logged_in.html", "w", encoding="utf-8") as f:
    f.write(doc_res.text)
print("Saved debug_requests_doc_logged_in.html, length:", len(doc_res.text))
