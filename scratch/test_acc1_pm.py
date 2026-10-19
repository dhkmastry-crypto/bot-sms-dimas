import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def test_acc1():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[0] # Account 1
    email = acc["email"]
    password = acc["password"]

    user_data_dir = os.path.abspath("browser_profile_augestel_1")
    cleanup_profile_locks_and_orphans(user_data_dir)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        print(f"Navigating to https://augestel.com/Switchfy for {email}...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)

        # Check if already logged in or login form present
        title = await page.title()
        print("Page Title:", title, "URL:", page.url)

        if "login" in page.url.lower() or "login" in title.lower() or "switchfy" in page.url.lower():
            try:
                login_el = await page.wait_for_selector("#loginEmail, input[name='email']", timeout=8000)
                if login_el:
                    print("Found login input! Entering credentials...")
                    await page.fill("#loginEmail, input[name='email']", email)
                    await page.fill("#loginPassword, input[name='password']", password)
                    try:
                        cb = await page.query_selector("input[name='remember']")
                        if cb: await cb.check()
                    except Exception:
                        pass
                    btn = await page.wait_for_selector("#loginForm button[type='submit'], button[type='submit'], #loginSubmit", timeout=5000)
                    if btn:
                        print("Submitting login...")
                        await btn.click()
                        # Wait for redirect
                        for i in range(15):
                            await asyncio.sleep(1)
                            u = page.url
                            t = await page.title()
                            print(f"[{i+1}s] URL: {u} | Title: {t}")
                            if "/client/" in u or "/dashboard" in u or "/test/" in u:
                                print("Logged in successfully!")
                                break
            except Exception as e:
                print("No login input or error waiting for login:", e)

        # Go to payment methods
        print("Navigating to payment methods...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)
        print("Final PM URL:", page.url, "Title:", await page.title())

        # Check PM page
        pm_info = await page.evaluate('''() => {
            return {
                bodyText: document.body.innerText,
                hasDimSongKang: document.body.innerText.includes('dimsongkang@gmail.com'),
                hasEmpty: document.body.innerText.includes('No Payment Methods Yet')
            };
        }''')
        print("Has dimsongkang@gmail.com:", pm_info["hasDimSongKang"])
        print("Has 'No Payment Methods Yet':", pm_info["hasEmpty"])
        print("Body Snippet:\n", pm_info["bodyText"][:600])

        await page.screenshot(path="scratch/acc1_pm_check.png")
        print("Screenshot saved to scratch/acc1_pm_check.png")
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_acc1())
