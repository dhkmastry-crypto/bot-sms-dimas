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
    "cf_clearance": "mUsakqbH0jWsA5OAb54GJymtHvKfUKoXo6fqDf1JsZQ-1792058308-1.2.1.1-3byqiULVxNukMm3EyOoXirkR7ZeNeNw9xZqeN4cmcGwPsW47eYXLw6wb0SBL_FX4_IypQtLqksKdG0Rdtmw41AxY_fLj0jwqeJ0qfDCFE1u0dvBaHFN1P6KeBKiQfslEPeugpztK3i2KFGmpYRUAnLm2_GMP307DZrk0zBaiw3ieWId_VWQUuI50F9HwlpgqWW4HAw46MRkOlXYXg9KKarztpnLDOF_H0N.RT635pJoFsaNWliHQgeo0_EExpQ3TJVfPRuFK9d6Awn6lm.5Zgu1Zc8wiAtLpvMygwcmRqVKZ5jp4lxIc..t9hZquyyCedIJEYo.lvorFhB2C3X22isdU_GViehEo9Cb7CTRMSUkg0Te0lg2P74dO_CcUCWbHgGTZRuDpHtOTpPUG1fEyjrFBoqMlu7shh4QDPfN3M4qHqscUx8zpbironj61YqZdhY99ujZM5PFjVOcF6BFHD8rOAJTVCSILON0d1Xonu5OcAMSeK4iFkH02wGZe.5Drv8_QzKKALDaW5GZ0cQ4b4A",
    "XSRF-TOKEN": "eyJpdiI6IkZhNzBvM21acFF0d1lTbndHWnJOMnc9PSIsInZhbHVlIjoidW94SEprenZ6Q01rQmxncmkvT3ZGcm5oMDlPb040aHFDSi9lQjR2VW1DS3JJeFJNUEFmZDFpdWRlbUorb1FsbDYyaU53VWRibWl5STRmbm1iZFhxMXJPMy9WTVBndDVHYzdUd1VaSWtGOG5xOUlRdzU5UVlZTG5Hc1VnaW5qUHAiLCJtYWMiOiI2YjIzZjI3ZTkxNDIxMDI0MzE0Y2NiZjIyZTU0OGQ0NGU0ZTQwY2JkOTQ1NWQxMWMwYTU1YjdhNDY0NjJjNjdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjR4SW1LRXIzK1d4QTV4Tm1BYU9iMlE9PSIsInZhbHVlIjoiTy9rQlJLaGNXVFExbmZPU21VYkxKaG9rRGsxSUsxSVpWRzRBS1lKSUZDcUdjQndJOVA4aVZ2Ym5nYUVLRHBvZEljVGlNRGQyVXhTZXFkWnZpRFhMc1h3U3g5V041SkRyV1RzbXlQUkZLSmREd0tPU0ZuREVqWEhFTHhnYUR4YmwiLCJtYWMiOiIyMGJmOWQ2NzE0OGNkNjgyMDljZDA1NmU0OWVhODYxMjBmZmE5NzJhYmM3NTQ5Njk0MjQ5Mjk5MThlYmRkYTA0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "X3hXAG6jD5yQMpSa1nGDe0ssNCDgzBlMuAWT6_B6UTk-1792060076-1.2.1.1-fGEI6G751y7E6a6Ml2Gc5.T5lsZbHDLrCapg.ZuGCgZIaIMLXehmGXDe2NVoCPDFg3dyDSSWFxI2BgtqraVOMM8seWs9dOGTu18_1ZEFeeH5uoVJeqhNk7J7_AkhBPRerq.CXWLEnezf611AJ8nQUG3yn4f_3B45BI5EzRN0RpXcOB6nxUNwzV55zqBLc8XEohW83lYJs0bwMu5jn9AFkZiZOiKTj8h4DP3n0Ws3kSDiZif3hruelUNzailRwRjxJgJI8KidcFeWtgldGc72BfLZUiQOA8tHSuyFytg_y2Rv2Wrv22v8dvz18GhaJlST5V0p8gojidFSdjKM_QIBHEGdPRgC_DYH3O4BFV_4OEDG6XgrhYnL9e4.K2z5vHxRyoY.8TD0RG64fpahLKwXQXEzuZCF5EufsJqAuBscgHzAvI.GvlT8T7lbFUWBPTaWEt6sG_KSJnVZZ.8hC._Xy7bRFWdB7TvtoEoy7evZqf6sU23nNBpDHFKKJ.kTnm2SzeC9aw_5zxPWDWD.Z_dtiw",
    "XSRF-TOKEN": "eyJpdiI6InE4S3lHRDY4ZTArdm5OZGplTDV3QUE9PSIsInZhbHVlIjoiUnRvZDFoU1huU1RUT3ZWRlhQZkJTQm1sTi9oSTRRMWh2K2FRaDQ1Nk4yTDNRMjhVeitWc3JpemZBODE3bFM4NXNZNjdNT2xwZzAvMHBMYmtONkpoNi9Ra2xqMFE0SkM1aUtFNDVFeW93czBNUE5wdldJTkNBK2pxOEJhR05UTHciLCJtYWMiOiI3ODI1MDk0ZmI5Nzc1Y2E4NGNiMjFhYjNmYjA5ZmYwNDkwMDg0NWVhYzExNGQwNmYxMTNiMDQ0NmI1YjQ1NTdjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImRmVzVwZTYrTkoxbmwzZWRxdFZkTVE9PSIsInZhbHVlIjoibldHNlRkbDBhbnpWcU9sQ0FxdW1La25YTnZmUzJhN2hzMysyYzAxTmFjYWJGOG5nZGJza1ZWZXNjc2tzRzg5SEk2b25VZ3dKTENUZ2lWYjdGNk1ycS9DUCt0a2FINHZwRWlqZlVxa3RhRjVtejZZbjVocjBucVhKV0poYXF4bmgiLCJtYWMiOiI5NzdlNDM2ODM5NTU1OWIxNWM5ZGMwNTRkZDNiYWQ1MDkyZjZmZGUyNGZhODk0MDEyZjMyOGExN2M5OThkZDFlIiwidGFnIjoiIn0%3D",
}

