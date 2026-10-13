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

        # Navigate to portal root
        logger.info("Opening https://augestel.com/Switchfy...")
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle", timeout=45000)
        logger.info(f"Loaded: {page.url} - Title: {await page.title()}")

        # Check if login form is present
        email_inp = await page.query_selector("#loginEmail, input[name='email']")
        if email_inp:
            logger.info("Filling credentials into #loginEmail...")
            await page.fill("#loginEmail", email)
            await page.fill("#loginPassword", pwd)
            rem = await page.query_selector("input[name='remember']")
            if rem:
                try:
                    await rem.check()
                except Exception:
                    pass
            await asyncio.sleep(1)

            submit_btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if submit_btn:
                logger.info("Clicking #loginSubmit...")
                await submit_btn.click()
            else:
                logger.info("Pressing Enter...")
                await page.keyboard.press("Enter")

            # Wait for navigation
            for sec in range(20):
                await asyncio.sleep(1)
                curr_url = page.url
                curr_title = await page.title()
                logger.info(f"Sec {sec+1}: URL={curr_url}, Title={curr_title}")
                if "login" not in curr_title.lower() and curr_url != "https://augestel.com/Switchfy":
                    logger.info("Successfully navigated after login!")
                    break

        await asyncio.sleep(2)
        logger.info(f"Status after login attempt: URL={page.url}, Title={await page.title()}")

        # Now navigate to test numbers page
        logger.info("Navigating to https://augestel.com/Switchfy/test/numbers...")
        resp = await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(4)

        logger.info(f"Test numbers page URL: {page.url}, Title: {await page.title()}")
        await page.screenshot(path="augestel_test_numbers_page.png", full_page=True)

        content = await page.content()
        with open("augestel_test_numbers_page.html", "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Saved augestel_test_numbers_page.html (len={len(content)})")

        # Inspect tables, buttons, datatables, scripts on this page
        analysis = await page.evaluate('''() => {
            return {
                title: document.title,
                url: window.location.href,
                csrfMeta: document.querySelector('meta[name="csrf-token"]')?.content || '',
                csrfInput: document.querySelector('input[name="_token"]')?.value || '',
                tables: Array.from(document.querySelectorAll('table')).map(t => ({
                    id: t.id,
                    className: t.className,
                    headers: Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim()),
                    rowCount: t.querySelectorAll('tbody tr').length,
                    firstRowText: t.querySelector('tbody tr')?.innerText?.trim()?.substring(0, 150) || ''
                })),
                buttons: Array.from(document.querySelectorAll('button, a.btn, .btn, a')).filter(b => {
                    const txt = (b.innerText || '').toLowerCase();
                    const href = (b.getAttribute('href') || '').toLowerCase();
                    const onclick = (b.getAttribute('onclick') || '').toLowerCase();
                    return txt.includes('add') || txt.includes('test') || txt.includes('number') || 
                           href.includes('add') || onclick.includes('add');
                }).map(b => ({
                    tag: b.tagName,
                    id: b.id,
                    text: (b.innerText || '').trim(),
                    href: b.getAttribute('href'),
                    onclick: b.getAttribute('onclick'),
                    className: b.className
                })),
                forms: Array.from(document.querySelectorAll('form')).map(f => ({
                    id: f.id,
                    action: f.action,
                    method: f.method,
                    inputs: Array.from(f.querySelectorAll('input')).map(i => ({ name: i.name, type: i.type, value: i.value }))
                }))
            };
        }''')
        logger.info(f"Analysis result:\n{json.dumps(analysis, indent=2)}")

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
