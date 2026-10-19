import requests
import json
import time
import sys
import os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
acc_path = os.path.join(BASE_DIR, "augestel_accounts.json")
with open(acc_path, "r", encoding="utf-8") as f:
    accounts = json.load(f)

print("=" * 65)
print(f"  ADD PAYPAL TO ALL {len(accounts)} AUGESTEL ACCOUNTS")
print("  PayPal Email : dimsongkang@gmail.com")
print("  Label        : Random (e.g. PP_xxxxxx)")
print("=" * 65)

s = requests.Session()
login_res = s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"}, timeout=10)
if login_res.status_code != 200:
    print("❌ Failed to log in to Admin Server!")
    sys.exit(1)

results = []

for idx in range(1, len(accounts) + 1):
    acc = accounts[idx - 1]
    email = acc.get("email", f"acc_{idx}")
    print(f"\n[#{idx:02d}/{len(accounts)}] Processing {email} ...", flush=True)

    try:
        res = s.post(
            f"http://localhost:5000/api/augestel/pool/add-paypal/{idx}",
            json={"paypal_email": "dimsongkang@gmail.com"},
            timeout=120
        )
        if res.status_code == 200:
            data = res.json()
            status = data.get("status", "unknown")
            msg = data.get("message", "")
            label = data.get("label", "-")
            
            if data.get("success"):
                if status == "already_exists":
                    print(f"  ℹ️ [ALREADY EXISTS] PayPal sudah terpasang sebelumnya di akun ini.", flush=True)
                else:
                    print(f"  ✅ [SUCCESS] Berhasil menambahkan PayPal! (Label: {label})", flush=True)
            else:
                print(f"  ❌ [FAILED] {msg}", flush=True)

            results.append({
                "idx": idx,
                "email": email,
                "success": data.get("success", False),
                "status": status,
                "label": label,
                "message": msg
            })
        else:
            print(f"  ❌ [HTTP {res.status_code}] {res.text[:200]}", flush=True)
            results.append({
                "idx": idx,
                "email": email,
                "success": False,
                "status": f"http_{res.status_code}",
                "message": res.text[:200]
            })

    except Exception as e:
        print(f"  ❌ [EXCEPTION] {e}", flush=True)
        results.append({
            "idx": idx,
            "email": email,
            "success": False,
            "status": "exception",
            "message": str(e)
        })

    # Small pause between accounts to prevent rate limiting
    time.sleep(1.5)

# Save report
report_path = os.path.join(BASE_DIR, "paypal_setup_report.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 65)
print("  SUMMARY OF ALL ACCOUNTS:")
print("=" * 65)
added_count = sum(1 for r in results if r.get("status") == "added")
already_count = sum(1 for r in results if r.get("status") == "already_exists")
failed_count = sum(1 for r in results if not r.get("success"))

print(f"Total Accounts  : {len(results)}")
print(f"Newly Added     : {added_count}")
print(f"Already Existed : {already_count}")
print(f"Failed          : {failed_count}")
print(f"Full report saved to: {report_path}")
