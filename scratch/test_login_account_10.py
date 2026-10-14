import asyncio
import os
import sys
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.async_api import async_playwright

async def main():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accs = json.load(f)
    
    acc = accs[9] # index 10
    email = acc["email"]
    pwd = acc["password"]
    print(f"Testing login for Akun #10: {email} with pwd: {pwd}")

    user_data_dir = os.path.abspath("browser_profile_augestel_10")
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        p = os.path.join(user_data_dir, lk)
        if os.path.exists(p):
            try: os.remove(p)
            except Exception: pass

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=-2000,-2000"
            ]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        # Buka halaman login / numbers
        await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        print("Page URL:", page.url)
        print("Page Title:", await page.title())

        # Jika butuh login
        if "/login" in page.url.lower() or await page.query_selector("input[name='email'], #loginEmail"):
            print("Form login terdeteksi. Mengisi email & password...")
            email_input = await page.query_selector("#loginEmail, input[name='email']")
            pass_input = await page.query_selector("#loginPassword, input[name='password']")
            if email_input:
                await email_input.fill(email)
            if pass_input:
                await pass_input.fill(pwd)
            
            # Remember me
            try:
                rem = await page.query_selector("input[name='remember'], #remember")
                if rem: await rem.check()
            except Exception: pass

            await asyncio.sleep(1)
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")

            print("Menunggu redirect setelah submit login...")
            for _ in range(15):
                await asyncio.sleep(1)
                if "/login" not in page.url.lower():
                    print("🎉 Login berhasil! URL sekarang:", page.url)
                    break
            else:
                print("⚠️ Masih di URL login:", page.url)

        # Sekarang coba cari API Key di halaman API/Docs atau Profile/Settings
        # Coba buka https://augestel.com/Switchfy/api/webhooks atau dokumentasi API
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        print("Webhooks page URL:", page.url)

        # Coba buka https://augestel.com/Switchfy/profile atau token/api
        await page.goto("https://augestel.com/Switchfy/profile", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        print("Profile URL:", page.url)
        content = await page.content()
        # Cari sk_live
        import re
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        print("Ditemukan sk_live di profile:", keys)

        # Coba juga di https://augestel.com/Switchfy/api/docs
        await page.goto("https://augestel.com/Switchfy/api/docs", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        content_docs = await page.content()
        keys_docs = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content_docs)
        print("Ditemukan sk_live di api docs:", keys_docs)

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
