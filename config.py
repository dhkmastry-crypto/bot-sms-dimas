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
    "cf_clearance": "EIeIWp4l3iYPU4WehBaphGtprE67XFIeiX_cav3gbkk-1791962034-1.2.1.1-czqvgQ.jCcO7R_u6P7VJB8B6AWmlTsK0Wdph8WtCaa_0UHm.ZUyyRr8e.jJGgmaB.c2RtkNUBVncUb6aL9MrnE.LvW5PFot8mPwPb42woRxqHIe.cH6wUuDB63iM6IDGEIsyxRNDF1EtZRO0GhRW7Qcskhkpo8LwNx.MWy9eQMMjroTZ3rZO6jHIch3DehkVbAE7HlMF0QBVX.sKV3n6..Xha.uq03Pzyefvol2o9OiTmb..3QOgEe8ePaCzi5N5jw8xG6vdzOtIbC0sfcAKk.LYH8Dem_YpX3uoB0Av2Q.RlMly89MCguI1la_mHJ5EONvBHEnigJh.KK8CKK4KQINfcuUchdnyEvPMBgvXg8F.lo2STLWMg_i.d2siiwGgSMYgIkNpq.uNkr6FL7Z9U.zGvM3w3FBvSiujQwtzVWVw6hXf9eKImO9f.oPa9RTHL1lM9y0ShcDpgeubAGxsnJqbxbkuPWG.mfkz8KxIifQC5f0O0U9MqSTc6N5GiOXqSEpohMdFQ01wmG1rDdrQoQ",
    "XSRF-TOKEN": "eyJpdiI6Img1bXNlUlptTDR0S3QxZSs0L2syeGc9PSIsInZhbHVlIjoiWXQzL0liSFpjNlBBdVlmRGlSRHpHT05DS2locDlFNy9xNUJGbFBLaDEwcXBTOG0ybWl2Z1hBWk4xZnlFRVdUYWw4UVNIaEZCRG5xOFloak92L2xGaFFuZGxmckNubGJWREhaTDNoZVRsNk5EeEhYZTRVWUdPUHNuVGE4cmlKZisiLCJtYWMiOiJlYmFhNjgzNzVjNzZhYWQ0MjJlOTA2NTVlNjM3YWQ4OTI0YTFjN2FmMGI4ZTZlYzVjMDU2YzNjOTYwNzA4ZGI5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkwrYUFMVWNOQWVDSHFmNE9GTmZ1RWc9PSIsInZhbHVlIjoiRlA4ci85VTd6bVVwVVhGODZWaDBydm03OElrV1pTQktDTGsyKzJBTGQyM3d5QmsvenhRdGlmWWFSMVpONE05ZGZESllHZjVFK1lLbi9uSUpyTy8zRmx6a3dqNGI2d2s5eXMvWGd3am9ZMmdiWTNYd1JldTgzcVJLTVlidmJPUHMiLCJtYWMiOiI3ZTk3ZWJlNzAyNTMxMDBlOGYzODM0MmMzOWIyOGUzZWIwZTFmMDg0NmUwOGNjMjJiOTVkZTk3OTY4YTJlZDg3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "D43dfenxtZ7QFwgro1_GqkKnhB1QaAZJbTX5a57r1Ik-1791962132-1.2.1.1-xNIYgJa.AREzHLWm9l1NSqwkE4A_Vojb2y.2HI_mYCqsmxZe1Xhg7C0BGpVFohRLQs0lyT36FqwU22Ydi2qxrHjsN2yhCjHl98HgFI8LCvip.ieI6UQcwqxqrPTbCOWyzJkxwqL0tYcBYSnKYBKJlJEiYmNuMgNgFtD6uxwX.ByM_2PKgvRmsU7rNjAwroG9Ekh1Cg1ZSN1XpbB7yiQo3PrXSyCAvZ70c3cJ0UvoyAipakn3xCJod0.11WzrmEzntE0uNOwfRCuqgKlT0GvD6kiNw0iNczP695vVh2Q6BmVMJGl.gMVvnz1TEWkUeBfMpVLiCPf9eY23Y10Mwi8mV60N9NlEiFwffYNuvrW6w46Tay1z0C8.lR.qGCR9qJfKk8vqvCvWTdYYExU2ul.AdHtcDXPd0QzewtKa.02BdynnPeXmDiJHZsxl0gitac.XbjyQdB7HgZErtQH8Nk47YOSLFTR9drEKBtxVDQQFvJW5_ZB7Tlh3fSxFPpAY0Nm3Y89COUZ2VC92UJkDsLittw",
    "XSRF-TOKEN": "eyJpdiI6IkU3QytSc0JzT3g1dnhQbmVGY2dlb3c9PSIsInZhbHVlIjoiS1BWNURRemd0OVlHNTlQeTVneGJBWGdrd0FpQ2dLU2xlRjg2RUVGbkFHV05wZTZ4Z3Z3ZGU4Sk0rYXQ2R1FTMHVGL0laejhJSFNUWlB5TDZhOVIvVzJRM3NJRzFQbEs3M1dXUnhRbnZLVkxCUXcrL0txYmJmWU9jSE9UNDNaVnEiLCJtYWMiOiJkNzAyNzU2Yzg3ZjA4ZjY3ZWY4MTVkMGRiZTQ4MjA0NzI4ODEzMmQ0Yjc5MTk2ZjI0YTk3Zjg4NzA0NWZhOWRjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkpQaVNOa0VsM2YwOXJhdVk5QXNGVHc9PSIsInZhbHVlIjoiSkUyY1JvU2tzbHhQaHlOemYvb2RXMThQN2dkMHpEbGlLVU9PalNHaGVYUXp6YmJINEROQXMrS0s1V3lKNEZtRkJWQUlmWTlweWwvUGpaRjhUYkczOHZLZVZsempKWWgrNHY2Z3NyM3h5MisvTS82NlY5NUtqRUF4OWt2OUFKa1AiLCJtYWMiOiI0ZWExYzUwZTRjNjJkY2Q0OWJjOTc4ODBlODJiZDIzYTk0NWYxMjExZDA0NzRhN2UwMDI0NDA1ZmRhNjk0ZmEyIiwidGFnIjoiIn0%3D",
}

