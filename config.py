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
    "cf_clearance": "SDPpCnPoO8w.0.BftoagTRz1PFUG7qFEUmsKbJXP48s-1791838499-1.2.1.1-GESOtRiOiTbQ4h40Iu4RGQQiHSzX7D3T4mmgr0yas_jP5.ygBJ2EsWO7roel5N3Yn5_wlN.dX658.aMg4PJSOMwKz6MYu2TcB.IZgMQ19tSsOi.lH770qtgVnpeMk7Y10pwJEbSHasbplPn2c.c484OCDnzeyXbKul5qcWnyoPVGVkx0oM9gIMEOp8aDgGsJq0.J64R6vxnXiLHO_BpsAA56hcjIlUIEj.7fWELkQkMZlkWl0jdQ1Zfos6286tyN.sQs8Ixt9c.sTlQtqQ7q1HY0eyuTVXuaDoV9P7jSeYImIx_nHE49pX2W9vsZxWUdYJDiLaupRaw91.BAG2aKpibATI.tZWKRQ5i3.W850q.TP3BL1xP1SxVFUPaR5ewgn8Sz2Go7Ba4ist6BqUcjhgaLWwAuWdtWi.CjPvhhfAC2UMDjLyM6S1mFGHU7I40ch92x73MyCNpnq_RTdsu6dOei6bVvuOYllsYQm577MGg7eaRr7ASGAobAeWYfcPOMco6_2qfWmV3_PERI2IS0ZQ",
    "XSRF-TOKEN": "eyJpdiI6InZ5WlpJdXNtT0NXd3U1M0FnYi9YWUE9PSIsInZhbHVlIjoidlg2WktpVFlPNW5weXhrUXR1eTVCSm9aZmVIM05FTVdwQmZyMGJHazd5SnVCVmhqT0k3RW04cW9DU1lzN2VmcUF2MHNuYUw0K1JvdWhpZVBVTXFKcXNrSFlWbUZaei9xcEFyTVBtWGxLUVVaVHNLNzN1QzFwcXdYaUxvWjNZNlMiLCJtYWMiOiI0ZTM4YzQ2NmU0MDQ5ZDIyMTQ2MTM0OWI3YmI1NGFhNDcwM2I0NTQyNjRlYTk2MWJlZjliMTEyM2I5NjEzNDNiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImJtN1RXM3pERS92NzlzM1RTbUdOYmc9PSIsInZhbHVlIjoiZENCRklka0tnVm5jbW9RT3R2MUI1Q2phNkJkSDM1Mk9xYzFyc1c5eE94aUlWbCtwdjJRUTZqL2lsSXlCbmZoR1BKaGt5bGNXSTErbXY4QUd3RHE1Q1dhZW1WYzZ1YUx1Z0wyd05KRWx4bkR0T0pNcnBoYWUxa25pRjcrZjFuckIiLCJtYWMiOiI3YTM4ZDAxZWFjNDkzOWI1YTU3MTg5YjE3Y2FjODRlZDllZjEzMDMyM2FjOTk4ZWQ5NmQ4YzVmNTBmNmQxMTBhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "LR5WMjBHFt97RiB9LV74EqsDxiKR7mQjafSG3DHzYdA-1791837663-1.2.1.1-46BKYFB8_gaUmuph.KmWyeZ79yYDpK2DUuOnEZ.96OTfo_j6zqaGl8k_TJaCafXoy.9zWl7icf2UosuMP3FRIG2LLG1BbMWnzqf7VXPdh0PerlIscraJNlbQGUScycJB9Bh7ZIF2oxGLPLprz5ErgHt2Kd_w_EXuWaV3grZpK9rawYxSqt4Z6NTCHC9MNLcU6fL32koigbh1HPJFITuye30_tcy6WY2BAHclpXEhsUCUPHzCzfqzmG4qyUX6HimVm.7gI05geHXHjM6ZV_2wkeihmsWL9XiJeT1G_WHGUMTN.71NlwUAbuWPQSDI389EObX6OXS5TmpJYa41LnOKAIvTVhQ6XZdb91BvSjpGno.ffBV9tqX1uWp4rZUkGBYV9GmYfjQ1lIrVbyTa8kE95d17bWb3NJsyZbDdV9zZD0fZUbdqBgFOTepv.Z0NzPubX_gFf5YBieKNAouMNQICj4U7hPz8F7jtdq6yTTZEMQJ4s7hV0oEZYu8YmMs7Hy12jNBAeqafk6.MvF7NDIkNCg",
    "XSRF-TOKEN": "eyJpdiI6IkVUVHdJYnA2Z2x1QzQ4TUJiQXBBQmc9PSIsInZhbHVlIjoiRkNpeGhISit4MUh0MXZ0czFsZ3BvVFJMNXJvR2JLbjBEbEhVS0wyTVNSSnBycnU4N3Y5bThseTYrOXAzNHcwU2V4V1pFYWNxS0h5WDdZMzZGbUhoYXBLYmlSd0NJTVExSEZ0UkhPdnppaGRhVEVzaU1YaE9rUkZIaWtoQ1NDMjciLCJtYWMiOiIxMDk4NjZhODZiYTJhOThjZjA1OGE5MzRjMTJlMTVhY2Y1YmU4ZGQwZTFmNmIxYThkNmIxZjJlYjU4NTAyMTI0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBFVWcwYmhPc1N2WUdYTEp3aURMZ3c9PSIsInZhbHVlIjoiNkdnY0VpVUlrVllXdFVKYjI0NWdQR1BkdW5OcEdQTDhZcFZ5Qk9IQnhHR0h4STFhdDZ6R3V3cFhGanlJc3FTMjlMRjBRaDdLOWtqejlnSlloVU90aktqZG5VMTBTK2tFcVY3QjVYdW5qbWxIYTM1SVZacnVtOGNBZmEreDJ4UzUiLCJtYWMiOiJjN2JmNDA5MTNjNTg1ZGE1MDUwNGRkMzkyNTE4ZjMwYjYyN2UzNWM5YTQ0ZTVlMDQzYTk3MTcxMTQ3YTM5NjQ3IiwidGFnIjoiIn0%3D",
}

