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
    "cf_clearance": "OnrLIwF6Lf0gcO3xsYN6R6XSQk5c3YaosU53f1xc3Tk-1792089038-1.2.1.1-xa4Zn1wnaFq17BP6xcdpsP1ii6y9VrF.k0ypqiL0WReoynWY2SCl7xNMVTVyv7VCyW6nYdP5VvYCjoelmkDpWurx4ExPQZyVD1n3rrxjWGkKw1nPjqx9LJ2iKADp3BBydveQNaBHHxFPuR8kO0DUEEQEfREnXeqGwb8DWRJx.TOy0_ohRahca4b4H7vYGQ4tEfS6amsViTxsMH9ne8DSTlEE_xfvRBVOwJFsrq4Imj0hL4m6odD.EnK0xffbQUbaYo6q5Xt5zadKitl.ClE40dx6WemHnx1keBDO_37T0eNHmIFNXsfxq3hjzP1gwhehiHqWKooLIRfJwFmdxEohE3AX9ODR4Yw3j6FGtABorGtQz6ihYFeoRCZ9xLSh8gnGh5z_tsUG.6._HniA9Kxn5S5GjC6I1S1Y7mAzlUK1so.GuJX6CtpV5BLP6GIgtTb_ovXgc0UlYerRjBj6k8DTLzf8TL_kHN_tR7LB9Fn2BI.SvlPpD_al6H6bzOetlkg8c95_KkYk6favvRCKHz3b4w",
    "XSRF-TOKEN": "eyJpdiI6Im5XVWNTMEFqbXZSd3I5dVl2cG9CT0E9PSIsInZhbHVlIjoiNFpTdHAyVXppanE3eEJnOUFZR3VhMEpQcmFkTUpnSmloTlY0aGxiYjhXQnphYzlyeEVXMi81aEFiaGVMSXFnMUlxSDdWVVJXUzl0THRxbCs2TGJQYlZOR0xOYStYN045b3ZqTkNPUWtnb01NWXZJTVpaUmhpWUxaMjBEWEtIdUwiLCJtYWMiOiJkNTY1ZjY1NTI0OTM5YTkzMWExNzc3MzYzM2Y4MzA4MzlhNzg2NjM3NjdlMWExZTcxZDI0Mzc3NjM4OGNjOTY0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkkrMWZjcHEvdm9ZSkJzV1pGUmFaQkE9PSIsInZhbHVlIjoiZVRZQjdON0h3TklCeGFTMHRsOVlKRjFNbnorQ01vbkRmRzAzVkxNWW9tTlpGOXoxcTNlcURmSXorOW5IMC9uQXNWazIxMmtqWkVxeVNNSDdvcFRxL3RyUndSSEZyQndrUFVTNVUyU1hFa3kvRUk0RGxzdmcvKzd2cDR5NnErekciLCJtYWMiOiJiODhhNzZlMmI0YzRhZGM5YzUyM2ZjODYwNWEzZDlkNzMwMWI0YzA5OWFiZDcyZTQ1MTNkMDY0ZjBjZWRhZWU1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "alM5KHSWXlBOt3h3cZCyaCnG0MxxLt6lR9eyI3ytJic-1792090809-1.2.1.1-QJpp23jFXMKbIVKm.UZe3YwFa7ahHLaelG5upQVRNjLCDpM8nx1e6MbZYehD80K9TpWyTWOxxLzeDU1LT5PvIVDn8z1TaSTRI8IlbpHifJERge5w7m7zNQaNGkfbrQXJgSXO9GfswkxjOdlA7_3OIY.TNA8S9fkh5FkRyH3b6dlhLA3EMrm2SeDsLEeWuMmleamUxVbETcr9RAFxrASpQRaQYaXFnpk3hPyFWb7gJR2TPRCNNS83vppx4CwsLZVlUv_Mf0VlFPzlETDdGozXbd0b5KNNAE2c3E_S88LFkh6FH1BLHT_zuyut9okgxH2SPDoMe6ah9YWOMM6NkvHxNDbBHLHQORf.Fn3iZcD_QMVlrqbDis3.SD6dCgRQB1rFIXDdQiMwRNH1LTLkwgOHC1JB8XA6iYAMt1mfjH1Uzeb4KYIzZwSz5mv3YoRNAuP3l5Mx41XTX5g2wliO5fLSbHPQGzedPWJ.5BIQlTEbgApCfLO3qCPA5rurbcc0Z1rZyb_Dfptv6z9u29iGkHj3Qw",
    "XSRF-TOKEN": "eyJpdiI6IndHVWZnRkVQenpFenA3aVhKNkxQcWc9PSIsInZhbHVlIjoiZ0FmYzRRdFdRYm43MnBNVlA0Unc2MjhSVFdMUVRuSUkyK0VoU2hYRytCb0ZkcGlxT1FqeTBsMXVYc3IxR0taWFg2SXRqQWhnLzc5Zkx2d0NOSk0wUUZsQlBMcW1UWUFPak9NdnFZMm01OVRxYjBIWGp5anpsZ21iOWxnWE5lUFAiLCJtYWMiOiIwZDg2ODcyNjVkZDc5NDFiN2IzY2EwYWMyMDc0OTQxMzU1ZDQwNGRhZjlmZTgxYTVjYWYxZWNkY2RkYzgxZGM1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFMaGlEdjdFRUJocXFnSFl4dHJBZWc9PSIsInZhbHVlIjoiWjZidFFQM1FSMHNlYmFYNGtVajJ0M0k5Y3RLbzRXdVRpeFh5YVFFOVVrQlE2bXlENk1CcXJVS1ZKZkV2ZnVpWjhjOEdjOTBYYjY5RWNPUlQweWVUWEhTckpsRG5nVmpKbjc0OEdZTjFEZW1FV0c2U0VMenFaMlYrMG5pb296bS8iLCJtYWMiOiJlNjI5OTJkNTRlYTU0MjM2M2E4YWM2YmFkNjJiMWY5ZjA5OGZkODdjZjI0ZTM2ZTBiYmFlM2NiODEyYjJkYzBiIiwidGFnIjoiIn0%3D",
}

