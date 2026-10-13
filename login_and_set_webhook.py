import asyncio
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "augestel_accounts.json"), "r", encoding="utf-8") as f:
    accounts = json.load(f)

async def login_and_setup(idx):
    acc = accounts[idx - 1]
    email = acc["email"]
    password = acc["password"]
    pdir = os.path.abspath(f"browser_profile_augestel_{idx}")
    print(f"Processing Akun #{idx}: {email}...")
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=pdir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        
        # If on login page
        if await page.query_selector("#loginEmail, input[name='email']"):
            print(f"Logging in Akun #{idx} ({email})...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            try:
                await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) el.checked = true; }")
            except Exception:
                pass
            
            btn = await page.query_selector("#loginSubmit, form button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
            
            # Wait for redirect
            for sec in range(15):
                await asyncio.sleep(1)
                if any(x in page.url for x in ["/client/", "/dashboard", "/test/", "/api/"]):
                    print(f"Logged in after {sec+1}s!")
                    break
            
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")
            
        # Check if on webhook page
        if await page.query_selector("#webhookUrl"):
            await page.fill("#webhookUrl", WEBHOOK_URL)
            cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
            if cb and not await cb.is_checked():
                await cb.check()
            msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
            if msg_cb and not msg_cb.is_checked():
                await msg_cb.check()
                
            save_btn = await page.query_selector('form[action*="webhook"] button[type="submit"]')
            async with page.expect_navigation(timeout=15000):
                await save_btn.click()
                
            val = await page.evaluate('() => document.querySelector("#webhookUrl").value')
            is_active = await page.evaluate('() => document.querySelector("input[name=\'is_active\'][type=\'checkbox\']").checked')
            print(f"🎉 Akun #{idx} SUCCESS: URL={val}, is_active={is_active}")
            await ctx.close()
            return val == WEBHOOK_URL and is_active
        else:
            print(f"❌ Akun #{idx} FAILED: URL={page.url}, Title={await page.title()}")
            await ctx.close()
            return False

if __name__ == '__main__':
    acc_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    asyncio.run(login_and_setup(acc_idx))
