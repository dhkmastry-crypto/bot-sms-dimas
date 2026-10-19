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

async def run():
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
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        print("Navigating to https://augestel.com ...")
        resp = await page.goto("https://augestel.com", wait_until="domcontentloaded")
        print("Landing URL:", page.url, "Status:", resp.status if resp else "None")
        await asyncio.sleep(2)

        print("Navigating to https://augestel.com/Switchfy/client/payment-methods ...")
        resp2 = await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        print("URL now:", page.url, "Title:", await page.title())

        # Check if login form is present
        login_el = await page.query_selector("#loginEmail, input[name='email']")
        if login_el:
            print(f"Login required for {email}. Filling form...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            
            try:
                cb = await page.query_selector("input[name='remember']")
                if cb:
                    await cb.check()
            except Exception:
                pass

            btn = await page.query_selector("#loginForm button[type='submit'], button[type='submit'], #loginSubmit")
            if btn:
                print("Clicking submit button...")
                await btn.click()
            else:
                print("Pressing enter...")
                await page.keyboard.press("Enter")

            for i in range(12):
                await asyncio.sleep(1)
                u = page.url
                t = await page.title()
                print(f"[{i+1}s] URL: {u} | Title: {t}")
                if "/client/" in u or "/dashboard" in u or "payment-methods" in u:
                    print("Logged in successfully!")
                    break
        
        # Now check if on payment-methods
        if "/payment-methods" not in page.url:
            await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
            await asyncio.sleep(2)

        page_text = await page.evaluate("() => document.body.innerText")
        print("Has PayPal already:", "PayPal" in page_text or "paypal" in page_text.lower())
        
        if "PayPal" in page_text:
            print("SUCCESS: PayPal is already configured on Account #2!")
        else:
            # Add PayPal
            rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
            label = f"PP_{rnd_suffix}"
            print(f"Adding PayPal with email dimsongkang@gmail.com and label {label} ...")
            
            res = await page.evaluate('''async (args) => {
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
                            resolve({ success: true, message: resp?.message || 'Success' });
                        },
                        error: function(xhr) {
                            resolve({ 
                                success: false, 
                                status: xhr.status, 
                                message: xhr.responseJSON?.message || xhr.statusText || 'Error'
                            });
                        }
                    });
                });
            ''', {"paypal_email": "dimsongkang@gmail.com", "label": label})
            
            print("AJAX result:", res)
            await asyncio.sleep(2)
            await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
            final_text = await page.evaluate("() => document.body.innerText")
            print("Verified PayPal:", "PayPal" in final_text)

        await page.screenshot(path="scratch/acc2_pm_final.png")
        print("Screenshot saved to scratch/acc2_pm_final.png")
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(run())
