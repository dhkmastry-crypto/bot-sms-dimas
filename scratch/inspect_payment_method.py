import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect():
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
        print("Navigating to https://augestel.com/Switchfy/client/payment-methods ...")
        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)
        print("Current URL:", page.url)
        print("Page Title:", await page.title())

        # Screenshot to inspect visually
        os.makedirs("scratch", exist_ok=True)
        await page.screenshot(path="scratch/payment_methods_page.png")
        print("Saved screenshot to scratch/payment_methods_page.png")

        # Inspect DOM for buttons, links, forms, tables
        info = await page.evaluate('''() => {
            const btns = Array.from(document.querySelectorAll('button, a.btn, a[href*="create"], a[href*="add"], input[type="submit"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText.trim(),
                href: b.href || null,
                id: b.id || null,
                classes: b.className || null
            }));
            const forms = Array.from(document.querySelectorAll('form')).map(f => ({
                action: f.action,
                method: f.method,
                id: f.id,
                inputs: Array.from(f.querySelectorAll('input, select, textarea')).map(i => ({
                    tag: i.tagName,
                    name: i.name,
                    id: i.id,
                    type: i.type,
                    placeholder: i.placeholder,
                    value: i.value
                }))
            }));
            const bodyTextSnippet = document.body.innerText.slice(0, 1500);
            return { btns, forms, bodyTextSnippet };
        }''')
        
        print("Buttons/Links:", info["btns"])
        print("Forms:", info["forms"])
        print("Body snippet:\n", info["bodyTextSnippet"])

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect())
