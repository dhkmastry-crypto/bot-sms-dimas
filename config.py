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
    "cf_clearance": "J2xgNaEGsSdjrTXC5oR6U.fyuwCX7kU3C4u2wF_1VeE-1791971085-1.2.1.1-GGwCm9bVoXOvxmEg3IQyDYNJY.MIpkRpfwz7on.96nnVj05mtM5E7pWr2M7CMVWUxZqMINlZyxReaaWRWJLxzvloRH6GNoRxWOI0V57I16XQvOaPUQ2Yz90gdXZ9BGsZDmX3P14N342PFQIW5wQ98yEo8tNvzijCKx.ClvTKCVPFz4pcX_KQJvqlYqYXOfpvsvT5.7o9QQkkDvFqv6_JRQUMqmFelhxyTsGihuFxvRK_cizdwjhl9_rNFPRpbaj24l_6tcVdfcSAEn480a5LrTpiAIqUjZO16_t0vIg3jdRO0PwOZDAP_ASxLx4GWM25dScP_0.FuXMIpDlj_v7U3Mc_PdvSZnAkNs3ndROyx0jvMQrbQ5nnerJotnyOg5yhYftVpErhSKuRruYsd2fgTxON5V_UZe__G5zIkdJhPxvSFzR8Kiwo1XDaBIFxbMtuPlb_XjVVIt9IzOjQgdnqyLbcbzQ6anfFwyJ8axgnlDd1Mgw4ugPY04B4_Nm_KfLMZO_K72rad6SeBl7GKZsgNA",
    "XSRF-TOKEN": "eyJpdiI6IkFscEk1V1E5ZUI0YTdDV0xRK1hIZGc9PSIsInZhbHVlIjoicG5LTjltQnJYNlRBaElIQ1JYMUhWdkhRdGZCN0hlL2FBcE9EYnhkZTRlb0E3czkya0dsZWx2ZEJwSGwyVXZCcDRRTWpLMFd1aE5rQlZZUXV1Z0ZFWkZraUcxWEJhL3prL0pXYkQ0TnNac0ZZaTRpQkZhbm1ET1JyK0dZMWdnUjYiLCJtYWMiOiJlMWUzYzA0ZTZhZDZhMTM5ODA4MzI0MTQ4NzM5NjQ2ZDgwYjdiZTFkYjA1MmVmNjg5MTc1YjNjZDdlYjMzNDAyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlRPSVQzb3R2bnVobFpsVGhMeWV6VWc9PSIsInZhbHVlIjoiRURHdDNzTEpVWHk1cEtNR2sxblRIVXduTWx2RDFMOTAyZStrMkM0VzBLVVd5ZnhzR2hTWU14N2cxVkFiZ3ZrWE9NdGFMNGZ5dnRoRWo2aVNqRkEra3JIaytFaDc4bVRoV3ZXTzZicWo5NDNwdG9mSHVTVDhJcUc5MWpNdzQrMkMiLCJtYWMiOiIxNTk1NzRkMWI2ZjBiZWY2YmJlYjEyNGQ4ODYyZmU0Zjg2YzkxOTEzODRhMDljZTdjZTM2MTBkN2UzNDU0ZjRmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "t1jJGB5CAbDwWotf1_P2gXMbIzn4aD2elylBYq3BXsM-1791971184-1.2.1.1-LubuKqIZUxjcZkb_oytaphr4v8YobVgpd3Gcb2vhMt8elkmaO4E4dL0MQ_2hNi3XUKegCI0WrDT58Ivmj7H1XjNxnIj2DTcnfXppgSkoIFPBV6Q0yVg8iQesGf4vhukHyd4.f8WO9scuz36bDYFJRQ0DJuGOTQQ_DecsEFCbYwGbVCjmS1yiiJKxqoDkMSWTD7AVMD.IH5gRXvR7AKxaheH41yO9RnUfgH0xME8HJt9l6JNUOIZL1d3G3gsPdPelSUk_OXR16LtShnjA5E4pYqSghEI5i3ZfaKRBvr0Enf8Z7NtMtxtUvG7Pg_LGrQckKuuziZPJD3l7d_cReu3syDhfhgUzo1_7F7I_1GbzW0lbJriQh.qqN5zKeunipkcd2N7L8qGrLtv7JGCA6geIE6gl6gMm22SxQSIx9OpsjItMo2wkDGFEGsJkZe4mLEIxTSRpqteiAQGASVv2iHw2gyeG4XoND5g9s2p3YntSnnTRjq9qzSGsCcnAr58qW_IltseAoYxWMwqJLZ9XauLVug",
    "XSRF-TOKEN": "eyJpdiI6IlZVSlFqMGtBUWxxeEdjQ0JuaVkxUVE9PSIsInZhbHVlIjoicW9sbm1aYmczRnhNcUs2OUIzSkFTcitwUndqVndReXZYaU5oNUVmR1pwa3hwQ0swN2M0UWJOMkxBOEhSaU4zN1BtejA0QTRDS0xDVEFVSENzdUx2eFhNNXMyejI5Sk1zMy9mcVZWUUJZcHQwS3BnUHRPYmZMNEhHYmxuQ2VXR3YiLCJtYWMiOiIxMzJjMmY3NzBjZjU5MzU5NTFkYzAyN2Q5ZWUyYjNkOGNhZmRhMmVkZmNiZmYwZDJjZTc1NGY0ZWI0MDFlMDliIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IngrQVp6VWFQQ2Z4WEtvYWZrcGJUMlE9PSIsInZhbHVlIjoidDA5ZWhmM3NEVS8zRVJOQmw5bmsxYzRma1dXaGFxNWl1aFlXcGhvaTBRNjh2NzNoMzVLa3RmMHVDRlA4N05PU0dwZVpXKzB2VVJ5N3lDdGdvY3h4M3VMOHNKVmp4MjZlOFRMVVp5dFYzbmt3cUIyWkg1Z2orUHVxaHluNVdMbDYiLCJtYWMiOiI0YWU5MGQ4M2Y2N2E5MGVlZjJiYTg4NTI2MDQ1NDg1ZGQzMzlhMmJlNjQzYWQwMzUyYjhmY2YyODk3MDc0MjdiIiwidGFnIjoiIn0%3D",
}

