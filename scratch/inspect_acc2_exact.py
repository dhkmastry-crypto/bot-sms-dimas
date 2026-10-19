import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[1]
    email = acc["email"]
    password = acc["password"]

    user_data_dir = os.path.abspath("browser_profile_augestel_2")
    cleanup_profile_locks_and_orphans(user_data_dir)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        print("Initial URL:", page.url)

        login_el = await page.query_selector("#loginEmail, input[name='email']")
        if login_el:
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            await asyncio.sleep(4)

        print("After Submit URL:", page.url)
        print("Title:", await page.title())
        
        info = await page.evaluate('''() => {
            return {
                text: document.body.innerText,
                alerts: Array.from(document.querySelectorAll('.alert, .text-danger, .invalid-feedback, .swal2-html-container, .wait')).map(e => e.innerText.trim())
            };
        }''')
        print("Alerts found:", info["alerts"])
        print("Body Text Preview:\n", info["text"][:600])

        await page.screenshot(path="scratch/acc2_login_state.png")
        print("Screenshot saved to scratch/acc2_login_state.png")
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect())
