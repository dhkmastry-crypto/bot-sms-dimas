import asyncio
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.async_api import async_playwright
from numbers_service import get_augestel_accounts

async def main():
    accs = get_augestel_accounts()
    for i in range(1, len(accs) + 1):
        prof = os.path.abspath(f"browser_profile_augestel_{i}")
        email = accs[i-1]["email"]
        async with async_playwright() as p:
            ctx = await p.chromium.launch_persistent_context(user_data_dir=prof, channel="msedge", headless=True)
            page = ctx.pages[0] if ctx.pages else await ctx.new_page()
            await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded")
            t = await page.title()
            u = page.url
            wait_el = await page.query_selector(".wait")
            wait_txt = (await wait_el.inner_text()).strip() if wait_el else "None"
            print(f"Akun #{i} ({email}) -> Title: {t} | URL: {u} | Wait: {wait_txt}")
            await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
