import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

async def inspect():
    print("=" * 60)
    print("STATUS PROFIL BROWSER AKUN AUGESTEL (1 - 7)")
    print("=" * 60)
    
    for idx in range(1, 8):
        pdir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")
        if not os.path.exists(pdir):
            print(f"Akun #{idx}: ❌ Folder tidak ditemukan")
            continue
            
        async with async_playwright() as p:
            try:
                ctx = await p.chromium.launch_persistent_context(
                    user_data_dir=pdir,
                    channel="msedge",
                    headless=False,
                    args=["--window-position=-2000,-2000"]
                )
                page = ctx.pages[0] if ctx.pages else await ctx.new_page()
                await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=25000)
                await asyncio.sleep(2)
                
                title = await page.title()
                url = page.url
                
                # Check for cooldown
                wait_el = await page.query_selector(".wait")
                wait_text = (await wait_el.inner_text()).strip() if wait_el else None
                
                # Check for login inputs
                login_email = await page.query_selector("#loginEmail, input[name='email']")
                
                # Check for webhook input
                webhook_input = await page.query_selector("#webhookUrl")
                saved_url = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : null')
                is_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? cb.checked : false; }')
                
                status_str = ""
                if webhook_input:
                    status_str = f"✅ LOGGED IN | Webhook URL: '{saved_url}', is_active: {is_active}"
                elif wait_text:
                    status_str = f"⏳ COOLDOWN ANTI-SPAM: {wait_text}s tersisa"
                elif login_email:
                    status_str = f"🔑 BUTUH LOGIN (Title: {title}, URL: {url})"
                else:
                    status_str = f"❓ Unknown state (Title: {title}, URL: {url})"
                    
                print(f"Akun #{idx}: {status_str}")
                await ctx.close()
            except Exception as e:
                print(f"Akun #{idx}: ❌ Error: {e}")

if __name__ == '__main__':
    asyncio.run(inspect())
