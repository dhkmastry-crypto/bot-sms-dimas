import asyncio
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from augestel_browser_pool import get_browser_pool

async def main():
    pool = get_browser_pool()
    # Check account 1
    page1 = pool.pages.get(1)
    if page1:
        await page1.goto("https://augestel.com/Switchfy/client/payment-methods", wait_until="networkidle")
        html_info = await page1.evaluate('''() => {
            return {
                title: document.title,
                bodySnippet: document.body.innerText.slice(0, 1500),
                hasEmpty: !!document.querySelector('.empty, :contains("No Payment Methods Yet")') || document.body.innerText.includes('No Payment Methods Yet'),
                tables: Array.from(document.querySelectorAll('table')).map(t => t.innerText),
                cards: Array.from(document.querySelectorAll('.card-body, .payment-methods, [data-payment-method]')).map(c => c.innerText.slice(0, 200))
            };
        }''')
        print("Account 1 PM Structure:")
        print("hasEmpty:", html_info["hasEmpty"])
        print("tables:", html_info["tables"])
        print("cards:", html_info["cards"][:3])
        print("bodySnippet:\n", html_info["bodySnippet"][:500])

if __name__ == "__main__":
    from augestel_browser_pool import AugestelBrowserPool
    # Can run through pool instance if running in admin_server process
