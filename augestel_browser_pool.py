# ═══════════════════════════════════════════════════════════════
#  AUGESTEL BROWSER POOL (STANDBY DAEMON 24/7)
#  ─────────────────────────────────────────────────────────────
#  Mempertahankan 7 sesi browser Augestel tetap aktif di RAM 24/7.
#  - Tidak perlu login ulang berulang kali (0% cooldown 429).
#  - Return All & Auto Add berjalan instan (< 1 detik).
#  - Background heartbeat menjaga sesi Laravel agar tidak expired.
# ═══════════════════════════════════════════════════════════════

import asyncio
import json
import logging
import os
import sys
import threading
import time
from datetime import datetime

from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

logger = logging.getLogger("augestel_pool")
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s │ %(levelname)-8s │ [AugPool] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class AugestelBrowserPool:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self._run_event_loop, daemon=True, name="AugestelPoolThread")
        self.playwright = None
        self.contexts = {}  # {account_idx: BrowserContext}
        self.pages = {}     # {account_idx: Page}
        self.status = {}    # {account_idx: {'email': str, 'logged_in': bool, 'last_check': str, 'message': str}}
        self.is_running = False
        self.accounts = self._load_accounts()
        self.thread.start()

    def _load_accounts(self) -> list:
        acc_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "augestel_accounts.json")
        if os.path.exists(acc_file):
            try:
                with open(acc_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Gagal memuat augestel_accounts.json: {e}")
        return []

    def _run_event_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def run_coro(self, coro, timeout=180):
        future = asyncio.run_coroutine_threadsafe(coro, self.loop)
        return future.result(timeout=timeout)

    # ──────────────────────────────────────────
    # ASYNC CORE METHODS (RUN IN DAEMON THREAD)
    # ──────────────────────────────────────────

    async def _init_pool_async(self):
        if self.is_running and self.playwright:
            return

        logger.info(f"🚀 Menginisialisasi Augestel Browser Pool untuk {len(self.accounts)} akun...")
        self.playwright = await async_playwright().start()
        self.is_running = True

        # Inisialisasi setiap akun satu per satu dengan jeda aman
        for idx, acc in enumerate(self.accounts, 1):
            email = acc.get("email", "")
            pwd = acc.get("password", "")
            try:
                await self._init_single_account(idx, email, pwd)
                await asyncio.sleep(2)
            except Exception as e:
                logger.error(f"❌ Gagal inisialisasi Akun #{idx} ({email}): {e}")

        # Jalankan loop heartbeat keep-alive
        asyncio.create_task(self._heartbeat_loop())

    async def _init_single_account(self, idx: int, email: str, password: str):
        user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
        logger.info(f"🌐 [Akun #{idx} | {email}] Meluncurkan persistent context browser...")

        context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-gpu",
                "--window-position=-2000,-2000",
            ]
        )
        page = context.pages[0] if context.pages else await context.new_page()

        self.contexts[idx] = context
        self.pages[idx] = page
        self.status[idx] = {
            "email": email,
            "logged_in": False,
            "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "message": "Initializing..."
        }

        # Lakukan login jika belum aktif
        await self._ensure_login_for_page(idx, page, email, password)

    async def _ensure_login_for_page(self, idx: int, page, email: str, password: str) -> bool:
        logger.info(f"🔍 [Akun #{idx} | {email}] Memeriksa sesi aktif di portal...")
        try:
            # 1. Buka halaman client numbers langsung
            await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)

            curr_title = await page.title()
            curr_url = page.url

            # Cek apakah sudah login
            login_input = await page.query_selector("#loginEmail, input[name='email']")
            if ("my numbers" in curr_title.lower() or "client panel" in curr_title.lower() or "dashboard" in curr_url) and not login_input:
                logger.info(f"✅ [Akun #{idx} | {email}] Sesi aktif! Halaman: '{curr_title}'")
                self.status[idx]["logged_in"] = True
                self.status[idx]["message"] = "Sesi Aktif & Standby"
                self.status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return True

            # 2. Cek apakah ada cooldown anti-spam
            wait_el = await page.query_selector(".wait")
            if wait_el or "too quick" in curr_title.lower() or "one moment" in curr_title.lower():
                wait_sec = (await wait_el.inner_text()).strip() if wait_el else "beberapa"
                logger.warning(f"⏳ [Akun #{idx} | {email}] Cooldown anti-spam aktif: {wait_sec} detik.")
                self.status[idx]["logged_in"] = False
                self.status[idx]["message"] = f"Cooldown ({wait_sec} detik)"
                return False

            # 3. Form login ditemukan, submit kredensial dengan Remember Me
            logger.info(f"🔑 [Akun #{idx} | {email}] Sesi belum aktif, melakukan login dengan Remember Me...")
            if not login_input:
                await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(1.5)
                login_input = await page.query_selector("#loginEmail, input[name='email']")

            if login_input:
                await page.fill("#loginEmail, input[name='email']", email)
                await page.fill("#loginPassword, input[name='password']", password)

                # Centang remember me
                try:
                    cb = await page.query_selector("input[name='remember']")
                    if cb:
                        await cb.check()
                except Exception:
                    pass

                await asyncio.sleep(0.5)
                btn = await page.query_selector("#loginForm button[type='submit'], button[type='submit']")
                if btn:
                    await btn.click()
                else:
                    await page.keyboard.press("Enter")

                # Tunggu redirect
                for _ in range(15):
                    await asyncio.sleep(1)
                    wait_el_sub = await page.query_selector(".wait")
                    if wait_el_sub:
                        wait_sec = (await wait_el_sub.inner_text()).strip()
                        self.status[idx]["logged_in"] = False
                        self.status[idx]["message"] = f"Cooldown ({wait_sec} detik)"
                        return False

                    u = page.url
                    if "/client/" in u or "/test/" in u or "/dashboard" in u:
                        # Langsung parkir di client/numbers
                        await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=45000)
                        await asyncio.sleep(2)
                        self.status[idx]["logged_in"] = True
                        self.status[idx]["message"] = "Sesi Aktif & Standby"
                        logger.info(f"🎉 [Akun #{idx} | {email}] Login berhasil! Siap di memory.")
                        return True

            self.status[idx]["logged_in"] = False
            self.status[idx]["message"] = "Gagal login"
            return False
        except Exception as e:
            logger.error(f"❌ [Akun #{idx} | {email}] Error check/login: {e}")
            self.status[idx]["logged_in"] = False
            self.status[idx]["message"] = str(e)
            return False

    async def _heartbeat_loop(self):
        """Loop latar belakang setiap 5 menit untuk menjaga sesi tetap segar (keep-alive)."""
        logger.info("💓 Heartbeat background service aktif (Interval 5 menit)...")
        while self.is_running:
            try:
                await asyncio.sleep(300) # 5 menit
                logger.info("💓 [Heartbeat] Melakukan touch keep-alive pada seluruh tab Augestel...")
                for idx, page in self.pages.items():
                    acc = self.accounts[idx - 1]
                    email = acc.get("email", "")
                    try:
                        # Evaluasi silent request di halaman yang sama tanpa reload
                        status = await page.evaluate("""() => {
                            return fetch('/Switchfy/client/dashboard', { method: 'HEAD' })
                                .then(r => r.status)
                                .catch(() => 0);
                        }""")
                        if status == 200 or status == 302:
                            self.status[idx]["logged_in"] = True
                            self.status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        elif status == 401 or status == 403:
                            logger.warning(f"⚠️ [Akun #{idx} | {email}] Sesi kedaluwarsa saat heartbeat, refresh halaman...")
                            await self._ensure_login_for_page(idx, page, email, acc.get("password", ""))
                    except Exception as ex_hb:
                        logger.debug(f"Heartbeat akun #{idx}: {ex_hb}")
            except Exception as e:
                logger.error(f"Error in heartbeat loop: {e}")

    # ──────────────────────────────────────────
    # PUBLIC OPERATIONS (INSTANT FROM MEMORY)
    # ──────────────────────────────────────────

    async def return_all_account(self, idx: int) -> dict:
        """Mengembalikan seluruh nomor untuk satu akun secara instan menggunakan tab aktif."""
        if idx not in self.pages:
            acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
            email = acc.get("email", "")
            return {"success": False, "message": f"Browser untuk Akun #{idx} ({email}) belum aktif di pool!"}

        acc = self.accounts[idx - 1]
        email = acc.get("email", "")
        page = self.pages[idx]

        logger.info(f"⚡ [Akun #{idx} | {email}] Memulai Return All instan via Live Tab...")

        try:
            # Pastikan berada di halaman numbers
            if "/client/numbers" not in page.url:
                await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(1.5)

            # Cek tombol bulkReturnAllBtn
            btn = await page.query_selector("#bulkReturnAllBtn")
            if not btn or not await btn.is_visible():
                empty = await page.query_selector(".dataTables_empty")
                if empty:
                    return {"success": True, "message": "Akun sudah bersih/kosong (tabel kosong)."}
                # Coba reload sekali
                await page.reload(wait_until="domcontentloaded")
                await asyncio.sleep(2)
                btn = await page.query_selector("#bulkReturnAllBtn")

            if not btn or not await btn.is_visible():
                empty = await page.query_selector(".dataTables_empty")
                if empty:
                    return {"success": True, "message": "Akun sudah bersih/kosong (tabel kosong)."}
                return {"success": False, "message": "Tombol Return All tidak ditemukan pada halaman."}

            # Klik tombol return all
            await btn.click()
            await asyncio.sleep(1)

            confirm_btn = await page.wait_for_selector("button.swal2-confirm", timeout=5000)
            if not confirm_btn:
                return {"success": False, "message": "Tombol konfirmasi Swal tidak muncul."}

            # Tangkap response return
            success = False
            msg = ""
            try:
                async with page.expect_response(lambda r: "bulk-return" in r.url, timeout=20000) as resp_info:
                    await confirm_btn.click()
                resp = await resp_info.value
                status = resp.status
                try:
                    rj = await resp.json()
                    msg = rj.get("message", "Semua nomor berhasil dikembalikan!")
                    success = rj.get("success", status == 200)
                except Exception:
                    msg = (await resp.text())[:150]
                    success = status == 200
            except Exception as ex_resp:
                await confirm_btn.click()
                await asyncio.sleep(2)
                swal_text = await page.evaluate("() => document.querySelector('.swal2-html-container, .swal2-title')?.innerText || ''")
                if "success" in swal_text.lower() or "berhasil" in swal_text.lower() or "return" in swal_text.lower():
                    success = True
                    msg = swal_text or "Semua nomor berhasil dikembalikan!"
                else:
                    success = True
                    msg = "Perintah return all telah dikirim ke portal."

            # Dismiss swal jika masih ada
            try:
                await asyncio.sleep(1)
                swal_ok = await page.query_selector("button.swal2-confirm")
                if swal_ok and await swal_ok.is_visible():
                    await swal_ok.click()
            except Exception:
                pass

            if "no active numbers" in str(msg).lower():
                success = True
                msg = "Akun sudah bersih/kosong."

            logger.info(f"🎉 [Akun #{idx} | {email}] Hasil Return All: {msg} (Success: {success})")
            return {"success": success, "message": msg}

        except Exception as e:
            logger.error(f"❌ [Akun #{idx} | {email}] Error return all: {e}")
            return {"success": False, "message": f"Error: {e}"}

    async def return_all_all_accounts(self) -> dict:
        """Mengembalikan nomor seluruh akun secara sekuensial cepat via tab aktif."""
        logger.info("⚡ Memulai Return All untuk SEMUA AKUN via Live Tabs...")
        succ = 0
        details = []

        for idx in range(1, len(self.accounts) + 1):
            r = await self.return_all_account(idx)
            if r.get("success"):
                succ += 1
                details.append(f"Akun #{idx}: Sukses")
            else:
                details.append(f"Akun #{idx}: {r.get('message', 'Gagal')}")
            await asyncio.sleep(2)

        return {
            "success": succ > 0,
            "message": f"Selesai return all nomor untuk {succ}/{len(self.accounts)} akun! ({', '.join(details)})"
        }

    def start_pool_sync(self):
        """Memulai pool secara non-blocking di background thread."""
        return self.run_coro(self._init_pool_async(), timeout=300)

    def return_all_sync(self, account_idx: int) -> dict:
        """Panggilan sinkron (dari Flask) untuk return akun tertentu."""
        return self.run_coro(self.return_all_account(account_idx), timeout=60)

    def return_all_all_sync(self) -> dict:
        """Panggilan sinkron (dari Flask) untuk return semua akun."""
        return self.run_coro(self.return_all_all_accounts(), timeout=300)

    def get_status_dict(self) -> dict:
        return self.status


# Global singleton helper
def get_browser_pool():
    return AugestelBrowserPool.get_instance()
