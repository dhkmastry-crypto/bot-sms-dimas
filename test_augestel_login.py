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
        content = await page.content()
        with open("debug_augestel_after_login.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved debug_augestel_after_login.html, length:", len(content))
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
