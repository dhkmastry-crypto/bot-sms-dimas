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
    "cf_clearance": "77ifC6ZC6pmjzQCy..jxhQ.Ef3fEXrHYXVR7JwmwS94-1791996574-1.2.1.1-b2OT6cYc5ICl1aOkqjDlKq0cTBaU4Xr5n9ENgcNHfeDdLPY4PR8TvXeunka7RJZziCDJHpT5F8ATEufhov1JZBSJN2cBHDNPHWu4AH0hTwubGDyrjpppjFOW2Wyy9SJaxTnZy8oTreIK7J7Ob.MBk4dOu5CFF1_uXQa.nl7JGFrzt3adCMUD8hjUOFBtIsxBftQAQkrge8LOg.AKX4NZ98K5YWcKx2eR0RPwWjwOwUUpkkiCBGcrBjjcjWi.D24bL8cK8Twv0Nok8whpgJcLCi8sbwuH5LEVuFx3WNbJBtoNMKi1Pu6qBue8UK7vicJroH6Y0UgLgG.D0U7zA4.UBZV2R9mT4BxYFIgnMCh97B6h.tdlNYBZYwlhs8vbvS00K4VmGLFn71G7SIg9B03zlJJTZjnfExrQ8.FtcXO.T2oHmFDSSjFm20jmCUnabhbXH3iYZDNQmlBoCk4gLP01BF1PeD8WNrNZZT3Yplt.tnMEK_GvpEH2YRgI6aDk2e66mRI7lhgonRfGbyDp9ij2lg",
    "XSRF-TOKEN": "eyJpdiI6ImhvWEJYRUtzWktOdzZjR08yVktJemc9PSIsInZhbHVlIjoiMUZ0ejd2NGVyZ1ZYSG9HT2RLSFZ2a0wyK3VqclJXbTgzSkEwV3R1Vk0rT0lUTXFiK05lZGdscmoraVpPUnlldmlrRG0zV0F0TzBwVG5IYlA5Z01WZnNRQnZOWUxCOVllT2JEN2szMWV0cEZ4bCt5dXBNR2hrc3NLbTVGLytvYmgiLCJtYWMiOiI5ZjNlMjRhYmRiMDA0N2MzZDhiMDBmZTk0OThhMjM3ZmJjZmM1M2JkYWQyMTNjNGIzM2QyYjI4OGJhOWM5MTgwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFPaFNFa3RNcVBWL0FMYjBKSFlQeXc9PSIsInZhbHVlIjoiWE9rYm44Sk01WW1FUXo3RUlMVkZXTktJZEtNYy93dFlQb1ZJN2w4SnJzWlJNQ0o5Z1d6VXVlRUYzVEJEUUZoVWc1UUI3cTJtT3l4VXBuaXdOdHlOWVVwZW03WndIWWs5MWI5QjVPejRXdFIyWE9mR3c0VUZ1dGEvdXFaN2ZUN0QiLCJtYWMiOiJiNzBkMWQ2NmE1NWE4MzIxYmU1MDQyNWU1ZmU1MTZlMTA4NjUxMDcyNTI3YjAwNmYxMzEzZTUxYzAzMjJkMDdiIiwidGFnIjoiIn0%3D",
}

