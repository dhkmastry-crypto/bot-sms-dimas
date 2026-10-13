import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"

async def setup():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath("browser_profile_augestel_1"),
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")
        
        await page.fill("#webhookUrl", WEBHOOK_URL)
        
        cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
        if cb and not await cb.is_checked():
            await cb.check()
            
        msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
        if msg_cb and not await msg_cb.is_checked():
            await msg_cb.check()
            
        save_btn = await page.query_selector('form[action*="webhook"] button[type="submit"]')
        print("Clicking save...")
        async with page.expect_navigation(timeout=15000):
            await save_btn.click()
            
        val = await page.evaluate('() => document.querySelector("#webhookUrl").value')
        is_active = await page.evaluate('() => document.querySelector("input[name=\'is_active\'][type=\'checkbox\']").checked')
        print(f"Akun #1 Result: URL='{val}', is_active={is_active}")
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(setup())
