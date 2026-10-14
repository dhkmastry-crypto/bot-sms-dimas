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
    "cf_clearance": "wDY6hlh7RdzFChIwL77.ihtnKByOQBkJjWTLDFXK0P8-1791953077-1.2.1.1-Io9QlwPr01gR.khiT510P6.tfB2PMtVHB0nfTxoBqsWm3nNoTp6kRmG93vMp.kdqCVVVCsFVcgwxzD6GmwTT0dU0q4yeeAsc2YpYlFemE._JRN7cd7VOQb4RSHwXMcqFtYbOWeJDfB_TWQISQZGQmQtP.beVAuKFBpAK6zmlq.WHhqGK7UtnNIMjZNXEgQwsPNkbR1ywQTiX.ns_QNZpCpcNRISjrS8XZdySkE4HHif0EUgHRRty2uomGcxyE1ZRmz6BmbI4U9CLtnAmjbtFhBbs4nLD0oMX9779t.oS2qgMz0tl3LG0px8EjftqfNi5bsEaUQC9l6jLteWbbulFcFSpXkkurSquef7vr2_xfObNVHRUqlyj8RayXaMfgMEwi9rIv7o4kbp01KKBsESsvhmA5Y1_FytI0HA8M_jtXTe7qaWTARUYx4cvOOEHyKQNNiGBEianGya_AbSapwbEfaq4LMOmNmbkc1VELf3GF09xM9CO575Wd4vvpYiqbcWyP5RLfjSHhKFtSNU8rgD73A",
    "XSRF-TOKEN": "eyJpdiI6IkdNREx0ZUUvSWdUZEpKcDdMYU5Janc9PSIsInZhbHVlIjoiMk5zNmxZblJNZGg1V3NHUWhmWk9iZHdsSTBmaXRQeUFmOWs1Z1JQQUZKWUFzL0JIaVM4WjFtck9zSXVBbHFrOXowSmQxR0VkbzdKcTZyMGw3UjdIZW0zL29haitpVGVSNkxiSnBWUjgxTWJDcTlrZTdnY2E3UVl2OHFreVVTRDAiLCJtYWMiOiIyZGExMTkxNWQwYzdlYTViNThkZDNmOWIwOGY4NDJlZWEwM2E2NTcwZWRkZTQzZjMwZTUxN2E0Y2ZiMzAxNWMxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjB2TGZUYThWaEM3NmR6Mi9jZUNveXc9PSIsInZhbHVlIjoiczZhbXZsKzh6MjZ4SVZUNkV3dW90elVkSTVzNzlJN3V0YkNqT3I4S3lIZWt5eDMwbEdIYzBkWGRxZThNVGYzZjVCeTllNldzTTNRSzQ1RVZpQnU2Zy8rUE9pWDl6amxGU1NuaEViSE5mUlpuUnhIdStSQ0JPZ1grczAxbXJaRC8iLCJtYWMiOiIwYzE4YzA1MDc0ZjNkYjlhNWM5OThkNGRlOGVhMTE2ZjhjMWQ3MjA5NmUwY2Q3ODQwNjgxZThlNTUyZGUyMDQ0IiwidGFnIjoiIn0%3D",
}

