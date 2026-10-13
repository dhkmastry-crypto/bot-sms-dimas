import re
from bs4 import BeautifulSoup

with open("debug_api_documentation.html", "r", encoding="utf-8") as f:
    html = f.read()

# Cari sk_live
keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", html)
print("Keys found in doc:", keys)

# Cari semua input atau element yang punya key
soup = BeautifulSoup(html, "html.parser")
for inp in soup.find_all(["input", "textarea", "code", "span"]):
    val = inp.get("value") or inp.get_text()
    if "sk_live" in val or "Bearer" in val or "token" in val.lower():
        print("Element:", inp.name, inp.attrs, "->", val[:100])
