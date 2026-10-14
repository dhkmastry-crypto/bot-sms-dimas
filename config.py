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
    "cf_clearance": "Gt1pVzmr3XPPASXnt21DWE6gPqj.NHSrdCd8OvNoidI-1791983783-1.2.1.1-I2Bp6wbVZNueQLcr19LV6hOpIiqWW.5RWaIwOAoMsgyXV6U8gvxW35ZcwfxInOx7jkowcR3eyBl6K_QJ9X.Ok8Ucf1pnPYGpFez4sPrnUKPdzt0VWz0b3gJPvoP.kuZtZbZ91IXqsb4F3wCGtttTUc9HlC2m6tVwzji71ImKzTLKaSobImlzWZ4_vcqh7P0tQ9CXGgwUvv3oCkpuGdFSuDagFbu2iV9_L_BsuYBPop8sWknWi.bldULy3_AoCr8Vwneeqri8_mxHrsdoqL52E3mtQGG.GvukgY1WqrhZ.6rrfokq10YOoIoX7HTnJ_F5maQS.rBGUmyjGWJHEzZ7x76A1p6_.tUknzdxFDUY5Ez1neV5zov3PUD5EjXp.EGLOhLyh1gQeF0F9cADfO87rnAfJDeosdHEXGTKGnMgnvJfbJ4PY.PIX3hDRfVZtpHwh2RRExyjnH7Sp9OXWSl.FlUqPouCLnLXLTEEuWcHIm0dm6nKNOw5ud8WYyMdblVEgUTXMvEEkUiO9F4j_I5VGQ",
    "XSRF-TOKEN": "eyJpdiI6ImFPcnFsLzR3eUpkR0hMZERNRDFVL1E9PSIsInZhbHVlIjoiZHhLNk9CNmxFanlrMjNZSmxPTkpIaUFlcjNWbTlQUGFGN1N3dC9OazZMdFNIWW42T3dydlFQMndMcUF4TW9icXRoTEM1N0oxOUR6Y1UrcEVhNmxQcmd0L0VRdW1kYWlqWnJmNS8vWldiTmdCOERUb1c0QkhsS2ZINUM4NnowWUoiLCJtYWMiOiI1MjBmYjM4ZDUyZjkzOWNiYzFkYTZjOTk4MTAyYmNmN2RiMmI5NmNjZjkxMDA3OGQ1ODdlNjEwYjVmZTg1NWQ3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImlLNTlEWTQzdkEwamdYa3d3eHNRa2c9PSIsInZhbHVlIjoiZTRrWGd0WSswc0hWcDNzc0pRaE52dFlNaDVyazBKTzVVc1pLb01BbTEyUnBzd0VLMXhEalpDcHZCREwzNVpBdjR3L3d3dVJ6WXFvd1BLOUhDZ1dNYXNMSEpabC9mRXRuV0t2cjdsWlZTZ1h3RHl4MlEzUFRzdnlLczYvQ3ZvNTIiLCJtYWMiOiIwZDVmYzIwMzc4ZmFjZWYzZDBmNzE3YjM1ZGRjMWExYzEzMjA5OGE1NTFjMTA5YWY5NmU5ODI0MzVlYTkyYTJiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "hJN4V8Y98GvxUkHBfMhcB.6I7ng3bPpk7Rw41xQE3VU-1791983848-1.2.1.1-bkuGJ.nti.BJdTRfdnG2pa5JtbvMhutqTAgZg91_AINsw4zqZEkxR5_PhhaJSzAWTjcjsit_cX.Bm_TL8IMmL1Y55GaMX.lymlcG94.i2LgNAMxJ94dRJRDrCRRaydeChokBy5IhDbposlJ8KaMKAw15NWQVRNS57xz1o1xYI1o4pNqDei0q46YEVpdVJnUIF7paH6fdC_k3UfKmrntj9B4fxjTof2RlWl5doKfv1ND7MXUrS4RjuKrhkNS8lYszMzzRoliJVDtf87tF280l2N4LLVrUtAXQ9D6Y7P11tddr7KVT6j7FD1G6dkJkzM7jp2c0OYWo1vRkEUUDzH8UJI34k9M2TC5RubnOriZQiDgS6bCtOmSkqrE2t6h5X4goWIeH_AZEb4NcCwq4rIr4dKGxlO7LWPpLRJ4Zu7NCNU7F65Riuxxt63t1nCEW16HpRmuV488yfb4aduIxBmKp8HxI3zlbAhsnCrenXSzBfc6wQMknNXt6k09rHUGPk9nc39To9Cz1Umy0FqKuz1skHA",
    "XSRF-TOKEN": "eyJpdiI6IlZHSUh0NW5rbHdnZXRhUUVJRklSN0E9PSIsInZhbHVlIjoiTUNCZ2lKWEZOZnloN1NVM3ZTYTZPajA0Q1NMbDdZZ0w1ekZFaWVkVTdaLzZXWGM1YzlEOEhIN093SDdaUnk5VlVtSStSbkxGNyszaXJNWk9Da211Z1dzUTFXUWRQRWgvYWxnL1NOakgrN3k3TFBBLy9ML1JBcHlBMTM1dkQxUFMiLCJtYWMiOiIyN2ZlOTU2N2NhMTNmNjQ5ZTA2NGYxOGQxZDM2NjA1ZTBiN2Y1NzE1MmYwMWFmYmFlOGVkZGMxMmU0ZWIwYmI4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ink2bzFDdnpwNk1pNU83cnozTmR3TUE9PSIsInZhbHVlIjoieldkeENkSDMzSmlJdnFOd0pPbXo3MW5QdTZaRTFnUHl2ZERxYXJOV3V5Y2pGYkJWb2ZhS1NBVCtNamQ2NklKVCsyaDJIOGYzbXRSdDAybnFrYjJraTlBRlJNY2dxNUUvZWdLdWM0U0F2TGtaY1RxOHdXaURxRStpeWZzU04zR3EiLCJtYWMiOiI2NGMxOGFkMzY5ODA1NjI1NTk1M2EyNmFjZDYzMGIzNGUzYmM1NWRmZjY4NDZlYjhmNGYyNmE5ZDBjODgzYzkxIiwidGFnIjoiIn0%3D",
}

