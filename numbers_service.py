# ═══════════════════════════════════════════════════════════════
#  MY NUMBERS SERVICE - IVASMS Portal Numbers Manager
#  ─────────────────────────────────────────────────────────────
#  1. Deteksi total nomor di https://www.ivasms.com/portal/numbers
#  2. Ambil list nomor (Nomor, Range, Rate, Limit, dll)
#  3. Export ke format Excel (.xlsx) dan TXT (.txt)
# ═══════════════════════════════════════════════════════════════

import os
import sys
import re
import time
import json
import logging
import asyncio
from io import BytesIO
from datetime import datetime
from playwright.async_api import async_playwright

import config

logger = logging.getLogger("numbers_service")

# Cache singkat agar tidak spam browser bila user sering refresh
_NUMBERS_CACHE = {}


def get_accounts():
    """Ambil daftar akun IVASMS terdaftar."""
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
            if config.IVASMS_EMAIL:
                accounts.append({"email": config.IVASMS_EMAIL, "password": config.IVASMS_PASSWORD})
            if getattr(config, "IVASMS_EMAIL_2", ""):
                accounts.append({"email": config.IVASMS_EMAIL_2, "password": config.IVASMS_PASSWORD_2})
        except Exception:
            pass

    return accounts


def get_augestel_accounts():
    """Ambil daftar akun Augestel terdaftar."""
    acc_file = os.path.join(os.path.dirname(__file__), "augestel_accounts.json")
    accounts = []
    if os.path.exists(acc_file):
        try:
            with open(acc_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            pass

    if not accounts:
        cfg = getattr(config, "__dict__", {})
        if cfg.get("AUGESTEL_EMAIL"):
            accounts.append({
                "email": cfg.get("AUGESTEL_EMAIL", "saputradimas0878@gmail.com"),
                "api_key": cfg.get("AUGESTEL_API_KEY", "")
            })

    return accounts


async def auto_login_if_needed(page, email: str, password: str) -> bool:
    """Auto-login jika terlempar ke halaman /login."""
    if "/login" not in page.url:
        has_login = await page.query_selector("input[name='email']")
        if not has_login:
            return True

    logger.info(f"🔑 Session expired, auto-login untuk {email}...")
    try:
        await page.fill("input[name='email']", email)
        await page.fill("input[name='password']", password)
        rem = await page.query_selector("input[name='remember']")
        if rem and not await rem.is_checked():
            await rem.check()

        await asyncio.sleep(1)
        sub = await page.query_selector("button[type='submit']")
        if sub:
            await sub.click()
        else:
            await page.keyboard.press("Enter")

        for _ in range(15):
            await asyncio.sleep(1)
            if "/portal" in page.url:
                logger.info("🎉 Auto-login berhasil!")
                return True
        return False
    except Exception as e:
        logger.error(f"Error auto-login: {e}")
        return False


async def wait_cloudflare(page, max_wait=30) -> bool:
    for _ in range(max_wait):
        title = await page.title()
        if "Just a moment" not in title:
            return True
        await asyncio.sleep(1)
    return False


async def fetch_all_accounts_numbers(force_refresh: bool = False, max_rows: int = 5000) -> dict:
    """Fetch semua nomor dari seluruh akun IVASMS yang terdaftar."""
    accounts = get_accounts()
    if not accounts:
        return {"success": False, "message": "Belum ada akun IVASMS yang terdaftar!"}

    cache_key = "all"
    now_ts = datetime.now()
    if not force_refresh and cache_key in _NUMBERS_CACHE:
        cached = _NUMBERS_CACHE[cache_key]
        cached_dt = datetime.strptime(cached["cached_at"], "%Y-%m-%d %H:%M:%S")
        if (now_ts - cached_dt).total_seconds() < 90:
            return cached

    all_numbers = []
    breakdown = []
    total_records = 0

    for idx, acc in enumerate(accounts, 1):
        try:
            res = await fetch_account_numbers(account_index=idx, force_refresh=force_refresh, max_rows=max_rows)
            if res.get("success"):
                acc_email = res.get("email", acc.get("email", f"Akun #{idx}"))
                acc_total = res.get("total", 0)
                acc_numbers = res.get("numbers", [])
                total_records += acc_total

                for num_item in acc_numbers:
                    tagged_item = dict(num_item)
                    tagged_item["account_index"] = idx
                    tagged_item["account_email"] = acc_email
                    all_numbers.append(tagged_item)

                breakdown.append({
                    "account_index": idx,
                    "email": acc_email,
                    "total": acc_total,
                    "count": len(acc_numbers)
                })
            else:
                breakdown.append({
                    "account_index": idx,
                    "email": acc.get("email", f"Akun #{idx}"),
                    "total": 0,
                    "count": 0,
                    "error": res.get("message", "Gagal")
                })
        except Exception as e:
            logger.error(f"Error fetching numbers for account {idx}: {e}")
            breakdown.append({
                "account_index": idx,
                "email": acc.get("email", f"Akun #{idx}"),
                "total": 0,
                "count": 0,
                "error": str(e)
            })

    result = {
        "success": True,
        "account_index": "all",
        "email": f"Semua Akun ({len(accounts)} Akun)",
        "total": total_records,
        "count": len(all_numbers),
        "numbers": all_numbers,
        "accounts_breakdown": breakdown,
        "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
    }

    _NUMBERS_CACHE[cache_key] = result
    return result


def _format_augestel_number_item(item: dict, idx: int, target_idx: int, email: str) -> dict:
    """Format single Augestel number item standardly."""
    num = str(item.get("number") or item.get("Number") or "").strip()
    rng = item.get("range_name") or item.get("range") or "Augestel"
    rate_raw = item.get("a2p_rate") if item.get("a2p_rate") is not None else item.get("A2P")
    if isinstance(rate_raw, (int, float)):
        rate_str = f"${rate_raw:.4f}"
    elif rate_raw:
        rate_str = str(rate_raw)
        if not rate_str.startswith("$"):
            try:
                rate_str = f"${float(rate_str):.4f}"
            except Exception:
                pass
    else:
        rate_str = "$0.0000"

    limit_val = item.get("portal_limit_a2p") if item.get("portal_limit_a2p") is not None else item.get("limit_a2p", 10000)

    return {
        "id": str(idx),
        "number": num,
        "range": rng,
        "rate": rate_str,
        "limit_range": str(limit_val or 10000),
        "sid_limit": "-",
        "sid_did_limit": "-",
        "account_index": f"aug_{target_idx}",
        "account_email": email,
    }


async def fetch_augestel_account_numbers(account_param: str = "augestel", force_refresh: bool = False, max_rows: int = 50000) -> dict:
    """Fetch numbers untuk akun Augestel (semua akun atau akun tertentu)."""
    accounts = get_augestel_accounts()
    if not accounts:
        return {"success": False, "message": "Belum ada akun Augestel yang terdaftar!"}

    acc_str = str(account_param).strip().lower()
    is_all = acc_str in ["augestel", "augestel_all", "aug_all", "all"]

    target_idx = None
    if not is_all:
        clean_num = re.sub(r'[^0-9]', '', acc_str)
        if clean_num:
            target_idx = int(clean_num)
        else:
            is_all = True

    from augestel_client import AugestelClient
    now_ts = datetime.now()

    # ──────────────────────────────────────────
    # 1. SINGLE ACCOUNT FETCH
    # ──────────────────────────────────────────
    if not is_all and target_idx and 1 <= target_idx <= len(accounts):
        acc = accounts[target_idx - 1]
        email = acc.get("email", "")
        api_key = acc.get("api_key", "")
        cache_key = f"augestel_{target_idx}"
        disk_cache_path = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{target_idx}.json")

        disk_data = None
        if os.path.exists(disk_cache_path):
            try:
                with open(disk_cache_path, "r", encoding="utf-8") as f:
                    disk_data = json.load(f)
            except Exception:
                pass

        # In-memory check (5 minutes TTL)
        if not force_refresh and cache_key in _NUMBERS_CACHE:
            cached = _NUMBERS_CACHE[cache_key]
            try:
                cached_dt = datetime.strptime(cached["cached_at"], "%Y-%m-%d %H:%M:%S")
                if (now_ts - cached_dt).total_seconds() < 300 and len(cached.get("numbers", [])) >= cached.get("total", 0):
                    return cached
            except Exception:
                pass

        # Disk cache check (5 minutes TTL)
        if not force_refresh and disk_data:
            try:
                cached_dt = datetime.strptime(disk_data["cached_at"], "%Y-%m-%d %H:%M:%S")
                if (now_ts - cached_dt).total_seconds() < 300 and len(disk_data.get("numbers", [])) >= disk_data.get("total", 0):
                    _NUMBERS_CACHE[cache_key] = disk_data
                    return disk_data
            except Exception:
                pass

        if not api_key:
            return {"success": False, "message": f"Akun Augestel #{target_idx} ({email}) belum memiliki API Key!"}

        try:
            client = AugestelClient(api_key=api_key, email=email)
            # 1 single request to get exact portal total & first 100 items instantly
            res_p1 = client.get_numbers(page=1, per_page=100)

            if not res_p1.get("success"):
                # Fallback to disk cache if rate-limited or transient network error
                if disk_data and disk_data.get("numbers") is not None:
                    _NUMBERS_CACHE[cache_key] = disk_data
                    return disk_data
                return {"success": False, "message": f"Gagal menghubungi API Augestel #{target_idx}: {res_p1.get('message', 'Error')}"}

            portal_total = res_p1.get("pagination", {}).get("total", len(res_p1.get("data", [])))
            raw_items = res_p1.get("data", [])

            formatted_numbers = []
            if portal_total == 0:
                formatted_numbers = []
            elif portal_total <= 100 or len(raw_items) >= portal_total:
                # All items fit in page 1
                for idx, item in enumerate(raw_items, 1):
                    formatted_numbers.append(_format_augestel_number_item(item, idx, target_idx, email))
            else:
                # Total > 100 (e.g. 1250 or 250).
                # Check if disk cache already has all items matching portal_total
                if disk_data and len(disk_data.get("numbers", [])) == portal_total:
                    formatted_numbers = disk_data.get("numbers", [])
                elif disk_data and len(disk_data.get("numbers", [])) > 0:
                    formatted_numbers = disk_data.get("numbers", [])
                else:
                    for idx, item in enumerate(raw_items, 1):
                        formatted_numbers.append(_format_augestel_number_item(item, idx, target_idx, email))

            result = {
                "success": True,
                "account_index": f"aug_{target_idx}",
                "email": f"Augestel #{target_idx} ({email})",
                "total": portal_total,
                "count": len(formatted_numbers),
                "numbers": formatted_numbers,
                "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
            }
            _NUMBERS_CACHE[cache_key] = result
            try:
                with open(disk_cache_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2)
            except Exception:
                pass
            return result
        except Exception as e:
            if disk_data:
                return disk_data
            return {"success": False, "message": f"Gagal fetch Augestel #{target_idx}: {e}"}

    # ──────────────────────────────────────────
    # 2. ALL AUGESTEL ACCOUNTS FETCH
    # ──────────────────────────────────────────
    cache_key = "augestel_all"
    disk_cache_path = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")

    # In-memory check (5 minutes TTL, verify total is not stale 500)
    if not force_refresh and cache_key in _NUMBERS_CACHE:
        cached = _NUMBERS_CACHE[cache_key]
        try:
            cached_dt = datetime.strptime(cached["cached_at"], "%Y-%m-%d %H:%M:%S")
            if (now_ts - cached_dt).total_seconds() < 300 and cached.get("total", 0) > 500:
                return cached
        except Exception:
            pass

    # Disk cache check (5 minutes TTL, verify total is not stale 500)
    if not force_refresh and os.path.exists(disk_cache_path):
        try:
            with open(disk_cache_path, "r", encoding="utf-8") as f:
                disk_data = json.load(f)
                cached_dt = datetime.strptime(disk_data["cached_at"], "%Y-%m-%d %H:%M:%S")
                if (now_ts - cached_dt).total_seconds() < 300 and disk_data.get("total", 0) > 500:
                    _NUMBERS_CACHE[cache_key] = disk_data
                    return disk_data
        except Exception:
            pass

    # Fetch aggregate across all registered accounts with API key
    all_combined = []
    breakdown = []
    total_portal_sum = 0

    for i, acc in enumerate(accounts, 1):
        em = acc.get("email", "")
        key = acc.get("api_key", "")
        if not key:
            continue
        try:
            sub_res = await fetch_augestel_account_numbers(account_param=f"augestel_{i}", force_refresh=force_refresh, max_rows=max_rows)
            sub_nums = []
            sub_tot = 0
            if sub_res.get("success"):
                sub_nums = sub_res.get("numbers", [])
                sub_tot = sub_res.get("total", len(sub_nums))
            else:
                # Fallback to disk cache for this account
                indiv_cache = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{i}.json")
                if os.path.exists(indiv_cache):
                    try:
                        with open(indiv_cache, "r", encoding="utf-8") as f:
                            d = json.load(f)
                            sub_nums = d.get("numbers", [])
                            sub_tot = d.get("total", len(sub_nums))
                    except Exception:
                        pass

            total_portal_sum += sub_tot
            for item in sub_nums:
                item_copy = dict(item)
                item_copy["account_index"] = f"aug_{i}"
                item_copy["account_email"] = em
                all_combined.append(item_copy)

            breakdown.append({
                "account_index": i,
                "email": em,
                "total": sub_tot
            })
        except Exception as e:
            logger.error(f"Error fetching Augestel #{i}: {e}")

    for idx, item in enumerate(all_combined, 1):
        item["id"] = str(idx)

    result = {
        "success": True,
        "account_index": "augestel_all",
        "email": f"Semua Akun Augestel ({len(breakdown)} Akun Aktif)",
        "total": total_portal_sum or len(all_combined),
        "count": len(all_combined),
        "numbers": all_combined,
        "accounts_breakdown": breakdown,
        "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
    }
    _NUMBERS_CACHE[cache_key] = result
    try:
        with open(disk_cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
    except Exception:
        pass
    return result


async def fetch_account_numbers(account_index = 1, force_refresh: bool = False, max_rows: int = 5000) -> dict:
    """
    Fetch semua nomor dari https://www.ivasms.com/portal/numbers untuk akun tertentu,
    atau 'all' untuk semua akun IVASMS, atau 'augestel' / 'augestel_all' untuk portal Augestel.
    """
    acc_str = str(account_index).strip().lower()
    if acc_str == "all":
        return await fetch_all_accounts_numbers(force_refresh=force_refresh, max_rows=max_rows)

    if acc_str.startswith("aug"):
        return await fetch_augestel_account_numbers(account_param=acc_str, force_refresh=force_refresh, max_rows=max_rows)

    try:
        account_index = int(account_index)
    except Exception:
        account_index = 1

    accounts = get_accounts()
    if not accounts:
        return {"success": False, "message": "Belum ada akun IVASMS yang terdaftar!"}

    if account_index < 1 or account_index > len(accounts):
        account_index = 1

    acc = accounts[account_index - 1]
    email = acc.get("email", "")
    password = acc.get("password", "")

    # Cek cache (valid selama 60 detik kecuali force_refresh)
    cache_key = f"acc_{account_index}"
    now_ts = datetime.now()
    if not force_refresh and cache_key in _NUMBERS_CACHE:
        cached = _NUMBERS_CACHE[cache_key]
        cached_dt = datetime.strptime(cached["cached_at"], "%Y-%m-%d %H:%M:%S")
        if (now_ts - cached_dt).total_seconds() < 90:
            return cached

    if account_index == 1:
        user_data_dir = os.path.abspath("browser_profile")
    else:
        user_data_dir = os.path.abspath(f"browser_profile_acc{account_index}")

    logger.info(f"🔍 Mengambil data nomor untuk Akun #{account_index} ({email})...")

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
        except Exception as e:
            logger.error(f"Gagal launch browser: {e}")
            return {"success": False, "message": f"Browser gagal dibuka: {e}"}

        page = context.pages[0] if context.pages else await context.new_page()

        try:
            await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
            if not await wait_cloudflare(page, 30):
                await context.close()
                return {"success": False, "message": "Cloudflare challenge timeout!"}

            await asyncio.sleep(2)
            if not await auto_login_if_needed(page, email, password):
                await context.close()
                return {"success": False, "message": "Gagal login ke akun IVASMS!"}

            if "/portal/numbers" not in page.url:
                await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
                await wait_cloudflare(page, 15)
                await asyncio.sleep(2)

            # Ambil total records dan data via DataTable internal fetch
            fetch_js = """
            async ([start, length]) => {
                try {
                    const url = new URL('/portal/numbers', window.location.origin);
                    url.searchParams.set('draw', '1');
                    url.searchParams.set('start', start.toString());
                    url.searchParams.set('length', length.toString());

                    const cols = [
                        { data: 'number_id', name: 'id', searchable: true, orderable: false },
                        { data: 'Number', name: 'Number', searchable: true, orderable: true },
                        { data: 'range', name: 'range', searchable: true, orderable: true },
                        { data: 'A2P', name: 'A2P', searchable: true, orderable: true },
                        { data: 'LimitA2P', name: 'LimitA2P', searchable: true, orderable: true },
                        { data: 'limit_cli_a2p', name: 'limit_cli_a2p', searchable: true, orderable: true },
                        { data: 'limit_cli_did_a2p', name: 'limit_cli_did_a2p', searchable: true, orderable: true },
                        { data: 'action', name: 'action', searchable: false, orderable: false }
                    ];

                    cols.forEach((col, idx) => {
                        url.searchParams.set(`columns[${idx}][data]`, col.data);
                        url.searchParams.set(`columns[${idx}][name]`, col.name);
                        url.searchParams.set(`columns[${idx}][searchable]`, col.searchable ? 'true' : 'false');
                        url.searchParams.set(`columns[${idx}][orderable]`, col.orderable ? 'true' : 'false');
                        url.searchParams.set(`columns[${idx}][search][value]`, '');
                        url.searchParams.set(`columns[${idx}][search][regex]`, 'false');
                    });

                    url.searchParams.set('order[0][column]', '1');
                    url.searchParams.set('order[0][dir]', 'desc');
                    url.searchParams.set('search[value]', '');
                    url.searchParams.set('search[regex]', 'false');

                    const resp = await fetch(url.toString(), {
                        method: 'GET',
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest',
                            'Accept': 'application/json, text/javascript, */*; q=0.01'
                        }
                    });
                    return await resp.json();
                } catch(e) {
                    return { error: e.message };
                }
            }
            """

            # 1. Fetch batch pertama (ambil 1000 atau total)
            first_batch = await page.evaluate(fetch_js, [0, 1000])
            if "error" in first_batch and first_batch["error"]:
                await context.close()
                return {"success": False, "message": f"DataTable API Error: {first_batch['error']}"}

            total_records = first_batch.get("recordsFiltered", 0) or first_batch.get("recordsTotal", 0)
            raw_rows = first_batch.get("data", [])

            # Jika total records > 1000, fetch sisa batch berikutnya
            if total_records > 1000 and len(raw_rows) < max_rows:
                current_start = 1000
                while current_start < total_records and len(raw_rows) < max_rows:
                    batch_len = min(1000, max_rows - len(raw_rows))
                    sub_batch = await page.evaluate(fetch_js, [current_start, batch_len])
                    sub_rows = sub_batch.get("data", [])
                    if not sub_rows:
                        break
                    raw_rows.extend(sub_rows)
                    current_start += batch_len

            await context.close()

            # Bersihkan dan standarisasi data baris
            clean_numbers = []
            for item in raw_rows:
                num_val = str(item.get("Number", "")).strip()
                if not num_val:
                    continue

                # Parse id dari number_id html checkbox
                raw_id_html = str(item.get("number_id", ""))
                import re
                m_id = re.search(r'value="(\d+)"', raw_id_html)
                clean_id = m_id.group(1) if m_id else ""

                clean_numbers.append({
                    "account_index": account_index,
                    "account_email": email,
                    "id": clean_id,
                    "number": num_val,
                    "range": str(item.get("range", "")).strip(),
                    "rate": str(item.get("A2P", "")).strip(),
                    "limit_range": str(item.get("LimitA2P", "")).strip(),
                    "sid_limit": str(item.get("limit_cli_a2p", "")).strip(),
                    "sid_did_limit": str(item.get("limit_cli_did_a2p", "")).strip(),
                })

            result = {
                "success": True,
                "account_index": account_index,
                "email": email,
                "total": total_records,
                "count": len(clean_numbers),
                "numbers": clean_numbers,
                "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
            }

            _NUMBERS_CACHE[cache_key] = result
            return result

        except Exception as e:
            logger.error(f"Error fetching numbers: {e}")
            try:
                await context.close()
            except Exception:
                pass
            return {"success": False, "message": str(e)}


def generate_numbers_excel(numbers_data: list, email: str = "") -> BytesIO:
    """Export daftar nomor ke file Excel .xlsx menggunakan openpyxl."""
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "IVASMS Numbers"

    # Styling header
    header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    data_font = Font(name="Calibri", size=11)
    center_align = Alignment(horizontal="center", vertical="center")
    left_align = Alignment(horizontal="left", vertical="center")
    thin_border = Border(
        left=Side(style='thin', color='E2E8F0'),
        right=Side(style='thin', color='E2E8F0'),
        top=Side(style='thin', color='E2E8F0'),
        bottom=Side(style='thin', color='E2E8F0')
    )

    is_all_accounts = any(item.get("account_email") for item in numbers_data) and ("Semua Akun" in str(email) or len(set(item.get("account_index", 1) for item in numbers_data)) > 1)

    if is_all_accounts:
        headers = [
            "No",
            "Account",
            "Phone Number",
            "Range Name",
            "Rate (A2P)",
            "Limit by Range",
            "SID/Range Limit",
            "SID→DID Limit",
            "Number ID"
        ]
    else:
        headers = [
            "No",
            "Phone Number",
            "Range Name",
            "Rate (A2P)",
            "Limit by Range",
            "SID/Range Limit",
            "SID→DID Limit",
            "Number ID"
        ]

    ws.append(headers)

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center_align

    for idx, item in enumerate(numbers_data, 1):
        if is_all_accounts:
            acc_label = f"Akun #{item.get('account_index', '')} ({item.get('account_email', '')})" if item.get('account_email') else f"Akun #{item.get('account_index', '')}"
            row = [
                idx,
                acc_label,
                str(item.get("number", "")),
                str(item.get("range", "")),
                str(item.get("rate", "")),
                str(item.get("limit_range", "")),
                str(item.get("sid_limit", "")),
                str(item.get("sid_did_limit", "")),
                str(item.get("id", ""))
            ]
        else:
            row = [
                idx,
                str(item.get("number", "")),
                str(item.get("range", "")),
                str(item.get("rate", "")),
                str(item.get("limit_range", "")),
                str(item.get("sid_limit", "")),
                str(item.get("sid_did_limit", "")),
                str(item.get("id", ""))
            ]

        ws.append(row)
        curr_row = idx + 1
        for c_idx in range(1, len(headers) + 1):
            c = ws.cell(row=curr_row, column=c_idx)
            c.font = data_font
            c.border = thin_border
            if is_all_accounts:
                if c_idx in [1, 5, 6, 7, 8, 9]:
                    c.alignment = center_align
                else:
                    c.alignment = left_align
            else:
                if c_idx in [1, 4, 5, 6, 7, 8]:
                    c.alignment = center_align
                else:
                    c.alignment = left_align

    # Auto adjust column width
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

    buf = BytesIO()
    wb.save(buf)
    buf.seek(0)
    return buf


def generate_numbers_txt(numbers_data: list) -> str:
    """Export daftar nomor ke plain text (hanya deretan nomor per baris)."""
    lines = [str(item.get("number", "")).strip() for item in numbers_data if str(item.get("number", "")).strip()]
    return "\n".join(lines)


async def return_all_augestel_portal(account_idx: int) -> dict:
    """Melakukan bulk-return-all pada portal Augestel untuk akun terpilih via browser session."""
    accs = get_augestel_accounts()
    if not accs or account_idx < 1 or account_idx > len(accs):
        return {"success": False, "message": f"Akun Augestel #{account_idx} tidak ditemukan!"}

    acc = accs[account_idx - 1]
    email = acc.get("email", "")
    pwd = acc.get("password", "")
    user_data_dir = os.path.abspath(f"browser_profile_augestel_{account_idx}")

    logger.info(f"🗑️ Menjalankan Return All Numbers Augestel untuk Akun #{account_idx} ({email})...")

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
        except Exception as e:
            return {"success": False, "message": f"Browser gagal dibuka: {e}"}

        page = context.pages[0] if context.pages else await context.new_page()

        try:
            await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="networkidle", timeout=45000)
            await asyncio.sleep(1.5)

            # 1. Cek apakah portal sedang dalam cooldown rate-limit
            wait_el = await page.query_selector(".wait")
            page_title = await page.title()
            if wait_el or "too quick" in page_title.lower() or "one moment" in page_title.lower():
                wait_sec = (await wait_el.inner_text()).strip() if wait_el else "beberapa"
                await context.close()
                return {
                    "success": False,
                    "message": f"Portal Augestel sedang dalam masa jeda keamanan/cooldown anti-spam ({wait_sec} detik lagi). Harap tunggu hingga countdown selesai sebelum melakukan return nomor."
                }

            # 2. Auto-login jika sesi expired atau terlempar ke halaman login
            login_input = await page.query_selector("#loginEmail, input[name='email']")
            if login_input or "/client/numbers" not in page.url:
                if "/Switchfy" in page.url or login_input:
                    logger.info(f"🔑 Session belum aktif untuk Akun #{account_idx} ({email}), melakukan auto-login...")
                    if not login_input:
                        await page.goto("https://augestel.com/Switchfy", wait_until="networkidle", timeout=45000)
                        await asyncio.sleep(1)
                        login_input = await page.query_selector("#loginEmail, input[name='email']")

                    if login_input:
                        await page.fill("#loginEmail, input[name='email']", email)
                        await page.fill("#loginPassword, input[name='password']", pwd)
                        try:
                            await page.evaluate("() => { const el = document.querySelector(\"input[name='remember']\"); if (el) { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); } }")
                        except Exception:
                            pass
                        await asyncio.sleep(0.5)

                        btn = await page.query_selector("#loginSubmit, button[type='submit']")
                        if btn:
                            await btn.click()
                        else:
                            await page.keyboard.press("Enter")

                        # Tunggu hingga login berhasil dialihkan ke dashboard/client panel
                        logged_in = False
                        for _ in range(20):
                            await asyncio.sleep(1)
                            # Cek jika muncul cooldown setelah submit
                            wait_el_sub = await page.query_selector(".wait")
                            if wait_el_sub:
                                wait_sec = (await wait_el_sub.inner_text()).strip()
                                await context.close()
                                return {
                                    "success": False,
                                    "message": f"Portal Augestel sedang dalam masa jeda keamanan/cooldown anti-spam ({wait_sec} detik lagi). Harap tunggu hingga countdown selesai sebelum melakukan return nomor."
                                }
                            u = page.url
                            if "/client/" in u or "/test/" in u or "/dashboard" in u:
                                logged_in = True
                                break

                        if not logged_in and (await page.query_selector("#loginEmail, input[name='email']")):
                            await context.close()
                            return {
                                "success": False,
                                "message": f"Gagal login ke Akun Augestel #{account_idx} ({email}). Kredensial tidak valid atau Cloudflare challenge aktif."
                            }

                # Navigasi ke halaman numbers setelah login
                if "/client/numbers" not in page.url:
                    await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="networkidle", timeout=45000)
                    await asyncio.sleep(2)

            # Cek cooldown lagi jika muncul di halaman numbers
            wait_el = await page.query_selector(".wait")
            if wait_el:
                wait_sec = (await wait_el.inner_text()).strip()
                await context.close()
                return {
                    "success": False,
                    "message": f"Portal Augestel sedang dalam masa jeda keamanan/cooldown anti-spam ({wait_sec} detik lagi). Harap tunggu hingga countdown selesai sebelum melakukan return nomor."
                }

            # 3. Cari tombol Return All
            try:
                btn = await page.wait_for_selector("#bulkReturnAllBtn", timeout=6000)
            except Exception:
                btn = None

            res_message = ""
            success = False

            if btn and await btn.is_visible():
                await btn.click()
                try:
                    confirm_btn = await page.wait_for_selector("button.swal2-confirm", timeout=5000)
                except Exception:
                    confirm_btn = None

                if confirm_btn and await confirm_btn.is_visible():
                    try:
                        async with page.expect_response(lambda r: "bulk-return" in r.url, timeout=25000) as resp_info:
                            await confirm_btn.click()
                        resp = await resp_info.value
                        try:
                            resp_json = await resp.json()
                            success = resp_json.get("success", resp.status == 200)
                            res_message = resp_json.get("message", "Semua nomor berhasil dikembalikan!")
                            if "no active numbers" in str(res_message).lower():
                                success = True
                                res_message = "Tidak ada nomor aktif yang perlu di-return (akun sudah bersih/kosong)."
                        except Exception:
                            res_text = await resp.text()
                            success = resp.status == 200
                            res_message = res_text[:150]
                            if "no active numbers" in str(res_message).lower():
                                success = True
                                res_message = "Tidak ada nomor aktif yang perlu di-return (akun sudah bersih/kosong)."
                    except Exception as e_resp:
                        res_message = f"Timeout respon portal return all: {e_resp}"
                else:
                    res_message = "Tombol konfirmasi Swal tidak muncul."
            else:
                # Cek jika tabel kosong
                empty_el = await page.query_selector(".dataTables_empty")
                if empty_el:
                    success = True
                    res_message = "Tidak ada nomor aktif pada akun ini (tabel kosong)."
                else:
                    curr_title = await page.title()
                    res_message = f"Tombol Return All tidak tersedia di portal (Title: '{curr_title}', URL: '{page.url}')."

            await context.close()

            # Bersihkan cache akun ini
            _NUMBERS_CACHE.pop(f"augestel_{account_idx}", None)
            _NUMBERS_CACHE.pop("augestel_all", None)
            cache_file = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{account_idx}.json")
            if os.path.exists(cache_file):
                try:
                    os.remove(cache_file)
                except Exception:
                    pass
            all_cache = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")
            if os.path.exists(all_cache):
                try:
                    os.remove(all_cache)
                except Exception:
                    pass

            if success:
                return {"success": True, "message": f"Berhasil return/hapus nomor Akun Augestel #{account_idx} ({email}): {res_message}"}
            else:
                return {"success": False, "message": f"Gagal return nomor Akun Augestel #{account_idx} ({email}): {res_message}"}

        except Exception as e:
            try:
                await context.close()
            except Exception:
                pass
            return {"success": False, "message": f"Error eksekusi return all Augestel #{account_idx}: {e}"}


