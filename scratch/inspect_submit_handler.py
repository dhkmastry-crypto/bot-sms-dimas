import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect_submit():
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

        fn_text = await page.evaluate('''() => {
            const events = $._data(document.querySelector('#addPaymentForm'), 'events');
            if (events && events.submit) {
                return events.submit.map(h => h.handler.toString()).join('\\n---HANDLER---\\n');
            }
            return 'No jQuery submit handler found';
        }''')
        print("Submit Handler Code:\n", fn_text)

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(inspect_submit())
