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
    "cf_clearance": "O9S8EEhjBAarnVkqdfv57.2sszRGsBK.F.wNd9VEoO8-1791969371-1.2.1.1-dYFs.wrJZd_a8iFvFcWHnxV0w2XLDBU5gu08qN.I6B7m6wztNHbb5WfXeVMm2pvZawerKSlPT88adXkrpFBHm1FxKxFaG4WkHIFElTaLqxYl6pEuzv28MOQLywOBDP1dSf1KRr5iHRY_UrGOqSfw7yUbsYetusRI1mZXgZTUcbP5fcS_dRqUP0yVCvUp7fOql6AJS89YpaOvJjKm.uEIfaRBEdmgUVh3.V0svFTcA1RbezMQSke0IJ6avO1P4dfoMgMiKOdu6ukTqqjPc0bz0feDRsbWbqMKd1gp17DNcE1N1Q4J6dYcepH6UpEAMyfq_FjvMeaWs7eVrtBS2g6X3X0UXHAU8OP2SQIMLI2pDeVNNvLSkDC_74568z0p.cw3H8hSf2Ab1OPZljIK2VCGQl6hmWDSIbTt_Uqb6Ogbts8TrRT.E11K7hO6oIdH8nzr4PwgnTioseVF.i2u8ZAF97cNV24YPUhRW9u.bVQHtSAYvZt7lIqFFWu2X3Y72uLnFt4Q8kM8Ky2y0SQe.Qa4rw",
    "XSRF-TOKEN": "eyJpdiI6IjRKWWRXd254NVFzTmY1SDB0Ryt6Z3c9PSIsInZhbHVlIjoiQnppNVJDNGVUeEZjSnpCclhXQUtUNWcvQk1oMHIybC9oRUdHSFhZdnhtcVJQd1lLYjBaaHhSdlJtZXVUT3BjaUplN1lwR0tiWDU1d3doc0E5bUFhZERaMDJ2NEc2ZlZSTHJUSGVyV1RlZjNwSitlaUs0RUpiNE16WllUZjkrZnIiLCJtYWMiOiJkNTk0ZWJkNzllNmU1MTcxYjQzMmIzMTU2MWE1M2QzMTAxYTJjZmZjNmE4ZjQ2YmZmYTdhYWM5OWQ1MGE5OWExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVIZHRDMjZCdnlzR0NnWTlEdEQ1ckE9PSIsInZhbHVlIjoiVkx0VTZmR0I3NEx6aU82S29ZQmNzZ1FVbFM3d0NZUFBpanJrMXZyTTdMY2p4Sk9LTUs1Z2ZRbU5jQnJBY2tCOE1jaUNOQzlBRkJYTE05UDJCeUJBZVYyTUtkdndxcEdQZEgwSDZqTEZ2b0QrSGlScFErYlp1Y21Kd0pWbnNoWnoiLCJtYWMiOiI1ZDU1Y2M2YzMwZjUxYmJhZjY2ODAyNWU1YWJkZTgzOGZjNzM0OTMwZGViNmI3ZmJhYzA3ODFlYzI2YTQyNzhmIiwidGFnIjoiIn0%3D",
}

