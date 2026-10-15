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
    "cf_clearance": "owQckm064_IfgoN.D_PGKClcEUOUPoM6fcbnXLAncMs-1792039170-1.2.1.1-jYH02NDO3PSSy49LwmxS4g4RQDggMEYnF6pCIVSt3q6zL6nugZxiIZ9jpPUvN.LnI3L_BmT9xaeU7sFqJOgEm8yno4aeqvq_US59s2vUwurw1z7opwNJKv6mnGu76GMj4NAwlf9pdwJzl08HAnL2SdELYh0fIhHRN8_Cmzdr8wlz5z1M9Hcm7c8aMSe_Xg6hRmWrDASA8pJJ2YIupxx8KbsOIGc1vCpGCRf9u6C_tXV__9wMAQozt2b.8L4h8EosDYC2vq4DNq0Ti4C.OnaeHd1upoOVauGyoZp9xOZVyT8kxYBfcJMyJ2SRjZJa0XW2Ec8RP6y1vCIrHxs6aZrAU2fc1FK.zdAx7WEZQx64wwRpDSZW2fJUHjA_t5geOpalzLcZkDYqXojNTg3LZ554tTNO41U6z481ee.MZBro03V1NIINTuvcrYnMHjeED1iuHmzg_SSTs.CVKB3PtK21SfcWQ_AKXxSgqiqiIPTKMVJ2NmBw6yS3VRDA33yO9E20Zm8Gex7JZgi1S0FfCkXDxg",
    "XSRF-TOKEN": "eyJpdiI6IkVmMlRmYWxIVnZBN3BlOTN6aDBaWlE9PSIsInZhbHVlIjoiM05ZRlNtVFR1dW1QMmtONUpSZGJ1eE1hWDBMVVAzTFp0eU9uLzhNbnVNYjdkODJ2Tjc3b21SZDlsUFVYYm9TeXQ0TTRURU5WZ0ZwanhlMkViZWxMK0hNbStIRFFzb294alVOTkNoLzgwWjNsMXVLN1hiaGFSNFF1NWZ0V2NjREkiLCJtYWMiOiJkNTJmYjJhMDFkMjJiNjQwZTYxNzA0OGRhYWQ4OGE5NzQwMjRiMGUyYTllMmY5ZjMyNDAyNjA0Mjc4ZDg0OWUxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InR6RWsxaHZQclZPZlZLbnNVMERLVWc9PSIsInZhbHVlIjoiVFNYb0dTaUg3Y0FZRzVxOHlvZkdLVmcyMVNSN0R4amlLT3ZBYnFjZDQxalR6eGVybURtZXJWMTVXeEZ6NW5Wc0NwS1FXVUxFdU5oNjcvVy9ibEFaRGJtZURXdWZqRmxXSEllaDhFcmJBYzVqZ1k3cUFUWUUxVlliVVpWVkZXd0EiLCJtYWMiOiIxNjg5OTg3NmYxNWFhZGVjY2RkYTVjYTIyYTYxOWU3N2M4MmY4M2IwNjA2MjUyZTlhYTFmM2Q3MDc3MjhjMDQ1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "n1YwIzNdlBkW9Tv0mLsB89n9hBZZwS235Bsqrhjz9qk-1792039161-1.2.1.1-06wAwZZv58k2iAcyWpE7vQY3yIskc5UY3iLvbnbUso7YEBe_A.aseVY9kPm2hZR8zDBcsz3KIeKnIcGZMdcfY25N8Gtt_3ykRQ.oYs92eXlD9aeccBlI0MMjI4uucBtPC_S8YMZQzuK8B106HAv5BMH33QIB5HqCrVzbXFRVxz5b6akSvnBKS2IOI.oKbU0yhMaWZ6_mRByla3A8x3PCQV_OMG1LGCDIqQ4JoRwtbXbBpD_MB2E5BK01FLN9Wt2368wYUuklhYoNvkAd8RbdNQSs4NJhWaZzx_.ufpiLpZXih2Zv_9NUN23Rfax4r7B9PGktVBfozmx80aXGEKrbrvvsKho9XvO1FUgs8dkDer7rt2C3p9urXaUOm.wVi5l2TXhtqeXDFIbg2bsDiCmfT4ZNKvIHhu68URbuYgAtE69k2j6C0FyX94Y20_ZlSJYLPIIFHuesCEkPMBxVdCFIVYY5no4gH08tJ_AfQCe4QAEuoAiOQC785oLeSYctOLTaBBrYNjDUjhK.PQ_Pat6AnA",
    "XSRF-TOKEN": "eyJpdiI6InliMU1YUkZ5Ukt1cGNFa1BTSTBkalE9PSIsInZhbHVlIjoidlJpSVVrd3dxYk52eFpZSVFoL0xmTStlZWZpRi9HbFViNnRzajZITG5XVVVvbHdZZlNTZXUya0RFai9VZnFmcXA1cHdqTFQweW1Ja2dZdUNPei9yMTlVNHBBaGxycE5aN0RBUmROVDYwNzNsRkRadFN3L1pZSVJ1R2RmMEZXWnAiLCJtYWMiOiJmMzUyZjc0Yzg2ZjVlOWQyNjk2YjhlMDZiOTEzOWEwZDU3ZDhhMTAwZjUzNTBiMjRlN2UyMThlODkzNWNiMTQ5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkMyWkR0Vm42RWFJV1FPUDJ1OWpJckE9PSIsInZhbHVlIjoiRWtQOHpTMWd1N3QxTGJSdC81cm51cnJITFNOa2Ftc05wZzNGV0YvclFiRVNDYjVlSVkwY0t6bWdVWnFSNGxmaVU0YWNpMmpBaVk1bUxlbmwzNTFrQm9sWVRqS05nbWVLak1IQlQyUi9NZ0ZNc2JiOXBUaGl6emtwUlNEeUc5NHgiLCJtYWMiOiI3YzI0ZmYyNDM4MDU1NTUzOGEzYTZjZTA2NGVhOTRkMzRlYTRlMzY1ZDJhNTNjZjc3NmI2MmIyYmZiZDkyM2IwIiwidGFnIjoiIn0%3D",
}

