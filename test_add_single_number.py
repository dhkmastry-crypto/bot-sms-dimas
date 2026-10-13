import asyncio
import os
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("test_add")

async def main():
    user_data_dir = os.path.abspath("browser_profile_augestel_1")

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        logger.info("Opening test numbers page...")
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle")
        await asyncio.sleep(2)

        # Get DataTable first row to see an available termination
        table_info = await page.evaluate('''() => {
            const table = $('#test-numbers-table').DataTable();
            const data = table.rows().data().toArray();
            return data.map(r => {
                // parse termination id from action html
                const match = (r.action || '').match(/data-termination-id="(\d+)"/);
                const termId = match ? match[1] : null;
                const numMatch = (r.test_number || '').match(/data-copy-number="([^"]+)"/);
                const num = numMatch ? numMatch[1] : '';
                return {
                    name: r.name,
                    test_number: num,
                    term_id: termId
                };
            }).filter(x => x.term_id !== null);
        }''')

        logger.info(f"Found {len(table_info)} rows in current page. First 3:")
        for r in table_info[:3]:
            logger.info(f"  {r}")

        if not table_info:
            logger.error("No terminations found in table!")
            await ctx.close()
            return

        target = table_info[0]
        term_id = target["term_id"]
        logger.info(f"Targeting termination: {target['name']} (ID={term_id})")

        # Call step 1: fetch termination info
        step1_res = await page.evaluate('''async (termId) => {
            const cfg = window.__cfg_clients_add_number_test || {};
            const url = cfg.k3 || 'https://augestel.com/Switchfy/client/numbers/terminations';
            
            try {
                const resp = await $.ajax({
                    url: url,
                    type: 'GET',
                    cache: false,
                    data: { termination_id: termId, _: Date.now() }
                });
                return { ok: true, data: resp, cfg: cfg };
            } catch(e) {
                return { ok: false, status: e.status, responseText: e.responseText };
            }
        }''', term_id)

        logger.info(f"Step 1 result: {json.dumps(step1_res, indent=2)}")

        if not step1_res.get("ok"):
            logger.error("Step 1 failed!")
            await ctx.close()
            return

        data = step1_res["data"]
        cfg = step1_res.get("cfg", {})
        if not data.get("success") or not data.get("terminations"):
            logger.error("No termination data in step 1 response!")
            await ctx.close()
            return

        term = data["terminations"][0]
        logger.info(f"Termination details: name={term.get('name')}, available={term.get('available_count')}, request_token={term.get('request_token')}")

        # Call step 2: Request number
        step2_res = await page.evaluate('''async (args) => {
            const { url, token, termId, requestToken, termTermId } = args;
            try {
                const resp = await $.ajax({
                    url: url,
                    type: 'POST',
                    data: {
                        _token: token,
                        termination_id: termId,
                        termination_term_id: termTermId,
                        count: 1,
                        sort_type: 'random',
                        request_token: requestToken
                    }
                });
                return { ok: true, data: resp };
            } catch(e) {
                return { ok: false, status: e.status, responseJSON: e.responseJSON, text: e.responseText };
            }
        }''', {
            "url": cfg.get("k4", "https://augestel.com/Switchfy/client/numbers/request"),
            "token": cfg.get("k5"),
            "termId": term.get("id"),
            "requestToken": term.get("request_token"),
            "termTermId": term.get("terms", [{}])[0].get("id") if term.get("terms") else None
        })

        logger.info(f"Step 2 result: {json.dumps(step2_res, indent=2)}")

        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
