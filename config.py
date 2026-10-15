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
    "cf_clearance": "r8UPx3o0rEea6lN3aH9Ygo.Nv0tW1ZcZfVzPGFyXpsw-1792107201-1.2.1.1-nNLDXPYF9G5cOalvVlu5zQuP9oC4ElmWYbLYI1evA.vJ9z1ORsDVciUZVL04E5fjwm2V14skn82tHBtEYTRTbbAt18b0em7fxZRKYPIubMfxB0jEYQmFB3k_q23lK0wc1R2Lv9yNJccMFs3BNpRkKsSbZSIvnZPKyspPu3Ud_aL7lG4FaoISkYiI45NcX0kPTiET58EfTXKvy_7MJzgPzboMpmnqsZU.SWzWDFfipNlgzh5STX43vacrVmA9dla_sk4vTVfBqy1j50M3Hj3gBDA3vBQmDhxZalZGFHmO.gm2JaPjaDLMFADv6qpIxLbEwzZqQZE1vbBDnqsyMpdH0VxHYwzhl9nmG1ixQv73nyp2vokxPMYEQHBgCgeNIFBY1dCk3sMIrHgYCEj4z7m48p2akGjohFkj0n8KNBlTX8avQqgAog6Zo4nlVMMIbS2Ne9BGg0U0_zssUAvRX0CLI8XFMAe_ufCbivgNporkbs0DHVrZrLtnICmDjHDGIGTZF7nZtuMJc8sobB2K3MXPXw",
    "XSRF-TOKEN": "eyJpdiI6IkxsQVI1MzJxajM0Qk9kejE3SWFtbWc9PSIsInZhbHVlIjoiRHNtQVRiRjY3MzlPaUxTcHBwSU92N0g5OWl1dHkraitLLzJpU1l2SnpYOUF4L3lkVE50L3FJUlJadnZ2M0lQSlQ2UjlTWldxckR1Q1QvSUZkSjVlK3FrNkc1akxlaVFqOHBIRjEvWUpvc00yRDBENlRKVXZTbmJ3U3FiR2dlVXciLCJtYWMiOiI1YjAwZTJhMjVhYTYwMWU5ZjNmNjkwODBhMzkxNTc0Zjc5NGU2NGViOWZiMDQ5NDRiNDliNzY3NDkxMjExMDA0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVuRXREbWRBeFB0UUx4MzcxU1hsTEE9PSIsInZhbHVlIjoidlZMQTBqOURTWEgrckNyNVIzY2poQkxQbmtJUS9IKzdTbzZPL01oR01kRmlCNVBVcHJhdTV6VVJtTDNRRG1JUUhxZnlkeXNkUDNTb1ZhSEJpWFlUU3ZHY0ZvSk9XR3NQZmtzcENDLy9OSVZ0c0pkMHhSbXZmcmMyWmlSNXpSVVIiLCJtYWMiOiI3NDMwM2ZiOTFjNTI4MDJiMzRiYTFiYTk1M2JiYTk2YTkzMDc3NzgyNjZlZjMwNmNlMjBjYWUxNTUxNWMxNDc1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Ky4ww0rfDvlgqBakpG1fn3w54nFltJiKqVQQ8Ka4xe4-1792107204-1.2.1.1-Lr4JKicvjoxCEn1Oj8WsIoigOqgfUp3fpNC0hnj2kPf4ad.cnHMpfyrMtqoe4boJ3eASSf43tV2IvuJE2sH4Im9hSN7JKac7CC1mwtoXRHgRF5bQSHl8czVO2OhrPisXjUqMt7fFvKpGU8VCX7M2ad0B09SCQlLm1G3zEtfcqrZmk8gpWvZNEJpTJ_u0e3qF_RKAm36nP8C0OJEyXif0a9JHshKISfJ0qXHSWdk42ymtkPQTNKaEKwmRkuDXqOvzP2GPcGtNHppSyTp21Z2rrbHRAp2B078Avbno4fHL_SvpafjOAdOEga0NzcKvRtigjjIN9Wcj8CzomT1bG_Awueyzm6tkm2UUJH1_9V0V5dKSdBh1OnHYtswHCyYAjFH_nEXaiXMYz.eBJFhhSTBH5qwzscuSFkABRxwSnVME4GclzOlcQarz2r9dr0z3CKGU0mpUqh1R72xr4rsutEylIsruxhopXMzSLnWCsOWQ7Wa8KrdTTTSitjdrwvaboe6e1s42RZ2FnuPZHtDEGv2qMw",
    "XSRF-TOKEN": "eyJpdiI6ImJUQ0w5Y0d5bGh3Nmc1QTR2Ky9KTHc9PSIsInZhbHVlIjoiaVcwT3FoVGVqYS9jaWRDVWZpSHlKdjdtQ053SGpoUmM4OHhaR2VLRDlHK3QrL3gxK1ZlTFZXSk1ob3dUK1NRNXhzckVlazZKbjFvL21ISkR5K1F4NnlkZjF4dmN6M2NBcnlRZGprdVVULzhSTy9neFZqTkhtZXpWa0lkZFhlM3kiLCJtYWMiOiJkZTg3MjZkYzVhZGZkZDgyNTdjYTg5MTUxNjhlOWI0ZTdlMGQ4ZmZhYjBlNWEzMTE5MmViNzEyN2I5YTViMzkzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ijd2V1l6T0pJS3NkWkdkNEU3dVpnT2c9PSIsInZhbHVlIjoiUmhHdEc0K1JqVmFZcUF1YWthUVVPeG5JNzlNR0s1WVljVnZWUC9GbnhLaG5RK3RmbkZncGExWm1na3o4bkZRYkhLeUVsSkZWeVNacmpXSzFlVDdGUXRadVU1anRUcVNGNXJhc2Z3bGRabzZPeFhHVE8vRnhsRG9ZTkxudHh4cW4iLCJtYWMiOiIyYWFjMjFlZDU4YzE0ZTQwY2IzYTkxYmNhZTk3NDQ2OWQ5NjBjOGExMzJhYmZmOTdjZjY1YzdkMWEzMjBmZThjIiwidGFnIjoiIn0%3D",
}

