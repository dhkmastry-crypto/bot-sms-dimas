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
    "cf_clearance": "CqUjQ00bkA1elOyeA4tl7qFo0aM3gjUStCl274mcM2M-1792060118-1.2.1.1-iNl7fHFOvlctLENbDH55yU1Tre04Gx35BcxXdlRGPFvzrke9LSRCRXqeH5VpqBMNjvodZn8UA7FLNVaIpTc4i6XTRB.B97sZ.RQcTExYZ0GkaBqy8yvN958gB1k8yxps2s3gkwgl4KrPUhWmSQ6VlgsWCr4HHobKVu7yhU0k65GuqhpBBgCNw5jJ3arqGyUyrABCR41_F2dbzns22H_JFURwVwh2Jn3R3xiHuAGakR6kwNSM78Ex1KBNkYefJEwYRgDiS90sfPPTJmq17kj3.cGsq08.ZileOhVenhPhbnbvCHRZogAtw.eekZMNInaCryHNwSVSsbdqmvPnZefdg4jc4rcOhBKe4WSdlBOTXa5JHWj2PD8Huwvj3f3_KeOmhnAuBw03C5YsphaFGsdoZQxyY4xfgfHeUmgsg7tE9Zi3gv.joEZlp6z6_AIdK4rMG7doMbl2B6fGIcVbYa06B8xAi8AsMoi0jYK70NClT7l6lrN38MsL3D4D3TtwfPoKF7YdbvdtBRdWNF9O9riChw",
    "XSRF-TOKEN": "eyJpdiI6InFXVmtXZkFGUUhEOVpETC9FbjRVQlE9PSIsInZhbHVlIjoicGVyV1NWRDZNdXVwSU5hZ3lFdTZVTlgvZjd3b20xc29XZ0gyam5FaGVPSVczeS9nT1FjV0FKbkJvbk54cnNZbFlmWjJQMm15R1dabmJjS3NWTmhMc0kzaHJuVHhxWTZMN0d0VllWZlZtQ0tuVzVkK01XNHBySFFSbzI2N0tJYlQiLCJtYWMiOiI3YzA1NDJkNTU0OTljMTQ0ZmJmZWEyNzBlMDQ3N2NmYWY5ZWZmZjA0ZDE3YjVlMGY2MzZkZWRjNzBjZjc0YTg0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im52QldHQUxsMmpZU0tCWmV5NUJBdGc9PSIsInZhbHVlIjoiZ0xQQmd1Q0dSQVp5MklqWDc0LzBYTGVMUzZFQmxtd0wyYWk2YmZuNjlrQi92NUs4V3loNFFoUFZwb29oQ1pCVHVUeVlJZ1J3QkcwejNZWGZhei9EUDZ0UFl3NWpTd1VJc3NXaTJDQWxGV01QeVJSTWlsSzNTVzJmbVR0WWI3RXAiLCJtYWMiOiI0OWVmM2E5NTc2M2ZkYjlkMTJkZjk0NjdkNDhjZTJkYTRiNDA4ZDVmMmVjMTU5Mjg5Y2Y2MTVmNzFmMTgzMGI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "X3hXAG6jD5yQMpSa1nGDe0ssNCDgzBlMuAWT6_B6UTk-1792060076-1.2.1.1-fGEI6G751y7E6a6Ml2Gc5.T5lsZbHDLrCapg.ZuGCgZIaIMLXehmGXDe2NVoCPDFg3dyDSSWFxI2BgtqraVOMM8seWs9dOGTu18_1ZEFeeH5uoVJeqhNk7J7_AkhBPRerq.CXWLEnezf611AJ8nQUG3yn4f_3B45BI5EzRN0RpXcOB6nxUNwzV55zqBLc8XEohW83lYJs0bwMu5jn9AFkZiZOiKTj8h4DP3n0Ws3kSDiZif3hruelUNzailRwRjxJgJI8KidcFeWtgldGc72BfLZUiQOA8tHSuyFytg_y2Rv2Wrv22v8dvz18GhaJlST5V0p8gojidFSdjKM_QIBHEGdPRgC_DYH3O4BFV_4OEDG6XgrhYnL9e4.K2z5vHxRyoY.8TD0RG64fpahLKwXQXEzuZCF5EufsJqAuBscgHzAvI.GvlT8T7lbFUWBPTaWEt6sG_KSJnVZZ.8hC._Xy7bRFWdB7TvtoEoy7evZqf6sU23nNBpDHFKKJ.kTnm2SzeC9aw_5zxPWDWD.Z_dtiw",
    "XSRF-TOKEN": "eyJpdiI6InE4S3lHRDY4ZTArdm5OZGplTDV3QUE9PSIsInZhbHVlIjoiUnRvZDFoU1huU1RUT3ZWRlhQZkJTQm1sTi9oSTRRMWh2K2FRaDQ1Nk4yTDNRMjhVeitWc3JpemZBODE3bFM4NXNZNjdNT2xwZzAvMHBMYmtONkpoNi9Ra2xqMFE0SkM1aUtFNDVFeW93czBNUE5wdldJTkNBK2pxOEJhR05UTHciLCJtYWMiOiI3ODI1MDk0ZmI5Nzc1Y2E4NGNiMjFhYjNmYjA5ZmYwNDkwMDg0NWVhYzExNGQwNmYxMTNiMDQ0NmI1YjQ1NTdjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImRmVzVwZTYrTkoxbmwzZWRxdFZkTVE9PSIsInZhbHVlIjoibldHNlRkbDBhbnpWcU9sQ0FxdW1La25YTnZmUzJhN2hzMysyYzAxTmFjYWJGOG5nZGJza1ZWZXNjc2tzRzg5SEk2b25VZ3dKTENUZ2lWYjdGNk1ycS9DUCt0a2FINHZwRWlqZlVxa3RhRjVtejZZbjVocjBucVhKV0poYXF4bmgiLCJtYWMiOiI5NzdlNDM2ODM5NTU1OWIxNWM5ZGMwNTRkZDNiYWQ1MDkyZjZmZGUyNGZhODk0MDEyZjMyOGExN2M5OThkZDFlIiwidGFnIjoiIn0%3D",
}

