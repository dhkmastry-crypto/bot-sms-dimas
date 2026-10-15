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
    "cf_clearance": "68b_mtpAA6tOa1vlJJSGd1qtVqaSfCr1AVbInnILjUU-1792081793-1.2.1.1-KzdTRsGH.JdUBKTvX6FoGc7e7tr8zyRhPNtciBR.CfiOuoB5JJOrfKKhoHz_wWd9HC0dYvjOlZ4h7uydCIyZSvU8mUqjmbNcwDui2fG1CP8qSiv9QS3cwUIZmbzaK7lmQwL14ySXTQyHfdtSErarMJUJByEMpcUabuBL5Jx4tjNkpcZNufGH4Dzs2WJoOCQSoTx8PlFq3PkwSL141ACCCASSqAi169Tq7Sd4ifcFCtmzu.6W2784oOt7CR9ZqgMrikUGPy8CaT7DIKTZtdWQOdeqQROf.nOWTH8vgnAO.XVyEmgMDVA4p.EKMvpBLn6o8twmCZZNTN.w6PlyxKf_6GmDCeDfZWIZ5rxmvyKqlOq3TUmSxtbMDPiY2zfIqKRAxTCPjgeKfMlD06AvlEgH6WZ3943l5hD25bFQJXuh04WMgDfGCU7arunu0kuuM.3iUQp5sCAWcjNFvF6Msl6vRqyiRafUpWRoRheZgoyAzkovXnNiJqMbqIHBIAQKrp3tDJKU32qoN3lVHAoLHBWDpw",
    "XSRF-TOKEN": "eyJpdiI6ImMwd1NCc0lWYmE2UFRLSnl1V1MyN1E9PSIsInZhbHVlIjoiSkhVby9UOUdKSkVSc2VOKytqa0ZhL2F6THJhYng2ZHJlby9MaEdES2REb1lTb1MyVExJbkR5dFRZNUYxR0JSZGZqSWZFa0g3bWlJLzhtQlAxRFFqekFoUkRIK0dhMVQrQVl5cU5nOS9mY1Z3UkZidW5xNEJDZlhaM0czbGh1bloiLCJtYWMiOiIyZDZiMGY0NTgxODhkYjU2ZTA1NjQxYjdjMmE0YjMxYTU0NjNmMWI3OTA3Mzk0MTg1NTZjZDg3NTQwZTM1OTczIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9VbkV3ZURSdE1ZRnp0SHYxZ25XbEE9PSIsInZhbHVlIjoiQkVWVkY0Rkl3RXp6TjlCZG5TV2NhTmFhTVZCSHFjZENoRDBueGE3K1lscVNyc29Rdm1WRkIydlE3ZjFZc2J3NHZhazRwdFBmWGM1TTRabVdZUUJwUDRvZ0VmZUU1ZVNFVndwT3RSTHZ6cmFHdmVLYjZhc09ZM1NZVDJScUZDMy8iLCJtYWMiOiIzNjFmN2M1MTI1OWE4NDU5N2JlY2MyMWFhOTI0YTM1NDA1OTZjMDU3Y2VhOWQ1YmY4ODc0YTY5YmY4ZmVhZmI1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "vL5xTxFkSjNB43I.zbJcrCJHxmbcLXO11dgSqwXoCRo-1792083565-1.2.1.1-lz2qMiTdX5ValqH7j19jEHFMwCX..Lj1zfaAiS_sncQOCw2YaK01_OY4YOOt4jF2IR5q_.nZR_b.BjPVLQzbb6EW.3YVYQ8Ts4uxkTx9njhze3S9igwhpONLlh2sWtAPvvYTNdSdm9uhyjc4WyRnbm3CrBiDwh22szSQMYMuxd_._ibEwJ75olKDoiFFFyCMGmTPpoB9zNcr7dkcF97e.9g6_M2Xyq5BMAfq0EC0lwAWx1kGIcHOsjTKRFoL_edB2k1ct9wQJ6s1mvcnakW_wkiXB6eFl06SCaPd3aWhc1FE_NPX2ZtQ9gYlWvr0VM47ND1hrd_KrNcJIfpI759GwxbJkUdmiRr5XI5JKx83v1Cw2juxkOG124jvtlc4emd6KUV8mHFohaPR1F7TWUR.5wlwtbEpvJ0p2q4yQXizdDsmfcxScX_VXrZr5iTAVxLMaaXvSpl3QsX_XcIdec83MLmBJyt2N1UlgOAYR2IfyekvthLydDf25LcjMw0l2DO7_Pm8OE292kRK.8DYpZrZbQ",
    "XSRF-TOKEN": "eyJpdiI6IlI2SFYvYTNMZmQzM3h5YTBFc29KOXc9PSIsInZhbHVlIjoiQ213TUk5MDlob3ErZzhVQUlmQ1BrK2lFZVNKUWZCY0JTNVdvSWs2YTIwZ3hRNmU5SmhEMVFsNHh2ZDNnSjBaUGpRZ3lCeUt1ZnVydVdqWElTd0xhUTNhbXNyTU0vb0FnNFJkNTcxNDFsWERmZGFnZFN6MVJCYVg0T0puQVNWTlQiLCJtYWMiOiI4MGFmMzRlYWMxYzI0NDY1NzE3NzhjMmU4ODMxNTI2NGE1YmYxNGFlY2NhYzc2OWU3NzY0ZjIwOWNiYTZjMDJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ikw4V0dtOXgvR3ZCT3B5QUFaUTAvdEE9PSIsInZhbHVlIjoiR21kd0RrSmhlaFJ3ZzNPc0ZOV0tJRTc5N3Q4WkNRY2Q2OU1JMG11cjQwSFh6aUp6Uk16Y0ZJKy9DaEc1VW1zdHRWYUFBUWtsRDJJQkI1aTEzbURMQWs4SGd5WEhndk1VMlhKMk5MbFB0MVN0YndCQ1NFTkN3OTBDeXFOR0o1SEsiLCJtYWMiOiIxMzcyNmI2NWEyYTIyM2UzY2IxYTYyYjFlMjFlMGE5MDQ0ZjZiMDU4Y2RmMzJkNzM1NGIwMzQ2NmI3MzA4NmQxIiwidGFnIjoiIn0%3D",
}

