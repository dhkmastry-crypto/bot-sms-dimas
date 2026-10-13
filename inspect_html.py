import re

with open("debug_augestel_after_login.html", "r", encoding="utf-8") as f:
    html = f.read()

keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", html)
print("Found sk_live keys:", set(keys))

links = [l for l in re.findall(r'href=["\']([^"\']+)["\']', html) if "Switchfy" in l]
print("Found Switchfy links:")
for l in sorted(set(links)):
    print(" -", l)
