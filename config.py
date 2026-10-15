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
    "cf_clearance": "pJ_H0amrkLCkVNR071kBwZgoFGtoGdR48JhNzAoTlW8-1792105349-1.2.1.1-sX427xYmNZArjsYrjKFYv2PULgPC8dgtx51sJsjDyNcrCxaKfxxWj9S0vi35K4esu0L5HsbUBi2.MjyQVzdm_93dyUg__GwlHNiahH6lyryiknt9A0Yl1zFzwubP5csC1cQYYO3kYREUuTkSkn273hanHsfF5ar1_D1ZLxnQfOqfhYdE8eaw.Poc4VTj_MjtZ0Jj9v8vVvvUgo0TrWIWKKv9xki6tnvYLIxRvb53VbY9Zfpu9TYes6kwgRqQ8sueQJkFXdrsG4wcsVP24FgbrszEEuKaAlqjJDihpQRN_2NsOi8e32QTl2sldny.gciEiTKlB4xsdgBRE5ZzM2StD2E9DR63dBrG5N0By0JxNUm_MeE9D7Us7Pmvxm.JIvoc6I8FZAStktDYBZxYzWEGPAq_8qJSmFBpfFor_3pDVW35eGi0uTjX19cOnJNQFQSHmacTkg8I7CINhn1AR.zkiX.0SWBtTvA6SKae0D1b8zgZJTujjB.3oji_ufJm9Dau_BjXhL2hlCIR3PipdVnOBA",
    "XSRF-TOKEN": "eyJpdiI6IkNMOXZoR3JUMXg4L014aUpFUHAwUHc9PSIsInZhbHVlIjoieXJKVVZoNDh2dGxTUHVQUHB0Wlh2V2l1enpiK2hZNUdFZlErNjhPTXNyeE1vYnpvS2tueGhSelRVc0ZnYmtlTEQrWGFrbGZsVXozYTBrWTMrN0VxZG9kcU5VTEhTcjNxQWZpZXFNcTZZSE5nejBNdlhIeEsxMjQwQW1PRUZBeVEiLCJtYWMiOiJmZThmMDFjZDhiZWVjNTc0MmU3YTM4ZTNlMjcxNmI2NWNiZDNhYjhhMTM2NzQyOWE5YjkyNjhhMjBlN2YzZDcwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhFK1FNaWtOVWtWQk5LY1pzNEV2OFE9PSIsInZhbHVlIjoiNGQzTVBIQnZmdnhrRG14S01HQVJVQm54VDhBNGhrOVNoZWRURG5ZQWRuUklsWFBRRlBLSGkvVkJTUUxzMGJBMVUwQlRyZkVjYldTdDg3TGxTMVhCMHFGVCtuWHVKWE84L3BMSXZuOERxNitiZHA2WDNLSVJGZERiMEl0WE9GRCsiLCJtYWMiOiJkMmIwYmQ0Y2VjNzQ3YWNhNDNkYTgxMzc3ZDIwOTk0Zjk0ODc0MDVkN2ZiZmU3NjQ5MWI3ZTM1OWNjNjYxNDJkIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ovGXxqm6gHjwM02kzUPE0m6Yw64Ta7uW3MDfFNOM2CU-1792103580-1.2.1.1-.WqFOGqmDOx.I0S2gszZt90vXHDM9qQQGD3pedbJBt_J7gm9vF3x2tZmY5jIwbRX1yQUGF6L17pHDdIDcCJQ9WQ8JnxY8wBBvkcFWDpAsqLT2UPq1DdqPSz5QoyenTGyPTkB3np0X3.PA1jYXfpidYLnQRjXtoIBFaJ987GDAByHN2elsgZYo.tAxu49rOa.gFk7XdtUYPOCBbKT51vG9B1VoIrv63FfIwkXx8nG0gN.18YGvLTQqJwCn_zilQ7B2vlS3PefnrFYhVTIEjilBr117jm7a1vwj38uMG7dhAkkH7c0hqC7KLKW28w1_0GCy5AYfdblU5_NHzKYJYhw_hd4m0T8ttQGQ89LmaZMeCryy8B_rt7PB3hRKPenYvadaKhOSyA6MwSZNV21nHwlHZcOGV75oyT7GDb8PwxaJFdAoii9vVeBo.Z7LvsYLbgdUPljiZ21ENY6wDUwHuqCmccFxAjcYsXoRtMPtmtXGWdYCQTFcl79PRyn8bjHFwo.j3nm5QSab4lK0lFG8xVyfQ",
    "XSRF-TOKEN": "eyJpdiI6ImVFUU9PNmhtTTZpWXZXRG5SdXVwVmc9PSIsInZhbHVlIjoiaTRHYUtCVDlaWG9lckRVZWtkcTI0UTh6L056WTBIaldmL1FpMnZwRHpTR1JoTjhuQ0J1a09jZEY0YnRUbk5QT3NRSE5BYXZIazlSeHJjTXBTQ2hWM1NFTEtFWWtrVHFYSEFBN1lhWENDbDQxaVU0bVBPU3NScGVONTFNcHZYNWEiLCJtYWMiOiIwMjcyZDY3ZDcwMzM0YTY3OTkyMzhkMzc2YzU5NTI2NTYwMjliZTc1NDE2YTBjZGIzZDYzYTkzZjY3YWMxMzE3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlN1cjB3T2xLQmU4cG1hZmNvelUwekE9PSIsInZhbHVlIjoiTDZIRW94LzczN1NIQXYxT0o1dzVXUHBaSlR1RTJiU24rczl1Y2doVzhCM3hHUkVrOXJLRjF5a3Z1YUdlMVBIRm5sSUdHUGZQVEhuOU5IL1ExWk1wTDdCMm5XOWlSQXZBc21xU3k2T2pPUkhxZUp5VEZYelpyZEJXT3dRNmJFR1IiLCJtYWMiOiI5ODJmZGVlOTdhOGJmNzgyMjZiNmQzNDhkMDc4ZmQ5MWEzMjQ1MjgwN2YwZTY2NDc3OWMyZTE2OTM2OGY4ZTk4IiwidGFnIjoiIn0%3D",
}

