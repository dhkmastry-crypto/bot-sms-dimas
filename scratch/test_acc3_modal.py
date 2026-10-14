import asyncio
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.async_api import async_playwright
from numbers_service import get_augestel_accounts
from auto_add_augestel import ensure_augestel_login

async def main():
    accs = get_augestel_accounts()
    acc = accs[2] # Akun #3
    email = acc['email']
    pwd = acc['password']
    print(f"Testing Return All for Akun #3 ({email})...")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath('browser_profile_augestel_3'),
            channel='msedge',
            headless=False,
            args=['--window-position=-2000,-2000']
        )
        page = context.pages[0] if context.pages else await context.new_page()

        ok = await ensure_augestel_login(page, email, pwd)
        print('ensure_augestel_login result:', ok)
        print('Current URL:', page.url)

        if not ok:
            print('Login failed!')
            await context.close()
            return

        print('Navigating to client/numbers...')
        await page.goto('https://augestel.com/Switchfy/client/numbers', wait_until='networkidle')
        await asyncio.sleep(2)
        print('Numbers URL:', page.url)
        print('Page title:', await page.title())

        # Check for wait/cooldown
        wait_el = await page.query_selector('.wait')
        if wait_el:
            print('Cooldown active! Text:', await wait_el.inner_text())

        btn = await page.query_selector('#bulkReturnAllBtn')
        print('bulkReturnAllBtn found:', btn is not None)
        if btn:
            print('bulkReturnAllBtn visible:', await btn.is_visible())
            await btn.click()
            await asyncio.sleep(1.5)

            # Check Swal modal
            swal_title = await page.query_selector('.swal2-title')
            if swal_title:
                print('Swal title:', await swal_title.inner_text())
            swal_html = await page.query_selector('.swal2-html-container')
            if swal_html:
                print('Swal content:', await swal_html.inner_text())

            confirm_btn = await page.query_selector('button.swal2-confirm')
            print('confirm_btn found:', confirm_btn is not None)
            if confirm_btn:
                print('confirm_btn visible:', await confirm_btn.is_visible())
                # Just inspecting, not clicking confirm yet
                print('Modal confirm button is ready!')

        await asyncio.sleep(2)
        await context.close()

if __name__ == '__main__':
    asyncio.run(main())
