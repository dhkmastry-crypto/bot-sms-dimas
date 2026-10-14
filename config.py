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
    "cf_clearance": "xxpJWW4Etgcnq22PtbgbGYtxRVRYH1ygX91B439Hwj4-1791943949-1.2.1.1-cLz6.KdPWwm9Q4oPay7ZX11gR7xXVBc9jyHejud742S5mx0STDqi4V.NejIr45ZSchuK5zscefAXHtDE.GprFiBCbzOKXtnICPDi7bmcZRlBbak1FSuygIZYUHlv9cKnvLxpLxqNYgbZwQ5YIr8Z1YMsx5zleFnPz.oTXIqtCybXgRK6CWBEArUXxKsWu4dPyMFdVHRLpzbqfo7Bxp9Pxf3EHgkfHPv_kDDbMBHDZoyMEeZpurrSTCnRsYmRWjsCz9o91XTwz9A42q4Tvry5.i14ziQNsboVrVzs9owIWsuIFkifEdJxlox2V0WTum0gKm8orW0SuEhhJXyBGUFbRKhuqTE7zZMxFzUKqa1vI_e.27jkqCpGSjHAPPVtrg5.1JZ6mg8.uLYvD_0SPjwNUlPy.wsvRWFDiplAn_TJxQG7Ch.T5LWf4tVk_m3WRFHz2D6UdcpWxgR7Z2C1vTk1ZQ_GmZiFjGe0flBX9tMFQPPWucuREzVHvLTSvH9JMojl_sGR5lUZt_VtpX1qufzUZw",
    "XSRF-TOKEN": "eyJpdiI6ImRCYzQ2dmtYZWZBSXFuV0d1dHRhZmc9PSIsInZhbHVlIjoiTDY1eEMrQlNzekgzaWg0aHFMZW43aGtidTZiRWpHR2lwVXFLUG1CVGJJQURxOGEzWGw0T1JzaTZyQUNOKytqaUJmb3BBTDdJOE5pOHg2cHIwVCszMmY3YmFvR3lMT05yRDFhV0YzNWFabFk4R0M5UHVVbHNrZXJQSmVnbWFscW8iLCJtYWMiOiI1NThmOTUzZTlmZDA3YWQ4NTA1YTZjZTQzMjlhZTllZTlkYzExNjBhNjQ3MDIwZTE0MzFkMzQyMmE4NzNkNjM1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJCNmF3QVVFTVR0V0VDdUJ1RW1uT1E9PSIsInZhbHVlIjoiYm1uVWxWK0M4NWh6WjliZ0hFc2VKZGxhVXMxYUFvODBucXhmQ3JFUmx0UDBuMzNJaThvVWlEMGdtR3VjN2pLTUNCZ2Y2MGR0c2pXOXQvZS9BZXpHUzFDQWZZemtEZ1E0Rnh2N25NbG9vRmdsSW5JY29obTMwVmZ2VTdkRUJHa3MiLCJtYWMiOiI4Y2U3YzhiNDFkOWVjZGY2NzJlODFhNjdkMTFjZDk3MmMzNTcxYTc4YjE4MmIzMDY4MDQ3MWY1YTkyYTI5ODI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "UXREhT0qfteZvnliie84oFaprMBoENZuB0B_OeiA6J8-1791944033-1.2.1.1-Xlt5EZcM2vWWpExo_vyaK1dwdtausTnRErbL8AAUioeYKv5YuoCszXMMOCWLfy.Xc1MNNjZqXMyYiPjozU4jFfVXvhrIONJ2n7hWS5FGtuazsRlicohuQwJmVbHeXcRPYbFCL7RKzTx3Nhv5V1x4gJzyFzIkmOEmIiw8Y3BQ5vzjo2RFTD5SQNj3aX1y4K28A4a0GCdpj6GApV3k4o1ozRLmAg2FmaB_8KULPcjuSjQmEffSpc.13TGKc5XUC2f64xFQ90jFHERKHCRTtDUQ7fiqXD0YqCKsBaWGxX7dFNLES5Yp9vSARFJjcs13MI3ZrzIms4JXC3fggli6ndfOt4RwymNBSO4eI0falZjcY6ENomoxctZLr2hkIoCnX.ILKO5Y41qe5TAT4OJdYa1VY08KPSpmX5tagnktoKmNXOMlM3vEY04sM_5tXNUq6qdfYz4IlzHtXYU3.gvqaPK79Yj8F5l6iulz47glZetdSaojg2uvuSKPBeVNmiXhFvoVFCWxKINglF5ojHOtCCtT2Q",
    "XSRF-TOKEN": "eyJpdiI6InFrTWhqYU12QW1YQVdJL1U2N0FUcmc9PSIsInZhbHVlIjoieFNZek1PZzJHTWRnUXNkVUxYa2dpMHVFQVBDOFZiRk11bVRCYXFTQVRmUzU4TVdyMzlSMlVqWmNHTGpEREduT3RGYkU2YWl2SUdtU3hVc3VUVmwrbVdXVGducHpHaDBWMXo4bFhoZ0MxN2hONWVHRmRMYWRyZU1CbTgvcXhhYkMiLCJtYWMiOiIwMTA5NTA0ODQ1M2VjN2Q3MTNiZGRlZTcxOTI0ZjUwMjI0YzE5ZGQxYmEwMTMwYTFlMWI5MDljOWVjYzQzOTZiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjEzQVZGV0cySEkwMWN4eWVXQ3VPbWc9PSIsInZhbHVlIjoiakRGWTF6UlF1aG53dUdINUdFNytuZFZnVGZEUHRTK3RnS09UR2VINmQ4ZTZKcmVOdDN0MG5uSDc0cm9ZUjRRTVFFL0IwaUI5Vk1Kb0Y5U0FJUkViN3RzUnhVNjlCdk5OQ2owVXhLRFFneG9SQlFsQzhHUVhvZlpmM1B0MGpWbk0iLCJtYWMiOiJiN2I3OTY5YzUxNWU2YjNiYzkwYzcwY2NhOWM0ODViYWEyOWU5NWUwMjM0NzU4MTEzY2VjODE0NDU1NzkxZWU2IiwidGFnIjoiIn0%3D",
}

