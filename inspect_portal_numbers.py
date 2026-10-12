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
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        print("Navigating to /portal/numbers ...")
        resp = await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(4)
        print(f"Current URL: {page.url}")
        
        # Capture title and body snippet
        title = await page.title()
        print(f"Page Title: {title}")
        
        # Check if table exists
        tables = await page.evaluate("""() => {
            const list = [];
            document.querySelectorAll('table').forEach(t => {
                list.push({ id: t.id, class: t.className, headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim()) });
            });
            return list;
        }""")
        print(f"Tables found: {json.dumps(tables, indent=2)}")

        # Check scripts or datatables ajax url
        scripts_info = await page.evaluate("""() => {
            const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerHTML).filter(s => s.includes('DataTable') || s.includes('/numbers'));
            return scripts.map(s => s.substring(0, 300));
        }""")
        print(f"DataTable scripts snippet count: {len(scripts_info)}")
        for s in scripts_info[:3]:
            print("--- SCRIPT ---")
            print(s)

        # Save HTML for inspection
        content = await page.content()
        with open("debug_numbers_portal.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved debug_numbers_portal.html")
        await context.close()

if __name__ == "__main__":
    asyncio.run(inspect())
