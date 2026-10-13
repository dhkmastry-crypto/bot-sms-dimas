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
    "cf_clearance": "bnt6ATJdWwqQOCHmC77YtGDqdAlrcBy8HHpiz5gyaL0-1791883715-1.2.1.1-9033ggbmkjGviqtgBBM9U0C6JxS7WWyIEQK1C6kjU03nc2oTMpVO7Vr9xBebcl0B1FY0uz_TfzXOSO6sAiAZOt7KMH4xpAFO7yODFEHG2dz3AREFETLCvkILk4ymUVP92WSoKJFUHUof0Q.o48YsIajt5Vez7vCsPzhl.E0BfuKKLkapw7apj.CLRUvBNfZeyGIAnIKP6QDe4RFe8Q2BVABhIUs_CK2TH8qu_.gRIJXXAgvoXo_ibE33TI6vLtbWFZVWq6xiHzGBs3eptMEi1_8FlJ_sGbyLnkwZ2a85HKch2NBZgJb7V22aBrd56S4Fa3jfJOhkAyAbjUuBJziJQTGM.UMcLHa0RN.vDrGgu6XgkCpUGcQB2WP1kTpe3fjES1NSvkCNp3OCNWi5.WM4iCHHOOPFmbzWx8K140MIqlFnduIdPGE5M3ACn._BBVJ8rYGdHcS6kkuoiEI_L.0.Ro_cCFGSpT9Tk.IudBvNhvamq6XbyN7BhvzEsWEg22b2ajyqKIh4uOxndDF0T080vw",
    "XSRF-TOKEN": "eyJpdiI6IlM5dC83ZHpOeEZLWjNNL3R6Z2NyZkE9PSIsInZhbHVlIjoicGFzN1V4ZUdKbXBzZVg0NHFUOCs2dkhVNVo4dzU2RWc5dlRlUUVuWUNxL3BkRVg4RkdCSDNlaERKbzgxYWhmYkFEejVjTEl5S2tjazRFWHIwMk1DaDJoWnJFYmZuR2VMNS9FWlBRR3JGL2JiNHRRTkMrTzdGWDB6TU1sMDZjWW4iLCJtYWMiOiJmYTQ3NThhODk4ZjMxYmNkZmU3NzljYzIyYzFmZTBkMjZhYjgzZTY2MTYyOWQwNDdkZmExYWMyYzE1NTNmNjFjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1xN1ZNc1VadGxWcFdiZml4Q2tpWkE9PSIsInZhbHVlIjoiVnZRRzNDSzhGdUYxdnFEMDBUS3V6UlFRditpOHNZblV5UWo0UDNmWHovZk9Lek1lU1hvb1JKSWpnU0Y5K1hzektZUlgwb0l0bVZNK21BZjgwelU3RnF4cE9zS0pJUTJBbGVITnJMTkpSdVgxdDRrSTNXNUt4TStuSlQ1bUhRazkiLCJtYWMiOiIzNTAwMTE0NTQxYjI2YWFjZTUzZGYxZTU3NDkxOGZjOWI5MDE2MGY5YTE5YWE4MzZkYjE2NWM1NGQwZjY0NzZiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "aDUluPzPlUS_9QDfXnEzB9gdc9glzmcN9WiZpd.Nd9Y-1791884895-1.2.1.1-DVze.9ouWafSjorGm6i8edmUnqcGhJwFGIGUZRkqHyZojKd0khDblDNB5533Xbsl.CXzRwATWJq8KirlIttMNHaMSzzuBbkd55mpJmz_PbgFjT9evX9.h9_f1gMMMiDvv4ksxbftvwtdiu8_53bu8dtfJrIf38C8H7cniWtaxpUY3xyU2fK0KRzo0vh2OE7HSIqr05orGVtUEV3B_3JTlBXTN7y4LEh0fYXnLI0cKZ95aNdTO2BmLfGzZRxH4s5k21REcFKiqOw7o5MkrNfrV1v9W9_ouPGLA9fZIFrbRlLS_DTrPPliZ9JrWvR1sw6xBMVzhiZ96.K6iizoJ8w2ppdV1RVL8.7MOmxXfwvYLaq9zzFSM3GXKcfeFSWYSiiwMl3NBAHDD44yHg0jC0pTk1ERO9yt52xzPLE6WTyxGgt2lzrhhQ5GST62OAFibBLpe7PPLoOLRPg6Wiwh.ui13At48B3iJXCXlxfGfHeMaTXe1IiySnXhDRZJqKviR6LIzqmPQLWab9wAuwbKxFn6KQ",
    "XSRF-TOKEN": "eyJpdiI6IkdtalkvS3YybW12VnlxRXRCT2tzRkE9PSIsInZhbHVlIjoiM2Z5NGo5THV2blB6ODdzV3E4YTBNTjAyeFMyZnE4RG9EOFpmOFZQbHIxSGMrTWF3cGkvZzRPMjJ0TUpYYzdRdUpueU1aMTdZSmN4eXJtamZ5NjU4R3NPa3p2ZHdMRldPUlhkZTI2WkcrREVCZ2lvOHlLczFISm8vWjdLVk43YmciLCJtYWMiOiIyMWI1ZGU3NDk4ZTE2MTI1YjY4Y2Q4MWQ0Y2Q3YTE3Y2E4MzY4MDM1ZDdkMzIzMGU1NDA2NzM4MjZkNGQxNTYzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRCeTVacTVkT0Q0eXRmYVB6RFJkK3c9PSIsInZhbHVlIjoiUWRYeHMxYVFPVlFLcGZOcnZNVzBaSFpySjR2TW1kYmt1a3BSb3k4cHlnMGs3dTZNNE1HNitPTE5TS2g0UkxBU0I5YXU0ME43ZmdhOC96Qmo3MDd1TU82aUFRSnZ0RjZXWmFSaHM4TWtkNDZMRGJVL3VEYnM1MTh3d25hSHVRWVoiLCJtYWMiOiIxMGZkMmQ5NzY1NWExZmJjNzIwZGJlNTE0ODk5N2U4ZTNlZjJmYWM5ZWVlNTdkOWNhMzM4Y2Y3MWRjYTk5YTFmIiwidGFnIjoiIn0%3D",
}

