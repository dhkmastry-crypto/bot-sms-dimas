import asyncio
from playwright.async_api import async_playwright

async def run():
    print("Launching browser...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        print("Clicking submit...")
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(6000)
        print("URL after login:", page.url)

        # Klik menu SMS API dengan text 'SMS API'
        print("Locating SMS API link in sidebar...")
        sms_api_link = await page.query_selector('a:has-text("SMS API")')
        if sms_api_link:
            print("Found SMS API link, clicking...")
            await sms_api_link.click()
            await page.wait_for_timeout(5000)
            print("Current URL after click:", page.url)
            content = await page.content()
            with open("debug_sms_api_page.html", "w", encoding="utf-8") as f:
                f.write(content)
            print("Saved debug_sms_api_page.html, length:", len(content))
        else:
            print("SMS API link not found!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
