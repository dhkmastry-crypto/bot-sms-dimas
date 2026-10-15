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
    "cf_clearance": "4aPzIHhCeF5hH779ipmmTi3E.fLLgyiR8pIozeLk9cE-1792041015-1.2.1.1-dwqvrgUAy_glkF_.i_BsPePJtkOBCarzyi4gK30mIipWJd0fo2.nu3JzT.HT.HTjDl1WG5JN82ssz.ar8dJc1C6oI5Pju5gvsAmOZQR5bkWKQb.zAp.2.z9rWUc_eAXzBcR9HmMAfpButg6kQg3GaqUpYsu_p3XKd2J8f7kbD2LAaZBln6RJzboreZ1OhFEGEhUBal2ZavHvKLWEgyljTKb7szYinqat.U_f9.e51ZoFbP92LU3Onm7Ua0zfpVZNezxRCpl.M4.6J.hr6xpZN0DfA9liHmXjkkSQo_0DRgQ6QJ9E3BW8LbU8nvtdGQTffaX5.EKFN6Y4GTYeQbCFIuCr3BpWQxfjQrflEjfyC8Q5ME.BChznki89eTGEx5bK9wyXWuFGBKn4pFd1Xhq8emzgKgw3HXJJPr2WPDGd54KTn4Ai5lWxdzWdIk_I5zNaH6dcsuKVZtuwKrTvpoqejhMPJUSan.HJbN_lUMQlHGHgc7RS.15gnPCSdN_SWfjHAGv_HC3qkagSNzCYoKwDPQ",
    "XSRF-TOKEN": "eyJpdiI6ImxTVnpUQzdqM0FiQXhLSWIrWVVGS1E9PSIsInZhbHVlIjoidDdpOFhlL04vZEJJajl1a0E0OVhyT2hiTXpXUXkwVzhSQkRPS0RrNkZnN2hXZldpL2ZSblRJRTRmcjB2M3NFNXgwSFZ2ZGZLU2tBVGdPQ2tYeExXM2pYTFhQV2NjMHNTa0QwcGJkekJicldqQ213a0pIcE1oM1QwNnA3ejk4UjgiLCJtYWMiOiI1MGE1YzFhM2FlNDcyNWUxODlhZTAyNWQ1ODMzYzcwMzBkNjhkMGJjODhkNjYwOTVmYTQyYmU2ODhhOGM4ZjlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9lZEtoNWFHV3FlaTBVaTdDSlR6aGc9PSIsInZhbHVlIjoiUU5RUGtoZm9pQ1ErZVNRZlR2WHozTHBNZ214VEtJc1VQMjlpOFBMTEo1YjNkTHZUWG5XVC95NnJjanl3ZUJTMHZpWlEyTjJwNlNjK3VTTFhpNU8xaUh3R0hVNzZxS1phRGg1K1NjLzlieHVuZXhjOWRreWc4MEpZZTdJcVJUN2oiLCJtYWMiOiIzNzVmZmQ3M2M0MzdiNmRlZWU2OTZmOGFlMjViNjc2ZGQxZTZmNDMxNWUwNjM4OGUyMWVjMzk3MWY2ZGEzMjAwIiwidGFnIjoiIn0%3D",
}

