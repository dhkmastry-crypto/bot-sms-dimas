import asyncio
import re
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding="utf-8")

async def test_single():
    email = "Ekiprijipratama03@gmail.com"
    pwd = "Ciparay024"

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        print("1. Membuka https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # Cek jika ada lockout countdown di halaman login
        lock = await page.query_selector("#loginLock")
        if lock:
            secs = await lock.get_attribute("data-seconds")
            print(f"⚠️ Lockout aktif pada form login: {secs} detik.")
            await context.close()
            await browser.close()
            return

        print("2. Login...")
        await page.fill("#loginEmail", email)
        await page.fill("#loginPassword", pwd)
        await page.click("form#loginForm button[type='submit'], button#loginSubmit, form#loginForm button")
        await page.wait_for_timeout(6000)
        print("   URL setelah submit:", page.url)

        print("3. Membuka https://augestel.com/Switchfy/api/documentation ...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        # Cek apakah sk_live sudah ada
        content = await page.content()
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        if keys:
            print("✅ Key sudah ada:", keys[0])
            await context.close()
            await browser.close()
            return

        # Klik generate API key
        print("4. Mencari tombol Generate API Key...")
        gen_btn = await page.query_selector("#no-api-key-box button, button[onclick*='generateApiKey']")
        if gen_btn:
            print("👉 Mengklik tombol Generate API Key...")
            await gen_btn.click()
            await page.wait_for_timeout(1500)

            # Cek SweetAlert
            print("   Mengecek modal SweetAlert...")
            # Gunakan Swal.clickConfirm() atau klik force
            swal_clicked = await page.evaluate("""() => {
                if (typeof Swal !== 'undefined' && typeof Swal.clickConfirm === 'function') {
                    Swal.clickConfirm();
                    return 'Swal.clickConfirm() dipanggil';
                }
                const btn = document.querySelector('button.swal2-confirm');
                if (btn) {
                    btn.click();
                    return 'button.swal2-confirm diklik via JS';
                }
                return 'Tidak ada swal confirm';
            }""")
            print("   Hasil klik konfirmasi:", swal_clicked)
            await page.wait_for_timeout(4000)

            # Cek popup sukses jika ada
            await page.evaluate("""() => {
                if (typeof Swal !== 'undefined' && typeof Swal.clickConfirm === 'function') {
                    Swal.clickConfirm();
                }
            }""")
            await page.wait_for_timeout(2000)

            # Ambil key baru
            new_content = await page.content()
            new_keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", new_content)
            print("🎉 Hasil Key:", new_keys)
        else:
            print("⚠️ Tombol generate tidak ditemukan di halaman.")

        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_single())
