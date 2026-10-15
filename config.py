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
#  AUGESTEL CONFIG (https://augestel.com)
# ────────────────────────────────────────────
AUGESTEL_ENABLED = True
AUGESTEL_URL = "https://augestel.com/api/v1/iprn"
AUGESTEL_API_KEY = "sk_live_FacL1Nd9nZLCYUK317e456JPVEZaNnAGlwWXY8fS"
AUGESTEL_EMAIL = "saputradimas0878@gmail.com"


# ────────────────────────────────────────────
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "K0SZv_vBMyS6TG4k7VZgncYjCkIY4yS4zGRNDDAPQNQ-1792033737-1.2.1.1-OZduStnH5pvqAzERKRGH2XaFhsJWJzCR4B_Y97S_g9dVP1Yag.5D4jclNZ.LrplDHrYGzIIC6KPkqbEH0zfm_ajlj9P8Dxyz9i8dGPhQKNsVm9AhIVUF5hzft3qBAikrEVhEstMNRVJkFw.b.x2mh4LsOam6RUlTVcppCYQwK6xkyZIj8QNjJQ.ufYKiTtOGLxPC5FNnlgv_5TuTSX_0aBvQJ27osVg2JJCLUo_gKCHU0pvo32VnIDblj15zQZoQp9eppSUMN6_VCr82SXjl2f_J7MTbJoWyrr2ej_gQLckXKxc_dLV799ndIGWH7q1XfZ_j3GVxQsejhTLcUwP.DqqT3ZNd84pnoB5Zhtfc45QvKDga0jH8s8h4zon7p5feCIXFaTv.21BtAXtITUpnlh_RhNbHoRwuL5hLDTO_HnEBwMED1.AzJJm4EHuefEO8gfnR1xM6MB0oGzOYGUHPaVTQQDP236Kd4IP9N7dZG5F7g8iEBgZKV1DbyX1B7cgM0fZsif7m4cba.3sMAXxlsA",
    "XSRF-TOKEN": "eyJpdiI6IkVXeTZUcGN2N252eU4rUm9mTXVscnc9PSIsInZhbHVlIjoiZ2VsNVgyM0ZKVXpaZHdsZXBDRjdnQTlQYm9YRDN0M2piQnQ5Y0tRb0Q5K1ZJZUQ0bXk5MU9kdXpzaHFCSW9RVDVEOHJuWTNrKzJMbndEV3JWV1hxVzkzbzhzV3RLeEFOV3lhS21VQU5SUTM2N0RHNFEyeCtEbzIvdm8zN0RObUoiLCJtYWMiOiI5MWRlNTAxMWViOTEzODc3ZDI4M2VmOTU0NGRlYWViYjk1N2I4MGYwZTQ4ZDlhZWY1NTVmNTExZGMyYzdiM2E3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImRJekU5WjQ2YmM1RHh3ZnpkZnhZd2c9PSIsInZhbHVlIjoiQVNLSndlbDJPazhSSjZQMEYzVkg0S0ExZnhXREN0aXBta0dkTEpGK01NZUpmMlBIcW5kUUxGTVJSbEhqWTU1c2pRcUdGNEtQUWlNZjQ3cnJHZmxxL251LzhXMmkxc2xrRFlXbFhIdGVFZGhNRExUZkgwZ2tYMHJKMGhzUjJtaUwiLCJtYWMiOiI0MDA0YjllY2U2OWM1ZjdiM2MxNmNmZmM4OWYyZDgxYTYxOWQwNjBjYmZmZDljNTYzZjg2MWY4MjgwMTUyYmU1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "FFMaeqd4.CU2Z1q7_YAP9DNvU.NgAPcpnbhzwqCsR0Q-1792033727-1.2.1.1-lronqYhKADTrTRze7NF9Vgp_GfMY6D28mAiWOdjBYo39AsXWtNEuGVimLBGgd35ZB_3Blgq90NF4dKuSlipTlfDhYfX4r_5uOiEql48ZZWYBz.0Y9gqm0cKyEhTP3IEUCTZHshtPnppUMZUHs4wq7HVBhu0hqfdobPQicfE5DXsWg6VOqVegzaFRUNFizxes7wwweP6QFi._08c6IGYApu01_2JjE1SWNEzIqo_zCLn8v2Bwt8GsJkHQhjessUeXpuPFpUm.APIUSBpOtAA2ySvf_smtAU6eAvIJxFi2XiPE_EfqSUftma9IhW0QGLpCS3F70AkbF4phdjyVJO0W7NK4d_NWSplFt3q5s4Jx2sB8AW8eOZuHGoMnKzS_m3jbNrfUBwVXnamHuZDA61DlSmlKWUIugALCrwnlgXnkr01mKlLlxTcVMfmdKEbu0g.Co258BcKKGSCk2j2jFaYnhDPDUBJYDfdS5mgp_.xIHd958bmcOI7Jrko994hcEqJm6RmgM3r0K5WGVqqhIZGcpw",
    "XSRF-TOKEN": "eyJpdiI6IjVaZzF5cU5teWhybnQrYzl4cnltSHc9PSIsInZhbHVlIjoicmVXalpuUktINmIrb0N0NFJ5dGg4Ukw0M2NLRldka1dBUUZCb1daTE8xaTF3WGU2blNsSzM0ZzAyODZ2U1BmbGs0QVNBRkgwTUQzRmNUVHBNdEI5dW02WUlCdzdCWFJZUlRCWnBVNkZTMUZCbm0zMHJmMjI3SHZGdHJ3eGh4SHYiLCJtYWMiOiIxMzA2MzA0ODAyZTBhMDU5Y2E1NzBhMmU0YjdkNWIyMTY4YzZiZmEyZTIyZmIxMTRhMDgyZDg4NGFlOTIzNWRiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZGbDNlNjVkblgzbGF5RnZhVTBLZ1E9PSIsInZhbHVlIjoid1lBeVVEVm9JMG9mdWg1eGlPSitiV0NxS1pCenZrWEZjaUpQdzVmTE9DeXJFNU1XQ01CSWRnb3VoRFhqRXZKbnVMb3ozdU9XazlDbHROS3VrVnpBSjkzaWlTMmlwZjhOSWxBL2dFcnY2QkhEYk96VFRVTHIrMlBoaHFneVBYZlYiLCJtYWMiOiJjZjY1YjBkN2JmMTdmNjRjMDQzY2RkOWNlNThkMjk1MWZhYzMxNzlhNTdlOGRlZjU4NjllNGRmN2E5MjY1NzUwIiwidGFnIjoiIn0%3D",
}

