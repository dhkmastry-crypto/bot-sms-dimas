import asyncio
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.async_api import async_playwright
from numbers_service import get_augestel_accounts

async def main():
    accs = get_augestel_accounts()
    acc = accs[0]
    email = acc['email']
    pwd = acc['password']

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath('browser_profile_augestel_1'),
            channel='msedge',
            headless=False,
            args=['--window-position=-2000,-2000']
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        # Listen to responses
        page.on('response', lambda r: print(f"HTTP {r.status} {r.url}") if 'Switchfy' in r.url else None)

        print("Navigating to https://augestel.com/Switchfy...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle")
        print("Page URL:", page.url, "Title:", await page.title())

        # Check wait element
        wait_el = await page.query_selector('.wait')
        if wait_el:
            print("WAIT ELEMENT:", await wait_el.inner_text())

        print(f"Filling credentials for {email}...")
        await page.fill("#loginEmail", email)
        await page.fill("#loginPassword", pwd)
        await asyncio.sleep(0.5)

        btn = await page.query_selector("#loginForm button[type='submit']")
        print("Submit button:", btn)
        if btn:
            print("Clicking submit button...")
            await btn.click()

        for sec in range(15):
            await asyncio.sleep(1)
            t = await page.title()
            u = page.url
            print(f"[{sec+1}s] URL: {u} | Title: {t}")
            if "/client/" in u or "/dashboard" in u or "/test/" in u:
                print("SUCCESSFULLY LOGGED IN!")
                break

        # Check error messages if any
        content = await page.content()
        if "credentials do not match" in content.lower():
            print("ERROR: Kredensial tidak cocok!")
        if "wait" in content.lower():
            print("FOUND WAIT in page")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
