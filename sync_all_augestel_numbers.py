# ═══════════════════════════════════════════════════════════════
#  SYNC ALL AUGESTEL NUMBERS TO DISK CACHE
#  ─────────────────────────────────────────────────────────────
#  Mengambil seluruh nomor aktif dari ke-7 akun Augestel secara
#  paralel (1 thread per akun/API key) hingga tuntas 25 halaman
#  (2.500 nomor per akun = 17.500 total nomor) dan menyimpannya ke cache.
# ═══════════════════════════════════════════════════════════════

import os
import sys
import json
import time
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("sync_augestel")

from augestel_client import AugestelClient
from numbers_service import get_augestel_accounts, _format_augestel_number_item


def sync_single_account(account_idx: int, account_data: dict) -> dict:
    email = account_data.get("email", "")
    api_key = account_data.get("api_key", "")
    if not api_key:
        logger.warning(f"⚠️ [Akun #{account_idx} | {email}] Tidak memiliki API key, dilewati.")
        return {"account_index": account_idx, "email": email, "numbers": [], "total": 0}

    logger.info(f"🚀 [Akun #{account_idx} | {email}] Memulai sinkronisasi seluruh nomor...")
    client = AugestelClient(api_key=api_key, email=email)

    cache_file = os.path.join(os.path.dirname(__file__), f"augestel_numbers_cache_{account_idx}.json")
    existing_dict = {}
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                d = json.load(f)
                for it in d.get("numbers", []):
                    num = str(it.get("number", "")).strip()
                    if num:
                        existing_dict[num] = it
        except Exception:
            pass

    page = 1
    max_pages = 30  # Cukup untuk 3000 nomor (portal maks 2500)
    per_page = 100
    total_portal = 0

    while page <= max_pages:
        try:
            res = client.get_numbers(page=page, per_page=per_page)
            if not res.get("success"):
                logger.warning(f"⚠️ [Akun #{account_idx}] Gagal ambil halaman {page}: {res.get('message')}")
                break

            items = res.get("data", [])
            pagination = res.get("pagination", {})
            total_portal = pagination.get("total", total_portal)
            last_page = pagination.get("last_page", max_pages)

            if not items:
                break

            for it in items:
                formatted = _format_augestel_number_item(it, len(existing_dict) + 1, account_idx, email)
                num_str = formatted.get("number")
                if num_str:
                    existing_dict[num_str] = formatted

            logger.info(f"  📥 [Akun #{account_idx} | {email}] Halaman {page}/{last_page} didapat (+{len(items)} nomor). Terkumpul: {len(existing_dict)}/{total_portal}")

            if page >= last_page:
                break

            page += 1
            time.sleep(1.2)
        except Exception as e:
            logger.error(f"❌ [Akun #{account_idx}] Error halaman {page}: {e}")
            break

    final_numbers = list(existing_dict.values())
    for i, it in enumerate(final_numbers, 1):
        it["id"] = str(i)

    final_total = total_portal or len(final_numbers)

    # Simpan ke cache disk akun ini
    now_ts = datetime.now()
    result = {
        "success": True,
        "account_index": f"aug_{account_idx}",
        "email": f"Augestel #{account_idx} ({email})",
        "total": final_total,
        "count": len(final_numbers),
        "numbers": final_numbers,
        "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
    except Exception as e:
        logger.error(f"Gagal simpan cache Akun #{account_idx}: {e}")

    logger.info(f"✅ [Akun #{account_idx} | {email}] Selesai! {len(final_numbers)} nomor tersimpan ke cache.")
    return {
        "account_index": account_idx,
        "email": email,
        "numbers": final_numbers,
        "total": final_total
    }


def sync_all_accounts():
    accounts = get_augestel_accounts()
    if not accounts:
        logger.error("Tidak ada akun Augestel terdaftar!")
        return

    logger.info("═" * 65)
    logger.info(f"⚡ MEMULAI SINKRONISASI PARALEL {len(accounts)} AKUN AUGESTEL")
    logger.info("═" * 65)

    all_combined = []
    breakdown = []
    total_sum = 0

    # Jalankan paralel 1 thread per akun
    with ThreadPoolExecutor(max_workers=len(accounts)) as executor:
        futures = [executor.submit(sync_single_account, i, acc) for i, acc in enumerate(accounts, 1)]
        results = [f.result() for f in futures]

    for res in sorted(results, key=lambda x: x["account_index"]):
        idx = res["account_index"]
        em = res["email"]
        nums = res["numbers"]
        tot = res["total"]

        total_sum += tot
        for item in nums:
            item_copy = dict(item)
            item_copy["account_index"] = f"aug_{idx}"
            item_copy["account_email"] = em
            all_combined.append(item_copy)

        breakdown.append({
            "account_index": idx,
            "email": em,
            "total": tot
        })

    # Re-index id gabungan 1..N
    for i, item in enumerate(all_combined, 1):
        item["id"] = str(i)

    now_ts = datetime.now()
    agg_result = {
        "success": True,
        "account_index": "augestel_all",
        "email": f"Semua Akun Augestel ({len(breakdown)} Akun Aktif)",
        "total": total_sum or len(all_combined),
        "count": len(all_combined),
        "numbers": all_combined,
        "accounts_breakdown": breakdown,
        "cached_at": now_ts.strftime("%Y-%m-%d %H:%M:%S")
    }

    agg_file = os.path.join(os.path.dirname(__file__), "augestel_numbers_cache.json")
    with open(agg_file, "w", encoding="utf-8") as f:
        json.dump(agg_result, f, indent=2)

    logger.info("═" * 65)
    logger.info(f"🎉 SINKRONISASI TUNTAS!")
    logger.info(f"📊 Total nomor teragregasi: {len(all_combined)} nomor (dari total {total_sum} nomor di portal)")
    logger.info("═" * 65)


if __name__ == "__main__":
    sync_all_accounts()
