import asyncio
import os
import sys
import json
import random
import string
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def add_paypal_acc2():
    user_data_dir = os.path.abspath("browser_profile_augestel_2")
    cleanup_profile_locks_and_orphans(user_data_dir)

    rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    label = f"PP_{rnd_suffix}"
    paypal_email = "dimsongkang@gmail.com"

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        print("Opening payment-methods page...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        await asyncio.sleep(2)

        print("Current URL:", page.url)
        print("Page Title:", await page.title())

        # Click "+ Add New Method" button or call openAddModal()
        print("Opening Add Modal...")
        await page.evaluate('''() => {
            if (typeof openAddModal === 'function') {
                openAddModal();
            } else {
                const btn = document.querySelector('button:has-text("Add New Method"), button:has-text("Add Your First Payment Method")') || document.querySelector('.btn-primary');
                if (btn) btn.click();
            }
        }''')
        await asyncio.sleep(1.5)

        # In modal, select PayPal
        print("Selecting PayPal method (data-method-id=12)...")
        await page.evaluate('''() => {
            // Click the card with data-method-id="12" or containing text "PayPal"
            const card = document.querySelector('[data-method-id="12"]') || 
                         Array.from(document.querySelectorAll('.payment-method-card, .method-card, .cursor-pointer')).find(el => el.innerText.includes('PayPal'));
            if (card) {
                card.click();
            } else if (typeof selectMethod === 'function') {
                selectMethod(12);
            }
        }''')
        await asyncio.sleep(1.5)

        # Fill label and email
        print(f"Filling Label: {label} and Email: {paypal_email} ...")
        
        # Try both direct fill and DOM evaluation
        await page.evaluate('''(args) => {
            const labelInput = document.querySelector('input[name="label"], #methodLabel, #label');
            if (labelInput) {
                labelInput.value = args.label;
                labelInput.dispatchEvent(new Event('input', { bubbles: true }));
                labelInput.dispatchEvent(new Event('change', { bubbles: true }));
            }

            const emailInput = document.querySelector('input[name="payment_details[paypal_email]"], input[name*="paypal"], input[type="email"]');
            if (emailInput) {
                emailInput.value = args.paypal_email;
                emailInput.dispatchEvent(new Event('input', { bubbles: true }));
                emailInput.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }''', {"label": label, "paypal_email": paypal_email})

        await page.screenshot(path="scratch/acc2_modal_filled.png")
        print("Screenshot saved to scratch/acc2_modal_filled.png")

        # Submit via AJAX or submit button
        print("Submitting PayPal addition...")
        submit_res = await page.evaluate('''async (args) => {
            return new Promise((resolve) => {
                const token = (typeof __cfg_clients_profile_payment_methods !== 'undefined' && __cfg_clients_profile_payment_methods.k4)
                    ? __cfg_clients_profile_payment_methods.k4
                    : (document.querySelector('input[name="_token"]')?.value || '');

                const postUrl = (typeof __cfg_clients_profile_payment_methods !== 'undefined' && __cfg_clients_profile_payment_methods.k3)
                    ? __cfg_clients_profile_payment_methods.k3
                    : '/Switchfy/client/payment-methods';

                $.ajax({
                    url: postUrl,
                    method: 'POST',
                    data: {
                        _token: token,
                        payment_method_id: '12',
                        label: args.label,
                        payment_details: {
                            paypal_email: args.paypal_email
                        }
                    },
                    success: function(resp) {
                        resolve({ success: true, message: resp?.message || 'Success', resp: resp });
                    },
                    error: function(xhr) {
                        resolve({ 
                            success: false, 
                            status: xhr.status, 
                            message: xhr.responseJSON?.message || xhr.statusText || 'Error',
                            json: xhr.responseJSON
                        });
                    }
                });
            });
        }''', {"label": label, "paypal_email": paypal_email})

        print("AJAX Submission Result:", submit_res)

        await asyncio.sleep(2)
        # Reload payment methods to verify
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        await asyncio.sleep(2)

        page_info = await page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('.card, tr, .payment-item')).map(c => c.innerText.trim());
            return {
                bodyText: document.body.innerText,
                hasPayPalInMyMethods: !document.body.innerText.includes('No Payment Methods Yet') && document.body.innerText.includes('PayPal')
            };
        }''')

        print("Has PayPal in My Payment Methods:", page_info["hasPayPalInMyMethods"])
        await page.screenshot(path="scratch/acc2_pm_success.png")
        print("Final screenshot saved to scratch/acc2_pm_success.png")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(add_paypal_acc2())
