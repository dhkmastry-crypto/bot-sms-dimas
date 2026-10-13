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
    "cf_clearance": "Bxw0R_zZGlOMayDiC14E4mZSmtyrBcL81Va5tjG6bF0-1791854780-1.2.1.1-PMzeQuiuFwaCOCVZRYAXR14FqmoTWAaL74wrr7pIR7CxitMEMBHxvjqO6srqIuLQQUF0KQt8HuZ_4BsZPDslkoRZKguno5XE2Vni1.elPWt8D_JLkl3UDic9Xzjsts3W930c4amK9VxwKDGN_33cSWYSixJhvCZKEo97zvz563AVbQQQlXXy6iG8a5h4Uiu6VEdJKn9j6ilHP9i5tPmnSYJ4SyAVDFn0zhwTPtH.35rriGeJp1YY2uiPfrqavBIXB.qLmOXhNdsyQOWIdr2vZjyb5ijooZ9BsL3lXfM.6YNBxFL5n5jn4TU1u3y2YQQRn48ue9FcRxGggCfmG53wzFLaRBpX_yzXd1DJOyS71OwuwnAA_lGkxKCh2WaTDZpnz3xgAVTE2BgorjLjS_SQPKYpoYvpDiU3tte4ohkk2li78OgZxqqQaOiB06ZjsUm6Rar7Avj2JDCT4FCgfS1n1nFUTvnkOJqd3rL6hBbE5knw9vtu6U8J8ZyKlt0uC1KimPDGx.n_YAwist1oOLhkJg",
    "XSRF-TOKEN": "eyJpdiI6IjY3aWNsTXFCQ296Q1B5dm1mZno1a3c9PSIsInZhbHVlIjoiTXBJRERwZHJSS0JuWXNtd1NvVVRoc0xJU1Q3d1hTM3BHZm1PejZMclJqODVBQUpBSWZtNHJQYUVlUjRXZVNqVk1ES01PdTg3RU0wWFhOcEMwdW9TZUc0bGJNck5FWWFrbWdrd0NUZ1ZGNFZtWmo4eDZuaEMvajRlY0FtY21hQk8iLCJtYWMiOiJhNzEwNzVmNjUzNzZmOTcwNzU1NzA2NzUxZjY1ZDc4MWRlZTliMzAwYmZjOTRlOTY3YTE1NzY0YWNmZjExZmQzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9EakVHTGs4aTlJZm82MTkxSnBjOHc9PSIsInZhbHVlIjoibGFiU1B6UDlITVllWHk1NHA5bEFXQUMxTnYzRkk2TUtOZTMzR0VmdnhuUXF5RWNieTluV0k0SjFqYUtSSkJnOUtPVTVYaUg3UzIvUHdkb3RWOHgrZUJIT0R0czAzNHdWYTUrWjFXVkFWZ1o1NTlYR0lUTDlGd1R3WWVVdlYzd1giLCJtYWMiOiJhNDgzYjE1M2NiMjg2NGI1NDMyYmU0NDdjMmIzYjgwYTkxYzBmMzYxNmI0ODEyNTVjNTdmY2UzOWVkMGFjNDg1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "CKVyDBNKpF3WAFRNQeDFzRYXdICZ5paCT8syPwovGyE-1791854139-1.2.1.1-vvtn9RZDR_G59eOQEXrlUeBcN3RAsLX69M3R.eSdmqQyKKzzDVXTFuWuXodax0AqRMyvo.FUtkOqYd4efac866ghzxrmDw97PhXfvmINbp5_x.yKTGkumGaOfIgom2zE9rejR969nZS3QoPw2GTPVXcrzQLMYrTQbrlTj6TcEuKGLA2eIecuHpmzz68T0lxw_W.YEw3Vchl4dyGZVAOIyMOnaySMdCmBUpEwotuZo.ZPIKWdUDE64rIBvo6qsb5JkHAPoJKAldT9um74kgMFTi6g7RjMi4Y6Ts8SlQfRN9j0Q7Hq8TYUdJBeLY3wUOXT6QsiajL7S7fKitaOrSMwH92QoaXT420nf77ZptVNd52xgkf43swVkDhz.GZPyaz4YEBdF8xK6wCVPC3tuUUFQwjfjvnocreS_ZC_bRkd.JqFxXAlnoPi6iYcJ2ihP_evULB3KRtrDJvWamMZY5GJ7mCVg44rjvr_4ZFtV395orTmHw6KpeJatedBRvIRvelrtkJE_p6eiFFzLXFRCYyy4w",
    "XSRF-TOKEN": "eyJpdiI6IjNrODBCWHBLR1J2eG1iZ3J4UVZKVnc9PSIsInZhbHVlIjoiSkIxV0Y3UlpYT0xnOHNNNE9xcVdLV3h2R2hxd1l5Rm1Eb3lpdlcvcm9ydXlhbGl4OStUdkNPcitoNmZuQjhiR3ZOdjVkVmFvWDBHSlR5eWV6L3RZdkhLT3lrY2FXTUVPdCswc3Y3MjlicXM1Z04wZStDS1FZdkZ6TVo1eGV2Q28iLCJtYWMiOiI5ZTc0ZjM0MmM3MjJiOTY2ZmNiMWI2ZGJmMjIzYWIyZmVlODJiNDFkOTdjNzIxODA0N2IxMzAwMmZjNTk0OTUwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImlhZHNUZ05RNUhIUVBZTnFZeXYwMlE9PSIsInZhbHVlIjoiY1VMOW0vOFY2RXJMdVoyU25uZHIxU0ZyNldjRHJPZkZxSENoZnN1cHRyajkzenlBK2lPYXhKOXFSMTlSYklJQWNHcndtMWFVTjhSZXBvR0FxYXBZUWRYc2hmT1BPbGx6RVVVVjB6WElRTVhRbkREWVR1RlhGMVcyS21nWkRwZDYiLCJtYWMiOiI1ZGFiOTk3MDExZmNlNzhjM2UwZTc0YTM1N2MzNjUyMzUxMGMwMTM4NDEyNmUzN2JkMjIxZmQzZmE2NTBjMjZkIiwidGFnIjoiIn0%3D",
}

