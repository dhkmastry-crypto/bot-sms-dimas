import asyncio
import re
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(5000)

        targets = [
            "https://augestel.com/Switchfy/api/documentation",
            "https://augestel.com/Switchfy/api/guide",
            "https://augestel.com/Switchfy/api/webhooks",
            "https://augestel.com/Switchfy/client/profile",
            "https://augestel.com/Switchfy/client/security",
            "https://augestel.com/Switchfy/client/dashboard",
        ]

        for url in targets:
            print(f"Visiting {url} ...")
            try:
                await page.goto(url, timeout=20000)
                await page.wait_for_timeout(3000)
                content = await page.content()
                keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
                print(f" -> Found keys: {set(keys)}")
                if keys:
                    print(f"SUCCESS! Found key on {url}: {keys[0]}")
                    break
            except Exception as e:
                print(f"Error on {url}: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
