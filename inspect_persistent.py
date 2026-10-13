import asyncio
import os
import re
from playwright.async_api import async_playwright

async def inspect():
    async with async_playwright() as p:
        user_data_dir = os.path.abspath("browser_profile_augestel_test")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=True
        )
        page = context.pages[0] if context.pages else await context.new_page()

        print("Navigating to https://augestel.com/Switchfy/api/documentation ...")
        resp = await page.goto("https://augestel.com/Switchfy/api/documentation", timeout=30000)
        print("Status:", resp.status if resp else "None", "URL:", page.url)
        await page.wait_for_timeout(3000)

        content = await page.content()
        with open("saved_profile_doc.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved saved_profile_doc.html, length:", len(content))

        # Check if logged in
        if "/login" not in page.url and len(content) > 70000:
            print("🎉 WE ARE LOGGED IN!")
            # Find script tags
            scripts = await page.query_selector_all("script")
            print("Total script tags:", len(scripts))
            for i, s in enumerate(scripts):
                txt = await s.inner_text()
                if any(w in txt for w in ["generate", "apiKey", "api/key", "regenerate"]):
                    print(f"=== Script #{i} has key logic! ===")
                    print(txt)
        else:
            print("Redirected to login or session expired.")

        await context.close()

if __name__ == "__main__":
    asyncio.run(inspect())
