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
    "cf_clearance": "tYTu1A2dCjM7EjKxsqDTsFchUifuH97qMkafYTBm7Tk-1792042797-1.2.1.1-Uqgu7WkaUwze47RV9X1fstv7hEw0tv7dq.uy4766DbzwUeLBREftsrkoc0Q9Z3lcfgw8A1UEQ9tKYqgQkVuk4VLiFJyRLy4wUwQXZ0T_b0M5VcPOjBoay2AQ0z_4D2BV1WY_O8ZaH_0YEKo8l6h9Z5Kt9lEkuKeMgDoaeJ2n0Lr2Ctqbr_Xm1G8LZq7qhsIjqrNSxE7X_U0QtkrBUyMr1r7IJwH1RbgRnx_QUCyjH7Kqhwslt1_ARql6UEFkHMFG1Ky8W_lfYNx8g_1QpcdYUqxl3.Ke2s67Y6ksxjrKFuzcXCw9r0l.SC9oX9kK4oczOrKDWBdvR4ME9Q98qjOssGDE_8xVbyLkr20ElnKvK4w9hxxPgo9Nue.ZQ1cQh8W6y5IB_Jox0gaHvpw6XW1Ylj8I5mhRwgHmFBZMHr2rg5kqPzAxhU8UJ6lPmgq.ofMi2w2RKwQSUPljSyELJh73MpyIcOkkfteJypLI8y5Kg1EKTK7DnDFdpjamIASM4zFudc7O8xtrVbrI6SEwAhLcqA",
    "XSRF-TOKEN": "eyJpdiI6IlVQaHQ2d1pXOUJaUXNEOFk2bU9SeWc9PSIsInZhbHVlIjoiUTJiTXozTUR2RjBLaXhWMkt4Q2Zrd2hmWFNBVEMxOGFPM2NMRzdUekxrNG9YYTI2VkVFWHpYcmtaWUlQczVkMk1SRDVOZkxMVU9uZU54eUVXNmplVmZCS0hQdEJ0MVJrYXdaWkRWSEdzc1pOWkxiZ0IrVVd2ZlVWWDBVYkdYUXMiLCJtYWMiOiI0ZWQ4ZTEzMTE0MzVlYjIzZGUyZjhlN2ExYTQzOTk2OGRmOWEzNDUyOTAwNDJkYTZhNjFkOTY1NjA0YTUzZmI5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilp1dDVrTFdIRlE0WlBLVlI3MGR5bFE9PSIsInZhbHVlIjoiYkVnUzZ1QXlnUFVpdEZ4NFdmY1JDMllxWlJzNmVrR2RjN0hSRGxUalErajNZbXJIMnY1TGVoTTMxTlh0ZUNPQzhMTXJWRllUekppVUdUYjNYVkdOUkxOdS91M0hCVWh6aEh1a2QxZDJPMXFFeFBQWXJHcm1RRkZZSy9YNS9acjgiLCJtYWMiOiIzMGUwZDZmMjg0ZjBjM2IyNzQ5MTAzMThjN2M1ZDc5MDBjNmU0YjI1Nzg5Njk5MzZlOWMwODE1MjRlOWFlZWM5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "MCBFpnYRIGbWnOFprblsLnT2_pA0oGEcN5gYTRP8bls-1792042831-1.2.1.1-GpwGZ4MIU7kPt3_TDgKozjLHMHi9UwF9lO7JkzeonOCdUpHE5cy_y9CZvJN3UN15nBByQ5X48rnmV2KChK1IzNg7ZFV8HaLvNfROnHt3cnZOOizp5nbCV55vU_smColuR2AONMbYWzeBuSZHWR1qMOSg_AO24bpeRuVEJCROeDQOovUyqbuzyRgu6Eb0gU37rTuf3iRrI9IAiIGP89NeL8UjQfFIMq5hadVp3S_pifUiFRAJhnhiZnFbXNh9H4pZeAiBmF_ZZJuDuOy_ym_0w3X_Kgb4iq.XoXfSGOrcCThnDpV6xjMHpjhhdfzn1MbpSQDMT9Ksh2T1EbmB6537er1ircBlTEi3Qf8ZQXkdNvfc.DDBYpN_WvzIQgbVtt6oijG5AvTm8cWi9dMeA1frR2eJ6eHX23XitLVsE61vJsEcUvqNkKliMlEr1FAK4Iuk44H5KJsGSFeb_iIjtS1hFurSDBrLJfZ.5A3bpGtjtqdK.L0SYcWJm_LNUBzx5YGkYs8Tl7KFNsL3b8iRuQ6YJw",
    "XSRF-TOKEN": "eyJpdiI6ImFSYnc0Qm9EZUJyb0YwYUdIcHluT1E9PSIsInZhbHVlIjoiSU9BZUJnenlTMXk4cnpQeTJlNThjUWV2THNwTXNMN1ZyeDFZYU5tMUVlL2dSWU9IQk94U0M3bGFrakRhZ3FWcUJkYjg5elFlSzRRVU9YNktDVUtqdEQrMTFqcTU0bWtEWGFkOTFEK1JQUGFUb2hPSlFEZ2lLYzdWcFRWOVVSNjkiLCJtYWMiOiI5ZTVhMGY5MzRiYWE0MWFkZTAyMWUxYmNiNDMwOTk5OWM0MzUzZmJlZWJiMGRkMzQ4OGZlOTBmZGZjYTQ5MzczIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImxpZzhrcVpHYmlRblVRUnVuUStwdmc9PSIsInZhbHVlIjoiSmlBc0xXNG5VblpBa3MrOGdPTDR1eU5GUTMxZGcyQkVoZ2g1eWYyNW92SDlSa1dHdGw0czZ0L01BVWNoTE1VZGZ3TUtjWDFiMGNpcXdxekE2L2liVU1ueGdSeGY3aGR4SGVnK2JmVTVncHdJcytWbHJMNEpYejNJUjZIVVJLUG4iLCJtYWMiOiJiOWFlMDIyYjEwNTQzMWIzODRlYjI2ZTAxZjQ2NGUzNGYzN2QzYzM0OTY2M2UxMGNlMWE1OGFlMDBhMTI0OWYyIiwidGFnIjoiIn0%3D",
}

