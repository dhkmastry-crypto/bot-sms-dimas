import asyncio
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.async_api import async_playwright
from numbers_service import get_augestel_accounts
from auto_add_augestel import ensure_augestel_login

async def return_account(idx: int):
    accs = get_augestel_accounts()
    acc = accs[idx - 1]
    email = acc['email']
    pwd = acc['password']
    print(f"=== TESTING RETURN FOR AKUN #{idx} ({email}) ===")

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=os.path.abspath(f"browser_profile_augestel_{idx}"),
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        login_ok = await ensure_augestel_login(page, email, pwd)
        if not login_ok:
            print(f"❌ Login failed for Akun #{idx}")
            await ctx.close()
            return False

        print(f"✅ Logged in successfully! Now navigating to client/numbers...")
        await page.goto("https://augestel.com/Switchfy/client/numbers", wait_until="networkidle", timeout=45000)
        await asyncio.sleep(2)

        # Check for wait element
        wait_el = await page.query_selector(".wait")
        if wait_el:
            txt = (await wait_el.inner_text()).strip()
            print(f"⏳ Cooldown on client/numbers: {txt}")
            await ctx.close()
            return False

        btn = await page.query_selector("#bulkReturnAllBtn")
        if not btn or not await btn.is_visible():
            empty = await page.query_selector(".dataTables_empty")
            if empty:
                print("ℹ️ Tabel kosong, tidak ada nomor untuk di-return.")
                await ctx.close()
                return True
            print("❌ #bulkReturnAllBtn not found or not visible!")
            await ctx.close()
            return False

        print("👉 Clicking #bulkReturnAllBtn...")
        await btn.click()
        await asyncio.sleep(1)

        confirm_btn = await page.wait_for_selector("button.swal2-confirm", timeout=5000)
        if not confirm_btn:
            print("❌ Confirm button in Swal not found!")
            await ctx.close()
            return False

        print("👉 Clicking confirm button in Swal modal...")
        try:
            async with page.expect_response(lambda r: "bulk-return" in r.url, timeout=20000) as resp_info:
                await confirm_btn.click()
            resp = await resp_info.value
            status = resp.status
            text = await resp.text()
            print(f"🎉 RESPONSE ({status}): {text}")
            await asyncio.sleep(2)
            await ctx.close()
            return status == 200
        except Exception as e:
            print(f"❌ Error waiting for response: {e}")
            await ctx.close()
            return False

if __name__ == "__main__":
    asyncio.run(return_account(1))
