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
    print(f"Testing Return All for {email}...")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath('browser_profile_augestel_1'),
            channel='msedge',
            headless=False,
            args=['--window-position=-2000,-2000']
        )
        page = context.pages[0] if context.pages else await context.new_page()

        await page.goto('https://augestel.com/Switchfy', wait_until='networkidle')
        print('Initial URL:', page.url)

        login_input = await page.query_selector('#loginEmail')
        if login_input:
            print('Submitting login form...')
            await page.fill('#loginEmail', email)
            await page.fill('#loginPassword', pwd)
            btn = await page.query_selector('button[type="submit"]')
            if btn:
                await btn.click()
            await asyncio.sleep(4)
            print('Post login URL:', page.url)

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
                try:
                    async with page.expect_response(lambda r: 'bulk-return' in r.url, timeout=15000) as resp_info:
                        await confirm_btn.click()
                    resp = await resp_info.value
                    print('Response status:', resp.status)
                    print('Response URL:', resp.url)
                    print('Response text:', await resp.text())
                except Exception as e:
                    print('Error waiting for response:', e)

        await asyncio.sleep(2)
        await context.close()

if __name__ == '__main__':
    asyncio.run(main())
