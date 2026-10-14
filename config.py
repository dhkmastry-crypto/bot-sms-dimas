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
    "cf_clearance": "cV4xo9UkcdIGuJ2wxVoXzkOdE5G6MoHYaQlEiLHaW7k-1792002930-1.2.1.1-CvSIcmJumh5uo5tcMnZpY5QCrqHzRakhuAD.hKO5wSLgvlm5SvzGVHnQ3MmFRLhqTbgpnMkhtWK8_35xZZPReLkkHX5QGbDRBx5wAcW2bF5qjFY5vluERHOSNYe9QjRG6lhFAzrVaHd8SF_aaGAlpTQ2kr4rxZvoWFm6.QauJfO08QC7_wDbxEIcTGMlyluyy_M61rzbieer_q3I7uadr1i68whm8wBtPQVI4nczLoTapoFZb9o.NSBDUoNpqgBmJ5EzQ2V9501.UuHsbMuryjuJXPVKmI8sBqTrGDFp0z4GX9fRaLZBMrygzZ.cnf4w9Fz7drUVbpD2AZi4DWfp8hkHKX6nFL7rms0HOdsgY7LiDkAZ2UM10b84RrXhrVRURxmAcMs38V2SlkHQcizYEYQ_UsZVruZsa__VwZdV.j75862vZpvvhXWOhI0.nwBIQ11gSNC9za2R_GNsqt3Q6NMWFDSQxPRVBh7d1ZDIN0qHstqXA5r5swOsmNZuW33neORgsuNXsoBOTuknHY0iJA",
    "XSRF-TOKEN": "eyJpdiI6ImJwUHhXcEJqSHBMemt5M1FuWnpDekE9PSIsInZhbHVlIjoiTE16L0VDeVVoVUl3a0ZOcnNZRkU1ellKa1NZMlVQZGYxWnNzOTF1SzBlMFkxM2hYdTZTN2pJLzdzbzRRdUVIM0RaL21oNmxRZ2ZCTXZBS1VtSldMMGVrd3htdXpudGJQVG1La3JCc1QrbkJyYzYvNVF4c0tJbjJkRTc0eGNxZWQiLCJtYWMiOiJmMDFlZjI4Mjc3ZDEzNGI3ZjNhOGZiODg1NmQyNmVhNGIxYTJhZTEyMDcxYjdmNjJhYzFhMDFiMmFjZGE3N2Y1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlRkZ0o1UnVlOUNrdG50WXNiU2txV0E9PSIsInZhbHVlIjoibHNEcXM2NFV1RzdYd090aVhyVTM2ZWtTR3JSUmNOazRMSlZ0MjdNdHBLWHpyNnY1S0NENFRkQmw2WWduNUZvOE44NUZZTmdQRkRHNS91ZWxFTVJDdTJabEFISFMxSE5pa25rTGh4OEdMaXRjZGplSWUyc3k3L3FVNTRjNnVYRngiLCJtYWMiOiI3NjZiNmMzMjQzZjhlYjc2ZmJkODNlMTMzNDI5YWMwNzBhNDk1YjIyY2EwYzIyNGQ3ZDMyNzNkZDk4ODkzYWNlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "yc8iSW9LOKRRfYZ04Si.2WnbS.3blMjHpQGzVZWXT0M-1792004748-1.2.1.1-LsrLJ88lgj3kjEJiTF_0SsdZE57DD.pEmr3lex_vqM7U1KjVn3BFLnAV2DvGWW5M_MB9UnZayte3n4vJOIeqkU1cqh9cSXt2XtwUUXNDif7n55hOwAfXG2N9i2And8AvJGWYgselB4CRSj54iBysFuyXCBbBtBZjc5f3_l12cAU_HRaIM3x2bhxn5OfZSahrJUjV1gmTcf1FAOcZthISicTQTkH6.0fbUTdThAT8bD_UTIJVYM1adq.pSVMPE0OM6sQ5Cs6jTq8qPLanlwWb2qv32cWouJKLogLr4SwtgHcQ0XN2LQccQ0PWqjq63IlmtBzc33Ysmot0abN.LFgL5BqUIcq64EUktyXbeEFfLwHvTqH1s55v1rrvnUk73oOfM5xyKEVH2MFfarXcMgeurhSsXD0uHsUjVr92nW_yGpix0aO31yumUErr746mZ6WjFBC8TY_dpYOAAWpPiSJSwy0cxLm99z84bkqj9Z0eAOC7wE2jEqLylSpvoxMDqI7OIVvXG5elI936W8bJJx5zkg",
    "XSRF-TOKEN": "eyJpdiI6IlpsSEJJSTFpZDFoZlNnUlE2bUM0ZlE9PSIsInZhbHVlIjoiVG9PdGJsTmZDQjMvWE9paWcrQUszakxtaHM3aS9rRG5aNVEvN1hYUHdpNFpWQXU4blJxUUlGeEV0N2ZQU3JQSUFLRjhjeXpENDFZV1FTRVJ2UVM2eWJYSldEd0pGVlpOV3dIOWM2eUh0cm9RMjJZdDgwNFlRQWtZNk5VdHBCUFkiLCJtYWMiOiJlNGQyODUxZmVmNjVkN2YyM2FmODM4ZmFlMDFmN2VhZDRkOWQ2MWU1NTM5MjcxNDY5YWZkZWEyMzFmMWRiNDdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVmWlNpbm9Nd2Yrd3IySzZKcHZvcXc9PSIsInZhbHVlIjoiS3BrMUJuWDBYd0wxb3pzZkJYcEFtOTlmeldQN0tTbVJmaUUzOFdSZHFrcFNFZ3I2dGw2OGJpY0ZiSndCRkVGUEQyOU5YTFJqUkhTU1lwSHZKQ0NuVnpiODFSTnZWZWUvSHFjRVhDaDFycUh4eFpNUld3bkNhVkY0NmM0K2JLUTYiLCJtYWMiOiIyZjI5ZmRhOTlmYTNlOWMzYjc1YWFlYjJiNTZiNjY4OWI3NTcyYWQwODBiNzc1YWNkMTkxNzE2Y2UyMzUzY2E4IiwidGFnIjoiIn0%3D",
}

