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
    "cf_clearance": "v7c6GYEghF16kaf2AqoDfz1VZpS4ntYCbLVT26nuuX4-1791985587-1.2.1.1-EEJhWDLdXdbFKF.QTaPCZQZJdHDGpbgTPr8j2nIHRg_Ip9E9dxnDD6pgjIU8V2nZeuDYs8FKGaOlkpEYUZkiUOy8cw2WdbFiQCkWzi1PcoOxccT20pFnUF2z_Pi3lxbH3iEir.1XDB784QBM3UHAmIHkm_pRnIkQZa0LHOTNyOBe5JrR51jag_fI3mCjMmWNiQBU3ACpLM66yJkAe31VGS28n87i62vhY7l.2kE_14IZzSVXGi7x3xUoMakHt3H0PlmGvF72BCyqDshy.HnEwtA4W9J5MOh6VNW4Ynv5fDnAhTPhIPBKosRgiBDL1eS_zl.8qB7k5n_PEWNtEkzBbMbanQSz29Vdc5PxdZ1DH1wsJwIj4K2AaRNCSxCHTokZpqhimzoLSMfWUNRVbWMTyQIbyl.XlyMFb9Q9pz2UjZ0xyZe2lR.l9mOARG1vXJULP1n73L8UT1MTdRnK1LTSVJz3qVF770AnbYLWFJfpf0YOV__cIHsSkuWiJcPE5o_6n4MPMuncrsb8FZ9xid4S1A",
    "XSRF-TOKEN": "eyJpdiI6IlNrTlpXdkdrMHVkMVNPSkdyUGY2ZUE9PSIsInZhbHVlIjoiQjliTlhNcDBHTFRiNkMvTS9EM2Y5dGxxTTZMT05BcGNLdXo3MUYwYzQxckVWVWd4N0NVMnJ4LzUydW5vQ29BakZ4UzFLWkdHRlNhY1pDZlRBenVjZWx2alRqQVlCMExjZkdJalM0eG9Kc2dxYUNIcTNyM0pYYTlZOTlRME5tYnYiLCJtYWMiOiIyY2QwODQ1NjExYzc1Mzk3MDY3YTVjYjQzZWMzNjM1YmE4MWQzODM1ZWY5ZjUxZThhZmMxYjM0YzY4NGFkNDVjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRRckIyUm1LdmVzQktlbUczeVo1ZUE9PSIsInZhbHVlIjoibXorNkFTL3FRazZ6UmRQT041T2RDdFk1Mk9Cb3NjOTkzQ3Jyc1NsdnFXSnVFZ0NqNnlkU1VqaE1tcVRrUTRiMnlpb1ZZQVh0blZrdzdNaXRkN3ExeUtMeU1YdTBCZ1ExWTJYRUZYeStnc1UzRTVXRDZ5SlVVRnFBRkZJc1NHYXUiLCJtYWMiOiI3ODkzOTIzMmI1YmY3ZTYzMGRiYjM0MGNjZWNhYTRmMmZjNzU4MWM2ZjNiODY3NjBhMDY1MjhiNWM0YjM5OTQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "LA9By.s3wDodFjmdlRDG6Oreyu8i2irTcnJUqz__h4s-1791985653-1.2.1.1-UCYuKEggaDzNuxLfqM1oFepQAVZZfp.fAo4zrs0bSksL77WrGXqm0vi7lHurIxwAJopSP49NQWahQT7UuWk9tvHS7kCelpQjsQzCDJ9Lovd.BiiZqtKvrP6kRSRNySYNyS3rNso2z95tOxV5GO3e9QUS2Ro05kXudyL4vF7bTqmU3D4AeUHWbVu.qHIrxwBQ8gMBm62ChVykYzCdtMH3T5TqQvqVABHXxBQpfr.XZFDk.l.INGqhrsKv5NRCecFi8.D4svs00PuZX9xvM.ITVzegFsU3JlGK7KaKzSdyNnIN6WoajTkYlUH6VMI0peh8wrIbnqIbdMgk09GXj9XTf5wQ0TKmnA38idKikR1NMfLbCb68R2RHcN8Y5ObVGyY3HI.96XlCM.BIfWV8UxGho7ylHy0UoSD4NVmxLQyZJ2PS.YcY1HVWkiPHGMLA33r37dv9VUu2cBQK.CfG5x0IsV7cp8MCT0YwwnqghtRUpWXAzHbG7vWwveaf4nwaCDA.aElSkBKke8I.K13jZ6J6Tw",
    "XSRF-TOKEN": "eyJpdiI6ImdGSFFTeDcxT3RJOTBoeWxuWUU3dXc9PSIsInZhbHVlIjoiQ0VUQjcvS3BNaUdqNTkyb2tjcFdIdVBMOElrbUFidk0xN0dOc1dVMnFyTVJRQ1c5bTVGUGJ0K1g1VnRkRGFrQi9hUlU5cmRFWDdmM2lWZlZkUTdnclloUW9NNFZMT2FrU2FZZXh5anRXQlFyOWJWdXliZlZ1eExoV1diRnVFS1kiLCJtYWMiOiJlMTlhM2FlYzI4NmVlNTE3YzZmNmRjY2IwMDY1ZGFmOGY5MmUwMzY3NTFiNDI0MTIxNWIwODk4ZGYwMjk4ZjJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im0rdXFJWmlzM3hKVjgvNXV1cVlXQnc9PSIsInZhbHVlIjoiUHlzRS9OanhtZ21nNTJUdWdySHFwblh4RDlxdFVQY1NMcURSTGY2bmdlSjhFNnlOVzlzYTBUMWxwaVdJSVVoaTg2Uml1NnlDeHArQnErNmxIT2JhL1dweWw5YTRYZFlOMkpjYU5sRjJ5N0ZZRDZvWWRqUVZ0U1NDSTFVTlZDZ0MiLCJtYWMiOiJiYzE5ZDc3NzNlNDMyYTg2ZWY1MTQzNDMzODk4YjkyYzk4OWZhZGIzMGM4MTZjNGVjNDA3MzBjYTJhMmExZWMxIiwidGFnIjoiIn0%3D",
}

