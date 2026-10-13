import time
import cloudscraper
import re

accounts = [
    ("Ekiprijipratama03@gmail.com", "Ciparay024"),
    ("Fikriramdn424@gmail.com", "Ciparay024"),
    ("dhkmastry@gmail.com", "dimas098."),
    ("mayateng86@gmail.com", "Lohan#098"),
    ("pakupakuwak@gmail.com", "Nathan27@")
]

print("Starting login sequence for 5 Augestel accounts...")
results = []

for idx, (email, pwd) in enumerate(accounts, 1):
    print(f"\n[{idx}/5] Logging in {email}...")
    scraper = cloudscraper.create_scraper()

    success = False
    for attempt in range(4):
        try:
            r = scraper.get("https://augestel.com/Switchfy", timeout=15)
            match = re.search(r'name="_token" value="([^"]+)"', r.text)
            csrf = match.group(1) if match else ""
            if not csrf:
                print("  ❌ Gagal mendapatkan CSRF token")
                break

            headers = {
                "Referer": "https://augestel.com/Switchfy",
                "Origin": "https://augestel.com"
            }
            post_data = {
                "_token": csrf,
                "email": email,
                "password": pwd
            }
            res = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers, timeout=15)

            if res.status_code == 429:
                retry_sec = 25
                try:
                    hdr = res.headers.get("Retry-After")
                    if hdr and hdr.isdigit():
                        retry_sec = int(hdr) + 2
                except Exception:
                    pass
                print(f"  ⏳ Rate limited (429). Menunggu {retry_sec} detik...")
                time.sleep(retry_sec)
                continue

            # Cek redirect ke portal / dashboard
            if "/login" not in res.url:
                print(f"  🎉 Berhasil Login! URL: {res.url}")
                # Ambil API Key dari halaman dokumentasi
                doc = scraper.get("https://augestel.com/Switchfy/api/documentation", headers={"Referer": res.url}, timeout=15)
                keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", doc.text)
                api_key = keys[0] if keys else ""
                print(f"  🔑 API Key: {api_key if api_key else 'Belum dibuat/Tidak ada'}")
                results.append({
                    "email": email,
                    "password": pwd,
                    "api_key": api_key,
                    "status": "success"
                })
                success = True
                break
            else:
                print("  ❌ Kredensial tidak valid atau ditolak oleh portal.")
                results.append({
                    "email": email,
                    "password": pwd,
                    "api_key": "",
                    "status": "invalid_credentials"
                })
                break
        except Exception as e:
            print(f"  ⚠️ Error: {e}")
            time.sleep(5)

    if not success and not any(r["email"] == email for r in results):
        results.append({
            "email": email,
            "password": pwd,
            "api_key": "",
            "status": "failed"
        })

    # Jeda aman antar akun agar tidak kena blokir Cloudflare
    print("  Jeda 6 detik sebelum akun berikutnya...")
    time.sleep(6)

print("\n" + "=" * 50)
print("HASIL AKHIR LOGIN AKUN AUGESTEL:")
for r in results:
    print(f"- {r['email']}: Status={r['status']} | API_Key={r['api_key']}")
