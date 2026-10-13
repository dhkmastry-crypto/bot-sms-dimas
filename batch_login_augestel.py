# ═══════════════════════════════════════════════════════════════
#  BATCH LOGIN AUGESTEL
#  ─────────────────────────────────────────────────────────────
#  Otomatis login ke seluruh akun Augestel di augestel_accounts.json
#  dan menyimpan sesi ke profil browser masing-masing
#  (browser_profile_augestel_1, browser_profile_augestel_2, dst)
# ═══════════════════════════════════════════════════════════════

import asyncio
import json
import logging
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from playwright.async_api import async_playwright

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("batch_login_augestel")


async def login_single_account(account_idx: int, email: str, password: str) -> dict:
    """Melakukan login pada satu akun dan menyimpan sesi ke browser profile."""
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{account_idx}")
    logger.info(f"👉 [Akun #{account_idx}] Memeriksa sesi untuk: {email}")

    async with async_playwright() as p:
        try:
            context = await p.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                channel="msedge",
                headless=False,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-gpu",
                    "--window-position=-2000,-2000",
                ],
            )
        except Exception as e:
            logger.error(f"❌ [Akun #{account_idx}] Gagal meluncurkan browser: {e}")
            return {"index": account_idx, "email": email, "success": False, "message": str(e)}

        page = context.pages[0] if context.pages else await context.new_page()

        try:
            # Buka halaman test numbers langsung untuk cek sesi
            await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)

            curr_title = await page.title()
            login_input = await page.query_selector("#loginEmail, input[name='email']")

            # Jika sudah login
            if "test numbers" in curr_title.lower() or "client panel" in curr_title.lower():
                if not login_input:
                    logger.info(f"✅ [Akun #{account_idx}] Sesi sudah aktif ({curr_title}). Tidak perlu login ulang.")
                    await context.close()
                    return {"index": account_idx, "email": email, "success": True, "message": "Already logged in"}

            # Jika terkena cooldown
            if "one moment" in curr_title.lower() or "too quick" in curr_title.lower():
                logger.warning(f"⏳ [Akun #{account_idx}] Cooldown aktif di portal Augestel. Menunggu 15 detik...")
                await asyncio.sleep(15)

            # Navigasi ke form login
            if not login_input:
                await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)

            logger.info(f"🔑 [Akun #{account_idx}] Mengisi kredensial login ({email})...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)

            rem = await page.query_selector("input[name='remember']")
            if rem:
                try:
                    await rem.check()
                except Exception:
                    pass

            await asyncio.sleep(1)

            submit_btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if submit_btn:
                await submit_btn.click()
            else:
                await page.keyboard.press("Enter")

            # Tunggu redirect
            success_logged_in = False
            for sec in range(15):
                await asyncio.sleep(1)
                t = await page.title()
                u = page.url
                if "login" not in t.lower() and u != "https://augestel.com/Switchfy":
                    success_logged_in = True
                    break

            if success_logged_in:
                # Navigasi ke test numbers untuk menyimpan state
                await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
                await asyncio.sleep(2)
                logger.info(f"🎉 [Akun #{account_idx}] Login berhasil! Profil tersimpan di {user_data_dir}")
                await context.close()
                return {"index": account_idx, "email": email, "success": True, "message": "Login success"}
            else:
                final_t = await page.title()
                logger.warning(f"⚠️ [Akun #{account_idx}] Login belum terkonfirmasi (Title: {final_t})")
                await context.close()
                return {"index": account_idx, "email": email, "success": False, "message": f"Redirect timeout ({final_t})"}

        except Exception as e:
            logger.error(f"❌ [Akun #{account_idx}] Error saat login: {e}")
            await context.close()
            return {"index": account_idx, "email": email, "success": False, "message": str(e)}


async def main():
    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    if not os.path.exists(acc_file):
        logger.error("❌ File augestel_accounts.json tidak ditemukan!")
        return

    with open(acc_file, "r", encoding="utf-8") as f:
        accounts = json.load(f)

    logger.info("═" * 60)
    logger.info(f"🚀 Memulai Batch Login untuk {len(accounts)} akun Augestel...")
    logger.info("═" * 60)

    results = []
    for idx, acc in enumerate(accounts, 1):
        email = acc.get("email", "").strip()
        pwd = acc.get("password", "").strip()
        if not email or not pwd:
            logger.warning(f"⚠️ Melewati Akun #{idx}: data email/password tidak lengkap.")
            continue

        res = await login_single_account(idx, email, pwd)
        results.append(res)

        # Jeda aman antar akun agar tidak terpicu rate-limit Switchfy
        if idx < len(accounts):
            logger.info("⏳ Cooldown 6 detik sebelum akun berikutnya...")
            await asyncio.sleep(6)

    logger.info("═" * 60)
    logger.info("🏁 RINGKASAN BATCH LOGIN AUGESTEL:")
    success_count = sum(1 for r in results if r.get("success"))
    for r in results:
        status_icon = "✅" if r.get("success") else "❌"
        logger.info(f"  {status_icon} Akun #{r['index']} ({r['email']}): {r['message']}")
    logger.info(f"Total: {success_count}/{len(results)} akun siap digunakan!")
    logger.info("═" * 60)


if __name__ == "__main__":
    asyncio.run(main())
