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
    "cf_clearance": "lRm6KYVL0itsF.hAOlqkt_9MaIxRYJe5n58sgUdj.gA-1791945754-1.2.1.1-zIm3h_tpjT2RIwW1YPfzizVECO05P9uzVgFTkyXxOE6_MzQvldDwFD2rJkJ2PbR..HqC.rNummGQN_3EDcdZZ_eiSO7yagyZFhARhwTnc2VI.cV1QS.VYrS2OTGDtcRsenAR7gAQ6rn9a5pSHYcRDv2MQUB2.2cM.PujICrzNNjPN7uwotbLvlu..8smTkLDK4JnZTWB7jFX899yIUDkzDEI7Dm.OGRH.FA3V5WuzCtfLqpaHoD3zslnS0ZpI2wlic1J5LtEGKuVmmb9WahTSPS5Wu3OWb4Vx2.nOts_V6dA1Z1BUo7Lba5pHs_LZ1ILrSQk1v7D17uVavL65_HlQV2Qzsm_aSca_OtIO36_FXBkEiHeKAO3KR.bnb_6knfi1e2chp3h3KGs9so3jSvwQ7wAExoBGWHZrLujVpE21UZKaYAgJvVG2DlYIwHnyLYGzzw2fAf.rCAXlyH.KfUKEHi6d7LFeEAT4nJzIsc5Q4BWchMswFpHfed.0nIEbFLTJVMLcb7w33oO1mrGWt3JZA",
    "XSRF-TOKEN": "eyJpdiI6Imo3c1FYaTIwbENBcTgvUW5vMHk2bnc9PSIsInZhbHVlIjoiWFJOdDN5a1RVMUwzYVpjdzltU1N1a2Z4VENmd3k2ZXB0MjQySjBTd3RmMVN2d2ZzRUF5d3FPczRiYys4eFdEcTFqYjduL0pjUktIcUxxdEUxRjl2QnlFRURGbWJNRTZCMkwzN00vbWVETkRhZlpUb0szbkpKUFZTNlliNkxkbGgiLCJtYWMiOiI3MDM4YWRiN2U1OTMxNjViODlkYzJhNWIxNzA0OTA1ZTk5ZTNkMzNlZmVjODczM2YwNzI4YzEzYTM2ZWI4MzJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFpc1k4ekZ6Wkx3YUZkbnduVmVhQkE9PSIsInZhbHVlIjoiZGFvTXdDOWlNSmdET2sxSXh0a1VKRzVSaWoxb2VDRzNyd05ITE1KU0Fqa2UwekNCNjBQNDg5M0xRYTFGU0FaQW15RGxuVWxoSTg1N3NHYUhyNlVNOUNUcFV6cnl2M3k5QmRCY3JUQU8vR29KZ2NrNFMvczY3eWlleDRuY2ZUWkciLCJtYWMiOiI3NDZlMzBlNmZhMGI0ZmNhYzM2YjJkODExYmViNDNhZjBiZjhjYTZhMTc1ODU2YWZlZDU1M2JiZjAzNjAzNDI4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "UXREhT0qfteZvnliie84oFaprMBoENZuB0B_OeiA6J8-1791944033-1.2.1.1-Xlt5EZcM2vWWpExo_vyaK1dwdtausTnRErbL8AAUioeYKv5YuoCszXMMOCWLfy.Xc1MNNjZqXMyYiPjozU4jFfVXvhrIONJ2n7hWS5FGtuazsRlicohuQwJmVbHeXcRPYbFCL7RKzTx3Nhv5V1x4gJzyFzIkmOEmIiw8Y3BQ5vzjo2RFTD5SQNj3aX1y4K28A4a0GCdpj6GApV3k4o1ozRLmAg2FmaB_8KULPcjuSjQmEffSpc.13TGKc5XUC2f64xFQ90jFHERKHCRTtDUQ7fiqXD0YqCKsBaWGxX7dFNLES5Yp9vSARFJjcs13MI3ZrzIms4JXC3fggli6ndfOt4RwymNBSO4eI0falZjcY6ENomoxctZLr2hkIoCnX.ILKO5Y41qe5TAT4OJdYa1VY08KPSpmX5tagnktoKmNXOMlM3vEY04sM_5tXNUq6qdfYz4IlzHtXYU3.gvqaPK79Yj8F5l6iulz47glZetdSaojg2uvuSKPBeVNmiXhFvoVFCWxKINglF5ojHOtCCtT2Q",
    "XSRF-TOKEN": "eyJpdiI6InFrTWhqYU12QW1YQVdJL1U2N0FUcmc9PSIsInZhbHVlIjoieFNZek1PZzJHTWRnUXNkVUxYa2dpMHVFQVBDOFZiRk11bVRCYXFTQVRmUzU4TVdyMzlSMlVqWmNHTGpEREduT3RGYkU2YWl2SUdtU3hVc3VUVmwrbVdXVGducHpHaDBWMXo4bFhoZ0MxN2hONWVHRmRMYWRyZU1CbTgvcXhhYkMiLCJtYWMiOiIwMTA5NTA0ODQ1M2VjN2Q3MTNiZGRlZTcxOTI0ZjUwMjI0YzE5ZGQxYmEwMTMwYTFlMWI5MDljOWVjYzQzOTZiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjEzQVZGV0cySEkwMWN4eWVXQ3VPbWc9PSIsInZhbHVlIjoiakRGWTF6UlF1aG53dUdINUdFNytuZFZnVGZEUHRTK3RnS09UR2VINmQ4ZTZKcmVOdDN0MG5uSDc0cm9ZUjRRTVFFL0IwaUI5Vk1Kb0Y5U0FJUkViN3RzUnhVNjlCdk5OQ2owVXhLRFFneG9SQlFsQzhHUVhvZlpmM1B0MGpWbk0iLCJtYWMiOiJiN2I3OTY5YzUxNWU2YjNiYzkwYzcwY2NhOWM0ODViYWEyOWU5NWUwMjM0NzU4MTEzY2VjODE0NDU1NzkxZWU2IiwidGFnIjoiIn0%3D",
}

