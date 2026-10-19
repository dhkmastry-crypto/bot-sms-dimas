import cloudscraper
import json
import re
import random
import string
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open("augestel_accounts.json", "r", encoding="utf-8") as f:
    accounts = json.load(f)

for idx in [1, 2]:
    acc = accounts[idx - 1]
    email = acc["email"]
    password = acc["password"]
    print(f"\n==========================================")
    print(f"Testing Account #{idx}: {email}")
    print(f"==========================================")

    scraper = cloudscraper.create_scraper(
        browser={
            "browser": "chrome",
            "platform": "windows",
            "desktop": True
        }
    )

    # 1. GET /Switchfy to get CSRF token
    resp = scraper.get("https://augestel.com/Switchfy", timeout=15)
    print("Initial GET status:", resp.status_code, "URL:", resp.url)
    csrf_matches = re.findall(r'<input[^>]*name="_token"[^>]*value="([^"]+)"', resp.text)
    if not csrf_matches:
        csrf_matches = re.findall(r'"_token"\s*:\s*"([^"]+)"', resp.text)
        if not csrf_matches:
            csrf_matches = re.findall(r'name="csrf-token"\s*content="([^"]+)"', resp.text)
    
    if not csrf_matches:
        print("❌ Could not find CSRF token on /Switchfy")
        continue

    csrf_token = csrf_matches[0]
    print(f"CSRF Token: {csrf_token[:12]}...")

    # 2. POST login
    post_data = {
        "_token": csrf_token,
        "email": email,
        "password": password,
        "remember": "on"
    }
    headers = {
        "Referer": "https://augestel.com/Switchfy",
        "Origin": "https://augestel.com",
    }
    login_resp = scraper.post("https://augestel.com/Switchfy/login", data=post_data, headers=headers, timeout=15)
    print("Login POST status:", login_resp.status_code, "URL:", login_resp.url)

    if "/login" in login_resp.url and login_resp.status_code == 200:
        print("❌ Login failed: redirected back to login")
        continue

    print("🎉 Login successful! Session cookies:", [c.name for c in scraper.cookies])

    # 3. GET /Switchfy/client/payment-methods
    pm_resp = scraper.get("https://augestel.com/Switchfy/client/payment-methods", timeout=15)
    print("Payment Methods GET status:", pm_resp.status_code, "URL:", pm_resp.url)

    # Check existing payment methods
    has_paypal = "PayPal" in pm_resp.text
    has_dimsong = "dimsongkang@gmail.com" in pm_resp.text or "di*********@gmail.com" in pm_resp.text
    print(f"Has PayPal: {has_paypal}, Has dimsong: {has_dimsong}")

    if has_paypal:
        print(f"✅ Account #{idx} ALREADY has PayPal!")
    else:
        print(f"Adding PayPal to Account #{idx}...")
        # Extract CSRF token from payment-methods page
        pm_csrf = re.findall(r'"k4"\s*:\s*"([^"]+)"', pm_resp.text)
        if not pm_csrf:
            pm_csrf = re.findall(r'<input[^>]*name="_token"[^>]*value="([^"]+)"', pm_resp.text)
        
        token_to_use = pm_csrf[0] if pm_csrf else csrf_token
        rnd_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        label = f"PP_{rnd_suffix}"
        print(f"Using label: {label}, CSRF: {token_to_use[:12]}...")

        # POST add payment method
        add_data = {
            "_token": token_to_use,
            "payment_method_id": "12",
            "label": label,
            "payment_details[paypal_email]": "dimsongkang@gmail.com"
        }
        add_headers = {
            "Referer": "https://augestel.com/Switchfy/client/payment-methods",
            "Origin": "https://augestel.com",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01"
        }
        add_resp = scraper.post("https://augestel.com/Switchfy/client/payment-methods", data=add_data, headers=add_headers, timeout=15)
        print("Add POST status:", add_resp.status_code)
        try:
            print("Response JSON:", add_resp.json())
        except Exception:
            print("Response Text:", add_resp.text[:300])

        # Verify by re-fetching
        verify_resp = scraper.get("https://augestel.com/Switchfy/client/payment-methods", timeout=15)
        print("Verify has PayPal now:", "PayPal" in verify_resp.text)
