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
    "cf_clearance": "LDJqWm4TytJf4h13Jxt9DrRDl8DCdJ1_Q2pKe89Dp60-1792040983-1.2.1.1-4XugI2aNEyhCDZdEWnqdV9VF7Rm.wNmH93WttUSMUGjp2dj.eI5bH3Zqxhn3kBZ06zCc0hDR8564itTaN_fTEMKV_E7lvR_kZjoZHloYZZOI62boASF9qqbF6FE1noXcy5BQ3M5dj9lHwCBe53gxCHro0SP4PNS3Gooc4Lh04Mzgc9rNtkqbYJbRGS4zDX0ShsrhVNu7l9vBGouhN2pF66DJjZfJS3Ne452h.9k7rMLC46BU.ZxA14pZnAM2rgIxC1RajXzfG5eKW39Mgt2nLMwp9iSuyUTwJkX3VHbtK46jzgp9EBVUH0owUVFIIyTA_o0zUvWvWMW1yzOUaW0b_qbT5uOkfpSEFodscUXv1xZbDOfuupttY88I2uV6lKqiOJDhqhSsBC.2jmkaCbfHkZ7WPyKvqJeFzYvtamoYp614c4yQGCZiLucIuedMqE3nGtLfWFsccxINETsq0bzr7M2tQXqw28McR6xcpUzG4.0vJzdx3x90pe9ArwLMDc0aBVzQCJ8WfCXMaB.9iF5RLg",
    "XSRF-TOKEN": "eyJpdiI6IjFsSDRGYUR3eUtQcHRtQVBJVVlXYmc9PSIsInZhbHVlIjoiODlRWkNsZGhDbUJoN2ZPL0loZTBUVXRMSmQyWEN4dmtsTWkxSmdEZ1JwV0Q4TEhGYXVJN3ZpQ0k3ZUZ5UE5rWjJqNU9ZaDVDeXFOK081N01uUWFUbTVPMkRSMUpGbzRHeDJnNk1NYU11MThoU295MVlOYXNvd0dHYUVOOE5DRWciLCJtYWMiOiI5MjQwMWMwNzE3OTc5Mzg1NjBmMTBmOGJiYzk1NGI4MmZiYWVhMDI1OGYyY2Y0Y2MwZjM5MTA0NGNhZTRjN2E0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9sZHRqTVNPdVFpUDBPbjM4dW1abXc9PSIsInZhbHVlIjoidVJNTmNYeWt1TVJTbFlxdHRyUkFPSy96WndtUFQzbTVIWGZhYk9nbUkwSFFPRXBGSlZlUFpmZG8zeUR5MG1MWTV5TDRYbjJ6aXlsbGJqV1RTRUlNeENjMzdrejRyQ29lSGtkM2pMOE4vMEZaUFlwdXREdUZubFROZ09MbnM4ZFAiLCJtYWMiOiI0ODY4NzNhY2FhNTk3NmNlZjUwOWI5MGUyMGJlYzBmZTY2NGNkOGZjNmE5OWI3OWY2NGMwZmFkOWQ0YjM2YThjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "n1YwIzNdlBkW9Tv0mLsB89n9hBZZwS235Bsqrhjz9qk-1792039161-1.2.1.1-06wAwZZv58k2iAcyWpE7vQY3yIskc5UY3iLvbnbUso7YEBe_A.aseVY9kPm2hZR8zDBcsz3KIeKnIcGZMdcfY25N8Gtt_3ykRQ.oYs92eXlD9aeccBlI0MMjI4uucBtPC_S8YMZQzuK8B106HAv5BMH33QIB5HqCrVzbXFRVxz5b6akSvnBKS2IOI.oKbU0yhMaWZ6_mRByla3A8x3PCQV_OMG1LGCDIqQ4JoRwtbXbBpD_MB2E5BK01FLN9Wt2368wYUuklhYoNvkAd8RbdNQSs4NJhWaZzx_.ufpiLpZXih2Zv_9NUN23Rfax4r7B9PGktVBfozmx80aXGEKrbrvvsKho9XvO1FUgs8dkDer7rt2C3p9urXaUOm.wVi5l2TXhtqeXDFIbg2bsDiCmfT4ZNKvIHhu68URbuYgAtE69k2j6C0FyX94Y20_ZlSJYLPIIFHuesCEkPMBxVdCFIVYY5no4gH08tJ_AfQCe4QAEuoAiOQC785oLeSYctOLTaBBrYNjDUjhK.PQ_Pat6AnA",
    "XSRF-TOKEN": "eyJpdiI6InliMU1YUkZ5Ukt1cGNFa1BTSTBkalE9PSIsInZhbHVlIjoidlJpSVVrd3dxYk52eFpZSVFoL0xmTStlZWZpRi9HbFViNnRzajZITG5XVVVvbHdZZlNTZXUya0RFai9VZnFmcXA1cHdqTFQweW1Ja2dZdUNPei9yMTlVNHBBaGxycE5aN0RBUmROVDYwNzNsRkRadFN3L1pZSVJ1R2RmMEZXWnAiLCJtYWMiOiJmMzUyZjc0Yzg2ZjVlOWQyNjk2YjhlMDZiOTEzOWEwZDU3ZDhhMTAwZjUzNTBiMjRlN2UyMThlODkzNWNiMTQ5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkMyWkR0Vm42RWFJV1FPUDJ1OWpJckE9PSIsInZhbHVlIjoiRWtQOHpTMWd1N3QxTGJSdC81cm51cnJITFNOa2Ftc05wZzNGV0YvclFiRVNDYjVlSVkwY0t6bWdVWnFSNGxmaVU0YWNpMmpBaVk1bUxlbmwzNTFrQm9sWVRqS05nbWVLak1IQlQyUi9NZ0ZNc2JiOXBUaGl6emtwUlNEeUc5NHgiLCJtYWMiOiI3YzI0ZmYyNDM4MDU1NTUzOGEzYTZjZTA2NGVhOTRkMzRlYTRlMzY1ZDJhNTNjZjc3NmI2MmIyYmZiZDkyM2IwIiwidGFnIjoiIn0%3D",
}

