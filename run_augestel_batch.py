import os
import sys
import time
import cloudscraper
import re
import json

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

accounts = [
    ("Ekiprijipratama03@gmail.com", "Ciparay024"),
    ("Fikriramdn424@gmail.com", "Ciparay024"),
    ("dhkmastry@gmail.com", "dimas098."),
    ("mayateng86@gmail.com", "Lohan#098"),
    ("pakupakuwak@gmail.com", "Nathan27@")
]

results = []

for idx, (email, pwd) in enumerate(accounts, 1):
    print(f"\n[{idx}/5] Login untuk {email}...")
    scraper = cloudscraper.create_scraper()

    # Ambil halaman login
    r = scraper.get("https://augestel.com/Switchfy", timeout=15)
    match = re.search(r'name="_token" value="([^"]+)"', r.text)
    csrf = match.group(1) if match else ""

    headers = {
        "Referer": "https://augestel.com/Switchfy",
        "Origin": "https://augestel.com"
    }
    post_data = {
        "_token": csrf,
        "email": email,
        "password": pwd
    }

    resp = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers, timeout=15)

    if resp.status_code == 429:
        wait = 15
        try:
            h = resp.headers.get("Retry-After")
            if h and h.isdigit(): wait = int(h) + 2
        except Exception: pass
        print(f"  Rate limited, jeda {wait}s...")
        time.sleep(wait)
        # Coba ulang sekali
        resp = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers, timeout=15)

    print(f"  Status login: {resp.status_code}, URL: {resp.url}")

    if "/login" not in resp.url and resp.status_code == 200:
        # Berhasil login! Ambil API key
        doc = scraper.get("https://augestel.com/Switchfy/api/documentation", headers={"Referer": resp.url}, timeout=15)
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc.text)
        api_key = keys[0] if keys else ""
        print(f"  [BERHASIL] API Key: {api_key if api_key else 'Tidak ditemukan di doc'}")
        results.append({
            "email": email,
            "password": pwd,
            "api_key": api_key,
            "success": True
        })
    else:
        print("  [GAGAL] Kredensial tidak valid atau ditolak.")
        results.append({
            "email": email,
            "password": pwd,
            "api_key": "",
            "success": False
        })

    # Jeda 6 detik antar akun
    time.sleep(6)

with open("augestel_login_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nSELESAI. Output disimpan di augestel_login_results.json")
