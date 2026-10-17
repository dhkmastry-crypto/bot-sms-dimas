import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import cleanup_profile_locks_and_orphans

async def inspect():
    user_data_dir = os.path.abspath("browser_profile_augestel_32")
    cleanup_profile_locks_and_orphans(user_data_dir)
    
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            args=["--window-position=-2000,-2000"]
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto("https://augestel.com/Switchfy/api/webhooks", wait_until="networkidle")
        print("URL:", page.url)
        
        info = await page.evaluate('''() => {
            const input = document.querySelector("#webhookUrl");
            if (!input) return { error: "No #webhookUrl" };
            const form = input.closest('form');
            if (!form) return { error: "No form for #webhookUrl" };
            
            const btns = Array.from(form.querySelectorAll('button, input[type="submit"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText,
                type: b.type,
                name: b.name,
                value: b.value,
                classes: b.className
            }));
            
            const allBtns = Array.from(document.querySelectorAll('button')).map(b => ({
                text: b.innerText,
                type: b.type,
                name: b.name,
                value: b.value,
                formAction: b.form ? b.form.action : null
            }));
            
            return {
                formAction: form.action,
                formMethod: form.method,
                formButtons: btns,
                allButtons: allBtns,
                formHTML: form.innerHTML
            };
        }''')
        
        print("Form Action:", info.get("formAction"))
        print("Form Method:", info.get("formMethod"))
        print("\nForm Buttons:")
        for b in info.get("formButtons", []):
            print("  ", b)
            
        print("\nAll Buttons on page:")
        for b in info.get("allButtons", []):
            print("  ", b)
            
        with open("scratch/form_32.html", "w", encoding="utf-8") as f:
            f.write(info.get("formHTML", ""))
        print("\nSaved form HTML to scratch/form_32.html")
        
        await ctx.close()

if __name__ == '__main__':
    asyncio.run(inspect())
