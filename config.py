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
    "cf_clearance": "jgdreXdSFZnx6ZfTkJQCa3YqkRlrrjYr8obXRezPiw0-1791969273-1.2.1.1-9ayzhti9pociSilxHGT_OJ_p5Pa1Z8s2V6GcByVvhK5q2hOKxDsWg1Kn74Crr6jF.8M4wTlAEE67QNVjxsCj7CmrXGDGUPaWvmp74t7KD2AIVKVZQ4tUP.Bwz_f0xO1vntnGySi1Ay0FfD15DwrRUFEnnhxNvMuhzmcdt_.0LMWXRPwAQGnyY2CPKlYiEJEaaVetPCcLxeouzDb65ECSOGrsEsTrtK35.cr4_q5Q_bVRh4qey23CWQrvQgIDBf8G6Qj5iLk8VPWKHJssMAn6DSmWBlCK7J4_fYnNi_z5LgT19OhILlfBezh3v0VZ64Y6t.GOdwGTlM8rqL45sZj1lP6diEAO1Kq9moyw3LQs6.bMc0p39ltfX_CX8x8r5a7sTZB_s0rqHeBNgliIKWSLpUSEVyYsYCPYr8tGV3De7n1q_hgL_nlq0m39B5JMjNb9EyUXkyn6DjRxe56LKpBnB7asQFHjn_1Ul8OawMaonFH2mNwfhxPjAfhzHg2FeVQt.sriNzHEBb2gE9vyM7K61A",
    "XSRF-TOKEN": "eyJpdiI6Ijk3YW1hUGhhY2szZjJ3QlJtMWRzZEE9PSIsInZhbHVlIjoiS2Z4Q0owUGx2bEtkWkVTQjdJRG1lWklMZGN6c1VIR3ZxVHhEVC8yMTgzYmkwd29GaHFiT2MwdUNMVDZ0M29QNElvL0lRZU1rNVBkU2w1RGFjdDF2T1lGZ1BoSHhDbndLdTZBQzRDaTJZemdsam0vWllJcERZS3lWYjhnMEQ2R0wiLCJtYWMiOiJkOWJlNDgxYzIxMzAxMDI3N2I3ZDZjY2RhNTM5YzU2MDYwZjZlZTVhNzIwYTc0YWY3MzgyZTAyMmE2ODljNzVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ijc4dXZlbEs1Z1UrOWkzdE0yeFJ3VGc9PSIsInZhbHVlIjoiNlV5c1NRMklnQVJid1ZOVkk0TFZBVzE3ZDkrUmdiZzlhMjlGL093aFp1d3Q1cGpLWWNkd2tkY0w2aW9vNXZpUEdzLzVocmFSNXE2elA5SzhFRm5tNFVkL0IvOGdXVllNMjhDNXZyM0VzRXppKzVQeDJnOWdsQlJQUERHOGk0amsiLCJtYWMiOiJhMTYwMzI0MDcwNmU1ZGZkMWFjODQ4NGQzZGUyNzEyMjVlOWMwZDNiNTRlY2IxMzE1NWU3ZDQ4NTU2NDQ5MTAyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "O9S8EEhjBAarnVkqdfv57.2sszRGsBK.F.wNd9VEoO8-1791969371-1.2.1.1-dYFs.wrJZd_a8iFvFcWHnxV0w2XLDBU5gu08qN.I6B7m6wztNHbb5WfXeVMm2pvZawerKSlPT88adXkrpFBHm1FxKxFaG4WkHIFElTaLqxYl6pEuzv28MOQLywOBDP1dSf1KRr5iHRY_UrGOqSfw7yUbsYetusRI1mZXgZTUcbP5fcS_dRqUP0yVCvUp7fOql6AJS89YpaOvJjKm.uEIfaRBEdmgUVh3.V0svFTcA1RbezMQSke0IJ6avO1P4dfoMgMiKOdu6ukTqqjPc0bz0feDRsbWbqMKd1gp17DNcE1N1Q4J6dYcepH6UpEAMyfq_FjvMeaWs7eVrtBS2g6X3X0UXHAU8OP2SQIMLI2pDeVNNvLSkDC_74568z0p.cw3H8hSf2Ab1OPZljIK2VCGQl6hmWDSIbTt_Uqb6Ogbts8TrRT.E11K7hO6oIdH8nzr4PwgnTioseVF.i2u8ZAF97cNV24YPUhRW9u.bVQHtSAYvZt7lIqFFWu2X3Y72uLnFt4Q8kM8Ky2y0SQe.Qa4rw",
    "XSRF-TOKEN": "eyJpdiI6IjRKWWRXd254NVFzTmY1SDB0Ryt6Z3c9PSIsInZhbHVlIjoiQnppNVJDNGVUeEZjSnpCclhXQUtUNWcvQk1oMHIybC9oRUdHSFhZdnhtcVJQd1lLYjBaaHhSdlJtZXVUT3BjaUplN1lwR0tiWDU1d3doc0E5bUFhZERaMDJ2NEc2ZlZSTHJUSGVyV1RlZjNwSitlaUs0RUpiNE16WllUZjkrZnIiLCJtYWMiOiJkNTk0ZWJkNzllNmU1MTcxYjQzMmIzMTU2MWE1M2QzMTAxYTJjZmZjNmE4ZjQ2YmZmYTdhYWM5OWQ1MGE5OWExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVIZHRDMjZCdnlzR0NnWTlEdEQ1ckE9PSIsInZhbHVlIjoiVkx0VTZmR0I3NEx6aU82S29ZQmNzZ1FVbFM3d0NZUFBpanJrMXZyTTdMY2p4Sk9LTUs1Z2ZRbU5jQnJBY2tCOE1jaUNOQzlBRkJYTE05UDJCeUJBZVYyTUtkdndxcEdQZEgwSDZqTEZ2b0QrSGlScFErYlp1Y21Kd0pWbnNoWnoiLCJtYWMiOiI1ZDU1Y2M2YzMwZjUxYmJhZjY2ODAyNWU1YWJkZTgzOGZjNzM0OTMwZGViNmI3ZmJhYzA3ODFlYzI2YTQyNzhmIiwidGFnIjoiIn0%3D",
}

