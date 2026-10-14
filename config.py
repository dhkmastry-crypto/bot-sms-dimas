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
    "cf_clearance": "BQB2iChol3L8x42qsry7f3Y6bi6ho8bMwOIesd1JBeE-1791952990-1.2.1.1-pA0kCwTtrynwxF7IojQJSOpL450AmFD0EsFpGOzPXShnCpiKzt.NOo9tc.1BTxOuq_qUyiz7UZUictmtGNV_GVZSly77zvt7puXvyONE0TylZJhACufallCa1FxCZZ5NO5a1IFGbDxQ.CzhQ1GGNYyXRnrxYjtW_DLtK5sO.dPlMxEGvo12c1sWU1bmFUjwOHIlplAR2oWjv.otKSmYMOaUC9q02MNEexx3AmG5K6JkxR5WbDPWYASybf25bIC6E.Kwsop0qyiYopznjY1pw2rgjp4MLTNUAzSx1ZIQPum4GSG43VJ80bZfgPnd6vabQ1dyQj.EvlJO22ByAWm0LoSs6G6lk46YQJW3DLk3bnXYGYoy0QaIblHasFt6VlVhDDtbXBgaqz48ZF45aNPIOJRLPKPJyhfd.bGaMncGH0skKvWcRU5ZzUp0jzduPkNExJ7uil_bkF5xc8zgdrW32pydYkdZW910P3pO0P93F_OdpnBc_915laBb1MTJLR4iSTZYx5mdx8mIq9w8aQQ8DfA",
    "XSRF-TOKEN": "eyJpdiI6IkZMZ0hraWo1WHFmR2dsaEhGalVNWkE9PSIsInZhbHVlIjoiL1VXbytKbmQzZ3NiWml3WithenBKWFN0TWs4bTFxOVJBTlVWeE5hVUlCOGJGalpXbWFXVHUxUGFqNTM1LzRUSWtNNS9oUVhsTVBrUk9kSlkrZGFqWHZBZ3Zjb1I2ZXVtMXhBY2pHYzc4VTZ4cFQweURkY2ZtTEFNK1pQWFV5SlgiLCJtYWMiOiI4YTYxYjBlMGFhZjUwMjkzNTZhNWMzYmNhOGRmNzVjNjNhOTE2YjNjNjVjZWYyMDRmZTNkNWRmOWE3NjgyYWZiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZUN1B1RlU2TkZVaXNhSk96aDZCalE9PSIsInZhbHVlIjoiTGV3SVZ4cjRKYUZhR1UzL2tXMDZHR3dPTXYzNVlSSWtGbjRQamQ0dGJkUUNVenhxRndxTmpLaEF1cUt4TGJvWktXb2VXSTkxQlpYMnFMakQwRHFObnpyZ1daTGtaY0hHK1VoTTdZeG51T0lyWHIyOFl2NjRTcXV3ZkpwT0VNVnAiLCJtYWMiOiJjNzgyZjEzOTU4NjBjZjkwNWUwMjg5M2QzYjZhZDhkOGVhMGJiOWI4MDVmZGE0YmY2YmQ4ZDQwZDYxM2MzZmFjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "gHoN7GrCZNr5hEUKTzEDQwDbT6EFg0HmlgTU.CV6K6I-1791951263-1.2.1.1-H0gRlhMgMANs7VMbt2Tp7ABvaJ051CFDf6XHjcbqCKY_eAX2TLga5P4ggcEit6aEBC.rIsTYJEDt21KYI_2eNzaokOIK.saWzZ06oAxc0eMr9zr6I4xkIwwhizA87y58ACAlCqFYIMwSE4dxetyGIEysRl4.FXHdzQOUcEMr8xf50jGOupScoKyDNqabJOqQLriTI5Nt.VlDincru9YENOseUXv6gaZbQH5hZYJwXvxyijObI0O3wz1BVVgQvO3w6N2w2545IhLh6bA6uO_8aqfLrXY._l3p0wJoYCSSYUaiI4J5YN8BPyEC1M0O9KzncAeCaJu3WukogqW2AiaPhIi4GvZNjKZU2e_zgLmvVNjMT7zImM6TohZZthKPh8a1fwTup_uw1vbqUl0zbStLzsQtuX8nzIKy0No3HDohIQqgzdm6S9XuCjdcJTB9f5C2V0TX6rCGKThI5646Y380BAGuUqpCwQkI_b2xfRYoZgB3At..wh9G70KZW4qaig7R3S0NXOXmACnQI2hOvXOQTw",
    "XSRF-TOKEN": "eyJpdiI6ImY4bEJUWlk3czRoU2NTVzFjTGViMUE9PSIsInZhbHVlIjoiSXowQk8xQWhtNDZuKzVpaXpycUZMOGhlNDdaYmdRc1UvQ3RVVUxxSHIrNUZFMnVqNEtpS2gvZGgvWW1KVFJ5eUFDYVgvRnlsSWR3cERGTkpwNURGM2VGTUI4VzJLOHFieWVqTjY0VWcwMzNNdGJCaGlqaFNYUXdJc1Z5U1VqTWwiLCJtYWMiOiJjZmVkZmI5YmQyZDc1ZmRhYzBlYjllMDgwNjZiYThkYzgxNjRjMWY3ZjUyZTQ2ZjA0ZWFlMGIzMzNkYzRmZDViIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InU4cmxoREcwR00ySG5WZHVLeXBQTmc9PSIsInZhbHVlIjoiakZITXhpTVRVWlk0YlUvaDhRcXlFVjV3ZFo0Wi9mMVdjdjVHVXBsS040VFh0SG0zd2pqNWtGUGFvUXRaZnJHWWNsb3NLMzcrdm80OEpmOHJUeVk0Um5OenRpTHhieDY2VE9RTHYvOUd2Mk5wRFQ3SlJHYVFzZ0t1SEZ2RWo3RkoiLCJtYWMiOiI1MDFmZDg2YjMzNDE0N2U4MzJjZmFiNWQ5YzJjMGEyZWZiMjliODI1NTNlYzhiODg0NmUwYjIzMTI2MzZmN2Q0IiwidGFnIjoiIn0%3D",
}

