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
    "cf_clearance": "VY2EnFPaeap_FDPgWe2n06OjxHKzOeScfaRRedICipM-1791885520-1.2.1.1-wrvIXEIIQYZmwZRJBdP2HKBzGBxyAGUdJ9rot0cvJYRdC76JWq57HdyXRE4LpJgXpgbfY5K0Wv4E1x_NeybCjlPhnhwleUlGZr2xBUffqH9iUu_RTaas5t7N9DgSnhMWF_ZBQ78GJt.J17X3gVvwqi52LWCNjU8QYbzrL0YL65WyXHgnrIH7Jt3ce57EYXsqiKzYJNaPaXG6gUm3_zsfYmVyVtLG55r7IzgXewbtaxWel4C3rgPgxruwv2LaAAHwFp0hs3ExWqtHNudK6G4KWwvkFUC5LvSGiu5kw6aZy220c18xFZHBLn8z6urfcz_VuCOeUOLySwM9w5i9bf.1a7qYPFyifrYCTgxMjl45imYNuxAPNUuO1P_bh600vv8teLCqahCgHPRHQG8isMDONwzIUZ8HrIunpMBT8Wyco5WLQ2Bq0oOq1Ydlv4U2mxrfYATk6a5jhzcGKdK.jEP50LjaMyemK2fWHGc7nm5TkPSjK.V5F.1ZVsdpJT5JO6DMY2kg_STm28VRoZ0c0gWqgA",
    "XSRF-TOKEN": "eyJpdiI6InNGMmxVdnNnaFhGRmZPZVM2R3JKOFE9PSIsInZhbHVlIjoiRmVsMEhITXVuek5UV1NvRHRmZ01KNk9LU1Q3NkdOTitlaFFaYndpU1pHclF1RjdOamNDQzg0MVZ4Y1NqaTd2MldUMStsU3BzT1d1d2V1enRlU3VqbVVGS2I5ZjRXTGFaR1FKckFpb3ZYTVB5YXhBblpxRHdKdkh3Q2swRTZwT0kiLCJtYWMiOiJkNzQxMzdmMDRiMDNhYzVhZGRmMmZkZDY1YjY3ZDY1NmYyM2JhMDE3NjNmM2YwYzZjM2Y2ZjVlNDJlMjNkZjBmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IklqaGlsZFNSU1llUUhZMERmTVhhdXc9PSIsInZhbHVlIjoiZ3dJbkhPUHJ4Ny9CWkY5QUhmM203UHI4Uit0Zmg2MkNXRHZmRmlwcjUvWUd5UE13aHRFZFE3azBnM3o2WTlNTnpZV21PMzRLMVBIM0t0NDlVNVRPSnRMRmlJeElBa3pVM3JTZjNHZjdqblJSamV6T3NsVEExWW1ndHBZNFlhN3IiLCJtYWMiOiJhMjMyMWE5ODljZjA4ZmQ4YzRlYmJhNjU5ZTJhM2ZlMDNhN2FiYWFjMWE3ZTgwYzY5OWVlNmFjYTdhNTEwMDQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "aDUluPzPlUS_9QDfXnEzB9gdc9glzmcN9WiZpd.Nd9Y-1791884895-1.2.1.1-DVze.9ouWafSjorGm6i8edmUnqcGhJwFGIGUZRkqHyZojKd0khDblDNB5533Xbsl.CXzRwATWJq8KirlIttMNHaMSzzuBbkd55mpJmz_PbgFjT9evX9.h9_f1gMMMiDvv4ksxbftvwtdiu8_53bu8dtfJrIf38C8H7cniWtaxpUY3xyU2fK0KRzo0vh2OE7HSIqr05orGVtUEV3B_3JTlBXTN7y4LEh0fYXnLI0cKZ95aNdTO2BmLfGzZRxH4s5k21REcFKiqOw7o5MkrNfrV1v9W9_ouPGLA9fZIFrbRlLS_DTrPPliZ9JrWvR1sw6xBMVzhiZ96.K6iizoJ8w2ppdV1RVL8.7MOmxXfwvYLaq9zzFSM3GXKcfeFSWYSiiwMl3NBAHDD44yHg0jC0pTk1ERO9yt52xzPLE6WTyxGgt2lzrhhQ5GST62OAFibBLpe7PPLoOLRPg6Wiwh.ui13At48B3iJXCXlxfGfHeMaTXe1IiySnXhDRZJqKviR6LIzqmPQLWab9wAuwbKxFn6KQ",
    "XSRF-TOKEN": "eyJpdiI6IkdtalkvS3YybW12VnlxRXRCT2tzRkE9PSIsInZhbHVlIjoiM2Z5NGo5THV2blB6ODdzV3E4YTBNTjAyeFMyZnE4RG9EOFpmOFZQbHIxSGMrTWF3cGkvZzRPMjJ0TUpYYzdRdUpueU1aMTdZSmN4eXJtamZ5NjU4R3NPa3p2ZHdMRldPUlhkZTI2WkcrREVCZ2lvOHlLczFISm8vWjdLVk43YmciLCJtYWMiOiIyMWI1ZGU3NDk4ZTE2MTI1YjY4Y2Q4MWQ0Y2Q3YTE3Y2E4MzY4MDM1ZDdkMzIzMGU1NDA2NzM4MjZkNGQxNTYzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRCeTVacTVkT0Q0eXRmYVB6RFJkK3c9PSIsInZhbHVlIjoiUWRYeHMxYVFPVlFLcGZOcnZNVzBaSFpySjR2TW1kYmt1a3BSb3k4cHlnMGs3dTZNNE1HNitPTE5TS2g0UkxBU0I5YXU0ME43ZmdhOC96Qmo3MDd1TU82aUFRSnZ0RjZXWmFSaHM4TWtkNDZMRGJVL3VEYnM1MTh3d25hSHVRWVoiLCJtYWMiOiIxMGZkMmQ5NzY1NWExZmJjNzIwZGJlNTE0ODk5N2U4ZTNlZjJmYWM5ZWVlNTdkOWNhMzM4Y2Y3MWRjYTk5YTFmIiwidGFnIjoiIn0%3D",
}

