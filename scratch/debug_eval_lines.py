import asyncio
import traceback
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import AugestelBrowserPool

async def test():
    # We can launch a single page test using Playwright to reproduce exact evaluate line
    from playwright.async_api import async_playwright
    p = await async_playwright().start()
    b = await p.chromium.launch(headless=True)
    page = await b.new_page()
    await page.goto("https://augestel.com", wait_until="domcontentloaded")
    
    paypal_email = "dimsongkang@gmail.com"
    label = "PP_123456"

    # Test line 1584
    try:
        t = await page.evaluate("() => document.body.innerText")
        print("Line 1584 OK")
    except Exception:
        traceback.print_exc()

    # Test line 1591
    try:
        res = await page.evaluate('''async (args) => {
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
                                message: xhr.responseJSON?.message || xhr.statusText || 'Error',
                                requires_2fa: !!(xhr.responseJSON?.requires_2fa)
                            });
                        }
                    });
                } else {
                    resolve({ success: false, message: 'no_jquery' });
                }
            });
        }''', {"paypal_email": paypal_email, "label": label})
        print("Line 1591 result:", res)
    except Exception:
        traceback.print_exc()

    await b.close()
    await p.stop()

if __name__ == "__main__":
    asyncio.run(test())
