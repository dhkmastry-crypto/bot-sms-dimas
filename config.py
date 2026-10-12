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
    "cf_clearance": "LlJW5oR03G12_rCDB7q13KkzP4NQCKUqdu1hs7ZWmXA-1791849352-1.2.1.1-G_mxQnHypZrzVIZljKG7AROxRyO3QmEHXUpHo3LB2NgI29mYPfaKcKTZLKpvVe1u5BWK2gflvOFXkxOUpj9p2j9v4sI_XSfuz4YKJ.shZbarK.TR00q592bs2Z50pw.TJtTWe7AWLajF0rbCYO.tXZ.Llbe5c_l.ok_zXzD2LWpRsdo3.EBAkBlG2nfMA.0CEjzZDgMl60dkckkICpmJlZNM9GWZezj1NTHwLP4GlKBIYrHx_1uNSSsEnIgh3NpUPaEirhwubdtj9C16OfvNHDWVqHU99DpoU_pJhfoNZxKlucX9JzkqOdaoaU77uCBf_P8HKsraDV0iccfXDMvoaOFmpJqeqcV9MVOEY29exI8qe1m8Kkt8II92CHr2v9HWHMv05lgNR19lZyGQtr9spZjUlVqAUU6IeZ6ER1EZSvjyEy370VviaKb1VnHYkgK8zp7MrdKst4tvW5uk13zd5YKtIS_qWFM5UVZLN2n2ImCUPzPyQQaTUHc.h.m3plqkfifpgxf_8jjlOPzwwcrAig",
    "XSRF-TOKEN": "eyJpdiI6Img3Q3RFVG5YSUNZRGRYTWoxQ2dyOFE9PSIsInZhbHVlIjoiZ2kxdWVURzByTWhSZWgrNFgvSzd6aDN2aitSbGRWd05QZ1cxNFR2eHBaSExDUi9jdzlxTWZKaFdsbWQvaEhsM0pLL2pQSkJuMTFkU1NPZFBJeFpLTTl6eEZITjE0TCtBTGNtV24yMkNuc0taZG1mSWVjWDZ0VXFyY25mWkJMN0MiLCJtYWMiOiIyN2ZmNThmYWYyMDkwZjdhZDczOWY4ZWE5NTk1YTkzODQ4MzhjNjBhYTM0MDIxOWFkNzk5ZTU1ZGZhYzc2MjJhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZsVSt4dEp4Um5NMWY2ak4xWVpDS0E9PSIsInZhbHVlIjoiUHpQNUhVTG1QazFVUDFxUVloT3gzam5MYUFxeXQwSGJLRXFOa2NMeWFoVXAwaEpJRThyQ3RVelA5RDIvYzEzbG1oU2NkdkhDbnkzWUtuM0dQVk5rdHpsNWk4OFNia3ZJVjRrUEROaVFXbEFTYUhtTWVhMjd6M05raHg0Y1NLZkkiLCJtYWMiOiJmOWZjYmQ4YTNhZTQwNzY1YmZiM2Q3OTk0ODE1Y2I4NjJiNmJiMzJlMjM2MjcyYWYzZDJmYWFhYmExMThlZTU3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "1BoWtKilLtQtwxbpvCr_4qQrtVN.6pz3FWiF.CRcIAE-1791848699-1.2.1.1-w9pdQWYFHMuCaqXzu2t7FN7FyD0DX7tY_z5MI7KBryBkVFK39voV09DK6A6wJsvY11obTEw3dyQrBRbpuRRwa7NyJTXprf2qZhglcbfNHZJ448XLFKu.LroYJ3PPCW6EwzP7a_WQiHxAkwuuZIVMjps2GcZfdeNcWbcGvErKEr.uKBlc2OeARFX.IIOWCqIaueqrw3RQOn60TkrB33UhYbzsw9myCyGtoPqNa3Nu7YKLkRXt9Lvfm5X9Nc.lsTL4bG1XXyPZFJLK1zRl895B8d_OcCLKyp6KboPOeItlu8NJTwKiTtQK7uwi3m_w8em42HnYtBmRa7PDw1UXa29nhtPjiTIF41Vfdg5Kd3k0ttI3ufpiz37gv7xVPLBiFxm6Ect3b0cCyWhUS2OYrt1xwRC12VwW4CsZtEVVSPydXYqEBj5nzrzgZlvu.UiJJPPYuYfqCuKSEcr1rfn3U7j8i7V677XCzh_wZlW9W_uuC4LLoHe8Vto1yhR3ECOHA7wT5OOom77FX8ZVjVqCjDYELQ",
    "XSRF-TOKEN": "eyJpdiI6IndONy9nOFJua3QyUlhyZWFERllrdXc9PSIsInZhbHVlIjoiQlNDTzZsN1NWNHRjYTFZNGNmK1lJbC9semxpbDk2MHVHZCtXQUxwc2ZQNmtVVUhVelY5dFcrOGZsb0t6Y0VqSUl3bSttZTF5NFh6SUhtUXdoRkRydmd4ZGZtTTdnc2xtd3hMaDNSUnF2dE1qa01US3VnSW5Ld3JLVkNUY3Uxa3AiLCJtYWMiOiI2NDEyMDI2NTFlODY3NWNmNDg4ZmI2ODZhZTMwMGM4YzVhY2I1ZDBlY2FkMzA5MGMwNGYwNjg1MjFkZGIxNDVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdYdFVYVjNxVlNYU0lEZk92WWNucEE9PSIsInZhbHVlIjoiUnNKZnc3SFlKMjh5Smh0WWVidjlaS0hrSUdJOWYyWkRqZ0ZDVGdkTUJuVnpZdG84K1o1eWZXTS9wMEN0TzFGY2J6bEJpdDdOMkE3OHZwNk5jMVJDZHRqMHh3NUp1V2NZTzJQSnBBUENPdjdvV1JRMHpEdDVnL0hxdnl4cTNvWFQiLCJtYWMiOiJhMjI2MDVlN2Q1ZWViNTFlZTFiYzk0OWZjMzU1ODU0NGQ1N2EzN2JjNDU3NTQ3NTNiYzc4NDcyMTI2ZWFlMDkyIiwidGFnIjoiIn0%3D",
}

