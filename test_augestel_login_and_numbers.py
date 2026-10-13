import asyncio
import os
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("test_augestel")

async def main():
    with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
        accs = json.load(f)
    email = accs[0]['email']
    pwd = accs[0]['password']
    logger.info(f"Testing login for {email}...")

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

        page.on("console", lambda msg: logger.info(f"[BROWSER CONSOLE] {msg.type}: {msg.text}"))
        page.on("response", lambda resp: logger.info(f"[RESPONSE] {resp.status} {resp.url}") if "augestel.com" in resp.url and any(x in resp.url for x in ["login", "number", "test", "api"]) else None)

        logger.info("Opening https://augestel.com/Switchfy/login...")
        await page.goto("https://augestel.com/Switchfy/login", wait_until="networkidle", timeout=45000)
        logger.info(f"Loaded: {page.url} - {await page.title()}")

        email_inp = await page.query_selector("input[name='email']")
        if email_inp:
            logger.info("Filling credentials...")
            await page.fill("input[name='email']", email)
            await page.fill("input[name='password']", pwd)
            rem = await page.query_selector("input[name='remember']")
            if rem:
                try:
                    await rem.check()
                except Exception:
                    pass
            await asyncio.sleep(1)

            # Find submit button
            submit_btn = await page.query_selector("form button[type='submit'], button#login-button, .btn-primary")
            logger.info(f"Submit button found: {submit_btn}")
            if submit_btn:
                await submit_btn.click()
            else:
                await page.keyboard.press("Enter")

            logger.info("Clicked submit, waiting for navigation...")
            try:
                await page.wait_for_url(lambda u: "/login" not in u, timeout=15000)
                logger.info(f"Navigated away from login! Current URL: {page.url}")
            except Exception as e:
                logger.warning(f"wait_for_url timed out or error: {e}. Current URL: {page.url}")

        await asyncio.sleep(3)
        logger.info(f"Current URL after login attempt: {page.url} - Title: {await page.title()}")

        # Now go to https://augestel.com/Switchfy/test/numbers
        logger.info("Navigating to https://augestel.com/Switchfy/test/numbers...")
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(4)

        logger.info(f"Target page URL: {page.url} - Title: {await page.title()}")
        await page.screenshot(path="augestel_test_numbers_screen.png", full_page=True)

        content = await page.content()
        with open("augestel_test_numbers_screen.html", "w", encoding="utf-8") as f:
            f.write(content)

        # Analyze page elements
        res = await page.evaluate('''() => {
            return {
                csrfMeta: document.querySelector('meta[name="csrf-token"]')?.content || '',
                csrfInput: document.querySelector('input[name="_token"]')?.value || '',
                tables: Array.from(document.querySelectorAll('table')).map(t => ({
                    id: t.id,
                    className: t.className,
                    headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim()),
                    rowCount: t.querySelectorAll('tbody tr').length
                })),
                scripts: Array.from(document.querySelectorAll('script')).map(s => s.src || s.innerText.substring(0, 200)),
                forms: Array.from(document.querySelectorAll('form')).map(f => ({
                    id: f.id,
                    action: f.action,
                    method: f.method
                }))
            };
        }''')
        logger.info(f"Page analysis: {json.dumps(res, indent=2)}")

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
