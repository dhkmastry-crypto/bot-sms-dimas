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
    "cf_clearance": "KLrVxzXIZCGW2aRbawzPv6NqNzDsCxa4yYBB94wEPoI-1792085413-1.2.1.1-knpIiQQmNbkpu2S.lnB6okrff1PIakfTlP2cIU42qjYnEPirnjm6oKYTgpzfA2eb5Pz71b0LzNOmmTp6p.Ma1EJ2ma_m0ZG7Y.hFN5zfG5Z0lWhnCTpemtcYsWKhna9r2u7rqcHRVe7dqtqDtSwMVea9zBWZ4cZvV9gZ9F56AMRhHkLoM7j1x1im6qFp3tKIo9sVOfgrAMgTXycvqd1pHktNmURwqNdrvWt4EirYC3Y8xi6GUuvCfJIBkbTvyTR3F3_AjsgzTi8K3BegxcDWP_kXto.E8ngnm7.TUPqOap7XagsO24eJ_KDjNGsZVD2f5TpaVUZwo5Ijey8Qcd6ss9C1yfRps5MuBbzul9X8JUt7UpT5N2kRGKGOcDziNndUWFfM_V7dttZg2ylf1GXQQWgQ4UTj4f5x4FJXNkYJ4d.HBlLrpKJici7whTAnowbE9h7sg6waZi45Ux3mlXtmW.ldDV30lxqVebDarNX_kw5QKH6y2hNgpUHVBrAAuMQWxTbbaiLXSUFaEhZlkaacLw",
    "XSRF-TOKEN": "eyJpdiI6IlNobFcwd1FKSkNxaitiNDA2WU8rRmc9PSIsInZhbHVlIjoiYW9TVUxLOU9wNTNhUGhDMDA3WStvdE9rOWpoaDVMQmI4Yll6Vk1Oc3ZQOHhrSzh1NVhPZkpYZHU5ZmVYT2JOMmdBbFlDaWVFWlA3bzRtdk9RN1FSeHVmSGVmRFRKKytKOStkeHZxamFvalFVWTg1UzNtaGhPN05ndWNQL0grdU0iLCJtYWMiOiJkZTY2YTYwN2I4MWIwMWM4YmJiN2EyYWMwZTIxMTI0NzkzOTFjZTY4YTI2MDk2MDU0MWMyZDFhOGE1NTY2YmM5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imh6UGJ4UjliaW5jZDlhMWpjNXc5SEE9PSIsInZhbHVlIjoibExYU3Nuc0Z0U0F0U3FMb2tDWkw5M3dreVVnYzBYRy9zMVRQbmsxWXVHbGkzeElvUDBGdmZYbUhiMTFNTWZ6SkkrSkdka1BiVXltTG5YQXlJSzVWY1YxU29IM2JRTTR0UE55TUxGOFpJTlNoTDlwTXhscDlwTThCTE5EQTZ4aVUiLCJtYWMiOiJjZjAyZTYzNWJiMWQwMzI3MzE2OTA5MmUwMmZmODFiMGViNWRlYTc1YTRkMDIxNjJlODE3NGI1Yzk5MmNjZjljIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "L08n_vhytl6vEXkmWISPlturoUQxxkPex3.7Wgd8oe0-1792085371-1.2.1.1-eSmaLfbhYBXLt5pMnuHxSSPSoQf_9o7o8ksH_lJrtBFQDsEONmQQzGujVe3FgO4Vw90ZsKsJ5aKnVh08z29SVxoV2j9UKcY6BgyDVdHgLMMzaDwARV_5N6vivWLzoojkbrzyaeOexxyh5ibYxICXTVZVVoh4So_tgY_MGAsizXAUE1z033npffz_JI4W10IF9GYFnSUZ9JQFFrjJg1K64Ie9VBmAAKj5s6EMwStrs9BTMAxQ5tmKJk8y1Gr69rRhj1yVx5ezXMYBOJn0qIXnOora_el2Kb_1EFpqyoNFfxsqEVkFX4WBjtLa2dOXBO1h.HUkIFf01ndaWOEzdQ23cCXY.3EFB9EIrTjt_NVZep0sxd51xCHpMVnEhPGILOb52tLf_or89bU9.IEMaIgiv1YBwJpPQ8HXxi1fF_NWYKXqNn.vvdPJgjgRl5bJEOWy.Sl_pWlBMC1vqZ9gOYE.nmBgV9g0YinuW5EVRNHh8QBmJ_ERVhPWveGjmpq.B9LTJjyzUarRyQvNo66rWqzWVg",
    "XSRF-TOKEN": "eyJpdiI6IjZPUDJxM1RoaVpUNk4yVUZzTE5pNEE9PSIsInZhbHVlIjoicm5lUWpFbENmMVh1N0wyakxsQncxRUNzQlZId1cra0hXblNET21aQ2dQZ3cyTndpdkFERXUzOHNxdEM0Vi9IVzE5NG9wMlB3SnRmMlV1WVpSVHo2YXhSaTAreUN0Z3ZINWFvNUkvd3B2dWhDNEtRQnpZd1JJMUJSUG1NcXk5NUoiLCJtYWMiOiIwMmNkMGRhMGM0NTFkMjA1ZGM5MzliZDczZTdiNzc0OTNkZDk0Yzg0YTNkZWI4MDk2MDM3NjFkZmU2YWI3ZjhlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IksySGU1Z0dNNXo1WDREYTF3V3F3Q2c9PSIsInZhbHVlIjoiWnpXZzdsK29QMmFuNkpRU05DNVoxTytHWnhQQk5mbmRLK1pYZUlYWEVyTGpkWVJ5TVdMcW9lU0hKMGFpbmdTMUxlN2szdnpwcC9nUEwyVld2UGJDaTdqa0lhTHpOZHh1emhUdnhJcXRwS21vMHJQTkRQNzkvMk15ZDJpZ3UzbmUiLCJtYWMiOiI3YWIwMzFkZTIwZGNlYTE4NWRhMDg5ZmUzNDJkZTUwYmVhZTZlNWY1MDA4ZDliYzEyMTNjYzk3YTY3MDdiZDIwIiwidGFnIjoiIn0%3D",
}

