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
    "cf_clearance": "qkzbYDYmrdK9TmxTkgk4bFgc6kTO.sBdPHMbkc1IiiI-1791856585-1.2.1.1-TLq41Bm6vQUrlhE2IwT1eU4TxVa_rA9jRK.QHHNdhO5J_rXLxCIcehFi4l00BnUXFpTCkiRXmCqEPUoIhNcR6I8UwweQGYPw8_HCcV9odrKncAiOxav..kQSZhhcZTt93ttxvcAm2uQBsK2kA3Gi4xep92eo4bscEtmytbgXCeb.QZs2tcWSpO5SPrYeAhbth13kd9q5Rz5GXedSrGtwCiHxesmzqpQyRq8WoelN70wucBJ9prTDZh6l4NfJ_yJ3BZEZeGP0bp0twwYEzofvzlH8sUDWBMWrReQy7es85u8ntOJIFX2ekTxODzG3fPabY8atXADLCpJ7Vd0OA.MHbXF9y52KJ6vvKWUsfZdhV284OeJDIxVmhMuungJ6.5gBaDdxuu4rbqFhMiQp1yI68rsNZRmITtc4UF6q3Z488Yf3KHM0ZGMndShJvjoWTmVwfYFMlfb0XBDIel6U_aedTnpnUVQq52nKOxWmv8UWMfFP_maxyp42kZYE7QUOjy0_ODa4mT_pj8bEKOdSAkTc_w",
    "XSRF-TOKEN": "eyJpdiI6IkxXWGh0M2xVdXVnT0NGaExCR3lTS0E9PSIsInZhbHVlIjoib3ZNOGpiMmg0Uk0xdXppOGxJa20yUHp4bXRpZ24yMHhsUHROVEFCUmhXb1E4SG9ISkx6QnRPbHZKUjlUbUEyaFdlVmdKYTd6UExKUkhHa3lzb3dTSVVpWWhrZ1BSaUtLaHN5WVczcHlhaldEenZua0V1SlRWeU54TmlTOFBnUWQiLCJtYWMiOiI5MWZhM2UzZTA0ZTBhZWU2YzQzMDYzY2U0ZGYxMWM2MGQwZTA5ZjQwNTcxZGIxMzg2YzY0NWM5NDdmYWU4ZWI4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBlaHhHVlE3c202ZXJCSGsvZHVZU3c9PSIsInZhbHVlIjoieHVUaVpJTllQZDg4WU8wZG5NTnJuVWZLVSt2TGZ2ZG9ZdXNkLzRCT0Z6cDRURXZoaFU4TWlhY0krM2VqMGdoVzkrQW1CQUlYa2ltaGl0azVkVGptSGNjcjV0NVNTK290SWphcXJxRUxqaDRyODY0ZTBwb0V3dVFOMFo0VEQ5bkMiLCJtYWMiOiI5ZThjMWMzNWNkYjRkYTM4NzhiMmMzNDlkYTNmZGI2ZDU2N2NjMzI5MzQ2MmJiMDc3OWE3MjQ2YjQ5YmMwODIwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "AkD5uZ26q7Rd7oNhBJIat_rCiZe5pLHeNmdacwlH254-1791855947-1.2.1.1-4kIg0UiL1jDEKLEYWFNMqNDIBObKZfARdJJuou.MXzaXDisDthprj3I2_9VEnM1DziwBVlyGcMy.u80vTGWRjeSSdEb28nZ5yBBgSMRY02sHyQMb_.G78l885Ay3mhC9B6xVRYxr6m6uCm5sHu5JHXQRrZXKYRIkHl5F.QOX1Cqp39T8ONfvMdS_61AX4U9xYLDO9SfEk7zGZ31QjFWLHDoZRQRne16uIM8SesxK4Of3liz2_7pSoKijgcuH1agYnMXCYKZ1DlxVTYEA1sN_uFNV9HIVszzX7dXD8e8Xh9fSQY2pPtgmRFdiJJXv_7oo.gvGYmsEZ5JQQsqmfhjm3jhb0VrhalgzzOMO5vxnHxpUT_rPI9_kbUeaEt66SXPMXrBa500eXXL9XCX5VthymesODSWxM8LyJSqteOFB0LLZNXYIgFlY7Ki0mE_6_j2nqRljubt4BQDQ6k9Mc4zXh5cBEn3py5S_iDPlUjMtE9c0hDkE2d5acNaJWSChTk_AoIERVbsrQ6aA60m45X5Rjw",
    "XSRF-TOKEN": "eyJpdiI6ImI2NVV2SzhwT0FFN0pocjRvWi9qSVE9PSIsInZhbHVlIjoiRmNOckNUd2c5MjlIVDRhVmw3elV3M1Zka01FeVcrbFlEOTFhTktieWRybWwrQStNQ0c5aGd0OU51RTQ4U3QrdDIyZk1YVmcwMnpEYzRpMFdHcHl1U3BOWmNjV0F6RnRDYzZtaFNZcHQ2VnU5bTAxbE1ZdnlHV0hXcUI1MUJwUkciLCJtYWMiOiIzNTBlYjhhMDdjMzE5N2E3OGU2NzY3OTI3OTAyYzAwMjY1YmE5NzJjNGYzYTFhZWY2YWNiZWI3YmI0ZDAzMmM2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldSRkNOaWFnTmJOZFBSYjM5THNWQXc9PSIsInZhbHVlIjoibU00WHJkZGFEQWZBUVk2WkRORW5xem9EUG9BTzFQTnBrRVhkVnNRdHE1WjlFak5YcHU4WE5FMnVNK0JKRjlSUStZOG40Z3MySGgwdGg5NlNnL01rbmFjY1U1ZDRDRVMyYWo3SG56SjQzQmVkenhzeGJBbGRHZ1pzZ1JMSU5DcngiLCJtYWMiOiI3ZDE1YzkxMjBjOGYyYzcxMjUwOGFhZTMwMjMyZmE4MTc1ZDc3YzAyMjI1YTQ0YzYzNmY2NTlhNWRmMjVlNzFkIiwidGFnIjoiIn0%3D",
}

