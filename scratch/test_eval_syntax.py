import asyncio
from playwright.async_api import async_playwright

async def t():
    p = await async_playwright().start()
    b = await p.chromium.launch(headless=True)
    pg = await b.new_page()
    
    label = "PP_123456"
    paypal_email = "dimsongkang@gmail.com"
    
    res = await pg.evaluate(f'''() => new Promise((resolve) => {{
        resolve({{ success: true, email: "{paypal_email}", label: "{label}" }});
    }})''')
    print("Eval result:", res)

    await b.close()
    await p.stop()

if __name__ == "__main__":
    asyncio.run(t())
