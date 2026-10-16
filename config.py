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
    "cf_clearance": "r39vSm5yFDDbdIw3DUfaHN5mO46cXEEKkGOKBOslsgc-1792152488-1.2.1.1-SM9.wBPNvl_fZhrun32sb9K1JFTKEqE2SKhBjnTjAT1AEA7raS4seeFAQkjlOx7n.qGLXHcLLPtjSUz3kHbL4yl6KBbzslN_QtrimL0tqs7fLouLzkstD5mKOmnlH6kytTStrzjnKA1a9kt770MHSAG1zrOPciFKG8JRMRgHBKul2Hc.W5QqFAs5ToDg1mQFLX9Y6KSZcpoBU5AifLMYmVhSqE2jIr7b3yJ316_rtZNdieNixRXYrPm2FkFkzwQOqS0qlp.LTdMdDOisXyoJlQEpb9IFuT028ncEwv8.ntlP_XmjjBpPYxEcxfR.jasKfqjfSU51x1Mm9COiGARZJaxC5tiY7ncHlpfbvTR6b3YbYqVv8.s2ksVn0lL_H6.KL1jZrsaH4lYz.PVWjkWgAR2kyrGYUHGWDtEpHUlfpmWGjzXHPO6nPvbFgDQhtXGY3.422BG2LurscfUX_LyrFGKFIN8LVB.GbViAz4IkG2LSffp43GfkL7hVBV39iA09Utu2qbTYcqmYLgJ2z06M8A",
    "XSRF-TOKEN": "eyJpdiI6Ii9ZalMxWnc3VXFJV2d6aTNZZ3pOUXc9PSIsInZhbHVlIjoiZ1JTelBORXhHNE5zeXpZOVM3cnVHejVPZjJYUnVUNHJ2RnJiUndLdjdzeDlPTWs0SGFlN3M2TWJJV1FQNXBBUVIvM0laWmxIeWt5NU9FZUxYbnpXNTFadzhFQmhEN2p3SlNxK3FocFFGck15eGVZZkV5WENpOGhaMERsQWJwZTYiLCJtYWMiOiJlMWUwZjllY2U4NDM2MDM3MGUyODQ0ZDRhZGFiYTNmNDk0ZjYyODk4ZDMzZWVlYjhhNjI3ZjI1YmRkY2M3ZTFlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjdZcElnVk9oMmZKbWpjZHNES3AwS0E9PSIsInZhbHVlIjoiWExtNnhEckNKaGdEejBUdU1CcnZDRm5GMEswUCsrYnIzWFMxazluSnJrZmx3MkcxenBVZSt4RTlKcE94KzlwTmZFTUlzWUo3bjdHNHpKUkRxZTRiZUdQcWdTc1ozYklyV3c4ZFFncU9GVUNON1BPMFJ5SGlGTXNoYjMyZHU5dG0iLCJtYWMiOiJhZTQxYjc2MzA5ZTExMzFjNzFhZTNmMGY0YjI0N2M5YjQ5ZGQ2YWFlZTVmNjkyMjIzNTc4NTQ3YTMyNGRjM2M3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "N8W7oY_uxd6W9axPScJ9hiRdsukJdh5cRX5svSCP13M-1792152515-1.2.1.1-esikbgTf.dbwlsaXdPvGJBLrsREfj7SR1aaKQW_1Ho9QkoiCyj.ALNL3eZvysyaHMT695sd76zZRBpxUVEjDfllK93B.94xsRY2qit1lBIXoqtzGqXdMgHRGwqTaKCLP5A.IkhPpywUqCwpLXnomO01PjI0HYle5Nyb6YBhhvA_mKdHKrYlNgbTcSFdXCZtryIUDo_c2wjKI5MGpif5jf__QkTUxWfWoUn2K7iDJyj0NG4NUw6tReEoU_MVk3irHf18jw1Wq2sYYyBry93.R2O8R57H8nPeVYPo.llSQZWjFezaQwJnx9Q.N7VZ5SJd5cNQU6PBiBlYxDPP6_S1pkNj7Q7RR4H88K0Ks3QZ6Grp7rYuFRp96_k0PlI_PdloXoKgAiRbtphRXjjz9q7MzRtqkzxxssC3NqMOF2MFjnqX4jWSJIh08tYv6frZlS01P5MpPjxW_CHeudn2kmFZEEPzHMaUHCBMs23GPFUTSEUhStzzd1ijadmwH0YWWqhJWl082QODdqbGvyCmYA7FmEA",
    "XSRF-TOKEN": "eyJpdiI6IlJRa0kxMnFlLzdUWU1Lams0RUl3SVE9PSIsInZhbHVlIjoibW1CclhTK0xHdklDaVlzOVlPSy80WGlZazY3YkpaWENyQTVBTmhLdXYwL29uSExwcWRHck1ZMW5qS05ZdmJ4cG5MMVlLUWxBWWxremtTUDVYSjVBRlR6cjNpVE0relNZMXZBL0JlcG5wb3h5VUpFaG5YUk91WDRiMzh6b1pMY1ciLCJtYWMiOiJlMzUzODNhNDkxOTQ5YTJlYjU1YjY2Y2NjOWQ5MDlkMjVkOTA4MTIyNzlhOGJlNzk3NWNiM2I3NTBlNGMxODg0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVjVXlhNWwwam9tRkgxSHBpQW1DeEE9PSIsInZhbHVlIjoiVisvRnIvZXIrWW9TUGxpRWgzNUVRcDE3blRBaWV5MVJmZlRESkg2SnRXK29ZWDVwR3EvSURmd0RPK28rRkgvd3pRZyszWHl4Rjk4cGJ6blpaaEZTaXh3R25QaStKTWpXQTg5SkpCa01iQWxhV3hEZld5THh5bEhRNU13aFIxTVciLCJtYWMiOiJiYTdlZGYyMjkzMDg3NDM1N2M1YWFjY2QxMjg0YjU2MTE1MDU2ZWNiOWIxMzEwZmZlNzExMjcwYTAwNDIyMDIyIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"