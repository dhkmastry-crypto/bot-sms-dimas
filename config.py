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
    "cf_clearance": "jR31xyELaA5Jm9KMhrPc8rOYOI60QuFhcRZFGHQTwjg-1791967557-1.2.1.1-kJ0DwyRT8RRt5fRKXJKgMbBjD74k9_1IbDfu1ztlWU0XoE_0w2THgn15ATvoFED1tWz2yuTUpt3.AnzRgL.8yLxMVSmyOlB3SRNVuxdGXaCvZwu5yiXBDRNmEZA4zvA9VM_zXsP7LHoMO2heVzB7mzCUFJI65OpoRRpQq2v880z2tTy6oTe9Flq0K8x_3X6ieVtp4tGduV6m_F3VBTct1xxZzajkf8mIsHKimOeykZ3N19PnHyWanFCdq_E1ojA3haDd_5ytrOoHe5LMqbzwSyoazOZnApOELcVX1sYGCGlcT1QB1CrQroHvTBksv.Xll99HC.z4sNFlS8YXrOE8csUW4.cQqd4ynMtuV7LNXm7piGVvNtovbR1p4GAHxhKQW1MGE1IlsDBCJFaoYMZOxOmEPaT3GKyGtF7Izc2fOY2YDtOWmlTw0oP7wz_8u0drpSU7.8OpKtvp9ig9KfmOwco8ubS0bskKAqb.l0lhRMWy5MhJLHUpAnyqVheCAlYGuJ7ke2Tc_Ed3cCEJqHrWAA",
    "XSRF-TOKEN": "eyJpdiI6IlVtRU5FRzVnQ1R5bHBZZHN4VTJLYUE9PSIsInZhbHVlIjoiZm1DazV5bjcwcURoTFJTWUpES1JXaXU3aXAvRTNKZGpWVy9CTHVMdHdxWWZLTldnLzNuWmpkWUh2Y3YzRHJLL05LSE1TdkY2b0xnNzlzMkhaKzNveEJ3WGltRVh1VjdPSzZwdkdhNndQSjdNQjJtd1JPdy81NWFSYWRrN0RkdSsiLCJtYWMiOiJmYjA2Njk3ZGYyZjUzNmE4YmE1NzRjYWQ1OWYyYzFhMGU3NjY2ZmE5YmI1Nzc4NjE2NWIyNzk3NTk3ZDdjNzhjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJXTlZyMGRvUjVvUGlXY01ISHVBRFE9PSIsInZhbHVlIjoiNllWU1EzSmlwZlQ3YVlYV1NjVW1seTIvY2c3VkNQV0haY0JVcTFsZmNEbFdtNnNDMzJVUmYrT0JsK3FJYVVidDZJNGRWdTQxdVUxQzRwY3cyUHlvdW1GNTdBbTBqWGVUV2U1Nk03Nk5FYllaVEJwT3d5NUs0Q2dVZ2pUQTJzWDgiLCJtYWMiOiJiOTQ3MGVhZTI2MmU5ZmM2YzQ1YmU0ZmYyY2UwZmE1YTc2ZjY1NmJjMmM5MzMwNGViNWQ3MTc1ZGIxMDg4NmZlIiwidGFnIjoiIn0%3D",
}

