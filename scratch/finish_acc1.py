import requests
import time
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

s = requests.Session()
s.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"}, timeout=10)

print("Monitoring Account #1 cooldown...")
while True:
    try:
        st = s.get("http://localhost:5000/api/augestel/pool/status", timeout=10).json()
        acc1 = st.get("status", {}).get("1", {})
        msg = acc1.get("message", "")
        logged_in = acc1.get("logged_in", False)
        print(f"[{time.strftime('%H:%M:%S')}] Account #1 status: logged_in={logged_in}, msg='{msg}'")
        
        if "Cooldown" not in msg or "0" in msg:
            print("Attempting to add PayPal on Account #1...")
            res = s.post("http://localhost:5000/api/augestel/pool/add-paypal/1", json={"paypal_email": "dimsongkang@gmail.com"}, timeout=120)
            data = res.json()
            print("Response:", data)
            if data.get("success"):
                print("🎉 Account #1 PayPal added successfully!")
                
                # Update paypal_setup_report.json
                rep_path = "paypal_setup_report.json"
                if os.path.exists(rep_path):
                    with open(rep_path, "r", encoding="utf-8") as rf:
                        rep = json.load(rf)
                    for item in rep:
                        if item.get("idx") == 1:
                            item["success"] = True
                            item["status"] = data.get("status", "added")
                            item["label"] = data.get("label", "-")
                            item["message"] = data.get("message", "Berhasil ditambahkan")
                            break
                    with open(rep_path, "w", encoding="utf-8") as wf:
                        json.dump(rep, wf, indent=2, ensure_ascii=False)
                break
    except Exception as e:
        print("Error checking status:", e)
    
    time.sleep(30)
