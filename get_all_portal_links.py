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
        await page.wait_for_timeout(4000)

        # Cari semua link di seluruh menu setelah login
        links = await page.eval_on_selector_all('a', 'elements => elements.map(e => ({href: e.href, text: e.innerText.trim()}))')
        print("ALL MENU LINKS ON PORTAL:")
        for l in links:
            if l['href'] and 'logout' not in l['href'].lower():
                print(f"[{l['text']}] -> {l['href']}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
