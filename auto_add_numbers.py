# ═══════════════════════════════════════════════════════════════
#  AUTO ADD NUMBERS - IVASMS
#  ─────────────────────────────────────────────────────────────
#  Otomatis add number berdasarkan Range Name dari halaman
#  https://www.ivasms.com/portal/numbers/test
#  dengan delay 1 menit per action.
#
#  Menggunakan Playwright persistent browser untuk bypass
#  Cloudflare dan menjaga session tetap valid.
# ═══════════════════════════════════════════════════════════════

import asyncio
import json
import logging
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from playwright.async_api import async_playwright

# ────────────────────────────────────────────
#  KONFIGURASI
# ────────────────────────────────────────────

# Range name yang ingin di-add (case-insensitive search)
# Contoh: "RUSSIA 1", "UZBEKISTAN", "MALAWI", dll.
# Bisa sebagian nama: "RUSSIA" akan cocok dengan RUSSIA 1, RUSSIA 2, dst.
RANGE_NAME = ""  # <-- ISI DI SINI atau via command line

# Jumlah maksimum nomor yang akan di-add (0 = semua yang ditemukan)
MAX_ADD = 0

# Delay antar action (dalam detik). Default: 60 detik (1 menit)
DELAY_SECONDS = 60

# Berapa banyak rows yang di-fetch per batch dari DataTable
BATCH_SIZE = 50

# ────────────────────────────────────────────

def get_account_config(account_index: int = 1) -> dict:
    """Muat konfigurasi dan direktori profile browser untuk akun IVASMS terpilih."""
    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        try:
            import config
            if getattr(config, "IVASMS_EMAIL", "") and getattr(config, "IVASMS_PASSWORD", ""):
                accounts.append({"email": config.IVASMS_EMAIL, "password": config.IVASMS_PASSWORD})
            if getattr(config, "IVASMS_EMAIL_2", "") and getattr(config, "IVASMS_PASSWORD_2", ""):
                accounts.append({"email": config.IVASMS_EMAIL_2, "password": config.IVASMS_PASSWORD_2})
        except Exception:
            pass

    email = ""
    pwd = ""
    if accounts and 1 <= account_index <= len(accounts):
        email = accounts[account_index - 1].get("email", "")
        pwd = accounts[account_index - 1].get("password", "")
    elif accounts:
        email = accounts[0].get("email", "")
        pwd = accounts[0].get("password", "")

    if account_index == 1:
        user_data_dir = os.path.abspath("browser_profile")
    else:
        user_data_dir = os.path.abspath(f"browser_profile_acc{account_index}")

    return {
        "index": account_index,
        "email": email,
        "password": pwd,
        "user_data_dir": user_data_dir
    }


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("auto_add")


async def wait_cloudflare(page, max_wait=30):
    """Tunggu Cloudflare challenge selesai"""
    for _ in range(max_wait):
        title = await page.title()
        if "Just a moment" not in title:
            return True
        await asyncio.sleep(1)
    return False


async def auto_login_if_needed(page, context, email: str = "", password: str = ""):
    """Auto-login jika session expired menggunakan akun yang dipilih"""
    if not email or not password:
        try:
            from config import IVASMS_EMAIL, IVASMS_PASSWORD
            email = email or IVASMS_EMAIL
            password = password or IVASMS_PASSWORD
        except Exception:
            pass

    url = page.url
    if "/login" not in url:
        has_login = await page.query_selector("input[name='email']")
        if not has_login:
            return True  # Already logged in

    logger.info(f"🔑 Session expired, melakukan auto-login dengan {email}...")
    try:
        await page.fill("input[name='email']", email)
        await page.fill("input[name='password']", password)

        remember = await page.query_selector("input[name='remember']")
        if remember and not await remember.is_checked():
            await remember.check()

        await asyncio.sleep(2)

        submit = await page.query_selector("button[type='submit']")
        if submit:
            await submit.click()
        else:
            await page.keyboard.press("Enter")

        for _ in range(15):
            await asyncio.sleep(1)
            if "/portal" in page.url:
                logger.info("🎉 Auto-login berhasil!")
                return True

        logger.error("❌ Auto-login gagal - tidak redirect ke portal")
        return False

    except Exception as e:
        logger.error(f"❌ Error saat auto-login: {e}")
        return False


