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

async def run_single(idx=2):
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[idx - 1]
    email = acc["email"]
    password = acc["password"]

    user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
    cleanup_profile_locks_and_orphans(user_data_dir)

    rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    label = f"PP_{rnd_suffix}"
    paypal_email = "dimsongkang@gmail.com"

    print(f"[{idx}] Starting for {email} ...")
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        print(f"[{idx}] Navigating to https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)

        # Check login
        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if login_input:
            print(f"[{idx}] Logging in...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            try:
                cb = await page.query_selector("input[name='remember']")
                if cb: await cb.check()
            except Exception:
                pass
            btn = await page.query_selector("#loginForm button[type='submit'], button[type='submit'], #loginSubmit")
            if btn: await btn.click()
            
            # Wait for redirect to dashboard / live-sms
            for _ in range(15):
                await asyncio.sleep(1)
                u = page.url
                if "/client/" in u or "/dashboard" in u or "/test/" in u:
                    print(f"[{idx}] Logged in successfully! URL: {u}")
                    break

        print(f"[{idx}] Navigating to payment methods...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)

        print(f"[{idx}] Current URL: {page.url} | Title: {await page.title()}")

        body_text = await page.evaluate("() => document.body.innerText")
        if "No Payment Methods Yet" not in body_text and paypal_email in body_text:
            print(f"[{idx}] ✅ PayPal already added!")
            await ctx.close()
            return {"idx": idx, "email": email, "status": "already_exists", "success": True}

        print(f"[{idx}] Adding PayPal (label={label}, email={paypal_email})...")
        
        # Method 1: Click the Add button in the UI
        add_clicked = await page.evaluate('''() => {
            if (typeof openAddModal === 'function') {
                openAddModal();
                return 'openAddModal';
            }
            const btns = Array.from(document.querySelectorAll('button, a'));
            const addBtn = btns.find(b => b.innerText.includes('Add New Method') || b.innerText.includes('Add Your First'));
            if (addBtn) {
                addBtn.click();
                return 'btn_click';
            }
            return false;
        }''')
        print(f"[{idx}] Add modal triggered via: {add_clicked}")
        await asyncio.sleep(1.5)

        # Select PayPal in modal
        paypal_selected = await page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('[data-method-id], .payment-method-card, .method-card, div'));
            const pp = cards.find(c => c.getAttribute('data-method-id') === '12' || (c.innerText.includes('PayPal') && c.getAttribute('onclick')));
            if (pp) {
                pp.click();
                return true;
            }
            if (typeof selectMethod === 'function') {
                selectMethod(12);
                return 'selectMethod_fn';
            }
            return false;
        }''')
        print(f"[{idx}] PayPal option selected: {paypal_selected}")
        await asyncio.sleep(1)

        # Fill inputs directly in the form
        filled = await page.evaluate('''(args) => {
            const labelEl = document.querySelector('input[name="label"], #methodLabel, #label, input[placeholder*="Label"]');
            if (labelEl) {
                labelEl.value = args.label;
                labelEl.dispatchEvent(new Event('input', { bubbles: true }));
                labelEl.dispatchEvent(new Event('change', { bubbles: true }));
            }
            const emailEl = document.querySelector('input[name="payment_details[paypal_email]"], input[name*="paypal"], input[type="email"]');
            if (emailEl) {
                emailEl.value = args.email;
                emailEl.dispatchEvent(new Event('input', { bubbles: true }));
                emailEl.dispatchEvent(new Event('change', { bubbles: true }));
            }
            return { hasLabel: !!labelEl, hasEmail: !!emailEl };
        }''', {"label": label, "email": paypal_email})
        print(f"[{idx}] Inputs filled: {filled}")

        # Also submit via AJAX directly to guarantee submission
        ajax_res = await page.evaluate('''async (args) => {
            return new Promise((resolve) => {
                const token = (typeof __cfg_clients_profile_payment_methods !== 'undefined' && __cfg_clients_profile_payment_methods.k4)
                    ? __cfg_clients_profile_payment_methods.k4
                    : (document.querySelector('input[name="_token"]')?.value || '');
                const postUrl = (typeof __cfg_clients_profile_payment_methods !== 'undefined' && __cfg_clients_profile_payment_methods.k3)
                    ? __cfg_clients_profile_payment_methods.k3
                    : '/Switchfy/client/payment-methods';

                if (typeof $ !== 'undefined') {
                    $.ajax({
                        url: postUrl,
                        method: 'POST',
                        data: {
                            _token: token,
                            payment_method_id: '12',
                            label: args.label,
                            payment_details: {
                                paypal_email: args.email
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
                } else {
                    // Try fetch fallback
                    const formData = new FormData();
                    formData.append('_token', token);
                    formData.append('payment_method_id', '12');
                    formData.append('label', args.label);
                    formData.append('payment_details[paypal_email]', args.email);
                    fetch(postUrl, {
                        method: 'POST',
                        body: formData,
                        headers: { 'X-Requested-With': 'XMLHttpRequest' }
                    }).then(r => r.json()).then(data => resolve({ success: true, message: data.message }))
                      .catch(err => resolve({ success: false, message: String(err) }));
                }
            });
        }''', {"label": label, "email": paypal_email})
        print(f"[{idx}] Submission response: {ajax_res}")

        # Reload & verify
        await asyncio.sleep(2)
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)
        
        body_after = await page.evaluate("() => document.body.innerText")
        verified = ("No Payment Methods Yet" not in body_after) and (paypal_email in body_after or label in body_after)
        print(f"[{idx}] Verification: {verified}")
        
        await page.screenshot(path=f"scratch/acc_{idx}_verified.png")
        await ctx.close()
        
        return {
            "idx": idx,
            "email": email,
            "label": label,
            "status": "added" if verified else "failed",
            "success": verified,
            "ajax_res": ajax_res
        }

if __name__ == "__main__":
    idx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    res = asyncio.run(run_single(idx))
    print("Final result:", res)
