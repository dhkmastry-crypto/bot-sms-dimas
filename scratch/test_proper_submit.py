import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from augestel_browser_pool import cleanup_profile_locks_and_orphans

TARGET_WEBHOOK = "https://dimsong.online/api/augestel/webhook"

async def save_webhook_account(idx: int, email: str, password: str):
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
    cleanup_profile_locks_and_orphans(user_data_dir)
    
    print(f"\n==================================================")
    print(f"PROPER SUBMIT for Account #{idx} ({email})")
    print(f"==================================================")
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=45000)
        
        if "login" in page.url.lower():
            print("  Logging in...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("input[name='password']", password)
            await page.click("button[type='submit'], .au-btn")
            await page.wait_for_load_state("networkidle", timeout=30000)
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=45000)
            
        print("  Current URL:", page.url)
        name = await page.evaluate('''() => {
            const el = document.querySelector('header, nav, .user-name');
            return document.body.innerText.match(/Welcome back,\\s*([^\\n]+)/i)?.[1] || "Unknown";
        }''')
        print(f"  Account Name: {name}")
        
        # Check current value
        val_cur = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
        print(f"  Current Webhook Value: '{val_cur}'")
        
        # Fill input and check boxes directly in DOM
        res_js = await page.evaluate(f'''() => {{
            const input = document.querySelector("#webhookUrl");
            if (!input) return {{ error: "No input #webhookUrl" }};
            
            input.value = "{TARGET_WEBHOOK}";
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));
            
            const cb = document.querySelector('input[type="checkbox"][name="is_active"]');
            if (cb && !cb.checked) {{
                cb.checked = true;
                cb.dispatchEvent(new Event('input', {{ bubbles: true }}));
                cb.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            if (msg && !msg.checked) {{
                msg.checked = true;
                msg.dispatchEvent(new Event('input', {{ bubbles: true }}));
                msg.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            // Submit form specifically
            const form = input.closest('form');
            if (!form) return {{ error: "No form found" }};
            
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {{
                submitBtn.click();
                return {{ success: true, method: "button_click", btnText: submitBtn.innerText }};
            }} else {{
                form.submit();
                return {{ success: true, method: "form_submit" }};
            }}
        }}''')
        
        print("  JS Submit result:", res_js)
        print("  Waiting 5 seconds for form navigation...")
        await asyncio.sleep(5)
        await page.wait_for_load_state("networkidle", timeout=20000)
        
        # Verify result on reloaded page
        new_val = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
        new_active = await page.evaluate('() => document.querySelector("input[name=\'is_active\'][type=\'checkbox\']") ? document.querySelector("input[name=\'is_active\'][type=\'checkbox\']").checked : false')
        print(f"  FINAL VERIFIED: url='{new_val}', is_active={new_active}")
        
        await page.screenshot(path=f"webhook_acc_{idx}_verified.png")
        print(f"  Screenshot saved: webhook_acc_{idx}_verified.png")
        await ctx.close()

async def main():
    import json
    accs = json.load(open('augestel_accounts.json', encoding='utf-8'))
    # Jalankan untuk akun 31 dan 32
    for idx in [31, 32]:
        a = accs[idx - 1]
        try:
            await save_webhook_account(idx, a["email"], a["password"])
        except Exception as e:
            print(f"Error on #{idx}: {e}")

if __name__ == '__main__':
    asyncio.run(main())
