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
    "cf_clearance": "cThvGMzafvaXfBwJ1yG5cvd.f5_cohO_J6DBU5UFu6A-1792094477-1.2.1.1-OWJHXhU8F0T3EuHLHg_2OoHHQIEHFeuplvKLkC9Qr6B42p7HkmgyWY.O.QyRqWac61FuHcuxTgRV958ukSBukpFEIdcAgQZBQaMlbjVHVt6pqwZoR10quM4iDFjNqyvvFmc.1w53_347qLWHAZ2_DXWVdxWdMs6PHyN5_b0qKNOPkVuH9GkaM7dBSB6FxCgGq.avwP7yHUXBQC.YSAkYnvjwBNBJmuKvxcXh1FPM4.rHvrREaSWhAuXdsljL5KFUTPG7Uj_TuEoNTtk8n9EJLSnY7wYNEXw6kQy.K_v5Y1Cprwtnc.FgTFNuBSinJt3kDUy3htwrMgzvcy5O6iJdFMfXydgJPdulVVxkMOoF32tvgofk6wjjNLTgL99WgbYpZm8gMjmkVJ2tCYR7C14fQI0dE7gNz6V.xK_5UzPZPW5he4tHlV8zbhMArSgvC3wiI1BjDY2YX.AGoKVe7CZ5QT_4spIcx3KMReTH2U70T7Yp0acB1dxS0hvlJKh_RrJkBdm2K.NFskocIZ2AyxrERQ",
    "XSRF-TOKEN": "eyJpdiI6IkFDQWFtUTJ5S1lsR1dJcFZsaXBkdFE9PSIsInZhbHVlIjoiYWFJSEdXL0R0Wm53UG14dUhvSHo1WjZ2aGV3Z2NSTlYwcGJ2czBaUDVybkZTa1BaUThjb09CSWJyV3hNaGUvRVMrdXNib1k4OTI2K1B4M09ZaCthNnlJcHpieTJRNW5Ndk1iSXJHb0NGNTdOZGNzVHBzbUtaTjY5SkVMTWV5MDIiLCJtYWMiOiJhM2I1YjhhMDk4OTAzNmM0MmU1NDVlZDdlNTQyYzg2YmU0ZmVkOGRlNTliMGUyNmE4NzcyMmFlOGQ1MjdmZmI2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlF4bldpOTZqVm80OWtmSTU2YU1Ydmc9PSIsInZhbHVlIjoiT3JzN1llTmI2RTJ4UzRlZnZSNXQvSW5GOWoxMGw1UTFEa0lPQVp3Vms4a1lHdXNHR2Z4dzNIcVFKWDlkN2thTFZLZTBWdUNFMzFrd3dtTHhlRUx2MmFqUEZiKzFLR0NSNXRCWFlCbVRSTDI0QnRMVnQydXV0M3Rib2ptb0t6clYiLCJtYWMiOiI1ZGRlMDIxY2YxZDEyODI4NGU1ZTU0YjFlMTA5ZDE5YWJjZWVhZmYzY2M1Mzc4Y2EyMjI0ZjYwMjhhYjM4ZGMxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "q.oFcaSALjRILMzaXd0kf67bVjrVPkMOtzNJyHpgA38-1792094477-1.2.1.1-SSaR7ECFXYoOQxSWie7VVXthU19cu52CEp6GFteDlIWbp91vjDJdw1sNNgFvvX9.exiUH1LE86P6.bTKYydO36Rp8lYTsg.o5CLaeoTaZPfJg9gKVMQhuV1rCALJ7QAeQr0ArNveOJtrZVX1QmIV3bAF7gQL51W4gc1z3D8bXgYUaADPtrJ8J.OihOMYx2hdOtkzsEPqIahgcDoZiszVZGMzTdVC1v6xywJYr5StaXUuJhlYC0x7tDee.0x_4kON90f4.vXUthu4u7ZoXc.5LpQZzafBX4EdiTUvh301BKxLtBUuqUgBJLTbX8TVl8FqQu5ZiUZAQ_26rX3N2Ny44UlUXeMr87rKg7M8us9Nli13LcrmLOw8_CNCPemnil_ZhIt7Qh.uIyC02doPW0UxQhwo80nkwUmHB0GK87Mfsx6DkXGIg0zzDRpFk52JlYEEymR8UV7hHnTMWeR_tlWxphiGScO0TtTUr7feUvUEllQiIaq.9LC.EFLrB7tuZD8dYFMuCzzZrsOaRpAu0G891Q",
    "XSRF-TOKEN": "eyJpdiI6InloaVBNM3lsdEJRVWVwbWFaWUNTa3c9PSIsInZhbHVlIjoiQWNRdFU0cmFZdkxlYVNxcjVSS2pmcm80d0VvdmZMQzg3dlhkRnprcy9vOG5xQ2VJVjcyUXFUb1phc0FzUEY3Ky90VzZyY2VPN0trUU1YMDNwUjl4R3d2MERCb2YzWDZuZ2djYWRXWER1YWJmcXUweVl6Mi9tYVRtZ1FZRlBvZ1oiLCJtYWMiOiIyMjJiMjIxZDA0Y2ExYTcxMzg1NjIzMTFhOWJhZjcxMmY4M2YxMTlhZmE1Y2UwMzk1NWEwOGMzNDM3NTQ3Yjg1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVGQ1JmVTdXVFpwLzFwRW1JeE5nNGc9PSIsInZhbHVlIjoibTl1V21lZ1RTdzVaVjAvNWJ1NEF6TVBTM2poN0ZETDV0ODgrUlg2S1YxMC9TcG5jTUxzOWdIZk1EdG5ZYmZKNWdML0NNdGt6M2hWNWR4b045Yjl2MWM2Sk1LYWdrN01hRDVCYjZjQURiV2RBYzlhYVh6ZFN0SUtNbmRiZGx1NysiLCJtYWMiOiIxMTEyODRjMmJjZWQyMTE2YTRhYTJlN2FhODE2Y2E0MWQwMzdjZDBjMjcxNmI0OGU5MjkxNmE0NmRlYTRlNmI3IiwidGFnIjoiIn0%3D",
}

