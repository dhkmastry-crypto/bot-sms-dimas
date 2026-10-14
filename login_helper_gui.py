# ═══════════════════════════════════════════════════════════════
#  AUGESTEL 1-TIME GUI LOGIN HELPER
#  ─────────────────────────────────────────────────────────────
#  Membuka browser Edge di layar VPS untuk akun yang belum login.
#  - Otomatis mengisi email & password
#  - Otomatis mencentang "Remember me"
#  - Menunggu Anda menyelesaikan Quick Check (puzzle 3 detik) & klik Sign In
#  - Otomatis mengambil API Key (sk_live_...) & memasang Webhook
#  - Menyimpan cookie permanen agar akun standby 24/7 di RAM!
# ═══════════════════════════════════════════════════════════════

import asyncio
import os
import sys
import json
import re
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCOUNTS_FILE = os.path.join(BASE_DIR, "augestel_accounts.json")
WEBHOOK_URL = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"

async def login_account(idx: int, acc: dict):
    email = acc.get("email", "")
    pwd = acc.get("password", "")
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")

    print("\n" + "=" * 60)
    print(f"🚀 [Akun #{idx}] Memulai Login untuk: {email}")
    print(f"🔑 Password yang digunakan: {pwd}")
    print("=" * 60)

    # Bersihkan lock file
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        lk_path = os.path.join(user_data_dir, lk)
        if os.path.exists(lk_path):
            try:
                os.remove(lk_path)
            except Exception:
                pass

    async with async_playwright() as p:
        # Buka Edge di layar desktop (visible, bukan offscreen)
        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            viewport={"width": 1280, "height": 800},
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=150,100",
                "--window-size=1280,850",
            ]
        )
        page = context.pages[0] if context.pages else await context.new_page()

        print("🌐 Membuka halaman login Augestel...")
        await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)

        # Cek apakah sudah login
        curr_url = page.url
        curr_title = await page.title()
        login_input = await page.query_selector("#loginEmail, input[name='email']")

        if ("my numbers" in curr_title.lower() or "client" in curr_url) and not login_input:
            print(f"🎉 Akun #{idx} ({email}) SUDAH TERLOGIN sebelumnya!")
        else:
            if not login_input:
                await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(1.5)
                login_input = await page.query_selector("#loginEmail, input[name='email']")

            if login_input:
                print("✍️ Mengisi Email & Password...")
                await page.fill("#loginEmail, input[name='email']", email)
                await page.fill("#loginPassword, input[name='password']", pwd)

                # Centang remember me
                try:
                    cb = await page.query_selector("input[name='remember']")
                    if cb:
                        await cb.check()
                        print("✅ 'Remember me' dicentang.")
                except Exception:
                    pass

            print("\n👉 SILAKAN LIHAT JENDELA EDGE DI LAYAR VPS:")
            print("   1. Selesaikan Quick Check (hubungkan garis warna puzzle)")
            print("   2. Klik tombol 'Sign in'")
            print("⏳ Menunggu Anda login (timeout 5 menit)...")

            # Tunggu user menyelesaikan login
            logged_in = False
            for _ in range(300):
                await asyncio.sleep(1)
                u = page.url
                t = await page.title()
                if "/client/" in u or "/dashboard" in u or "my numbers" in t.lower():
                    logged_in = True
                    print(f"\n🎉 LOGIN BERHASIL TERDETEKSI! URL: {u}")
                    break

            if not logged_in:
                print(f"⚠️ Waktu habis atau login belum selesai untuk Akun #{idx}.")
                await context.close()
                return False

        # Sekarang ambil API Key & Webhook
        print("🔍 Mengambil API Key (sk_live_...) dari portal...")
        api_key = ""
        # 1. Cek dari profil
        await page.goto("https://augestel.com/Switchfy/profile", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2)
        content = await page.content()
        keys = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content)
        if keys:
            api_key = keys[0]
            print(f"🔑 Ditemukan API Key di Profile: {api_key}")

        # 2. Jika belum ada, coba di API Docs atau Webhooks
        if not api_key:
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            content_wh = await page.content()
            keys_wh = re.findall(r"sk_live_[a-zA-Z0-9_\-]+", content_wh)
            if keys_wh:
                api_key = keys_wh[0]
                print(f"🔑 Ditemukan API Key di Webhooks: {api_key}")

        # Simpan ke augestel_accounts.json
        if api_key:
            acc["api_key"] = api_key
            print(f"💾 Menyimpan API Key ke {ACCOUNTS_FILE}...")
            try:
                with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
                    all_accs = json.load(f)
                if idx - 1 < len(all_accs):
                    all_accs[idx - 1]["api_key"] = api_key
                    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
                        json.dump(all_accs, f, indent=2)
                    print("✅ augestel_accounts.json berhasil diperbarui!")
            except Exception as e_save:
                print(f"❌ Gagal update file: {e_save}")

        # Pasang webhook jika ada form webhook
        try:
            print(f"🔗 Memastikan Webhook terpasang: {WEBHOOK_URL}...")
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(1.5)
            url_input = await page.query_selector("input[name='url'], input[name='webhook_url'], #webhookUrl")
            if url_input:
                cur_val = await url_input.input_value()
                if WEBHOOK_URL not in cur_val:
                    await url_input.fill(WEBHOOK_URL)
                    save_btn = await page.query_selector("button[type='submit'], #saveWebhookBtn")
                    if save_btn:
                        await save_btn.click()
                        await asyncio.sleep(2)
                        print("✅ Webhook berhasil disimpan!")
        except Exception as e_wh:
            print(f"⚠️ Note webhook: {e_wh}")

        print(f"✨ Akun #{idx} selesai disiapkan! Sesi cookie tersimpan permanen.")
        await context.close()
        return True

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Helper Login GUI Augestel")
    parser.add_argument("--account", type=int, help="Index akun spesifik (1-16). Default: semua akun 10-16")
    args = parser.parse_args()

    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
        accounts = json.load(f)

    if args.account:
        targets = [args.account]
    else:
        # Default akun 10 s/d 16
        targets = list(range(10, min(len(accounts) + 1, 17)))

    print("═══════════════════════════════════════════════════════════")
    print(f"   AUGESTEL GUI LOGIN HELPER - TARGET AKUN: {targets}")
    print("═══════════════════════════════════════════════════════════")

    for idx in targets:
        if idx < 1 or idx > len(accounts):
            print(f"❌ Index akun #{idx} tidak valid!")
            continue
        acc = accounts[idx - 1]
        success = await login_account(idx, acc)
        if not success:
            print(f"⚠️ Ingin melanjutkan ke akun berikutnya? (Jeda 3 detik)")
            await asyncio.sleep(3)
        await asyncio.sleep(1)

    print("\n🏁 Semua proses selesai! Menutup helper.")

if __name__ == "__main__":
    asyncio.run(main())
