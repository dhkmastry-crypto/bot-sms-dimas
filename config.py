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
    "cf_clearance": "5lYd_oiy4lNbDxE4wfQqQ7pdfxgyBDuOvp.4JctS4qs-1791881900-1.2.1.1-zP9bbG9forfwlz1jc4_LTp3tFM4Mg6tOCjK_JnZ.1qcD7.JL1Hu7XZ0l4RJrbEOrC555ZH0cMBp4UMFiHzRNE8QvbOBsG4ooE2zqGk.4zqB4WA_SdYJLhRYSqEjpim61Ly_PV7eHBhHS1mqzDa5jLlyT3pK7WqCrKR4YyeqvU_o04VO7E.X1Z8EBYfEsFi2rIvU_ruJyNoYngmvZmfhMHjKghZWtw8ctdcycgflggvHQTauBacK7ZeOQ6XBjtIE1ZkEgDGHI.f2HFoUddnVdl_RAGVh1H2j6OlFSaKOzh3FnJOj6uLfXlnc0OnD8BcIjEzA1tGq6QAkT406stfAdpmkX9NNM00w58HYyI2oVGi6ME9FbyL1nFFjUGl3SnlpeePoSY28WT9snsmhfNVy1XdVlzqW8xgpKg1tZBBukxRaiTDuqaKy2E4QpMJ8oDjwVbyfll5jueJWlwX.N8buKAJYtGt1YchPt7uyEFYSBZ6.9m39Ooz6k.sW5ETFKBAk3KL3ywHruPVQuOqnojmGyhw",
    "XSRF-TOKEN": "eyJpdiI6ImFtUHRqRlVGTHJMcFZta2tNWkRrVVE9PSIsInZhbHVlIjoiY0JLdk5sN1F4V3lnOXVUWlVwVXZFanM3ZkpVM0o0d2h5U0lScXJ4bXNmWUh2QzhtbWNmdll1ODVJWWJJVHpkN2h4MWUvMWx5MXlyOUcza2hlL0RpaHV6UVpSY1BVQ1JOb3A0OHFaaHJZcllmdXBpTHBGb2tORHVrOWZVZ1gvZGoiLCJtYWMiOiJlZDk3NGEzNDE2NzFhZDk3MmRjY2Q4Mjk2YTJmZWRmOTRkZGM0NWQyZGIxNjIyMWI5MTRjNWM5MzA0MmVhYjAyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InFMeUF4b0RWeFF2dUVUTk9XandCT3c9PSIsInZhbHVlIjoiVW5MRXRmSzdOaXFJdG82WUlLd2JoZFpyZjJMT3VHc1ZoYkRwU3ZGbUF1T0x0S2hVUEV6RkQ2Tytxc3pqMEhIUHlTWWlhYlMvQkdhLytmeFJVcGphemhDeFB1OWtSRVFJWHdVYkd2aDMycEY0VmtrSkU0NlB5N1NqWnpHNS81cnEiLCJtYWMiOiJkNjA5Zjg5N2Y2YWFkMzMyM2MwNzEwZWM3NmZmZDljZjViNmU2NDM2Y2YxOTIwODFkNDQ2NGI1YWUxMTIyZTVmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "5wvmp5cJS99H9RrpR515TPkB9RgeYVogbCKiKNdfh40-1791883090-1.2.1.1-ImZBfZxZfxDbuhDMZ_LEJx9v7bpmlOuLlyYweKXDNDsqUqDRq1lF6kR92hw.E57o5eOM87cgp0ggTN2ZRV5HVo0LcK1Uap3fn.TsbKpV5iV9TDw2RbisOL7HhT3uS6Cpw0gtO6F.smVsoSm_wrN2YXdb7VBxCsAMJ9YeAAFzfhdgURGSTlMAF_MfEhMbUlxplY1TRlfemcma0T5VtjLPhsRFgMg_2E6NlRC5wcIhIrtBObQP_jkaBJXjyUh0.8pmzT8ao02YGZi8uItUwY672h6bPCf9MRwOSC0zA98b3hRtwFGGVCsHrhLFJfiwU8xqyRpfzW2caot3oGqqqGo9lXvgIOGCeXD5bHOfqKPYkAu3cVgsSvd9KBX4gVKjZLEt.yVJLSqDRSQtSa2aJuO.gRAt__lqXdFw27.D0y960MyDtyKT9IHKz_0C3mDhxntzMQuph4iy4W1RwYGXEA_h8ARLbwuTSnPU5zd.jVSIrb5skKbUMEhxOnvP374a9FAsjD50CczMRfweerGjs0fAlw",
    "XSRF-TOKEN": "eyJpdiI6ImQxUnR3Ynd5TmM0MElSdHRZZS9Wc3c9PSIsInZhbHVlIjoiY0h3SkZ5TzAvYVlsdmxvdy9XdzlCNUR2R1VnMnljQmFSam9TYXZjVTNiWXExK0dEamN6U00yV3BZM2N0L1RJYVhENEZKamd4bVlhNFRzd0pibmJjUGFBMHZyK0dJdG5nNnM1S3BkdzRHQlJRSWRxM3YrdU9jbHk1NktkeUxxbnEiLCJtYWMiOiI3ZTgwOTVjYmM3ZWQ4NDJiMmI2YTAyZGNjYjBmN2YwZDk4NzFiZDM1OGNiNGQwNDkzZjAyZDFhMTcxNDU2OTBiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImFJVlRybGRjaWhOcUFySEl4YTN2QWc9PSIsInZhbHVlIjoiV2FCdnIwR25CS29zODFPMmlVU1FySHRhUXlNenVoZW9PYnpPRkxzeDF0NlJLRk9Rc1cveGZoZ3NCWVlPOCtFU3NPTzZNNUgxOStYcCsxN2NKZG9XVVlYNGt3UkxKUitHU1hwN2Jha25FS0UzVGNEVDlFTUhBZkJNVUZFcG1vUUEiLCJtYWMiOiJhYWZkYzMyMzQ0NTQ0YjhjYWM0YzVjMTNlOWFmOGEzZjRmOWEzNjVlMTYzMzY4NzkzZmZhZDczODczYzEyNjY2IiwidGFnIjoiIn0%3D",
}

