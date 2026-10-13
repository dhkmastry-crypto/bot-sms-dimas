# ═══════════════════════════════════════════════════════════════
#  AUTO-SETUP WEBHOOKS AUGESTEL (1 - 7)
# ═══════════════════════════════════════════════════════════════
import asyncio
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

async def setup_account_webhook(acc_idx: int):
    profile_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{acc_idx}")
    if not os.path.exists(profile_dir):
        print(f"⚠️ [Akun #{acc_idx}] Direktori profil tidak ditemukan.")
        return False

    print(f"\n🚀 [Akun #{acc_idx}] Menyiapkan webhook di {profile_dir}...")
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        try:
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle", timeout=30000)
            
            # Check if redirected to login
            if "/login" in page.url.lower():
                print(f"⚠️ [Akun #{acc_idx}] Belum login atau session kedaluwarsa.")
                await ctx.close()
                return False

            # Isi webhook URL
            url_input = await page.wait_for_selector("#webhookUrl", timeout=10000)
            await url_input.fill(WEBHOOK_URL)

            # Pastikan is_active tercentang
            active_cb = await page.query_selector('input[type="checkbox"][name="is_active"]')
            if active_cb and not await active_cb.is_checked():
                await active_cb.check()

            # Pastikan message.received tercentang
            msg_cb = await page.query_selector('input[type="checkbox"][name="events[]"][value="message.received"]')
            if msg_cb and not await msg_cb.is_checked():
                await msg_cb.check()

            # Klik simpan
            submit_btn = await page.query_selector('button[type="submit"]:has-text("Save endpoint"), form[action*="webhook"] button[type="submit"]')
            if submit_btn:
                await submit_btn.click()
                await page.wait_for_timeout(2500)

            saved_val = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
            is_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? cb.checked : false; }')

            success = (saved_val == WEBHOOK_URL and is_active)
            if success:
                print(f"✅ [Akun #{acc_idx}] Webhook BERHASIL dipasang! (Status: Aktif, URL: {saved_val})")
            else:
                print(f"⚠️ [Akun #{acc_idx}] Status tersimpan: {saved_val}, active: {is_active}")

            await ctx.close()
            return success
        except Exception as e:
            print(f"❌ [Akun #{acc_idx}] Terjadi kesalahan: {e}")
            await ctx.close()
            return False

async def main():
    print(f"============================================================")
    print(f"  AUGESTEL WEBHOOK AUTO-CONFIGURATION (AKUN #1 - #7)")
    print(f"  Target URL: {WEBHOOK_URL}")
    print(f"============================================================")

    results = {}
    for idx in range(1, 8):
        success = await setup_account_webhook(idx)
        results[idx] = success
        await asyncio.sleep(1)

    print("\n============================================================")
    print("  RINGKASAN HASIL KONFIGURASI WEBHOOK")
    print("============================================================")
    for idx, ok in results.items():
        status = "✅ BERHASIL" if ok else "❌ GAGAL"
        print(f"  Akun #{idx}: {status}")

if __name__ == '__main__':
    asyncio.run(main())
