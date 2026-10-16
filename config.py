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
    "cf_clearance": "Cpew.bRr07hVuKU7soGEnry5mEsWscqUMJ67g6dChyA-1792114439-1.2.1.1-jseKC7o5h7xuWakV0W7vjmEw0_RIrsUVwroSLeFV4_aIpaXhtzPkLm6EVYuzO_Dh0U0n_BQ1rmbscX0XI6nxHf0A0LIw6AxwqFIc0L0i77k1lX8VFmYHRdDEzk9xJYA353Re912hwPOXN2FxeMAYL3OK35UTdJiCJ1WHTwE7BAFZoGxhLPsqO4eIMjmpaeYlmB2nnG5QFd09PXMUbMyw7l5LUkHnLvigFNH2.zSd_yeLTIR4Yc_QOStEJ4qQlJ2okqEO8ruU.f7.ZpqFl4P6Zzsnc7tBeVQTtDORtpdaBuc9fCofQoi5j1NtJkW088nRjtw5thskRw9XKvAoiW2lFLS_d4inxQevsARwypHsLXldqBz_TUZZVFCzg5dA87NV1IKsMbvQIBSw9XAGnVRe3TWSlReZLc.xEZL8tLszRUVz40XWyKvcQFl0HlAMrNqmSnnDCUEYW0rVHE8PxC4bj6a.F0gfhay_.taR504.kt0VvNNivPKk__hXWHJ5Fa3SVZAiv.GwXvMAmDhF7trzUw",
    "XSRF-TOKEN": "eyJpdiI6IlkzTVhaakJLZkZ2eGNQVzNBbDBCQ1E9PSIsInZhbHVlIjoiS2xMSkttOXlZS0Y0L2NkRVp6d09IUTlOdTl1VW4vbCtQNm1WMmJRZXhoSGhMb0Q2by9aM0N2ZGdFa3p4d3hYc1hyS0l0K3ZqR0IydG1TUzdXdGsxL0F6NTlmU1ZiSXBBYkp4Zjl6SUt2elVnYWJWL0REdjB2c3VMOHlHL3dQRHkiLCJtYWMiOiJlYzNmZGRhZmZjYmYxZGU3YzUyMmJjZTY4MzE4OWM5YjllODk4MzA4NTc2YWNhYWQ3YTU5NzUyOWQxOTEzMzQ5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZFN25RTC92YzZWTytONzJPR3FSN1E9PSIsInZhbHVlIjoiUTVURHR1OGtUcWZsRFZuUzluVFM4c2EwbGZ0dk1sR0l4eFN1RmEzNWhaVXdIZ2xJa1VDTTVkdGpGMTlaSnlGWEtKSHBvbGxwRS9HcUJKYVJuWFdwUGo2ODVSSjc2U0djaFQ2cU0wblhVWmdQWjdxVEFUbnFmNTNUL3Ixc3R3SlAiLCJtYWMiOiI4ZTg4NDEyOTQ2OWQ5N2U5MGUwMjFkYWZhZTA1NWM1NmIxMDRlZWIwMjUzZDg5NGMzNDYwOGI1N2Q1MzY4MTc2IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "l9lHzy5suHqqHTQOy0EEqJ361JD6.HmDCUNZw_Q7Bww-1792114451-1.2.1.1-iJpcp7xOf8dV34nvue_wuEHbdb2mC74uDQcr4jkEQ_TivO8b8TQZaOLORZSZiKzkJLErmnbJTARWYE8_syT8qc5rMe5IIHYPQT9OrBQlfjzEp.G18d.Czonxclk0JVMWGDK1Wq22PKiee2Vi2PFzu_7vu9cKXdhyGJYKSac9aX4RDWKlS3XA9OX_HZYnzfBdZiKqYNzW92QXWcH6nyfVRsnP7SrvLuh5eTJDvmetzO1WmBTfwiVcfHiMl.Q8XgoOtdVOMknZlB761U7k6UAH3jg0YI.B.Ofp4OCBu4Uomgb.aKkSN5oi9RhJfR6XLOOUF8hFekV7sxnAIM.pkVBPkVhyZi3GTYH2orwwk3HmQrgiq7uR4pFro5Czry7YRcGioJca_d3jkno00DCRpbYU9UbGqKM10aNpSK2_DXk76Y_qQc19NXKY9i6c7pEXrKXVJOH5vPArj7m9ZFKKV3lBoIKUSaVRC0aN4Wj.0Z41JO0lccaAyVza1eTOvXfYgkcTH1qxv_TWhUX2JqAYD1nZqg",
    "XSRF-TOKEN": "eyJpdiI6IllCN2M4T09Zc3dHc1N3bldvTFdRTUE9PSIsInZhbHVlIjoiZTJyUmtTaklqc3ZlRjlDVllZeDlpRm0yYnBwRTQ1K3pHN0UxTHU4WCtaT3FyRC9MKzFtZTZtYXRQRllvSHlIZUtzbHlvNW5SMXNmcW1KQmNIUnp6NG91enE5Q0RsVlJLWEo4VWFZT1J4L3o2LzRyNVMyVUtjOGZmM1JpTjBjYXUiLCJtYWMiOiJkOGIwMDZjNDU5MjA0ODY1NGNkMjJkMDY2NDQzZjc5ODJmZDQyYmNlZmM2ODgzZTQ4NWVkMjlmMDBkYzA0MzA3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9PZDFEY3VFNVhxc0l2a1BSaGFVL1E9PSIsInZhbHVlIjoiL2dwdjVoZ1c4YU1CT25UcjZ5VzlQTlNyWDdsQ3lZVnB5YVhnK0crWVpBdFhuemNtNVlRelpmaGV3dVN6NVFMeVc2VUpwaXY4d1ZqbFlmY2NTd1JhYnJ2WFIzb0ErTHJPMHFRSWo5NjNENGtlSEpRN1FNbmthSFJXUG85UW5SRHgiLCJtYWMiOiJmNDYwY2QwNjczNWNiN2FmODBjOTA5OTk0YjExMDAzMmE3YjI1NWRkOTg2ZTIxZDNkZDAwYTU2ZmUxNjJkODIxIiwidGFnIjoiIn0%3D",
}

