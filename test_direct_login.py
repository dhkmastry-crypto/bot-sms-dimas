import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("Navigating to Switchfy login...")
        await page.goto("https://augestel.com/Switchfy/login", timeout=30000)
        
        # Fill email & password
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        
        # Click Sign in button specifically
        print("Clicking submit button...")
        btn = await page.query_selector('form[action*="/login"] button[type="submit"]')
        if btn:
            await btn.click()
        else:
            print("Button not found!")

        # Wait for navigation or change
        await page.wait_for_timeout(7000)
        print("URL after login:", page.url)
        content = await page.content()
        with open("debug_successful_login.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Wrote debug_successful_login.html, length:", len(content))

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
