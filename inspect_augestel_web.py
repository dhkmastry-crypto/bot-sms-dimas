import asyncio
import os
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("inspect_augestel")

async def main():
    with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
        accs = json.load(f)
    email = accs[0]['email']
    pwd = accs[0]['password']
    logger.info(f"Using account {email}...")

    user_data_dir = os.path.abspath("browser_profile_augestel_1")

    async with async_playwright() as p:
        try:
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
        except Exception as e:
            logger.error(f"Failed to launch browser: {e}")
            return

        page = context.pages[0] if context.pages else await context.new_page()

        # Listen to all network requests to catch API / datatable URLs
        captured_requests = []
        page.on("request", lambda req: captured_requests.append({"url": req.url, "method": req.method}))

        logger.info("Opening https://augestel.com/Switchfy...")
        await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(3)

        logger.info(f"Current page URL: {page.url}, Title: {await page.title()}")

        # Check if login form exists
        email_inp = await page.query_selector("input[name='email']")
        if email_inp:
            logger.info("Filling login form...")
            await page.fill("input[name='email']", email)
            await page.fill("input[name='password']", pwd)
            rem = await page.query_selector("input[name='remember']")
            if rem:
                try:
                    await rem.check()
                except Exception:
                    pass
            await asyncio.sleep(1)

            btn = await page.query_selector("button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")

            # Wait for redirect
            for _ in range(20):
                await asyncio.sleep(1)
                logger.info(f"Waiting redirect... URL: {page.url}, Title: {await page.title()}")
                if "/login" not in page.url and ("dashboard" in page.url.lower() or "Switchfy" in page.url):
                    break

        logger.info(f"Logged in state. Now navigating to https://augestel.com/Switchfy/test/numbers...")
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(4)

        logger.info(f"Target page URL: {page.url}, Title: {await page.title()}")
        await page.screenshot(path="switchfy_test_numbers_edge.png", full_page=True)

        content = await page.content()
        with open("switchfy_test_numbers_edge.html", "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Saved switchfy_test_numbers_edge.html (len={len(content)}) and screenshot.")

        # Inspect table and buttons on this page
        info = await page.evaluate('''() => {
            const forms = Array.from(document.querySelectorAll('form')).map(f => ({
                id: f.id,
                action: f.action,
                method: f.method,
                inputs: Array.from(f.querySelectorAll('input, select, button')).map(i => ({
                    tag: i.tagName, name: i.name, type: i.type, value: i.value, text: i.innerText
                }))
            }));
            const buttons = Array.from(document.querySelectorAll('button, a.btn, .btn')).map(b => ({
                tag: b.tagName,
                id: b.id,
                text: b.innerText ? b.innerText.trim() : '',
                href: b.href,
                onclick: b.getAttribute('onclick'),
                class: b.className
            }));
            const tables = Array.from(document.querySelectorAll('table')).map(t => ({
                id: t.id,
                headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim())
            }));
            return { forms, buttons, tables };
        }''')

        logger.info(f"Tables: {json.dumps(info['tables'], indent=2)}")
        logger.info(f"Forms: {json.dumps(info['forms'], indent=2)}")
        logger.info(f"Buttons (first 15): {json.dumps(info['buttons'][:15], indent=2)}")

        # Print all AJAX requests to see endpoint
        relevant_reqs = [r for r in captured_requests if "augestel.com" in r['url'] and not any(ext in r['url'] for ext in ['.css', '.js', '.png', '.jpg', '.woff'])]
        logger.info(f"Captured HTTP requests: {json.dumps(relevant_reqs, indent=2)}")

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
