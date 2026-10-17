import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TARGET_WEBHOOK = "https://dimsong.online/api/augestel/webhook"

async def check_and_fix(idx: int, email: str, password: str):
    print(f"\n==================================================")
    print(f"Checking Account #{idx}: {email}")
    print(f"==================================================")
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
    
    # Bersihkan locks jika ada
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        p = os.path.join(user_data_dir, lk)
        if os.path.exists(p):
            try:
                os.remove(p)
            except Exception:
                pass

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(3)
        
        # Cek jika login
        if "login" in page.url.lower() or "login" in (await page.title()).lower():
            print(f"  Akun #{idx} perlu login...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("input[name='password']", password)
            await page.click("button[type='submit'], .au-btn")
            await page.wait_for_load_state("networkidle", timeout=30000)
            await asyncio.sleep(3)
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(3)
            
        # Ambil user name di navbar
        user_name = await page.evaluate('''() => {
            const el = document.querySelector('.welcome-user, .user-name, header, nav');
            return document.body.innerText.match(/Welcome back,\\s*([^\\n]+)/i)?.[1] || "Unknown";
        }''')
        print(f"  Logged in as: {user_name}")
        
        # Cek input webhookUrl saat ini
        url_input = await page.query_selector("#webhookUrl, input[name='url']")
        if not url_input:
            print(f"  ❌ Form webhook tidak ditemukan di Akun #{idx}!")
            await ctx.close()
            return
            
        curr_val = await url_input.input_value()
        is_active = await page.evaluate('''() => {
            const cb = document.querySelector('input[type="checkbox"][name="is_active"]');
            return cb ? cb.checked : false;
        }''')
        
        print(f"  NILAI DI PORTAL SEKARANG: url='{curr_val}', is_active={is_active}")
        
        if curr_val == TARGET_WEBHOOK and is_active:
            print(f"  ✅ Akun #{idx} SUDAH TEPAT: {curr_val} (Active: {is_active})")
        else:
            print(f"  ⚠️ Akun #{idx} PERLU DIPERBAIKI! Memasang {TARGET_WEBHOOK}...")
            await url_input.fill(TARGET_WEBHOOK)
            
            # Centang checkbox
            await page.evaluate("""() => {
                const cb = document.querySelector('input[type="checkbox"][name="is_active"]');
                if (cb && !cb.checked) {
                    cb.checked = true;
                    cb.dispatchEvent(new Event('input', { bubbles: true }));
                    cb.dispatchEvent(new Event('change', { bubbles: true }));
                }
                const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
                if (msg && !msg.checked) {
                    msg.checked = true;
                    msg.dispatchEvent(new Event('input', { bubbles: true }));
                    msg.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }""")
            await asyncio.sleep(1)
            
            # Klik Save endpoint
            save_btn = await page.query_selector('form[action*="webhook"] button[type="submit"], button:has-text("Save endpoint"), button:has-text("Update endpoint")')
            if save_btn:
                btn_name = (await save_btn.inner_text()).strip()
                print(f"  Mengklik '{btn_name}'...")
                await save_btn.click()
                await asyncio.sleep(4)
                await page.wait_for_load_state("networkidle", timeout=15000)
            
            # Verifikasi ulang
            new_val = await page.evaluate('''() => {
                const el = document.querySelector("#webhookUrl, input[name='url']");
                return el ? el.value : "";
            }''')
            new_active = await page.evaluate('''() => {
                const cb = document.querySelector("input[name='is_active'][type='checkbox']");
                return cb ? cb.checked : false;
            }''')
            print(f"  HASIL SETELAH SAVE: url='{new_val}', is_active={new_active}")
            
            # Screenshot bukti
            ss_file = f"webhook_verified_acc_{idx}.png"
            await page.screenshot(path=ss_file)
            print(f"  Screenshot disimpan: {ss_file}")
            
        await ctx.close()

async def main():
    import json
    accs = json.load(open('augestel_accounts.json', encoding='utf-8'))
    # Cek akun 31 dan 32 dulu
    for i in [31, 32]:
        a = accs[i - 1]
        try:
            await check_and_fix(i, a["email"], a["password"])
        except Exception as e:
            print(f"Error checking #{i}: {e}")

if __name__ == '__main__':
    asyncio.run(main())
