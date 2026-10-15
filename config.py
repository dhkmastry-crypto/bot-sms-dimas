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
    "cf_clearance": "1JzDslUVLszC_2V16somq7urj4vif3Bb87DaOdr57og-1792103538-1.2.1.1-rjNW6YWvuFvlH3JqbI.WdkNB_bzSLfK_G8NDHP8lr1WvbWD0d4UoI9HxO3P0O0xb6z2KdBmph.JOpCiweMIKNZGuzrjakl2xhPFk5Q7Obh5E3yQbSFdT2dLv4UQgWdTEdMJoTgvyV87bxA3NP7noRWxrrgWPIVuFLNasS9kdZp9w82KnWMa2yZew7osEI.bgINBucLVfvqFn8p7Ur1oceRGCpDhVeAG2ZX.OvyiBMX7Q1MrscjaTNYkcAFiCLSt1fl7s8uMsJFHTtl2GURJt99_kmUuyELB3qebvgBO6B7ON3m0wxKJSo0A2h_h7e5gT3mIKz0zCaAYkuh69XJEI0yQQ.aEQDcNg6HHUE_dzOhBY49GUbnDoCVoVv1DKO2_gD5Thw7d..KtgXUZAqwvwROEKshlIkrECRqtKCGqDjDnkVOyhrVeSAXQYT3Y2tNj73xQAVCY4V7QrwQ9xkQumbEDQwOrcPyxAL1GcJIVdbEeWfA6UpRX_qdz8QgZYvq7Y8IiQw7ru2gRiEG6dfBtbNA",
    "XSRF-TOKEN": "eyJpdiI6Ik1Gcit0NHE4SG5ybjVTU2E2NytUUUE9PSIsInZhbHVlIjoiOEx4Z2VmZlZ2bG5GTERkR0NFMDdkSGgvL21Fdm55U3NBaXYxR2VidGEybXBaRE9GWitkMnM3MzFEK2dHZ09uUFdrdzI3RTRmM3lhNXQ1L2lzaFowVEpzc2UrSGtUT09YWmhkdEtyVS9jc3RhMDRVTzYveW52MDdweTlyVjNqYjAiLCJtYWMiOiJkYmRlNzczNTNlZTMwYTZhMzlmZTdmZDlhMjg2NThhNzYyYWI3Mzk5OGM0Y2Y3MDE0ZTFhZDc3YmIxNzhiNDM2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhSZmRDZEtBTm83aWNhWXJwQ1V6S2c9PSIsInZhbHVlIjoiVnhxMWZOU2NxMmtKWGFoY2VIc3NrVzZhMEQzUUtzMi9sZjdtYnJuTFJuTyttRVpMZXI2NjUxMWFlV3paYUV3ZHV4ZWFNRVNialhvaENrUEZaeGhLTHRyTEpkRnNDWEZWNlVOSjh2aDNVTWpSVmNwZWk2N2tyalFmUm11dGlOdWciLCJtYWMiOiJjNzE4ZDI2YWYzNzlkMjNjN2EyYzU2MWUwYTVmMTE2ZDNkMGM1MGU2NjY4N2Q4ZGZkY2Y0YWVlZDMyOWQyNTFmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ovGXxqm6gHjwM02kzUPE0m6Yw64Ta7uW3MDfFNOM2CU-1792103580-1.2.1.1-.WqFOGqmDOx.I0S2gszZt90vXHDM9qQQGD3pedbJBt_J7gm9vF3x2tZmY5jIwbRX1yQUGF6L17pHDdIDcCJQ9WQ8JnxY8wBBvkcFWDpAsqLT2UPq1DdqPSz5QoyenTGyPTkB3np0X3.PA1jYXfpidYLnQRjXtoIBFaJ987GDAByHN2elsgZYo.tAxu49rOa.gFk7XdtUYPOCBbKT51vG9B1VoIrv63FfIwkXx8nG0gN.18YGvLTQqJwCn_zilQ7B2vlS3PefnrFYhVTIEjilBr117jm7a1vwj38uMG7dhAkkH7c0hqC7KLKW28w1_0GCy5AYfdblU5_NHzKYJYhw_hd4m0T8ttQGQ89LmaZMeCryy8B_rt7PB3hRKPenYvadaKhOSyA6MwSZNV21nHwlHZcOGV75oyT7GDb8PwxaJFdAoii9vVeBo.Z7LvsYLbgdUPljiZ21ENY6wDUwHuqCmccFxAjcYsXoRtMPtmtXGWdYCQTFcl79PRyn8bjHFwo.j3nm5QSab4lK0lFG8xVyfQ",
    "XSRF-TOKEN": "eyJpdiI6ImVFUU9PNmhtTTZpWXZXRG5SdXVwVmc9PSIsInZhbHVlIjoiaTRHYUtCVDlaWG9lckRVZWtkcTI0UTh6L056WTBIaldmL1FpMnZwRHpTR1JoTjhuQ0J1a09jZEY0YnRUbk5QT3NRSE5BYXZIazlSeHJjTXBTQ2hWM1NFTEtFWWtrVHFYSEFBN1lhWENDbDQxaVU0bVBPU3NScGVONTFNcHZYNWEiLCJtYWMiOiIwMjcyZDY3ZDcwMzM0YTY3OTkyMzhkMzc2YzU5NTI2NTYwMjliZTc1NDE2YTBjZGIzZDYzYTkzZjY3YWMxMzE3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlN1cjB3T2xLQmU4cG1hZmNvelUwekE9PSIsInZhbHVlIjoiTDZIRW94LzczN1NIQXYxT0o1dzVXUHBaSlR1RTJiU24rczl1Y2doVzhCM3hHUkVrOXJLRjF5a3Z1YUdlMVBIRm5sSUdHUGZQVEhuOU5IL1ExWk1wTDdCMm5XOWlSQXZBc21xU3k2T2pPUkhxZUp5VEZYelpyZEJXT3dRNmJFR1IiLCJtYWMiOiI5ODJmZGVlOTdhOGJmNzgyMjZiNmQzNDhkMDc4ZmQ5MWEzMjQ1MjgwN2YwZTY2NDc3OWMyZTE2OTM2OGY4ZTk4IiwidGFnIjoiIn0%3D",
}

