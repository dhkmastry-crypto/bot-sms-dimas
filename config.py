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
    "cf_clearance": "BpcUX652y2axxxKepozvCYFT5WPbdC8HcW34oioh7Hs-1792069147-1.2.1.1-nFUlzUhjzRHT0uaKZMo3c._X0J093qEp1Ex9ddYtLk0L8dUjn351Iw7YLADO59lK6st8gWrI0wh0eUt8GZZwGYKTq8noJOgCAyejhF3KFWKZXKb0cvgCHwLW3rWhsXEVDgmlgakK7J5JFFgv1TRs7UjrYUjuwPMrZosbrXMddovlIVNeR4wFqNVXyZi9UNQ4DQN3GySTTGorlxJlwL_gm3VkO22prdOiw3BFL5psO_FdQRzoLnG5asIM3D5RfHwI_5qyiLwRop4AWEviKkrZepW.Fhvyfyn1Ebi0e7N_i6nlixzAc_.1P5jr0jwm1xiy4GwuHQRnW.WTMIdsE_Efs.EXg07QlokP7WE3eOujdkv5OiIgh.qiOXUww3xZIaT3bIl6g4Ystmk1YgRAlRQL_jc69Nk_U.752zPEmP6NC8kV5xZpOA5PBh.Tygj9DYTBAMOSMNJKER5QlEQ81ieMCkR8eMi7p2i0BpOmIqEWX6pgFi9kz3BrUpXP1IGE5JX_FpqudTwKffRMW8S6hxEKTg",
    "XSRF-TOKEN": "eyJpdiI6ImkraWJIbHVVWHE1eFMzVy9SOVBHQ0E9PSIsInZhbHVlIjoibkdQRHlBck1Cb3RMa09nOXV1OXhSbjNnQUpJZmpjUlhyRkI5eEhJczIvMkNhMVBQdHA2VmdLMnFsa2ZBbU5wVks5UzhhY3lTTG1jM1BYMDJERWdrdWd3OHhBZ09PYnJPS0tZbVR4N3NrVGV0ZDk4RGE1d2tOMHBNUmV1YkU5NjAiLCJtYWMiOiJjNzhiMjQ0ZDY3NjRjOWRiMmQwMmJlMjMzODc1OTNiM2U2NTNlZTNhODM3NjViNDg4NTk1ZGZmYjY0ZjZiNmJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImhzQllXSStGemE2U2k5U3FFT2lYYlE9PSIsInZhbHVlIjoiTzdQSEtKbUg1aUJOd1ExTjBzS2pJM3hUUVV5U2ZOd1kwVHZMejZvVHJWU2lMNnhtYkhWZEhBN2NIbWo5Q1NibkF1TkhNWFQzY1V0dk5rOVM0RHNFcUZCNjRWNlBhK3hTTWhQTmRWaUpPeEliWTQ1TGQ0Qm1haWxWc0dOZ3FEaTgiLCJtYWMiOiI3OWUwOWYwMGNhZDQ5N2RiODU4MjdjMDEyMDk0YTU0M2MxNjI4NDI3ZTU1NGQxY2E3ODM4NDc4Y2ZiMmI4ODE1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "KH.0gQ4jJYkHICPLIgprDFtx5k_lv_hDUT9B8T_vyz0-1792069105-1.2.1.1-Xswy3sVteR6cBxtYnKQv8jUh_IIqcFKBLGHdjXeXF2FoBnrT6B4lMD0LayltY4Z4.TllDPR1POdtGzA5ODeCIIQAhUkxZ9qnIfiUaq1rD5xmLOiaWdf5hD4op6h9g5m_FiWo3JAR6z31JpEDVB3cAMSwkPlDSPXmgTrv9LlWk0cSgQ4c5DPsvrIhUUrU9Kw9eQPJClSReYEB6c2TksBpDxxqJt5qQDKp088Ei2_g1_bVDo3eJT7DIEI.Tbq7pqur6yKVzjM2wrRgAblmjGxwxHrKpx5yqIQ8E1nYCVFqB.8MgOZIn2t6BKb.4JGK6FCn5VRPeHJhZVgacFuxT7ObGOH4L7cGNes_.hbDwj1SzOXyg62b5sfGqYmBo3JXsWpRMYAzhZnS.Gv.ElHWq5bzd6eMZXxtscOfnGJLZmN2cejvKvbmbjdBpcvOrYB33r5WhiB64l9txiA2AFC04MH9UYbK.n2Lfj.k8lV46ErxTbB0VchNgREHTEhjnZLm7oKYrVEoG69qx9Uu7ObyT3i5hg",
    "XSRF-TOKEN": "eyJpdiI6InprVGsyUVE4dkMycXZCMWxEN25LUHc9PSIsInZhbHVlIjoidVNZekVJWTFiYWxidjl0Q3ZPMlRPNGhwWm1jU1lSWk5Jc3AvUWdNaUpHTis1YXhlUnRUZEQ3MFJyVFJZQ0l2b3RTTnY1Y2l4ZkpxMzlCL1ZhNkcwTWpaaU5wZlhqWkhpRW50MEZqNjAzcTZBRm0zMlUzc0EwZTBFVXMzNHBoc2oiLCJtYWMiOiJkYzYyNzE3MzE5N2I1ODc1MTU5NjIxYjI5NTU4NjYyZTliNzc5OTA4YTVhYzZlMDJjOTAwMDhhOTZkOGNjZTk3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlQxL0RJM2hONVFGenBoSzRDelhJQnc9PSIsInZhbHVlIjoiV0g5bnZVaHpIeW1HYUFHajM1US82VG1VcERYVzdBdk0yY1VEV0tmQWJaTHgrVGVxMGFuVFV3UUduV2haQ0pZcWo1cFYrejRxemJDUHY2ZHFOVGxGdjBaOGN3QitQdnBmcHdNdkdDUmlRYjlCMGY1czBQREcvM2JYREdWNDlQdkIiLCJtYWMiOiJmMTJhZjgwODUwMGM2ZjFhYzE1NGVlODM5Nzk5MmZmNDFiNGRlZTQ0ZTI1OWZjMWI1YzIyMDY2Y2RjMjk1YzVmIiwidGFnIjoiIn0%3D",
}

