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
    "cf_clearance": "qK.vMk2Onv2QGxT7okiBYFLlLlpWfIGrKGaaH03x0Zs-1792083607-1.2.1.1-CPr4o8IYQyQbYiiqJwNYDihYvpB6CHiAFw7kvseRq9i0XMQgN2IzSNy8LBHKHmA_3_Hx9sI0aUPT6dwApB6RTlCBYaqkWmROeV1ep9mYCUo3e0KPGXWY5zqmjDrI272bKYPnpm9QwmiAN.j5tkxCkqgA.kpImYwE.qJSPOGZiV4CwP2rV2OkUoCG6Gk98aZGsgQZyZyWk_Ltv8OHy5TKlHULIdOPCU0lh4aCJ1dZz6qkhqQRdsde7ShWxxVqPjv1EzFBxNrrdYQ7siQuV5UXIzFH_YyuAGKu6Ouu.ZRMvDNlaWQbxk1o82.vjSsgLetjuAucHpmLB4h9dWDXNBBPgJ7XP9WTmNp1ZRD5hngqQlTy8fh9ryAkWaDxqraWTHBmeBf5jVtuMWx_LpRy5GXWm9zQ_vvh9zEgbIisUSVlhNqTk5KaXxeo0lqZxy7Xi4Cgj7I4OvUawF0NRc5NJud8J6WirpOcEC3fLZ3TIz0oYrBhewi.FjhEuOTZuuE8JP6EuEvmXVE2HStR9Ho1lWFP7Q",
    "XSRF-TOKEN": "eyJpdiI6IkttVmh0QUdmK1JIS0Zhd3JMUU5laGc9PSIsInZhbHVlIjoiSFVJUHRHK1YwRWxDZExQZ2RWVnR6SGtuYm1RQ25NTHBWMFZvZ1lGcDZjYnRSSlR6MVo1bWN1TjYrK0k4YTlkVUtZek1uQ3pzR0svSlhVeVprTGpHbFdhYnVGZ1pCZ3YxOW9pM3Y4UWgrSVc2TTEyUkpWY3lxQWx3d0tsV3BBdWkiLCJtYWMiOiI2YTk5NTA5Mjg2MGE4Y2U1ZjZmOTNiYzYwNmRhZTBhZGU4MTlkNTE0OGViMGI4NmExNDA3NTc5OGE1Mzk4NDdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFoZThpTlRmS2dlQ0wybW5iOXJDa1E9PSIsInZhbHVlIjoidk42S29sMmxyWFI2ZnRjRVNDa3pQOFMxR2R5ZG14YUZYQ3R0cnk1K3NsenhYdmJDalcyNFNEL2dnOWZ5SFlpTU9zMFEwWU53S2Y5Qi9MWHkrb2FuL3RIeS9najcwQld0V1J2ZFZZdU1qNFloOU5vdGtUK0haQ1ljb05NM3Y4OXkiLCJtYWMiOiJhMTQ3YzEwMzBmMzcyZjljZDk0YzVjZTI2YWJiN2ViYmRhYzU2N2I3YmRiMTFiODU3NWZkOTM3NWM1ZjljYzYyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "L08n_vhytl6vEXkmWISPlturoUQxxkPex3.7Wgd8oe0-1792085371-1.2.1.1-eSmaLfbhYBXLt5pMnuHxSSPSoQf_9o7o8ksH_lJrtBFQDsEONmQQzGujVe3FgO4Vw90ZsKsJ5aKnVh08z29SVxoV2j9UKcY6BgyDVdHgLMMzaDwARV_5N6vivWLzoojkbrzyaeOexxyh5ibYxICXTVZVVoh4So_tgY_MGAsizXAUE1z033npffz_JI4W10IF9GYFnSUZ9JQFFrjJg1K64Ie9VBmAAKj5s6EMwStrs9BTMAxQ5tmKJk8y1Gr69rRhj1yVx5ezXMYBOJn0qIXnOora_el2Kb_1EFpqyoNFfxsqEVkFX4WBjtLa2dOXBO1h.HUkIFf01ndaWOEzdQ23cCXY.3EFB9EIrTjt_NVZep0sxd51xCHpMVnEhPGILOb52tLf_or89bU9.IEMaIgiv1YBwJpPQ8HXxi1fF_NWYKXqNn.vvdPJgjgRl5bJEOWy.Sl_pWlBMC1vqZ9gOYE.nmBgV9g0YinuW5EVRNHh8QBmJ_ERVhPWveGjmpq.B9LTJjyzUarRyQvNo66rWqzWVg",
    "XSRF-TOKEN": "eyJpdiI6IjZPUDJxM1RoaVpUNk4yVUZzTE5pNEE9PSIsInZhbHVlIjoicm5lUWpFbENmMVh1N0wyakxsQncxRUNzQlZId1cra0hXblNET21aQ2dQZ3cyTndpdkFERXUzOHNxdEM0Vi9IVzE5NG9wMlB3SnRmMlV1WVpSVHo2YXhSaTAreUN0Z3ZINWFvNUkvd3B2dWhDNEtRQnpZd1JJMUJSUG1NcXk5NUoiLCJtYWMiOiIwMmNkMGRhMGM0NTFkMjA1ZGM5MzliZDczZTdiNzc0OTNkZDk0Yzg0YTNkZWI4MDk2MDM3NjFkZmU2YWI3ZjhlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IksySGU1Z0dNNXo1WDREYTF3V3F3Q2c9PSIsInZhbHVlIjoiWnpXZzdsK29QMmFuNkpRU05DNVoxTytHWnhQQk5mbmRLK1pYZUlYWEVyTGpkWVJ5TVdMcW9lU0hKMGFpbmdTMUxlN2szdnpwcC9nUEwyVld2UGJDaTdqa0lhTHpOZHh1emhUdnhJcXRwS21vMHJQTkRQNzkvMk15ZDJpZ3UzbmUiLCJtYWMiOiI3YWIwMzFkZTIwZGNlYTE4NWRhMDg5ZmUzNDJkZTUwYmVhZTZlNWY1MDA4ZDliYzEyMTNjYzk3YTY3MDdiZDIwIiwidGFnIjoiIn0%3D",
}

