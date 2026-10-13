# ═══════════════════════════════════════════════════════════════
#  MY NUMBERS SERVICE - IVASMS Portal Numbers Manager
#  ─────────────────────────────────────────────────────────────
#  1. Deteksi total nomor di https://www.ivasms.com/portal/numbers
#  2. Ambil list nomor (Nomor, Range, Rate, Limit, dll)
#  3. Export ke format Excel (.xlsx) dan TXT (.txt)
# ═══════════════════════════════════════════════════════════════

import os
import sys
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


async def fetch_account_numbers(account_index = 1, force_refresh: bool = False, max_rows: int = 5000) -> dict:
    """
    Fetch semua nomor dari https://www.ivasms.com/portal/numbers untuk akun tertentu atau 'all' untuk semua akun.
    """
    if str(account_index).strip().lower() == "all":
        return await fetch_all_accounts_numbers(force_refresh=force_refresh, max_rows=max_rows)

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
