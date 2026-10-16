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
    "cf_clearance": "Dw.rOPqefliUvgiWrB.N8I7oGdnoD5bFAige6n3vsig-1792123509-1.2.1.1-.NHgchxAlTlpHdoWa5gCkPihRpu7jANKQV179FkkQc8VpQ1LKMHy13EGwk7We5Rkp6VItukHv29x87i5cei1eSw0pa25.yENYNjm1eUDIAK_dNwGgwRCnlz4oKTHNnl2wI_kEy.PTTDCbEfYTtMX47KdRnuScz__vB2UjX.1Fi5eWYnv1QoJGKHAOQrl5L7UE.v.mFiwKWKEGtOU2.nZkZfagLyQT219lwCd9BeulKPDs0BLo7zdhYV.Gn.FJdMxPQHeUrgXDQ97aS_42kCSm2WKBLeGHVNs9czBx1N0yjf4TqJUDjWIOdfKu2Z61htXCOZew4doa1awXGDKrbq1r5_ADJv2XT.LoLF7lYg7WJeiF8tpQz0m9IIBeMRlyWJRmJRpJO2A6tI.BWWYSy0Bljmhpf5ZqZ7WS_KEUSZDGpoCR6UCQDs5v5zAnPA8eTHd3ovltYSlPvo5C2eyNPkYZs_ColxStLXKHbHmHtCuaIeFkUqqZS02bKqZldwWn5Xb029bDj9bfhGSAPYSKl5WFQ",
    "XSRF-TOKEN": "eyJpdiI6InA5UjhGUXlCT1ZTU2Z1T2NVa3h0T1E9PSIsInZhbHVlIjoiTXNzV1pLa0d2dGU5cFYraHp5bWZwVzduRVluTmhJSTVqQmkyWWV5VDM2VjVqQVlMZWZqWnZ1SXhaUis0TmovWVFJVGc0Q251VmNtUGRRMWYxNVNQZTQ4bG1SZEdtVklZdjduUk5QaVV3WTBURHc0MXQ2VDNGL2JHcXRkbnlaRHIiLCJtYWMiOiJhODhmMDJiNzkzNDQyNGVkOGJkYTYxMjIxN2VmNGNlMzEwMWE3ODI4ZGJhYjU4MzI2YTdmYTg1NzUxNmRhNmMzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkNHWFQ3OU9tdkdKMFNKSDNnalkrTXc9PSIsInZhbHVlIjoiY1ViTnBLcWFSZ1FZRmZxakdrbjl1TWE5dnJFbGVJMFFNZExkOEt4QU1tbXFSQ3ZObURtVkt5aVpPKzE4bVBuSkdTWEpYTFpUSzBQUDdYTFNvd00yalRDL2ZIRHRpamJvUm5OaVJQNnFaa1ZhM1JUeDRVVU9KRlk2ODVvZkI0d0UiLCJtYWMiOiI2NDE4ZTA5ODk5ZDA3YWFjMmRmMjBjNDJmOGY5MzBlMjJmNTNhOWViNjBmMzNmZmZiNjQ1ZjA1MTkzMmNiMWQ2IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "LqEXns3QIZE_FAXjbFrVGvQ9FMWwHz5hxZYBQBehpXQ-1792123499-1.2.1.1-VeU8L_RJlX0plmY9Q1OI1OOqxySuPmFmzwPNYnOUpemtt.TzBcyu3CqTMgTr7Hd175ONuSK6lJd4x0fVA7L9VJWyqnKVSORNQ_w7QtcLXweS_Pt3scFax3xtIM1qvdRnCwl6trbOUcUlPBnvz7q6XOq0WIjOgZs6dAVdl36BPMmtY3TfK2.mUmgjQe.8bDPtYWD.HHN.SatUpL7uin6efne8.Pzlla0LheCO1cn0hQRLCGuupHKqLfN8sArrgXJ_x_3MvAf_2CJBJbWFQmkMgzCnCvvB4fZD4bZd7ZpMVVGDqu8Czn1dIOjB7Ph61.c4V6OcvCxinsqlrS6zqlaHaA3QQCUIGKByCEZ1Tv_cPtwp4E82xZDxN9aYS5L13UKaj7mlqs9JpxmyUD4uY0fmPxWW8PRSQDSoNxYDC54BxKxRcSoDpqFlPPNx1M44mDCNziBAWiwY.97AmsrRFXFaXTJM5jjXEZbmtqOixQDkM.taUcDG1c85s_S_zjdaAJOqfPc8hdWmNEznvk1XlyCb0w",
    "XSRF-TOKEN": "eyJpdiI6ImQzU00xZ2loYXJzZVlJVkhVcXlaT2c9PSIsInZhbHVlIjoid1FsbnNsL0N4azRCYlA2NmpwcEwvL1UzREFiaXhvS01DWFlPQXNQbGM5VWNrTnFyUWV1cDRBb1l5WE80SXF6a0JFSXZHSjV1YndWR2ZCQ0ZzZnc5ZnlRSWYvd3VFdkVvVXFzV0c4Q25NT0RCNEZWUWV2cW5QK05pUFk2R1lHL2YiLCJtYWMiOiJjOGE4ZWFiMzY3ZWNjMjg3YTQ5MTgxZjg5OWI3MWRjMTM4N2EyNmE1NjU4MzA5OGZjOTU1ZTA5M2M1OTEzYTY0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ijl4MGc5cDNKbDU2dnRhUEUxUmxweEE9PSIsInZhbHVlIjoiL0xzMXB6cmFqRHNwZXhEMjZIOHNNenRlWjdyZUdLVGZ4UDVvcWpVS01mZ254anlHWUUxQzE5S0hTenN5TjVpV2VZWmdwZ2ZpQWgrZDA1UEhhczBaR3hZa1VaTzRnTE5PSFhLTHZvN1JjR0gzOUlERktHelBKSk5lVDRQSVBwbEQiLCJtYWMiOiI2OTU2ODgzZWY3ODM5NGRlYWVkNDVmNmVlYjlkMmJjMGNiNzcyZTY0ODE3NDdhNzI3NTk1MGQ4MWZhNDU2YmE5IiwidGFnIjoiIn0%3D",
}

