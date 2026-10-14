import asyncio
import json
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config, ensure_augestel_login, fetch_test_terminations

async def test_search():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=cfg["user_data_dir"],
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        
        logged = await ensure_augestel_login(page, cfg["email"], cfg["password"])
        print(f"Logged in: {logged}")
        
        # Test fetch_test_terminations with "pakistan"
        res_pak = await fetch_test_terminations(page, "pakistan", start=0, length=5)
        print("Pakistan fetch result:")
        print("  recordsFiltered:", res_pak.get("recordsFiltered"), "recordsTotal:", res_pak.get("recordsTotal"), "error:", res_pak.get("error"))
        for d in res_pak.get("data", []):
            print("  Name:", d.get("name"), "| action:", d.get("action")[:50] if d.get("action") else None)

        # Test fetch_test_terminations with "german"
        res_ger = await fetch_test_terminations(page, "german", start=0, length=5)
        print("German fetch result:")
        print("  recordsFiltered:", res_ger.get("recordsFiltered"), "recordsTotal:", res_ger.get("recordsTotal"), "error:", res_ger.get("error"))
        for d in res_ger.get("data", []):
            print("  Name:", d.get("name"), "| action:", d.get("action")[:50] if d.get("action") else None)

        # Test fetch_test_terminations with "germany"
        res_ger2 = await fetch_test_terminations(page, "germany", start=0, length=5)
        print("Germany fetch result:")
        print("  recordsFiltered:", res_ger2.get("recordsFiltered"), "recordsTotal:", res_ger2.get("recordsTotal"), "error:", res_ger2.get("error"))
        for d in res_ger2.get("data", []):
            print("  Name:", d.get("name"), "| action:", d.get("action")[:50] if d.get("action") else None)

        await context.close()

if __name__ == "__main__":
    asyncio.run(test_search())
