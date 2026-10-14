import asyncio
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def debug_login():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=cfg["user_data_dir"],
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        print("Initial URL:", page.url, "Title:", await page.title())
        
        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if login_input:
            print("Found login form, filling credentials...")
            await page.fill("#loginEmail, input[name='email']", cfg["email"])
            await page.fill("#loginPassword, input[name='password']", cfg["password"])
            
            # Check remember me
            await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); } }")
            
            # Check if there is cooldown on page before clicking submit
            wait_el = await page.query_selector(".wait")
            if wait_el:
                print("Wait countdown found before submit:", await wait_el.inner_text())
                
            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                print("Clicking submit button...")
                await btn.click()
            
            # Monitor for 15 seconds
            for i in range(15):
                await asyncio.sleep(1)
                u = page.url
                t = await page.title()
                wait_el = await page.query_selector(".wait")
                w_txt = (await wait_el.inner_text()).strip() if wait_el else None
                err_el = await page.query_selector(".alert-danger, .invalid-feedback, .error")
                err_txt = (await err_el.inner_text()).strip() if err_el else None
                print(f"Sec {i+1}: URL={u} | Title={t} | wait={w_txt} | err={err_txt}")
                if "/test/" in u or "/client/" in u:
                    print("SUCCESS LOGGED IN!")
                    break

        await context.close()

if __name__ == "__main__":
    asyncio.run(debug_login())
