# ═══════════════════════════════════════════════════════════════
#  AUTO ADD NUMBERS - AUGESTEL
#  ─────────────────────────────────────────────────────────────
#  Otomatis add number dari halaman portal Augestel:
#  https://augestel.com/Switchfy/test/numbers
#  menggunakan browser persistent Edge offscreen.
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
#  KONFIGURASI DEFAULT
# ────────────────────────────────────────────

RANGE_NAME = ""
MAX_ADD = 0
DELAY_SECONDS = 15
BATCH_SIZE = 25
BATCH_COUNT = 250  # Default 250 nomor per request sesuai form Augestel
MAX_ACCOUNT_NUMBERS = 2500  # Batas maksimal nomor per akun portal Augestel

# ────────────────────────────────────────────

def get_account_config(account_index: int = 1) -> dict:
    """Muat konfigurasi dan direktori profile browser untuk akun Augestel terpilih."""
    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
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
            email = getattr(config, "AUGESTEL_EMAIL", "saputradimas0878@gmail.com")
            pwd = getattr(config, "AUGESTEL_PASSWORD", "dimas098.")
            accounts.append({"email": email, "password": pwd})
        except Exception:
            pass

    email = ""
    pwd = ""
    api_key = ""
    if accounts and 1 <= account_index <= len(accounts):
        email = accounts[account_index - 1].get("email", "")
        pwd = accounts[account_index - 1].get("password", "")
        api_key = accounts[account_index - 1].get("api_key", "")
    elif accounts:
        email = accounts[0].get("email", "")
        pwd = accounts[0].get("password", "")
        api_key = accounts[0].get("api_key", "")

    user_data_dir = os.path.abspath(f"browser_profile_augestel_{account_index}")

    return {
        "index": account_index,
        "email": email,
        "password": pwd,
        "api_key": api_key,
        "user_data_dir": user_data_dir
    }


