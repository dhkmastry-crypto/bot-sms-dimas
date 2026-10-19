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

        print(f"--- Processing Account #2: {email} ---")
        await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)

        # Check if login form is present
        login_el = await page.query_selector("#loginEmail")
        if login_el:
            print("🔑 Login required. Filling credentials...")
            await page.fill("#loginEmail", email)
            await page.fill("#loginPassword", password)
            try:
                await page.evaluate('''() => {
                    const el = document.querySelector("input[name='remember']");
                    if (el) { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); }
                }''')
            except Exception:
                pass
            await asyncio.sleep(0.5)
            await page.click("#loginSubmit")
            
            # Wait for dashboard/client
            logged_in = False
            for _ in range(15):
                await asyncio.sleep(1)
                if "/client/" in page.url or "/dashboard" in page.url:
                    logged_in = True
                    break
            print(f"Login success: {logged_in}, URL: {page.url}")
            if not logged_in:
                print("❌ Failed to log in!")
                await ctx.close()
                return

        # Now go to payment methods
        print("Navigating to payment methods...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=45000)
        print("Payment Methods URL:", page.url)

        # Check existing payment methods
        body_text = await page.evaluate("() => document.body.innerText")
        if "PayPal" in body_text:
            print("✅ PayPal is ALREADY added to this account!")
            await ctx.close()
            return

        print("Adding PayPal now...")
        # Random label
        rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        label = f"PP_{rnd_suffix}"
        print(f"Label: {label}")

        # Open Add Modal
        await page.evaluate("openAddModal()")
        await asyncio.sleep(1)

        # Click PayPal
        await page.click('[data-method-id="12"]')
        await asyncio.sleep(1)

        # Fill details
        await page.fill('input[name="label"]', label)
        await page.fill('input[name="payment_details[paypal_email]"]', 'dimsongkang@gmail.com')

        # Execute AJAX submission directly via page
        res = await page.evaluate('''async () => {
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
                            responseJSON: xhr.responseJSON 
                        });
                    }
                });
            });
        }''')

        print("AJAX Response:", json.dumps(res, indent=2))
        await asyncio.sleep(2)
        await page.screenshot(path="scratch/acc2_success.png")
        print("Screenshot saved to scratch/acc2_success.png")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_acc2())
