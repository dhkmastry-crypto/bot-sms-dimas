import asyncio
import re
from playwright.async_api import async_playwright

async def run():
    print("Starting browser...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to Switchfy...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(4000)

        # Coba buka https://augestel.com/Switchfy/api/documentation
        print("Opening API doc...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", html)
        print("Keys on /api/documentation:", set(keys))
        if not keys:
            # Cari input atau code block
            inputs = await page.eval_on_selector_all('input, pre, code', 'elements => elements.map(e => e.value || e.innerText)')
            for item in inputs:
                k = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", item)
                if k:
                    print("Found in element:", k)

        print("Opening API guide...")
        await page.goto("https://augestel.com/Switchfy/api/guide", timeout=30000)
        await page.wait_for_timeout(3000)
        html2 = await page.content()
        keys2 = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", html2)
        print("Keys on /api/guide:", set(keys2))
        if keys2:
            print("FOUND KEY:", keys2[0])

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
