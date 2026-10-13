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
    "cf_clearance": ".V3phxPiQQoBEnLiPQdoq8vPKnDGP0Mg8dQCvQBQqeE-1791867434-1.2.1.1-O3Iz6U1yB7.XSHFewpp5AzmaqQRti8nQXo6HMTQjtfOAehRdaA_TVqKYlRW5qedGwBsoZ9TgRy62lIV91SiIIXVy2GMv71z0eIRRgBL13_yExTCL6IdKEnc3hOflSVRZcNrlNsc8Bnwr.qXY_6ZzoZ4iFgseWLnH06HoLvFgAryloVUY6L_eVm3fLogRzF9L0XY3AQzn1RiGYdRBR5XOGq0Kft9m2M3fjvRdcGdiCizPYKfaWmUzIPiyarOQ.Ov7.yckeVD3.PzpjJH_Ea_TVuRaKKORqdM7lLxcJylTzHlZs45jpprLFDGe3b1Wu3UWWc8EIFxc5v33MjIG44r0TqJE4dt4IaxaHl2ahAjHaMp0rG1CU6S079504CrQwNh1txb891KXZxBqoZMegdqsVb8lODfOMLZsKKN0hRu70d7DX47t2LhNzvFZVI5RPHX6R4Ze7Bi3V3AAFQDepdrsYpJ14dBhmFwo.eH4kXBXi6uGOTcfuwjyk_fXadV1FU22TMlT2KQUFgLNFgulMjvPnQ",
    "XSRF-TOKEN": "eyJpdiI6IjRjd3g4YW0zcGhwS21udzg5MHNMVHc9PSIsInZhbHVlIjoiTHZTaUNKRDlnWUhQUTR3MkJiSTJJaFU5bzM5OGczRG0wWitaYUZBRmFOK1ptc2ZmeHV5VGJCWXpkaHhOTzk3Q05qR250cnFmRVk5V0xqQUN4WnFQeUVtTWtrWm03aVNMQkxkN3pVR0liTCtuc3Q1Z2hCanVPUng3b2FodC9tcWkiLCJtYWMiOiI4ODM0NTkxZWVjYjJhMzg3ZTg2YWE5NDE0MmNmZDNiODAwNDlmMWJjYWQ3OTM0NDlkNTk4M2VmYzBjYzVlMmRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImtyMkpHYW94TjdaQWE1TC9HelBEcFE9PSIsInZhbHVlIjoiZjJqQzUzc0VwMXVCL1FhY3hLb2VhbDNLWDdLSUtVS05HS2c0b3EyRXlzTmdsWGkwT1d3T2FETEN3Y0lRNGl3MVdteURoN0Fqc1FRWlMvbnMvYkhEdGRYd3IxRXVWUmZZNS9reXBEWno3d0NmV0ZMaTJpaDdhaklJVjFlNjByOVYiLCJtYWMiOiIyYWRkODc0NDNmYzU5MTUyN2M5Y2ZhZmZmODBmY2JlZDA2NTMwOTE4MmI4M2IxOTkzNjY4ZTU4ODRmNmFiZTQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "vJye4MFXL8RUEmjkZ3IY_9nY875NwLINqAUIcmgHUnI-1791866815-1.2.1.1-vdbL7NhePA4WhNZSdxDunqCtoAIiK_k6yYsQhvXmYI7U7x0Ly5e.hnE2Gr7LvOUipRnPaWBX_bgIvsFlMyP8.RPW9gtfxoPzjv49QewC2b20TEkmWJTk_UTZN9By4SrecbBXfNQwehPa0eXH_Bp6Wk41njEIdBBxg_r7yZ5tClN1nW6bKmdbSilXEQ0FFFJVIiqL.n_bLtHRben.wJRx.FojD4Ozy9_f8VEJhnjEqFR78dAsyg4QW.iaqYiY5yuPuIe2FPwjGjPWqgPRPCXYJ0gP4V7Dt.Rpk5v_ayiPz7Vhow5dLkxIbR3XmtwwzdI0OObJPlSm6TrrVd.___MkckR7BBX97Db2dPSY.eGT_ddLQn4QXXal73KdT.alx7BiQdIWOEeD9vRw5wM32jtBZbOtse17toJlntZPtFkSI2LjJ4_xvHBU.4oHHXPkh2N9MoFKGslG54rSlCL4ztxuvRV76IuCaCPFKYcgfFBe0fcgXwHOCDmXUbot_xYVQADnfO0.zxyjccQS4LFmGzXTuw",
    "XSRF-TOKEN": "eyJpdiI6InQ5TFNVZUtuVzRJWWRKakFaNzhaVkE9PSIsInZhbHVlIjoiT3hUelJGMEtvZ1JweTBNMDBMZUI1VXBqR0xmUklPeDJjcEpvUVRiQjNORGFNcTFtbEtqNitnZ2cxU2V1ZU52ZnhjL3U0TUlnN2MxemxrSHZoTlBwb1JzRnNMcVlnSDBObUZxSDZwZ3gvdTNTRGRjVkI2bmd1M3FHaG1UVGpxVEQiLCJtYWMiOiJiYzQ4NmZmN2MwZWQ2MmQyYTUxYTc1YTgyYWZhMjE3OGI2MmFiYWYxNGNjZGIyMzc2NTkzMjE1YTI4OGI4MWQwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZDaGtmNllHUDh2RnNncjBlekN0anc9PSIsInZhbHVlIjoic2Y5QVF4OFpPekhONE9CaFg4VkN2c2MzcUkwc1RuOXlEN1ViNmhESTdzRFNRTGQ0QVhjbkRoV0EveUw3OTJGd2ZyRHgwTFFSZWZuVHFCbzkwRTY1QmNIVm1GNTMyMmdkVkNRKzdKWFNtMEF1TlkrQnkrTTlGM0Z1VHVsUk5UQTgiLCJtYWMiOiJjMjQyOTFmNmU0YmZhYWY4ZWQyMDk2YjljMTc4ZmNlMjhmMmJiZGU1NmIxZjQ2Y2RkMTQxODM4ZGIxNGIxZGQ3IiwidGFnIjoiIn0%3D",
}

