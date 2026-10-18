import asyncio
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_WEBHOOK_URL = "https://dimsong.online/api/augestel/webhook"

def cleanup_profile_locks(user_data_dir: str):
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        lk_path = os.path.join(user_data_dir, lk)
        if os.path.exists(lk_path):
            try:
                os.remove(lk_path)
            except Exception:
                pass

async def test_acc(idx):
    with open(os.path.join(BASE_DIR, "augestel_accounts.json"), "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[idx - 1]
    profile_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")
    cleanup_profile_locks(profile_dir)
    print(f"Testing account #{idx}: {acc['email']}")

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
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        print("Page URL:", page.url)

        # Check state
        cur_state = await page.evaluate('''() => {
            const input = document.querySelector("#webhookUrl");
            const cb = document.querySelector('input[name="is_active"][type="checkbox"]');
            const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            const na = document.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            const nr = document.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            return {
                url: input ? input.value : "",
                is_active: cb ? cb.checked : false,
                msg: msg ? msg.checked : false,
                assigned: na ? na.checked : false,
                removed: nr ? nr.checked : false,
            };
        }''')
        print("Current State:", cur_state)

        target_url = cur_state.get("url") or DEFAULT_WEBHOOK_URL
        sub_res = await page.evaluate(f'''() => {{
            const input = document.querySelector("#webhookUrl");
            if (!input) return {{ error: "No input" }};
            const form = input.closest('form');
            const delInput = form.querySelector('input[name="_method"]');
            if (delInput) delInput.remove();
            
            input.value = "{target_url}";
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));

            const cb = form.querySelector('input[type="checkbox"][name="is_active"]');
            if (cb) {{ cb.checked = true; cb.dispatchEvent(new Event('change', {{ bubbles: true }})); }}

            const msg = form.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            if (msg) {{ msg.checked = true; msg.dispatchEvent(new Event('change', {{ bubbles: true }})); }}

            const na = form.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            if (na) {{ na.checked = false; na.dispatchEvent(new Event('change', {{ bubbles: true }})); }}

            const nr = form.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            if (nr) {{ nr.checked = false; nr.dispatchEvent(new Event('change', {{ bubbles: true }})); }}

            const updateBtn = form.querySelector('button[style*="primary-color"]') || 
                              Array.from(form.querySelectorAll('button')).find(b => b.innerText.includes('endpoint') && !b.innerText.includes('Remove'));
            if (updateBtn) {{
                updateBtn.click();
                return {{ success: true, text: updateBtn.innerText.trim() }};
            }} else {{
                form.submit();
                return {{ success: true, method: "form_submit" }};
            }}
        }}''')
        print("Submit result:", sub_res)
        await asyncio.sleep(4)
        
        final_state = await page.evaluate('''() => {
            const na = document.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            const nr = document.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            const input = document.querySelector("#webhookUrl");
            const cb = document.querySelector('input[name="is_active"][type="checkbox"]');
            const text = document.body.innerText || "";
            return {
                url: input ? input.value : "",
                is_active: cb ? cb.checked : false,
                msg: msg ? msg.checked : false,
                assigned: na ? na.checked : false,
                removed: nr ? nr.checked : false,
                is_delivering: text.includes("Delivering") && !text.includes("switched off automatically")
            };
        }''')
        print("Final State:", final_state)
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_acc(2))
