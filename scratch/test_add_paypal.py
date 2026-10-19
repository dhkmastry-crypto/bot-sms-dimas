import asyncio
import os
import sys
import random
import string
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def test_modal_fields():
    user_data_dir = os.path.abspath("browser_profile_augestel_1")
    cleanup_profile_locks_and_orphans(user_data_dir)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)

        # 1. Open modal
        print("Opening Add Modal...")
        await page.evaluate("openAddModal()")
        await asyncio.sleep(0.5)

        # 2. Click PayPal (method ID 12)
        print("Selecting PayPal (method ID 12)...")
        await page.click('[data-method-id="12"]')
        await asyncio.sleep(1)

        await page.screenshot(path="scratch/step2_paypal.png")
        print("Saved step2_paypal.png")

        # 3. Inspect inputs in #addPaymentForm
        form_info = await page.evaluate('''() => {
            const form = document.querySelector('#addPaymentForm');
            if (!form) return { error: 'No form' };
            const inputs = Array.from(form.querySelectorAll('input, select, textarea')).map(i => ({
                tag: i.tagName,
                name: i.name,
                id: i.id,
                type: i.type,
                placeholder: i.placeholder,
                value: i.value,
                visible: i.offsetParent !== null
            }));

            // Check submit button
            const submitBtn = form.querySelector('button[type="submit"]');

            return {
                formAction: form.action,
                formMethod: form.method,
                inputs: inputs,
                submitBtnText: submitBtn ? submitBtn.innerText.trim() : null
            };
        }''')

        print("Form Info after selecting PayPal:")
        import json
        print(json.dumps(form_info, indent=2))

        # Check form submit handler in client JS
        submit_code = await page.evaluate('''() => {
            // Find how #addPaymentForm handles submit
            return {
                hasJQueryHandler: typeof $ !== 'undefined' && $._data ? !!($._data(document.querySelector('#addPaymentForm'), 'events') || {}).submit : false
            };
        }''')
        print("Submit code check:", submit_code)

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_modal_fields())
