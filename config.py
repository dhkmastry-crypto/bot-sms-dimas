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
    "cf_clearance": "NZM4rFnzvZiyJQR6XG53Gx0mmwgkhYXi5NfWoHWVrR0-1791835844-1.2.1.1-DmI20ifpOyVwYTY_tn6zn_mREAGx09TkqR.f5rmzK7vCeO5UoGQGEEzzDg5VWY7pd84aA9iFKhfgxDe7ebfZort..zFph1sQZfwuiNq1nkr_IIsEd1hRMZHAc4S.bbyBEA00rEB5CU2Fgndvq1KPZ1SJG1VwyPwfdtyxJJBMEtoOrh_j0PduQPckD2z59A02KJVa72I5VT1xJFqXvEi2aaTrJ48AoQXHS2bi_2VhGgOSbaGtYK9g_5MR.khtaT994KPEbxXz47lHzI_1W.ISNnZdbKNLa0UmIPrb1Bk4WuHg5.DuyOecg0g_L4318_rCrkVaN4HbWtcYFUApivHbBoqAA6iP_.xPJbKyRbuq1b0yxsxbZJ4ml3azKO8g1CKCBWW5.c2zVAx4JV7NQQzTF9YI6P7d4JxoXZ6Rqm6hf7dKdnHDsFRWDtnRtg_4wC39HZoRRHajglrMT9YtkJ.s0cHEvgEaFCfwdGs5zRyob97CiZiG6u.Ia057TFgqTxaND0VEBJccEDtxL8nHcPQjaA",
    "XSRF-TOKEN": "eyJpdiI6InU3b2RXTDBNKzkzc1lBR0lzRWVKUmc9PSIsInZhbHVlIjoiZzB2TXMvbFZoRWNITVhkWHVXMStjWm5zZG15YkFGMmpxYXRLWHVweUNZbDZEMENSaDVHK1h0a21RMFdINy9KeFl2WE04QXBxL0FxaXMzdWVRT0FjWHR5ZWhEOTJGUk5RSE5MeFBkb2w5VmhzdVE1UGllY29wS3ZzeEczaHR1bFEiLCJtYWMiOiJlMDQ1YzcwYmU3ZTVkODBlZTI1MDM1NjM3ZTY5ZTgxOTdlOWJjOWJhZWE0ZDVhMjc0ZTBiNjhiMmJhZWZmM2MwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRZTkNWSUlRaXNzYUU2MStqQnNOMGc9PSIsInZhbHVlIjoiYVdETzJjenh0Nys5U25xSFlQZDQ5U2IrcU9vLzlmc1FVZGhEcCtmOWtyeGV4Y25Wb0dNa1pEdDQzUGZQVnBhNE1WazdKLzNZSXNzeGpNZlg4amFoaHE3aWdZc0FlZ1JpSEFDYTZMUFlKN016QklLUUIzek02Y0dHUm1YY2RhZ1oiLCJtYWMiOiIxYzI5ZjRjNGQyOGU0NTNjMjE2MTk2YjA3NTBkMjI5MjRlOWI2YjI0MjM2YzdmNzVmYjBjNGVmYWZiZTUyMzg3IiwidGFnIjoiIn0%3D",
}

