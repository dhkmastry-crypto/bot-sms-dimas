import asyncio
from playwright.async_api import async_playwright
import os

async def inspect():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath("browser_profile_augestel_32"),
            channel="msedge",
            headless=True
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded")
        print("Page URL:", page.url)
        print("Page Title:", await page.title())
        
        # Check buttons inside form
        btns = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('button, input[type="submit"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText,
                type: b.type,
                name: b.name,
                formAction: b.form ? b.form.action : null,
                classes: b.className
            }));
        }''')
        print("Buttons found:")
        for b in btns:
            print(" ", b)
            
        # Check form inputs
        inputs = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('form input')).map(i => ({
                id: i.id,
                name: i.name,
                type: i.type,
                value: i.value,
                checked: i.checked
            }));
        }''')
        print("\nInputs found:")
        for i in inputs:
            print(" ", i)
            
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect())
