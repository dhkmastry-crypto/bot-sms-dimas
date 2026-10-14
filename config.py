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
    "cf_clearance": "QUoUQVJ5ryLcSS8hza0icdapAlw8LdoKKcZsHlJF41Q-1792002935-1.2.1.1-bbKmirsLE3Up4.uCpfxIG7KyZ3jkicu8kfgyhwL8PaMm95o1cKViZDTHkswJjFQVnJsEn.E74DCn_lqHRsMuGR89Dp4DKTN_CK6Z6Gpy18Io_2Hpmwd22NjEfwqJG26hrEbIdla7OQdv0n62Ln3Hl8cUk4uaSaY6WDGiy5hUWRGAC2qD_8Vlf5WJVBAJt.LhqRX7ftT8DFZBnYtIVO1A8SEuvjbqVS2qfEVeo9wXHbRSybHGCGQmAGP4hixLb2toeeGea.gdpzAaICk2Izw3yOz573yZ8vRofn07t3PZFMQ6J0IJsMDSp.0wDPdSkbK0l2c1gPtfVsI8d5Ol4CZr5VkxGXosZcV6JILYHk5KoBtcRmLWA6PsvdHYkcG6SDDDmMu0Y50VxWDemS1TIvTgpI4oneiVeo1xdAbXYpIr8fI77BPFf.uqFiJPBV8yjmWzvyLfETDOssWU6GUtIybV.FmXrYfQCL1V_9XJxmx6m8WwJ_sHnlq1wWlLX_BtO2wIxM.fqsrKeY731SEl0RQ4pg",
    "XSRF-TOKEN": "eyJpdiI6IllaTVBla25tZUxTZ2R1eE40Ky9LZEE9PSIsInZhbHVlIjoiMzZlUnc4L2c0K2tTMUpjdnIzOGJBT09aZ0E2LzREMXBRWEt6UzErMDlWMHFOdlRwa0Q2Ykt4eUxXYndDQkxLNWo5VCtRSDc0U0dwTEdtQUhieTZNL0piOWxnUjljUU9JK1JiL0NqS1lYRElndVAyME53MXBMd1UrK0NmWGhkZWoiLCJtYWMiOiIxNzkzNjY5ZmZhMmMyMDMwNTc0MDc1NTQ0Y2U3NGE4ZTcxMDUwMDBjNDY4M2YyMTAzYThmZTFiMWRhYzg1M2U3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilo0ekFZU3dzWE1FYmxZdGplQlBhZVE9PSIsInZhbHVlIjoiYWhjV0dTRWpHNGIvYys1YmIzdW1lYUFsd2VKdHIvWStJeHpraW9MWkplMEhPTTBnR0JhTWlpNTVQVG5qVHlqV29rN2Y3d3dNQytjM3kyS0pTU2xwZngzNGJDakdBU2tJL3B1bDA0bWZ2ZXBUQjZHSDdub1FPRFJ0cnY2b1ZKeXMiLCJtYWMiOiI1MmU1Njk5MjBjODU3OGRiOWUxYjM3Nzc3NGM3ZTY2NTgzNzUzOGZkZGNlZTQwNDliMmQxMTIxZDlkODkwMzRjIiwidGFnIjoiIn0%3D",
}

