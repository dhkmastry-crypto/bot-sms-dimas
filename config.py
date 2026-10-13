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
    "cf_clearance": "4ztRWIY6lF_Tk2TWLLqHJy9Vjq7ctQRwnMh3t4AwpBM-1791871043-1.2.1.1-s1dviQBzPHvHwkq6F.LygJdo.28VecV2YXFxPcL4t9dLDTykn2PPR2zddMnumx2l5PEdjno1Voj2YTnj4MTBdkvwhUnI7UMa4HbfWmFW9xKH8bhbMZij3ltjnPlQ2jlP5NSWO9bAhDOEflOatkz.wLa0SP4tk_BIs__AnePjdGXtBD1ZgizJBcnPxCpnfDV_7RO3LRbOuEJCBgqBcXjeSBNNQIvBR07wc7dObEDixCOUOZDpPkA7iC0dgEc0mnFeOtzZz8ACGYctwnMCck6vikk8b8UHUP_YGUPUKXhXPPA7vq6VddBZM6_o9JcofMkOtjvguKOZghm.MthvCxmyurteXJFVNAyfOlT8erPRt8Z8ZCqXcaQh6CSEbzPX2amZj9_okBU7tU39xEZkrEaBedFSedQ6uL3vOOu8yd_udTw1aL9DmZcKiaSysUo57iNpz2QGshxS8SyV1z2I0NAMMRxmo_shsFb5xyVtCSDAGDcQNdYaC7qxVPZ4h2zW3xk2asqHkOKv61760Zy02Fxb6w",
    "XSRF-TOKEN": "eyJpdiI6InI0Zk00bzhvU2dwUjBNYkpubk9PcFE9PSIsInZhbHVlIjoiMkNDaERHeFg3Z2dDWUwyWDdaeHRYczhwTXRWNHBrZ0hmSkN1T296VGhWRlBuM08vajdPNzhGU094WUF2dkhJOFRMZW1lSktFOGhEZ09WTmRveGQ2UW4vbS9Uem5seUpkRTNQV0djKzZsQXdsL1RKNDVjdm1NWWZVdWdqdmlYWlgiLCJtYWMiOiJlMGU0ZGFiOGU1ODEyMjdkYjA0MDU3ZTkwYTEzNjBlYWYwYzVhZGFhMTVlZTBhZmQ0NTNmYjM2ZWNhZDNhZTFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRVbCtydXJXYXRkWDNqbDlGU3pPbkE9PSIsInZhbHVlIjoiUTBaMjJRVFZOUkRXSUFMc0dBRVhTbG95Rk5qYlJuajVIR21US1BvOG1nYzB6ejF1WXkxSVZtTmVzQXcxK2c5TjNmOS9UbzRpeS9EV2tVQXM2WGlZWVJTNXE4dG9jUWpycTFUSEpYWTJpQjVJUUtIc1VhdGZWOWlJZjNNTnlrN3oiLCJtYWMiOiIwYzU3OWVlMDUwMDFkNmNiZGY2ZjdlYmJhNjdlYTRlZmVjOGNjM2Y5YjVlN2VmZDdjNjk3ZjEzZGIyYmRhMzM1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "6ONGAKQV1tvzrEQyTMZkOYbTv4H7CZH.0tqwYjRdkK4-1791870434-1.2.1.1-L2HhPC2QEHgiuUZ9K0OyPr6kX9da8HeT0Eaul7bW5Zz1eLP0LqIEvf7LYCWm27fJ1c1zwGVqieXHmM7H6xcgo7pbEozopo.X_FBFttnRpPH.JPzPjq1B5rWx5JCAsTnJ7iaRGAB1Q7sYkyx5198uI5u8.sAYaCbH5rJJN0xo1W_MJ00At4i5fYntelduTBwOCFgXfyj0sZ0AtRy5FyCVw3XZ1llzUIHVnzOzNh.lz6ZxQf5WChwxmdNRtlefM0XIdqtB3w_XgnzY7jwzs0IkptT1nc8kOVPnVr217mKHOuy8a6lWHkMqcsP6VWlSJypyUvrmuDCLLyi4yoWOfTDGGO_dmOeY5ajQiCPq8BrtcE8kukYZgJ_6lm8uaiVsj78wjAwsMrVy6Q1NQo3uNH4NvoDV.gDURhVfajbNGsL1WrkQcoVy.XNAwRP0rhOlvlb_eONQYCb5ug0bRjdVE1ICltiPf3MqxkAyiWSy3zF8WKBL1O.vx08mLaBLrX5.MN3b6S2IpZUoYW9t9TjcHpHelA",
    "XSRF-TOKEN": "eyJpdiI6IlVXT0ZJcEhvS1VRQkxsQkYxWHJvc1E9PSIsInZhbHVlIjoiaW42emtlQXFETWdtV1ZhMUxKTHFVcVFETkNwN3I1NHVKQlp3SUVmZ0t5USs3a1JVbU1yT3dGREpvWHBtM2JNaVZ3TFFOTHR1WTk1b1IxdE5SSkR4RkZvaFcvQ1NpTlV5Qm9STnpZakc3ejZWbjdEREZ4NmpDb0JVRHM0UUFUNWYiLCJtYWMiOiI1M2JlNTlmODgyNTAxNzY2ZDUxZTYzZTAzOTJjNzU5YmVhNmMxMTFkN2Q5NzM4NWYzMDVmM2E1MjZlMTc0N2MzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Inp6ZUpCa01oQUEweUNpKzhnK1JoZnc9PSIsInZhbHVlIjoiM3NwVEF6MW1jM3Z6N29MZXFIREdqbVErSFdoblZId1cxNm1qdWZkM3hNRUJkNE9xTFI3YVVPdUhNSVVUMmdOdXhSQi9kYUFPdnV5cWFMbW8wTlp0V1BEZGdVR3ozZW5PLzd0d1ZuMkxtSWlUMG5zZkZ3eEdUWkc2dS85VkkyMm0iLCJtYWMiOiJhMThjM2Y1ZGNkMDYzMjcxYWNjOWQ0YTVmOGQ1MDQzMjQ2MTQ5MmYwZDg4MGFmNzk2MGJkNmIwYjI1N2QyMTU5IiwidGFnIjoiIn0%3D",
}

