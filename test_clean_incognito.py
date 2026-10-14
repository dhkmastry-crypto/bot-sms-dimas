import asyncio
import json
from playwright.async_api import async_playwright

async def test_clean_login():
    with open('augestel_accounts.json') as f:
        accs = json.load(f)
    acc1 = accs[0]
    
    async with async_playwright() as p:
        # Pure incognito browser, no persistent profile
        browser = await p.chromium.launch(channel="msedge", headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto('https://augestel.com/Switchfy')
        await asyncio.sleep(1)
        print("Page loaded:", page.url, "Title:", await page.title())
        
        await page.fill('#loginEmail', acc1['email'])
        await page.fill('#loginPassword', acc1['password'])
        
        btn = await page.query_selector('#loginSubmit')
        if btn:
            await btn.click()
            
        for i in range(10):
            await asyncio.sleep(1)
            u = page.url
            t = await page.title()
            print(f"Sec {i+1}: URL={u} | Title={t}")
            if "/test/" in u or "/client/" in u or "/dashboard" in u:
                print("SUCCESSFUL LOGIN!")
                break
                
        card = await page.query_selector('.card')
        if card:
            print("Card text:", repr(await card.inner_text()))
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_clean_login())
