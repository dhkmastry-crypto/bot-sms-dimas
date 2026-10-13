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
    "cf_clearance": "r7XwtRJroOIFf8wWWOavttO5y8WijSC.KedinizDaWg-1791850513-1.2.1.1-21vujutlhgIWo.StxeOct5GAAHOBpmTl06M0A_F69N8tQoTnvdvZWy9MwaplPoFAds5sJ_pBRYiVExsuC9ZqFOUCDmbsahbb9niJz0YsNmgGj4tsfO3vW2RrATNUJC61_8RazWOo.vTq3rWeQRfKSqKKtzYFuri3yR9PYCnVpo7nOiS0GG8_xlkuCX7yAtXHbEVatKAdTgXbV_BcBs04IexyLeWXxyP6prLjK77r7n9ldFE.1PRGnk1fgoRoql2GQKMYgXeFAru_isxqlBOzs9U6IMuMII3VfnT_DTyZ0OgMKz4gafGuc.6dSIZBeLtgne370FWjG5wufC.3ydKF8AitY7yBLQ_bgDuP2poBwr4.fr8vx57W_90P4qrXNHnz5GTMkY8g5ZgAUCeT4AIuXm0Gb1nCCJf8ULzSZsNNRKrwehMNHf39oA1J_mjvzUM4ca_.C.oss901eksL8.ClK2dSJDuzSLeDrVdHrWfzQwq1dcB6lV0xSLOSFz4nEwl9wwnDopr83DlXZevTAfonZw",
    "XSRF-TOKEN": "eyJpdiI6Ikd2T0VWY1NWb3E2TklqUFQxN0QrWWc9PSIsInZhbHVlIjoia2FmOEJONTBmUkpMTXlST2NsTC9XaU1TbjVOVlpEWlFUTzRLWlEyVmR0Wmt0Q2JFeG9Rc3dQS1lONEs4aTA0UHFXNmVFbmY3UVg5c2xWMncrY2FhZUh3dzNWbms3RzVUd0lVYWRoa0pGbGpoVUVYMHNNSmF2dXlSM2hqWWFiNlIiLCJtYWMiOiIxMDFmZWE2Y2I3NGYzYTkxZjFjOTFjNmI2NDJiMTI2ZTkwMTIwNDQ2YzdmYTJjOWU3MDdkY2JiYzI1ZDg3NTQwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IktQc2s5Z2pVQk5xS2lYZisrOGJ6M0E9PSIsInZhbHVlIjoiUW9Sb2Z1UDk3OWdyZC9mTUliMThkNHVMTjd3cW9oOE5QOHJ1WllPdlNaSzdkbHNPOFA1dlVOVGZ5OWRwNGdPaFNqL2pUZFpsSGp3NXJnRWx1VVA1Rng1N0RkYXpuME4xb2pNeUJ5dEFZeUw1cjlNNFpxWFhyenFNejRkbGJLaVAiLCJtYWMiOiJjYjk0NjYwNzExMDVmNmQ1M2NiZjU3OThiOTg1YTcxOGM3ZjZiNDcwMjc1ODYwMDEwYmZjMDA2NzY1ZTc3NDYwIiwidGFnIjoiIn0%3D",
}

