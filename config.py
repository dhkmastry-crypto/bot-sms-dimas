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
    "cf_clearance": "ui7j14QrAAvsr7JrTRz4B7YyvMkn2mz6AlQI7WLUtws-1791894565-1.2.1.1-QftwJ_YuGUIi41ljaWjQdlgcfhi0mLj66uhFMI5lNN68ydHKJ4C.bD_tn.yCeo7O3iIbMMeca308tngKgNg6zR6bToV4MAWbPh6WHYlnmVo6stgeKzOx6XuIHo46XL_BiNZNmnc56H8Xh2tycHJmW02V0HapCPhj3CMnR_Jg13hdAoC8Rt0_N6nkHKwLtq2VG5sW1UOhEUlWGTvPPCXonK9Rnn9eOt_ARRKFgt4IIAYyr9acY8N.kyETl82GfCgCr3qdZSt.dlqKC5kRrZtJXDqiVBjHBGsuVuD4A97vXCH1tvFpJXjmukjJRBWwnD4O59_2SVd5P8F.TIZjZryyM4hy4lsZ4kmmonZTSbx9FNPbOaZW_McvPWCjETpqWGraq_wqtamPQfnFQha9YeePoCBwq1wul9po55lWxwcZbgozeWFWarwhMTE74uAL3LBNjD4YBYFkDcrcYsMVLs0yp3Wsmyfyla_mykOXHgTxJM5.NIr9DmtxK0RM6q5vLHkCQF2_lf8cms1jagBQhaT9BA",
    "XSRF-TOKEN": "eyJpdiI6IkJXdVZFQWhvQm5aSU1id2htMlZrZ0E9PSIsInZhbHVlIjoiNWpleU9CaDZuYVN6eEFod1Q1aTUxeDRLbWJZTzhFVGt3R2k3WWplakxtN0pyRERSN3VCS0hsRWYxM05lNFpmRjdvdFpoaGNaSG5hMUxFWmIwNDlsYmFMeWJXN2lvYnptbnNtKzBzblJPR3lzeS8xNWVoTXBpaEhpOXQ1YjBmczgiLCJtYWMiOiIxOWJlYzQxMDE2ODZiMTJiMTU4NjIxNjE4MTgxZWQ0NGEwMjlmYjllNDM0MWFjNTM3ZWIxZjBmY2NhZmM3YmRjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkpCMVNFazVNZ3dzNC9zZHh0MjExN0E9PSIsInZhbHVlIjoiV2huUzhNL1JmTml6WkdqZDI1bmZqcVN0Q3BFaHEyQlAxalVnYk9CSDl0NDBDaE1kUGZ1d0tSaE95UUNNL0h4Rk1zM3NYeENVOTZTdE15ZzR0NUkyRGhsaDFrVTVYWVFNNUE5SmUwN1crN1BVRXpvbGI0TUZRTG1OQmpEM1UraUUiLCJtYWMiOiI0YmUxM2U4MmRlZDA5ODdiMTFmOGY3NDIzMzEyYjNkZDU0ZTU2NGZiNjY2YzQ2MjcyYjEyZWM3NzI1YjVjMGZiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "RUJ.Rrg8liM3.p1yGe3HRAYt4FfA42S6epxs9ARHAJo-1791893943-1.2.1.1-s36zlcaqsJN9CXWNJ7Yv2JGGdc59sBVWZMZPNpDu05XQYZhOnCRBwPH5TGF1MKeICb554S4m9P8SUh4aYLeVyyoD9GFtCmXpa6JOiaoX03VoyCPrFp2xf_aybiSXY4uzZ8mtD7NsgZ09WbjRTX1XaLVFY2bSdMkaANzHRuUdO7dijAoMkvZ3UvFPsEyDWBCmsxfhjT62Q2zZ4b.B2Q5zFWbkGTo3PkAJx73Y9eHqBn7VuRoB71Sw3ZMIeDXdygC7m0GcjCbhalGgCM42ilYhDEiqEtecocCTRJYMDGxdiRg3FpTBhNFPnrwC9s1RNmR9pB1S53yUgILRCBD_5U.DaUOmY_rnjzVIVbk1inMz6rgb7mYX5mONjqGc0h3Gk2QpJkNi4gvaCo.WJwcA5YgJEwI3PS6tH6P8KEzet9Edsca2KH8urTUxh6aykaIuKecGDfvx3dZ35u.PGYVj379XZBwBEtHAE6rd40K0k2uDfHAdc3y1y9jkAhByc4QutSdycMdAlMRsXOTS0UTJlcdlCA",
    "XSRF-TOKEN": "eyJpdiI6IkJnSW5ncmhzSEdDY3JFZjBTVkRvS3c9PSIsInZhbHVlIjoiVGFCSkluemREb1NBcE1ybVNJV3VaQmZadldZMjhOaVBEK2xOamxHOEJ2MWpqaVVIQWlhekNnd3RCNzZiaHR2bmUySHBpVWp3UFZGdWQxTUN1dHZWMEZkMHlOYnlYZFRicFg1czAyWUdMV1ZDaTFEMFNFSTNvSEZjY2Vkbi9UOGciLCJtYWMiOiIxNThlZjkyMzJjZDBmODM3ZTBiMTNkZmY5ZDVkMmE4NmZhMTBhZThjODc4NTAwNDhkYzkzM2MwN2MzY2Y5MzE1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVpSVR1NkpFUGtFL3p2NExCaXNzZkE9PSIsInZhbHVlIjoibTVDcGRGNWwrUGZEamN1bUF5ZzRabEs5Zmw5M0tJb2ppaVRHcW1QRDNCNWVDZ2x2QWJkZEdqdmNGRnc5dGp4UU83ZHA2VjdndncrdzZkOGh3T1d6NmcxQkhlN3VjSVJvY0QzTWcrbEdMdzZ0ckpYdnI0bkxnVHNZSUVBc3lEYkkiLCJtYWMiOiJlN2NmYWFjMjY0MWJhNmQ4ZTBhYTFkZTg1Mzk4Zjk4NzAwMGFmOTEyMmY1MjQ0ZjEwY2JhOWE4NDhmYzRmMzBmIiwidGFnIjoiIn0%3D",
}

