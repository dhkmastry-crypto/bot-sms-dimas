import asyncio
import os
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("inspect_js")

async def main():
    user_data_dir = os.path.abspath("browser_profile_augestel_1")

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

        logger.info("Opening https://augestel.com/Switchfy/test/numbers...")
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)

        # Extract functions related to adding numbers
        js_data = await page.evaluate('''() => {
            const result = {};
            const fnNames = ['openAddNumberModal', 'closeAddNumberModal', 'submitModalAddNumbers', 'addNumber', 'addTestNumber'];
            for (const fn of fnNames) {
                if (typeof window[fn] === 'function') {
                    result[fn] = window[fn].toString();
                }
            }
            // Also check window config objects
            result.configs = {};
            for (const key of Object.keys(window)) {
                if (key.includes('config') || key.includes('Config') || key.includes('AddNumber') || key.includes('LaravelDataTables')) {
                    try {
                        result.configs[key] = JSON.stringify(window[key]);
                    } catch(e) {}
                }
            }
            return result;
        }''')

        for k, v in js_data.items():
            if k != "configs":
                print(f"=== FUNCTION {k} ===")
                print(v)
                print()
            else:
                print("=== CONFIGS ===")
                print(json.dumps(v, indent=2))

        # Also get table data rows from DOM or DataTable API
        table_rows = await page.evaluate('''() => {
            const table = $('#test-numbers-table').DataTable();
            if (!table) return 'No DataTable found';
            const data = table.rows().data().toArray();
            return data.slice(0, 5);
        }''')
        print("=== DATATABLE ROWS (FIRST 5) ===")
        print(json.dumps(table_rows, indent=2))

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
