import asyncio
import re
from playwright.async_api import async_playwright

async def run():
    print("Launching Chromium...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Monitor all requests and responses
        async def on_response(response):
            try:
                ct = response.headers.get("content-type", "")
                if "json" in ct or "text" in ct:
                    body = await response.text()
                    keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", body)
                    if keys:
                        print(f"!!! FOUND KEY in response from {response.url}: {keys[0]}")
            except Exception:
                pass

        page.on("response", on_response)

        print("Navigating to login...")
        await page.goto("https://augestel.com/Switchfy/login", timeout=30000)
        await page.fill("#loginEmail", "saputradimas0878@gmail.com")
        await page.fill("#loginPassword", "dimas098.")
        
        # Submit
        await page.click('form[action*="/login"] button[type="submit"]')
        await page.wait_for_timeout(6000)
        print("Logged in, page url:", page.url)

        # Check cookies
        cookies = await context.cookies()
        print("Cookies count:", len(cookies))
        for c in cookies:
            print("Cookie:", c["name"], c["domain"])

        # Try visiting /Switchfy/api/documentation
        print("Visiting /Switchfy/api/documentation...")
        resp = await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
        print("Response status:", resp.status if resp else "None", "Final URL:", page.url)
        content = await page.content()
        with open("doc_page_result.html", "w", encoding="utf-8") as f:
            f.write(content)

        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        print("Keys on doc_page_result:", set(keys))

        # Try visiting /Switchfy/client/profile
        print("Visiting /Switchfy/client/profile...")
        resp2 = await page.goto("https://augestel.com/Switchfy/client/profile", timeout=30000)
        print("Profile URL:", page.url)
        content2 = await page.content()
        keys2 = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content2)
        print("Keys on profile:", set(keys2))

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
