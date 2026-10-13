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
    "cf_clearance": "Lhu7xQ9Py5xPh5wHT1mYwxeExkq6JO.Km2lilxHID.Y-1791852975-1.2.1.1-V95H1jkn6vBQINPVOKxbC8usy_vEZY0jOGnt8riTw5F1kiUwvPg_RwGKn0Hesgid3m55qpLDvl2s6pV0h2VNXCAN5jdEGCkIblFkCtrbgNhDlv71begG2HKk4r8VZD7r1CobWUtu.dqGYpARLo3EW.2YqZhZIqp8jn.fMUcz93YS4._BLiBHDdPs4fFFZeHnkZh1S9bTBqsw0oMwbUb_TwlSlOsX1ZSO8Ui.pmdbd8sYDzmw5PpAySaQAQWuXNXnX4r3_oYqDkJlQnmcBDOrGK9NgSuXKr7sJjVqcrSlSOx2IUZo_cSv48uQpfy9sewk1uP_YPHWzE85sdHNxG4uDhzXB9gGxJ4DoMcFXYsmI4ku6oT2GH0ojL.RtdzY5VtPxZb8yEMauYp2eY4ECIN.QGgi96s.n8tAeX3VAZavUedKDl7KVvcT7Lk_luG5sd7DTtv4ivVEBbnYpC5kR0EgAMJSacgsusNuKHwWAYcro3TtXS_D_SA8vx6mxqb4POYGqE13si5m48q9Rys.DX4oqw",
    "XSRF-TOKEN": "eyJpdiI6ImpkTlFCM2JuZi9GQTZBNXVGTEFaTFE9PSIsInZhbHVlIjoiTDJTWjB3ZEVpalM5cEY3T051eGNHRzlhc3ZneFJyeWVqTHJOdUtCdlVIZWNSYlVvZ1RqdU5wZVk2OTRUOVVBVDVzK0h0bUE4NTBic1RYYS8xYVhydVMvYURHS3ZzWkRKTGFiam9tcDFEMzNSOVFBTFBnVTh4bU9vOGxRT0ZtZjciLCJtYWMiOiIyYWZkM2MxMjdlMWJjN2MwYjUxZGNjMjY1YWRjNjllOGFiMGNkZWZlZTA1MjNlMzc1ZjU5ZDRmZGUyNGVlMzc1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImtuZnBscU5vMjU5VS9LNE9FMmM4Ync9PSIsInZhbHVlIjoiY0cyNjhwKzVMYkRRYW10alJ0NGpVc0p0YzZzbVROUXRPbHFjcnFXeUpIR2RCTzBteTgraXRKeURjUkxoME1Odmx2L3pyS1R5ekN5YWhTOXJYL2VIQnpZL1JoTHhkS3dNcDBZK2c4V3Q2NG9yeEFLK3I5OXVpanhDd2J4Ykg1bWwiLCJtYWMiOiIwYzdmNDEzNmQ1MWRjYmJlZWUxOTE2OWRhMWM0ZDNjNzlhOTBkZDQ5ODhiODg3MWQ1MzcxNzAyYWQ0MDU2NDhmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "CKVyDBNKpF3WAFRNQeDFzRYXdICZ5paCT8syPwovGyE-1791854139-1.2.1.1-vvtn9RZDR_G59eOQEXrlUeBcN3RAsLX69M3R.eSdmqQyKKzzDVXTFuWuXodax0AqRMyvo.FUtkOqYd4efac866ghzxrmDw97PhXfvmINbp5_x.yKTGkumGaOfIgom2zE9rejR969nZS3QoPw2GTPVXcrzQLMYrTQbrlTj6TcEuKGLA2eIecuHpmzz68T0lxw_W.YEw3Vchl4dyGZVAOIyMOnaySMdCmBUpEwotuZo.ZPIKWdUDE64rIBvo6qsb5JkHAPoJKAldT9um74kgMFTi6g7RjMi4Y6Ts8SlQfRN9j0Q7Hq8TYUdJBeLY3wUOXT6QsiajL7S7fKitaOrSMwH92QoaXT420nf77ZptVNd52xgkf43swVkDhz.GZPyaz4YEBdF8xK6wCVPC3tuUUFQwjfjvnocreS_ZC_bRkd.JqFxXAlnoPi6iYcJ2ihP_evULB3KRtrDJvWamMZY5GJ7mCVg44rjvr_4ZFtV395orTmHw6KpeJatedBRvIRvelrtkJE_p6eiFFzLXFRCYyy4w",
    "XSRF-TOKEN": "eyJpdiI6IjNrODBCWHBLR1J2eG1iZ3J4UVZKVnc9PSIsInZhbHVlIjoiSkIxV0Y3UlpYT0xnOHNNNE9xcVdLV3h2R2hxd1l5Rm1Eb3lpdlcvcm9ydXlhbGl4OStUdkNPcitoNmZuQjhiR3ZOdjVkVmFvWDBHSlR5eWV6L3RZdkhLT3lrY2FXTUVPdCswc3Y3MjlicXM1Z04wZStDS1FZdkZ6TVo1eGV2Q28iLCJtYWMiOiI5ZTc0ZjM0MmM3MjJiOTY2ZmNiMWI2ZGJmMjIzYWIyZmVlODJiNDFkOTdjNzIxODA0N2IxMzAwMmZjNTk0OTUwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImlhZHNUZ05RNUhIUVBZTnFZeXYwMlE9PSIsInZhbHVlIjoiY1VMOW0vOFY2RXJMdVoyU25uZHIxU0ZyNldjRHJPZkZxSENoZnN1cHRyajkzenlBK2lPYXhKOXFSMTlSYklJQWNHcndtMWFVTjhSZXBvR0FxYXBZUWRYc2hmT1BPbGx6RVVVVjB6WElRTVhRbkREWVR1RlhGMVcyS21nWkRwZDYiLCJtYWMiOiI1ZGFiOTk3MDExZmNlNzhjM2UwZTc0YTM1N2MzNjUyMzUxMGMwMTM4NDEyNmUzN2JkMjIxZmQzZmE2NTBjMjZkIiwidGFnIjoiIn0%3D",
}

