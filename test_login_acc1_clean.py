import asyncio
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def login_acc1_clean():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=cfg["user_data_dir"],
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        
        # Clear cookies to clear the throttled session
        await context.clear_cookies()
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        print("URL after clear:", page.url, "Title:", await page.title())
        
        # Fill login
        await page.fill("#loginEmail, input[name='email']", cfg["email"])
        await page.fill("#loginPassword, input[name='password']", cfg["password"])
        
        # Check Remember Me
        await page.evaluate("""() => {
            const el = document.querySelector("input[name='remember']");
            if (el) {
                el.checked = true;
                el.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }""")
        await asyncio.sleep(1)
        
        btn = await page.query_selector("#loginSubmit, button[type='submit']")
        if btn:
            await btn.click()
        else:
            await page.keyboard.press("Enter")
            
        for i in range(15):
            await asyncio.sleep(1)
            u = page.url
            t = await page.title()
            print(f"Sec {i+1}: URL={u} | Title={t}")
            if "/client/" in u or "/test/" in u or "/dashboard" in u:
                print("SUCCESSFULLY LOGGED IN!")
                await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle")
                await asyncio.sleep(2)
                break
                
        cookies = await context.cookies(["https://augestel.com"])
        has_rem = any("remember_client" in c["name"] for c in cookies)
        print(f"Cookies after login: total={len(cookies)}, remember={has_rem}")
        await context.close()

if __name__ == "__main__":
    asyncio.run(login_acc1_clean())
