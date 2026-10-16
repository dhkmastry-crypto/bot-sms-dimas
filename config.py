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
    "cf_clearance": "UDjQppbu_NmAIHH0u0aNVQOa_emabsmT27HowgKvpnM-1792134384-1.2.1.1-RXeJausaGU3ba4rOsIbLTxpb.Mhp7r7SbBxt5tNxr_bmbQw7W.konfXf3EesjXaSn1a.4AxeLxlaxsJ6WKTSb_JHMOjAVaeZTLJhA7_woNtQeKRbnUyXXiKVCwM7EgCykfEGxWaUTWdCFX1g3iqduz.N7chTumLFGXa_6qz6ebHpxshp40dITsQrIeNcEIunjPX7thGTlfdb266dAlqqxYlorSJFRPAVveC1Y5fPAKy9MYMsUYECWEGGT49z6rW9Utcq06J74ujgsJjqpls3jan07ave0YKpD6ZlsqrtPGBVPYrxqbSQfkuwBA2d4vd2JFC5vvBLLhLa3hSbqJwj3qFcPoDH09_WmcFYjXpFGlMmknNrcAoJib5stP5RnFpLY2Chbu3TzsXw4win_O4LWeoeZR0rvRXj1R1yGp6lhGBCe1AoGMdsLR9CznXJ7gvcLih3u.JcoqxG7D6Bhoafadt960TXyQfiDrpCJL.WZcU0DwILn2b_9BShcd9wfkDXVPGGi2scN.Nj8r_sbVyWiw",
    "XSRF-TOKEN": "eyJpdiI6IlFWZFUwU2xhUis5eE9KYXhGVk9XTXc9PSIsInZhbHVlIjoiczlzQmx5dnFBUHJIWVk5a2ZBMjU0THlOcjBvdGhnWFd1THl3VWJZbG4vamlGOVI3K1RMdytqYW94Y2kwMUpXMFZXYVZYTFpHQ044R1duMzRCMlpWS2dwZlhVRThSOTM4d2dJaFNXdHUwS1YwRytDYVpnTTFVdHc1UkpUUjhxTDAiLCJtYWMiOiI5NDA4Njk5ZTljYTUwMWM4YzhjNWY0MWE5ZjI0N2VkNmZkZjJiNTFmYWViNTY0NjlmMDY1ODBhNzA0MjJjNzFjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlNLSVBYS3gwNVBSYkh4bWxIcnRxaEE9PSIsInZhbHVlIjoiVUVaZkdoRzBBWVZyQUI2Y01EM3FORVFUZHpDelR0cVMxY1cvOVB2OFFjT1BkdXA5SlRGR2dTd1ByUTBJYm9sQ3QxLzlYYURPWHJnQmNHZUZLenZTUk5LdTlxNDRKdzdaVGVYc2tkajhVa2kvV3pZeHdadHNqazNQaWxxY0lmNzEiLCJtYWMiOiJiNTJlYzljNDNkZjcyYmRjNzVhZjQxMWFiMDVlNTYwOWZmYzNiZDk5NjUwODQ1MzQ1ODZjOTEwMmE2NzIyM2JjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "fr9AX4R0OZunNV81hWOwtlGw.hLXC0jJ3K6aO1Oi2nM-1792134401-1.2.1.1-Yb7gUjnmaE9x8O8J8j5_mekEnhXPgOulHBbV999CqeGRj0VzQA9ID6scz.xlFLNtLUGoeVPljug_gWGNfkcBKyw75cmKq_30t4l8nFP7dSdT7hMJpPmiAbVT8pbRE9Ir6uOcCP4oqz5iORJ.r8tXcPMydc66EWfOoA_20ZgODRWeWZ3VEH9cpFNZt1tkT3RztVAP7rbNpMWo.qhzT7.O2mWbGuN0Jw4xvLgDdXmLQmS1_XUl3Pm6eEFjgww_MqLuvBT4NA3XmPJIQ5C7UpkHgVXtFhzMDo9lwf1TlJugUsR7HVe9Lmp_ipz0hLfZCap6oTY_j_ovtyJq8CkusmFEJim_.gXBmZ2Xh6b3YhG6YPE7EPsQui0hQAwqx.lMcWPZb6hWMhR4DOXqF8LqR8fsm3QuzSgl21DkKHzVmX_90.DpoekX_hYOolH69iYJ0WD0D4lOASGbdnyg7fOkrSsp8kwD1YxKsInic6J2yNMn.5f._j8FBt8g8dtlsTaxgvLz5mhLmP1cJXHJnU40S.9vTA",
    "XSRF-TOKEN": "eyJpdiI6IjZPQW1pUWl2V0F0dWJiUG5uT0p2Snc9PSIsInZhbHVlIjoiYmJKQzgzS1NNK1VPdi9tUEdSTTdtRmNCZnlBZ3l3Zml4Z0R5TWJLMjViSmtxLzNyYnlHUHkrVDJnbEZwUk92ZUROMmFTYzJ2MDM1V0hLZk9EQXhCZitIWEpZaUJvY3Q4U2krdjVuVWs0d1BsbG1TRk8yaGowUnJsOWdRcWVTeEIiLCJtYWMiOiI0NjIxNmZmNTdhZjM0ZTI0ZjAxNjk3ZmFlZTg2MTRlOTRhYjRjYmI1ZmQ1NTFjY2ZmZTQ3MjFhYmE0YzJjZGYyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjB3TU5wemRzcndRMEZuTEt5Vy9ORlE9PSIsInZhbHVlIjoibjF1MWhteFNZSitUWm1XbzVMWC9zYTJpV05WUmROZHlWUjFLU21hS2dVQ3ZOSWRNQmxIaW5rdGFyM1pTWUdaQjZJeEp6QzVxdVRSQ1VlbmRaZnpiMitRLzNlUVcrUHcvZTA1Z054YTBpTC96d3dUQUtaa0h0V2Z5ZCtsYTRnYUUiLCJtYWMiOiI1NjNlNzFiYTU4NjM3MGIyMDU3ZmMwMzBlMWQ1NzM2NGY1ZGJkYmQxZTg4MGVhYTQ3OTEwMzM1ZWZiZDk2YWU5IiwidGFnIjoiIn0%3D",
}

