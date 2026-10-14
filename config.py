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
    "cf_clearance": "2trWk6uhMjVUVJ9sNK40ntND4I.kUU6rl1rcWBEag6s-1791996453-1.2.1.1-HQJfV5ZdVIKwstQGqOmtKRsdMHlOm.YMxAHiajP5WiDxirWyrteBtO6FdU2mmHRyWxF_kOur2dEWK1083zkxhorYyKVQzSh9Up9vY2l9yXSofHFVp_vl8jY5RSvOL3nzGjPhddcuT.wbMHFX3CC9Fjriv5iwCpUiz3nXwDI9tMeFU6UyMSFi420AKiRErEHKD4MYDM73ek2Tb2.ObY87Q9UDb3uF20V6zKAhyexl_YdWFxXsLEFfI0D1pmBpO9R2MqckeVZZNf1wmitK7Cfqw65rYajWxlXUUNNMQVzhN7oDodvXF67cvA.VuhgLWIjIou2HT9OhkxUfX_9MmDxIO_XQN_lUufn2KNkjn7f5wtIdgApeKaXeBMRp.TIgoOp0GFrh21S.wLeYc_r_5Cewtty70lSGHxafIvviJg1Fy5r3JLZxsNT.Kf9pTAC2xczCEZOeqeaXQV6xez04velOf1OUeTMU9UGhpcMq8ImrOmKFwQ5_3FitegbrWLrWlwgBbUb1OJaGfl7dOnFEOLR63A",
    "XSRF-TOKEN": "eyJpdiI6Im12eTh4eFVucndNSkgvT1diY1ZEL0E9PSIsInZhbHVlIjoiNk1aZjh4SXhqZ0pPUWZJUy9QcFZEaGdDOGM3S3VWWm9NQnhhdU9kVmZSWTFPcTVyUmMwanQ1azUwMEtOUlhaSjZkSEJMMitwOTcvTC85UVN2RDYzWGlLUmFhWE9mKzc4cm1ITGhDY1NKSmFjQyswS0pqWkZWWXBwRVdkUGR5S0IiLCJtYWMiOiJhNjRjMDBjMzdkNWQ3M2U1M2JkYjMzYTdmY2JkOTEyNGEwMDA0OTVmYWMwNmYxMmFiNWM2MzFkMzBhMDM2NmQyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBrNkJYb3hpNnd2a2hTdEVQc3kwQXc9PSIsInZhbHVlIjoiY2EybGh6M0ZrMHpmU2pyZ05yWVJxRFQveW1sTWxBKzNsb2pLejVvVUpTMk03aFA2SGh4UDRpU0RwUWZvUWo1U2NZZEJWbkltTHN3RDlPQTNSb1hQRFdwZUJtZE8yWk9IK2ZmTmtQSUhsT1Fkamw3S1pYN0lWRklIYWcvRmV0VCsiLCJtYWMiOiJhNGI1YmMyMGVlNzkxOWRmZTE4ZWNhMzRiYzYyNjhmNDZlYTY1MDY3MTkzMzVlMmMxZmE2N2Q1ODFhMDZhM2NkIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "8FGdUYI5e06b5kaH3z5E6N2eGCx1rq8yVmogDXK8DLg-1791994759-1.2.1.1-lw_0v.gBnlvUEzv.l_Z3uQSTal2AMhY09AbJd050JtzOSUt2UEUhID48cZP8gwjbYBT6LbdcIlHIZrr2UYYfQD_esIBTg5CogmhyDMG_C4Tq8Qo2szpPuJjoMO3pT_wD5NBS8smXG0nNrp2u2EqgYroI8DVEgkv81jEmNB8ZREGdQlj_0t_shB.S1qSEc8jYCGeAa_BVap5LFikcT5mZmqfuVAkZUMnx7um7aJ9yI1iWjESFCWePbb2KBqaWSxJCiL28Q69XPubMSkFAznWj7eZbXbImuGvagifNeFHVcFwUqMH3wbyoUAsXrlFjszLcYDeuz.hUy.PrXIdBe0tGOSEq5ZHQNSbCg5_lyKNGComX2E7opHHiYu_n1CZ0AuL5j8E6_6kfEQ0LhSkjmztlvCwLcE7WfziNJUg9NYbb8nxyGsa8i3SdLOEh2CEYJlqzI322ePWqIyaaJ9GGKGdu8arrv6.ydmr5yQ9i6fG2.TZhat3Z6_lwCEBcPwOJs6pG2QwOk81rGEl5jwjndIBhPQ",
    "XSRF-TOKEN": "eyJpdiI6IkNiR3FRVm55THFFdzBKTkk4a3phS3c9PSIsInZhbHVlIjoiK3cwVURKSUY1a2daTDNTaVdqNFJmeW9xUW1XNERVN3JBaUFUN0hGcmVjcEV5TW5GVTdTa2VIK0tVMEQ1VWJUaXBkWTVtdndib1RwQWhjWFk5cDJtMjFKeE9EZTVxaERLdWF3d0pnbVlmQjlSSjVUWWloZ0x3bGc4YkREa1FhcDAiLCJtYWMiOiIxNjA3MTJlYWFlN2ZhYzc5YTVmNzJhNDAxOTc0NGIyMDAwYTc5YmI5OGQ0YjQxNDg4ZDhjMzA1ZjMxODc1ZTYyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlBMZnFybmtqdlNVbTlaWGxUY1dYTUE9PSIsInZhbHVlIjoiNmRmWk53RENWVTMzZlA0YXA0M3V5aXludnEzWkpOOTlEcTFwMEZmNlpxZEgyU2dWcUZ5eStBNDBtUExFTnNWcE8wSDBkeXlya0planVwNE9ralFjWDdaKzczRGNZc0JidklIM3BPL2tPMkNIWkdhcVlQb1g1Yjd1aURoVlFsS0EiLCJtYWMiOiI4NmI5M2QwYzYyMjRlNWYyYTVkODc1MDI0OWJmMzhlMTQyNzdhYTZkNDNhMWFiYzBjOGRkYmFjOWQzNjUzOWZhIiwidGFnIjoiIn0%3D",
}

