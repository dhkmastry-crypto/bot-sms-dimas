import asyncio
import os
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("test_acc2")

async def ensure_augestel_login(page, email, password):
    logger.info(f"Checking login status for {email}...")
    await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
    await asyncio.sleep(2)
    
    title = await page.title()
    login_input = await page.query_selector("#loginEmail, input[name='email']")
    if "login" in title.lower() or login_input:
        logger.info(f"Not logged in. Performing login for {email}...")
        # If on another page, go to Switchfy
        if not login_input:
            await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)
        
        await page.fill("#loginEmail, input[name='email']", email)
        await page.fill("#loginPassword, input[name='password']", password)
        rem = await page.query_selector("input[name='remember']")
        if rem:
            try:
                await rem.check()
            except Exception:
                pass
        await asyncio.sleep(1)
        
        btn = await page.query_selector("#loginSubmit, button[type='submit']")
        if btn:
            await btn.click()
        else:
            await page.keyboard.press("Enter")
            
        for _ in range(15):
            await asyncio.sleep(1)
            t = await page.title()
            u = page.url
            if "login" not in t.lower() and u != "https://augestel.com/Switchfy":
                logger.info(f"Login success! Landed on {u}")
                break
        
        # Navigate to test numbers
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)

    logger.info(f"Ready on test numbers page: {page.url} - {await page.title()}")
    return True

async def main():
    with open('augestel_accounts.json', 'r', encoding='utf-8') as f:
        accs = json.load(f)
    acc2 = accs[1]
    email = acc2['email']
    pwd = acc2['password']

    user_data_dir = os.path.abspath("browser_profile_augestel_2")

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        ok = await ensure_augestel_login(page, email, pwd)
        logger.info(f"Result for acc2: {ok}")
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
