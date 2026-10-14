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
    "cf_clearance": "kAOCi0h3BXlKQMM6G5hrNc9YraX8jUBSCa2tUev2dQ4-1791951177-1.2.1.1-MbHjjfq__sEKmbBxn.l0X3VCginX59WH7rwKKbNFF26B8gGvrXLvkQmo8Vi.XIFAjnbN3HedqLmcXKxB1c0BUHjP7BQ0s4n63yTXc4tJQgwSo.Qcbe2CWkbaW3v5FJzYRX1qw4GKjsOw9IlqJh2qa5p.E.tGgV5AmkOP8.9UfCsDkaO0DMQoYOm5FEAmplRVtj6TyPszyTKIMddqTniwWL0UVTZwhhk42YwtRI29QuPKAcRC2xR1DuNQtUDkKUl6IDBxeYeE6Jg2BbqxM4GyqKK1F.ziu6KKncFp5PsJc8I_veFoozK3U9HA5tG_s3FIBDqUNegGZw7cNme_v2src5X9GS0l2djiXYTFmP9zzDcuyiU0gr9V2S8qlRbc6RZqtt8Jtg3tjh39JEoq.5J.iR6QrtWm22kjplRjUcxkcdLFrf6IbjW6VdizKPkQmSA.caK9NiA7Di48fJSlKi5MNd5pXB5sCYSU3smlmcYgUwucj0aZuTSOi2V5asp266P40YVPMTu.Sb3x4P3nwUX_Jw",
    "XSRF-TOKEN": "eyJpdiI6IkZVOWhFb2NXeEZSQjBpdFhTSmVwNkE9PSIsInZhbHVlIjoiYXY0WndVN0ZTNFRBZEFwUUVtNWE2YUt4VEJ0M2ZHNTNIVXRFSzl3MlY2WXlRZ2diT2pVU1Z5T3pLVFhCRlZCTmFseVRsdGU3dzNqUzJNTTh6N3FYTDNjVUtRc0l4RVI3eFdqQ3NCYWo3K2V0aEF1VmNuODVKR1k2dDJxKzFsNEwiLCJtYWMiOiIwYzcwM2NjOGYwMDI4Y2M0Zjc1MTgyOTY4ZjQ4NGQwNjNhYTljNDA0ZjQ5ZWE1NjkyMGQ3MTg3MDg0NWYyODVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhFY1NiUFQ4TnR2dlhmdXM0b2gzU1E9PSIsInZhbHVlIjoibWpwbEs3WTcwdmRCbEx4MTdkL0EyeGlhM2lvSjQ2NGxhand6R3JSazM1d29qNk0weHNMdURrczlqZngxS2wrUUk3V1RjMUJYTUVhdnhmd1Z4NlN4MDAwM0laRlQ1Wm9INUl2VWRQUWMyZkhla2FWSGpEellWVUtCRkpBZ2g2OCsiLCJtYWMiOiIxZTAwODI5OGRjYjQ3NDMyNjI2M2JmYWRkMDU0OWYyNmU1YzAyY2FkZTQ1MWQxZmFlMDg4YjBkNzNiOWJmYTE0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "gHoN7GrCZNr5hEUKTzEDQwDbT6EFg0HmlgTU.CV6K6I-1791951263-1.2.1.1-H0gRlhMgMANs7VMbt2Tp7ABvaJ051CFDf6XHjcbqCKY_eAX2TLga5P4ggcEit6aEBC.rIsTYJEDt21KYI_2eNzaokOIK.saWzZ06oAxc0eMr9zr6I4xkIwwhizA87y58ACAlCqFYIMwSE4dxetyGIEysRl4.FXHdzQOUcEMr8xf50jGOupScoKyDNqabJOqQLriTI5Nt.VlDincru9YENOseUXv6gaZbQH5hZYJwXvxyijObI0O3wz1BVVgQvO3w6N2w2545IhLh6bA6uO_8aqfLrXY._l3p0wJoYCSSYUaiI4J5YN8BPyEC1M0O9KzncAeCaJu3WukogqW2AiaPhIi4GvZNjKZU2e_zgLmvVNjMT7zImM6TohZZthKPh8a1fwTup_uw1vbqUl0zbStLzsQtuX8nzIKy0No3HDohIQqgzdm6S9XuCjdcJTB9f5C2V0TX6rCGKThI5646Y380BAGuUqpCwQkI_b2xfRYoZgB3At..wh9G70KZW4qaig7R3S0NXOXmACnQI2hOvXOQTw",
    "XSRF-TOKEN": "eyJpdiI6ImY4bEJUWlk3czRoU2NTVzFjTGViMUE9PSIsInZhbHVlIjoiSXowQk8xQWhtNDZuKzVpaXpycUZMOGhlNDdaYmdRc1UvQ3RVVUxxSHIrNUZFMnVqNEtpS2gvZGgvWW1KVFJ5eUFDYVgvRnlsSWR3cERGTkpwNURGM2VGTUI4VzJLOHFieWVqTjY0VWcwMzNNdGJCaGlqaFNYUXdJc1Z5U1VqTWwiLCJtYWMiOiJjZmVkZmI5YmQyZDc1ZmRhYzBlYjllMDgwNjZiYThkYzgxNjRjMWY3ZjUyZTQ2ZjA0ZWFlMGIzMzNkYzRmZDViIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InU4cmxoREcwR00ySG5WZHVLeXBQTmc9PSIsInZhbHVlIjoiakZITXhpTVRVWlk0YlUvaDhRcXlFVjV3ZFo0Wi9mMVdjdjVHVXBsS040VFh0SG0zd2pqNWtGUGFvUXRaZnJHWWNsb3NLMzcrdm80OEpmOHJUeVk0Um5OenRpTHhieDY2VE9RTHYvOUd2Mk5wRFQ3SlJHYVFzZ0t1SEZ2RWo3RkoiLCJtYWMiOiI1MDFmZDg2YjMzNDE0N2U4MzJjZmFiNWQ5YzJjMGEyZWZiMjliODI1NTNlYzhiODg0NmUwYjIzMTI2MzZmN2Q0IiwidGFnIjoiIn0%3D",
}

