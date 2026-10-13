import asyncio
from playwright.async_api import async_playwright
import json

async def main():
    with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
        accs = json.load(f)
    email = accs[0]['email']
    pwd = accs[0]['password']
    print(f"Logging in with Playwright for {email}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        await page.goto('https://augestel.com/Switchfy', wait_until='domcontentloaded')
        await asyncio.sleep(2)
        print('Page title on Switchfy:', await page.title(), 'URL:', page.url)

        # Fill login form
        email_inp = await page.query_selector('input[name="email"]')
        if email_inp:
            await page.fill('input[name="email"]', email)
            await page.fill('input[name="password"]', pwd)
            btn = await page.query_selector('button[type="submit"]')
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
            await asyncio.sleep(4)
            print('After login URL:', page.url, 'Title:', await page.title())

        # Navigate to https://augestel.com/Switchfy/test/numbers
        await page.goto('https://augestel.com/Switchfy/test/numbers', wait_until='domcontentloaded')
        await asyncio.sleep(3)
        print('Numbers page URL:', page.url, 'Title:', await page.title())

        # Take screenshot
        await page.screenshot(path='switchfy_test_numbers.png', full_page=True)
        print('Saved switchfy_test_numbers.png')

        # Inspect page content
        content = await page.content()
        with open('switchfy_test_numbers.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Saved switchfy_test_numbers.html (length:', len(content), ')')
        
        # Check buttons, forms, inputs, modals
        elements = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('button, a.btn, input, select, form, table, .modal')).map(el => ({
                tag: el.tagName,
                text: el.innerText ? el.innerText.trim().substring(0, 100) : '',
                id: el.id,
                name: el.getAttribute('name'),
                type: el.getAttribute('type'),
                action: el.getAttribute('action'),
                class: el.className
            }));
        }''')
        print(f'Found {len(elements)} elements')
        for el in elements[:40]:
            if el['text'] or el['id'] or el['name']:
                print(' -', el)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
