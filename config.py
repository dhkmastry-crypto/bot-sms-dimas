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
    "cf_clearance": "PaQZbAKAaMqYL5_Jo1tp7Vg9Hb7YrRhS.l2BtYps40k-1792065534-1.2.1.1-.fGey94ncq8nNeEDdb8GY756U0hE_ywqV5vekdzQSt6AeY8phrQrgD1Knjf1J_am7zOhT1UC9J2FLmn6TW0.eNlUtG4efFvZyur0bC9W91G0FyBI1x2QSjm7VRG7f.MB9taVpWkjYVs4U..AcRFqEPu5VZXKqiyFlh8Nu0d.Bfbc2JIv7SvptXHUCEzarnePVhcHJ.ofhIWc9WOA9sIdGNfGSg5JOPmQv8sYayEpVoeLfc36xfs6MS6ito.o27KrCF7pVogk5os1NCT5b7xUEjzpBpLr1Joa4X2Y31s3yXr1xN.yDuDgoRyB3k8bdtKhzPdQ44tmHVKWqYmBzAoDhj3_lxV2KjiWVmRK3FqyNp2pemlW_jD.zzNCL9H0glWU.iwsUkq56_IRtLkgqnC1N.1IAfvUGKqzlN3_ODaHoGz4GWv6dvYIbxsST92qU1zRYbNfa3IB59mY1TcxiUMCiyRB..dhEGzNKPhmbSCQvzlzgQKDW8uugVBSUf4ClVZhHPpTLsekOyw.ARlBqKgopA",
    "XSRF-TOKEN": "eyJpdiI6IjBEK3RTK2ZUNm5CRlFjUzdQUXZKMXc9PSIsInZhbHVlIjoibkpnaTl6Q3NQZ2pSRzBSNG1SUUpVclU3eUtLQzNlcDczcTlSZWs5Zi9ReG9xMDRYOE1ObVFGb0hxQjk2aVAyMjFwc21JSi9zSHc5QmZ2Vm83TUpMMUFJT0VjZHJTN3l2SWFFdWJ3QnVtakJTSzRWVUF5RzFSbVFxNVN3MGlTSkkiLCJtYWMiOiJjZWFkNDA2NjQ0NmZiMzgxM2E3OWQ1ODdiN2IwMDhkMmUyY2MzOGIwZDgxN2VkYmRkODQ3MDA1OTdlNTFiYzJhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InBkdWZLQnRodUdqUmZXdGJiOVJzRlE9PSIsInZhbHVlIjoicWk5SHl0RDhPYXBaMlZLSG9ZYy80TURtR0JTUUg4TlUxcENXYXJOOUFwYmkvY2NucUlOTmJsUlRCMW13clZSNVlSU290ak9iOFNjcm5mL0pXem9lR250UnpOZzd3aGlpU3dmT0lENEpSeVRFcTJXQjBRbUVGclF5WWxQdVduRkYiLCJtYWMiOiIxMmI3MWJhZjAwZDdkM2JkZmExMGQwNGEzZTM4Njg4NDMzYWE3YWVkNmU2ZGY2ZDRiODhiMzE3MDZmMWNkZGJhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "LPL7EZkRG4Tdzu7PL6PplEPFSAyHKa8zGUfWpZDlr2Y-1792067299-1.2.1.1-gefUJDS6O138INP0BmziBEOJRst0eozHaHMh3Q3y9JXTYZDKwbYOZKMGTWLnfGR1_b3_NBimWiWXGsP_EVGASJ3SUYWJQOxpN8jC6TIhpT2VWSM6.shLGQz57pqgLHgqFCNbBYv1yRFQQXi5PJTPEU5ZmjZfgnAa3HsoDWTn9Iax2hTvGurOsCRWV05Ad2hQpDb_kV9.LeN8Cf_1MI3y.EzSY3obn1aDElidZRZbrODFW5OLaSHcSCptMhc0grpVPP29ruK9o3K36zybAANZX2GZlRV5d3dVtztjTrrCrEm2jLNtbA_YUH7ZI1LcQT331eRUHkWRsubKHC1HAJLYw5qf2z7FTeGBTV8ltsmCLhrLWoLLjDG9Mw8q54OyRKMRT7EPZ9I0.4jnRhwYTkgfXIt69yFHSEXpMDEsAJWpMCW0TXp9o3uBaugbE9JsteWpj5j6b3PRVUp5VEGWcnYSQahWUq5mfkn1CdaZLvbb6Ju7Vo8BVN8eVvV6lurovAinRhpbOTDuWhFmW7ksEiq0Gw",
    "XSRF-TOKEN": "eyJpdiI6Ijl0azNEU0hZeGJ5VS9VSFFkVzZ0dkE9PSIsInZhbHVlIjoiRTJkMXFuN0ZDL3hJakx5amRaUm1zNW4wcmNBTEVGOWFiOHJTeE1Jei9kZjNrL2l4VWVRSUdjLzBmSkR6U1ViYjN1d2xFelA3N0wxNnJjYU1adHZNUG8rLzFiQ2ZyY0dDMXRvVzBHRnpRVEU3YWxsVTRTVkJQbUNURng0MHlZbHAiLCJtYWMiOiJhZDE2NzlkOTkwNmFjNzY4YjIyNzY2NDk4NTkwODM0ZTViMDdjYTM5MDAwMWRjN2Q2NGNmMWEyNjEwZmI1NDRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlUrQ21GVkVkQ0lONysvbkhYTmgyalE9PSIsInZhbHVlIjoicHRBdE5LWG5SVUhhQjljcHJiMTRSN0ZZclVEL1YyR1EyRHNEOEQvbC9ZYy9wcDlDS1BMU2h1NEl1S2U1bTRqUVZyYmlQb1graXVPUjByR1hmT2U1WkYzNjVKOHFMNTI3RVRqT1NGQTZFdjhwSXdjT09OeTFicmxya2xnTVViVlQiLCJtYWMiOiIyYzA5NWIzYTJkYTY4MjQxMjVmOTQ4Mjc1MjQ1YjZhYTgwM2U0NTk5NmQ3YjkzMjhmMzJlZmFjNWEwNzc0YTRlIiwidGFnIjoiIn0%3D",
}

