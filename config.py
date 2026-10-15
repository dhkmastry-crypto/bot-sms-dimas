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
    "cf_clearance": "7WDOBb3xUaXcIzu3w8EvkNEG.90djISNiBq3sQQIVko-1792063729-1.2.1.1-f.ex61V6Qw4PB046_DIgigz6B8dCOOL0KaAkWwPxJEVTlbUnxIKbgUMeaLZ47jwumNtWL.XxiYRkQsb1eX.EnwzFTwqhtGfEz6x55.04Ye4UWXTOkOyqkPo_ZVX1x7T3hR7qvXH3ClAYWRM6pP2CJYag37.J4dkG6DV4_1qwcyBvnP0EMOtjdzjoUSv49zn49_xC6PkF.qHe22jYsWU5ZmMFbaO9V1ZJluG5n2Y3zpt6G.Rsc3t0KLNj9AHby9Pk.DySLyV4i0R1WIJifKCK0SpK0H1tZFxKmREuWTmKUxl37bpNaLXEcEAHy6vG6D5YxxzKDc8_E1g9I7T3AQW7GdniF7zcyM3ncXDjBWk3Q3JVX3FytMnoP2ivDAkuhTrg5LeLRUEkQHOE_bMoM489rItyDlAFN8UrvrdHdb6ndl4vxzfVvZcceTsHX0v3VuFZo9tlhfbGGyX1O1KpYF1q3dQgjbr4GFNBCWZwmhAP0Krdy3Vd7PYRv8CgG.TQTYjTIu3RwCunsl42RrNZGqHjSw",
    "XSRF-TOKEN": "eyJpdiI6ImVHcEhhRGxTSjJGd1pHNU1SWkwvY1E9PSIsInZhbHVlIjoiWC9ZaXdVakFhYVdsbGZuU3BOQ09MZWR5MktTaVQ4T0R0K3VaZjlQSW1CT3FjbjEwK05xWEhUU0xLSW5oemRUU0RidWNSeDArWC9GakMrbDc2dkptR2JKYktXTFpkc09YOGpvSDdTZUpCTGprSjBVa2liSndkckkwNnROc0gwbVgiLCJtYWMiOiI3MzQ3NzViZWZmMmQ5Y2M1NzI3ZjgxM2M5NGM5YjQ2YTBlMzY2ZWVhZDNhMWY5NGExYWUzNjgxMDc1NzFiZDUyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjQyYnp1WXFYUy9yV0NPSEU1TFYwOVE9PSIsInZhbHVlIjoiTko0b2gvb25vbGtVMEhqbm5xU0F5RjRHcTNHRDFtOUJqZWZZblFPYVRVK0RKWE45STg3WHAyVmNOblc2cHp3TzJpYVNVNG5ud29NeHk1N0RTS2JLbDFGOHVheDdQNFpnREtaNHlLcWI3SFVvWWo4VllHbStJRUNJRlpjUDRVU0wiLCJtYWMiOiI1NmFhZDdkM2JlMmNiNzczYjA4NDhiZjk4NjA4YWFkMmZhNzQ3MjE1ZDdhNmFjMGJlOGRjNTdlM2Q0M2I2NWM5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "K4QtjNd.QhnBVsraRBCwRQP9I_NWWibQedZxTbrnI_s-1792065492-1.2.1.1-EG03fYcwPHMU4t2lu3pCzVh8r82GG9p5eQjneqV.7L0op_9OptdtdpvU8H8LsQ7S5ugyp3rRer.buYYQlcJBxvgBaR2O2u2v38IHRTMb8.ToZOchLNO_IN1jNuygL0jvbKb.uVhphDhMIJDEdhYInaY.7DBGIAZNyPcIaq7NjN6zhmq69vFTsFaAgtNuNZBZaV2ibitChy.ZB2OjhlH6UxugYwk3nv.0dYoD50lx.iFOW0DNKdmPh7Ez4gEEvo0qan1P34b_39fkuAD89YIkmC.vlPidQQMkK4of.blzdkHaX_Q9WHwQCVudLXKNokXdVjQpUNBua4LQ3eSsidVqDTbmY6xDgjH3zv.RLSZjN9PXpbt3FLQD_rM6HMgMPruipK4sNIYNP6AyMZZgaTrn5L4FKmIgUeef9iksD7ILDzAOB.Dzinq6Zmc72Hp3810XzWUO0P1GMAantCb5nPN4uqT6SPRsVgOcLRDW4lmrW2Utp7s2pjA74pWgRLgz16FsRwi.DHiW9g0mEs_qHA9cCg",
    "XSRF-TOKEN": "eyJpdiI6InZ5K29UOTJobDRFRVl5YXZITU93NHc9PSIsInZhbHVlIjoiM0k4ZUsveDNlUnFHNEFjUWNKMlhXUzA2VTgxeXhONGlDaGJVdGZUZVNjd2hIV0tVUDluRlBJY1VWN29QL2lRblhub3NnWlNmcEVlOHZYMTRHVHBkdXVVdXoxelR1RFJjNy83cHRjWUpHUW5yU1NIZmQ1djBReUMwUHAvS1lMWVQiLCJtYWMiOiI0OTFjYzhmNjUxZmU1NTQ2NThmOThlOGRhZjAxY2ZjMTIyYjM1OGZlZDUwN2RkOGEzMGI0OThmYjIzYjZhYWJhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1xVEpCd1lZVktBVTdJV3dRc1hHd3c9PSIsInZhbHVlIjoiYzBYS3Jya2pyS0Y3TFg3RWdSbzNiRUdjTWYwbGFGWm9BV0hDeUdzV3NkNkp2RWZreEJMS2g3QXZiMzgwMTBqR1hWejBFNFAwUGRURTV0eUswWHA4c3ZKWGFUNGNIelV1ZDFKcmMwbkJmVWp1UE14MStjVWNXVjMyUGljK1NsU2kiLCJtYWMiOiJhMDRlNTVlZThhOTNkY2Q2NDJmZmUxM2M5ZWJhM2FjODdlNGNkNTIyZTc0YWJkN2QzMTEyNDZmY2U2OTJlMWU2IiwidGFnIjoiIn0%3D",
}

