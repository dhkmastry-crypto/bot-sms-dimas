import asyncio
import json
import os
import re
import sys
import time
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


async def generate_key_for_account(p, email, password):
    print(f"\n==================================================")
    print(f"🔑 Memproses akun: {email}")
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
        print("1. Membuka portal login...")
        await page.goto("https://augestel.com/Switchfy", timeout=35000, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # Cek jika ada lockout countdown
        lock = await page.query_selector("#loginLock")
        if lock:
            secs = await lock.get_attribute("data-seconds")
            print(f"⚠️ Lockout aktif pada form login: {secs} detik.")
            return ""

        print("2. Mengisi kredensial...")
        await page.fill("#loginEmail", email)
        await page.fill("#loginPassword", password)
        await page.wait_for_timeout(500)

        # Klik submit
        submit_btn = await page.query_selector("form#loginForm button[type='submit'], #loginSubmit, button:has-text('Sign in')")
        if submit_btn:
            await submit_btn.click()
        else:
            await page.keyboard.press("Enter")

        print("   Menunggu redirect...")
        for _ in range(12):
            await page.wait_for_timeout(1000)
            if "test/live-sms" in page.url or "/login" not in page.url:
                break

        print(f"   URL: {page.url}")

        if "/login" in page.url:
            print("⚠️ Gagal login, masih di halaman login.")
            return ""

        print("3. Membuka https://augestel.com/Switchfy/api/documentation ...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=35000, wait_until="domcontentloaded")
        await page.wait_for_timeout(2500)

        # Cek apakah key sudah ada
        content = await page.content()
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        if keys:
            api_key_found = keys[0]
            print(f"✅ Key sudah aktif: {api_key_found}")
            return api_key_found

        # Klik tombol Generate API Key
        print("4. Mencari tombol Generate API Key...")
        gen_btn = await page.query_selector("#no-api-key-box button, button[onclick*='generateApiKey']")
        if gen_btn:
            print("👉 Mengklik tombol Generate API Key...")
            await gen_btn.click()
            await page.wait_for_timeout(1500)

            # Konfirmasi SweetAlert via JS
            await page.evaluate("""() => {
                if (typeof Swal !== 'undefined' && typeof Swal.clickConfirm === 'function') {
                    Swal.clickConfirm();
                }
            }""")
            swal_btn = page.locator("button.swal2-confirm")
            if await swal_btn.count() > 0:
                try:
                    await swal_btn.first.click(force=True, timeout=3000)
                except Exception:
                    pass

            # Tunggu respons generate key
            await page.wait_for_timeout(4000)

            # Jika ada SweetAlert sukses ("Success"), klik juga
            await page.evaluate("""() => {
                if (typeof Swal !== 'undefined' && typeof Swal.clickConfirm === 'function') {
                    Swal.clickConfirm();
                }
            }""")
            await page.wait_for_timeout(1500)

            # Baca ulang isi halaman
            new_content = await page.content()
            new_keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", new_content)
            if new_keys:
                api_key_found = new_keys[0]
                print(f"🎉 SUKSES GENERATE KEY: {api_key_found}")
            else:
                code_el = await page.query_selector("code, #api-key-display")
                if code_el:
                    txt = await code_el.inner_text()
                    m = re.search(r"sk_live_[a-zA-Z0-9_\-]+", txt)
                    if m:
                        api_key_found = m.group(0)
                        print(f"🎉 SUKSES DARI ELEMEN: {api_key_found}")
        else:
            print("⚠️ Tombol Generate API Key tidak ditemukan.")

    except Exception as e:
        print(f"❌ Error saat memproses {email}: {e}")
    finally:
        await context.close()
        await browser.close()

    return api_key_found


async def main():
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
            for acc in all_accounts:
                if acc.get("email", "").lower() == email.lower():
                    if key:
                        acc["api_key"] = key
                    break

            # Simpan langsung ke augestel_accounts.json
            with open(ACC_FILE, "w", encoding="utf-8") as f:
                json.dump(all_accounts, f, indent=2)
            print(f"💾 Update augestel_accounts.json untuk {email} -> {key or '(Belum berhasil)'}")

            # Jeda 6 detik antar akun
            await asyncio.sleep(6)

    print("\n==================================================")
    print("🏁 HASIL AKHIR DAFTAR AKUN & API KEY:")
    print("==================================================")
    for i, a in enumerate(all_accounts, 1):
        print(f"{i}. {a['email']} | API Key: {a.get('api_key') or '(Kosong)'}")


if __name__ == "__main__":
    asyncio.run(main())
