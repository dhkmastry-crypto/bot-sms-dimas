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
    "cf_clearance": "C3V0XvUMewX3E7X5i_GMajr04OMVoXMlEjtTEWdL48U-1792026485-1.2.1.1-4ehMAcO31vm5l_oCCICnMb5rox8tJS1et162TXGXKzfbTLdp1kzf64n2XhO2ib7.I5aQx0ySeM2xo9lYuJyQvBvLGLaAKCLqiXRF9QLtDJ4xfytv_vB41pZ1DwbzKXTraewb6xbX1z5rZYwppcdtWgsrpAqg6keHz0LSon_NZ8FdPx4PXZvLDQKzWxuuz1KVU3oDw_P5TO1V2bxSewxCfYRxE2e2yLkkSWqUSw7L6sOf6D2Q_Kb3yDGqlKrx3EBBk386CUz8.aEJiJ2uIadH9QKt7qW28KeVk.DfrF0QxxkaKzv1_5XMAcyIZlFbD7z8.byAWqFVVNe2UvcEkxsq9IS8FGsvVFANShDWJG6ob7qapDnZWJyNDDy.cXm3xerCHNTYVkhbuJ4uG0QxCd7befgxe1qAZR4AGxbGekY3wdB2DQX5GIaYlckagNudMwn9bqWiGO0pAusWemm7KHyjp3vVSTZGJ7mOtuypmOfCIPy5RxRR8XexJxiHlFYas3kTWpSqrH4q75xyUHRxkBQqXA",
    "XSRF-TOKEN": "eyJpdiI6InpzYjB5cjBmb1VGM1FFUkc4ajlVZ3c9PSIsInZhbHVlIjoiSUZjRUNVYzl0SEpBOGlJOUFxSXlnVERad3UxeVZJTW5NM1pMVG1lK2lCeGZnZUdrQkZ4UEhKVDg0Qy9oTDZ1c3RWLyt4N3AzdVZUWkpmbnc2TDExZEpBN09IaUR5OGlqQ2lHdjV2ZFp5UnNrMVk2dTVpSnJZY01pV1VOQmFhWisiLCJtYWMiOiJmNWNjYjUwZTYyYzQ2Mjc3YTc4MjcxNGIyMmQ2MjgzYTZlNDQ0OWM1YjkwMGYyZDRhNzg4N2Y0NmIyMDNjNTIzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlZ6dVQvS1BVNWZIU3BPYzE1QzFxSGc9PSIsInZhbHVlIjoiVmNrTEFXcmRNVFZrYVJlS1oza3RNaStKMTNxY0VTNGczZ0cvNk54QXFycXBjQjJBUnBRQ2hrMzUvYk4rK1BIM01JK2NOZE9ac3h1dkNwQVpCZHpwUXcxUm9LbWlaRjNML3dkSTBydWdOamdsZTFOOCtIajRKTzZQKzhtZzBGM0YiLCJtYWMiOiI0MTg0MmFhYzJhOGFkOWRkNGQ5ZGFmZjM4NjgwNzhjZGQ2OTBkZTRlM2VhZmEwZWVkODdlNDI5NmI4YTg5MzlmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "nZO8VRiP3O2socgVvX24z9sp9JmAiv1IF7ydh2C6edE-1792026475-1.2.1.1-PMyhu_8r0NW.soUxGplwgXhgjRUNNZYnMxVZJrp6NzO__h3KyTiR1dochDHHvpePt.HsO22q6k0N.sScBWoJdAyQFRMn0k38GW0.A2mwH6o4AkSPep9ePBKNGtScBTwpcHNZvQD_HYusoYaDtcKrl5FAYeyo2AEl.poL6.HJ4UCVRDpMb8T7_OZHRp88HU.G3GXvZdZAH1Wm28loNkGlVxxsyRmTuiIchZuRGiSvet7xLnjXkD70EqSWXQ_g4N4k342C3YHpv6obYDir3Z8b0YEOv6zKoRMMnt3KnADXP4aDrcCxQPl8cgf.D40e8FQpLcKZi9IlATr2TpSkoqA5pm1ou21l07FbL8dULv7cWCqauzJ5OCcK4fMzI49w37XRsGW2sd5MK2sUkzc0D2AX_xj2hgQ63YfpJ0BmjEDwBg0ja59bVQsUfyYmHeIiJmAeX6io7eHCPk3yj.De8kGDUBjtx4ok1yOFkqUYAl5cjTktOM3YylSitKPfRMYzXnAB6CAsO3qTiNOQ9h798cCL9g",
    "XSRF-TOKEN": "eyJpdiI6Im1zWGgyWGhXRlUrMWlyYktCaTJ4Rnc9PSIsInZhbHVlIjoiTVFUek9iYjRQYjBvZ3g4WlNHeTRRYnJ3ZVFZbjdEdVQySTY5NXB6WEk5aEcyWmpmWlpqNXNzelNZMXVOOE1ZVDh2eHBERWE0Vy9EVFJCaVNmdjRtQUdIVURhU0ZSbUl5S2piTFpiV05FOHUxaFJ1RHdRVFJCR2tIM3RSNlZldE8iLCJtYWMiOiI4ZmI5MmRhZTU5ZmU5NmE2MjRmMmY3NjE2OTRhNDAxMmJiMTRiYTU3Yzk2MjA3ZmRmMWE0MGRiYmUyY2I1NjcyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZIbC9CWVdiRGN4bGM0ZWRCbkdHWHc9PSIsInZhbHVlIjoiSW9nT0NGME9YdUltcFVNb1BqMzlnblllMDFTS2VOTGFDVk5PTmlZcjRXL0FlY1RwQm1XVlBHMmNHc0hFUmJrQXViRk9LMU1KU3pFczZNQ0t4dThqN2o1dFZrZkRlODFHMUhKbElCeWFNb3hiWEpFOTRPSnNoaVBOU0NMSmZKWmIiLCJtYWMiOiI4MTRjM2Y0M2YwMTkyNjMwMTNhYjA5ODFmMWI5YjgwZTdkYjJkM2E3MzZjMjBhZGUxMzBiN2NiNDAwN2ZkMGI3IiwidGFnIjoiIn0%3D",
}

