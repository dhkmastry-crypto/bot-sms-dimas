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
    "cf_clearance": "ZGvyh_PC_qeSORLHzYbOLgcrMA3cjegOFgJ20tIuB84-1791879470-1.2.1.1-fMrr3yK3oJ52OGh6ZFK4czUlioPg2tIyaDaQB9iy8RLvwQIlEQ0d3rlZKUZQPwK6AKY2XhVhayYpotq3bhbRcS4ZQzt5KMCg1VbdRmkX6HLBIe9fDgTvGoEKzyZdZgo2gLKL.dgxqyYQzRpY2iNwEsVG0Fp7dHaqcOUgCm5ybrLN9fy8a4ilNGryV1vMHGRBT6wTObN1n2PpjtJmC.l1Kaqg5ljL0nXOR8CL.JgxNXk27hqRaVZMXbp8fQ_Is8sNBR0Da6GqarAUEVWC4LRYNVz8LcdPoFBWzR9edROQFYGj8leXfjvBXna_sxe5XXDEXfVGA6UKQH8_D_T_zdBDOL_6RxOSC2eJHOVqB.jInPXOFBiFuHBNNJxTknl7sJ9X3RrDRye0YMYRsbtBAhATqSt.hS7Tynm2w4KChp8rs1Tjc7cvlLi4.mjSovAylMoSjaEe09iNz7Dguo_I6lmP6gHukPmWGtUguZPgkcViKfp4qFfXM.HQrBW82BT9W78V2t9fo.mehTI6Kxq1KJGR.A",
    "XSRF-TOKEN": "eyJpdiI6IlRrR09WRW9Nb0lWSTAvRXhnQVhoR1E9PSIsInZhbHVlIjoiU2pacERoYm8yTDl5NnpIdVFTWjF6RFE1UHZYVnE1Y3N2LzVuRlNXWkZzQTcrZVoyekxjVmR2UVd4K3BNYkhKNFh5ZGhOc2tMMndVNUVaNHVzOFhaU1RGT1I4U200Y3hXUWtBK281eTNoZE9NOEdRd3dxcVkzZnRobVAxck1SUWUiLCJtYWMiOiI0NmYwMjAzZTkxY2FiNDljYmRmZDFmMjc4MjNkMGM3MGQyY2U2NWUwNjliZGU5NTc3MzIyMzFlYzM3NDg2OTQxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJtV3YxUERUQ1ZIb25JamV4V1NYL1E9PSIsInZhbHVlIjoiakYrZWZGWXFMZkVKWmJ5STNJUklYVXVVOXFKTEFNd1E2K1g1ejJCNkJnRVh1WHZJOHphZjFwcDJGUjJwaFUwWU5SSEtJdVhuc0Y3UG1CdnZqY01Xbm8xdzY5RkMzL1RoS2hoY0N1VEc4WnN0Szl5aEU1cFV4NE01b1hTaFR5QjQiLCJtYWMiOiJkMGMzZDgxNjAyNDVlYzEwYmI5NjE1MTJjOTIwM2EzNzFhNGJjMDMyNzUxNGVkMGNmMzI1NjkxZTZmYzNkZmMxIiwidGFnIjoiIn0%3D",
}

