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
    "cf_clearance": "9jhYsJyONM7Qm3JH48OTLyjlTY8hR3uXub8wEhsAQ.o-1791858392-1.2.1.1-ptBXMEwEjnIWcRjOwBGZXtykDCJ_Iec193BsQ5fT7kTM7SAJIgupMF0MZYfG1FfDg8UEE60V3LwecYgdp8UALd9C5fiQjgnQn8gPMJyBwcVcFS2lxy2djjVUN7xPSa4cxNMBxk_Dgt69xp.MA1ByjKwbPv3MDLJ2_Po.rljIUb5sWesUw5c4fUhuslj8pjpQNOQUCzPcL2JqFA6NR1mRvUKSznvr4KH4OESwI91NYVk.O397.qRbtNAht9TUW1k3EukEkY6xlTncttiaAIx7drSeq8XbO6CAyMdrg9Clkj8wSh5c0ngI.CX9SLp0W_RP1vAkZPlY2g5cWg.glfJFoVXwCk4U0W80lqv4ByaXePB.eS2o6wjyALA7z0vYgTYW8TgPnYX1zbSproIWO4URoYrrPIJsnyFVmpOZUpU37bivcbbdoFPKmXZ6pgWCAqYRCBAuILYjCH6VvbWQZRvBDUcQ5IouFTFqkWVUAdp0j3KDnkEbvdCJqhNXu9fxkKfA6Nhl3SlDUJc9FanBWeszdA",
    "XSRF-TOKEN": "eyJpdiI6IlN0WjlrSVVBNHpQamk3SjFBTVpLNXc9PSIsInZhbHVlIjoiK21NM1hlUkNiZ0o2Ty9mS21ZaUJ4THM3TTZYYk9yMnA5N0VRM0VNeFRRK2RyQnlucHdKQWF5YVJkTGEwUmlkM1B3RWNLckdGY2pRUEpMd3dUSWNLYk1lZDZKa0NHMGx1Y2xoOHR0cStIQXo5OTlGZmlrTkM0SGxhalNFdVdZa0giLCJtYWMiOiIzYmZlZjE5ZjEyOWRjZjhkNmE4NTA5NjA3NDg0YmE1YzRmNGE5YWIxNWYwNGViZmY5N2E5OTZhYTdkZjQwOWE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjR1T0xQakg4R3ZMUGJtWXZrQk85T1E9PSIsInZhbHVlIjoiQllSODFsVzg0U1Y3NjgxUUNSNUFTM0hHR1haTnRibUZ3VFlXNUxXS3RyMkFTT29GWHNzMVpoT3VlcWx4dUpKbXVYZkxRc1gyV3RJTloybGFSVERIRkswS0RXZWQ3VVJtVVNlcVZxQ3dZeUdyVVFibFZXRjk1ODhwY3Fta0I5bTgiLCJtYWMiOiI1YmE2NTYzNTM3YzdmYzMyNWVjNjY5Y2Y3OTJhYzE2ZTAyMWE2OTAxMzAyNmRhZWM1ZTc3YmE1ZjYzZjM2ZjhjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "hJ992s.w8mAZfo7ig1a5vwEtFfa1l9vtS7dhvKj9jlM-1791859568-1.2.1.1-7Cfp9EONiVq7OvV.YJKDANzFnhmGn5Vbg8T7ueKB8j9Kxc2QHwiXQOM9Y7Uk0cKP7lWEyyZ.lltJ3ezNIU6b3xTE5ZHwYa0mgGt1lBlysdLGXllqGZp4JpSu0AijKmvHt2B2Q8DHQ_O0iwes1P2TQ_.lkCUYN6LPNd1MDGQDgG.muh7bo2CDGcUdRV2V_FeQxFjeJ8kPhz_y8PJ7OBtFU52CIMq8IqDrLDvslBdiQhousgsG4mQFp3qXrfNmDvz0vfHzwN6J3341fPjno37KmCrzeGmvEeSVtvk64siROe35PeSOKxpjpImM8CfNxPnd4jYKHyW6mi97A4tYhNV.SCOE8jPJIsiFw36.Y0tc_Ie4mgcckofaSRvfwzH_wzNwshkK_seb1bEkyhzzESFzNSQ5Yy.FA.38pQ69CSQubVrLTfAQNGYj7dwPDKazav7_QSEvKLVL65BenvdC0VD_WCYgGOOIHF27_O3ybVfZbusjeAInk4QWWP.Z95l2.NXQXNLo1C7Pp6pTyWUasE6d4g",
    "XSRF-TOKEN": "eyJpdiI6IlNZSlU2bWtrRURBVjZoQWVxNmpQSXc9PSIsInZhbHVlIjoibDZFVE8rNzFDVzZreklNNlk4NFBuNkJPcUVFSENTcDR1Zyt5NjVmdytRK3NaZVZuZ0pDREYzcnhTMnJYaHgveUM4S0VNT0duQnVnYVErVGZieityN3B2L3RaTzVYam83SHJFOFJBK3dpUjY2aHU2bEpxUURYTkxpaHFnQXNGc1UiLCJtYWMiOiI5ZTA5NDY2ZGYyZDc1ZDUxYzFlOGYxOGIzOWU0NmJiNGJhZTQ2ODk0Yjg5MTQwYTZjMjcyMjY1ZGZmNGEzY2E5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjB1MlFmRE5zRU42dkRwMThzeXdxWUE9PSIsInZhbHVlIjoiUHV5Vy9vUzhWVVZpa1lTc0pQdXo0WXRkVWVYNDZZZDBET1Fna3hnc1RmT1NXZi82Q1RIY2hPR01pS1FBUk9HaVZjM0RGVzJuMGprOUNEaHhBd3NnUy9Fb2tlSm0yS293QXFmV0tqMzl0Zmh5a2ZxMjBPTFdZTFdnVHVkRkswcEIiLCJtYWMiOiIxNzc1MGMzZTg3NzZhNDEyYmZlODQ3NWYwODIwZTExYjgzYzczNmM3NWMwYTNiMWNiNWE2OGFjYmQ3YzA0ZjZmIiwidGFnIjoiIn0%3D",
}

