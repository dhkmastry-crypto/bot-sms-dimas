import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect():
    with open("augestel_accounts.json", "r", encoding="utf-8") as f:
        accounts = json.load(f)
    acc = accounts[0]
    email = acc["email"]
    password = acc["password"]

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

        # Step 1: Ensure logged in via https://augestel.com/Switchfy
        print("Checking session via https://augestel.com/Switchfy ...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle", timeout=30000)
        curr_url = page.url
        print("URL after /Switchfy:", curr_url)

        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if login_input:
            print(f"Logging in as {email}...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")
            await page.wait_for_load_state("networkidle")
            print("Post-login URL:", page.url)

        # Step 2: Navigate to payment methods page
        print("Navigating to https://augestel.com/Switchfy/client/payment-methods ...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)
        print("Payment Methods URL:", page.url)
        print("Page Title:", await page.title())

        os.makedirs("scratch", exist_ok=True)
        await page.screenshot(path="scratch/payment_methods_page.png")
        print("Saved screenshot to scratch/payment_methods_page.png")

        # Step 3: Inspect DOM
        info = await page.evaluate('''() => {
            const btns = Array.from(document.querySelectorAll('button, a.btn, a[href*="payment"], a[href*="create"], a[href*="add"], input[type="submit"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText.trim(),
                href: b.href || null,
                id: b.id || null,
                classes: b.className || null,
                onclick: b.getAttribute('onclick') || null,
                dataTarget: b.getAttribute('data-target') || b.getAttribute('data-bs-target') || null,
                dataToggle: b.getAttribute('data-toggle') || b.getAttribute('data-bs-toggle') || null
            }));

            const forms = Array.from(document.querySelectorAll('form')).map(f => ({
                action: f.action,
                method: f.method,
                id: f.id,
                classes: f.className,
                inputs: Array.from(f.querySelectorAll('input, select, textarea')).map(i => ({
                    tag: i.tagName,
                    name: i.name,
                    id: i.id,
                    type: i.type,
                    placeholder: i.placeholder,
                    value: i.value,
                    options: i.tagName === 'SELECT' ? Array.from(i.options).map(o => ({ value: o.value, text: o.text })) : null
                }))
            }));

            const modals = Array.from(document.querySelectorAll('.modal')).map(m => ({
                id: m.id,
                title: m.querySelector('.modal-title') ? m.querySelector('.modal-title').innerText.trim() : null,
                inputs: Array.from(m.querySelectorAll('input, select, textarea')).map(i => ({
                    tag: i.tagName,
                    name: i.name,
                    id: i.id,
                    type: i.type,
                    placeholder: i.placeholder,
                    options: i.tagName === 'SELECT' ? Array.from(i.options).map(o => ({ value: o.value, text: o.text })) : null
                }))
            }));

            const tables = Array.from(document.querySelectorAll('table')).map(t => ({
                id: t.id,
                headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim()),
                rowsCount: t.querySelectorAll('tbody tr').length
            }));

            return { btns, forms, modals, tables, bodySnippet: document.body.innerText.slice(0, 1000) };
        }''')

        print("=== MODALS ===")
        print(json.dumps(info["modals"], indent=2))
        print("=== BUTTONS ===")
        print(json.dumps(info["btns"], indent=2))
        print("=== FORMS ===")
        print(json.dumps(info["forms"], indent=2))
        print("=== TABLES ===")
        print(json.dumps(info["tables"], indent=2))
        print("=== BODY SNIPPET ===")
        print(info["bodySnippet"])

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect())
