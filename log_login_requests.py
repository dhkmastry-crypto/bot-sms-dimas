import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        page.on("request", lambda r: print(f">> REQ: {r.method} {r.url}"))
        page.on("response", lambda r: print(f"<< RES: {r.status} {r.url}"))

        print("Navigating to https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        print("Clicking submit...")
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(6000)
        print("Final URL:", page.url)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
