import asyncio
import re
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def inspect_login():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(user_data_dir=cfg['user_data_dir'], channel='msedge', headless=True)
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto('https://augestel.com/Switchfy')
        print('URL:', page.url, 'Title:', await page.title())
        content = await page.content()
        forms = re.findall(r'<form[^>]*>', content)
        print('Forms:', forms)
        inputs = re.findall(r'<input[^>]*>', content)
        for inp in inputs:
            print('Input:', inp)
        wait_span = await page.query_selector('.wait')
        if wait_span:
            print('Wait span:', await wait_span.inner_text())
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect_login())
