import re

with open("debug_augestel_after_login.html", "r", encoding="utf-8") as f:
    text = f.read()

urls = re.findall(r'/Switchfy/[a-zA-Z0-9_\-\/]+', text)
for u in sorted(set(urls)):
    print("URL:", u)
