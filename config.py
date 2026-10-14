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
    "cf_clearance": "2JmD8aR_zTwbLC2WmoGJOfDnRj59zPqFXognUO9af6g-1791947568-1.2.1.1-sIeIPp3cLnd69pte.dJJsnB6E3ia7LizcX03Y.NA_Pvgym98BpBJLBI_AgnFQ2Ho0hTkMDttYgX5P2hygSgGdhmnetbmn8O7vCnlytYw.WROmR9aISRJ1o4t7KfWne4tGlrhZIbCTOAhbUNAQTdjhcLn75Vc3zTE4x1GgZBic9WAPkdHx7nNxhr_LQyYsoTUTxUe8zVuJ4DlGFgd277SwJ7ZNzliX5YtXGvJaMO1JAOl9YhZDL3XFtZjtECsuXk0JDhk87uzLdaAvfrEM2qLEDIb.LWrCZDOUgdFiwjc_3RQrnjVXNtG4wwgMWnhlCzyKXAJrVl55nNQ0UnQGIxpVEvK8D.3nAXlpunJPg7boNNg1BmLE0YSZDagi2nmRWGOKZjsDj5.N_EHEDQT9pZ.ZktV3tl4GDhrKbZdWdAEczAZ.d6ck8eYsLp7N9w3hXX0_frzzVrX_NYGuYsHog5FPV.hYah0ylH0oaYADje7IcdWLRaCm_c8oj_Zz01R4aFzPJ5nNvCr6q.tVbtzDeSAvA",
    "XSRF-TOKEN": "eyJpdiI6InBiSktkTE91QmJIdjBpcEpVOGppQ3c9PSIsInZhbHVlIjoiWUFBdEFyYVoweDd4VkZLZzRhbWIrMGJ6ZVVMZFd4bHA1WUVmR1JIRjhrQTJremt4Ukord1ZnTWR1c2JtanFsaXF1bHZVLzJLZzZ2alVOTlBHUDBTSVR5cXREbTUwait1cUdkNjd6OEphdzZCZWhjWHVmZnRGbTZ5bFM4Y1JON0siLCJtYWMiOiIxY2ZjYzk0YWQ4YmU5Yjk3Y2I5ZTJhYTI2YjEzYTFhNzc1ODA4ODNlMmFiOWM2MGIwY2UzOTM1YTIzNmY2YTFmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjlRRTRMU2NoenU1WUFpSGhjU0FhTUE9PSIsInZhbHVlIjoiMS9VemtNT01GZTJoakNCWE81Z2EwbnF3L1NWMzVVcm5jN1RBZHp0Y21BUjJTNVZmUVdaOXc3Z3RnRGZmSTFMZGpwK1A3Wmo1dmk0RDVsbDhpRFV4ZHY0SU1LOUlHTDdGWnRIN1gwOExhNE1YOXpGWHBKdmJnSnlmdCtGODkzRXIiLCJtYWMiOiJjOThlNTE4ZGRhMDY1NjBkYmMwNTM2NTY0MGU4ZDI4MzNjMzZmNmYxZWUxNjdlYTYzN2M2YzhjNDAwZjQ3MmNlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "JhwJ_SsdBOPlBl4BLClM86Q9D4zwshd73re5TBIqTCM-1791945842-1.2.1.1-kAia14Mo3Q7Re.VZjQnJGtKbWfD7C4tao8gA3MbuCEiXgqtDK3B_iPwm.9XVdno2P2ECPpMvgwPuor5yJvJWMf3rQlYgSv07zsqaraksmwd1tXbR7nBEnQPsqVeZr9FiZOOLS8ZsO.bVhtLGohqG3QAYl90jfv0B17XrThcyRuKOsVvBUnVi_4iMnpx5gBP0yo_MYbhuKnnyzL7TmM0fZzMCf6c1AQ3nCenW426QB6TGPTWPZ4MOrzjZaoZZMxKUldbE.4JeET8VToSAUFhrZ1AJrqtC4c3dBSvqdVU3Elwku4BpdbCvlB79lCZPsFeMLqSqvQmRyGpY08ZzgLnboXqp..xxIxxWgxYayX9_WyC2Op2T7tpcPu9LZUZy3ccE2BvGIM6vxHNfZFBS6O8oiw5ljGUaKQzFTQpGnGpBAqu9uDIlbH2D2.FkXF_sL5GhLwWSg_0NdO2Tz2dwAQhJCrgREo_YRXpA8KMaKwEikU4iT9WZB2ETlQVbpwjEImpgjnTXfLKNKkExZWrvejkfqQ",
    "XSRF-TOKEN": "eyJpdiI6IkRlWGpVNXI4M3dncDhvNVlkamZyeUE9PSIsInZhbHVlIjoiaTd3YWJpazV1cjF1QkhuZXlLaVJLdWFXclA5N1c1WVpLcGpYcndTMHFNdVpDRDNPUkpTSlZzL2FIL0ZIY0RNR0g5QVlEY01tTVVFTUlXMHZacmtJNFg4Q0pmTTBYdkpaaEJYMEM4UGVYTForaDRpTlNKYytMRkJDTHhCL01IZG0iLCJtYWMiOiJkNjQ4MmVmMjdlNGVlZGQ0ZTdkMGM0MGQ0Y2RhMzhmNDRjNzE2ZGFkMmY2Nzg5ZjVhMDJlMzIzMWY1NzdhODc4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZpY1Jsb2thUmFVbS81K04yYnpGVmc9PSIsInZhbHVlIjoiSGdGNGFhT1RtUVdMOU9NaUVOMlZxRmY0czJTemhvd2JPRmE3TThBeGpsUjMzdTBLZ1FjQTNWUE4zS3NlYVNNVzdicW1EUGxCMEdkeXVJVHRmVXBtb1AvVUpKWXNuZ0YrbWtSVWFVSCtxNjF1Z3ZldTRGZDVibkJJU1QzenhSa2UiLCJtYWMiOiJkMTRhMGVkNTgxMTY1ZDQ4MjdlYjQ0Y2I2YzMzMzc2Mzc2MDY4MzQ4YzE5ODYxZTIwMmY1NWRiMTU2ZDAzZTc4IiwidGFnIjoiIn0%3D",
}