async def fetch_ranges(page, range_search, start=0, length=50):
    """
    Fetch data ranges dari DataTable API.
    Mengembalikan list of {id, range, test_number, ...}
    """
    result = await page.evaluate("""
        async ([rangeSearch, start, length]) => {
            try {
                const url = new URL('/portal/numbers/test', window.location.origin);
                url.searchParams.set('draw', '1');
                url.searchParams.set('start', start.toString());
                url.searchParams.set('length', length.toString());

                // Columns sesuai DataTable config
                const cols = [
                    {data: 'range', name: 'terminations.range', searchable: true, orderable: true},
                    {data: 'test_number', name: 'terminations.test_number', searchable: true, orderable: true},
                    {data: 'term', name: 'term'},
                    {data: 'A2P', name: 'A2P'},
                    {data: 'Limit_Range', name: 'Limit_Range'},
                    {data: 'limit_did_a2p', name: 'limit_did_a2p'},
                    {data: 'limit_cli_did_a2p', name: 'limit_cli_did_a2p'},
                    {data: 'created_at', name: 'terminations.created_at'},
                    {data: 'action', name: 'action'},
                ];

                cols.forEach((col, i) => {
                    url.searchParams.set(`columns[${i}][data]`, col.data);
                    url.searchParams.set(`columns[${i}][name]`, col.name);
                    if (col.searchable) url.searchParams.set(`columns[${i}][searchable]`, 'true');
                    if (col.orderable) url.searchParams.set(`columns[${i}][orderable]`, 'true');
                });

                // Filter by range name (column 0 search)
                if (rangeSearch) {
                    url.searchParams.set('columns[0][search][value]', rangeSearch);
                }

                url.searchParams.set('order[0][column]', '8');
                url.searchParams.set('order[0][dir]', 'desc');
                url.searchParams.set('search[value]', '');

                const resp = await fetch(url.toString(), {
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept': 'application/json'
                    }
                });

                if (!resp.ok) {
                    return {error: `HTTP ${resp.status}`, data: [], recordsTotal: 0, recordsFiltered: 0};
                }

                return await resp.json();
            } catch(e) {
                return {error: e.message, data: [], recordsTotal: 0, recordsFiltered: 0};
            }
        }
    """, [range_search, start, length])

    return result


async def add_number(page, termination_id, csrf_token):
    """
    Add number via AJAX POST ke /portal/numbers/termination/number/add
    Mengembalikan {success, message}
    """
    result = await page.evaluate("""
        async ([id, token]) => {
            try {
                const resp = await fetch('/portal/numbers/termination/number/add', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRF-TOKEN': token,
                        'Accept': 'application/json'
                    },
                    body: `_token=${encodeURIComponent(token)}&id=${encodeURIComponent(id)}`
                });

                const status = resp.status;
                let body;
                try {
                    body = await resp.json();
                } catch(e) {
                    body = {message: await resp.text()};
                }

                return {
                    status: status,
                    success: status >= 200 && status < 300,
                    message: body.message || JSON.stringify(body)
                };
            } catch(e) {
                return {status: 0, success: false, message: e.message};
            }
        }
    """, [str(termination_id), csrf_token])

    return result


async def get_csrf_token(page):
    """Ambil CSRF token dari halaman"""
    token = await page.evaluate("""
        () => {
            const meta = document.querySelector('meta[name="csrf-token"]');
            if (meta) return meta.content;
            const input = document.querySelector('input[name="_token"]');
            if (input) return input.value;
            return '';
        }
    """)
    return token


