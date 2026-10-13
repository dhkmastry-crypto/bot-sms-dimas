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
    "cf_clearance": "5wvmp5cJS99H9RrpR515TPkB9RgeYVogbCKiKNdfh40-1791883090-1.2.1.1-ImZBfZxZfxDbuhDMZ_LEJx9v7bpmlOuLlyYweKXDNDsqUqDRq1lF6kR92hw.E57o5eOM87cgp0ggTN2ZRV5HVo0LcK1Uap3fn.TsbKpV5iV9TDw2RbisOL7HhT3uS6Cpw0gtO6F.smVsoSm_wrN2YXdb7VBxCsAMJ9YeAAFzfhdgURGSTlMAF_MfEhMbUlxplY1TRlfemcma0T5VtjLPhsRFgMg_2E6NlRC5wcIhIrtBObQP_jkaBJXjyUh0.8pmzT8ao02YGZi8uItUwY672h6bPCf9MRwOSC0zA98b3hRtwFGGVCsHrhLFJfiwU8xqyRpfzW2caot3oGqqqGo9lXvgIOGCeXD5bHOfqKPYkAu3cVgsSvd9KBX4gVKjZLEt.yVJLSqDRSQtSa2aJuO.gRAt__lqXdFw27.D0y960MyDtyKT9IHKz_0C3mDhxntzMQuph4iy4W1RwYGXEA_h8ARLbwuTSnPU5zd.jVSIrb5skKbUMEhxOnvP374a9FAsjD50CczMRfweerGjs0fAlw",
    "XSRF-TOKEN": "eyJpdiI6ImQxUnR3Ynd5TmM0MElSdHRZZS9Wc3c9PSIsInZhbHVlIjoiY0h3SkZ5TzAvYVlsdmxvdy9XdzlCNUR2R1VnMnljQmFSam9TYXZjVTNiWXExK0dEamN6U00yV3BZM2N0L1RJYVhENEZKamd4bVlhNFRzd0pibmJjUGFBMHZyK0dJdG5nNnM1S3BkdzRHQlJRSWRxM3YrdU9jbHk1NktkeUxxbnEiLCJtYWMiOiI3ZTgwOTVjYmM3ZWQ4NDJiMmI2YTAyZGNjYjBmN2YwZDk4NzFiZDM1OGNiNGQwNDkzZjAyZDFhMTcxNDU2OTBiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImFJVlRybGRjaWhOcUFySEl4YTN2QWc9PSIsInZhbHVlIjoiV2FCdnIwR25CS29zODFPMmlVU1FySHRhUXlNenVoZW9PYnpPRkxzeDF0NlJLRk9Rc1cveGZoZ3NCWVlPOCtFU3NPTzZNNUgxOStYcCsxN2NKZG9XVVlYNGt3UkxKUitHU1hwN2Jha25FS0UzVGNEVDlFTUhBZkJNVUZFcG1vUUEiLCJtYWMiOiJhYWZkYzMyMzQ0NTQ0YjhjYWM0YzVjMTNlOWFmOGEzZjRmOWEzNjVlMTYzMzY4NzkzZmZhZDczODczYzEyNjY2IiwidGFnIjoiIn0%3D",
}

