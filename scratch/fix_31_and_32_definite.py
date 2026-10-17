import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

TARGET_WEBHOOK = "https://dimsong.online/api/augestel/webhook"

async def setup_account(idx: int, email: str, password: str):
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
    cleanup_profile_locks_and_orphans(user_data_dir)
    
    print(f"\n========================================================")
    print(f"CONFIGURING WEBHOOK FOR ACCOUNT #{idx} ({email})")
    print(f"========================================================")
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=45000)
        
        # Check if login needed
        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if login_input or "login" in page.url.lower():
            print(f"  [#{idx}] Needs login. Performing login...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("input[name='password']", password)
            rem = await page.query_selector("input[name='remember']")
            if rem:
                await rem.check()
            await page.click("button[type='submit'], .au-btn")
            await page.wait_for_load_state("networkidle", timeout=30000)
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=45000)
            
        print(f"  [#{idx}] Page URL: {page.url}")
        
        # Now fill and submit cleanly without _method=DELETE
        res = await page.evaluate(f'''() => {{
            const input = document.querySelector("#webhookUrl");
            if (!input) return {{ error: "No input #webhookUrl" }};
            const form = input.closest('form');
            if (!form) return {{ error: "No form" }};
            
            // 1. CRITICAL: Remove the hidden _method=DELETE if present!
            const delInput = form.querySelector('input[name="_method"]');
            if (delInput) {{
                delInput.remove();
            }}
            
            // 2. Set webhook URL
            input.value = "{TARGET_WEBHOOK}";
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));
            
            // 3. Set is_active checkbox
            const cb = form.querySelector('input[type="checkbox"][name="is_active"]');
            if (cb) {{
                cb.checked = true;
                cb.dispatchEvent(new Event('input', {{ bubbles: true }}));
                cb.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            // 4. Set events[] checkbox
            const msg = form.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            if (msg) {{
                msg.checked = true;
                msg.dispatchEvent(new Event('input', {{ bubbles: true }}));
                msg.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            // 5. Click the update/save button (NOT remove!)
            const updateBtn = form.querySelector('button[style*="primary-color"]') || 
                              Array.from(form.querySelectorAll('button')).find(b => b.innerText.includes('endpoint') && !b.innerText.includes('Remove'));
                              
            if (updateBtn) {{
                updateBtn.click();
                return {{ success: true, method: "button_click", text: updateBtn.innerText.trim() }};
            }} else {{
                form.submit();
                return {{ success: true, method: "form_submit" }};
            }}
        }}''')
        
        print(f"  [#{idx}] Submit initiated:", res)
        print(f"  [#{idx}] Waiting for page response...")
        await asyncio.sleep(6)
        await page.wait_for_load_state("networkidle", timeout=20000)
        
        # Verify result
        final_url = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
        final_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? (cb.checked || cb.hasAttribute("checked")) : false; }')
        alerts = await page.evaluate('() => Array.from(document.querySelectorAll(".alert, [role=\'alert\']")).map(a => a.innerText.trim())')
        
        print(f"  [#{idx}] VERIFIED: url='{final_url}', is_active={final_active}, alerts={alerts}")
        
        ss_path = f"webhook_final_acc_{idx}.png"
        await page.screenshot(path=ss_path, full_page=True)
        print(f"  [#{idx}] Full page screenshot saved to: {ss_path}")
        
        await ctx.close()
        return final_url == TARGET_WEBHOOK and final_active

async def main():
    accs = json.load(open('augestel_accounts.json', encoding='utf-8'))
    for idx in [31, 32]:
        a = accs[idx - 1]
        try:
            ok = await setup_account(idx, a["email"], a["password"])
            print(f"Result Account #{idx}: {'SUCCESS' if ok else 'FAILED'}")
        except Exception as e:
            print(f"Exception on #{idx}: {e}")

if __name__ == '__main__':
    asyncio.run(main())
