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
import re
import sys
import threading
import time
from datetime import datetime

from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
        self.webhook_guardian_status = {}  # {account_idx: {'email': str, 'is_delivering': bool, 'is_active': bool, 'is_paused': bool, 'auto_recovered_count': int, ...}}
        self.webhook_url = "https://bonnet-grinning-naming.ngrok-free.dev/api/augestel/webhook"
        self.webhook_guardian_enabled = True
        self.auto_add_running = False
        self.auto_add_stop_flag = False
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
        # Jalankan loop Webhook Guardian (Auto-Heal 24/7)
        asyncio.create_task(self._webhook_guardian_loop())

    async def _init_single_account(self, idx: int, email: str, password: str):
        user_data_dir = os.path.abspath(f"browser_profile_augestel_{idx}")
        # Bersihkan lock file usang jika ada
        for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
            lk_path = os.path.join(user_data_dir, lk)
            if os.path.exists(lk_path):
                try:
                    os.remove(lk_path)
                except Exception:
                    pass

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
        """
        Browser & Cookie Guardian (Heartbeat & Keep-Alive Daemon):
        Loop latar belakang setiap 3 menit untuk menjaga browser & sesi cookie tetap hidup 24/7.
        - Memastikan proses browser tidak crash (auto-relaunch jika mati).
        - Memastikan sesi cookie Laravel / Remember Me tetap valid (auto-relogin jika expired).
        - Menjaga tab tetap standby di RAM agar return all & webhook berjalan instan.
        """
        logger.info("🛡️ [Browser/Cookie Guardian] Service aktif! Memantau liveness 7 browser & cookie (Interval 3 menit)...")
        while self.is_running:
            try:
                await asyncio.sleep(180)  # 3 menit
                logger.info("💓 [Browser/Cookie Guardian] Memeriksa kesehatan browser & touch session keep-alive...")
                for idx in range(1, len(self.accounts) + 1):
                    acc = self.accounts[idx - 1]
                    email = acc.get("email", "")
                    pwd = acc.get("password", "")

                    try:
                        page = self.pages.get(idx)
                        ctx = self.contexts.get(idx)

                        # 1. Proteksi Crash / Browser Mati: Cek apakah page atau konteks tertutup
                        is_dead = (page is None) or (ctx is None)
                        if not is_dead:
                            try:
                                is_dead = page.is_closed()
                            except Exception:
                                is_dead = True

                        if is_dead:
                            logger.warning(f"⚠️ [Browser Guardian] Browser Akun #{idx} ({email}) terdeteksi crash/tertutup! Meluncurkan ulang sekarang...")
                            await self._init_single_account(idx, email, pwd)
                            page = self.pages.get(idx)
                            if not page:
                                continue

                        # 2. Proteksi Sesi & Cookie: Cek apakah sesi login masih aktif
                        curr_url = page.url
                        login_input = await page.query_selector("#loginEmail, input[name='email']")

                        if ("/client/" in curr_url or "/api/" in curr_url or "numbers" in curr_url) and not login_input:
                            self.status[idx]["logged_in"] = True
                            self.status[idx]["message"] = "Standby di RAM (24/7)"
                            self.status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        else:
                            # Cek form cooldown atau re-login
                            wait_el = await page.query_selector(".wait")
                            if wait_el:
                                wait_sec = (await wait_el.inner_text()).strip()
                                self.status[idx]["logged_in"] = False
                                self.status[idx]["message"] = f"Cooldown ({wait_sec}s)"
                            else:
                                logger.warning(f"⚠️ [Cookie Guardian] Sesi login / cookie Akun #{idx} ({email}) kedaluwarsa! Login ulang otomatis dengan Remember Me...")
                                relogin_ok = await self._ensure_login_for_page(idx, page, email, pwd)
                                if relogin_ok:
                                    logger.info(f"🎉 [Cookie Guardian] Akun #{idx} ({email}) Sesi & cookie BERHASIL dipulihkan!")
                                    log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ 🛡️ [Cookie Guardian] Sesi Akun #{idx} ({email}) kedaluwarsa dan telah otomatis di-login ulang (Remember Me)!\n"
                                    try:
                                        with open(os.path.join(BASE_DIR, "bot.log"), "a", encoding="utf-8") as f_log:
                                            f_log.write(log_line)
                                    except Exception:
                                        pass

                        # 3. Jika akun sudah login tapi belum punya API Key atau webhook, lengkapi otomatis
                        if self.status[idx].get("logged_in") and not acc.get("api_key"):
                            try:
                                await self.ensure_account_setup(idx)
                            except Exception as e_setup:
                                logger.error(f"Error auto-setup on heartbeat #{idx}: {e_setup}")
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

    async def check_account_status(self, idx: int) -> dict:
        """Memeriksa status sesi live tab untuk 1 akun tertentu secara real-time."""
        if idx not in self.pages:
            return {"logged_in": False, "message": "Browser belum aktif di pool"}

        page = self.pages[idx]
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        email = acc.get("email", "")

        try:
            curr_title = await page.title()
            curr_url = page.url
            login_input = await page.query_selector("#loginEmail, input[name='email']")

            # 1. Cek form cooldown
            wait_el = await page.query_selector(".wait")
            if wait_el:
                wait_sec = (await wait_el.inner_text()).strip()
                self.status[idx]["logged_in"] = False
                self.status[idx]["message"] = f"Cooldown ({wait_sec} detik)"
                return self.status[idx]

            # 2. Cek apakah sesi aktif di panel client
            if ("/client/" in curr_url or "my numbers" in curr_title.lower() or "client panel" in curr_title.lower()) and not login_input:
                self.status[idx]["logged_in"] = True
                self.status[idx]["message"] = "Standby di RAM (24/7)"
                self.status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return self.status[idx]

            # 3. Coba verifikasi dengan evaluate silent request yang mendeteksi redirect login
            res_eval = await page.evaluate("""async () => {
                try {
                    const r = await fetch('/Switchfy/client/numbers', { method: 'GET', redirect: 'follow' });
                    return { ok: r.ok, url: r.url };
                } catch(e) {
                    return { ok: false, error: e.toString() };
                }
            }""")
            if res_eval.get("ok") and "/client/" in res_eval.get("url", "") and "login" not in res_eval.get("url", ""):
                self.status[idx]["logged_in"] = True
                self.status[idx]["message"] = "Standby di RAM (24/7)"
                self.status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                self.status[idx]["logged_in"] = False
                self.status[idx]["message"] = "Perlu Login Portal"

            return self.status[idx]
        except Exception as e:
            return {"logged_in": False, "message": str(e)}

    async def relogin_account(self, idx: int) -> dict:
        """Memaksa re-login pada tab yang sedang terbuka di pool."""
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        if idx not in self.pages:
            await self._init_single_account(idx, acc.get("email", ""), acc.get("password", ""))

        if idx in self.pages:
            page = self.pages[idx]
            ok = await self._ensure_login_for_page(idx, page, acc.get("email", ""), acc.get("password", ""))
            return {"success": ok, "message": self.status[idx]["message"]}
        return {"success": False, "message": "Gagal membuka tab browser"}

    def check_account_sync(self, idx: int) -> dict:
        """Pengecekan live tab sinkron dari Flask."""
        return self.run_coro(self.check_account_status(idx), timeout=15)

    def relogin_account_sync(self, idx: int) -> dict:
        """Pemicu login ulang sinkron dari Flask."""
        return self.run_coro(self.relogin_account(idx), timeout=60)

    async def _sync_accounts_async(self):
        """Menyinkronkan daftar akun aktif dengan augestel_accounts.json secara dinamis di background."""
        new_accounts = self._load_accounts()
        self.accounts = new_accounts
        total_accs = len(new_accounts)
        logger.info(f"🔄 Sinkronisasi pool dinamis: terdeteksi {total_accs} akun Augestel di disk.")

        if not self.is_running or not self.playwright:
            return

        # 1. Tambahkan / inisialisasi akun baru (misal akun 8, 9, 10) yang belum ada di pool
        for idx, acc in enumerate(new_accounts, 1):
            email = acc.get("email", "")
            pwd = acc.get("password", "")
            if idx not in self.contexts or idx not in self.pages or self.pages[idx].is_closed():
                logger.info(f"✨ [Pool Auto-Add] Menginisialisasi browser baru untuk Akun #{idx} ({email})...")
                try:
                    await self._init_single_account(idx, email, pwd)
                    await asyncio.sleep(2)
                    if self.status.get(idx, {}).get("logged_in"):
                        await self.ensure_account_setup(idx)
                except Exception as e:
                    logger.error(f"❌ Gagal auto-init browser Akun #{idx}: {e}")
            else:
                if idx in self.status:
                    self.status[idx]["email"] = email
                # Jika akun sudah login tapi belum punya API Key atau belum pasang webhook
                if self.status.get(idx, {}).get("logged_in") and not acc.get("api_key"):
                    try:
                        await self.ensure_account_setup(idx)
                    except Exception as e:
                        logger.error(f"❌ Gagal auto-setup Akun #{idx}: {e}")

        # 2. Tutup dan bersihkan akun yang sudah dihapus dari file
        existing_indices = list(self.contexts.keys())
        for old_idx in existing_indices:
            if old_idx > total_accs:
                logger.info(f"🗑️ [Pool Cleanup] Menutup browser profil Akun #{old_idx} karena telah dihapus...")
                try:
                    ctx = self.contexts.pop(old_idx, None)
                    if ctx:
                        await ctx.close()
                except Exception:
                    pass
                self.pages.pop(old_idx, None)
                self.status.pop(old_idx, None)

    def sync_accounts_sync(self):
        """Panggilan sinkron dari thread Flask untuk sinkronisasi akun baru/update."""
        return self.run_coro(self._sync_accounts_async(), timeout=180)

    def _update_account_key_on_disk(self, idx: int, api_key: str):
        """Menyimpan API Key baru ke memory pool dan file augestel_accounts.json secara permanen."""
        if 0 < idx <= len(self.accounts):
            self.accounts[idx - 1]["api_key"] = api_key
        
        acc_file = os.path.join(BASE_DIR, "augestel_accounts.json")
        try:
            if os.path.exists(acc_file):
                with open(acc_file, "r", encoding="utf-8") as f:
                    disk_accs = json.load(f)
                if 0 <= idx - 1 < len(disk_accs):
                    disk_accs[idx - 1]["api_key"] = api_key
                    with open(acc_file, "w", encoding="utf-8") as f:
                        json.dump(disk_accs, f, indent=2)
                    logger.info(f"💾 [Akun #{idx}] API Key berhasil disimpan ke augestel_accounts.json!")
            
            # Jika akun #1, perbarui juga config.py jika belum terpasang
            if idx == 1:
                try:
                    from admin_server import save_config
                    save_config({"AUGESTEL_API_KEY": api_key})
                except Exception:
                    pass
        except Exception as ex:
            logger.error(f"Gagal simpan API key ke disk untuk Akun #{idx}: {ex}")

    async def ensure_account_api_key(self, idx: int) -> dict:
        """
        Ambil API key yang sudah ada atau generate API key baru secara otomatis
        dari portal Augestel (Switchfy/api/documentation).
        """
        if idx not in self.pages:
            return {"success": False, "message": f"Browser Akun #{idx} belum aktif di pool"}
        page = self.pages[idx]
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        email = acc.get("email", "")

        try:
            logger.info(f"🔑 [Akun #{idx} | {email}] Mengakses halaman API Documentation...")
            await page.goto("https://augestel.com/Switchfy/api/documentation", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)

            # Jika diarahkan ke form login, re-login dulu
            if "/login" in page.url or await page.query_selector("#loginEmail, input[name='email']"):
                await self._ensure_login_for_page(idx, page, email, acc.get("password", ""))
                await page.goto("https://augestel.com/Switchfy/api/documentation", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)

            js_extract = """
            async () => {
                // 1. Cek apakah ada display API Key di halaman
                const keyEl = document.querySelector('#api-key-display');
                if (keyEl && keyEl.textContent && keyEl.textContent.trim().startsWith('sk_live_')) {
                    return { success: true, api_key: keyEl.textContent.trim(), generated: false };
                }
                const match = document.body.innerText.match(/sk_live_[a-zA-Z0-9_\\-]+/);
                if (match) {
                    return { success: true, api_key: match[0], generated: false };
                }

                // 2. Jika belum ada, panggil generate-key melalui AJAX internal Switchfy
                const cfg = window.__cfg_clients_api_documentation || {};
                const genUrl = cfg.k3 || 'https://augestel.com/Switchfy/api/generate-key';
                const token = cfg.k4 || (document.querySelector('input[name="_token"]') ? document.querySelector('input[name="_token"]').value : '');

                try {
                    const resp = await new Promise((resolve) => {
                        window.jQuery.ajax({
                            url: genUrl,
                            type: 'POST',
                            data: { _token: token },
                            success: function(r) { resolve(r); },
                            error: function(xhr) { resolve({ success: false, error: xhr.statusText || 'AJAX Error' }); }
                        });
                    });

                    if (resp && resp.success && resp.api_key) {
                        return { success: true, api_key: resp.api_key, generated: true };
                    }
                    return { success: false, error: resp.message || resp.error || 'Gagal generate API Key', resp: resp };
                } catch (e) {
                    return { success: false, error: e.toString() };
                }
            }
            """
            eval_res = await page.evaluate(js_extract)
            if eval_res.get("success") and eval_res.get("api_key"):
                found_key = eval_res["api_key"]
                was_gen = eval_res.get("generated", False)
                action_str = "dibuat baru (Auto-Generate)" if was_gen else "berhasil diambil"
                logger.info(f"🎉 [Akun #{idx} | {email}] API Key {action_str}: {found_key[:12]}...")

                # Update memory dan simpan ke disk
                self._update_account_key_on_disk(idx, found_key)
                return {"success": True, "api_key": found_key, "generated": was_gen}
            else:
                err_msg = eval_res.get("error", "API Key tidak ditemukan dan gagal di-generate")
                logger.warning(f"⚠️ [Akun #{idx} | {email}] {err_msg}")
                return {"success": False, "message": err_msg}
        except Exception as e:
            logger.error(f"❌ [Akun #{idx} | {email}] Error ensure_account_api_key: {e}")
            return {"success": False, "message": str(e)}

    async def ensure_account_setup(self, idx: int) -> dict:
        """
        Memastikan akun baru/update siap pakai sepenuhnya:
        1. Pastikan Sesi Login Aktif.
        2. Periksa / Ambil / Auto-Generate API Key jika belum ada.
        3. Periksa / Auto-Pasang Webhook jika belum aktif.
        4. Parkir kembali halaman ke client/numbers.
        """
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        email = acc.get("email", "")
        res_summary = {"email": email, "index": idx, "api_key_ok": False, "webhook_ok": False}

        if idx not in self.pages:
            return {"success": False, "message": f"Browser Akun #{idx} belum aktif di pool"}
        page = self.pages[idx]

        # 1. Pastikan login
        if not self.status.get(idx, {}).get("logged_in"):
            ok_login = await self._ensure_login_for_page(idx, page, email, acc.get("password", ""))
            if not ok_login:
                res_summary["message"] = self.status.get(idx, {}).get("message", "Gagal login")
                return res_summary

        # 2. Periksa & Auto-Generate API Key jika belum ada
        curr_key = acc.get("api_key", "").strip()
        if not curr_key:
            key_res = await self.ensure_account_api_key(idx)
            if key_res.get("success"):
                res_summary["api_key_ok"] = True
                res_summary["api_key"] = key_res.get("api_key")
        else:
            res_summary["api_key_ok"] = True
            res_summary["api_key"] = curr_key

        # 3. Periksa & Auto-Pasang Webhook jika belum terpasang
        wh_chk = await self.check_account_webhook_status(idx)
        is_active = wh_chk.get("is_active", False)
        is_paused = wh_chk.get("is_paused", False)
        curr_url = wh_chk.get("url", "")
        if (not is_active) or is_paused or (curr_url != self.webhook_url):
            logger.info(f"⚡ [Akun #{idx} | {email}] Webhook belum terpasang/aktif, memasang webhook otomatis...")
            wh_res = await self.setup_account_webhook(idx, self.webhook_url)
            res_summary["webhook_ok"] = wh_res.get("success", False)
            res_summary["webhook_url"] = self.webhook_url
        else:
            res_summary["webhook_ok"] = True
            res_summary["webhook_url"] = curr_url

        # 4. Kembalikan tab utama ke client/numbers
        try:
            await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=20000)
        except Exception:
            pass

        res_summary["success"] = bool(res_summary["api_key_ok"] and res_summary["webhook_ok"])
        return res_summary

    def ensure_account_setup_sync(self, idx: int) -> dict:
        return self.run_coro(self.ensure_account_setup(idx), timeout=120)


    async def setup_account_webhook(self, idx: int, webhook_url: str) -> dict:
        """Pasang / aktifkan webhook secara instan via tab yang sedang terbuka di RAM."""
        if idx not in self.pages:
            return {"success": False, "message": f"Browser Akun #{idx} belum aktif di pool"}
        page = self.pages[idx]
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        email = acc.get("email", "")

        try:
            logger.info(f"🌐 [Akun #{idx} | {email}] Mengakses halaman webhook portal...")
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)

            # Jika diarahkan ke form login, lakukan re-login
            if "/login" in page.url or await page.query_selector("#loginEmail, input[name='email']"):
                await self._ensure_login_for_page(idx, page, email, acc.get("password", ""))
                await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)

            # 1. Isi URL webhook
            url_input = await page.wait_for_selector("#webhookUrl", timeout=15000)
            if url_input:
                await url_input.fill(webhook_url)

            # 2. Centang checkbox is_active dan message.received
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

            await asyncio.sleep(0.5)

            # 3. Cari dan klik tombol submit spesifik: "Save endpoint" atau "Update endpoint" (JANGAN sentuh "Remove"!)
            save_btn = await page.query_selector('button:has-text("Save endpoint"), button:has-text("Update endpoint")')
            if save_btn:
                btn_name = (await save_btn.inner_text()).strip()
                logger.info(f"Mengklik tombol webhook: '{btn_name}'...")
                await save_btn.click()
                try:
                    await page.wait_for_load_state("domcontentloaded", timeout=15000)
                except Exception:
                    pass
            else:
                logger.warning(f"Tombol Save/Update endpoint tidak ditemukan untuk Akun #{idx}")



            await asyncio.sleep(2)

            # Verifikasi apakah tersimpan di halaman setelah reload/redirect
            saved_val = await page.evaluate('() => document.querySelector("#webhookUrl") ? document.querySelector("#webhookUrl").value : ""')
            is_active = await page.evaluate('() => { const cb = document.querySelector("input[name=\'is_active\'][type=\'checkbox\']"); return cb ? (cb.checked || cb.hasAttribute("checked")) : false; }')

            # Simpan screenshot untuk verifikasi visual
            ss_path = os.path.abspath(f"webhook_result_acc_{idx}.png")
            try:
                await page.screenshot(path=ss_path)
            except Exception:
                pass

            # Kembalikan tab ke halaman client numbers agar siap standby untuk Return All & Heartbeat
            try:
                await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=20000)
            except Exception:
                pass

            ok = bool(saved_val == webhook_url and is_active)
            logger.info(f"🎉 [Akun #{idx} | {email}] Webhook status: is_active={is_active}, url={saved_val}, ok={ok}")
            return {"success": ok, "is_active": is_active, "url": saved_val, "email": email, "screenshot": ss_path}
        except Exception as e:
            logger.error(f"❌ [Akun #{idx}] Error setup webhook: {e}")
            return {"success": False, "message": str(e), "email": email}

    def setup_account_webhook_sync(self, idx: int, webhook_url: str) -> dict:
        return self.run_coro(self.setup_account_webhook(idx, webhook_url), timeout=60)

    async def setup_all_webhooks(self, webhook_url: str) -> dict:
        results = {}
        for idx in range(1, len(self.accounts) + 1):
            res = await self.setup_account_webhook(idx, webhook_url)
            results[idx] = res
            await asyncio.sleep(1)
        return {"success": any(r.get("success") for r in results.values()), "results": results}

    def setup_all_webhooks_sync(self, webhook_url: str) -> dict:
        return self.run_coro(self.setup_all_webhooks(webhook_url), timeout=300)

    # ──────────────────────────────────────────
    # WEBHOOK GUARDIAN (AUTO-RECOVERY / AUTO-ON)
    # ──────────────────────────────────────────

    async def check_account_webhook_status(self, idx: int) -> dict:
        """Memeriksa status webhook akun secara silent melalui fetch dari tab aktif."""
        if idx not in self.pages:
            return {"ok": False, "message": f"Browser Akun #{idx} belum aktif di pool"}
        page = self.pages[idx]
        acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
        email = acc.get("email", "")

        try:
            # Jalankan fetch silent ke Switchfy/api/webhooks dari konteks origin augestel.com
            js_eval = """
            async () => {
                try {
                    const res = await fetch('/Switchfy/api/webhooks', {
                        headers: { 'Accept': 'text/html' },
                        cache: 'no-store'
                    });
                    if (!res.ok) {
                        return { ok: false, status: res.status, error: 'HTTP ' + res.status };
                    }
                    const text = await res.text();
                    
                    // Cek jika sesi habis dan diarahkan ke login
                    if (text.includes('id="loginEmail"') || text.includes('name="password"')) {
                        return { ok: false, session_expired: true, error: 'Session expired' };
                    }

                    const parser = new DOMParser();
                    const doc = parser.parseFromString(text, 'text/html');

                    const whForm = doc.querySelector('form[action*="webhook"]');
                    if (!whForm) {
                        return { ok: false, error: 'Webhook form not found' };
                    }

                    // Checkbox is_active
                    const cb = whForm.querySelector('input[type="checkbox"][name="is_active"]');
                    const is_active = cb ? Boolean(cb.hasAttribute('checked') || cb.checked) : false;

                    // Endpoint URL input
                    const urlInput = whForm.querySelector('input[name="url"], #webhookUrl');
                    const current_url = urlInput ? (urlInput.getAttribute('value') || urlInput.value || '').trim() : '';

                    // Checkbox message.received
                    const msgCb = whForm.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
                    const msg_received = msgCb ? Boolean(msgCb.hasAttribute('checked') || msgCb.checked) : false;

                    // Cek peringatan otomatis gagal 20 kali (Delivery was switched off automatically)
                    const textLower = text.toLowerCase();
                    const has_auto_failure = text.includes('Delivery was switched off automatically') || 
                                             text.includes('consecutive failure(s)') ||
                                             textLower.includes('tick the box above to resume');

                    // Webhook dianggap sehat dan aktif jika is_active=true, URL terpasang, dan tidak ada failure otomatis
                    const is_delivering = is_active && !has_auto_failure && (current_url.length > 0);
                    const is_paused = has_auto_failure || (!is_active && current_url.length > 0);

                    return {
                        ok: true,
                        is_active: is_active,
                        is_paused: is_paused,
                        is_delivering: is_delivering,
                        url: current_url,
                        msg_received: msg_received
                    };
                } catch (e) {
                    return { ok: false, error: e.toString() };
                }
            }
            """
            result = await page.evaluate(js_eval)
            result["email"] = email
            result["index"] = idx
            result["checked_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return result
        except Exception as ex:
            return {
                "ok": False,
                "email": email,
                "index": idx,
                "error": str(ex),
                "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    def check_account_webhook_status_sync(self, idx: int) -> dict:
        return self.run_coro(self.check_account_webhook_status(idx), timeout=30)

    async def check_all_webhooks_status(self) -> dict:
        results = {}
        for idx in range(1, len(self.accounts) + 1):
            res = await self.check_account_webhook_status(idx)
            results[idx] = res
            await asyncio.sleep(0.5)
        return results

    def check_all_webhooks_status_sync(self) -> dict:
        return self.run_coro(self.check_all_webhooks_status(), timeout=60)

    async def _webhook_guardian_loop(self):
        """
        Sistem Penjaga Otomatis (Webhook Guardian):
        Berjalan 24/7 di latar belakang. Memeriksa status webhook setiap akun secara berkala.
        Jika webhook terdeteksi OFF (is_active=False) atau PAUSED oleh Switchfy (20x gagal),
        sistem akan secara otomatis menyalakan kembali (Auto-Heal / Auto-Resume) tanpa perlu campur tangan manual!
        """
        logger.info("🛡️ [Webhook Guardian] Service aktif! Memonitor kesehatan webhook 24/7 (Auto-Heal ON)...")
        # Beri jeda 30 detik saat pertama kali pool start agar semua akun selesai login
        await asyncio.sleep(30)

        while self.is_running:
            if not self.webhook_guardian_enabled:
                await asyncio.sleep(60)
                continue

            try:
                for idx, page in list(self.pages.items()):
                    if not self.is_running or not self.webhook_guardian_enabled:
                        break
                    acc = self.accounts[idx - 1] if 0 < idx <= len(self.accounts) else {}
                    email = acc.get("email", "")

                    if idx not in self.webhook_guardian_status:
                        self.webhook_guardian_status[idx] = {
                            "email": email,
                            "is_delivering": False,
                            "is_active": False,
                            "is_paused": False,
                            "url": "",
                            "last_check": None,
                            "auto_recovered_count": 0,
                            "last_recovery": None,
                            "status": "Checking..."
                        }

                    res = await self.check_account_webhook_status(idx)
                    if res.get("ok"):
                        is_active = res.get("is_active", False)
                        is_paused = res.get("is_paused", False)
                        is_delivering = res.get("is_delivering", False)
                        curr_url = res.get("url", "")

                        self.webhook_guardian_status[idx]["is_delivering"] = is_delivering
                        self.webhook_guardian_status[idx]["is_active"] = is_active
                        self.webhook_guardian_status[idx]["is_paused"] = is_paused
                        self.webhook_guardian_status[idx]["url"] = curr_url
                        self.webhook_guardian_status[idx]["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        # Evaluasi kondisi Auto-Heal:
                        # 1. is_active mati (False)
                        # 2. is_paused aktif (True / 20 failures)
                        # 3. URL kosong atau berbeda dari target
                        needs_healing = (not is_active) or is_paused or (curr_url != self.webhook_url)

                        if needs_healing:
                            reason = []
                            if not is_active: reason.append("is_active=False (OFF)")
                            if is_paused: reason.append("Portal Status=PAUSED (20 failures)")
                            if curr_url != self.webhook_url: reason.append(f"URL mismatch ({curr_url} != {self.webhook_url})")
                            reason_str = ", ".join(reason)

                            logger.warning(
                                f"⚠️ [Webhook Guardian] Akun #{idx} ({email}) Webhook terdeteksi bermasalah! [{reason_str}]. "
                                f"🛡️ Memulai AUTO-HEAL: Mengaktifkan kembali webhook sekarang..."
                            )
                            self.webhook_guardian_status[idx]["status"] = "Auto-Healing..."

                            # Jalankan auto-heal dengan setup_account_webhook
                            heal_result = await self.setup_account_webhook(idx, self.webhook_url)
                            if heal_result.get("success"):
                                self.webhook_guardian_status[idx]["auto_recovered_count"] += 1
                                self.webhook_guardian_status[idx]["last_recovery"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                self.webhook_guardian_status[idx]["is_delivering"] = True
                                self.webhook_guardian_status[idx]["is_active"] = True
                                self.webhook_guardian_status[idx]["is_paused"] = False
                                self.webhook_guardian_status[idx]["status"] = "🟢 Delivering (Auto-Healed)"

                                logger.info(
                                    f"🎉 [Webhook Guardian] Akun #{idx} ({email}) BERHASIL di-ON-kan kembali otomatis! "
                                    f"(Total Auto-Recoveries: {self.webhook_guardian_status[idx]['auto_recovered_count']})"
                                )

                                # Tulis notifikasi ke bot.log agar tampil di dashboard live-stream
                                log_entry = (
                                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} │ INFO     │ OTPBot │ "
                                    f"🛡️ [Webhook Guardian] Webhook Akun #{idx} ({email}) sempat OFF/Paused dan telah OTOMATIS DINYALAKAN KEMBALI!\n"
                                )
                                try:
                                    with open(os.path.join(BASE_DIR, "bot.log"), "a", encoding="utf-8") as f_log:
                                        f_log.write(log_entry)
                                except Exception:
                                    pass
                            else:
                                logger.error(f"❌ [Webhook Guardian] Gagal auto-heal Akun #{idx}: {heal_result.get('message')}")
                                self.webhook_guardian_status[idx]["status"] = f"Heal Failed: {heal_result.get('message')}"
                        else:
                            self.webhook_guardian_status[idx]["status"] = "🟢 Delivering"
                    else:
                        if res.get("session_expired"):
                            logger.warning(f"⚠️ [Webhook Guardian] Akun #{idx} sesi login habis, melakukan re-login...")
                            await self._ensure_login_for_page(idx, page, email, acc.get("password", ""))

                    await asyncio.sleep(2)

                # Cek berkala setiap 2 menit (120 detik)
                await asyncio.sleep(120)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in _webhook_guardian_loop: {e}")
                await asyncio.sleep(30)

    def get_webhook_guardian_status(self) -> dict:
        return self.webhook_guardian_status

    async def _trigger_guardian_auto_heal_async(self) -> dict:
        """Trigger pemeriksaan dan auto-heal instan untuk semua akun sekarang juga."""
        results = {}
        for idx in range(1, len(self.accounts) + 1):
            chk = await self.check_account_webhook_status(idx)
            is_active = chk.get("is_active", False)
            is_paused = chk.get("is_paused", False)
            curr_url = chk.get("url", "")
            if (not is_active) or is_paused or (curr_url != self.webhook_url):
                heal = await self.setup_account_webhook(idx, self.webhook_url)
                results[idx] = {"checked": chk, "auto_healed": True, "heal_result": heal}
            else:
                results[idx] = {"checked": chk, "auto_healed": False, "status": "Already Active"}
        return results

    def trigger_guardian_auto_heal_sync(self) -> dict:
        return self.run_coro(self._trigger_guardian_auto_heal_async(), timeout=180)

    def get_status_dict(self) -> dict:
        return self.status

    # ──────────────────────────────────────────
    # AUTO-ADD NUMBERS VIA LIVE BROWSER POOL
    # ──────────────────────────────────────────

    async def run_auto_add_account(
        self,
        account_idx: int,
        range_filter: str = "",
        max_add: int = 0,
        delay: int = 15,
        workers_count: int = 2,
        batch_count: int = 250,
        number_prefix: str = "",
        shared_stats: dict = None,
        stats_lock: asyncio.Lock = None,
        status_callback = None
    ):
        """Menjalankan Auto-Add Augestel menggunakan Live Browser Profile yang aktif di RAM."""
        from auto_add_augestel import (
            fetch_test_terminations,
            get_termination_details,
            submit_add_number,
            run_worker,
            MAX_ACCOUNT_NUMBERS
        )

        if account_idx not in self.pages or account_idx not in self.contexts:
            msg = f"Browser Akun #{account_idx} belum aktif di RAM pool"
            logger.error(f"❌ {msg}")
            if status_callback:
                status_callback({"last_message": msg})
            return

        acc = self.accounts[account_idx - 1] if 0 < account_idx <= len(self.accounts) else {}
        email = acc.get("email", "")
        password = acc.get("password", "")
        context = self.contexts[account_idx]
        main_page = self.pages[account_idx]

        log_msg = f"🚀 [Live Pool] Memulai Auto-Add untuk Akun #{account_idx} ({email}) via Browser Profile RAM..."
        logger.info(log_msg)
        if status_callback:
            status_callback({"account_email": f"Akun #{account_idx} ({email})", "last_message": log_msg})

        # Pastikan sesi aktif dan buka halaman test numbers
        try:
            if "/test/numbers" not in main_page.url:
                await main_page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)

            login_input = await main_page.query_selector("#loginEmail, input[name='email']")
            if login_input:
                await self._ensure_login_for_page(account_idx, main_page, email, password)
                await main_page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)
        except Exception as ex_nav:
            logger.warning(f"Nav test numbers error: {ex_nav}")

        # Cek jumlah nomor akun saat ini
        init_count = 0
        try:
            cnt = await main_page.evaluate('''async () => {
                try {
                    const resp = await fetch('/Switchfy/client/numbers?draw=1&start=0&length=1', {
                        headers: { 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json' }
                    });
                    if (resp.ok) {
                        const data = await resp.json();
                        return data.recordsTotal !== undefined ? data.recordsTotal : (data.recordsFiltered || 0);
                    }
                } catch(e) {}
                return -1;
            }''')
            if cnt >= 0:
                init_count = int(cnt)
        except Exception:
            pass

        if init_count >= MAX_ACCOUNT_NUMBERS:
            warn_msg = f"⚠️ [Akun #{account_idx}] Sudah mencapai batas {init_count}/{MAX_ACCOUNT_NUMBERS} nomor! Melewati akun ini..."
            logger.warning(warn_msg)
            if status_callback:
                status_callback({"last_message": warn_msg})
            return

        # Fetch terminations matching filter
        needed_records = 50 if max_add <= 0 else min(max(max_add, 25), 100)
        dt_res = await fetch_test_terminations(main_page, range_filter, number_search=number_prefix, start=0, length=needed_records)
        raw_rows = []
        total_found = 0
        if dt_res and not dt_res.get("error"):
            total_found = dt_res.get("recordsFiltered", 0) or dt_res.get("recordsTotal", 0) or 0
            raw_rows = dt_res.get("data", [])

        if status_callback:
            status_callback({"total_found": total_found, "last_message": f"Ditemukan {total_found} terminations untuk Akun #{account_idx}."})

        if not raw_rows:
            warn_msg = f"⚠️ [Akun #{account_idx}] Tidak ada termination yang cocok dengan filter."
            logger.warning(warn_msg)
            if status_callback:
                status_callback({"last_message": warn_msg})
            return

        # Antrian pekerjaan
        clean_prefix = re.sub(r'[\s\+\-]', '', number_prefix) if number_prefix else ""
        queue = asyncio.Queue()
        for r in raw_rows:
            action_html = r.get("action", "")
            id_match = re.search(r'data-termination-id="(\d+)"', action_html)
            term_id = id_match.group(1) if id_match else None
            num_html = r.get("test_number", "")
            num_match = re.search(r'data-copy-number="([^"]+)"', num_html)
            num = num_match.group(1) if num_match else ""
            clean_num = re.sub(r'[\s\+\-]', '', num)

            if clean_prefix and not (clean_num.startswith(clean_prefix) or clean_prefix in clean_num):
                continue
            if term_id:
                queue.put_nowait({
                    "name": r.get("name", ""),
                    "test_number": num,
                    "term_id": term_id
                })

        q_size = queue.qsize()
        if q_size == 0:
            return

        # Buat worker pages jika workers_count > 1
        worker_pages = [main_page]
        for w_i in range(1, workers_count):
            try:
                new_p = await context.new_page()
                await new_p.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded")
                worker_pages.append(new_p)
            except Exception as e:
                logger.warning(f"Gagal buat tab worker #{w_i + 1}: {e}")

        account_state = {
            "current_total": init_count,
            "added": 0,
            "limit_reached": False
        }

        # Jalankan worker
        tasks = []
        for i, w_page in enumerate(worker_pages):
            tasks.append(
                asyncio.create_task(
                    run_worker(
                        worker_id=i + 1,
                        account_idx=account_idx,
                        account_email=email,
                        page=w_page,
                        queue=queue,
                        shared_stats=shared_stats,
                        account_state=account_state,
                        stats_lock=stats_lock,
                        delay=delay,
                        max_add=max_add,
                        batch_count=batch_count
                    )
                )
            )

        # Monitor progress dan check stop flag
        async def monitor_task():
            while any(not t.done() for t in tasks):
                if self.auto_add_stop_flag:
                    logger.info("🛑 Auto-add stop flag terdeteksi, membatalkan tasks...")
                    for t in tasks:
                        t.cancel()
                    break
                if status_callback:
                    status_callback({
                        "added": shared_stats["added"],
                        "failed": shared_stats["failed"],
                        "skipped": shared_stats["skipped"],
                        "current_action": shared_stats["current_action"],
                        "last_message": f"Menambahkan nomor Akun #{account_idx}: Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}"
                    })
                await asyncio.sleep(1)

        mon_t = asyncio.create_task(monitor_task())
        await asyncio.gather(*tasks, return_exceptions=True)
        mon_t.cancel()

        # Bersihkan worker pages tambahan (hanya sisakan main_page)
        for wp in worker_pages[1:]:
            try:
                await wp.close()
            except Exception:
                pass

        # Kembalikan tab utama ke client/numbers
        try:
            await main_page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="domcontentloaded", timeout=20000)
        except Exception:
            pass

    async def run_auto_add_multi(
        self,
        account_indices: list,
        range_filter: str = "",
        max_add: int = 0,
        delay: int = 15,
        workers_count: int = 2,
        batch_count: int = 250,
        number_prefix: str = "",
        status_callback = None
    ):
        self.auto_add_running = True
        self.auto_add_stop_flag = False
        shared_stats = {
            "added": 0,
            "failed": 0,
            "skipped": 0,
            "current_action": 0
        }
        stats_lock = asyncio.Lock()

        try:
            for idx in account_indices:
                if self.auto_add_stop_flag:
                    break
                if max_add > 0 and shared_stats["added"] >= max_add:
                    break
                await self.run_auto_add_account(
                    account_idx=idx,
                    range_filter=range_filter,
                    max_add=max_add,
                    delay=delay,
                    workers_count=workers_count,
                    batch_count=batch_count,
                    number_prefix=number_prefix,
                    shared_stats=shared_stats,
                    stats_lock=stats_lock,
                    status_callback=status_callback
                )
                await asyncio.sleep(2)
        finally:
            self.auto_add_running = False
            if status_callback:
                status_callback({
                    "running": False,
                    "added": shared_stats["added"],
                    "failed": shared_stats["failed"],
                    "skipped": shared_stats["skipped"],
                    "last_message": f"Auto-Add Selesai! Total Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}"
                })

    def stop_auto_add(self):
        self.auto_add_stop_flag = True
        self.auto_add_running = False


# Global singleton helper
def get_browser_pool():
    return AugestelBrowserPool.get_instance()


