import asyncio
import json
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

        await page.goto('https://augestel.com/Switchfy', wait_until='networkidle')
        print('URL:', page.url, 'Title:', await page.title())

        login_input = await page.query_selector('#loginEmail')
        if login_input:
            print(f'Logging in {email}...')
            await page.fill('#loginEmail', email)
            await page.fill('#loginPassword', pwd)

            # Check remember checkbox
            cb = await page.query_selector("input[name='remember']")
            if cb:
                await cb.check()
                print('Checked Remember Me!')

            await asyncio.sleep(0.5)
            btn = await page.query_selector("#loginForm button[type='submit']")
            if btn:
                await btn.click()
            await asyncio.sleep(4)
            print('Post login URL:', page.url, 'Title:', await page.title())

        # Extract all cookies
        cookies = await ctx.cookies(['https://augestel.com'])
        cookie_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cookies_augestel_1.json')
        with open(cookie_file, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, indent=2)

        print(f"Successfully saved {len(cookies)} cookies to {cookie_file}!")
        for c in cookies:
            print(f"  Cookie: {c['name']} (expires: {c.get('expires')})")

        # Now test going directly to client/numbers using those cookies!
        await page.goto('https://augestel.com/Switchfy/client/numbers', wait_until='networkidle')
        print('Direct numbers access URL:', page.url, 'Title:', await page.title())

        await ctx.close()

if __name__ == '__main__':
    asyncio.run(main())
