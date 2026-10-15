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
    "cf_clearance": "MhS46YmpW2dmBSAv7CiWNV56aAo4iELHmSYt9udAH2s-1792099913-1.2.1.1-ddnnwrA0ohiijhiRCujhuBN80lU5FahWunxnr0gNppz8fq6KBB11_TqV7ACc1W1kgdF34VnE2.5j4ivY0x4IlQVRoAOCEqm5uaQHEc.gf8HKefNPBKCCXbRTlZCnwy3CAoPLqFTMe5HBrCB3N0CW3CC.F7y2nNIARlSaFc7s8.LNQqeAvwE.sI1pPfYq_zD0.JRWSYo3hkvZbCvwVveMNsMQ5FAF_6fqgXnshNi31oxZnxIEAa6SGvWquDfYDWBr5smIYVg7HJygQyzMs_N3JQA0sAZyYXxY_nPJd3S7i4gVhe.KUMa998R.a8jT6tZne_V6iFG42ZM.BBhobiO8BzOLwK3VIKX18l9xaVDh1MEWNlUve9EIj8GrExUPZJmQwsLx7CAvRZQ0E2AuFRy4nlEcPzfGXDyLCF.gzTxTP9aoXf5r_jKfZ2ieLVX.Mg0tn5YyzBNP3cJ7qXnzzP7GcEi.MEtcSbacxFpZ9y75M0jKFPXwmm.mqMAiX5FCMOh4tuD9ZujHDRpIEkw8GUyA1g",
    "XSRF-TOKEN": "eyJpdiI6InVkVGQyZXhIR1pXRFEva2cyeWUzMHc9PSIsInZhbHVlIjoiYlNjTHIzTUF5Ni9McjJFNVFsTE56eTFTakZYemg3NGhFcUltRkxSWGVvWEMra3JxTG1aTndjcmV2TXU1dk1QRERzNDhJRDdCcHBKVy9yb3lDZHlaMHFrU1g0ZlVlR2JaUjI1Y3Fkb1VONzBBYWdBeEZXMlZLdk5McmpmdVhEUnQiLCJtYWMiOiIxYjdhZTA4YjA5ODBmYTBjODUxYzgzMTA5YzE3MjAyM2FhMTliNzg3YmZmZGJlNTkxMTRmZTY4NTE0MDY4MzViIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik1ydU9ZSksvREgxOTZQZjhWeGtpeGc9PSIsInZhbHVlIjoiNWRNN0ZjTkhhUkNpVVJzMzdYc2tTbTFCWkJCOGh4YmVvRTNkamFjVnpJM003S2VSUVBSMytjZk0rUW9VelA4RWVFNFFTanU2NDVQNUpBYnFpUW82MUgzQmpKN3F4MWZwKy9aa3dUbDdjNklIdEp4eXZFOXRLVnNZcE9uZnJSOTMiLCJtYWMiOiI2MjAzN2Q1MjQyNDk3ODdkNjA4NWRiMDUxZDFkZjg3MWVkMjZlZTE2MGRmM2ViNjkwZGRmNzc0MjMxYzJiNGE1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "r3UM6MsD2A2DiRqzlSm1krWnKaPmKnG0a_4aWALRPRo-1792098102-1.2.1.1-kG2otxeaikDTztlx52aRYk8.z68IUqEfP.jPMYtYEpF0tbh1S6yCUDNOilP5pn1Wkiv_yb4RlOGUB9RPPu3lVzFMidw3OCLNuokflgkWVTw7ubwrVcoFyWRoHZJP61xZHtwQoYrNjT6CqYDkMoMbV09PMu41zXx9CIZ5PJBDM51TMzcBpnEPySdlN8lpYbJjUxuHFfYIFlABhJjsGcC0w1QMoREbH1FqSvmfEK2LN8PRP84xSzm__XO_h3SmjkSN8mbw4ZcWKbu.dGYfL8c_uu04S8LookwPodXJhaUzm9YoNVEXeFCbASzHaNchv5DURDM9ADMgeAinGZosia.M0pj30AC0nnhlv12sxF3UR0Qdu.hJyHeM7UiSW1vChvVKyzGKdbO1tk88pE02JAVTfwYZdpNo_dC_prnysTtYggmbcUUpuweU6lxqPAd1MeBdQxlnmuZkXC26f00bKw20ENfM4vONIghdc2fX720ij8Idrb11n2JLiEsBjXqkbmgqa1L0tpE2qejO7GphF5gyYA",
    "XSRF-TOKEN": "eyJpdiI6IjQ4RTNTQWJGYUVDa0ZVcXZJZjNLOGc9PSIsInZhbHVlIjoiMmw0b01zWG9vY01Rb215WkJpV0RSSnRwNE9UaTl6Mm9yL0dUYlIvbGVhQVZ6S251SGEwa1F6MnEzNlY3Z2YrWGZnR3VFWVVxdEhndUlMZVVHUW5xamFYNzc5bFJYSEp1L2FGNUp1TG9pRmFNVElhck52c00wY2lwaW91Tk5wZzAiLCJtYWMiOiIzYWRmZmQ1MDIxZjQzYThmNmQxZmJiMTZmNjEwOWRjNWJhMTEzYTg1ZDlkNWNkNzM2ZWM4Y2U0MzAyMTc0ZmMxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVpbzZ1cHNDeG9FMTVXdG9WVjd0Qnc9PSIsInZhbHVlIjoiV0ZtTEhjOFkyRjc2N0pUempuR2RnZHNZU3BMWWVudXhKS2xQSzV4UlhGVkNXRENNa0R0YU5sa0RHSlJJVUxFc0FVTVEzT0JOSWFtTFdxTkFUbCtTaGMzNzQ5TUdiZ2NZdTlBYWcvTXNkd0JEN1dJSmtGY1ltZC81TzRYdzhlNDkiLCJtYWMiOiIwMzJiYjRkZDFiMTUxMWNhYzZmMmE2MmQzNzkzNTJjOGNjNzA4M2VmY2U0NzhkMmY3OGI5MTllNjBmOGU0YTc0IiwidGFnIjoiIn0%3D",
}

