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
    "cf_clearance": "SDPpCnPoO8w.0.BftoagTRz1PFUG7qFEUmsKbJXP48s-1791838499-1.2.1.1-GESOtRiOiTbQ4h40Iu4RGQQiHSzX7D3T4mmgr0yas_jP5.ygBJ2EsWO7roel5N3Yn5_wlN.dX658.aMg4PJSOMwKz6MYu2TcB.IZgMQ19tSsOi.lH770qtgVnpeMk7Y10pwJEbSHasbplPn2c.c484OCDnzeyXbKul5qcWnyoPVGVkx0oM9gIMEOp8aDgGsJq0.J64R6vxnXiLHO_BpsAA56hcjIlUIEj.7fWELkQkMZlkWl0jdQ1Zfos6286tyN.sQs8Ixt9c.sTlQtqQ7q1HY0eyuTVXuaDoV9P7jSeYImIx_nHE49pX2W9vsZxWUdYJDiLaupRaw91.BAG2aKpibATI.tZWKRQ5i3.W850q.TP3BL1xP1SxVFUPaR5ewgn8Sz2Go7Ba4ist6BqUcjhgaLWwAuWdtWi.CjPvhhfAC2UMDjLyM6S1mFGHU7I40ch92x73MyCNpnq_RTdsu6dOei6bVvuOYllsYQm577MGg7eaRr7ASGAobAeWYfcPOMco6_2qfWmV3_PERI2IS0ZQ",
    "XSRF-TOKEN": "eyJpdiI6InZ5WlpJdXNtT0NXd3U1M0FnYi9YWUE9PSIsInZhbHVlIjoidlg2WktpVFlPNW5weXhrUXR1eTVCSm9aZmVIM05FTVdwQmZyMGJHazd5SnVCVmhqT0k3RW04cW9DU1lzN2VmcUF2MHNuYUw0K1JvdWhpZVBVTXFKcXNrSFlWbUZaei9xcEFyTVBtWGxLUVVaVHNLNzN1QzFwcXdYaUxvWjNZNlMiLCJtYWMiOiI0ZTM4YzQ2NmU0MDQ5ZDIyMTQ2MTM0OWI3YmI1NGFhNDcwM2I0NTQyNjRlYTk2MWJlZjliMTEyM2I5NjEzNDNiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImJtN1RXM3pERS92NzlzM1RTbUdOYmc9PSIsInZhbHVlIjoiZENCRklka0tnVm5jbW9RT3R2MUI1Q2phNkJkSDM1Mk9xYzFyc1c5eE94aUlWbCtwdjJRUTZqL2lsSXlCbmZoR1BKaGt5bGNXSTErbXY4QUd3RHE1Q1dhZW1WYzZ1YUx1Z0wyd05KRWx4bkR0T0pNcnBoYWUxa25pRjcrZjFuckIiLCJtYWMiOiI3YTM4ZDAxZWFjNDkzOWI1YTU3MTg5YjE3Y2FjODRlZDllZjEzMDMyM2FjOTk4ZWQ5NmQ4YzVmNTBmNmQxMTBhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "WGv4n8FPVKfadpB4s9zWbwRym7RmWyr.xH_BfYhw6eU-1791839467-1.2.1.1-0gAQ7noyXT0nvEZK8bqrYKq0lTdwBzbo4pYx.x2aBVAiR0rOLnpwWd4Nd0duaMng9FW2mOkSmAV3CxX1t6ClnfQ5fOuBcu5br0wiA7R1RwKws9HxHY7lk68QK8U7BvxPmeFB6hPsN3zoCbqjtZZAGzaKEzWWJJJji.weWx9Nsm6oL80GsbIlVyHJxDUPIl2GCQOixOz9Cjz.E.C4j.MN6ZK4fbz1wrNbBxbw4Clcl9GLVess9VvkGCxqDp2R9ECgGs9QIGRbvLaQDXCHYmehjRPIoCjeEy3kFGERYBhPZXTZh1Bqx7LkovgAWVvGCk.NgrXFSwbRkBjHFFl_WCqO.vR1NbLFMPTTlwRfZENT0A7irX7nH6ytBdgYTTD4v3SIpOTxqOMaIa6dCLcuMNwIbQJrVs25dGEp3OaI4T9END0Y9qOjhyadSXYzQlpqmhAjOIHrQVqCW4AEMidG4qTpcAvQj_puARH.TKEU1CrJ9F8ArBk8r3gjC.O17E9gHqhWP4KFbkqf6zdwwWBK.k75RQ",
    "XSRF-TOKEN": "eyJpdiI6ImhsVVNrS2ZIR1RaTTVybnA0T3RjSlE9PSIsInZhbHVlIjoidmN4VzMvQ0w3WXl5VTJmd0Z2Y0I1UXNBWE9BLzRQYUxaUmRyTjRmbjh5MmlaYVlwdm0vQXFDZENMMndqbGVtOWhqUldKQmFCTVB4b001UGdoYzNTaVk2bDA0R09sVnJsQjdacmgyRFdVQWp2a0YxdWxwTlNMK3dSa2oyZWd3YVgiLCJtYWMiOiIzNmYyMjIzYWU5NDFjNjQwOWMxODNlMjBhZWQ1OGRlMjkxN2MzMWRlYjFhZWJmMjIwYTdlZDI5YjdmN2ZiZTdlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9tVjNSRmN2NmVuUnp6Q2Y4RityOUE9PSIsInZhbHVlIjoieU1vVlBpdVVpZmZyTUZwd2lNSFFkTnRoYmlsTXdSYldaa1kwNVFPU3ZWeTBHUVdMeTJIeEpEb1lTcVJoMEdnK05jQlFmRDJMbXZnRCtBZnpNdEZmTTExVm1vdjROdkkramFDaXhkaFV5VXd1U0oxanhDeFlkUVp6Y1BBZ2toM00iLCJtYWMiOiJjMjFkMjE2MTAyNDA1M2JkMTE5ZGJmNWQ4MTk2MzExZjM2NmI0NjNjYmU2YWFiOTRlYmU5YzgwZDdlMDNmZjNmIiwidGFnIjoiIn0%3D",
}

