# ═══════════════════════════════════════════════════════════════
#  NONAKTIFKAN EVENT number.assigned & number.removed (SEMUA AKUN)
# ═══════════════════════════════════════════════════════════════
import asyncio
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WEBHOOK_URL = "https://dimsong.online/api/augestel/webhook"

def load_accounts():
    acc_path = os.path.join(BASE_DIR, "augestel_accounts.json")
    if os.path.exists(acc_path):
        with open(acc_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def cleanup_profile_locks(user_data_dir: str):
    for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
        lk_path = os.path.join(user_data_dir, lk)
        if os.path.exists(lk_path):
            try:
                os.remove(lk_path)
            except Exception:
                pass

async def process_account(p, idx: int, account_data: dict):
    profile_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")
    email = account_data.get("email", f"acc_{idx}")
    password = account_data.get("password", "")
    
    cleanup_profile_locks(profile_dir)
    
    print(f"\n─────────────────────────────────────────────────────────────")
    print(f"👉 [Akun #{idx:02d} / 34] {email}")
    print(f"─────────────────────────────────────────────────────────────")
    
    ctx = await p.chromium.launch_persistent_context(
        user_data_dir=profile_dir,
        channel="msedge",
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-gpu",
            "--window-position=-2000,-2000"
        ]
    )
    page = ctx.pages[0] if ctx.pages else await ctx.new_page()
    
    try:
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(2)
        
        # Cek jika perlu login
        curr_url = page.url
        login_input = await page.query_selector("#loginEmail, input[name='email']")
        if "/login" in curr_url.lower() or login_input:
            print(f"  🔑 Perlu login ulang, mengisi form kredensial...")
            await page.fill("#loginEmail, input[name='email']", email)
            await page.fill("#loginPassword, input[name='password']", password)
            try:
                rem = await page.query_selector("input[name='remember']")
                if rem:
                    await rem.check()
            except Exception:
                pass
            
            sub_btn = await page.query_selector("button[type='submit']")
            if sub_btn:
                await sub_btn.click()
            else:
                await page.keyboard.press("Enter")
            
            # Tunggu redirect
            for _ in range(15):
                await asyncio.sleep(1)
                if "/client/" in page.url or "/dashboard" in page.url or "/api/" in page.url:
                    break
            
            await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(2)

        # Cek status form saat ini
        cur_state = await page.evaluate('''() => {
            const input = document.querySelector("#webhookUrl");
            const cb = document.querySelector('input[name="is_active"][type="checkbox"]');
            const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            const na = document.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            const nr = document.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            const daily = document.querySelector('input[type="checkbox"][name="events[]"][value="earnings.daily"]');
            const text = document.body.innerText || "";
            return {
                has_form: Boolean(input),
                url: input ? input.value : "",
                is_active: cb ? cb.checked : false,
                msg: msg ? msg.checked : false,
                assigned: na ? na.checked : false,
                removed: nr ? nr.checked : false,
                daily: daily ? daily.checked : false,
                is_delivering: text.includes("Delivering") && !text.includes("switched off automatically")
            };
        }''')

        if not cur_state.get("has_form"):
            print(f"  ⚠️ Tidak menemukan form webhook (Mungkin belum login atau cooldown). URL: {page.url}")
            await ctx.close()
            return {"idx": idx, "email": email, "success": False, "reason": "No form found"}

        # Cek apakah sudah dalam kondisi mati
        if cur_state.get("assigned") is False and cur_state.get("removed") is False and cur_state.get("url") and cur_state.get("is_active"):
            print(f"  ✅ SUDAH NONAKTIF! number.assigned=False | number.removed=False (URL: {cur_state.get('url')})")
            await ctx.close()
            return {"idx": idx, "email": email, "success": True, "already_disabled": True}

        print(f"  ⚙️ Mengubah webhook: mematikan number.assigned & number.removed...")
        target_url = cur_state.get("url") or DEFAULT_WEBHOOK_URL
        
        # Modifikasi DOM & Submit
        sub_res = await page.evaluate(f'''() => {{
            const input = document.querySelector("#webhookUrl");
            if (!input) return {{ error: "No input #webhookUrl" }};
            const form = input.closest('form');
            if (!form) return {{ error: "No form found" }};

            // 1. Hapus _method=DELETE agar tidak menghapus webhook
            const delInput = form.querySelector('input[name="_method"]');
            if (delInput) {{
                delInput.remove();
            }}

            // 2. Set endpoint URL
            input.value = "{target_url}";
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));

            // 3. Pastikan is_active checked
            const cb = form.querySelector('input[type="checkbox"][name="is_active"]');
            if (cb) {{
                cb.checked = true;
                cb.dispatchEvent(new Event('input', {{ bubbles: true }}));
                cb.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}

            // 4. Pastikan message.received AKTIF
            const msg = form.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            if (msg) {{
                msg.checked = true;
                msg.dispatchEvent(new Event('input', {{ bubbles: true }}));
                msg.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}

            // 5. MATIKAN number.assigned & number.removed (UNCHECK)
            const na = form.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            if (na) {{
                na.checked = false;
                na.dispatchEvent(new Event('input', {{ bubbles: true }}));
                na.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
            const nr = form.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            if (nr) {{
                nr.checked = false;
                nr.dispatchEvent(new Event('input', {{ bubbles: true }}));
                nr.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}

            // 6. Klik tombol simpan (Save / Update endpoint)
            const updateBtn = form.querySelector('button[style*="primary-color"]') || 
                              Array.from(form.querySelectorAll('button')).find(b => b.innerText.includes('endpoint') && !b.innerText.includes('Remove'));

            if (updateBtn) {{
                updateBtn.click();
                return {{ success: true, method: "button_click", text: updateBtn.innerText.trim() }};
            }} else {{
                form.submit();
                return {{ success: true, method: "form_submit" }};
            }}
        }}''')

        print(f"  Submitting form: {sub_res}")
        await asyncio.sleep(5)
        try:
            await page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            pass

        # Verifikasi akhir
        final_state = await page.evaluate('''() => {
            const na = document.querySelector('input[type="checkbox"][name="events[]"][value="number.assigned"]');
            const nr = document.querySelector('input[type="checkbox"][name="events[]"][value="number.removed"]');
            const msg = document.querySelector('input[type="checkbox"][name="events[]"][value="message.received"]');
            const input = document.querySelector("#webhookUrl");
            const cb = document.querySelector('input[name="is_active"][type="checkbox"]');
            const text = document.body.innerText || "";
            return {
                url: input ? input.value : "",
                is_active: cb ? cb.checked : false,
                msg: msg ? msg.checked : false,
                assigned: na ? na.checked : false,
                removed: nr ? nr.checked : false,
                is_delivering: text.includes("Delivering") && !text.includes("switched off automatically")
            };
        }''')

        is_ok = (final_state.get("assigned") is False and 
                 final_state.get("removed") is False and 
                 final_state.get("msg") is True and 
                 final_state.get("is_active") is True)
        
        status_icon = "🎉" if is_ok else "⚠️"
        print(f"  {status_icon} Hasil Akhir: assigned={final_state.get('assigned')} | removed={final_state.get('removed')} | msg={final_state.get('msg')} | delivering={final_state.get('is_delivering')}")
        
        await ctx.close()
        return {"idx": idx, "email": email, "success": is_ok, "state": final_state}

    except Exception as e:
        print(f"  ❌ Error memproses Akun #{idx}: {e}")
        try:
            await ctx.close()
        except Exception:
            pass
        return {"idx": idx, "email": email, "success": False, "error": str(e)}

async def main():
    accounts = load_accounts()
    print("=" * 65)
    print(f"  MEMATIKAN WEBHOOK number.assigned & number.removed")
    print(f"  Total Akun: {len(accounts)}")
    print("=" * 65)
    
    results = []
    async with async_playwright() as p:
        for idx in range(1, len(accounts) + 1):
            acc = accounts[idx - 1]
            res = await process_account(p, idx, acc)
            results.append(res)
            await asyncio.sleep(1.5)

    print("\n" + "=" * 65)
    print("  RINGKASAN HASIL UPDATE SEMUA AKUN")
    print("=" * 65)
    succ_count = sum(1 for r in results if r.get("success"))
    print(f"Total Sukses: {succ_count} / {len(accounts)}")
    for r in results:
        status_str = "SUKSES" if r.get("success") else f"GAGAL ({r.get('reason') or r.get('error')})"
        print(f"Akun #{r.get('idx', 0):02d} ({r.get('email')}): {status_str}")

if __name__ == "__main__":
    asyncio.run(main())
