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

async def test_acc2():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[1] # Account #2
    email = acc["email"]
    password = acc["password"]

    user_data_dir = os.path.abspath("browser_profile_augestel_2")
    cleanup_profile_locks_and_orphans(user_data_dir)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        # Step 1: Ensure login
        print(f"Ensuring login for Account #2 ({email})...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle", timeout=30000)

        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if login_input:
            print("Form login detected, submitting credentials...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
            await page.wait_for_load_state("networkidle")
            print("After login URL:", page.url)

        # Step 2: Go to payment-methods
        print("Navigating to https://augestel.com/Switchfy/client/payment-methods ...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)
        print("Page URL:", page.url)

        # Check existing payment methods
        existing = await page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('.rounded-2xl, .rounded-xl')).filter(el => {
                const txt = el.innerText || '';
                return txt.includes('PayPal') || txt.includes('Tether') || txt.includes('Cash');
            }).map(el => el.innerText.trim());

            const body = document.body.innerText;
            return {
                hasPayPal: body.includes('PayPal'),
                hasUSDT: body.includes('Tether (USDT)'),
                bodySnippet: body.slice(0, 800)
            };
        }''')
        print("Existing check on Account #2:", existing)

        # Step 3: If no PayPal, try adding PayPal!
        if not existing["hasPayPal"]:
            print("Account #2 does NOT have PayPal. Adding now...")
            # Generate random label
            rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            label = f"PP_{rnd_suffix}"
            print(f"Using label: {label}, paypal email: dimsongkang@gmail.com")

            # Open modal
            await page.evaluate("openAddModal()")
            await asyncio.sleep(1)

            # Click PayPal
            await page.click('[data-method-id="12"]')
            await asyncio.sleep(1)

            # Fill form
            await page.fill('input[name="label"]', label)
            await page.fill('input[name="payment_details[paypal_email]"]', 'dimsongkang@gmail.com')
            
            # Submit via button click or function
            print("Submitting form...")
            result = await page.evaluate('''async () => {
                return new Promise((resolve) => {
                    const form = $('#addPaymentForm');
                    const formData = {};
                    form.serializeArray().forEach(item => {
                        if (item.name.includes('[')) {
                            const matches = item.name.match(/(.+)\[(.+)\]/);
                            if (matches) {
                                if (!formData[matches[1]]) formData[matches[1]] = {};
                                formData[matches[1]][matches[2]] = item.value;
                            }
                        } else {
                            formData[item.name] = item.value;
                        }
                    });

                    $.ajax({
                        url: __cfg_clients_profile_payment_methods.k3,
                        method: 'POST',
                        data: {
                            _token: __cfg_clients_profile_payment_methods.k4,
                            ...formData
                        },
                        success: function(resp) {
                            resolve({ success: true, response: resp });
                        },
                        error: function(xhr) {
                            resolve({ 
                                success: false, 
                                status: xhr.status, 
                                responseJSON: xhr.responseJSON,
                                responseText: xhr.responseText ? xhr.responseText.slice(0, 500) : ''
                            });
                        }
                    });
                });
            }''')
            print("AJAX Result:", json.dumps(result, indent=2))
            await asyncio.sleep(2)
            await page.screenshot(path="scratch/acc2_after_add.png")
            print("Saved scratch/acc2_after_add.png")
        else:
            print("Account #2 ALREADY has PayPal!")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_acc2())
