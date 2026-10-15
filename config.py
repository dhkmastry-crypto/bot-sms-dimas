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
    "cf_clearance": "ha.kQbBnYJbjlLRpa.DHLLHdv0C3RCLNgzk6j_cUE9A-1792037365-1.2.1.1-sKCHjtM26XJR3JpsUi.a59gWya26cKzYXBwphw2kAyhfFN4vmko08W4Ho6HM8us6AB1kaRE0syP5TQ_cC8AQ8RnQh.A3iMHQ1p7HxwPvPnWiLUDv._0tUyCtjx6c7.CMWXLjlJ6MJiIcJR5iN40iUrE3i6m3YAuzjmvgmOWpOcUD2el50l2k5RpJ1cRceVDM9Q2J7JXFRVo1l5_cYabIiGh_eeedzYRVom5LZM4s.jQSWAqrm6XEfa2TZi7HDgJA1a8P6OYMx9yjXrqPoV_W6f1qgwGTVS9Yb3wnKvMS6gDHqNLigG.MULcdHro6lA9Q0.AOQzszhhh1pm5lvPPCQqo5uGdhSV9TVLK5N27LejONkBy.ONzk44u5scpeTISHBkxZyPHl0LNBuJwWGJe3WboqrWgw_CZbnLmwba_RCJvbMZVljnxJlMQt5JvmQrBRbaUOQ_IW.a_QRE5AP0liu.gp7YyOM46ckB94_LVA1hXN8NeL0Scl.CMQjq5Zz6THZ0YCa3ezMvRIL_Psxin8CQ",
    "XSRF-TOKEN": "eyJpdiI6IlNiWEhERmVvYWhHbWxnbHZneVl1ZXc9PSIsInZhbHVlIjoicEp0M2F5TjlyZVk3QnZnOGVKRjFWY2ROOER3ZXNpUERObEtXNWk2NmNrUkUxYVBTaU13VERodFlrc1JReHliN0JiM0JhbFNJdVhCVTJySjVyQ3hoYlpjaElsQnVERXpYWG15TERhWGxPMkVCNncxR2picDYrVEc0aFFxRlVLd1giLCJtYWMiOiJmMzA2ZDcyMzUwYzZlNjc5YTc4NWY0YTBhYjUzMmVkNWFiMTVmM2I5YmJmZTI0M2E2YTMwZTJiNzRlYjFlMTkwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InBndDVJbTF1UGNXWVhzNXNsVGJNZUE9PSIsInZhbHVlIjoiV2Z3L05wTHJGS2JLYnZ3NTgwaG12QjFFaUFUMmVzcmtpMmxyRUJyYUhXNEszRlZrcWlscWxZNXR1TmZRNlh0OGxHbWdqdnZqRC9tYk9zWk1GajUvZ3NtSThGR0h3czdzTFpsQlVITng3aGd1TCt0UkF6dlhFSHJ6cjZaSXdvOHQiLCJtYWMiOiI1MTkyNDM5NzNkNjRlOTA5MzVkMGI1NWUxNWQ0MDc4NjBkMDBjM2FlNTdlNzA0Mzk2ZWUxMTcwMGQ5MWI1MmM2IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "OmWHd9yTq.3nS.W73Us6iHjhr4qbD5TRCMUO.x.iqd8-1792037353-1.2.1.1-I6NtNTBXvgMfNcRpJvNwzCth.xVbmm5FMjeK8q3wSMJDWD3mgMrTvetTYTFJnZpSdBLfnyxCSCrtiaWsEZynMG4JutE5siirozlNPqonZ1SGzoOaiKNQVfVdaVvkdjbv01Li_GqmWQ04yq1qGnBZbuKGqpvTWrAdQtfT2TF7h9Mqtb1o2fMLw2JuVbyrGrfO.5f_Dax4mQRXIFhRy8fgxrauwp8Jtn5IvaxevqadQQm_MnDtLjznMzLQoA.XT3lHUYWN8RMcU.Pk4j3qV9ilH4oZ1pJRX2sAsey5ESfD.5loxu1mhblX5u74J.TqqpPmBPopBg1oCfVa6MDnt7FsjcpUkzaJClFYFCbvMoqEwA8MqMFhdtoq1.TsGHSVAc096G6GzC2P7jjWLNmeI1i7KACidtWq3.oHZ3hmteysprrtnNxga8.npd_ebZTUZfvkQPOpJPPF5TeC_6ZdiltmZg7vLAPzSeh4YPLqTF0IhWjZ.VM2NcUKnZnZBoXT51Eu2lFZ.MnmjjbLTyJdMyD2rQ",
    "XSRF-TOKEN": "eyJpdiI6Ikx1RzBrTU9BZVRlNVh2WU5kMElwY0E9PSIsInZhbHVlIjoiUHFoamZnTUx5MTBia2N4MFRONlJiOHZUQS84OWVpaDk4d3RXeVlyQkJhZ0p0NFJQYkFBdTdkNzI3UngzOUxWeXFLVWJ4bW1FNmZWR0R6aWdZZE1TaGc4QytoMG82UlRVRGsrT2FyNTdiL1lYZmo0NVM5UmdNMVVtS1N6eXVOZm4iLCJtYWMiOiIwYjhmMDhiZmEzMWZlOTEwNWE3YmUwYWM3MDljODA1MDY5YmNiNWVlMGU5MmJhNjJmZmFjZjAzYTNjNDdkM2ZiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikx6a2c0cjdOMXhqeUNpSUVHdkQrb3c9PSIsInZhbHVlIjoiSDVtWG5UT2xDUGZEaUdyMll5QW1sU3VtK2lESWVqRlR0M09TMTlQbDlRNTYzVS9MN25yY08vdXBzRWdpWllCOGNDdVBWRTNqS2ZxZWRhMnNOeDBndHFvL1Z6MDZOczdxcnZzQlZNWWZacC8rd3kreGcxS2g5VUhDYU5kUnpvdzciLCJtYWMiOiJlNmRkNjczMDY4M2MyMDBiYTdlMjlmNWRmN2RmYWI5MmI2ZTA5NWMyZjkxYjczZTgzOGI2MGMxMzI0MTUzYTM2IiwidGFnIjoiIn0%3D",
}

