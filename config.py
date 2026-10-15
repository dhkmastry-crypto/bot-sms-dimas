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
    "cf_clearance": "EnXu3Mrem0.ZyVfoMYeCqFq.lMxP3cN89BPc1LesiBU-1792043799-1.2.1.1-X947JZviFVpkxogHdUfsqsWsnSIoLYzMRlNuRHw1lsRt6nJ83p.YmkUA.5gRycLGj6l0xL1oKo40pvGM4BuQi9slOkTcOUWX.PdlHArzKk8SRkNM0pmKU.jPYx6T6ef6WMJsjqum7UgfQOU5qz21xH1Kbd5TgpNx_qupTrmDs1gsFj6fSrPvBpytxsMo_m4QlyZfu.UVLjnuLAdbS6vCq2NPqTY5zx_OHtpZRclTAk3PQor8GJwmLA_ijTZSodvCAL8mR8A7MIZNzreGkw0tulBm4_cHEBtVfT6o2_ghLpiavaCiXMo2JUb5OS_voD1gI96TvMa9zu_UaTY3.wJTcPfVqe9Bss6LikRvsz4PPCL.RSJQHd5rbST4a.kxkCeECXlHPNJRrhqhDtFEk6MqlOGwIgfV_sHILnUU5.XRf0WpXOaTgUFnDLLf3qyofHU5t4mmyoYYdFpS9GKBqUeofCdt.ZMwIhtA1427TPNz9MBvFemCNC0n6AWrygGw6HwJQrk8qALlRIiUQLRCgVAMNA",
    "XSRF-TOKEN": "eyJpdiI6IktRRi9nS0QwRVVUeWNOd3hmd0p4eEE9PSIsInZhbHVlIjoiaXExZjcrSHg4TmpwbFowTWVBL3N6Q0h5Q0hIdW9KdEZBaC9GV2ZBWVJhNUdYNmp4aUNOTUR0eFdleFk0ZFRQUlFvT3BtbW5ETXQ4ODhodGtQMWRCTytuM0xXbkpJWXVNNlBwVVo2WHlYUC81bVlaV25CeDV4VklvNlQ1d09OY1kiLCJtYWMiOiJkN2VmNzExMzk1ZWE5MjhjYzY0NmRmOTJlYmM0ZTMzNTU4Y2E0OWRhMzgxNDRhN2M2ZWY5NmE0OTFkNTk0OGU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVtVkxyeEJGUWtFTlZHZTdRWEJQR2c9PSIsInZhbHVlIjoiK2NPc0Qwb25HUEdnVkR4Q040K1hhRFB0clZscWtQVzNXSEdzTTRNWkNldlhRcFVQYjd3MHF4NnQzUTY1cjJ5b3U1RnM5aE1pcElvbGswTktXSzR0bE1vOVExam5pVlhUMk5hQjBjeHU1enAvdzlrazl0K0lwd3lSUnptenQ3ODQiLCJtYWMiOiI0NmNjMzAyNDg2MTc2YWE4OWUxMDdmMThkNTBjMzhkODdhYjBhYjM0NjYwY2E3OGIwYTZhYTQ2Yzg0ZTE4MGNiIiwidGFnIjoiIn0%3D",
}

