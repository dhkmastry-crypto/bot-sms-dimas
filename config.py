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
    "cf_clearance": "XF.1ZcpD_QaUsEULjbDu8TtGYfNYrwl.BAA8sZikiTw-1791836684-1.2.1.1-kCwC0i1kuM8Q1lp58hKROHKHX38xLVIqXIQI0wDfXiBJnfCeTes2alX7MksstE3L26PZr8A5Wa6SWkWy_2CtYQBmFT7BXxy7qopA34Kj69aPYazQBcfKeGWeQagLD.2AZy7DS.qBdqYCnQbddEFXJ9CyVFZr_HamdhFVxcQX5nBsTHS62Hd8.wDiTRnViqhPH1cmH1rwlAzlK8Vt6OrfBET0_tWQA4zAYJajrrkDfA1I0oZBN19QuxzQq5ieqdrc9u6C_ajRug_bxaJ2nchSuMQgDmQp6cSIlMH201f9nVuhnX6akEAbEReS4znjSgh8ZannMs2JtpZoW50qMRadGcdLKlA972hEPF.ZFpjAy7Bk4TD52UZXo22VZMLu0GDLChEZnVqnhHVOOd6dJcWfo2a1Uo7DbR2t6wVLb22Oe_10gc1ojE7ju0Pmaaf8.xljl2PKzX6ZErHzhW8ic.oVH2cQf6XDc.2NHO7G8cyg_DrFiWLKb2dSg39WCH8F87a5e3B.AMztg.xJsdg1XfYauA",
    "XSRF-TOKEN": "eyJpdiI6InVFZ2xsbnhvM1djTWVpU0hSMGs4b1E9PSIsInZhbHVlIjoiWFlPdjkzUWEzbFgrall5eDdBUFNqcm9BYTNwTDZkTFRaL0ZiZGtuM2VnYjBacDNsWXZyaldJeUloZGI2U0pNNUROM3Q2d2RQRDIrL2pDSXhmVVh0bVBEWk5yeCszWGo5Y2tSR3BaUzNKd2tCUTNJcUpiU1NSSDdiUXVPQ200YmMiLCJtYWMiOiIwYTI3OGI2MzhjNmQyYmVhMDFiOWY5ODQ1N2U1YzBmZjk5OWYxMmRiNDczMTNkZWE0ODczMWJmNDIzYjlmZWQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxhQ21JZGJtaThzWjZsUXhSejBqVUE9PSIsInZhbHVlIjoibFF2YjBHQ1c4b3BRSnRUOVhUSkpDY2NnMFVkcVVRalNuY0lyRitXc0pYaHc3MEdWVmhvQ01oNWZYVnhOZFFKZnFrV2dwd0hLcHRtbUpQSnpBZnIxMmxZRE0zdFBzRGozVkNNWHlUVDB3OXZJbGQrUjYzWFpzelpBbDBjWUxRamwiLCJtYWMiOiJmZmMxNjQ3OGU2ZmZjYTk3OGU2ZmExODRmNTNkMjEyZDU3NDU5MWZmNDE2MmM4Yjk1MTQxNGU2NWI3NGI1OWQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "LR5WMjBHFt97RiB9LV74EqsDxiKR7mQjafSG3DHzYdA-1791837663-1.2.1.1-46BKYFB8_gaUmuph.KmWyeZ79yYDpK2DUuOnEZ.96OTfo_j6zqaGl8k_TJaCafXoy.9zWl7icf2UosuMP3FRIG2LLG1BbMWnzqf7VXPdh0PerlIscraJNlbQGUScycJB9Bh7ZIF2oxGLPLprz5ErgHt2Kd_w_EXuWaV3grZpK9rawYxSqt4Z6NTCHC9MNLcU6fL32koigbh1HPJFITuye30_tcy6WY2BAHclpXEhsUCUPHzCzfqzmG4qyUX6HimVm.7gI05geHXHjM6ZV_2wkeihmsWL9XiJeT1G_WHGUMTN.71NlwUAbuWPQSDI389EObX6OXS5TmpJYa41LnOKAIvTVhQ6XZdb91BvSjpGno.ffBV9tqX1uWp4rZUkGBYV9GmYfjQ1lIrVbyTa8kE95d17bWb3NJsyZbDdV9zZD0fZUbdqBgFOTepv.Z0NzPubX_gFf5YBieKNAouMNQICj4U7hPz8F7jtdq6yTTZEMQJ4s7hV0oEZYu8YmMs7Hy12jNBAeqafk6.MvF7NDIkNCg",
    "XSRF-TOKEN": "eyJpdiI6IkVUVHdJYnA2Z2x1QzQ4TUJiQXBBQmc9PSIsInZhbHVlIjoiRkNpeGhISit4MUh0MXZ0czFsZ3BvVFJMNXJvR2JLbjBEbEhVS0wyTVNSSnBycnU4N3Y5bThseTYrOXAzNHcwU2V4V1pFYWNxS0h5WDdZMzZGbUhoYXBLYmlSd0NJTVExSEZ0UkhPdnppaGRhVEVzaU1YaE9rUkZIaWtoQ1NDMjciLCJtYWMiOiIxMDk4NjZhODZiYTJhOThjZjA1OGE5MzRjMTJlMTVhY2Y1YmU4ZGQwZTFmNmIxYThkNmIxZjJlYjU4NTAyMTI0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBFVWcwYmhPc1N2WUdYTEp3aURMZ3c9PSIsInZhbHVlIjoiNkdnY0VpVUlrVllXdFVKYjI0NWdQR1BkdW5OcEdQTDhZcFZ5Qk9IQnhHR0h4STFhdDZ6R3V3cFhGanlJc3FTMjlMRjBRaDdLOWtqejlnSlloVU90aktqZG5VMTBTK2tFcVY3QjVYdW5qbWxIYTM1SVZacnVtOGNBZmEreDJ4UzUiLCJtYWMiOiJjN2JmNDA5MTNjNTg1ZGE1MDUwNGRkMzkyNTE4ZjMwYjYyN2UzNWM5YTQ0ZTVlMDQzYTk3MTcxMTQ3YTM5NjQ3IiwidGFnIjoiIn0%3D",
}

