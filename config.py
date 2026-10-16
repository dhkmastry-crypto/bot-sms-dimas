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
    "cf_clearance": "GvwSGuSqdYPRn3tosBKcrqYLNgTX2c6EDLxdUhWzQSE-1792141628-1.2.1.1-90vp15yeS9AmX1ImA.BGiBGmy6iqXhQSyAwjS3z_TEkJHkeQjcO7GruRE0WjdjQcvdMB2pDw7tIsCkV0gT.YLEzLgATrSDbd1SDP.8V089hqQhT5jBkQmHUDVRuG225Pq6IELVYReLlxAixxw_d1IBpuwxATGQU2ibsLIy4bwt9Uroj5u8eUri9GvNz3X2VgegQh5xPNiLHwetNMi.q6ZpvlO0IRdvTawNaAQudPfzKB_Z0KWsqfMEsLHjiAcC.Cx1Gn4CUqHGlOGlrtNfJbN5gXcNMOFn2YZP9hdYtJcVNmsa385An5u6PtApHxYVF.RtrByRlRN2Calnlvgz8eY4sR6B5QKf_CRJQs8AgKd02y.agob0NcCT.sBA4P6.f.RobmwO_yKXlfFiDy11fQ3Cx3qDH2CH22FeWxDTR8B_LtKZNLe.dlTsX.FId1d9GvqnF35rZmz4x1vfIw4g5jL.EYZ3PanPkyhrfk0yvA9SpIjmSscQHRqXKQu81.eEkkxS44LmIqchgOCadQJN8oMQ",
    "XSRF-TOKEN": "eyJpdiI6ImlOa2ZsdncyRmpFV1AwVlpqMCtxQkE9PSIsInZhbHVlIjoiOHhHVmxMT0NlUWdCd3liendLd0hCY0kzSkwwdEsrTWthNm5YWHBCZUZyQmdmdm9FZ0JFMWtURVJRTWpIOWF4R2NTK3FrQlVKUGRpR0huOHRwWVJoWGN0eDMwckNQRzNPcjR5WEZYV1FscmNUNWNZcEFENGZsOWNmdHpvWWFFeGciLCJtYWMiOiIyOTZjYWZjZDAwMjg3MmRiMWEwMjgwZTQwZDU2YjY0Njg3ZTE4MTM0YWI5ZTE2NzU0M2NmMzljM2ZlNDMxN2YxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikk0RW5Fb0htWU56VjZBV09hZC9VYmc9PSIsInZhbHVlIjoiV0FtbTJUV2pDQWsxdHlBVlJKYW5KVVEvV1JteVllOGNKNk9zMGhVVDNYcG9qd3BtWEhtWWtLNkdSTW9BQ1R4WElJeldWVFBReTBQQ1hCYkhBMGloczZlaUg5OVhycnA2TnB1S29nbGlXREpaS2Npb3ptaldwT202YlRCcGNLTFciLCJtYWMiOiIwODcxMTQ2ZGY4MzhjMDQ2YjNmYWIxM2I0MjAwNWIzYWM4YTA3OTZhZjMxZTJmZjRiZTU3YTY2ZTg5ZThmZTFlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "igqVGBjHQxRmE680QvpwURs2t5HBHMMDYj6Qf6Yu4VE-1792141638-1.2.1.1-m3cysC8VxMeowk4p.qbctYy5WdsqKm0U0aUrPfC8ACkLLo0lc8YvrbV7erOBd4Jq8lodIi9g6eskoFR71PE7iVZoT1Mesycm2qE113QfvLaC7NmOjyN.cS5OAA8DjZelaL6HRjF44us3iMj3yMfKxXHxV3r7SvxWI6m1zaPNCT70bD9SqLFjzOdA.ReiHj6u4_TOgCjJa6UDAAw_roSBGCPEHB6qzoz.r4obuY7YrY7ztyuxvu_hZvamyEgx2S2loR1AZKFCPvH38oXWCkzOuvEg6CcTTg2HZQ8hxrneitZqBYIIUMQkDMVbVgtCj9ZrYHVegTrAY61tvGr6kWco3MKRu2pilDFyiZ.PdF6fIYWc4QiBR.P0dyHL8XS9zXBgYWs3PUoQ00wDQAEyTT0vMUU2hfAv8biSu27Go56oBzIrAeAkj5vjs0wo1rsz29S3jAIG9Oy79dKLBIISQs9QBxv6PtzwRR5N6ieFRmdOVZE7do6Em6szkvvnlxudZMJBgpIU0zAwc5b13boIRFJSTA",
    "XSRF-TOKEN": "eyJpdiI6IkFpbU12VEJpQ3d2K2RuUFU0dW9RV0E9PSIsInZhbHVlIjoiTlMvZm5OeFc1VjNLR2RHeFV4cG0vQW9MKy82ZFdWSlByWjVPODk3S2x5S1FpU1RNR0F5eUlENGJhWmllOWNDcGN5dHhpMTg1ek1sbm4rMVpPZU4yNy9ISXArQVJybEVtcVRpbHlYLytqaHlTR2FBUGptUm1mUmRoNG1qM1l4T3kiLCJtYWMiOiJhMmRjYjI0ZDVjNzZkZTc0MGU1ODc1YjM2OWIyMjJiOGFlZjFjNDA3MWQ3ODJiNjdmYWMxZGMzZDUxMDdhYTdjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlFzRjNMSWxGK3FkcnRoaCtWQ0NmTVE9PSIsInZhbHVlIjoiNmc2MHZLMnFuY1Mvdk1UQ1RWNXk1UWN2VGF0TldtcFhPdDFad2liM3JFRmNBZS9jSTRodU9DclYvNnB5Tlh0S2NnWTB1dEhFcXdQTW5TVnJ3elZKWk1yblRWNVJpakx1UFlMRUNpd3h1OWRDNDdCMFg5bjl5MTJVSFZnRXByTmEiLCJtYWMiOiJjMjAyMzcxZTc1MTUzYTUxOTE5NDYxNjQ2ZGI2NWZjMmMxMWZlNzBjZGE4ZjA5OTgwOWI3OWI4YTZkY2M0NzBlIiwidGFnIjoiIn0%3D",
}