async def _delete_ivasms_single_account(acc_idx: int, acc: dict) -> dict:
    """Helper eksekusi delete all numbers untuk 1 akun IVASMS."""
    email = acc.get("email", "")
    password = acc.get("password", "")
    user_data_dir = os.path.abspath("browser_profile") if acc_idx == 1 else os.path.abspath(f"browser_profile_acc{acc_idx}")

    logger.info(f"🗑️ Menjalankan Delete All Numbers untuk Akun IVASMS #{acc_idx} ({email})...")

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
        except Exception as e:
            return {"success": False, "message": f"Browser gagal dibuka: {e}"}

        page = context.pages[0] if context.pages else await context.new_page()

        try:
            await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
            await wait_cloudflare(page, 25)
            await auto_login_if_needed(page, email, password)

            if "/portal/numbers" not in page.url:
                await page.goto("https://www.ivasms.com/portal/numbers", wait_until="domcontentloaded", timeout=45000)
                await wait_cloudflare(page, 15)

            # Eksekusi return all numbers via API endpoint internal IVASMS
            res = await page.evaluate("""
                async () => {
                    try {
                        const tokenEl = document.querySelector('meta[name="csrf-token"]') || document.querySelector('input[name="_token"]');
                        const token = tokenEl ? (tokenEl.content || tokenEl.value) : '';
                        
                        const resp = await fetch('https://www.ivasms.com/portal/numbers/return/allnumber/bluck', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-CSRF-TOKEN': token,
                                'Accept': 'application/json, text/javascript, */*; q=0.01'
                            },
                            body: '_token=' + encodeURIComponent(token)
                        });
                        
                        const status = resp.status;
                        let json = {};
                        try { json = await resp.json(); } catch(e) { json = { text: await resp.text() }; }
                        return { status, success: status >= 200 && status < 300, data: json };
                    } catch(err) {
                        return { status: 0, success: false, error: err.message };
                    }
                }
            """)

            await context.close()

            # Bersihkan cache
            _NUMBERS_CACHE.pop(f"acc_{acc_idx}", None)
            _NUMBERS_CACHE.pop("all", None)

            if res.get("success"):
                return {"success": True, "message": f"Berhasil menghapus/return semua nomor pada Akun #{acc_idx} ({email})!"}
            else:
                msg = res.get("data", {}).get("message") or res.get("error") or f"HTTP {res.get('status')}"
                return {"success": False, "message": f"Gagal return nomor: {msg}"}

        except Exception as e:
            try:
                await context.close()
            except Exception:
                pass
            return {"success": False, "message": f"Error eksekusi return all: {e}"}


