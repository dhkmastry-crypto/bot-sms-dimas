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
    "cf_clearance": "Zc6RBQACGkow0vg8QY0I56dZ669xvTsm54oqZ.NrViA-1791880092-1.2.1.1-Y_iGRnTvIpu1rfIUpEY7Q669mQWE473Rx0H0sA9.ZTlfZ71aefdiU7cn4eYWyHw8uGMeQU8B19GI1gCj36nkmVLeyWo.bMnXbMFSFjjRkzJC7zELkDriVWJfNpxjzrOwdOYc6hKCwE04sWnRjLBag1LSInyyyODoDZG3UbexQqLAjrS6PvGRjhI0B07SYbdFCr7fDJYonNKUo1Zv_HEiXV01wCAbQHBWfQuTrtOnuJ8_Jb4sWFjZ8uOJww8lzj01RdFbBNaz.nvUEB.rb64IvfefLumjoUbttoOsKMXGiA6j41_fe8dsd1mQEANgQHvZJ0n2A09L2fY9V4LJPdqWdMCXS5NauwCY13A_rWoxqWI2ZCk9KgC72iMaryuNGuMZxwYz94mz4cwUvJe5LCnFBcAIJbt76rTqpbnSyp4Wk0PO4WrulfX.aWJYdHidrGcC9LLB.NKzwpQ2sf5LznOD9EkxBUVl2Gr8Q7qFg1xg9A5Hdis5PpCWwEdmci0t5g3.Z7nf70EmgYxlXg6kI43E_Q",
    "XSRF-TOKEN": "eyJpdiI6ImYwYi9nd0hjbkJZMnVJWGpMVEcvalE9PSIsInZhbHVlIjoiQkJNY3M3WGV5eHVKQjJROXYrTEFZWkE4bVNsZHcxVjFBM0IwQjJ2Y2QxMXhPTEhCTVBtREdWVllNQ0hYQVR2Ym5wZGkvaDl2NG4wKzEycm5sODFxTGZva0RTZXVaNGNJRGpmUjE5aXlNNXVSTWNHVGxKU2h4dzBod09EYk5XT0IiLCJtYWMiOiJjNTgyOTc5ZDA1NmE0ODcwMjM3ZjY0NGUxNmFjYjg5NTlmMmU3NWU4MDhiYjZhZTdlYTU0NzE4ZWM1ZmQzYTQ2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikp3K3BRZEc5N28rWTNMNndIYWYxSFE9PSIsInZhbHVlIjoiamFYUmZBbG9hTjBjQktsZTZ0OUs2dnU5WVFuS2U2MWMyZHNGb1lZOUJjbTh3U1J4NEVCK3o0VDdKR2tJcVVtbFJBQTRnWStITWg1cm1TTmRDb2V1OUkxZUdDQmZhcmxFRFNvTWdrNzliNWwvaXlrWmluczczUTRaVCtXeUtpclciLCJtYWMiOiJmZmE2MzY5NzM5YTMxNGRhM2RjNTkxYjc5YjA4ZmYzODU3NWZhNGEwMjAxNWY1Y2U5OWE4NTNmZGQ3YmFlMDA0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "mzNCvWgySS0Ir5MnH4RymK3fmoOI4GH1Wex4SxcjQYY-1791881278-1.2.1.1-FDfkm3OuMlhYuqkfLJt5HobyWfbO_egYBlFITqXQR.N0w2JaL6JwC7MN6zE2ubw7rwosS51D_w8am3xdDXbhLYWR8o6iItl6r1s1kmWT4bNFGOK6LdkRz7NDSVp4oT1r6E6xgHszlz3krrVoxFYTrrmFfoQtYLxKmgjatuhFQY9qIMSdLK3tdox6fYJGew.uEkeAnDR3XGzYHIk8WzLeqiajIY1Iw_3Hg4LwPwfyDO1vg6tUZR1r1bx6Q.LPyl05m.2RwYuic93s5LZMeYpqOAkSoXr4KJ167lG.l_XMUZFsdow0_bG1vdNH2WmEI9aBXa1P6Vp6EoZ3jb5Pg_ktcbhq9m5SuLpEK3NUjfYJape7GtBxc4JkzIRoFa4.PiHPlqFuKk_cYst3vLpJXaWZpSYc.Y9esmWnKGO1dT9xdIjsOjQl6v35lcSmT4yZLCU1aCh4MGRlveCWztsy7qwnRcDN0hGndY78uhR.I0frzhnzjgVU9jRb4hCtc.4e6I8yZqxec45.N4NQxaDSkMk3RQ",
    "XSRF-TOKEN": "eyJpdiI6IjZVWitFZythbWhFMXh3dXV2b1QxV0E9PSIsInZhbHVlIjoiR3crcDltaE0xSWZlMjZ5K1ZQOWFwQkRaMWhRWW5VWEVnZlp4TW1kVktSNHM3bml0b0ZZalVuT1dZNDRUcmFBR2xNczRtQ1MzTjJpK3RKWGFTSG1jZW5RQVYveGVCaE1NM0dNYXhISXkwUTAwanpFOHlZRUR3ZmdJWU9pSmpJQnkiLCJtYWMiOiI2OWE4M2MzMDBhOWYwZGM2NjFlMjU4YzhjZWQzNDllMWZiNWZiZmFhMTc4ODU1ZmUxMzJlNzU2N2RmZDJiYTIzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxQMVhEQ2pZZjBzYldrVEdRU0tYNGc9PSIsInZhbHVlIjoiS3BuUGVERVpCQzJaQStNY21tVWNTWVBVL0U3bkgxbVZPNnV5bUZOTGpOUEdRMmJEYlZVT1ZXY0RYQ3NqNWhzQno1UE9hWG1YRnRJNzFhaHBxeWRIWnVxbFVwU2dKSmxpNjRBNkNMb3AxR0ZhNGFRVGI0emJxT0JPcGo2cTMyRzgiLCJtYWMiOiIxZjg3MDcwNTAwYzNmOTI0ZWYyZDEwNWEwYzBlOWViZTcyNTVjY2IxMWVlMTEyOGM5YmQ1MmI2ZGM3MmM4NTdkIiwidGFnIjoiIn0%3D",
}

