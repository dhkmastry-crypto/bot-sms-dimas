import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def dump_html():
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
        content = await page.content()
        with open("scratch/payment_methods_dump.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Dumped HTML, size:", len(content))

        # Now test clicking openAddModal() and see what appears!
        print("Clicking Add New Method...")
        await page.evaluate("openAddModal()")
        await asyncio.sleep(1)
        await page.screenshot(path="scratch/after_open_add_modal.png")
        print("Screenshot saved to scratch/after_open_add_modal.png")

        # Check what became visible
        visible_info = await page.evaluate('''() => {
            const visibleModals = Array.from(document.querySelectorAll('div, form')).filter(el => {
                const style = window.getComputedStyle(el);
                return style.display !== 'none' && style.visibility !== 'hidden' && (el.id.toLowerCase().includes('modal') || el.id.toLowerCase().includes('add'));
            }).map(el => ({ id: el.id, className: el.className, textSnippet: el.innerText.slice(0, 300) }));

            return visibleModals;
        }''')
        print("Visible modals/containers:", visible_info)

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(dump_html())
