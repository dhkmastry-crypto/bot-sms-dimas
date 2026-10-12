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
    "cf_clearance": "qdI2jI.ZGAk3Lto_EHtl5htjJBIrTZc4M.ICOhdKRdo-1791834878-1.2.1.1-ZUCBsJGRJBg2oNKCGPkOkfhj6ca0q_qHyqVVbI64MEA0EdRwt8gSsw4f45NppB4zleJoDMiR5an8BjYk5NiIhktmqdGXJi1juQmkR7czBGg7jvEoXN5Xk.6NGUy2ST0lt1kx5X0ge1yLKeNL7C851c7qJUdlmDpWjgwbO5nUEcqU.V3ySwjyZpSxhupsqXIN1gFSGlF4JepLiyfPHr068_wB9dFcFK1I_8mbixP5EZOZTz9jLx7NKTtlfqqQPvz22Ehu4MuYZkIaaa6YaHTjhDI9x6DcvbedQYlnRXx7.tOcGi3MShXDsFPi5O7wwvu_COqyVbGkgPu58uG4LT3Yxk6rAlhyAf44uzjAqQwKpQ0B687o.oeQYVSejPoK4W9Jd33GhxtH1JGPr4LZHebQ15vz9DpHtZz9tKL3hT7fdN.SB7SLpV1sUtTvqcUPok.kMPD9tZTfWg_IMfyQqMnQJDvRlOrQmatM5OLj49G8err_mLMK2GI4yopVSwIcjCHqLl0y8MS_rc5NWX5K9ox39A",
    "XSRF-TOKEN": "eyJpdiI6Iko2ZGszNFhEbjBzK0RzY2RDSGRUb0E9PSIsInZhbHVlIjoiYUZKRm0vM0QvSjRaUXhiQ0pWMG1XQW90Rmk0R21LcnN6QmZ6M09FZVFpSE5qU3dsWE82ZEd5M0luWXZpTUJ3akZURkpkeEhPYk4vdUwreVFYTW1rL0RzU3EyV3lRY2NGanpHcGdKZHcvRkVEV1BzRnJvOWR1STBIWXE4TVBocXEiLCJtYWMiOiI0ZjkwMGFkNGRlMmNhNDUyNGZhYWFjZjlmZTAxNzk5MjZiMmEyY2E5ZWM1ZTFjYTgzYmRjNDU5ZDU4MTM5NDE2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBQK3BWdWlXQURzd2llamErcS9qdkE9PSIsInZhbHVlIjoiZW5tVk1EQXJhajFDMEJJTldWNWt3Y1Vha1pmb21TajVEZklKMUlBNDU4azdRenNLelZqSmRUTGZySEk4OEpENkZOK0txejdNUFB1VXZiMUxoNk10VkJNa2FQdnorS3hsSmxyaUpBMWMwNFpTMlBxc3ZWR1RCdzZQTHlLZXZmR0UiLCJtYWMiOiIzYjEwZTQxZGYwMDY3ODQwODFiMzgwMjlkMGY3ZTU5YWNjNTQ1MzA2Njk2YTZlMDI2MDg4YmE2YmJkOWQ2OGJhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "WExm14F9VMyzXDNMT_X_os6GwhJq.ieLNppGoykGNSk-1791834033-1.2.1.1-L8z3uumVTayfG1WMSOYpDDETnhl6UJRx2fulxXopxPYNN9LluBLWnSJaulTa7dMnXrObTiLhJZpGvSNdlCP0ao6IvuH55rC58q363BxRO0xq5hMTOs.6N6ePdnWSOgAF0KvN5aA5vOM.OVbE.N78LUPkU.Vn_1XZ3BjymLhkHFkBdiIoaGtrfM5nek.MdAo2VPvOTtueGobra1Rp38aqVg_hO5mzyJiR3KyQPAfa19xqMzARQwnBFgzH4TcXtV5MeoGmRlZ6DGnnf8lFGV5RCQ.6vzEn6T0vaoTEIV1zzIrqsYMOXdoHJbGxPLMNilZSp4FE4RHUy8dbCIi_rDQKZEMLOFajfkt4Vn3naJN363JUcQCgpB0NE_zE2rQFwWfwHtQejfxBcdQCKjsb.aftn3Z5FEmHngzdWgVFLsFuKJFhqd.NlVjwmQ0eU8UfBn8D0GOwAedCKWlOcQqFE07GXCdrwxYd7iMv.SdcQG1.FhtNWqbLYlFKD4ry3r1A6hMbC9X7RzjZBig9twthP.q_aQ",
    "XSRF-TOKEN": "eyJpdiI6IkVYbmd6RVFoMzViclVORit3TStmR1E9PSIsInZhbHVlIjoiTVVaRGk3UzljeWFHUXFrVWs1MWZFV1ZHVThTT1pMTEVsbHptS3B6M3AzRUl4cUtFeHJMZjR0OC9aZ3M1VmNkYUg1MVVqNzI2NnVzZGYzQThLTEpQKzdvZjNZQ0thc3RNejVtaC9SQzJDY3FkYkxOdlBlVTd6b2wvazUxZ0hQTk0iLCJtYWMiOiJhNWQ3MmJhZTcwY2U2ZmIwNGM0M2IzNWJiNjM3MWYyZDM2ZGU2M2U1ZTEyNWJiNTc1YTk2MGFiZmYxMzc2MWIwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imw0QkZGcE9QTHVOeElLOGFWbFlYdUE9PSIsInZhbHVlIjoiQjNvSHdqelVlQysySzl5S2syRHQvYVE5QjcwSHpncnpXUW92cjhvRUVkMHNBM3BFMUZHbHBOUmplS1ZLdFkvSmh6cnh0RmhtUVdmaGpOaHhuYW03UHIrWW5kYS9FejVRbkZCU21rNU9rd3VLT1FXQkhBejVhQVZBRGNiMzFXZmYiLCJtYWMiOiJlNWYxODlkYTFiZTAzM2VkZDRmNTAzM2NhYTEyYjdmNWFlNGQyZTUxMmFmYzZkMDUzYTlkOGE3ODI5ZjgzYTAwIiwidGFnIjoiIn0%3D",
}

