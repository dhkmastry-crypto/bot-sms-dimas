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
    "cf_clearance": "zovZqTN_xySPebQVfQh4lB7c5W4qRhZzaALDradTYcc-1792079986-1.2.1.1-YCGnE3cCPEk6OKUTs7EWspU04mbd9AS8Qu_ynSVVp8FHoutygEHcqvpB7NFlwW3r9PcgthwxrH45bxQZYVwfv6Kx4GqQQtvlc2qzE0HTxtzU6yS4x6YdA_Ur.JHUSrjqfOXIy_iBF10JmNQumytJ1lQ8RY5UqG2wCPby4o4ZOVQVQYLc5URXZzd3bmriw0LKJktfYqXCJBlwjlSCzSwa.fsoYsiYobLraiL.Kbz94VCgm6vcvHxd73kx7QO3WEaAf173YlbuRHQL.GjODgQylKRXfS_3sWfGAZ1Ojnx85GF_HSF0VUQSmwrLaRzJ9wKD7IojXoKvFOsp9Rrz3UZ0JOQwIeqDaPixZbWVh9w0xe81dq3Cv98UTO0pRFrrJ0RV2Bw.0IjRXhAguQPnB_tC7DSlUAujybf_.wP80Ai9VxnRfBplLiqIwi24Ata51f_M8j_uz85pxDhV.2Hh2FKdpVzKsSQHdKWwPsy9w6RgVCHk1BdqyxjyXz3GU1wHt8G2_Ru0OuB.iUZ0zis6BwvqXA",
    "XSRF-TOKEN": "eyJpdiI6IldnYVA5eTRBakRFaVBhMFpibVRnMHc9PSIsInZhbHVlIjoiaEFFUGFRbmJ4Q3FGZ0xqSUQzMGVtMGJLOEQrcEtlb0dOSm1OT2lHQUFXV285MnpuS2kzVndKSDUyTjVSODFJQm5WeWQ5RFl6ZzJUTHZGc0RFWjByNU0xQkI2Q2d6ZU5ML3NwSE1mU0U2emhxZy91Qkdyc0pxdjEyeWZzRm54SU4iLCJtYWMiOiI1YjkyOTcwYWMyNDZjN2ExYTQ5MTBlOWQ3NTI3MjYwZjRmMDczZWNlMjkxMzllODUzNzY0OTkwNmYzYmQwYmRlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImZCWlJCVGYvOGJRSUpDcER5aVdHMVE9PSIsInZhbHVlIjoiK0tnWkRRZFYwTGRUQ2lmL0VNZFdWbkJ6SWhObDFvdERaTjhtREFJMGdaOFRjQTdLb2FRbXJKS0lrY0plc3hxZ1IySGlvM3FJVjRKYmFCMzkxcUhNcTNuQ0ZBb0ZmaXBHeERaaXNFdW9hQ3JJQzgzeHBxTEY2UlBtRWhURjRGYU8iLCJtYWMiOiI0ZTZkZjU1NTAyNmM3Y2NiNzRiNDNjYjI3NjFjMzZlZWYyNjc2ZWZiZmYxY2Y5MzdhZjYyMGI3OTg2MjhjM2I0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": ".m3VieuAeYr3Y.kH9n._SMG9Eyt3eR1Uo3d1na2mNog-1792081752-1.2.1.1-aDShSojseExKoxmxW8.ZiuXUWbnSEel_QQQPuaa0kZoxClYmZDxt3a8pJDmLmrT02mt9DvP0uJjRQtmQm1O_09uAZOt_M4.Hbizhw54ZF96jyoC_JH.ZrGt_.9EieDmywVrm5VtcMXLdOXixS6zS7GLKO3tlVtBNGNgNs81ryPHHDbm7LDFE9qEM_PIG8_PWKspxWQCfDHROn9MgQhnVipcIorvppN9qHuMo.TrzxBHruySyN46nwwlQjLGbw2LQNxT1e4SFh4pqJ2O.zCOqWTbaAFdbI_fi9LxQR41.2Hm8IkqjPRgd4yRXevfnJ48t2R8bV5cn2vPgzKAqMb5pXW1y.Vsm.hMQExRTSizT3UEcc1VluQAw.qwH3owfe_lxmAqV3pcZysTfhco9zZxhR8SHwK6S3JDNLeqgsRjJQkgNLEAyp6JbSx2V.qDnvTHWfBCZRPTrV996qpMUngKV2EofZlK6.QzV1F2JtMqxVRfwEN_eKP1L_rsqE5NNi_Ckcr5OUmOZSIHRnt4FLkIkCg",
    "XSRF-TOKEN": "eyJpdiI6Ikw1YnRreWtZSDZzamI0aVdrRUlOQ1E9PSIsInZhbHVlIjoidENOY2Q1WDcvMDk3ZHZkeldtK0x6elVWU2Iwd3pVTGlqZnNGMlE3UjllRzIxc1BwdENzM1lPYUQvYVdNTE4xc1pVY2pwUm8vVmpkV0w2NUZkVDhTbjhPNEJaWXZTTzR4T2Zvd3JKMlAwV3pYZkhIUWRrZ1hRUFFUQzhkSzdhOEIiLCJtYWMiOiIwYWI1ZTZjMTIwOThhZTA0NWYxOTY3ZjEzYzU1YzBhM2JjMjc4ODMzOTA0Y2ExMTllYmVmZTRiMThkMDVjYzFlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im4xQmI0TkJWWVUxYjNQZFlOcVhKN1E9PSIsInZhbHVlIjoiY2VrTitybTR4VUNaSHdKRzNaSHY1Nm80RDROZDRGSGxCZWV6MktVaTczUm5UcWx0OFRCbFIxaWpFQWY3NlUraTZoc3dVZXJTdzl5bHNQNEtOTy92UGp4Z1hseUhmczJPYnpsMmx6SWEyb0E0ajdKMWY4bGxSMVVLcjdRa1lIOVQiLCJtYWMiOiI5NWZkMzY1Yzk4YTgxYWY0ODFjMWFjZjc0MTE0MzA0NWQ3ODIwYzkzOGQ2YjlmYzFmZGZjN2EyODIxOWNmYjM5IiwidGFnIjoiIn0%3D",
}

