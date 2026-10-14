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
    "cf_clearance": "YhmcB.6IdCM3Iy.X2BXOss23Iay2agr54bM_3FeoaDw-1791940333-1.2.1.1-6COH5S.q1rcpO55MHPlGe0tKJgXMiFPaHBhD_XDRhhl6_xgx1HbSzTMmYaCm91OGR6AouXVTUCkv55F9atAOAy_SXg7uHPp.c5LF9HSGrm88bn5rumvlv4_nWjecjZ0amqdB6uPxYYggqf55ufihUNRjek3jFRjIbu8OMlPhWf8cISNMRHsu1gdNtQvtb840xcDHNHvSaWNa3h_dAhUqa1ZKdH1UT6AKYr3RujyO9DfraWKhsPXcEK6Za6whnVvO3okxM20Dfm0mWVqeEtIgNp06R97O80kgKsG9SoDrxG6XHCzw_4XpWun8gP.Osdv1USKXkW.VygSOTaVu.5JJewD1jSGiKZnrSf2kJ1R5yKzg1GFQLg0gvhmIxGrcRPXBmTdDQET9qYv8b655ISFyhSYhpHDIYNC8Og2wgc2gA4JjYLcyt1eZcn9jVxLVIWnv.BzijEXZOQ3KcaJ0y_AjUogvDAQItaFZyG4.rACGc_VCVBzlkVtN8KI9I.4oFu64NW0.TeLwBlTjTF51lvLQ5A",
    "XSRF-TOKEN": "eyJpdiI6IlQ3TU9XTnMvcWp5dlhQdnBnbzRDZlE9PSIsInZhbHVlIjoiNDhkb2xWZ1l5ZXdtWVB5Sk9qbVZzWmJBZ2Rxb3E5WXRxSU9LR2ltd1E5YUZ6dkFaRWhxYU1wZGc4S1poMnlhVFhzVVhOdUVtaXlROXA3M0hJb25UVnYxYXd5ZFh5eDYxaENESFZ4K0pVdDNOSktNZjN4L3J1aVdHelpmSFBCbGYiLCJtYWMiOiIxNWZmMDU3OTZjZjk2ZmE1MjZhY2ZhNzU3OWU0NjI1YzZiNWIzNzE2YmQwMmNjMDJmM2EwMDFmYzE5NTljNzg0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImpTQ2YxTVZFYks4REZnMy95cVY2enc9PSIsInZhbHVlIjoiMWZHcnNFbnQ5QUpISlFBU0Mvc1V0UkNqbmVhWFh6aTFlN1U2THkvNHRmNjl4cUltL1kveXAzMjRYVWtmVmhabXJKdTMxNTJKYlkxK1VrNUJEdmN4Q3JTRXBIWVI4ei9nU3pqRVVheWltQ3lUaFVmMTZ0NWxmQTVoVTR2TTlMZUkiLCJtYWMiOiJjYjViMWUwOTc0MDUwMDA5NTY5NzNmMDM5YWFiN2JhYThkOTc0OTcxMGFlMDkxYzZjMGIyNzAyNmU3OWJjYWNjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "JMaSQPjPE1zX2sK1V9Sad2j1Wny7pj1UYVZ7wNzx.Ew-1791940362-1.2.1.1-0aF_mlHt0UKIONo7TsqzgdadMGEhpt1evsztbYv1K61DezCnTppMxNONp8hdtJyu.tb.CDrMW2kxw7gZ8vvK437vdwcM5Uta2VUhB9rJ3fAtIADd1NXqy_PLi3SUg03pB6EpQWn3e.OUYwHa3ePbuKYS.iLqycqimuOhxgZcrP3a2ms.holfh_DNg4NwNOaQJivosi.Yk_meOFNwvgC06gaFGncpd16AyyMQ7bUhciBCAw7sL10xphDgs31Io5ZlT1J.e8TlfsF_syRG7ZsE5Ac.HNMdIaEoPvLZgzCjmQVdRU50JbDW2Pe57X9UaLV8n7Q1XVVnnkYPqjIYaAHCroC_gJytabQSMZN5DIjsveWuG0f6.BsVXxJSQFAsbJZoHPMvA1R_JiP3.AaKyKF7bZZojskwMlkakXWC2seT8qejYurPwPAywZSxxd86YCFB.tkzQtd.JPfXxrNZwmL.F1.sTUZCpL92XOzHpFkHruptztZoUS4psbElgaOllcZSuILJMS1JWSN.8jvrXHbPcw",
    "XSRF-TOKEN": "eyJpdiI6Ik83Unp4bmJ0K09JYlJlZVpDSDNUTXc9PSIsInZhbHVlIjoiaURjVnZtV2F0S0MwbnVhNU5XYmlxblUya2VpS0F2MElQcGlSS2pXblhhK3pITVFDRkN4WTY1ZEVjajl4bzhGSTh0YVAzaUNIMjR5R2hlQ3J0OEZoSHFpQ0ZvOXpWRk5vSEt0RWdYWnJhRGdmcDlwUm1uMjVQNmF5cWZrN3ZiMkYiLCJtYWMiOiI0NzA0Mzg1NWY1MDkyZTNmMTUxZTY3MDM4NDMwODczZjRiYTYxMjdiYjY4MmE1Yzk2YWM2MGM4YzA1YWFhZDRhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhNQVhldDhmOWxuek91TjZialRJRHc9PSIsInZhbHVlIjoiOTNZMFoxQVM1YzBqZEhjNktwR0RuN3g5VDc1bFgyaHJ5RmkvbWIwbnUrNlcvWGlaakNKY0hYV3l1ZE1KMHRxeVltWUxrVStRekFzTzgzSit3dDhqdCtFazFjSHBRd05uWlliNTdnK1d2OUhXTUhYdVNkaVRvOS9TR2lnU09WbU0iLCJtYWMiOiI5ZTU0YmIwZjU4ZmU0OTJlYzg1ODY0ZDdjMWJhMzI1MTVlNzI1OWRiMzkxZWU2MzkyNzlhNjYyZjBkNWM0M2QxIiwidGFnIjoiIn0%3D",
}

