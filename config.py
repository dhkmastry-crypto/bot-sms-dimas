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
    "cf_clearance": "slkmZP.AgPBjwomweoK11S7ivHxXkLFaDNnzXCYjtRA-1792099955-1.2.1.1-SK74lxECMLiul88.WnbVqg2voRffnW5HwjfOwnm0N_l0f7pUnxkK32wbw0JFn8yKBKVL4NSyE4HP2mgPtrf3yCCoGYaUNXEncBSpZHAQ8azXrbhG.8qNQhLXjQZgCgD.mvLKUadWhsQnPKc6eLfyKFpbawIQ7nKxCMfyU9tYnC6.N5x5oUIXWT6y2HF_85_bKDkKQ8cbJozgNUjPt.WxNCGnXWmopbHyxghgP2NJF91caC0aVSH7klTBQX39DE6Fe2m5SiClQDcPU9hLxMNfgIZ4y9kzmL6t84DNdveQrKfQk4WDTQ.sb3duk1lDg0R1ajuDCGkpm0NSRmmmVdRNu4aRRFBfs98G06HxWl_PrqEoNGDs.wM7U0FRtiehokPWb9Jia_RnuMUDrFUq5a6N495vYAX0G6Ln6nkxIz32VByz3HmaUoXrLXLLTZS0F3BfwTRcvcwQEh9pGj.HBEseioXmTIxNP4.T7Q3VX2FqQ12hiycRXn8.Dm1X5WP132zWRxbaGho8qU_Hf2KAaaoVOg",
    "XSRF-TOKEN": "eyJpdiI6IjJwdEpxSmRVQW1BSWRPUk4zbW9rTlE9PSIsInZhbHVlIjoieVVtUWRET2QzK2JSSmt0Z3lYdXRqZ2w2eWJMSm1jN09mM012OCtGbFFYMFFjbFloczVaU0RPb2FXb3VMcUlOaUdZZlNnQUwxbTVGSWxlekVRcG1QZlZPbFFBVUViSXZSRlcrbEVxSU5MdUcrRHVJRlVvZ1B0ZUlvNXdpbDJwbmYiLCJtYWMiOiI3ZDdhMTU0MzMyNThhYWMxYTJkZTUzOGFjZjZlYWMzMzIzZjExYzZiYmYwOTQxMWU1MDZhNTYyNGQ0NWI3OWM2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InlESS9pSWdtcUNBdjlmaHVNcWpZNkE9PSIsInZhbHVlIjoiU0lYMnZsZ2RZcldRcS9VVGk0ak5TY3ZLK08xVkVaeE5UQkF2RXlYdzZQZmRXWUZQUEJmMGFWSkFERVlMbENEazdpbmtnWEJhSmg4a1JwM3ByQmhsOXdTN09TU1Yrcllwb3pjcDBWR3ZPbTVpaVJHNGNMVnYxTnFvVDF2TjkvVVIiLCJtYWMiOiI5Y2UzZWM1OTRkMWFlYWFiNmRjZWFmN2NlNmVhYjhkMDQ5ZTgzODEzZjIyYTllODVmYmMyNDEzNTA2YWFhNDVkIiwidGFnIjoiIn0%3D",
}

