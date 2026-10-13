import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"

async def retry_acc6():
    pdir = os.path.abspath("browser_profile_augestel_6")
    print("⏳ Menunggu cooldown anti-spam portal Augestel untuk Akun #6 selesai...")
    
    while True:
        async with async_playwright() as p:
            ctx = await p.chromium.launch_persistent_context(
                user_data_dir=pdir,
                channel="msedge",
                headless=False,
                args=["--window-position=-2000,-2000"]
            )
            page = ctx.pages[0] if ctx.pages else await ctx.new_page()
            try:
                await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(2)
                
                # Cek jika sudah terpasang
                wh_input = await page.query_selector("#webhookUrl")
                if wh_input:
                    val = await page.evaluate('() => document.querySelector("#webhookUrl").value')
                    active = await page.evaluate('() => document.querySelector("input[name=\'is_active\'][type=\'checkbox\']").checked')
                    if val == WEBHOOK_URL and active:
                        print("🎉 Akun #6 sudah aktif terpasang Webhook!")
                        await ctx.close()
                        break
                    else:
                        await wh_input.fill(WEBHOOK_URL)
                        cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
                        if cb and not await cb.is_checked():
                            await cb.check()
                        msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
                        if msg_cb and not await msg_cb.is_checked():
                            await msg_cb.check()
                        save_btn = await page.query_selector('form[action*="webhook"] button[type="submit"]')
                        async with page.expect_navigation(timeout=15000):
                            await save_btn.click()
                        print("🎉 Akun #6 Webhook BERHASIL dipasang!")
                        await ctx.close()
                        break
                        
                # Cek cooldown timer
                wait_el = await page.query_selector(".wait")
                if wait_el:
                    wait_sec = int((await wait_el.inner_text()).strip() or "60")
                    print(f"⏳ Cooldown Akun #6: tersisa {wait_sec} detik. Tidur {min(wait_sec + 2, 60)} detik...")
                    await ctx.close()
                    await asyncio.sleep(min(wait_sec + 2, 60))
                    continue
                    
                # Coba login
                email_input = await page.query_selector("#loginEmail, input[name='email']")
                if email_input:
                    print("🔑 Mencoba login Akun #6 (pakupakuwak@gmail.com)...")
                    await email_input.fill("pakupakuwak@gmail.com")
                    await page.fill("#loginPassword, input[name='password']", "Nathan27@")
                    btn = await page.query_selector("#loginSubmit, form button[type='submit']")
                    if btn:
                        await btn.click()
                    await asyncio.sleep(3)
                    
                    wait_el2 = await page.query_selector(".wait")
                    if wait_el2:
                        wait_sec2 = int((await wait_el2.inner_text()).strip() or "60")
                        print(f"⏳ Masih dalam cooldown: {wait_sec2} detik tersisa...")
                        await ctx.close()
                        await asyncio.sleep(min(wait_sec2 + 2, 60))
                        continue
                        
                await ctx.close()
            except Exception as e:
                print(f"Error pada loop retry Akun #6: {e}")
                await ctx.close()
                await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.run(retry_acc6())
