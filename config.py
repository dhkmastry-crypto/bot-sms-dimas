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
OWNER_LINK = "https://t.me/dimsongkangs"

# Chat ID Pemilik bot Telegram (Private Chat ID untuk menerima file .txt nomor otomatis)
# Isi dengan ID akun Telegram Anda, atau kirim /start ke bot di chat pribadi untuk auto-detect
OWNER_CHAT_ID = "8584584698"

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
    "cf_clearance": "Sj5Y1U1Uyv3INngWsYUrUnqK1jWLQJBZ8pzdirro3OI-1792150678-1.2.1.1-PN6_9T6yGRc51IajL6vTmJTC60CFPv1tx8gP9Bl0eIUIpWZsVdJhP15oBDuWoC_66XW.9O78TQt6u9kDuf_GGtIw5j667863jQ0yk6jWVvDr4CfajW6i3MmBFgmDL2Rex9oBQK3pllJxx5QmN5_IDU8xwP16KWs5rcwxLHespjxbq3wsDcS1_RZJ45JQRjI6Nbnct8S7w_pENXn_Xg0Q5m9MgWj4M.bGQO4r5DBCRm2N3NUS6KqwwQI41uUDSk8npIzcDyLQ3_EGqnWShg5_zQsM1pOAy_tJtEi.JE.XvUhYLgrAejqSnsG9NhmBnqNqOCM9Y4rvD8XU8GpNNeQoA9TVlAgjT2CvCl35xq_.hOlS4982JXMC3T6T7CE0.mA6MSZ6kqkomweA8Sbbw4yLRV4G_KTv8iiOs6yZhiKscvwCvhE4_W8MEI6L0m6mMuSPSz9FhFt6nqEmqaRPJu5TewKrNNicUzBeQ_kqUCPVhtz_8OkidwbgNGLgfNN0BTUBgDdAREb4c4BR4VWNP8hnDA",
    "XSRF-TOKEN": "eyJpdiI6InJWZXFKUVJyV1JRSWRhZGF3dnh4c0E9PSIsInZhbHVlIjoiQlZWZDU2cEVOT0FydXhubFAvaVpHbkxvdWlHRXhma1dhYmhXUkZ4eGgwRzVKRUxCK3krZzlsM2NTNDhvWDhVQUl1VXVaMDhna21sN1hyYTlIMjkwVDdveGdzeVRtTGdxazRTaG9uczVDRi9LSk9mS3NNZGRodFhHdWxHYUh5MFUiLCJtYWMiOiIwOTFmODg5Mjg4NWNhZTAyYWU1OGQ4ZTk1YmI1MzExNjgyNzMyMzY2MWQ5MjJkOGRhMTc3MzVhZTMzZTliZjZkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImgvL3JOZldHakR6WklFM0w0R28vd1E9PSIsInZhbHVlIjoibkNtNDBkMWIzREFVTTBDMlBoQytteEJUcFFpNnN0amVOdXMrZEpwUFVMZlZSYWJjYi9lT25nM2hpK1pNek9yUzRYZHFLK2ViZVFVdjhwS1d3ZGxjano0ZUFrbjdTTGtRMDBSZjdvSC80V3V3Yzl6eHVDNW5KRHBUS082TENPWGMiLCJtYWMiOiI0NDc1N2VhNGNmYWEzOWM1OWI2M2NhNDk5ZDkxYjI4YzlmMGM3M2RmMDZhNThiOWVhOTRlZjdiNTcxMmNiM2ZjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "FobvLWkUgZWj_jSn9JQpAn2gdjskDr4wzoIj8qrehZc-1792150698-1.2.1.1-cTg4rtQk1GLUTP_X2UcmNmh.HvG.uS8akOP3wB8edFZ5eVcn8VFpUmdA0.xBK3Cy1UCTMjw021Fe8mwnpX5eE_HMZzS0Zn4QeBhehso4Hx8g6Gxf_5pQkftfDy5cfhJKnkMwaMPjzlYdhuSi6f1Qq3VYDBE4ao3S4t.138H3mDL9E1Mqemf4OBID.YGVjRXZDXPAL8vY_a2AVaINMLpB_Xpc45XLqiXQl.3nsJPXHiqEKDtao4rR8uobTBHYnUUsshz5wJSwnEtoQUqb8cDrer_UA0v3kGbhTEJu69SEhL0Akzfv0jdVBqbeeQQp3ztTcpLlY5yZ.CT7tMDuRESGu2JykkO0WDnVhDZyKg9Qyg0ISXphxH9wcUWk90wbjZyKkbhILobgWdTB.I._3AmEkk5DHZ.5Astq_UZOn2T3PteybDsZXPjV4yNsHMuLEEcW.4e.BXSimGhkDQ3ppxW4KhMAjALyeDIpx9BjFPrMM_FBj40IVxEuDPevEHfI0iJeAxPfoDcwZvjXqdklJyQ.6w",
    "XSRF-TOKEN": "eyJpdiI6Im0xWnp0NTdTMlN6ZU9hcUhzRkNoMWc9PSIsInZhbHVlIjoiWTZSNkQ0ckN2ekN5ZDRiVnRwRk9LNzB5SE9VenBLY2pRZUNlWEoxWDZyTHBteVNHMmxTMkZpeWtXMXRjYXUwQjNoeFVpNzlwZENpZzRSN3RubUQ3enNTMkVpei96Ynp3bU1WS2ZMaWo3UlJ4Mkx5NmVXV05kbXRsblc2ckZuZXYiLCJtYWMiOiI0YzBjZGYwMTI5MmU4ZWY5YmM0NjU1NzA5MWE1M2U0Nzc5ODcyOTE0YzZhOTVhZWQ1ZTM4YjZlZTdjNzFhMDA0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im10OE5xeDFnSFF6MWN3YlpFYmRubVE9PSIsInZhbHVlIjoiNElpbTBDaWx0V0F1cGo2UUdMdDJ6d0R6eWE4Sm9SVEFyQVN1blIvUGZJMElzblg4aCs1ajVWWG0zdXNpdC9Fc2VxVm1Sc2pZSCtFVzA0RitBeWt6TUJJTUUyVEMxSytvR2lON1NzcEF1aVdrbHovd1FlekQ2azFqOUVnMzlQR24iLCJtYWMiOiI4NjA0NGM1ZDlhMzRiYmQ4NjY5MDUyOWVhNTZiODFjMjQ3OGUxNzg1ZTNhN2VlMTUyNzg3ZWIyNzQwNjMxM2FkIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"