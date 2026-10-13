# ═══════════════════════════════════════════════════════════════
#  AUTO-SETUP WEBHOOKS AUGESTEL (1 - 7) DENGAN AUTO-LOGIN
# ═══════════════════════════════════════════════════════════════
import asyncio
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_accounts():
    acc_path = os.path.join(BASE_DIR, "augestel_accounts.json")
    if os.path.exists(acc_path):
        with open(acc_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

async def setup_account_webhook(acc_idx: int, account_data: dict):
    profile_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{acc_idx}")
    email = account_data.get("email", "")
    password = account_data.get("password", "")

    print(f"\n🚀 [Akun #{acc_idx} - {email}] Menyiapkan webhook di {profile_dir}...")
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            channel="msedge",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=-2000,-2000"
            ]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        try:
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)
            
            # Jika diarahkan ke form login, lakukan auto-login
            if "/login" in page.url.lower() or await page.query_selector("#loginEmail, input[name='email']"):
                print(f"🔑 [Akun #{acc_idx}] Membutuhkan login. Mengisi kredensial...")
                await page.fill("#loginEmail, input[name='email']", email)
                await page.fill("#loginPassword, input[name='password']", password)
                
                try:
                    await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); } }")
                except Exception:
                    pass
                    
                await asyncio.sleep(1)
                submit_btn = await page.query_selector("#loginSubmit, button[type='submit']")
                if submit_btn:
                    await submit_btn.click()
                else:
                    await page.keyboard.press("Enter")
                    
                # Tunggu login berhasil
                logged_in = False
                for _ in range(15):
                    await asyncio.sleep(1)
                    if "/client/" in page.url or "/dashboard" in page.url or "/test/" in page.url or "/api/" in page.url:
                        logged_in = True
                        break
                        
                if logged_in:
                    print(f"🎉 [Akun #{acc_idx}] Login berhasil! Mengakses webhooks...")
                    await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
                    await asyncio.sleep(2)
                else:
                    print(f"⚠️ [Akun #{acc_idx}] Gagal login. Melanjutkan...")
                    await ctx.close()
                    return False

            # Tunggu elemen #webhookUrl
            url_input = await page.wait_for_selector("#webhookUrl", timeout=15000)
            await url_input.fill(WEBHOOK_URL)

            # Pastikan is_active tercentang
            active_cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
            if active_cb and not await active_cb.is_checked():
                await active_cb.check()

            # Pastikan message.received tercentang
            msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
            if msg_cb and not await msg_cb.is_checked():
                await msg_cb.check()

            # Klik tombol simpan
            save_btn = await page.query_selector('button[type="submit"]:has-text("Save endpoint"), form[action*="webhook"] button[type="submit"]')
            if save_btn:
                await save_btn.click()
                await asyncio.sleep(2.5)

            saved_val = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
            is_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? cb.checked : false; }')

            success = (saved_val == WEBHOOK_URL and is_active)
            if success:
                print(f"✅ [Akun #{acc_idx} - {email}] Webhook BERHASIL aktif! (URL: {saved_val})")
            else:
                print(f"⚠️ [Akun #{acc_idx}] Hasil: saved={saved_val}, is_active={is_active}")

            await ctx.close()
            return success
        except Exception as e:
            print(f"❌ [Akun #{acc_idx}] Terjadi kesalahan: {e}")
            await ctx.close()
            return False

async def main():
    accounts = load_accounts()
    print(f"============================================================")
    print(f"  AUGESTEL WEBHOOK AUTO-CONFIGURATION (1 - {len(accounts)})")
    print(f"  Target URL: {WEBHOOK_URL}")
    print(f"============================================================")

    results = {}
    for idx, acc in enumerate(accounts, 1):
        success = await setup_account_webhook(idx, acc)
        results[idx] = success
        await asyncio.sleep(1)

    print("\n============================================================")
    print("  RINGKASAN HASIL KONFIGURASI WEBHOOK")
    print("============================================================")
    for idx, ok in results.items():
        email = accounts[idx-1].get("email", "") if idx <= len(accounts) else ""
        status = "✅ AKTIF" if ok else "❌ GAGAL"
        print(f"  Akun #{idx} ({email}): {status}")

if __name__ == '__main__':
    asyncio.run(main())
