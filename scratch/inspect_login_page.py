import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect_login_form():
    user_data_dir = os.path.abspath("browser_profile_augestel_2")
    cleanup_profile_locks_and_orphans(user_data_dir)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle")

        info = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('input, button')).map(el => ({
                tag: el.tagName,
                id: el.id,
                name: el.name,
                type: el.type,
                placeholder: el.placeholder,
                text: el.innerText
            }));
        }''')
        print("Switchfy elements:", info)
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect_login_form())