async def run_worker(worker_id: int, account_idx: int, account_email: str, page, initial_csrf: str, queue: asyncio.Queue, shared_stats: dict, stats_lock: asyncio.Lock, delay: int, max_add: int):
    """Worker task independen yang mengeksekusi penambahan nomor dari antrian."""
    csrf = initial_csrf
    while not queue.empty():
        # Cek apakah max add sudah tercapai
        async with stats_lock:
            if max_add > 0 and shared_stats["added"] >= max_add:
                break
            shared_stats["current_action"] += 1
            action_num = shared_stats["current_action"]

        try:
            row = await queue.get()
        except asyncio.QueueEmpty:
            break

        termination_id = row.get("id")
        row_range = row.get("range", "")
        test_number = row.get("test_number", "")

        if not termination_id:
            queue.task_done()
            continue

        logger.info(f"── [Worker #{worker_id} | Akun #{account_idx}] Action #{action_num} ──")
        logger.info(f"  📋 Range: {row_range} | 📱 Number: {test_number} | 🆔 ID: {termination_id}")

        res = await add_number(page, termination_id, csrf)

        success = res.get("success", False)
        status = res.get("status", 0)
        msg = res.get("message", "Unknown")

        if success:
            async with stats_lock:
                shared_stats["added"] += 1
            logger.info(f"  ✅ [Worker #{worker_id}] Berhasil! {msg}")
        else:
            if status == 419:
                # CSRF Expired, reload page untuk token baru
                logger.warning(f"  ⚠️ [Worker #{worker_id}] CSRF expired, refreshing page...")
                try:
                    await page.reload(wait_until="domcontentloaded")
                    await asyncio.sleep(2)
                    new_csrf = await get_csrf_token(page)
                    if new_csrf:
                        csrf = new_csrf
                    retry_res = await add_number(page, termination_id, csrf)
                    if retry_res.get("success"):
                        async with stats_lock:
                            shared_stats["added"] += 1
                        logger.info(f"  ✅ [Worker #{worker_id}] Berhasil setelah refresh! {retry_res.get('message', '')}")
                    else:
                        async with stats_lock:
                            shared_stats["failed"] += 1
                        logger.error(f"  ❌ [Worker #{worker_id}] Gagal: {retry_res.get('message', '')}")
                except Exception as e:
                    async with stats_lock:
                        shared_stats["failed"] += 1
                    logger.error(f"  ❌ [Worker #{worker_id}] Error saat refresh: {e}")
            elif status == 429:
                logger.warning(f"  ⚠️ [Worker #{worker_id}] Rate limited! Menunggu 120 detik...")
                async with stats_lock:
                    shared_stats["skipped"] += 1
                await asyncio.sleep(120)
            elif "already" in msg.lower() or "exist" in msg.lower():
                async with stats_lock:
                    shared_stats["skipped"] += 1
                logger.info(f"  ⏩ [Worker #{worker_id}] Sudah ada: {msg}")
            else:
                async with stats_lock:
                    shared_stats["failed"] += 1
                logger.error(f"  ❌ [Worker #{worker_id}] Gagal: [{status}] {msg}")

        queue.task_done()

        async with stats_lock:
            curr_added = shared_stats["added"]
            curr_failed = shared_stats["failed"]
            curr_skipped = shared_stats["skipped"]

        logger.info(f"  📊 Stats: Added={curr_added}, Failed={curr_failed}, Skipped={curr_skipped}")

        if max_add > 0 and curr_added >= max_add:
            break

        if not queue.empty() and delay > 0:
            await asyncio.sleep(delay)


