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
    "cf_clearance": "jmQK1g_xBeDUoRtH9XNHJAemP9rX.9EQOV6mLj0KnKw-1791933091-1.2.1.1-dClybhfwUxaqjxtyvOeO2j2XRrrguAr2lCOKESL6ghfsj6yqCAzDX6YvFVZTt3OJ3TQp4H2ZsYS7KkUdF7KXVG3zikuOvz1B1O4c.0CmKPtu2kyiBIiCjYbh8LXt4sw1HUaPXUtpUgkbFKH9UgcURWNtQ3rsG9q2fjKIuzQHz6hKlWdZDa7jffv6uesmmWo40HBtgKtl6IFalVZDThJ5Oe6NZY5FaY..MO76y.OVrqcqNUGnSq8XOtsJGMmWzK73pw2DMUQdb2lu.DhpR5z5KKq1QH55mTmRWWOEzvADfFq_2SWE3Nqx1oacGXdi2vJmuC6C9oXRExwyUR7Ijh0qN8fIVWK7mhbul_DoH9ba0BrIs4lHjMOEh1CDw96.t2krl1ujm6vRstZzkDl7B.Flxgx11MVRCyYw7P7lRE641xcCATLzzRwN.qauHS..HZocYjeyDAPnfW2yQ_fus1CYU03dM6KdB.GPOcb2867D0U23IAscia6fAQC119AxuepMpYLGEbsP8XbhE3ZmJEdWwA",
    "XSRF-TOKEN": "eyJpdiI6IjYvZ2NXUU5QcGN5SGVzeXJQM1pBVHc9PSIsInZhbHVlIjoiekl3VElQdHR4VUlrK0UvMS9LYUEvQmRLQ20yc09JdG5tTURGMVVzSExweGh6Rk5WUGVDT0diVjJvZDdsOXo5cTJHUmNqYjJWQTZ6U08zczJwVFNBZzJaUy9WdjQ5aklJTnZab3RBZFFmNlplWklXVWF6cTlrbFpnM0VCZU9vM2oiLCJtYWMiOiJiNjdmMGFmOGYxNDM4YjU4ZGZiNjc2YThlMzg0ZGVmZjI5M2M0MTBjMWRmNGNhM2Q2Y2QyODJiNmEyM2I1NTlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImoyblBleTcyakx1QWNYZjZXOWpWQnc9PSIsInZhbHVlIjoicWdoY2tVUHZOeUxBc1EyeVZYOWlGWlh5MUhLRzBKbnZCMXhNb1FBQTE4T2RzckozSlRPcEd5YVBlcmFVRkhFZGo1RWRSL3BJa2lmR1JFMVF3S1ZlRmE5SDNLZjlnL1dwZUU5VWJzNWlIVlUyZXkwSmF3V050ZVRSb3ozclVWQ1YiLCJtYWMiOiI0ZTUxNWNlZTFmN2ZhNzUxMTRkZDg5NjZlOGEyZWZiYTQ2MjM0YzQ2NTVjOTI3ODgxMmQxNTJlM2IyOGIyNGE1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ZqWHXrGuUhlGjbKfOz7fUQHWzGibkfuZGfb.gyBQ_Io-1791933081-1.2.1.1-ofkgAE3i5vryuL7NL1i5v5t3boZlJRa6aX7ZLellcWYvpRzXUkTzhglTv.QACJ4megPwfkNITMjn7KemOK2elL_Qra93Pva4N8mItdxD_TmOAwnz5.r2J3XxZuuGXyvuBRYQzKmg3TjizXrRHwkpTthUZhPd7.585dnXivYWBRWl2SaRVWq1r77ab5V6lxVHXggQl0KnPYbEt4QWKJiiMTE1ERYgSfzJby_o_XEboguzf6KLqIEEEl4MM3C405emMXcs7czC2J8qvy9hW8ZG9jahYaJToTlOebXpG.AEia_XK7KGTXGF460f3q.h7F6H752Q_AyqFStBX04bG8mAAyBIokWA4bvzGYxMfPrezYL97tqCfHfiD6ngOQMSL6IR3qosD4RslH7sHE8DpS.CPtj3Oog6VPTU7GlhRPJDcW1q8JziwBDkIXKtCV8FrLGl3yIkAK7..b9RCyB2uBJ.OEfxpAnxkuvk2HRZpzPRHAFJkrUK_kt4LY2shwSHwrgKSRUZ7BWZPL9D8cayYGbwsA",
    "XSRF-TOKEN": "eyJpdiI6InFpSjQrd3V0TU5zV2x4Wi9wczNPUVE9PSIsInZhbHVlIjoiMGkvYXVYWHpQdWtvOWNGSDZjdDFLbU1HWkttVmhaN256TGd3RkIwSGlWMlJIL0Y5N29LMzhEUXJWUnVLNDZQT2RZR1NiRXBZd0NUaXJXeGl2SG1ZTVg5TGsrb3FNenZpZXM0Z0JqZ0lSL2FPQXkzdDJ5djFTOVYwTWNjY0ozV3oiLCJtYWMiOiIzZmY5ZWU0OGFiN2I2Yjg2MzM3YTJjYWMyZDAxOTllYjRhMmM2NDlmYTQ2NWNlM2IwNWNlN2Q1ZDQxMDliY2RkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikppc0NDTmJIWTJpbG5YVlNJRHhKRXc9PSIsInZhbHVlIjoiTERxVnhZL2cxZERncVZZdHI1WXZPRlFnK28yR3VzWEttREJ0Tm16d3pEY1IxenVmN1hxUkVORjg4cUJ5ZjB5MlR3cCs5ejhUdGtkMllGRjFHOGhnS2RWNEt6dXhOcDV4L3k0blBoQUZmcEwvL1Ayd0k3bzEwa09MdXl5UzVnUHciLCJtYWMiOiJkYTAxOGFmMzAwMzIxMzI2YWVlYmZhMTQ3ZWI3NDRjNWY5YjY4ZWNjZTMzYjJhZTc0Y2NhZjg1YTdmY2NkYjhmIiwidGFnIjoiIn0%3D",
}

