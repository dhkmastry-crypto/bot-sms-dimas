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
    "cf_clearance": "kiIYZ0ip5abU8vJyu7mmNirRT2gAcLEmQWbBzgRP2Rw-1791956599-1.2.1.1-BIpbnp8lctJ.m3OqZ_m.113qYoRDuqguSIcDaf7mbd8rh.7Lj6DUU5ZwSo6UoOShQoFlEWRTRKQYHeQKLsgab9ZgZh_qrDt8Kf1VdT6R_klXGxJu1uTmVRTMU7KkzIvr2kvfSXg80.sEXifCYFg.t1TXLSX103Dz2gH5eZT.i.gVWlAru1dGVyu4MBqFRd2Nrr_hrus0TcaJU4FEBKgorYSzv1aT4Ixs_wOGomoM0h_7YRZcvGJdoByx6fTI1pdHkVOSCIaGqjSNcluGYvdU8DAaOKRUCvM9l1H8aSW1xzFK1Z4LicE8VsoU5VMrHpOmog1E7XOWLWxG.0MXUAyiLXhsT71wAu5HheDu9CI6xvAGzqmJUZ5hnJgf9C6JOcGEg3FyD9s_rmDK5E5wuxGLNPCzu1nT9madsppRg7bEAwauC7lPY5VbFxIfyoZGDGvtfx6X0AHwKi4qjqRGtdS18nwFBqVZTz1idOdookKkDP0EfA8rnIwNWXqfsJmdl20x1dWb0QfD7RbWhxrQ1aMDuA",
    "XSRF-TOKEN": "eyJpdiI6InB2YWlnN3NwV2RvejJNZjBZRm9WbkE9PSIsInZhbHVlIjoibG1tayttTTNlcWNkakZ5ZGlWWEg0b01jT0tFR0JEbUdPL1kyZ3cvUGROQjFkdmJZcy9YN0ljMjRDc2MyUVorWm5FanN6Wm1mYloxdWpNeTFMR0g0NEhtNGdabFNHYmRCVkdHbDRzSlFJcDlrc0lpVTF0SHVIQjdYMUhiSEpXb2kiLCJtYWMiOiIyZDM5NzI3ZWM0OGMyNWM1MGJjOTYxMDdkZGM2Yzg4YzliZDBhYWI5YWEyMWFhYmUwMGI3ZGVlNTQ1MDEyMDVlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InQvelBQdmhqbjdPZTdOSDZaeHg3bmc9PSIsInZhbHVlIjoia1I1U3JNaHV3QXFta21qVWowUUJUbjdNRTNBY2lyRWxXeE5wWGUzU295MlhnUE4xdDFnSkZ0M3B0eDA0RDgxTGl0VElqaHZhQ0tYWitKZEpGdlpZaC9YMjFndkt4QVNDdWdLcWNrUHpZUVR5TjhDR05BelNERmU2KzJuRTkxRGUiLCJtYWMiOiJhZjUxNTA5OWQ1ZDAwNWFiZTA4YjNiYTBiNWIyNThlNzNkZDY2OGI2MTM5OGYyZTI3NDJjNWI2MzBiMWRmOTJhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "YC9DO3w4iV9oP0OKy1mhfbekZomYhSVyMKyp7815NrQ-1791954883-1.2.1.1-G7wkSnznp4byPkzY60VGa89c4ZowaaVG8KXGYjSHBlXl7dq3tt_xeYvrrddxhm4zM5ZtB5txxk7.QQDsCH76.JzhDcuSO0sHB1XpG7_TRVS50Dd8CdVsUy_Q7FAVTkNldtqIeci7UG87A35_ttqYI5mp9fvpgXCP7m2LwQvaImeE74Bl_vynf49b2hc6Qbj3CtyQqSoCaFwbwcMSFi7KN1K1hiplcBa_sUcaZjUtZWQQR25hqCvTonzs8OTMRK9ewDe2REgqT4.f94FnPqhHWeKEFrlw0oE4RGovMB0RG6rsIsepeJy.u3OB1SVDXqZIPJicVFVK3_LPljinzvo8RPDk1583PuC6sbr7.aPBpBC7Xq_VTrB1iia5cn1Bx6wCMlqI6CH5Fpz_6ogsjGPdK2KTxxFqwiy02Ae18DE32JXRa3z32CJm3kP.XZiYF3VkNjAsAmImqCSnU3eZibJNnp8VSMdG8ITiCngBrrCfTHMFbHjs1a7Y2ePwUCVMlbhoNaD4UtQbRGnWCCKTmG4BmQ",
    "XSRF-TOKEN": "eyJpdiI6IkZZYmg3VVRvV0syUzUybENBOG5TRXc9PSIsInZhbHVlIjoiTDlqQ3hBTnFyU1RmVTZHTTBnc1FlTUxkdVV0bHRDRi9NZmJKYkxUV28zMlRSNXl2OW0rcEZGdlBZWHExaXowZWNpRkVFQ0lJbjRTRkwwTU03U3FvcjVtNGdiTm0rWUpxQnozbXdPWEFZNEFUZ0djcjljT0I3T2RTek4xaytxSlIiLCJtYWMiOiI4MjMyY2U0Yzc2ZDkwOWMwZGJhMmNlYWE4ZWY0OTUwYzBmMTBlY2JhNzRmNGEwYWQyOTAxZDhjZDYyMTEzODBlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlE2SnpQQjJEUGhlUkIyTjE2YnVzZFE9PSIsInZhbHVlIjoic3djWG5EcTZVY2hKU2ZOTlVUNW1IN3Z0Q1JiUEpQRUNuK202Wm1wdjJzRkIrSEZGMDFTcTAwb0JWS2VKVHR2RC9YRmtXdHJnZWo3UUdFOVlhTG1mZUZ0MFo3aDExaVgvb2FxbGtUNUFGWkxpMzBEM0lXYUZPSU4vQnFHbGRqa2YiLCJtYWMiOiI0MmYxODM5YmQ0ZmFjYzkzODkxMjYxNTFmYWUxMTQ3MTg2M2QwNjhlODlmY2UwN2YxMmVhZmE0MTA5OTVhMjU4IiwidGFnIjoiIn0%3D",
}