async def main():
    range_name = RANGE_NAME
    max_add = MAX_ADD
    delay = DELAY_SECONDS
    account_arg = "1"
    num_workers = 1

    # Format CLI: python auto_add_numbers.py "RANGE_NAME" [MAX_ADD] [DELAY] [ACCOUNT_INDEX_OR_ALL] [WORKERS]
    if len(sys.argv) >= 2:
        range_name = sys.argv[1]
    if len(sys.argv) >= 3:
        try:
            max_add = int(sys.argv[2])
        except Exception:
            max_add = 0
    if len(sys.argv) >= 4:
        try:
            delay = int(sys.argv[3])
        except Exception:
            delay = 60
    if len(sys.argv) >= 5:
        account_arg = str(sys.argv[4]).strip().lower()
    if len(sys.argv) >= 6:
        try:
            num_workers = max(1, min(int(sys.argv[5]), 36))
        except Exception:
            num_workers = 1

    # Interactive mode jika tidak ada parameter
    if not range_name:
        print("=" * 60)
        print("  ⚡ MULTI-WORKER AUTO ADD NUMBERS - IVASMS")
        print("=" * 60)
        print()
        print("  Penggunaan CLI:")
        print('    python auto_add_numbers.py "RANGE_NAME" [MAX_ADD] [DELAY] [ACCOUNT] [WORKERS]')
        print()
        print("  Contoh (VPS High Performance):")
        print('    python auto_add_numbers.py "RUSSIA" 50 15 1 4      # Akun 1, 4 Workers paralel')
        print('    python auto_add_numbers.py "RUSSIA" 100 20 all 8    # Semua Akun, 8 Workers paralel')
        print()

        acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
        accounts_list = []
        if os.path.exists(acc_file):
            try:
                with open(acc_file, "r", encoding="utf-8") as f:
                    accounts_list = json.load(f)
            except Exception:
                pass

        if accounts_list:
            print("  📋 Daftar Akun IVASMS:")
            for i, a in enumerate(accounts_list, start=1):
                print(f"    [{i}] Akun #{i}: {a.get('email')}")
            print(f"    [all] Semua Akun Sekaligus (Parallel All Accounts)")
            choice = input("  Pilih Akun [1/2/.../all] (default 1): ").strip().lower()
            if choice:
                account_arg = choice
            print()

        range_name = input("  Masukkan Range Name: ").strip()
        if not range_name:
            print("  [!] Range name tidak boleh kosong!")
            return

        max_input = input("  Maks jumlah add (0 = semua) [0]: ").strip()
        max_add = int(max_input) if max_input else 0

        delay_input = input("  Delay per action per worker (detik) [60]: ").strip()
        delay = int(delay_input) if delay_input else 60

        w_input = input("  Jumlah Parallel Workers (1-36) [1]: ").strip()
        if w_input.isdigit():
            num_workers = max(1, min(int(w_input), 36))

    # Tentukan target akun yang akan diproses
    acc_file = os.path.join(os.path.dirname(__file__), "ivasms_accounts.json")
    all_accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                all_accounts = json.load(f)
        except Exception:
            pass

    if not all_accounts:
        all_accounts = [{"email": "Default", "password": ""}]

    target_accounts = []
    if account_arg == "all":
        target_accounts = [get_account_config(i + 1) for i in range(len(all_accounts))]
    else:
        try:
            target_idx = int(account_arg)
        except Exception:
            target_idx = 1
        target_accounts = [get_account_config(target_idx)]

    print()
    logger.info("═" * 58)
    logger.info("  ⚡ MULTI-WORKER PARALLEL AUTO ADD NUMBERS")
    logger.info("═" * 58)
    logger.info(f"  🔍 Range Name       : {range_name}")
    logger.info(f"  👥 Target Akun      : {len(target_accounts)} Akun ({', '.join('Akun #' + str(a['index']) for a in target_accounts)})")
    logger.info(f"  🚀 Parallel Workers : {num_workers} Workers")
    logger.info(f"  📊 Max Add          : {'Unlimited' if max_add == 0 else max_add}")
    logger.info(f"  ⏱️  Delay Worker     : {delay} detik")
    logger.info("═" * 58)

    # Proses setiap akun (atau jalankan worker per akun)
    for acc in target_accounts:
        acc_idx = acc["index"]
        user_data_dir = acc["user_data_dir"]
        login_email = acc["email"]
        login_password = acc["password"]

        logger.info(f"🚀 Membuka browser context untuk Akun #{acc_idx} ({login_email})...")

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
                    ]
                )
            except Exception as launch_err:
                logger.error(f"❌ Gagal launch browser Akun #{acc_idx}: {launch_err}")
                continue

            main_page = context.pages[0] if context.pages else await context.new_page()

            logger.info("🌐 Navigating ke halaman Test Numbers...")
            try:
                await main_page.goto(
                    "https://www.ivasms.com/portal/numbers/test",
                    timeout=45000,
                    wait_until="domcontentloaded"
                )
            except Exception as e:
                logger.warning(f"Navigation warning: {e}")

            if not await wait_cloudflare(main_page, 30):
                logger.error("❌ Cloudflare challenge timeout!")
                await context.close()
                continue

            await asyncio.sleep(2)

            if not await auto_login_if_needed(main_page, context, email=login_email, password=login_password):
                await context.close()
                continue

            if "/portal/numbers/test" not in main_page.url:
                await main_page.goto(
                    "https://www.ivasms.com/portal/numbers/test",
                    timeout=30000,
                    wait_until="domcontentloaded"
                )
                await asyncio.sleep(2)

            main_csrf = await get_csrf_token(main_page)
            if not main_csrf:
                logger.error("❌ Gagal mendapatkan CSRF token!")
                await context.close()
                continue

            logger.info(f"🔐 CSRF token verified: {main_csrf[:15]}...")

            # Fetch matching numbers ke antrian
            logger.info(f"🔍 Mengambil daftar nomor range '{range_name}' dari DataTable...")
            items_queue = asyncio.Queue()
            fetch_start = 0
            has_more = True
            total_found = 0

            while has_more:
                batch_res = await fetch_ranges(main_page, range_name, fetch_start, BATCH_SIZE)
                if 'error' in batch_res and batch_res['error']:
                    logger.error(f"❌ DataTable Error: {batch_res['error']}")
                    break

                records_total = batch_res.get('recordsFiltered', 0)
                rows = batch_res.get('data', [])

                if fetch_start == 0:
                    total_found = records_total
                    logger.info(f"📊 Ditemukan {total_found} total records untuk '{range_name}'")

                if not rows:
                    break

                for r in rows:
                    items_queue.put_nowait(r)

                fetch_start += BATCH_SIZE
                if fetch_start >= records_total:
                    has_more = False

            if items_queue.empty():
                logger.info(f"📭 Tidak ada nomor yang ditemukan untuk '{range_name}'.")
                await context.close()
                continue

            # Buat worker pages / tabs
            logger.info(f"⚡ Menyiapkan {num_workers} parallel worker tabs...")
            worker_pages = [main_page]
            for _ in range(num_workers - 1):
                try:
                    new_p = await context.new_page()
                    worker_pages.append(new_p)
                except Exception as tab_err:
                    logger.warning(f"Tidak dapat membuat tab tambahan: {tab_err}")
                    break

            shared_stats = {
                "added": 0,
                "failed": 0,
                "skipped": 0,
                "current_action": 0
            }
            stats_lock = asyncio.Lock()

            # Jalankan worker secara paralel
            worker_tasks = [
                run_worker(
                    worker_id=w_i + 1,
                    account_idx=acc_idx,
                    account_email=login_email,
                    page=p_inst,
                    initial_csrf=main_csrf,
                    queue=items_queue,
                    shared_stats=shared_stats,
                    stats_lock=stats_lock,
                    delay=delay,
                    max_add=max_add
                )
                for w_i, p_inst in enumerate(worker_pages)
            ]

            await asyncio.gather(*worker_tasks)

            # Summary per akun
            logger.info("")
            logger.info("═" * 58)
            logger.info(f"  📊 RINGKASAN AKUN #{acc_idx} ({login_email})")
            logger.info("═" * 58)
            logger.info(f"  🔍 Range Name : {range_name}")
            logger.info(f"  ✅ Berhasil   : {shared_stats['added']}")
            logger.info(f"  ❌ Gagal      : {shared_stats['failed']}")
            logger.info(f"  ⏩ Dilewati   : {shared_stats['skipped']}")
            logger.info(f"  📊 Total      : {shared_stats['added'] + shared_stats['failed'] + shared_stats['skipped']}")
            logger.info("═" * 58)

            await context.close()

    logger.info("🏁 Semua proses Auto-Add selesai!")


if __name__ == "__main__":
    asyncio.run(main())
