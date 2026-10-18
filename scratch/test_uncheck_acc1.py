import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\ADMIN\Downloads\OTP IVA SMS"
TARGET_WEBHOOK = "https://dimsong.online/api/augestel/webhook"
idx = 1
profile_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")

async def main():
    print(f"Testing proper uncheck of number.assigned & number.removed for Account #{idx}...")
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            channel="msedge",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=-2000,-2000"
            ]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        print("1. Opening /Switchfy/api/webhooks...")
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)
        
        res = await page.evaluate(f'''() => {{
            const input = document.querySelector("#webhookUrl");
            if (!input) return {{ error: "No input #webhookUrl" }};
            const form = input.closest('form');
            if (!form) return {{ error: "No form found" }};
            
            // 1. Remove _method=DELETE if present
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
            
            // 4. Set message.received checkbox = TRUE
            const msg = form.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            if (msg) {{
                msg.checked = true;
                msg.dispatchEvent(new Event('input', {{ bubbles: true }}));
                msg.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            // 5. Explicitly UNCHECK number.assigned and number.removed
            const na = form.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            if (na) {{
                na.checked = false;
                na.dispatchEvent(new Event('input', {{ bubbles: true }}));
                na.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            const nr = form.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            if (nr) {{
                nr.checked = false;
                nr.dispatchEvent(new Event('input', {{ bubbles: true }}));
                nr.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            
            // 6. Click save/update button
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
        
        print("Submit initiated:", res)
        print("Waiting 5s for page reload...")
        await asyncio.sleep(5)
        await page.wait_for_load_state("networkidle", timeout=20000)
        
        state_after = await page.evaluate('''() => {
            return {
                url: document.querySelector('#webhookUrl')?.value,
                is_active: document.querySelector('input[name="is_active"][type="checkbox"]')?.checked,
                msg: document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]')?.checked,
                assigned: document.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]')?.checked,
                removed: document.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]')?.checked,
                daily: document.querySelector('input[type="checkbox"][name="events[]"][value="earnings.daily"]')?.checked,
                bodyText: document.body.innerText.includes('Delivering') ? 'Delivering' : 'Not Delivering'
            };
        }''')
        print("State AFTER update:", state_after)
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
