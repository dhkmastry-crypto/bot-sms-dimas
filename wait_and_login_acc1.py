import asyncio
import re
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config

async def wait_and_login():
    cfg = get_account_config(1)
    print("Mempersiapkan browser untuk Akun #1...")
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=cfg["user_data_dir"],
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        while True:
            await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded")
            await asyncio.sleep(1)
            
            # Cek apakah sudah login
            title = await page.title()
            if "/test/" in page.url or "/client/" in page.url:
                print("Akun #1 sudah logged in!")
                break
                
            await page.fill("#loginEmail", cfg["email"])
            await page.fill("#loginPassword", cfg["password"])
            
            # Centang remember me
            await page.evaluate("""() => {
                const el = document.querySelector("input[name='remember']");
                if (el) {
                    el.checked = true;
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }""")
            
            btn = await page.query_selector("#loginSubmit")
            if btn:
                await btn.click()
                
            await asyncio.sleep(2)
            wait_el = await page.query_selector(".wait")
            if wait_el:
                raw_txt = (await wait_el.inner_text()).strip()
                nums = re.findall(r'\d+', raw_txt)
                sec = int(nums[0]) if nums else 60
                print(f"⏳ Cooldown masih aktif: {sec} detik tersisa. Menunggu...")
                # Tidur selama sec + 2 detik
                wait_time = min(sec + 2, 60)
                await asyncio.sleep(wait_time)
            else:
                u = page.url
                t = await page.title()
                print(f"Hasil submit: URL={u} | Title={t}")
                if "/test/" in u or "/client/" in u or "/dashboard" in u:
                    print("🎉 LOGIN BERHASIL UNTUK AKUN #1!")
                    await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle")
                    await asyncio.sleep(2)
                    break
                else:
                    await asyncio.sleep(5)
                    
        cookies = await ctx.cookies(["https://augestel.com"])
        has_rem = any("remember_client" in c["name"] for c in cookies)
        print(f"Status sesi Akun #1: cookies={len(cookies)}, remember_client={has_rem}")
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(wait_and_login())
