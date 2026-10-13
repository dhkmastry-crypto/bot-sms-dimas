import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch persistent context to keep cookies/session solid
        user_data_dir = "./browser_profile_augestel_test"
        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=True
        )
        page = context.pages[0] if context.pages else await context.new_page()

        print("Navigating to https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", timeout=30000)
        await page.wait_for_timeout(2000)

        # Cek apakah sudah di dashboard atau perlu login
        if "login" in page.url.lower() or await page.query_selector("#loginEmail"):
            print("Logging in with credentials...")
            await page.fill("#loginEmail", "saputradimas0878@gmail.com")
            await page.fill("#loginPassword", "dimas098.")
            await page.click('button[type="submit"]')
            await page.wait_for_timeout(5000)

        print("Current URL:", page.url)

        # Sekarang buka Developer -> SMS API (https://augestel.com/Switchfy/api/documentation)
        print("Navigating to https://augestel.com/Switchfy/api/documentation ...")
        await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
        await page.wait_for_timeout(4000)
        print("Current URL:", page.url)

        content = await page.content()
        with open("debug_doc_page_persistent.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved debug_doc_page_persistent.html, size:", len(content))

        await context.close()

if __name__ == "__main__":
    asyncio.run(run())
