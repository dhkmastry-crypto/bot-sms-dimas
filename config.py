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
    "cf_clearance": "HtHW3E7EN9PCOmzPk3SUMpGb8vmhRBZAmvYYXr7SdoI-1791954796-1.2.1.1-9Ui.mxfO4n1fff.HMruGEt_Ni8mLbr.aeqs4cxJ9X53cPIcKMj85kC2jDL4sK_P1f2QU2tcE6PZXfZUl7ia72.sGQxF4f.R.FJKInvupizWLGouqd5FSbVGMoPyaQU.U2oF74pRNy9qVCvLPFSPX6XXwBs2zKxBHMwTcOxGb0a0nGegZPTYOumYCu9ercD1dzbB46qUQomknOI5k0oV5Iywua7bpV4z69eeoPcfdCFE55AWJu.jlNZ_16ZuKN7ndB60QXOCgJ6A48O4DOoiVJ11y_u5c7inXfUowlC0dYBQ1xCeyvNYTOdrznV7pdVgZX_Y9M3EDFDMRkWOj9mdCTAztspuXn.vLPAv_rGuYV6abKd5N27jnMT0JrrDGxQmrX.9_qC.NvhEbLsVvZ6QT2u6VnLFv6Ct0Gwz8JFmy2Pc99lMypUj0p6fzmsMaXvyp4xO3JfQVkbnNypZjZPs1WgTywGXiZMGuq.LTsDnZvl.GO6UYlpoTJkZBLNLercspBw8O1SyBtVmgeY3uBQuiOw",
    "XSRF-TOKEN": "eyJpdiI6IlQwSTJsendwMSs0K0liaXBQODc0Zmc9PSIsInZhbHVlIjoibFNvMXMrNUMrZDZpck1CMXpzdTloY3R2aEV6OGNpT1hqcGhlMm1XVnlDR1plS1NiNXN1QmhSbktkeEtibWdQUnE5RVhtY1NqZzdqbXJSdkxqa0kzOW4wZkUyQjczeXRkYUxtSFhNc0FjMW0xZVcxZWxrcm82NEo1Z0NUaGlxdHgiLCJtYWMiOiIxMDA0MDYxOGFkZWNhMjFjMDEwZDJjNGQ5ODg1YjIzOGRiNzZjODhhOTFmNzA2NGUzNjNmM2M2YzhjZGM5NWM3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJKZGRXSWpRNFVwaGE4M2xrNjV5Rmc9PSIsInZhbHVlIjoidVlBZDhjbW9tQm91dVRWeUEvNS84dnJYdS95S0VXLzUwSHd1dTR3d1Y1UTJMUklEbm9DME1ZWVF6Qys3TGFEZmVoZ2QxWHE3Z0Y5NnZVay8yNkx0MnBrejFtSG9zcDVPdWE2L0xjd0wwSGdiTDc2WEtJOWplMThQT2tacVhtZG0iLCJtYWMiOiJlZjBkNWRiODEyNWY1OGJlZTA0MDI0MWFjOTMwMDAyMzkwN2E1MTU5ZDAzMWRlYjJhYjg2ZGE3MzFlZWNhNWRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "wDY6hlh7RdzFChIwL77.ihtnKByOQBkJjWTLDFXK0P8-1791953077-1.2.1.1-Io9QlwPr01gR.khiT510P6.tfB2PMtVHB0nfTxoBqsWm3nNoTp6kRmG93vMp.kdqCVVVCsFVcgwxzD6GmwTT0dU0q4yeeAsc2YpYlFemE._JRN7cd7VOQb4RSHwXMcqFtYbOWeJDfB_TWQISQZGQmQtP.beVAuKFBpAK6zmlq.WHhqGK7UtnNIMjZNXEgQwsPNkbR1ywQTiX.ns_QNZpCpcNRISjrS8XZdySkE4HHif0EUgHRRty2uomGcxyE1ZRmz6BmbI4U9CLtnAmjbtFhBbs4nLD0oMX9779t.oS2qgMz0tl3LG0px8EjftqfNi5bsEaUQC9l6jLteWbbulFcFSpXkkurSquef7vr2_xfObNVHRUqlyj8RayXaMfgMEwi9rIv7o4kbp01KKBsESsvhmA5Y1_FytI0HA8M_jtXTe7qaWTARUYx4cvOOEHyKQNNiGBEianGya_AbSapwbEfaq4LMOmNmbkc1VELf3GF09xM9CO575Wd4vvpYiqbcWyP5RLfjSHhKFtSNU8rgD73A",
    "XSRF-TOKEN": "eyJpdiI6IkdNREx0ZUUvSWdUZEpKcDdMYU5Janc9PSIsInZhbHVlIjoiMk5zNmxZblJNZGg1V3NHUWhmWk9iZHdsSTBmaXRQeUFmOWs1Z1JQQUZKWUFzL0JIaVM4WjFtck9zSXVBbHFrOXowSmQxR0VkbzdKcTZyMGw3UjdIZW0zL29haitpVGVSNkxiSnBWUjgxTWJDcTlrZTdnY2E3UVl2OHFreVVTRDAiLCJtYWMiOiIyZGExMTkxNWQwYzdlYTViNThkZDNmOWIwOGY4NDJlZWEwM2E2NTcwZWRkZTQzZjMwZTUxN2E0Y2ZiMzAxNWMxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjB2TGZUYThWaEM3NmR6Mi9jZUNveXc9PSIsInZhbHVlIjoiczZhbXZsKzh6MjZ4SVZUNkV3dW90elVkSTVzNzlJN3V0YkNqT3I4S3lIZWt5eDMwbEdIYzBkWGRxZThNVGYzZjVCeTllNldzTTNRSzQ1RVZpQnU2Zy8rUE9pWDl6amxGU1NuaEViSE5mUlpuUnhIdStSQ0JPZ1grczAxbXJaRC8iLCJtYWMiOiIwYzE4YzA1MDc0ZjNkYjlhNWM5OThkNGRlOGVhMTE2ZjhjMWQ3MjA5NmUwY2Q3ODQwNjgxZThlNTUyZGUyMDQ0IiwidGFnIjoiIn0%3D",
}

