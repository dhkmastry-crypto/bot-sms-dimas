import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"

async def test_acc1():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath("browser_profile_augestel_1"),
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")
        
        # If redirected to login
        if "login" in page.url.lower() or "login" in (await page.title()).lower():
            print("Logging into Account 1...")
            await page.fill("#loginEmail, input[name='email']", "saputradimas0878@gmail.com")
            await page.fill("#loginPassword, input[name='password']", "dimas098.")
            try:
                await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) el.checked = true; }")
            except Exception:
                pass
            btn = await page.query_selector("#loginSubmit, form[action*='login'] button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
            await page.wait_for_timeout(3000)
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")

        print("Current page title:", await page.title())
        print("Current URL:", page.url)

        # Set webhook URL
        input_el = await page.wait_for_selector("#webhookUrl", timeout=10000)
        await input_el.fill(WEBHOOK_URL)

        # Ensure is_active checked
        active_cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
        if active_cb and not await active_cb.is_checked():
            await active_cb.check()

        # Ensure message.received checked
        msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
        if msg_cb and not msg_cb.is_checked():
            await msg_cb.check()

        # Submit form
        save_btn = await page.query_selector('form[action*="webhook"] button[type="submit"]')
        async with page.expect_navigation(timeout=15000):
            await save_btn.click()

        saved_val = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
        is_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? cb.checked : false; }')

        print(f"🎉 FINAL CONFIRMED STATUS: URL='{saved_val}', is_active={is_active}")
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(test_acc1())
