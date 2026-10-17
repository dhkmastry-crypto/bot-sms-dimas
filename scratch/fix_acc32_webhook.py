import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TARGET_WEBHOOK = "https://dimsong.online/api/augestel/webhook"
EMAIL = "aug_42f2622a@monemail.fr.nf"
PASS = "5kz#gld2W3PD"

async def fix_webhook_32():
    print(f"Mengakses browser profile 32 untuk {EMAIL}...")
    user_data_dir = os.path.abspath("browser_profile_augestel_32")
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)
        
        # Cek apakah perlu login
        if "login" in page.url.lower() or "login" in (await page.title()).lower():
            print("Perlu login, melakukan proses login...")
            email_input = await page.wait_for_selector("#loginEmail, input[name='email']", timeout=10000)
            await email_input.fill(EMAIL)
            pass_input = await page.wait_for_selector("input[name='password']", timeout=10000)
            await pass_input.fill(PASS)
            
            # Submit login
            submit_btn = await page.query_selector("button[type='submit'], .au-btn")
            if submit_btn:
                await submit_btn.click()
                await page.wait_for_load_state("networkidle", timeout=30000)
                await asyncio.sleep(3)
                
            print("Login selesai, menuju /webhooks...")
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)
            
        print("Halaman saat ini:", page.url)
        print("Judul:", await page.title())
        
        # Isi URL webhook
        url_input = await page.wait_for_selector("#webhookUrl, input[name='url']", timeout=15000)
        cur_val = await url_input.input_value()
        print("Nilai input saat ini:", cur_val)
        
        await url_input.fill(TARGET_WEBHOOK)
        print("Telah mengisi:", TARGET_WEBHOOK)
        
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
        
        # Cari tombol save endpoint
        # Mari periksa semua tombol di form
        btn = await page.query_selector('form[action*="webhook"] button[type="submit"], button:has-text("Save endpoint"), button:has-text("Update endpoint")')
        if btn:
            btn_txt = await btn.inner_text()
            print(f"Mengklik tombol '{btn_txt}'...")
            await btn.click()
            await page.wait_for_load_state("networkidle", timeout=20000)
            await asyncio.sleep(3)
        else:
            print("Tombol submit tidak ditemukan!")
            
        # Periksa nilai setelah disimpan
        final_val = await page.evaluate('() => document.querySelector("#webhookUrl, input[name=\'url\']") ? document.querySelector("#webhookUrl, input[name=\'url\']").value : ""')
        final_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? (cb.checked || cb.hasAttribute("checked")) : false; }')
        print(f"HASIL AKHIR AKUN 32: url='{final_val}', is_active={final_active}")
        
        await page.screenshot(path="webhook_acc32_final.png")
        print("Screenshot disimpan di webhook_acc32_final.png")
        
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(fix_webhook_32())
