import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print("Navigating to Switchfy login...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        
        # Click submit and wait for navigation
        async with page.expect_navigation(timeout=30000):
            await page.click('button[type="submit"]')
            
        print("Logged in successfully! Current URL:", page.url)
        
        # Click menu SMS API
        print("Clicking link to SMS API / documentation...")
        link = await page.query_selector('a[href*="/api/documentation"]')
        if link:
            await link.click()
            await page.wait_for_timeout(4000)
        else:
            await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
            await page.wait_for_timeout(4000)

        print("URL on doc page:", page.url)
        content = await page.content()
        with open("debug_api_documentation_auth.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved debug_api_documentation_auth.html, length:", len(content))

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
