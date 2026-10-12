# ═══════════════════════════════════════════════════════════════
#  IVASMS OTP BOT - KONFIGURASI
#  Isi semua konfigurasi di bawah ini sebelum menjalankan bot
# ═══════════════════════════════════════════════════════════════

# ────────────────────────────────────────────
#  TELEGRAM BOT CONFIG
# ────────────────────────────────────────────

# Token dari @BotFather
BOT_TOKEN = "8773155835:AAGJjiP2soccLPvic0N3zWOYrBpB-qWWGuY"

# Chat ID grup Telegram (gunakan angka negatif untuk grup)
# Jalankan get_chat_id.py untuk mendapatkan Chat ID
GROUP_CHAT_ID = "-1003979578338"

# Link tombol CHANNEL
CHANNEL_LINK = "https://t.me/dimsongotp"
GROUP_LINK = CHANNEL_LINK

# Link tombol FILE (pengganti PANEL)
FILE_LINK = "https://t.me/dimsongfile"
NUMBER_LINK = FILE_LINK
OWNER_LINK = ""

# Sensor teks tengah nomor telepon (contoh: "••••", "~", atau nama brand)
SENSOR_TEXT = "••••"

# Nama bot yang muncul di pesan
BOT_NAME = "OTP_BOT"

# ────────────────────────────────────────────
#  IVASMS CONFIG
# ────────────────────────────────────────────

# URL IVASMS
IVASMS_URL = "https://www.ivasms.com"

# Kredensial akun IVASMS untuk auto-login otomatis
IVASMS_EMAIL = "lesehp60nz@deltajohnsons.com"
IVASMS_PASSWORD = "scorpion998"

# Kredensial akun ke-2 IVASMS
IVASMS_EMAIL_2 = "dimsongkang@gmail.com"
IVASMS_PASSWORD_2 = "dimsongkang@"

# Endpoint halaman SMS Received
IVASMS_SMS_ENDPOINT = "/portal/sms/received"

# YesCaptcha Client Key untuk bypass Cloudflare Turnstile
YESCAPTCHA_KEY = "b2a81640d7b006b1d5c15459ec72366b442af456139860"

# Interval polling dalam detik (10 detik agar tidak terkena rate limit IVASMS)
POLL_INTERVAL = 10

# ────────────────────────────────────────────
#  ELITE-SMS CONFIG (https://elite-sms.com/api)
# ────────────────────────────────────────────
ELITE_SMS_ENABLED = True
ELITE_SMS_URL = "https://elite-sms.com/api"
ELITE_SMS_API_KEY = "d3a3c3c16dd897f09dfa3778a92d04331a33f876"

