import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

async def test_fetch():
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
        print("Navigating to https://www.ivasms.com/portal/numbers ...")
        await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
        
        for _ in range(30):
            title = await page.title()
            if "Just a moment" not in title:
                break
            await asyncio.sleep(1)
        await asyncio.sleep(3)

        # Call DataTable AJAX from inside the page
        res = await page.evaluate("""async () => {
            try {
                const url = new URL('/portal/numbers', window.location.origin);
                url.searchParams.set('draw', '1');
                url.searchParams.set('start', '0');
                url.searchParams.set('length', '10');
                
                const cols = [
                    { data: 'number_id', name: 'id', searchable: true, orderable: false },
                    { data: 'Number', name: 'Number', searchable: true, orderable: true },
                    { data: 'range', name: 'range', searchable: true, orderable: true },
                    { data: 'A2P', name: 'A2P', searchable: true, orderable: true },
                    { data: 'LimitA2P', name: 'LimitA2P', searchable: true, orderable: true },
                    { data: 'limit_cli_a2p', name: 'limit_cli_a2p', searchable: true, orderable: true },
                    { data: 'limit_cli_did_a2p', name: 'limit_cli_did_a2p', searchable: true, orderable: true },
                    { data: 'action', name: 'action', searchable: false, orderable: false }
                ];

                cols.forEach((col, idx) => {
                    url.searchParams.set(`columns[${idx}][data]`, col.data);
                    url.searchParams.set(`columns[${idx}][name]`, col.name);
                    url.searchParams.set(`columns[${idx}][searchable]`, col.searchable ? 'true' : 'false');
                    url.searchParams.set(`columns[${idx}][orderable]`, col.orderable ? 'true' : 'false');
                    url.searchParams.set(`columns[${idx}][search][value]`, '');
                    url.searchParams.set(`columns[${idx}][search][regex]`, 'false');
                });

                url.searchParams.set('order[0][column]', '1');
                url.searchParams.set('order[0][dir]', 'desc');
                url.searchParams.set('search[value]', '');
                url.searchParams.set('search[regex]', 'false');

                const resp = await fetch(url.toString(), {
                    method: 'GET',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept': 'application/json, text/javascript, */*; q=0.01'
                    }
                });
                return await resp.json();
            } catch(e) {
                return { error: e.message };
            }
        }""")

        print("AJAX Response Keys:", list(res.keys()) if isinstance(res, dict) else type(res))
        if isinstance(res, dict):
            print("recordsTotal:", res.get("recordsTotal"))
            print("recordsFiltered:", res.get("recordsFiltered"))
            data_sample = res.get("data", [])
            print(f"data count in sample: {len(data_sample)}")
            if data_sample:
                print("First row:", data_sample[0])

        await context.close()

if __name__ == "__main__":
    asyncio.run(test_fetch())
