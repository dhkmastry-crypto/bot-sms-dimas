import asyncio
import json
import os
import re
import sys
import time
import cloudscraper
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ACCOUNTS_TO_GENERATE = [
    ("Ekiprijipratama03@gmail.com", "Ciparay024"),
    ("Fikriramdn424@gmail.com", "Ciparay024"),
    ("dhkmastry@gmail.com", "dimas098."),
    ("mayateng86@gmail.com", "Lohan#098"),
    ("pakupakuwak@gmail.com", "Nathan27@")
]

ACC_FILE = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")


def wait_for_cooldown():
    """Wait until Laravel login rate limit (429) clears"""
    scraper = cloudscraper.create_scraper()
    while True:
        try:
            r = scraper.get("https://augestel.com/Switchfy", timeout=12)
            m = re.search(r'name="_token" value="([^"]+)"', r.text)
            token = m.group(1) if m else ""
            res = scraper.post("https://augestel.com/Switchfy/login", data={"_token": token, "email": "test@test.com", "password": "dummy"}, timeout=12)
            retry = res.headers.get("Retry-After")
            if not retry:
                print("✅ Cooldown selesai! Rate limit aktif telah terbuka.")
                return
            sec = int(retry)
            print(f"⏳ Menunggu rate-limit cooldown portal Augestel: {sec} detik tersisa...")
            time.sleep(min(sec + 2, 15))
        except Exception as e:
            print(f"⚠️ Error checking cooldown: {e}")
            time.sleep(5)


async def generate_key_for_account(p, email, password):
    print(f"\n==================================================")
    print(f"🔑 Memproses pembuatan API Key untuk: {email}")
    print(f"==================================================")

    browser = await p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
    )
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800}
    )
    page = await context.new_page()

    api_key_found = ""

    try:
        # 1. Buka halaman login
        print("1. Membuka https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=35000, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # 2. Input kredensial
        print("2. Memasukkan kredensial login...")
        email_input = await page.query_selector("#loginEmail, input[name='email']")
        pwd_input = await page.query_selector("#loginPassword, input[name='password']")

        if email_input and pwd_input:
            await email_input.fill(email)
            await pwd_input.fill(password)
            submit_btn = await page.query_selector("button[type='submit'], #loginSubmit")
            if submit_btn:
                await submit_btn.click()
            else:
                await page.keyboard.press("Enter")
            
            print("   Menunggu redirect dashboard...")
            await page.wait_for_timeout(6000)

        print(f"   URL setelah login: {page.url}")

        # 3. Kunjungi halaman Developer API Documentation
        print("3. Membuka https://augestel.com/Switchfy/api/documentation ...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=35000, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        # 4. Cek apakah tombol Generate API Key ada
        content = await page.content()
        existing_keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        if existing_keys:
            api_key_found = existing_keys[0]
            print(f"✅ API Key sudah aktif: {api_key_found}")
        else:
            print("4. Mencari tombol 'Generate API Key'...")
            # Coba cari tombol generate
            gen_btn = await page.query_selector("button:has-text('Generate API Key'), button[onclick*='generateApiKey'], #no-api-key-box button")
            if gen_btn:
                print("👉 Mengklik tombol 'Generate API Key'...")
                await gen_btn.click()
                await page.wait_for_timeout(2000)

                # Jika ada SweetAlert dialog konfirmasi
                swal_confirm = await page.query_selector(".swal2-confirm, button:has-text('Yes'), button:has-text('Generate')")
                if swal_confirm:
                    print("   Mengklik konfirmasi SweetAlert...")
                    await swal_confirm.click()
                    await page.wait_for_timeout(3000)
                else:
                    await page.wait_for_timeout(2000)

                # Tunggu dan baca ulang isi halaman
                await page.wait_for_timeout(3000)
                new_content = await page.content()
                new_keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", new_content)
                if new_keys:
                    api_key_found = new_keys[0]
                    print(f"🎉 SUKSES GENERATE API KEY: {api_key_found}")
                else:
                    # Coba cari di dalam code atau input atau span
                    code_el = await page.query_selector("code, #api-key-display, .font-mono")
                    if code_el:
                        txt = await code_el.inner_text()
                        m = re.search(r"sk_live_[a-zA-Z0-9_\-]+", txt)
                        if m:
                            api_key_found = m.group(0)
                            print(f"🎉 SUKSES MENDAPATKAN KEY DARI ELEMEN: {api_key_found}")
            else:
                print("⚠️ Tombol Generate API Key tidak ditemukan secara visual.")

        # Fallback: jika belum ketemu, cek halaman Webhooks
        if not api_key_found:
            print("5. Mengecek halaman Webhooks...")
            await page.goto("https://augestel.com/Switchfy/api/webhooks", timeout=20000)
            await page.wait_for_timeout(2000)
            wh_content = await page.content()
            wh_keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", wh_content)
            if wh_keys:
                api_key_found = wh_keys[0]
                print(f"🎉 Ditemukan API Key di halaman Webhooks: {api_key_found}")

    except Exception as e:
        print(f"❌ Error saat memproses {email}: {e}")
    finally:
        await context.close()
        await browser.close()

    return api_key_found


async def main():
    wait_for_cooldown()

    # Muat accounts yang sudah ada
    all_accounts = []
    if os.path.exists(ACC_FILE):
        try:
            with open(ACC_FILE, "r", encoding="utf-8") as f:
                all_accounts = json.load(f)
        except Exception:
            pass

    async with async_playwright() as p:
        for idx, (email, pwd) in enumerate(ACCOUNTS_TO_GENERATE, 1):
            key = await generate_key_for_account(p, email, pwd)

            # Update entry di all_accounts
            updated = False
            for acc in all_accounts:
                if acc.get("email", "").lower() == email.lower():
                    if key:
                        acc["api_key"] = key
                    updated = True
                    break
            if not updated:
                all_accounts.append({
                    "email": email,
                    "password": pwd,
                    "api_key": key or ""
                })

            # Simpan langsung ke augestel_accounts.json
            with open(ACC_FILE, "w", encoding="utf-8") as f:
                json.dump(all_accounts, f, indent=2)
            print(f"💾 Disimpan ke augestel_accounts.json untuk {email} (Key: {key or 'Belum ada'})")

            # Jeda antar akun agar tidak kena rate limit
            await asyncio.sleep(5)

    print("\n==================================================")
    print("🏁 SEMUA AKUN SELESAI DIPROSES!")
    print("==================================================")
    for i, a in enumerate(all_accounts, 1):
        print(f"{i}. {a['email']} -> {a.get('api_key') or '(Kosong)'}")


if __name__ == "__main__":
    asyncio.run(main())