# ────────────────────────────────────────────
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "Tp1q8P1q3vzhnmkS82iN9Qz4UTcQyt6AeQfwmXUgo0M-1791840304-1.2.1.1-h6yivTw_KBEJSlItSjamUN9KTY_DcjTA71ZaS8V.yqxzXoGfVGF1VJfJShr3y2YCbmYqJNbp2dRw92Qu_WykbB6Jk7BiLIoEtZEhDogdd9oFVGv.lHgaLNWGqji4ZKadGToUsnNy7YO1RIonOslYLNp9AWeQMsdxvzY5PtpDzwO67BENeNgYuRCyXTn3Ckf8QXwWb8Z298OzKnfVbpo_GFiq6EkVIUUmIA7lvI6dUlzqCjueaWrhoTf2NDYKwa4PeXTKmnW087kJp.FHYpmo799Xrq3Tq1Xg8449Q1J9smKUFRXRdHZDZ0RrmJSUuImFSZc.xulA0.TYZYPHfo1YtzTRybT1UYsjg6wvJ8FGZRnKKHXY9nLA9JTvaiE4mlh4_W3.Kj6nvYQ19pjVy5xtg3ZEPDi83OvENHbKbyrsd5JNwd0GC4NZTRRhD4ov0MhwFQjABzlMvsl9EC0J.Pn6A7zgsBSDzjrX8tjIkNhN_k4V7C_FxN3Wu3blP5qCaDM1paH_svohgML3nezClsrh3w",
    "XSRF-TOKEN": "eyJpdiI6IjFLaklYVGY5TUMrUllCT1NNRnNxYnc9PSIsInZhbHVlIjoiL3RnT0hrTFJYM0FpQVNKVUNWZHpqQ3M2czZhYXNSajhiRS92SWIrQU5zamErYy9BRGlTcjVJSUNRTDVWVHd6K2ZpQWdEek9kSmxmelNZMXlEbWszdm9VWWtNT3JBbURhR3MyckxEQUN3a2p5M2pGNXBzYkxxWGhZY2t5bkZVanMiLCJtYWMiOiJkY2Y5NWUwMzZhMWNiYjMzNGNkYzA2MTdlZGMzZTg0ZjZkODQyODgyYzM1ODBkZTM2ZTZkODhmYTQ0ZTI1YTBkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1mSmZXSHV2UktvUFF0M0dPNlBDb3c9PSIsInZhbHVlIjoiSzhRbXRWYzRDS0I1OU1wQ1YybmtMaEJyNi9zS0xxckJyOVYxKy81ek5kQ3kwUWhuSGhVaWdIaW5NNHhrSDNKbVQzbzZXQUsyd0FPOEIxa0lJZG5xbFpFT0hneDUzYnI1UTN1MTRQdkZTTzcvNDFKODllZUMyMGVLL043aFlSS0IiLCJtYWMiOiI2YTE1NzlmYTg4MTg2OWM4M2E0MTVjOGU2Y2RiMDhlZGE2YWQ1OWY0MTAyNmRjMDg3ZjQyNTU5YjVjNzE1NTg5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "WGv4n8FPVKfadpB4s9zWbwRym7RmWyr.xH_BfYhw6eU-1791839467-1.2.1.1-0gAQ7noyXT0nvEZK8bqrYKq0lTdwBzbo4pYx.x2aBVAiR0rOLnpwWd4Nd0duaMng9FW2mOkSmAV3CxX1t6ClnfQ5fOuBcu5br0wiA7R1RwKws9HxHY7lk68QK8U7BvxPmeFB6hPsN3zoCbqjtZZAGzaKEzWWJJJji.weWx9Nsm6oL80GsbIlVyHJxDUPIl2GCQOixOz9Cjz.E.C4j.MN6ZK4fbz1wrNbBxbw4Clcl9GLVess9VvkGCxqDp2R9ECgGs9QIGRbvLaQDXCHYmehjRPIoCjeEy3kFGERYBhPZXTZh1Bqx7LkovgAWVvGCk.NgrXFSwbRkBjHFFl_WCqO.vR1NbLFMPTTlwRfZENT0A7irX7nH6ytBdgYTTD4v3SIpOTxqOMaIa6dCLcuMNwIbQJrVs25dGEp3OaI4T9END0Y9qOjhyadSXYzQlpqmhAjOIHrQVqCW4AEMidG4qTpcAvQj_puARH.TKEU1CrJ9F8ArBk8r3gjC.O17E9gHqhWP4KFbkqf6zdwwWBK.k75RQ",
    "XSRF-TOKEN": "eyJpdiI6ImhsVVNrS2ZIR1RaTTVybnA0T3RjSlE9PSIsInZhbHVlIjoidmN4VzMvQ0w3WXl5VTJmd0Z2Y0I1UXNBWE9BLzRQYUxaUmRyTjRmbjh5MmlaYVlwdm0vQXFDZENMMndqbGVtOWhqUldKQmFCTVB4b001UGdoYzNTaVk2bDA0R09sVnJsQjdacmgyRFdVQWp2a0YxdWxwTlNMK3dSa2oyZWd3YVgiLCJtYWMiOiIzNmYyMjIzYWU5NDFjNjQwOWMxODNlMjBhZWQ1OGRlMjkxN2MzMWRlYjFhZWJmMjIwYTdlZDI5YjdmN2ZiZTdlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9tVjNSRmN2NmVuUnp6Q2Y4RityOUE9PSIsInZhbHVlIjoieU1vVlBpdVVpZmZyTUZwd2lNSFFkTnRoYmlsTXdSYldaa1kwNVFPU3ZWeTBHUVdMeTJIeEpEb1lTcVJoMEdnK05jQlFmRDJMbXZnRCtBZnpNdEZmTTExVm1vdjROdkkramFDaXhkaFV5VXd1U0oxanhDeFlkUVp6Y1BBZ2toM00iLCJtYWMiOiJjMjFkMjE2MTAyNDA1M2JkMTE5ZGJmNWQ4MTk2MzExZjM2NmI0NjNjYmU2YWFiOTRlYmU5YzgwZDdlMDNmZjNmIiwidGFnIjoiIn0%3D",
}

