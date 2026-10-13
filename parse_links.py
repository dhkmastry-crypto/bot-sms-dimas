import re
from bs4 import BeautifulSoup

with open("debug_augestel_after_login.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

for a in soup.find_all("a"):
    href = a.get("href")
    text = a.get_text(strip=True)
    if href and href != "#":
        print(f"Text: '{text}' | href: '{href}'")
