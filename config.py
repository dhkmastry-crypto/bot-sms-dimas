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
    "cf_clearance": "qEyixsqEeLOp3x7NfKyl6BhNr0IDobGGzgU14JUceTs-1792139820-1.2.1.1-e3Pxg5jTmhQamR7035Fy1QxTgmalIITHTE_Kt6UaBFeDVrSRHsVlYvBXOT7j4B9aJkp_xZS05500W0s2TI3tfWW5fJYzJUc7FWRWOQoqqW7zJcnrHn6iPgOAuzgToEs4ip93S3Bh31KB70RXAUKZZa9ZtMD0gXnpXSTFMAXzwbvNPq81ryFZMLF8.br5KYpHMObnOhnkctMpQFdiLx.pgo1t4HJFtnqoY_k7emwU1Zdja9IRj52GjLaYsd4OZfNj8xo0qHqH8tvOPHL1.LuqvsvJSURaxDUSuAYBZOVgUFQtCiBfbot64r5Z2hmfSWW72gs7lD_ytyYgeQFxW8o6lrTSZJQlf02aLRtAQyxcdGOjJCykt8RSanjRh2WizmC9kxCg_6dzys1SdqZosMkZCgSx7YXXAyRwPtRLomhmdLSRLKOJFLtWJvyPTSU.BH2mj4TDar7307Ue6S34Uiw9HqE2eFwsJGp45jMooGSyQTfg0AnppW1.RemfdFObBNUTgFXPcQQ_BWc0gtdQwV3E8Q",
    "XSRF-TOKEN": "eyJpdiI6IlBjUWc3YWVWNDNWNGdTdmRZd1VuUWc9PSIsInZhbHVlIjoiWW1hTlR5TU5ldngxWXp6bURiRUpQYkxIUlVqT1BjWVU3VDVweW9MM0ZQVnFIdDczZUpUdXJsdGZkL2E0WjhHM0RNQ2ZRdDRFQzNsaGZqbFFxa0JBdVgzVXJ3Q2JJVDFZdGU3a2ZnbCtWUmNlbkZCM0RKdW5udFErSm1CNllsMkQiLCJtYWMiOiJhZGU4ZTYwYzJjMGIyMzRlZDU3ZjFhN2JlZjRjMTUyNmY3MGVlMTM3ZTBhN2Q2YTU4YjUzZGI2MmY2MzdhYmIxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikl5MzFhL0JtOFNGb29RczJvVjlLMVE9PSIsInZhbHVlIjoiWTRlTEZQQmxVTEhXcnJRakdpWHJwZ1pVdFFvNEVhUm5nd1BMemhtNmhWQXdMdGFXbHM3WDYyTWJ2TGpBY1NCOS90MlJFRFMxRmZOeXkyMzd3bU5qVSsrUytTVVJWVnpSbDZZV3g3N1BxRmw1Y3Y5eEtYVTBjcVpScjhxbEEvWjkiLCJtYWMiOiI0NzAxNDUxYmY2YmJiZmJjY2VlMWUxZGUyYTdkMzNlNDJjNmQzMjc3ZDQzOTZiODRlZjI5MjQwZWViNzg1YWJhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "wYKihnOJKvueYJLwSCveCR2mJFUlj_n7AnzMLhFyg4Y-1792139831-1.2.1.1-B14TsDYt1BZODI0sTiBcpHQHYl8cxbmJrpo2EtJtriPoLvQA8tqcehzjWo6F4YSPfO7jvBYirhnNmeorEs4OKgS_iyM1j33i9933c5oaEHxiN5GXEYS7QOgnMNJ0IFVjNNjEH4Ptj5sgtQufKhAey3D63b3vabk9ceQ5cNqPy1lpIct7H.mzs2IuTsfUuWosR9Kl7Q286VGggHSlMX6GRb24Hu1gQ8gLXjtd3oz8gPPkUMJvssRRcQqEPx0s3ccxQk8v9Lk6Zi8.4_0InCWw3nPMSsKdJANMfQd4Ccam7RvnuNIVouTihGMG53Rm.sMVQWwE9sE88UrfT4_HWgVeextpxhQqxtY0i2liMTWVksOtZAq44lFJmk9DRuccIvPJvWBv7di_dYCnBae5pTo61j73My6O0Ut5yV0Asa5B0PoLHIMzEUDgf0HXxZ8iH1iYM7W0hn0mm_53CKeRLX4qKsNOeXVaDM3ZPG_XZMxumeN_rhX07Arr3QPOVzf0YwFYYELiFAhbWxb61yQI.c10Cw",
    "XSRF-TOKEN": "eyJpdiI6IlJNVCtERk5RK21CTE81MDR0VHZXY3c9PSIsInZhbHVlIjoiYXN2L3J4YzBlWC9HZDViNU5CcGNST3ZjWXRQWnFFdXRpRFp4b09jREtaL2lITVlwR0FxRUhTeHdkL0dmQlpaQjYyaVd0TTJWcTRjd0tIc1pVYkIxcWgrQmtTVzdGWWpqekZBYW5pcHQ2NXdzRXhOTGZvbTc3WkFmU3B1TXUyMU4iLCJtYWMiOiJiYjRhNTRiYTI3NjQxYzI1MTQwZTU3NGZlMGU5NWMwNjA0YTQ1ODE0NjY5OTNlMzUxMmM2ZjE3ODE3YjExYTBiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImxhZW1ZdkRiWHVudHhRT3JPZlovamc9PSIsInZhbHVlIjoiZDlFcUQ0bFp1WG9yQkp0bjFZNlNBR3VMVzZNWVVKMzNlTHlxeXZ2UkVmU0xWQzhuYTlzQUgwOU9ZeENuWGtTbUxYRlhCa2dOMzV2WkJvUGR5QWY4QWFpc1VPKy9pTnBBU2ZpVkhkVWZJbCtJZlhQczhTcFpSVXVuUkxtZERiTWEiLCJtYWMiOiIzZGI0NjY2YmY2ZTQ2ZTZhNWNjN2NjZmEzZmQ4ZDU2YjVhZGNkODUwOTQ4ZmEwZWRmNjdmNzU5YzY0NTgxMmRhIiwidGFnIjoiIn0%3D",
}

