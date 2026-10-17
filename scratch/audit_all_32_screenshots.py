import requests
import time
import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "webhook_screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

session = requests.Session()
login_res = session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})
if login_res.status_code != 200:
    print("Failed to login to admin server!")
    sys.exit(1)

accs_path = os.path.join(BASE_DIR, "augestel_accounts.json")
accounts = []
if os.path.exists(accs_path):
    with open(accs_path, "r", encoding="utf-8") as f:
        accounts = json.load(f)

print(f"==================================================================")
print(f"  AUDITING ALL {len(accounts)} AUGESTEL ACCOUNTS VIA SCREENSHOTS")
print(f"==================================================================")

audit_results = []

for idx in range(1, len(accounts) + 1):
    acc = accounts[idx - 1]
    email = acc.get("email", f"acc_{idx}")
    print(f"\n[#{idx:02d} / {len(accounts)}] Checking {email}...")
    
    # 1. Navigate to /Switchfy/api/webhooks
    nav_res = session.post(
        f"http://localhost:5000/api/augestel/pool/eval/{idx}",
        json={"script": "window.location.href = '/Switchfy/api/webhooks'; 'navigating';"},
        timeout=15
    )
    if nav_res.status_code != 200 or not nav_res.json().get("success"):
        print(f"  ⚠️ Could not navigate tab #{idx}: {nav_res.text}")
        audit_results.append({
            "idx": idx,
            "email": email,
            "success": False,
            "error": "Failed to navigate"
        })
        continue

    # Wait for page to render
    time.sleep(2.5)

    # 2. Extract DOM details
    eval_res = session.post(
        f"http://localhost:5000/api/augestel/pool/eval/{idx}",
        json={"script": """(() => {
            const urlInput = document.querySelector("#webhookUrl");
            const urlVal = urlInput ? urlInput.value : "";
            const cb = document.querySelector('input[name="is_active"][type="checkbox"]');
            const isActive = cb ? cb.checked : false;
            const bodyText = document.body.innerText || "";
            const isDelivering = bodyText.includes("Delivering") && !bodyText.includes("switched off automatically");
            const nameMatch = bodyText.match(/Welcome back,\\s*([^\\n]+)/i);
            const userName = nameMatch ? nameMatch[1].trim() : "";
            return {
                url: urlVal,
                is_active: isActive,
                is_delivering: isDelivering,
                user_name: userName,
                page_url: window.location.href
            };
        })()"""},
        timeout=15
    )
    dom_info = {}
    if eval_res.status_code == 200 and eval_res.json().get("success"):
        dom_info = eval_res.json().get("result", {})
    
    # 3. Take screenshot via debug endpoint
    debug_res = session.get(f"http://localhost:5000/api/augestel/pool/debug/{idx}", timeout=15)
    scr_src = ""
    if debug_res.status_code == 200:
        scr_src = debug_res.json().get("data", {}).get("form_info", {}).get("screenshot", "")

    dst_name = f"acc_{idx:02d}.png"
    dst_path = os.path.join(OUT_DIR, dst_name)
    if scr_src and os.path.exists(scr_src):
        shutil.copy2(scr_src, dst_path)
    
    res_entry = {
        "idx": idx,
        "email": email,
        "user_name": dom_info.get("user_name", ""),
        "webhook_url": dom_info.get("url", ""),
        "is_active": dom_info.get("is_active", False),
        "is_delivering": dom_info.get("is_delivering", False),
        "screenshot": dst_path,
        "screenshot_rel": f"webhook_screenshots/{dst_name}"
    }
    audit_results.append(res_entry)
    
    status_icon = "🟢" if res_entry["is_delivering"] and res_entry["is_active"] else "🔴"
    print(f"  {status_icon} User: '{res_entry['user_name']}' | URL: '{res_entry['webhook_url']}' | Active: {res_entry['is_active']} | Delivering: {res_entry['is_delivering']}")
    print(f"  📷 Screenshot saved: {dst_name}")

    # 4. Return tab to /Switchfy/client/numbers
    session.post(
        f"http://localhost:5000/api/augestel/pool/eval/{idx}",
        json={"script": "window.location.href = '/Switchfy/client/numbers'; 'returning';"},
        timeout=15
    )
    time.sleep(0.5)

# Save JSON summary
summary_path = os.path.join(OUT_DIR, "audit_summary.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(audit_results, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 66)
print(f"AUDIT COMPLETE: All {len(audit_results)} accounts checked & screenshotted!")
print(f"Summary JSON saved to: {summary_path}")
print("=" * 66)
