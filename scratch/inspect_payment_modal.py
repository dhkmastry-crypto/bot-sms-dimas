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

        await page.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle", timeout=30000)

        details = await page.evaluate('''() => {
            const addModal = document.querySelector('#addModal, [id*="addModal"], [id*="AddModal"], [class*="modal"]');
            const form = document.querySelector('#addPaymentForm');
            
            // Look for any scripts containing openAddModal
            const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText).filter(t => t.includes('openAddModal') || t.includes('addPaymentForm'));

            return {
                addModalHtml: addModal ? addModal.outerHTML : (form ? form.closest('div').outerHTML : 'Not found'),
                scriptsSnippet: scripts.join('\\n---SCRIPT---\\n')
            };
        }''')

        print("=== MODAL HTML ===")
        print(details["addModalHtml"][:3000])
        print("\n=== SCRIPT SNIPPET ===")
        print(details["scriptsSnippet"][:4000])

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect())
