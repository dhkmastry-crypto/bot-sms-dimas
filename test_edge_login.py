import asyncio
import re
from playwright.async_api import async_playwright

async def run():
    print("Launching Chromium...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            channel="msedge"
        )
        context = await browser.new_context()
        page = await context.new_page()

        print("Navigating to https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.wait_for_timeout(2000)

        print("Filling login credentials...")
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        
        # Click Sign in button specifically inside the login form
        login_btn = await page.query_selector('form[action*="/login"] button[type="submit"]')
        if login_btn:
            print("Clicking login button...")
            await login_btn.click()
        else:
            print("Login button not found, clicking fallback submit...")
            await page.click('button[type="submit"]')

        print("Waiting for page navigation / dashboard...")
        await page.wait_for_timeout(8000)
        print("URL after login:", page.url)

        # Now click the SMS API link in sidebar
        api_link = await page.query_selector('a[href*="/api/documentation"]')
        if api_link:
            print("Clicking SMS API menu link...")
            await api_link.click()
            await page.wait_for_timeout(6000)
            print("URL after clicking SMS API:", page.url)

            # Dump page
            content = await page.content()
            with open("debug_real_api_doc_page.html", "w", encoding="utf-8") as f:
                f.write(content)
            print("Saved debug_real_api_doc_page.html, size:", len(content))

            keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
            print("Found keys on SMS API page:", set(keys))
        else:
            print("SMS API menu link not found on current page!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