async def delete_all_account_numbers(account_index=1) -> dict:
    """
    Menghapus/mengembalikan semua nomor ke sistem (Return All Numbers).
    Mendukung akun IVASMS (via /portal/numbers/return/allnumber/bluck)
    dan Augestel (via /Switchfy/client/numbers/bulk-return-all).
    """
    acc_str = str(account_index).strip().lower()

    if acc_str.startswith("aug"):
        aug_accounts = get_augestel_accounts()
        if not aug_accounts:
            return {"success": False, "message": "Tidak ada akun Augestel terdaftar!"}

        if "all" in acc_str:
            # Hapus semua akun Augestel secara paralel terkontrol (Semaphore 2)
            sem = asyncio.Semaphore(2)

            async def _worker(idx):
                async with sem:
                    return await return_all_augestel_portal(idx)

            tasks = [_worker(i) for i in range(1, len(aug_accounts) + 1)]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            succ = 0
            details = []
            for i, r in enumerate(results, 1):
                if isinstance(r, dict) and r.get("success"):
                    succ += 1
                    details.append(f"Akun #{i}: OK")
                elif isinstance(r, dict):
                    details.append(f"Akun #{i}: {r.get('message', 'Gagal')}")
                else:
                    details.append(f"Akun #{i}: Error")

            # Pastikan semua cache Augestel dibersihkan
            _NUMBERS_CACHE.clear()
            for i in range(1, len(aug_accounts) + 1):
                f_path = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{i}.json")
                if os.path.exists(f_path):
                    try:
                        os.remove(f_path)
                    except Exception:
                        pass
            all_path = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")
            if os.path.exists(all_path):
                try:
                    os.remove(all_path)
                except Exception:
                    pass

            return {
                "success": succ > 0,
                "message": f"Selesai return all nomor untuk {succ}/{len(aug_accounts)} akun Augestel! ({', '.join(details)})"
            }
        else:
            # Single account
            clean_idx = re.sub(r"[^\d]", "", acc_str)
            target_idx = int(clean_idx) if clean_idx else 1
            return await return_all_augestel_portal(target_idx)

    # IVASMS accounts
    accounts = get_accounts()
    if not accounts:
        return {"success": False, "message": "Tidak ada akun IVASMS terdaftar!"}

    if acc_str == "all":
        succ = 0
        details = []
        for i in range(1, len(accounts) + 1):
            r = await _delete_ivasms_single_account(i, accounts[i - 1])
            if r.get("success"):
                succ += 1
                details.append(f"Akun #{i}: OK")
            else:
                details.append(f"Akun #{i}: {r.get('message', 'Gagal')}")
        return {
            "success": succ > 0,
            "message": f"Selesai hapus nomor untuk {succ}/{len(accounts)} akun IVASMS! ({', '.join(details)})"
        }

    try:
        acc_idx = int(account_index)
    except Exception:
        acc_idx = 1

    if acc_idx < 1 or acc_idx > len(accounts):
        return {"success": False, "message": f"Akun #{acc_idx} tidak ditemukan!"}

    return await _delete_ivasms_single_account(acc_idx, accounts[acc_idx - 1])
