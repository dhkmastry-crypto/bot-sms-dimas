import asyncio
from playwright.async_api import async_playwright

async def t():
    p = await async_playwright().start()
    b = await p.chromium.launch(headless=True)
    pg = await b.new_page()
    
    # Test 1: object arg with async (args) => { ... }
    try:
        res1 = await pg.evaluate('''async (args) => {
            return args.a + args.b;
        }''', {"a": "hello ", "b": "world"})
        print("Test 1 success:", res1)
    except Exception as e:
        print("Test 1 error:", e)

    # Test 2: wrapped in parens
    try:
        res2 = await pg.evaluate('''(async (args) => {
            return args.a + args.b;
        })''', {"a": "hello ", "b": "world"})
        print("Test 2 success:", res2)
    except Exception as e:
        print("Test 2 error:", e)

    # Test 3: without async/arrow, or string interpolation
    try:
        email = "foo@bar.com"
        label = "test"
        res3 = await pg.evaluate(f'''() => {{
            return '{email}' + ' ' + '{label}';
        }}''')
        print("Test 3 success:", res3)
    except Exception as e:
        print("Test 3 error:", e)

    await b.close()
    await p.stop()

if __name__ == "__main__":
    asyncio.run(t())
