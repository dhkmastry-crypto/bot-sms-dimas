import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

async def debug_account_31():
    user_data_dir = os.path.abspath("browser_profile_augestel_31")
    # Kill any lingering edge locks
    from augestel_browser_pool import cleanup_profile_locks_and_orphans
    cleanup_profile_locks_and_orphans(user_data_dir)
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        # Listen to requests and responses
        page.on("request", lambda r: print(f"REQ: {r.method} {r.url}"))
        page.on("response", lambda r: print(f"RESP: {r.status} {r.url}"))
        
        print("1. Opening /api/webhooks...")
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")
        
        print(f"Current URL: {page.url}")
        print(f"Current Title: {await page.title()}")
        
        # Check current inputs
        val_before = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : "NO_ELEMENT"')
        print(f"Value before: '{val_before}'")
        
        # Fill URL
        target = "https://dimsong.online/api/augestel/webhook"
        print(f"2. Filling {target}...")
        input_el = await page.wait_for_selector("#webhookUrl")
        await input_el.fill(target)
        
        # Check active
        print("3. Checking is_active...")
        await page.evaluate('''() => {
            const cb = document.querySelector('input[type="checkbox"][name="is_active"]');
            if (cb && !cb.checked) cb.click();
        }''')
        
        # Check form and action
        form_info = await page.evaluate('''() => {
            const f = document.querySelector('#webhookUrl').closest('form');
            return {
                action: f ? f.action : null,
                method: f ? f.method : null,
                token: f ? f.querySelector('input[name="_token"]')?.value : null
            };
        }''')
        print(f"Form info: {form_info}")
        
        # Find submit button
        print("4. Finding and clicking submit button...")
        btn = await page.query_selector('form button[type="submit"]')
        if btn:
            print(f"Button text: '{(await btn.inner_text()).strip()}'")
            print("Clicking button...")
            await btn.click()
            print("Waiting 10 seconds for network and response...")
            await asyncio.sleep(10)
        else:
            print("Submit button not found!")
            
        print(f"URL after submit: {page.url}")
        val_after = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : "NO_ELEMENT"')
        active_after = await page.evaluate('() => document.querySelector("input[name=\'is_active\'][type=\'checkbox\']") ? document.querySelector("input[name=\'is_active\'][type=\'checkbox\']").checked : false')
        print(f"Value after: '{val_after}', is_active: {active_after}")
        
        # Check for any alerts/errors on page
        alerts = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('.alert, div[class*="emerald"], div[class*="rose"], div[class*="red"], div[class*="green"]')).map(e => e.innerText.trim()).filter(Boolean);
        }''')
        print(f"Alerts found: {alerts}")
        
        await page.screenshot(path="debug_31_after.png")
        print("Saved debug_31_after.png")
        
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(debug_account_31())
