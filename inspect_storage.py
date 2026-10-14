import asyncio
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def inspect_storage():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(user_data_dir=cfg['user_data_dir'], channel='msedge', headless=True)
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto('https://augestel.com/Switchfy')
        
        cookies = await ctx.cookies()
        print('COOKIES:')
        for c in cookies:
            print(' ', c['name'], '=', c['value'][:25], 'domain:', c['domain'])
            
        local_keys = await page.evaluate('() => Object.keys(localStorage)')
        print('LOCAL STORAGE KEYS:', local_keys)
        for k in local_keys:
            v = await page.evaluate(f'() => localStorage.getItem("{k}")')
            print(f'  {k} = {v[:50]}')
            
        session_keys = await page.evaluate('() => Object.keys(sessionStorage)')
        print('SESSION STORAGE KEYS:', session_keys)
        
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect_storage())
