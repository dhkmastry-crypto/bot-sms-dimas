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
    "cf_clearance": "ui7j14QrAAvsr7JrTRz4B7YyvMkn2mz6AlQI7WLUtws-1791894565-1.2.1.1-QftwJ_YuGUIi41ljaWjQdlgcfhi0mLj66uhFMI5lNN68ydHKJ4C.bD_tn.yCeo7O3iIbMMeca308tngKgNg6zR6bToV4MAWbPh6WHYlnmVo6stgeKzOx6XuIHo46XL_BiNZNmnc56H8Xh2tycHJmW02V0HapCPhj3CMnR_Jg13hdAoC8Rt0_N6nkHKwLtq2VG5sW1UOhEUlWGTvPPCXonK9Rnn9eOt_ARRKFgt4IIAYyr9acY8N.kyETl82GfCgCr3qdZSt.dlqKC5kRrZtJXDqiVBjHBGsuVuD4A97vXCH1tvFpJXjmukjJRBWwnD4O59_2SVd5P8F.TIZjZryyM4hy4lsZ4kmmonZTSbx9FNPbOaZW_McvPWCjETpqWGraq_wqtamPQfnFQha9YeePoCBwq1wul9po55lWxwcZbgozeWFWarwhMTE74uAL3LBNjD4YBYFkDcrcYsMVLs0yp3Wsmyfyla_mykOXHgTxJM5.NIr9DmtxK0RM6q5vLHkCQF2_lf8cms1jagBQhaT9BA",
    "XSRF-TOKEN": "eyJpdiI6IkJXdVZFQWhvQm5aSU1id2htMlZrZ0E9PSIsInZhbHVlIjoiNWpleU9CaDZuYVN6eEFod1Q1aTUxeDRLbWJZTzhFVGt3R2k3WWplakxtN0pyRERSN3VCS0hsRWYxM05lNFpmRjdvdFpoaGNaSG5hMUxFWmIwNDlsYmFMeWJXN2lvYnptbnNtKzBzblJPR3lzeS8xNWVoTXBpaEhpOXQ1YjBmczgiLCJtYWMiOiIxOWJlYzQxMDE2ODZiMTJiMTU4NjIxNjE4MTgxZWQ0NGEwMjlmYjllNDM0MWFjNTM3ZWIxZjBmY2NhZmM3YmRjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkpCMVNFazVNZ3dzNC9zZHh0MjExN0E9PSIsInZhbHVlIjoiV2huUzhNL1JmTml6WkdqZDI1bmZqcVN0Q3BFaHEyQlAxalVnYk9CSDl0NDBDaE1kUGZ1d0tSaE95UUNNL0h4Rk1zM3NYeENVOTZTdE15ZzR0NUkyRGhsaDFrVTVYWVFNNUE5SmUwN1crN1BVRXpvbGI0TUZRTG1OQmpEM1UraUUiLCJtYWMiOiI0YmUxM2U4MmRlZDA5ODdiMTFmOGY3NDIzMzEyYjNkZDU0ZTU2NGZiNjY2YzQ2MjcyYjEyZWM3NzI1YjVjMGZiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "d9hpJIzGTtnlFyOfUIev8Ms75QTPAisZnczsE7wAoSo-1791895754-1.2.1.1-fS.K_69EMAVvPzh1DF30oM5xH1yhfDgtaxvhTXkby.6zzGYwiis6OJ34wzHs8nJJahorTlwBhBwbuHfrjgZOuvHvkGmeKiuqUEH3VTz5IbxEigC4l1SxXn5PUKzCI0u4S18PsLk_1TYH5cx1UCImJlX8QSx63Ing_ZnMO1eSpkRMHoYyAPzq1djnMUJ0wFKDpn._qPMR0XqLTN.0Ah.5MAZ1KQJ1p1IPZwawXaw.ZfRu7lCHQ35bYxpqXEnxEMT_qyg8ZY_lcVlmYGN5948hQpUWGTVeEXRG_21pZv_OIvevFX15jOnJyhcYRlRmKNPuEYxKx_SFbd887DIl1NaCNez9yJbBdlgediOVWndRJV_6k4db0XzTTTgFNcPEKSyk78vZD2OhMPTdaYixyZda0ui7.0Eg37aDifS2pqCTTi7hX0zh1YaGFyBIFpP3x9amq_WRYyuefX704M4rlTAGtm8SsisYWJqzgxQlAWBRwmswBzd5hv.YFNxf9O7.0u47.iX.gI204fJSlyBvXnl_ZA",
    "XSRF-TOKEN": "eyJpdiI6Ikc1aTQ4dlk0TjdZMXQ1cmhSN2sxSmc9PSIsInZhbHVlIjoiKzdRSEpRTldYR3M3dTJLc2liaElQYnI3K2lkdnNZTHh1T0FsTksxekJ0NnNaenlXVTJkenZ3bFRRS0xnWDJGNTFIM0dNdGVqQ3hnTkZpMTZmRnlkNERwQ1RxbTFtelRSYnh6RmFDcVBZVzBtaEFlNkVLWmc4Q1ZrWmxEUWErZFIiLCJtYWMiOiI4MzAzODBlZmRmOGUyZTVmYWQyMmVhZmZmNjQyNjIwOTQ5NjBlZTc5YTRlNDRkNjhlZTA2OTM0MGNjMTcyNjc2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxzRjVxTEt5cFpXU0YxRHBWMm1GWHc9PSIsInZhbHVlIjoiZE9CeFhMN3JTQlk4US9xUlZ0SVBwYkFZNzhoU2hudXRCY1ViVER1UkFVU3Y5VDNkN0ZtLy80TkN1b1NubUYyTXc0RGdIMVhmZmsyOXdYZG0wN2xvNjcvUWJoQ3JRT0hYVVlWY3loanRGWlZzck1GMlFFOC9CK3REay9zcVNzM3oiLCJtYWMiOiIyNjY1NzIyYmU4ZTRjYTQxZTFlZWRiYjI4YjRjNjc4NDUyYWQ0NWMxZjA2MzBiYjcxNjYxNDZmOWU4NWMyNmY2IiwidGFnIjoiIn0%3D",
}

