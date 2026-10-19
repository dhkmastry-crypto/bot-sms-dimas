import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect_acc2():
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

        print(f"Navigating to /Switchfy for {email}...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle")

        login_el = await page.query_selector("#loginEmail")
        if login_el:
            print("Entering credentials...")
            await page.fill("#loginEmail", email)
            await page.fill("#loginPassword", password)
            await page.click("#loginSubmit")
            await asyncio.sleep(4)

        print("Final URL:", page.url)
        print("Final Title:", await page.title())

        # Grab any error text or alerts on page
        page_info = await page.evaluate('''() => {
            const alerts = Array.from(document.querySelectorAll('.alert, .error, .invalid-feedback, .text-danger, .swal2-html-container, .swal2-title, .wait, #loginError, .login-error, span[role="alert"]')).map(e => e.innerText.trim()).filter(t => t.length > 0);
            return {
                alerts: alerts,
                bodySnippet: document.body.innerText.slice(0, 1000)
            };
        }''')
        print("Alerts:", page_info["alerts"])
        print("Body snippet:\n", page_info["bodySnippet"])

        await page.screenshot(path="scratch/acc2_login_error.png")
        print("Screenshot saved to scratch/acc2_login_error.png")

        # If logged in, go check payment methods
        if "/client/" in page.url or "/dashboard" in page.url:
            await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
            body_pm = await page.evaluate("() => document.body.innerText")
            print("Payment methods has PayPal:", "PayPal" in body_pm)

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect_acc2())
