import asyncio
import re
from playwright.async_api import async_playwright

async def check():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://augestel.com/Switchfy')
        await page.fill('#loginEmail', 'Ekiprijipratama03@gmail.com')
        await page.fill('#loginPassword', 'Ciparay024')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(4000)
        await page.goto('https://augestel.com/Switchfy/api/documentation')
        await page.wait_for_timeout(2000)
        content = await page.content()
        keys = re.findall(r'sk_live_[a-zA-Z0-9_\-]+', content)
        print('Ekiprijipratama03 Keys:', keys)
        if not keys:
            print('URL:', page.url)
            btns = await page.query_selector_all('button')
            for b in btns:
                t = (await b.inner_text()).strip()
                if t:
                    print('Button text:', t)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(check())
