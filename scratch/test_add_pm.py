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

async def test_add_acc2():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[1] # Account 2
    email = acc["email"]
    password = acc["password"]

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

        # Navigate to payment methods
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        await asyncio.sleep(2)

        # Login if needed
        login_el = await page.query_selector("#loginEmail, input[name='email']")
        if login_el:
            print("Logging in...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            try:
                cb = await page.query_selector("input[name='remember']")
                if cb: await cb.check()
            except Exception:
                pass
            btn = await page.query_selector("#loginForm button[type='submit'], button[type='submit'], #loginSubmit")
            if btn: await btn.click()
            for _ in range(10):
                await asyncio.sleep(1)
                if "/client/" in page.url or "/dashboard" in page.url:
                    break
            await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
            await asyncio.sleep(2)

        print("Page URL:", page.url)

        # Inspect JS config object on the page
        cfg = await page.evaluate('''() => {
            return {
                cfg: typeof __cfg_clients_profile_payment_methods !== 'undefined' ? __cfg_clients_profile_payment_methods : null,
                tokenInput: document.querySelector('input[name="_token"]')?.value,
                metaCsrf: document.querySelector('meta[name="csrf-token"]')?.content,
                hasJquery: typeof $ !== 'undefined'
            };
        }''')
        print("Page JS CFG:", cfg)

        # Submit AJAX POST
        print(f"Submitting AJAX POST for PayPal (label={label}, email={paypal_email})...")
        res = await page.evaluate('''async (args) => {
            return new Promise((resolve) => {
                const token = (typeof __cfg_clients_profile_payment_methods !== 'undefined' && __cfg_clients_profile_payment_methods.k4)
                    ? __cfg_clients_profile_payment_methods.k4
                    : (document.querySelector('input[name="_token"]')?.value || document.querySelector('meta[name="csrf-token"]')?.content || '');

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
                    headers: {
                        'X-CSRF-TOKEN': token,
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    success: function(resp) {
                        resolve({ success: true, resp: resp });
                    },
                    error: function(xhr) {
                        resolve({ 
                            success: false, 
                            status: xhr.status, 
                            statusText: xhr.statusText,
                            responseText: xhr.responseText?.slice(0, 500),
                            responseJSON: xhr.responseJSON
                        });
                    }
                });
            });
        }''', {"label": label, "paypal_email": paypal_email})

        print("AJAX Response:", res)

        # Reload and check
        await asyncio.sleep(2)
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        await asyncio.sleep(2)

        check_res = await page.evaluate('''() => {
            const text = document.body.innerText;
            return {
                hasDimSongKang: text.includes('dimsongkang@gmail.com'),
                hasNoPaymentMethods: text.includes('No Payment Methods Yet'),
                textSnippet: text.slice(0, 1000)
            };
        }''')
        print("Verification Result:", check_res)

        await page.screenshot(path="scratch/acc2_verify.png")
        print("Screenshot saved to scratch/acc2_verify.png")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(test_add_acc2())
