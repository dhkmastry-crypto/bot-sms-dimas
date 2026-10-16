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
    "cf_clearance": "6aYau3JPasz_cNTGm9_M9NzcznOlPv8TPkRw03g_eu4-1792109006-1.2.1.1-ueHcRuRUpWPe.tUIu4_cYtS2u1HUHlZDS6ZHksf2Tj6U5AJTx7LR9H4xnc_9NDimIEMQD3akFCSsFPRwjK6aSXa085wqcTK.aagEFehRWXJchE5lTAFdOoH2DdYizJhOSlLSQwbfoDqNgrPrysEwB3msY3cxV2wEhQmyjt9w2V8rxBTZkNCSYrnmzHDAAJf0xdRVZjl8LwhLO9Z2XVyX15gqzo5A4vYIjyHjtvUzvgqENmVfX2Wz7dxMwBwtmeY2qzL3MkJOfuXaUOMkDabkJveJQUeC5SYjjxBNDSs4qcndZ3dmM.hy2w4EUgDBqmI3nOV9Q_dQfrijbR0jfjmVQ6agtb7pJef4eIP0H3N7CeaWlhmuZR2RT8n5fcxjBikPG6X6fvpZCnPQewKbub4JpTVVx6kGy_1uT04yiDosW3PAYKMs28SMQkJna8P2z9VYFAmRV2vzm2jnDvTp9JbJHQ9ZwlzgujIdYLzt5mHvS8Lr_xAgzSrt9HEULmMkNb9DDF9_1F9AYl9VenwC55221w",
    "XSRF-TOKEN": "eyJpdiI6IjgrbHlGOENpd3c2MFpveEdkN3lmOGc9PSIsInZhbHVlIjoiZmw0OEpZelZwSk4yWGlGN1dwNjNTY1A5eWlJTDJlejdOWnBTSHdNRmVENm91bkdoRUVVcUxoS3FTekd5aW85bHVUbkx6NW44VU5SRnNtSzB5VTlMVDdWNjNSRnBTOXUydUkyL1RCUktjUVMwaGUreGs3MSt3QVBJZWVrMmU2Rm0iLCJtYWMiOiI4YjIyZWE4NmExMmI0ODM5ZmVkNTg4NGFmNDRhMjAwNGEyZTc0ODRjZWZhNmQwZDIwY2M4ZDdhNTVlNmNlYWJiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImxFbDZLcW1oODJteER3ZWdMcCtDcWc9PSIsInZhbHVlIjoiWmJZMk9Ta2hhL0NCSm5KUmV5ZXdScnhnK3RHem5jYVpTYmVkMmRaZjcwSlg4KzJ0ZE5oN254ZVQyVVNrQW5xTTdoWk5tenJrMkZpems3bmNyaHU5YmhJdzFKUFpITTRCbCs4ZmFmS21BczBYNDd6b1EyZDJwd1JCOStpcUVLbFoiLCJtYWMiOiI2NzRjZjAwOGI4NjM2NDAzNjU3MGYzOWZjMmRjOGQxMTIxNjMzZTRiMzQ0MGQwNmIzZDA1NjAzNGVhMDQxZDYwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Wwedu29AHdPn4YkwxSuXeq7quXvv25BwgMxnOQ_uH0Y-1792109016-1.2.1.1-O6Pom4v9SLaH28SrF1J55b1NLj_O_OyzZKz1X_zXDJaYjwqaRizL_8NKiVwG4FjozM4vdQYLfdMcEU83fSt5_mOulWI3kFyqFtkc4jFEFIjdJ2yEdAPa.vvprHjgocSnNP5rDjESV3doM8phU5l2w4j.q.QFMWPeMhs2YZtm97CGB9vhh3RlqMllMXMM9_6kkxInbH._3S2.dKPwwEzLh.QDYQXiMsIW5XEgp6gMiuKXY1dIYuUzW6yGzDxzRqf0aEEUDJwxMl9PoJFTEfecg9l8G2i8tEmCXdGx3gXYSs_Uv1AEzfj4044mcZno5DLADb2uXKKUZMHvaRp1cufMTtayPqrshMjrzhAv6YCVsrBYu2Jb83ElX1aKoc5.IYGj_Hrtljs_RWi42wP9lK0UlfPmqoPeCcQ3lUIeLxkLwXiPuNdqaA.pYNxwq9OrI6kEXiX2DE2D9uTMjm2gq8B_T3E3YnxkIEijp5OrxIg0C.ihO.v9GDg6YvMtPhVC6tG1Ob8t9miNdScIOQUcMl72sw",
    "XSRF-TOKEN": "eyJpdiI6InprZzRQODhzdVYxSW1uT2xTUDl1TWc9PSIsInZhbHVlIjoiNE5OYkQza0ltemtpVE9NRUoyVnF6bmNwRk5hZnI3ZW1xNUp2L2VIbVVLMlJkb0Q4NktCZDJnUlhiT2c5RjJUWTBSK1JacHlNVnlsNXJiZWQ1NmZyeE9YUGRDaWVUYnNlRGZHL0RHMWNjV0xZeVRZYnhyTW5BWnNBZWRQbEJtd1oiLCJtYWMiOiIxYTljNWIzZDExMjMwODRmZmZjYzJmOTgyNGI1ODc4OGU2ZTU0NDI5ZTAxYTEzZjMzZmRkNWYxMTY2MjJiZjYwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldKTDdtV3VIOVJ3RDRZSVpETWUwV2c9PSIsInZhbHVlIjoiSXVXWTN0UjdXTkN0Y3Q2RVJQcTRFQmlQVmdzOFJvZ0tJMDJiUmRZN2ZJVmRzTWZTN2REUXQ4Qml0RzdiemtZTGZBdDc3S2J3N1MxK2hWWXVmV3UxRjJVVW5tSjI1S21rcVM1ZzhGZFM3RUE0ME1zbFpOMUtqN3ZVbHhkY2lIZVUiLCJtYWMiOiJlOWEwODgzNTExNzc0Zjk1MWI5M2FjODcxNDRiZTc4Mjk1ZGJlZDJjOTJhNzUzNzIxZGEwMDZlNjBhY2ZiNGFkIiwidGFnIjoiIn0%3D",
}

