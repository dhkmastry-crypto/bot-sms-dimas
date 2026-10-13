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
    "cf_clearance": "mzNCvWgySS0Ir5MnH4RymK3fmoOI4GH1Wex4SxcjQYY-1791881278-1.2.1.1-FDfkm3OuMlhYuqkfLJt5HobyWfbO_egYBlFITqXQR.N0w2JaL6JwC7MN6zE2ubw7rwosS51D_w8am3xdDXbhLYWR8o6iItl6r1s1kmWT4bNFGOK6LdkRz7NDSVp4oT1r6E6xgHszlz3krrVoxFYTrrmFfoQtYLxKmgjatuhFQY9qIMSdLK3tdox6fYJGew.uEkeAnDR3XGzYHIk8WzLeqiajIY1Iw_3Hg4LwPwfyDO1vg6tUZR1r1bx6Q.LPyl05m.2RwYuic93s5LZMeYpqOAkSoXr4KJ167lG.l_XMUZFsdow0_bG1vdNH2WmEI9aBXa1P6Vp6EoZ3jb5Pg_ktcbhq9m5SuLpEK3NUjfYJape7GtBxc4JkzIRoFa4.PiHPlqFuKk_cYst3vLpJXaWZpSYc.Y9esmWnKGO1dT9xdIjsOjQl6v35lcSmT4yZLCU1aCh4MGRlveCWztsy7qwnRcDN0hGndY78uhR.I0frzhnzjgVU9jRb4hCtc.4e6I8yZqxec45.N4NQxaDSkMk3RQ",
    "XSRF-TOKEN": "eyJpdiI6IjZVWitFZythbWhFMXh3dXV2b1QxV0E9PSIsInZhbHVlIjoiR3crcDltaE0xSWZlMjZ5K1ZQOWFwQkRaMWhRWW5VWEVnZlp4TW1kVktSNHM3bml0b0ZZalVuT1dZNDRUcmFBR2xNczRtQ1MzTjJpK3RKWGFTSG1jZW5RQVYveGVCaE1NM0dNYXhISXkwUTAwanpFOHlZRUR3ZmdJWU9pSmpJQnkiLCJtYWMiOiI2OWE4M2MzMDBhOWYwZGM2NjFlMjU4YzhjZWQzNDllMWZiNWZiZmFhMTc4ODU1ZmUxMzJlNzU2N2RmZDJiYTIzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxQMVhEQ2pZZjBzYldrVEdRU0tYNGc9PSIsInZhbHVlIjoiS3BuUGVERVpCQzJaQStNY21tVWNTWVBVL0U3bkgxbVZPNnV5bUZOTGpOUEdRMmJEYlZVT1ZXY0RYQ3NqNWhzQno1UE9hWG1YRnRJNzFhaHBxeWRIWnVxbFVwU2dKSmxpNjRBNkNMb3AxR0ZhNGFRVGI0emJxT0JPcGo2cTMyRzgiLCJtYWMiOiIxZjg3MDcwNTAwYzNmOTI0ZWYyZDEwNWEwYzBlOWViZTcyNTVjY2IxMWVlMTEyOGM5YmQ1MmI2ZGM3MmM4NTdkIiwidGFnIjoiIn0%3D",
}

