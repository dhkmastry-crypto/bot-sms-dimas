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
    "cf_clearance": "6B.QuhTmSThCMa2Y27A.3YontP1Aiw8C5GFhaQfUR_A-1792021052-1.2.1.1-HXB0QtzyjS2sWSYzgNETPfI6cboofY5rEh75suIUJVjB69ogqmts0sX_m6uDBUgsZoBLCHbSw6NKQhgM1dKracO4aSQ.2WWY.OgYxryDNnXD6hJacn2oHMbciGVd8rxuZRqVdCzV4OJYaOVe4vbNjNCljJASjjLXBcZLZ7h8BlwN9NHlBdveYQTyRy4FsTjctO26SGwG6zmuoanxXyEGr14zDb5ILyJJJYmekz_mrf96Ujixuh0EFCIj4wZjy.EcV4F6eh1QLB7LXDnl8ryjsKRCrKAeMINBKvTK8AK4ijrGJ4ADruOefd8Ru21DtIPcS2R4TQwuDjzcEsFaq7HZO6sofNS2Z2C_kSzLnqwuIiJzN2eLuN0i5BnoDqihqJp2BBtwljKCeLa.k..3738ky4BZmskGxTiSkBGM_JR7tXn98rb3Fc89intMZiv6Z2IsjtGl0PBN0B6t0xabYsAosQ76jkSlCYexIbSj8DxQvE4Mj3SyxgOA15GueHkn2cNEK.IHBqzTc32_rOikWY6xJQ",
    "XSRF-TOKEN": "eyJpdiI6IkFTZCt4VmxtUEUyZWpCd0lsQmRyVXc9PSIsInZhbHVlIjoiOGxScjdUNHFIeGlLNlU1UHpBYnVlMmZGVm9uakNDWVVEeWdDT0g2U2RsVnJwbFY5eS90UmFnbFFWUXo5N0E5VlVmRmMyaU0ybG1xcDA4VVdGVmJZb0NzWERYTURoZ1VkM1RSWnBWTVE2aXVpWjZNeHVvVitpZ2g2RWtVOEgzNEUiLCJtYWMiOiIyODBjN2E5MmNkMzc2MjMxYmJmZjg0NDdjOWZjNTlhNjBkMzYxMDcwNmQ5NmE5MzdjOGE1NTAzMjdmODhhZWYwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJQRys3TDZqZE9RWkZIbzIxZHNvNkE9PSIsInZhbHVlIjoiMk1CVm15eGNnY2ZYREtjMDZ0WGRNOXJsSmpHVWZEWnZERFBRTDJjOGc4b0NtR0ZzRkRydHBmdkhjUXQyRndmU0xtQkFNOGlwOGtnSGZHRFM1Q3pEdzczSVR5MG5NVDhScjVjc3I2WmNGZWJIYlVnUVYyZTV3WHdjNi80eHVDOHQiLCJtYWMiOiJhZGZiNTVlMTgxZTlhZDc1ODJiMDlmZTRhNmMxZjJjYTdhYzFhNTJkNDdlNWQ5ZmEwYWFlODIyZDdlZjBjM2YzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "vWNM9QX6KVjPby6OcaHRt7F0RfuMgo_ZVlZz62yf4lY-1792021041-1.2.1.1-MUXkhM1I7Hy0xnJ58x.YAmxP94d6MOFOISjJw2w1kBO.lR97ScK61Rwm8qNy65maN21LEFgisy2wcz4aBPsHnyacN4zUj8XzElMD7RGbUvhWq4_9oBnnzIJfRl6.TOU0nvfmOrLzeCn_A8NlMRFZO.MXB0D1c78e.KGRgMDFe2CSI3P9Dv_fOZacIru1h1bMJBq7jRDck_QyCStTDsb7HyZI0m5OjbZL_.Mn9w0u9wez_nJHFXpn1UnnlMKlNoQmLwOu9erbpCdRzTW8wpQyiOyjoxxQy21Fe89ig.bjiUK9JwoYJP9hGxlxGySb.zoHZTbTUZ5MIMWOMZ0W29T6lh3MItpon70bZQpgJLwcSt6KbILueKb.usDnszQnKCcPfmnomrAfzfdAYAKgR5oVx3CfwJnUN2NBOLhCJdS_3kBB5qvZdP0OrkL.YAYCjvIKLRhqWwx753vNn2vvSvBznLtKqy5XH.Bww7xdcscF0H_Zd_lykr0KQ_gPkgFDuI7.HvgGvFLfjTfcw3lQdfeSMg",
    "XSRF-TOKEN": "eyJpdiI6InNvTi9vZGhtNkFGNEtDL24vMjRNcHc9PSIsInZhbHVlIjoidGgxS1ZQWXd2VXZrZmsxWDNMQzJnZ0ZzS3hIRWFqZ0xmR2hjUW5tQkFpSk1BQ2RaRGFsNEoxcFo4TDhKY0xQakZtc0tTUkRscnZvMmNLelQ1SWVHeUhENWVoc1BqRVNDempubWFRbDlJVyt5Q2daZ3Y5cTYwcXUzVGszTWs4angiLCJtYWMiOiI0MWQ3OGIzNTBkY2NlZDRiMDY5YzA5MTViODUxOGMwMzc4MTRkZDZkNjk4ODQwNGUxNGJhY2RjOGM2MTZmOTI5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImtiQkhaeGt3MTdVa1VFVHR4YVZGcnc9PSIsInZhbHVlIjoiVndjTmZNclk5dnA2VHpXMW91MjUwTFpueTl3Z0ZzaVh0MjJwd2dwV2Y5Vi80MVJndDVOcXRWYkJDRnB3TmpVcU4xL1QrRnppTnJjMUJORDFhR29FRWNranNwdjczQ0laUUoxYzFxRURFUXRwMXEzUWFRRkxMOTFjTElnQkNNVFUiLCJtYWMiOiJkODNjNjczOWNiOTdkNWE5MTYxY2ViODJlYjA3M2MwOTkzODIxN2NjYTNjMWNiNDA5OTNkZTNjY2I5OWZiZWE4IiwidGFnIjoiIn0%3D",
}

