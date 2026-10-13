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
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "KGajUphNGecG7vB2ARYylHYNHql._.sVTzlgW4Ysehg-1791863810-1.2.1.1-3gXiTKW7FYiCVN7ABA0E906n_E4vsiijDb.FwWY_7xSNbupfDdIW.Urumt7XpOxs8ZfzXAWppV2jXTq288wizEoug1NtFF40Hgy8V3Jn9sEDJeWbZ3UNh9z27WU00qcVfvlMh33tXYcIMZu2yzLrP0kTrrPliK8yeglWKi3XPetT8z8MXJICP4TrOxkV_9fQIBavQEolZeGM0x0D45k4Nz4V1AHjl_xB0jrVtYxNlXId8vzpZbk.M9mTtyQgjRBCvehsu5sYVMoCjBYXrrZXvX.q5IL.KFqkh6paQElXE76UDpiGpW229iG0IwA.LfxmP7oq9Vu76FohmM6vMN9LeE_zi9K9cxKtNdpw0BYadpAy2OkewT07WRI33jY_kWFTGWgvc.ZYJYc8t2KsFNdNy5RqSVXrRI1Bp6RfW9rkmiJV1tX7DjoLlA2TgETa4u2GCGRC12V2rrwLQrpHLfujAzpDnjDd.LfazDkZEHqDmMpzVPyNTt4ntLJS47rbuA_QiJMuKA2opxgVXGtMGJ9UrQ",
    "XSRF-TOKEN": "eyJpdiI6IllDZ085b3h6WkNqbVJnTmlhT3UwakE9PSIsInZhbHVlIjoiUzJjSktwZklsQmNFcy9sMFVUMnJ4WXdLQWZ4Y1ZWOTFtV3lNcHFnd01XTWVrUW5tcFlyemVRbkM0SVZaQVg3RFFzbERVWkN2THc2dmZBOHNjelBQYkllaDc0cE1UNldWYUFaa0I2aXhwbWFyc2ltMFVsS3FMZ090Z05yNzMyVDQiLCJtYWMiOiJjMzZjZTM4YzU3YTY2N2Q4Y2E0YTU2YTdhMWM1NzgzMWMwY2UwZjM5NjU0ZjAxZWY2ZDg0OTcwNWJjNTg0ZDE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik5EMGp6aGtnQ0F3WFU1OXJHSk9pUlE9PSIsInZhbHVlIjoiL2lSMUZUNlRMcEdCZGZ3Q0Z2WVJRT2NHQ1FiM21obFRISlVXRFIveW95ci9iSkpJdUJ2ZGVVTWxCSGtwb2dQSS8wM0FvZWV0T2pqaks2V3lYRmNYNnlpZ2xFVE1CMEw1T1ZaL2RNL2YyQmZ0ZGg2U1NaSlJoeXJkd3d2MnBoemMiLCJtYWMiOiJkYTc1NDFiN2FhMGQ0OGYyNWMwZDZmZTExODM1OWU4ZTkxMWRhMTdkMTcyZjcyNWRhNTc0NTdkYTc5OTdjNmY4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "IuCqRKlhoO.oGse9K3HCWlalNc0JqAg4bLM_posuDbY-1791865007-1.2.1.1-eyb5sycVMITiJo52et0OJGh2GpPeT2UsLH4Gj7V29k0Ry79dSkTicSragW7SQyTUhupkTRppwCUQbJTwcGek5nRdvrXAoW2yCwyM7B10CcB6y_gltaXAh.hTvtzNlvYeT13vYitFCoxxTU4SY3XH888wC57xMFSgatILLqEN3CYVbkVltaS85oTfuv6zgqYzTC7035ZkMXGT984yxJVcabOws6MOuL1Lequ5PEN3xL.AqhG3JOC7HH0ZPsoUZEYi9biTPLHlx1EUtq3VOx.9z.96faccCzsc5dg5JgCVItPquR9S7APOw7J3RSxZm.sHKuzNr2zvjan545cENfIwRmNI.NlGjUQk6TMlj3E9uUmMGuj_1zMipjHG3RHetYSURzXXImStsnSTM138e5QR4PwV7lG6zNfmTsZ3xDoeJCuqcbRpNyP44PQxMwr0mFNJ.BpeE5dSicsuOaOfVtQdRfVyA7xDpoQ_78bzbfyGctEDx18d9frPzzPnWIOo2snuNnZTv0lLlA13iXOW0bYntQ",
    "XSRF-TOKEN": "eyJpdiI6InFPaDhlZG4ybVNPU29hbEJwUjRmVkE9PSIsInZhbHVlIjoiY3pPa1NhNUZ5ZENSU0Vrb3NsTUV6ZUlycFpYRjBEbWlPVjBiOGNVcHpyc1lNS0kxTHNMb3pPNUxmdlhYVm0xNWRmTmUxRXVSTDZIUjZhQXA1MllWbXB2RG0vK0oxU0JubFUrMWRITXNZTzRUb3I0ZlhZcFIySTdLaHM5Wm54TjAiLCJtYWMiOiI5NmQ2NGYyZjljNDc3ZTM2YTcxMjk3NTQ0MGIwNzQ2YzhkYWZjMGM2NzIzMTlmY2E0YmMyYmRhZmQ2NjZjNTU5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkQ3bmNIM0pRclVyR0NuVWdNeEtnZEE9PSIsInZhbHVlIjoiS2tROEUyd25qMVBrdlZSek5KRlovV2JaSm5DMGh4S0ZOcTRsa1FSTkVjMHRmenFWeXo4dkdiMnNza0lXQ2JvblIyV2c3czg2OFJDVzAzaVp5c1RndGRhSXgxalcwYnpuUmdmZUcxdUdvMHdpUG5PUkM3ME13am9TRVYwWElXVzEiLCJtYWMiOiJjZDgxNzQ2MDIwYmZjNzA4MzhlNGMxYTZkYzBhY2QzNTQzYzZjZWU4YjE5NDMyZmVlMGFkZjM0ZDJkNTE4MWE0IiwidGFnIjoiIn0%3D",
}