async def get_account_current_numbers_count(page, account_idx: int, api_key: str = "", email: str = "") -> int:
    """Cek total nomor yang sudah aktif di portal untuk akun ini."""
    # 1. Coba lewat API Augestel (tercepat ~200ms)
    if api_key:
        try:
            from augestel_client import AugestelClient
            c = AugestelClient(api_key=api_key, email=email)
            res = c.get_numbers(page=1, per_page=1)
            if res.get("success"):
                tot = res.get("pagination", {}).get("total")
                if tot is not None:
                    return int(tot)
        except Exception as e:
            logger.debug(f"API check total numbers gagal: {e}")

    # 2. Coba lewat browser session yang sedang terbuka
    if page:
        try:
            cnt = await page.evaluate('''async () => {
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
                return int(cnt)
        except Exception:
            pass

    # 3. Fallback ke disk cache lokal jika ada
    try:
        cache_file = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{account_idx}.json")
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                d = json.load(f)
                return int(d.get("total", 0))
    except Exception:
        pass

    return 0


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("auto_add_augestel")


async def ensure_augestel_login(page, email: str, password: str) -> bool:
    """Login ke portal Augestel jika session belum aktif atau expired."""
    try:
        logger.info(f"🔍 Memeriksa status login untuk {email}...")
        await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)

        title = await page.title()
        if "one moment" in title.lower() or "too quick" in title.lower():
            logger.warning("⚠️ Terdeteksi rate-limit cooldown Augestel. Menunggu 10 detik...")
            await asyncio.sleep(10)
            await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded", timeout=45000)

        login_input = await page.query_selector("#loginEmail, input[name='email']")
        curr_url = page.url
        curr_title = await page.title()

        if "login" in curr_title.lower() or login_input or "/login" in curr_url or curr_url == "https://augestel.com/Switchfy":
            logger.info(f"🔑 Session belum aktif, melakukan login untuk {email}...")
            if not login_input:
                await page.goto("https://augestel.com/Switchfy", wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(2)

            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            rem = await page.query_selector("input[name='remember']")
            if rem:
                try:
                    await rem.check()
                except Exception:
                    pass
            await asyncio.sleep(1)

            btn = await page.query_selector("#loginSubmit, button[type='submit']")
            if btn:
                await btn.click()
            else:
                await page.keyboard.press("Enter")

            for _ in range(15):
                await asyncio.sleep(1)
                t = await page.title()
                u = page.url
                if "login" not in t.lower() and u != "https://augestel.com/Switchfy":
                    logger.info(f"🎉 Login berhasil! URL: {u}")
                    break

            await page.goto("https://augestel.com/Switchfy/test/numbers", wait_until="networkidle", timeout=45000)
            await asyncio.sleep(2)

        final_title = await page.title()
        if "test numbers" in final_title.lower() or "client panel" in final_title.lower():
            logger.info("✅ Siap di halaman Test Numbers Augestel!")
            return True
        else:
            logger.warning(f"⚠️ Halaman saat ini: {page.url} ({final_title})")
            return True
    except Exception as e:
        logger.error(f"❌ Error saat memastikan login Augestel: {e}")
        return False


async def fetch_test_terminations(page, range_search: str = "", start: int = 0, length: int = 25) -> dict:
    """Fetch terminations dari DataTable Augestel."""
    res = await page.evaluate('''async ([rangeSearch, start, length]) => {
        try {
            const url = new URL('/Switchfy/test/numbers', window.location.origin);
            url.searchParams.set('draw', '1');
            url.searchParams.set('start', start.toString());
            url.searchParams.set('length', length.toString());

            const cols = [
                { data: 'name', name: 'name', searchable: true, orderable: true },
                { data: 'country', name: 'country_code', searchable: true, orderable: true },
                { data: 'test_number', name: 'test_number', searchable: true, orderable: true },
                { data: 'a2p_rate', name: 'client_a2p_rate', searchable: true, orderable: true },
                { data: 'portal_limit_a2p', name: 'portal_limit_a2p' },
                { data: 'a2p_sid_range', name: 'a2p_sid_range' },
                { data: 'a2p_multi_limit', name: 'a2p_multi_limit' },
                { data: 'a2p_sid_did_limit', name: 'a2p_sid_did_limit' },
                { data: 'created_at', name: 'terminations.created_at', searchable: false },
                { data: 'action', name: 'action', searchable: false, orderable: false }
            ];

            cols.forEach((col, i) => {
                url.searchParams.set('columns[' + i + '][data]', col.data);
                if (col.name) url.searchParams.set('columns[' + i + '][name]', col.name);
                if (col.searchable !== undefined) url.searchParams.set('columns[' + i + '][searchable]', col.searchable.toString());
                if (col.orderable !== undefined) url.searchParams.set('columns[' + i + '][orderable]', col.orderable.toString());
            });

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
                return { error: 'HTTP ' + resp.status, data: [], recordsTotal: 0, recordsFiltered: 0 };
            }
            return await resp.json();
        } catch(e) {
            return { error: e.message, data: [], recordsTotal: 0, recordsFiltered: 0 };
        }
    }''', [range_search, start, length])
    return res


async def get_termination_details(page, termination_id: str) -> dict:
    """Fetch info detail termination & request token dari Augestel."""
    res = await page.evaluate('''async (termId) => {
        try {
            const cfg = window.__cfg_clients_add_number_test || {};
            const url = cfg.k3 || 'https://augestel.com/Switchfy/client/numbers/terminations';
            const resp = await window.jQuery.ajax({
                url: url,
                type: 'GET',
                cache: false,
                data: { termination_id: termId, _: Date.now() }
            });
            return { ok: true, data: resp, cfg: cfg };
        } catch(e) {
            return { ok: false, status: e.status, error: e.statusText || e.responseText };
        }
    }''', str(termination_id))
    return res


async def submit_add_number(page, term_data: dict, cfg: dict, count: int = 250) -> dict:
    """Kirim POST request untuk menambahkan nomor ke akun."""
    res = await page.evaluate('''async (args) => {
        const { url, token, termId, requestToken, termTermId, count } = args;
        try {
            const resp = await window.jQuery.ajax({
                url: url,
                type: 'POST',
                data: {
                    _token: token,
                    termination_id: termId,
                    termination_term_id: termTermId,
                    count: count,
                    sort_type: 'random',
                    request_token: requestToken
                }
            });
            return { ok: true, data: resp };
        } catch(e) {
            let msg = 'Failed to add number';
            try {
                if (e.responseJSON && e.responseJSON.message) {
                    msg = e.responseJSON.message;
                }
            } catch(ex) {}
            return { ok: false, status: e.status, message: msg };
        }
    }''', {
        "url": cfg.get("k4", "https://augestel.com/Switchfy/client/numbers/request"),
        "token": cfg.get("k5"),
        "termId": term_data.get("id"),
        "requestToken": term_data.get("request_token"),
        "termTermId": term_data.get("terms", [{}])[0].get("id") if term_data.get("terms") else None,
        "count": count
    })
    return res


async def run_worker(worker_id: int, account_idx: int, account_email: str, page, queue: asyncio.Queue, shared_stats: dict, account_state: dict, stats_lock: asyncio.Lock, delay: int, max_add: int, batch_count: int = 250):
    """Worker task independen yang mengeksekusi penambahan nomor dari antrian."""
    while not queue.empty():
        async with stats_lock:
            # 1. Cek apakah batas 2.500 nomor akun ini sudah tercapai
            if account_state.get("limit_reached"):
                break
            curr_acc_total = account_state["current_total"] + account_state["added"]
            if curr_acc_total >= MAX_ACCOUNT_NUMBERS:
                account_state["limit_reached"] = True
                logger.warning(f"🛑 [Akun #{account_idx}] Batas maksimal {MAX_ACCOUNT_NUMBERS} nomor telah tercapai (Total: {curr_acc_total})! Menghentikan penambahan untuk akun ini.")
                break

            # 2. Cek apakah target max_add global telah tercapai
            if max_add > 0 and shared_stats["added"] >= max_add:
                break

            # Hitung jumlah nomor yang boleh diminta (jangan sampai melebihi 2.500 nomor akun)
            remaining_quota = MAX_ACCOUNT_NUMBERS - curr_acc_total
            req_count = min(batch_count, remaining_quota)
            if max_add > 0:
                req_count = min(req_count, max_add - shared_stats["added"])
            req_count = max(1, req_count)

            shared_stats["current_action"] += 1
            action_num = shared_stats["current_action"]

        try:
            row = await queue.get()
        except asyncio.QueueEmpty:
            break

        term_name = row.get("name", "")
        test_number = row.get("test_number", "")
        term_id = row.get("term_id", "")

        if not term_id:
            queue.task_done()
            continue

        logger.info(f"── [Worker #{worker_id} | Akun #{account_idx}] Action #{action_num} ──")
        logger.info(f"  📋 Range: {term_name} | 📱 Number: {test_number} | 🆔 ID: {term_id} | 🔢 Request: {req_count} nomor (Sisa kuota akun: {remaining_quota})")

        # Step 1: Ambil detail termination & request token
        info_res = await get_termination_details(page, term_id)
        if not info_res.get("ok"):
            logger.warning(f"  ❌ Gagal memuat info termination ID {term_id}: {info_res.get('error')}")
            async with stats_lock:
                shared_stats["failed"] += 1
            logger.info(f"  📊 Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}")
            queue.task_done()
            if delay > 0:
                await asyncio.sleep(min(delay, 5))
            continue

        d = info_res.get("data", {})
        cfg = info_res.get("cfg", {})
        terminations = d.get("terminations", [])

        if not terminations:
            logger.warning(f"  ⚠️ Tidak ada termination aktif pada ID {term_id}")
            async with stats_lock:
                shared_stats["skipped"] += 1
            queue.task_done()
            continue

        term = terminations[0]
        if term.get("no_numbers") is True:
            logger.info(f"  ⏭️ Nomor habis untuk {term_name}, dilewati.")
            async with stats_lock:
                shared_stats["skipped"] += 1
            logger.info(f"  📊 Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}")
            queue.task_done()
            continue

        limit_per_term = term.get("limit_per_termination")
        curr_from_term = term.get("current_from_termination", 0)
        if limit_per_term and int(curr_from_term) >= int(limit_per_term):
            logger.info(f"  ⏭️ Batas alokasi tercapai ({curr_from_term}/{limit_per_term}) untuk {term_name}, dilewati.")
            async with stats_lock:
                shared_stats["skipped"] += 1
            logger.info(f"  📊 Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}")
            queue.task_done()
            continue

        # Step 2: Request penambahan nomor
        add_res = await submit_add_number(page, term, cfg, count=req_count)
        if add_res.get("ok"):
            added_nums = add_res.get("data", {}).get("numbers", [])
            actual_added = len(added_nums) if added_nums else req_count
            num_preview = ", ".join(added_nums[:3]) + (f" ... (+{actual_added - 3} lainnya)" if actual_added > 3 else "") if added_nums else f"{actual_added} nomor"
            logger.info(f"  ✅ BERHASIL: {actual_added} nomor berhasil ditambahkan ({num_preview})!")
            async with stats_lock:
                account_state["added"] += actual_added
                shared_stats["added"] += actual_added
                tot_now = account_state["current_total"] + account_state["added"]
                logger.info(f"  📈 [Akun #{account_idx}] Total nomor akun sekarang: {tot_now} / {MAX_ACCOUNT_NUMBERS}")
                if tot_now >= MAX_ACCOUNT_NUMBERS:
                    account_state["limit_reached"] = True
                    logger.warning(f"🛑 [Akun #{account_idx}] Batas maksimal {MAX_ACCOUNT_NUMBERS} nomor telah tercapai! Menghentikan penambahan untuk akun ini dan lanjut ke akun berikutnya.")
                    while not queue.empty():
                        try:
                            queue.get_nowait()
                            queue.task_done()
                        except Exception:
                            break
        else:
            msg = add_res.get("message", "Gagal request")
            msg_lower = msg.lower()
            if "limit" in msg_lower or "maximum" in msg_lower or "reach" in msg_lower or "quota" in msg_lower or "not allowed" in msg_lower:
                logger.warning(f"  🛑 [Akun #{account_idx}] Portal Augestel menyatakan limit nomor tercapai: '{msg}'! Menghentikan penambahan pada akun ini dan lanjut ke akun berikutnya.")
                async with stats_lock:
                    shared_stats["skipped"] += 1
                    account_state["limit_reached"] = True
                    while not queue.empty():
                        try:
                            queue.get_nowait()
                            queue.task_done()
                        except Exception:
                            break
            else:
                logger.error(f"  ❌ GAGAL: {msg}")
                async with stats_lock:
                    shared_stats["failed"] += 1

        logger.info(f"  📊 Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}")
        queue.task_done()

        if delay > 0 and not queue.empty() and not account_state.get("limit_reached"):
            logger.info(f"  ⏳ [Worker #{worker_id}] Delay {delay}s sebelum action berikutnya...")
            await asyncio.sleep(delay)


async def process_account(account_idx: int, range_filter: str, max_add: int, delay: int, workers_count: int, batch_count: int, shared_stats: dict, stats_lock: asyncio.Lock):
    """Menjalankan proses auto-add pada satu akun Augestel."""
    acc_conf = get_account_config(account_idx)
    email = acc_conf["email"]
    password = acc_conf["password"]
    api_key = acc_conf.get("api_key", "")
    user_data_dir = acc_conf["user_data_dir"]

    logger.info("═" * 60)
    logger.info(f"🚀 Memulai Auto-Add Augestel untuk Akun #{account_idx}: {email}")
    logger.info(f"📂 Profile Browser: {user_data_dir}")
    logger.info(f"⚡ Parallel Workers: {workers_count}")
    logger.info("═" * 60)

    # ── Pengecekan Cepat: Apakah akun sudah mencapai batas 2.500 sebelum meluncurkan browser? ──
    init_count = await get_account_current_numbers_count(None, account_idx, api_key, email)
    if init_count >= MAX_ACCOUNT_NUMBERS:
        logger.warning(f"⚠️ [Akun #{account_idx} | {email}] Sudah memiliki {init_count}/{MAX_ACCOUNT_NUMBERS} nomor (Batas Maksimal Tercapai).")
        logger.warning(f"⏭️ Melewati Akun #{account_idx} dan otomatis lanjut ke akun berikutnya!")
        return

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
            logger.error(f"❌ Gagal meluncurkan browser untuk Akun #{account_idx}: {e}")
            return

        page = context.pages[0] if context.pages else await context.new_page()

        # Login check
        logged_in = await ensure_augestel_login(page, email, password)
        if not logged_in:
            logger.error(f"❌ Tidak dapat login ke akun #{account_idx} ({email}). Melewati akun ini.")
            await context.close()
            return

        # Double check jumlah nomor setelah login
        if init_count <= 0:
            init_count = await get_account_current_numbers_count(page, account_idx, api_key, email)
            if init_count >= MAX_ACCOUNT_NUMBERS:
                logger.warning(f"⚠️ [Akun #{account_idx} | {email}] Sudah memiliki {init_count}/{MAX_ACCOUNT_NUMBERS} nomor (Batas Maksimal Tercapai).")
                logger.warning(f"⏭️ Melewati Akun #{account_idx} dan otomatis lanjut ke akun berikutnya!")
                await context.close()
                return

        remaining_quota = MAX_ACCOUNT_NUMBERS - init_count
        logger.info(f"📊 [Akun #{account_idx} | {email}] Jumlah nomor saat ini: {init_count}/{MAX_ACCOUNT_NUMBERS} (Sisa kuota: {remaining_quota} nomor).")

        # Fetch terminations matching range_filter
        logger.info(f"🔍 Mencari terminations dengan filter: '{range_filter}'...")
        raw_rows = []
        page_size = 100
        start_idx = 0
        total_found = 0
        while True:
            dt_res = await fetch_test_terminations(page, range_filter, start=start_idx, length=page_size)
            if not dt_res or dt_res.get("error"):
                break
            total_found = dt_res.get("recordsFiltered", 0) or dt_res.get("recordsTotal", 0) or total_found
            chunk = dt_res.get("data", [])
            if not chunk:
                break
            raw_rows.extend(chunk)
            if max_add > 0 and len(raw_rows) >= max_add:
                raw_rows = raw_rows[:max_add]
                break
            start_idx += len(chunk)
            if start_idx >= total_found or len(chunk) < page_size:
                break

        logger.info(f"📋 Ditemukan {total_found} total records ({len(raw_rows)} diambil) untuk filter '{range_filter}'")

        if not raw_rows:
            logger.warning(f"⚠️ Tidak ada termination yang cocok dengan '{range_filter}'.")
            await context.close()
            return

        # Parse rows into actionable items
        queue = asyncio.Queue()
        for r in raw_rows:
            action_html = r.get("action", "")
            id_match = re.search(r'data-termination-id="(\d+)"', action_html)
            term_id = id_match.group(1) if id_match else None

            num_html = r.get("test_number", "")
            num_match = re.search(r'data-copy-number="([^"]+)"', num_html)
            num = num_match.group(1) if num_match else ""

            if term_id:
                queue.put_nowait({
                    "name": r.get("name", ""),
                    "test_number": num,
                    "term_id": term_id
                })

        q_size = queue.qsize()
        logger.info(f"📥 {q_size} terminations dimasukkan ke dalam antrian kerja.")

        # Persiapkan worker pages
        worker_pages = [page]
        for w_i in range(1, workers_count):
            try:
                new_p = await context.new_page()
                await new_p.goto("https://augestel.com/Switchfy/test/numbers", wait_until="domcontentloaded")
                worker_pages.append(new_p)
            except Exception as e:
                logger.warning(f"⚠️ Gagal membuat tab worker #{w_i + 1}: {e}")

        account_state = {
            "current_total": init_count,
            "added": 0,
            "limit_reached": False
        }

        # Jalankan parallel workers
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

        await asyncio.gather(*tasks)
        await context.close()

        # Update cache disk jika ada penambahan nomor
        if account_state["added"] > 0:
            final_acc_total = account_state["current_total"] + account_state["added"]
            try:
                cache_file = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{account_idx}.json")
                if os.path.exists(cache_file):
                    with open(cache_file, "r", encoding="utf-8") as f:
                        cd = json.load(f)
                    cd["total"] = final_acc_total
                    with open(cache_file, "w", encoding="utf-8") as f:
                        json.dump(cd, f, indent=2)
                agg_file = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")
                if os.path.exists(agg_file):
                    os.remove(agg_file)
            except Exception as ex_cache:
                logger.debug(f"Gagal update cache disk akun #{account_idx}: {ex_cache}")

        logger.info(f"🎉 Selesai memproses Akun #{account_idx} ({email}). Total ditambahkan pada akun ini: {account_state['added']} nomor (Total sekarang: {account_state['current_total'] + account_state['added']}).")


async def main():
    args = sys.argv[1:]
    range_filter = args[0] if len(args) > 0 else RANGE_NAME
    try:
        max_add = int(args[1]) if len(args) > 1 else MAX_ADD
    except Exception:
        max_add = MAX_ADD
    try:
        delay = int(args[2]) if len(args) > 2 else DELAY_SECONDS
    except Exception:
        delay = DELAY_SECONDS
    account_arg = str(args[3]).strip().lower() if len(args) > 3 else "1"
    try:
        workers = int(args[4]) if len(args) > 4 else 2
    except Exception:
        workers = 2
    try:
        batch_count = int(args[5]) if len(args) > 5 else BATCH_COUNT
    except Exception:
        batch_count = BATCH_COUNT

    # Load daftar akun
    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    all_accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                all_accounts = json.load(f)
        except Exception:
            pass

    if not all_accounts:
        all_accounts = [{"email": "default", "password": ""}]

    # Dukung multi-akun (contoh: "1,3,4" atau "all" atau "2")
    target_indices = []
    if account_arg == "all":
        target_indices = list(range(1, len(all_accounts) + 1))
    elif "," in account_arg:
        for x in account_arg.split(","):
            x = x.strip()
            if x.isdigit():
                val = int(x)
                if 1 <= val <= len(all_accounts) and val not in target_indices:
                    target_indices.append(val)
    else:
        try:
            val = int(account_arg)
            if 1 <= val <= len(all_accounts):
                target_indices = [val]
            else:
                target_indices = [1]
        except Exception:
            target_indices = [1]

    if not target_indices:
        target_indices = [1]

    logger.info("═" * 60)
    logger.info(f"🎯 Target akun terpilih: {', '.join([f'Akun #{i}' for i in target_indices])} ({len(target_indices)} akun)")
    logger.info(f"🔢 Maksimal nomor per akun: {MAX_ACCOUNT_NUMBERS} nomor (Otomatis skip / lanjut jika penuh)")
    logger.info("═" * 60)

    shared_stats = {
        "added": 0,
        "failed": 0,
        "skipped": 0,
        "current_action": 0
    }
    stats_lock = asyncio.Lock()

    for idx in target_indices:
        if max_add > 0 and shared_stats["added"] >= max_add:
            logger.info(f"🎯 Target max_add ({max_add}) telah tercapai!")
            break
        await process_account(idx, range_filter, max_add, delay, workers, batch_count, shared_stats, stats_lock)

    logger.info("═" * 60)
    logger.info("🏁 AUTO ADD AUGESTEL SELESAI!")
    logger.info(f"📊 Ringkasan: Added={shared_stats['added']} | Failed={shared_stats['failed']} | Skipped={shared_stats['skipped']}")
    logger.info("═" * 60)


if __name__ == "__main__":
    asyncio.run(main())
