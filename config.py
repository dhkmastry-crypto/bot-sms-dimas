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
    "cf_clearance": "r5FEMz1nKj1bXrl3k6gQVfK63_aDtLLmYxobX5KCI_8-1791980119-1.2.1.1-hE_xIsENTPs5rpeHmtx46xvZ6pK3HWSnTNNZIb5Gsm2fl.L9NYECIgkj7m3diF9KXYVkLlIQskFHQsax4xI4sAYtRfUvTk20Z2B.T5axW3Hmq7RUbpWmCEO1OhN5GlATpvze0_aPbuXKXDSNV7o0JNn0MgZfSwL0WNDcUH5nPqa.AUG2Mwgx1i9vpLdWhArFDAKIOTfCYpLZL.mbnKd.lq8cnVr_10eFxiJ6Ew1oRlFZXuUBgqyslNvlfvHMPUQtBx.Ywqt.suItaIbthxTzCc_JVDM1h2kjaEQ7SOm6feQKaAF.zfLdVY27RcxGSIci4QA9WCm1leRP8rloXdrnQSNv_Q0jekVMD7u8AONIXml_FTxWBNWVvCYdc7su7H.utQLhZc8cQ5qhPLJoEmdYm75PEyq2ZpNTtLC5pzKuSYXq_KDMc1PMXIceEULpqoVvVzJ4NYXE2t4HyJ.RNwZXxIrVA4p7XWTOpZf27FHgGA2KD38AjITJGEZfZRgCEJHmD0upzTpFbwKTPHhHmef5vA",
    "XSRF-TOKEN": "eyJpdiI6IjloejJrOTJoTWFJc3JFQk1hQTk1dmc9PSIsInZhbHVlIjoiYjNpNUVHSzJLSncwVjRZTnlGNk1zNk00M1FsZjA4cnVhVWZYdWZUNlkycDlRVGJ1K1ljbEszR0VGc0R0SG5HcCtoaUg2Z0dkYm5keVJFRUtOdEExVHRFSk1hK0ZzRjdrZnRqZHNoTUZ5ZzRoendPUTdOWXAzU0xjSStycmYyanoiLCJtYWMiOiJmYjM2MTYxYTVhM2U3MmYxMDQwZDQyMjI2ZjM3MWIxMzNkMzVkOTg5MmZiN2U1MzVmOWU5NzdmZWNhMmM2MDdmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjIxSm9nRERSbVE3WW5pNDFmbUxrbnc9PSIsInZhbHVlIjoid1lONlhnMEVJZy9rb1BlTjhhZC9MVW41V2x6OU1yZU03dVVCR3VydVFMUFlDS0E4STJRMUNVSmdIekEzc2VDWHUrUEVCZ2hwdXFDTWZ1R3lPK0JEUzVJbWxReGJCdE9tMHdVbnNKU3FqSnJNTFZHWXJvTzNvYUFXUkRIaHAwRVIiLCJtYWMiOiIyOTY5MzVmMmU0OGE3N2NiNWQ2ZWVkMGRhMGViYjM2ZGM1ZjQ5M2Q5MDE1NjY1NDAyNTc2MmYwNDUxZmQ1ZmI4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "SyTNCb8qq3UJSm9uxxw1FeEPPKYOQIPI6s7.RbYkdtw-1791978422-1.2.1.1-TlCjSoR3kVeaazT3e_4JksnpQTRHW.5.kOfDRnDu.v7k2Yx6YlxNyRe9xtn6I_47qxP1R5QVwQO45i.QWoF2CGxVyXPFNpcip4UnBnFkDoGwNmhibp5ojBySfzFQa9PfVNJHGj0NXiDXQ0GdR.KkXdfEj5e_I4DEKkDWkKxSokWdXskC4TuvJ.UB3IHzII_I8DwnbpigIcDQvlXQJH6tF1IxZC4ULtMWbQ4kngaa6Fklcd.6nYznkWgmkWctpAiDJJKziVkLnbWoFBTS0A5pMoZTQTO6tLLKVDRLwdpRFVAOli0XTblisL8UT.nDgmicoW1MxiMFm35xVleBqXns_M4kL_w2RXXrIB4irTNmgYSg4AfKLczVAwnFFS10FDJDGJ_sCyfIAI6AyiHr30ooKQC2YX4sWa22VEOUJ2wTvo1zevXAUtJ85U5rR9JTv1w6eNw0Uk9Ds0aeKPIh7nbQcQncYGr7GzG8nos9MnfssF5ft4E5a0tlvMHAnQFcuzZxI0ysSRE87_0kggStdqGcdw",
    "XSRF-TOKEN": "eyJpdiI6Ii9vMEErSGZGaFNUNVRuN0hCU1ZNWVE9PSIsInZhbHVlIjoia1hGVUdOejdBeXVGbk1KRCtId1Q2NCsxN3JQQ1l1R3NCencyTXhFeGdjbkJLeFQwb2huQy9NaXVMaWdNbW5pR3B3eWxjdHdqWXFKQkl2MlpTL2VRTzV5cTFSeUlGS1NxNFBManBZNjl4VHVJYUpDV3AxMmJrV1JKYmQzV0plYU8iLCJtYWMiOiJmYTgwZDhhMzJkODUwMDcyN2RiNDI1ZmU2Yzg5ODUxMDFlZTYxYzNlZjIwZTdmMTljYTY1MDNhM2RjYzlkMDlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRJWnZzejN3ald3b0dMYWlueU16MlE9PSIsInZhbHVlIjoiTGw5NXFnOEFyNUg5cnE0UHg3b2l4UnVCTG9Qa2xRdlg5YVhxQVMxT0U0Z1pMVE5jUjBvS2s2Y01SMG1qYlRrSEVIbFFEbFd6ZWVYTWNySG5tRFhzMkhxZ1R6dHJBZ25VVHZsOWFiYjlSbUJqVG5RenNwQjhMa1pwMi80YWlKMzciLCJtYWMiOiIwZTUyMDAzYmJkY2ZjZTc5NWRmMjc2NjkxY2EwOGNmZDExN2JlOTI1NmNkYzYyZGU1MjFjNTNlZTdmZWU4ODZlIiwidGFnIjoiIn0%3D",
}

