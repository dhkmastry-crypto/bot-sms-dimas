import os
import sys
import json
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = r"c:\Users\ADMIN\Downloads\OTP IVA SMS"
log_file = os.path.join(BASE_DIR, "bot.log")

webhook_data = {
    "total_revenue_usd": 0.0,
    "total_revenue_idr": 0,
    "total_sms": 0,
    "today_date": datetime.now().strftime("%Y-%m-%d"),
    "today_revenue_usd": 0.0,
    "today_sms": 0,
    "yesterday_revenue_usd": 0.0,
    "yesterday_sms": 0,
    "by_account": {},
    "by_country": {},
    "by_platform": {},
    "recent_transactions": [],
    "last_event_time": None,
    "sync_source": "Augestel Real-Time Webhook Engine (https://dimsong.online)"
}

rate_per_sms = 0.0160
today_str = datetime.now().strftime("%Y-%m-%d")

if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if "[Augestel Webhook] Sent OTP:" in line:
                ts = line[:19]
                parts = line.split("[Augestel Webhook] Sent OTP:")
                rest = parts[1].strip()
                subparts = [p.strip() for p in rest.split("|")]
                if len(subparts) >= 3:
                    cc = subparts[0]
                    plat = subparts[1]
                    otp_acc = subparts[2]
                    otp = otp_acc.split("(")[0].strip()
                    acc = otp_acc.split("(")[1].replace(")", "").strip() if "(" in otp_acc else "Akun #1"

                    webhook_data["total_sms"] += 1
                    webhook_data["total_revenue_usd"] = round(webhook_data["total_revenue_usd"] + rate_per_sms, 4)

                    if ts.startswith(today_str):
                        webhook_data["today_sms"] += 1
                        webhook_data["today_revenue_usd"] = round(webhook_data["today_revenue_usd"] + rate_per_sms, 4)

                    if acc not in webhook_data["by_account"]:
                        webhook_data["by_account"][acc] = {"email": acc, "sms": 0, "usd": 0.0, "idr": 0}
                    webhook_data["by_account"][acc]["sms"] += 1
                    webhook_data["by_account"][acc]["usd"] = round(webhook_data["by_account"][acc]["usd"] + rate_per_sms, 4)
                    webhook_data["by_account"][acc]["idr"] = int(webhook_data["by_account"][acc]["usd"] * 16250)

                    if cc not in webhook_data["by_country"]:
                        webhook_data["by_country"][cc] = {"sms": 0, "usd": 0.0}
                    webhook_data["by_country"][cc]["sms"] += 1
                    webhook_data["by_country"][cc]["usd"] = round(webhook_data["by_country"][cc]["usd"] + rate_per_sms, 4)

                    webhook_data["recent_transactions"].insert(0, {
                        "time": ts,
                        "account": acc,
                        "platform": plat,
                        "otp": otp,
                        "country": cc,
                        "rate_usd": rate_per_sms
                    })
                    webhook_data["last_event_time"] = ts

webhook_data["recent_transactions"] = webhook_data["recent_transactions"][:30]
webhook_data["total_revenue_idr"] = int(webhook_data["total_revenue_usd"] * 16250)

webhook_file = os.path.join(BASE_DIR, "augestel_earnings_webhook.json")
with open(webhook_file, "w", encoding="utf-8") as f:
    json.dump(webhook_data, f, indent=2, ensure_ascii=False)

print(f"Generated augestel_earnings_webhook.json:")
print(f"Total Webhook SMS: {webhook_data['total_sms']}")
print(f"Total Webhook Revenue: ${webhook_data['total_revenue_usd']:.4f} (Rp {webhook_data['total_revenue_idr']:,})")
print(f"Accounts in Webhook: {len(webhook_data['by_account'])}")
print(f"Last Event Time: {webhook_data['last_event_time']}")
