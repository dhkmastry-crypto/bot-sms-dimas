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
    "cf_clearance": "JhwJ_SsdBOPlBl4BLClM86Q9D4zwshd73re5TBIqTCM-1791945842-1.2.1.1-kAia14Mo3Q7Re.VZjQnJGtKbWfD7C4tao8gA3MbuCEiXgqtDK3B_iPwm.9XVdno2P2ECPpMvgwPuor5yJvJWMf3rQlYgSv07zsqaraksmwd1tXbR7nBEnQPsqVeZr9FiZOOLS8ZsO.bVhtLGohqG3QAYl90jfv0B17XrThcyRuKOsVvBUnVi_4iMnpx5gBP0yo_MYbhuKnnyzL7TmM0fZzMCf6c1AQ3nCenW426QB6TGPTWPZ4MOrzjZaoZZMxKUldbE.4JeET8VToSAUFhrZ1AJrqtC4c3dBSvqdVU3Elwku4BpdbCvlB79lCZPsFeMLqSqvQmRyGpY08ZzgLnboXqp..xxIxxWgxYayX9_WyC2Op2T7tpcPu9LZUZy3ccE2BvGIM6vxHNfZFBS6O8oiw5ljGUaKQzFTQpGnGpBAqu9uDIlbH2D2.FkXF_sL5GhLwWSg_0NdO2Tz2dwAQhJCrgREo_YRXpA8KMaKwEikU4iT9WZB2ETlQVbpwjEImpgjnTXfLKNKkExZWrvejkfqQ",
    "XSRF-TOKEN": "eyJpdiI6IkRlWGpVNXI4M3dncDhvNVlkamZyeUE9PSIsInZhbHVlIjoiaTd3YWJpazV1cjF1QkhuZXlLaVJLdWFXclA5N1c1WVpLcGpYcndTMHFNdVpDRDNPUkpTSlZzL2FIL0ZIY0RNR0g5QVlEY01tTVVFTUlXMHZacmtJNFg4Q0pmTTBYdkpaaEJYMEM4UGVYTForaDRpTlNKYytMRkJDTHhCL01IZG0iLCJtYWMiOiJkNjQ4MmVmMjdlNGVlZGQ0ZTdkMGM0MGQ0Y2RhMzhmNDRjNzE2ZGFkMmY2Nzg5ZjVhMDJlMzIzMWY1NzdhODc4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZpY1Jsb2thUmFVbS81K04yYnpGVmc9PSIsInZhbHVlIjoiSGdGNGFhT1RtUVdMOU9NaUVOMlZxRmY0czJTemhvd2JPRmE3TThBeGpsUjMzdTBLZ1FjQTNWUE4zS3NlYVNNVzdicW1EUGxCMEdkeXVJVHRmVXBtb1AvVUpKWXNuZ0YrbWtSVWFVSCtxNjF1Z3ZldTRGZDVibkJJU1QzenhSa2UiLCJtYWMiOiJkMTRhMGVkNTgxMTY1ZDQ4MjdlYjQ0Y2I2YzMzMzc2Mzc2MDY4MzQ4YzE5ODYxZTIwMmY1NWRiMTU2ZDAzZTc4IiwidGFnIjoiIn0%3D",
}

