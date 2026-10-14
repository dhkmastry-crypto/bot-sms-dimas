import asyncio
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def inspect_post():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(user_data_dir=cfg['user_data_dir'], channel='msedge', headless=True)
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto('https://augestel.com/Switchfy', wait_until='domcontentloaded')
        await asyncio.sleep(1)
        
        await page.fill('#loginEmail', cfg['email'])
        await page.fill('#loginPassword', cfg['password'])
        
        # Check Remember Me
        rem = await page.query_selector("input[name='remember']")
        if rem:
            await rem.check()
            
        print("Submitting form...")
        async with page.expect_navigation(timeout=15000):
            await page.click('#loginSubmit')
            
        print("After nav URL:", page.url)
        print("After nav Title:", await page.title())
        content = await page.content()
        print("Content sample:", content[:1000])
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect_post())
