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
    "cf_clearance": ".ZeTt1o.Iu5Grglwq69J9MgnNwXWpQPFUTjDqSIKGjg-1791860198-1.2.1.1-AcHp8woudPIbUfCctxHRrE_7kRZWdlH0hlnghHugp3.F260C41xqxtYfbZiE7qqLnAzrx_C7mUeWi20ao1kyN79URq2J8.9ptYWRL9bKXNUZ68LlIP4vMFOhcxGumODiJAU.AAhjg.QAgfNjVf8s6bTJK1i2fz62GRXjAWWbk1paR2cvucW6f.UG54_fWNcZrMNrOWLTT6dZp4zRL9n5hAbhwzganQQLduFtbe818h4_QCktrIFIHrDx59Omwv0NS3Yg6Zl4UIMS6.2ecEkNFSGa_Oncchwbn2f29lU.0xIjBjgC5hKyXQ2Fu5La_ayOHMFDWQAz3Sj8nCLvTdPPbwjxS8c5HH9XTqXVJnZ87A4Y8jbUltjmxWALeWktv9EhijNdDLtPmUPUg_oD20n89jvbh2tvKgNqycMLIIJ_4M1S97rDDG3tUHej0IGKe_qoQNZlrAGoKp.z76iK0CkXlcsjftAcBZBS4t.ztfO4io1HPM8CzLsAorNXH38ju8glpWo4U067BnSrDgcbOP75hw",
    "XSRF-TOKEN": "eyJpdiI6InZZYU1oRHExTzk0TC90SVVxdGsrYWc9PSIsInZhbHVlIjoidUtwWnIrN3lJaUE1aWlOY05mV3dpazZNWm9QUXBGc2d6d0VvL1VlWmJWelc0LzUrb2s1bGtEMG5DTTg2RlBTMUhhakVhVTVIR2ZTOWthdFJEdHEva1JSVlcwYzFhd203UlMvbUxvOFI5WWRUQXIzZ3R6NzBQN1NhQjRqSjBZN3giLCJtYWMiOiI3OWM4NjY3OTMyNmQ5ZmJiM2U1OGVlYmY4OTY3ZWJkMTEzZjMxMWJlNTdiMDJlY2JjZDA1YmUyMmVlN2M1N2IzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRBNnJISTZxU1JpZnVDNmhKdVRVS3c9PSIsInZhbHVlIjoiMFhUYnV5WStNQnVNd0EwYmp4YWJpQnBYeSs5MXpQd1B0c3NkTnkxSXQ2OTFCekxGWnp0ZUJzVlZScVpadkhsNWRqb3VEY0ZvMFNUMDB1Y1RFMnBuRlE1T3FpVHBtbStSTEVJTWdHYmpVdDlFNzRSTzdYZ1hnS3JhR2cvSnFaRUMiLCJtYWMiOiI5ZTY3MjVlNTBlNGFjMzZjM2JjODRhMDE2MTc5NDU1MzBiOWNjZTlkMWI2YmNlMjk3MjU0YWEyNzAyYmQzMTc2IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "hJ992s.w8mAZfo7ig1a5vwEtFfa1l9vtS7dhvKj9jlM-1791859568-1.2.1.1-7Cfp9EONiVq7OvV.YJKDANzFnhmGn5Vbg8T7ueKB8j9Kxc2QHwiXQOM9Y7Uk0cKP7lWEyyZ.lltJ3ezNIU6b3xTE5ZHwYa0mgGt1lBlysdLGXllqGZp4JpSu0AijKmvHt2B2Q8DHQ_O0iwes1P2TQ_.lkCUYN6LPNd1MDGQDgG.muh7bo2CDGcUdRV2V_FeQxFjeJ8kPhz_y8PJ7OBtFU52CIMq8IqDrLDvslBdiQhousgsG4mQFp3qXrfNmDvz0vfHzwN6J3341fPjno37KmCrzeGmvEeSVtvk64siROe35PeSOKxpjpImM8CfNxPnd4jYKHyW6mi97A4tYhNV.SCOE8jPJIsiFw36.Y0tc_Ie4mgcckofaSRvfwzH_wzNwshkK_seb1bEkyhzzESFzNSQ5Yy.FA.38pQ69CSQubVrLTfAQNGYj7dwPDKazav7_QSEvKLVL65BenvdC0VD_WCYgGOOIHF27_O3ybVfZbusjeAInk4QWWP.Z95l2.NXQXNLo1C7Pp6pTyWUasE6d4g",
    "XSRF-TOKEN": "eyJpdiI6IlNZSlU2bWtrRURBVjZoQWVxNmpQSXc9PSIsInZhbHVlIjoibDZFVE8rNzFDVzZreklNNlk4NFBuNkJPcUVFSENTcDR1Zyt5NjVmdytRK3NaZVZuZ0pDREYzcnhTMnJYaHgveUM4S0VNT0duQnVnYVErVGZieityN3B2L3RaTzVYam83SHJFOFJBK3dpUjY2aHU2bEpxUURYTkxpaHFnQXNGc1UiLCJtYWMiOiI5ZTA5NDY2ZGYyZDc1ZDUxYzFlOGYxOGIzOWU0NmJiNGJhZTQ2ODk0Yjg5MTQwYTZjMjcyMjY1ZGZmNGEzY2E5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjB1MlFmRE5zRU42dkRwMThzeXdxWUE9PSIsInZhbHVlIjoiUHV5Vy9vUzhWVVZpa1lTc0pQdXo0WXRkVWVYNDZZZDBET1Fna3hnc1RmT1NXZi82Q1RIY2hPR01pS1FBUk9HaVZjM0RGVzJuMGprOUNEaHhBd3NnUy9Fb2tlSm0yS293QXFmV0tqMzl0Zmh5a2ZxMjBPTFdZTFdnVHVkRkswcEIiLCJtYWMiOiIxNzc1MGMzZTg3NzZhNDEyYmZlODQ3NWYwODIwZTExYjgzYzczNmM3NWMwYTNiMWNiNWE2OGFjYmQ3YzA0ZjZmIiwidGFnIjoiIn0%3D",
}

