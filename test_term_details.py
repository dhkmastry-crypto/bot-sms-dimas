import asyncio
from playwright.async_api import async_playwright
from auto_add_augestel import get_account_config, ensure_augestel_login, fetch_test_terminations, get_termination_details

async def test_term_details():
    cfg = get_account_config(1)
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=cfg["user_data_dir"],
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await ensure_augestel_login(page, cfg["email"], cfg["password"])
        
        # Check Pakistan terminations
        res_pak = await fetch_test_terminations(page, "pakistan", start=0, length=3)
        print("Pakistan terminations found:", len(res_pak.get("data", [])))
        for d in res_pak.get("data", []):
            import re
            m = re.search(r'data-termination-id="(\d+)"', d.get("action", ""))
            tid = m.group(1) if m else None
            print(f"Term: {d.get('name')} (ID: {tid})")
            if tid:
                info = await get_termination_details(page, tid)
                print("  ok:", info.get("ok"), "error:", info.get("error"))
                if info.get("ok"):
                    data = info.get("data", {})
                    terms = data.get("terminations", [])
                    print(f"  terminations count: {len(terms)}")
                    if terms:
                        t = terms[0]
                        print("  term details:", {
                            "id": t.get("id"),
                            "limit_per_termination": t.get("limit_per_termination"),
                            "current_from_termination": t.get("current_from_termination"),
                            "no_numbers": t.get("no_numbers")
                        })
        
        # Check German terminations
        res_ger = await fetch_test_terminations(page, "german", start=0, length=3)
        print("\nGerman terminations found:", len(res_ger.get("data", [])))
        for d in res_ger.get("data", []):
            import re
            m = re.search(r'data-termination-id="(\d+)"', d.get("action", ""))
            tid = m.group(1) if m else None
            print(f"Term: {d.get('name')} (ID: {tid})")
            if tid:
                info = await get_termination_details(page, tid)
                print("  ok:", info.get("ok"), "error:", info.get("error"))
                if info.get("ok"):
                    data = info.get("data", {})
                    terms = data.get("terminations", [])
                    print(f"  terminations count: {len(terms)}")
                    if terms:
                        t = terms[0]
                        print("  term details:", {
                            "id": t.get("id"),
                            "limit_per_termination": t.get("limit_per_termination"),
                            "current_from_termination": t.get("current_from_termination"),
                            "no_numbers": t.get("no_numbers")
                        })

        await context.close()

if __name__ == "__main__":
    asyncio.run(test_term_details())
