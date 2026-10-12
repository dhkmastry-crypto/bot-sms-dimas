import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

async def inspect():
    user_data_dir = os.path.abspath("browser_profile")
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=-2000,-2000",
            ]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        print("Navigating to /portal/numbers ...")
        await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
        
        for _ in range(30):
            title = await page.title()
            if "Just a moment" not in title:
                break
            await asyncio.sleep(1)
            
        await asyncio.sleep(4)
        print(f"Current URL: {page.url}")
        print(f"Page Title: {await page.title()}")

        # Check tables & columns
        info = await page.evaluate("""() => {
            const tables = Array.from(document.querySelectorAll('table')).map(t => ({
                id: t.id,
                className: t.className,
                headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim())
            }));
            const cardHeaders = Array.from(document.querySelectorAll('.card-header, .card-title, h1, h2, h3, h4, .badge')).map(e => e.innerText.trim());
            return { tables, cardHeaders };
        }""")
        print(f"Info: {json.dumps(info, indent=2)}")

        # Check DataTables settings or AJAX calls
        scripts_ajax = await page.evaluate("""() => {
            const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerHTML).filter(s => s.includes('DataTable') || s.includes('ajax') || s.includes('numbers'));
            return scripts.map(s => s.substring(0, 500));
        }""")
        print(f"AJAX Scripts count: {len(scripts_ajax)}")
        for i, s in enumerate(scripts_ajax):
            print(f"=== SCRIPT {i+1} ===")
            print(s)

        # Look for any network endpoint mentioned in HTML
        html = await page.content()
        with open("debug_numbers_portal.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Written debug_numbers_portal.html successfully")
        await context.close()

if __name__ == "__main__":
    asyncio.run(inspect())
