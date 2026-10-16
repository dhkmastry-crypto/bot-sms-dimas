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
    "cf_clearance": "bHqGv4NHT5bCsu6RlBpsdU3IdWhfo3a47GN.XJ9sAB4-1792132569-1.2.1.1-6VYD3U8hUQ097g122p1ZA13o75SHThwfREjiiYZh1JFknmOYMB.C0cD00IIjlAdPSDA.H0cbtLsDdXFAtg6uchFivIHqG9lT0wu4Hv5kEejpzfvqTXwFJDj5h1vj.QcIRnsDYt0WemeR9bNIU25sASV66SW_wppPabRdcOauXn6dmE45a93gZGtc5FvOclSqcSIbw5MRu8h0W5dVSNkKvtxYh2ofPuntfsnursZvVdo.nY6PIJ8DkJsooRg3TRQNcUErFklKtCQK7uavvOyvXASS.9OZrYtJ8V1qCGpvgSux0bdhZ_4Oh3FVU9tYGGuEPlHqguSblvarKpvqFza7MkTdpzkc9CPU7EsSWOIIgDgWup4SWFgY02ffzxp0EKpVSOyEqvuJHtI85QFopUO9eCjWeji3rv0XwbEyg02K3o_lDV4.0NXnbDI8wGAv8q9JLwRFMtXbgTRjSBLKQt7GhNHFZGBSYOthe8wxXXBezi9QRUKBA.KhP8s3WzereBElZraKdYJKQxIrG_LP8h0eew",
    "XSRF-TOKEN": "eyJpdiI6ImVXdzNyVUtRK3BKVTBxVERZUFN1OUE9PSIsInZhbHVlIjoiZDhRMEFjbWNyWTFIc2hqbkNnbXl5S1I1NWZ1Smp2NitwTUJOZ0pNOUFCQ3dQbUJIYStkRjlMQXFCNnN2UHBTeUZyMFI1RU9KUWNEa0NFM1hlNnluVkY5Rk45TlBTaU1rL2VNdTJsYU5aN1hYTklEZC9VTjhDS2x0K2plelZ3NzYiLCJtYWMiOiI2NjU2MDE0ODc5Mzk0Yzg1NTk1NTJiYzViMzJmY2ExMzYxMDc1ZmZjMWYxYTYyMDhiN2YwNDc1ZWNjMTY5ZDliIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVPUVF2dHN6TXFhSEFZb2tLVGdFRXc9PSIsInZhbHVlIjoiSTlxVndPZ2x6WGlOY3ZNZmlYY1JaNW41clZxbDNSWDJUSm5YYTlQdnhZb3FLcW5QaXFIZjBNaFNPOUUzZ1VZQ0h4T2JDd1YrN1k4WW5nMGdlQ1dRTDk1R2txZ052ditBRWI1WjhDLzE4YVFNREwwb2pSTmEyZEpScUhXb0VmbnoiLCJtYWMiOiI5NWY0ZWY1YmViNWNiOWZjYTM0ZTExOGJkOGZmMjMwYjM0OWZjODVkNDcxZWQwY2JjYjZkZTIwZmRlNWY2NmZiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "axiklL7iTpL3jZ5wX9mSo.UH.aKOzzZH061KlrNB6T0-1792132588-1.2.1.1-q_VTQjk4brW8GkGhQAga4C34ZnZWwWnomHQZwuf40u4rC5DsQFEzdN5tqHDVkevEr0ZAvStKaVGSRqrkmeRDF2ZBVUrwe6xSG2qwa4_bfQNxZ_P_dz1QCu4Jh5Oa12UY7M8zPB57AS6hr4LUpTMqLZpNXJ._dUVExjgOn.X_.d_uJUmbmLCX3q7.c8WbX_p60mOyXX6J5ySJW.pouOEEqr3N59IatckYWuL8GH8VQjJKKGS0r7nLNIbPSUxX5TtqytNaoylPz_FF3pbJlqYyAh3C7ZG4XNCSvZFjjkhwhXPNVEtPEx0ggIGkNfEpsQIwHIGcJUjS7qgZwR.x5qQaeRHBWIeHCYPEsRHnw0Bj1jDIcQ73ViQ1OkUhDQWHnNxYhHyeYEIVJiNNBWO.h4GIZaxFe.rfvuTMLLjGAuNI5F166X6BI33CnfftHEYdS4RIy9_gdYCjt1golKAwTWB7NTw3.N3PcuiWV2_7vgc7LUJYBMoyhw.KppJCQSn4z3oxFbCfBwM4DDCG0jN1E5nv1g",
    "XSRF-TOKEN": "eyJpdiI6Ik5jUEdta3NSVkx4TDhFdmVuL3N1V0E9PSIsInZhbHVlIjoicE5zR01VMWMxWjNsVldid0owTTZQUjdVTFdrZnQ3MEQ2emYvZmR1aVNkM1NaaGRkbWNuM1NwT3pjV0V1NEt1WlNOWHprUXVkaEZtaGppajR0SDVsajB6eUcxekhtVjlPNVZ1K1NqMDVUemtENjJHWU02WGU4RzdNREdYb1o5cUwiLCJtYWMiOiI5NTFkNjA0MGY1YjUyNjJiYjk2ODcwZTRiMjMwZGFhZGJiNjU3M2M3YzNjZjNjY2ExNjY3Y2QxN2FhOTRmMjg3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik8wbGJPRXg1N3JnaE5UbkgzUFBVOUE9PSIsInZhbHVlIjoiU3Y3MEJENjdYOXdpZmlOQWcvS0NKNjZzQUJHTlFYMzhhZUc4TXhJTmRpZnVabzRON0N6aFk4K0JBZitieWFvSVhmYlRTYXhYUXk2dzJGUk96bGJpcFdEMnJQWjFHejFkUC9SK0loYVdVOHpiZXVpRXIrSUp1NnR2ekU2dzVSOEIiLCJtYWMiOiJmMTYyMzQ5ZGVlNjAwYWE3NzAzYzY4NGEwNGRhYjIzNDBiNWQzY2M5Y2ZkOTdlMmVkNDRmMDVhMDY5YTJkZmRiIiwidGFnIjoiIn0%3D",
}

