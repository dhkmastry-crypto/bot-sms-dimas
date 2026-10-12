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
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "H6Xlbjl6gmTrTDa2uTPFr3oIK0aS1f8QXC3lRq9eyX4-1791845733-1.2.1.1-8wJ3nPjP76.M0UvQ5jlZIuIpoNcWLpbzGJXT8csncwyDLykmqHkaeNlMF5YKLy2Or_ScQ7Mn1AGF0s4Kv5C3SlkJJWJ_SYmsbVn32MP87I5OsKdGDC.9kE4TnyQmsRcsz8lZfPOMPSOM6mpERq._LolHfDLE.gNWWAK9UWbTvkEzHhr4bUXm_NXvP4ILQRBcO3nA4cdsD0NEycE1gORDNtYO.40rRzLEXtxakbrkb.Og6Ed2dlYTypBU2_wM09OqmD5pWWIh3db_EDqkpCSBLauGj4rfqQgTz1T4uaK4I15xaJDK5byYN9noCGKC04KB0wQpEt5acReRmaD3BsjAEXN3vVLWkYcI_hhpYBo4m33t0L2drg33ELTbZl4M5RWPC1VlSEIoyUnJho72fuu3qHvXZR2XFtzV0fYVQCOiI_KyjHbzkdY7a48jQmuXYsgQzLvqlCcnV_.AR4Y027LYljJ_ySZnGVXgQXpLy68kKlbEqzfvvrLXvZa6XfZc3zf3wZltff1aXkyJ7KkQ5pNe0w",
    "XSRF-TOKEN": "eyJpdiI6IlVGWG5yOXZvSXQyTmRidkoxQWxxVXc9PSIsInZhbHVlIjoiWExWSjJGWGpzdUlxMy9EdHY3cnNtUmZQM3pOZDRNS3pOdW0vZXV0bmJHVG95aTdlVEcxVmFOSklNaFdWdjltYmVrM0trTFV2N0NwVi8vNGUvNVlVZ0tlcFJjQ3QrRzZGUXF1bGRlYnZKUzhKSGErQ0kyNlZyUVNOeURDWk5IUHgiLCJtYWMiOiI4ZTU1YTJlYzNhMTZkNGUwNGNiYzY1YmJmYTljOGZkMGZiZGRhMzM5ODkxMGNhZTE5YjljMmJkNTFkMWI2MTU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJicWo1RjU2UEFuSitQUHl4aCtZTHc9PSIsInZhbHVlIjoiQUx5SERMeUxwcFhyV2M5LzdNRFMrMU5wSmV2VS9GZXpGdVNYSFlnaUFBZGVxWC9BeFpMTW9Wb3QrMTBvWXpQbXpVSDIzdElaUlozWHBhQmlQUlRER1FrVmNjM3oxM3hKYjF0eFhXSlRNMVJWWDRnWUpGMGFpbjh2STMwc2NCL3IiLCJtYWMiOiJmYWIzNDFiOTVjMTEyMTAwZmE3ZDUxYjhlNmU5MDlhMGNlZGIwZjhlYzVjYWEzYzFkZWQwOGQ0NDU4OTc4NmRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "hyE_z5_F1r6PTC7s40kQF3m25p5nBjKAe2_onuRcjOA-1791846779-1.2.1.1-zFiV5WRHsdAJOpQeFjP3gDYKOcZAOvoQihuCnnRRCz81JtqlIZZ2u5.lJtgaSE0NbVvTF8bY1DuBkMenBKenlJ8y6x8cHROyFmtkDaycAJByL01b2f93sc9vuPVdy7vjNE1ZEDTwOxho7wKxS87F7OFyI.ymEgi_P2hY6yQX7aPOLZyY4jFy1xWLozLUBgRVOv33LMzv8beTeMNUmyk77VVWlMrj3Tf2QkWP21W8qfp2Eom_8rrePWoVh7DEwD63qVhP303BJ_u_CShhG05lCwKCTPU4vkjYRgKcjUODEUxTqgS1DTmm2xlNryE_wTT8TzqHdw2gFSLbDUvIhbhIkU64QPSmtPlN5HBE5IiCjVdSU4oujUNqXu99byqPf7qwrmyUiWSYrWbumTTlX5WdP8aeAyLrhIw262xWRqtSazfsUDt5L.RJK6LcJZK.zW24clPOctoxWNPZrgmN2xGpXJ1NwEeQkN9H89uYyJWyL8FONjNp_SUsUWpaBvqTifkhHwreSocjwvlPOx4mWyNTaA",
    "XSRF-TOKEN": "eyJpdiI6Iis4MW5CcDdhdUowbjRtV0RsZndmWEE9PSIsInZhbHVlIjoiRmhFWVdSblhSaEhKZnRzanJzUGlLZWNsdmNOckk2dCs1UDluTkdXNXNwT1lFSGlwU0wyK0o1MEVIb3kyQVBVeHJTdFY1d0Y5SENGZml3cDRnNkZCY0Nkb0dSR09KeTdLcjB6NWxoSklzVlBzMzZrckJIdjBkNGJvUDJmSGVPSmoiLCJtYWMiOiIwYmRjYjc4NmY0OWZiMDY1NTBlMjU3ODJkODgwM2Q3ZTA3NmQyNGZmOTE0MDRlZGZmOWU0NmIxODdiOTAyOTAyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik54eEoxNjlxY2puczJndWpUZk1Ibmc9PSIsInZhbHVlIjoidWdwbFVzUHpzQk5wV2JaVFJUdW5JWTQrNnRKOHhMWEI2NVNpTFRxV1E2U2hqYU1GSDVCUmk3c1FmWWhtcHRuOVAwNDRjaW9KNW9tdmpzTnZIbVdIYk04TUpoZ1NoZlpNQjZSYjlnOU01aDZlTmNMKzZNMVpVa1c5WXZkV1BmaDIiLCJtYWMiOiJiYzMyZmIyYjNjNjIyOTg2YmZjODJhNzE0Njc3MjhhMDFlNGU4MjE5YTgwNWVjZTE2MjY3YzdiZDhkY2QzNDQyIiwidGFnIjoiIn0%3D",
}

