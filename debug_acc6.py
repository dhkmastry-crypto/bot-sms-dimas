import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

async def inspect_acc6():
    pdir = os.path.abspath("browser_profile_augestel_6")
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=pdir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle")
        
        print("Akun 6 Initial URL:", page.url)
        print("Akun 6 Initial Title:", await page.title())
        
        # Check wait
        wait_el = await page.query_selector(".wait")
        if wait_el:
            print("Cooldown on Akun 6:", await wait_el.inner_text())
            
        # Try fill login
        await page.fill("#loginEmail, input[name='email']", "pakupakuwak@gmail.com")
        await page.fill("#loginPassword, input[name='password']", "Nathan27@")
        
        try:
            await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) el.checked = true; }")
        except Exception:
            pass
            
        btn = await page.query_selector("#loginSubmit, form button[type='submit']")
        if btn:
            await btn.click()
            
        await page.wait_for_timeout(4000)
        
        print("After submit URL:", page.url)
        print("After submit Title:", await page.title())
        
        # Check alerts or errors
        alerts = await page.query_selector_all(".alert, .toast, .text-danger, .text-red-500, [role='alert'], .wait")
        for a in alerts:
            t = await a.inner_text()
            if t.strip():
                print("Alert:", t.strip())
                
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect_acc6())
