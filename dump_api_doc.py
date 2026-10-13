import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Logging in...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(4000)

        print("Navigating to https://augestel.com/Switchfy/api/documentation ...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
        await page.wait_for_timeout(4000)
        content = await page.content()
        with open("debug_api_documentation.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved debug_api_documentation.html, size:", len(content))

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
