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
    "cf_clearance": "VXqW0Q4HEfaDm5s2wHWg4fRv1mg3or4SZzvSOC.Szsc-1791892758-1.2.1.1-3dzJMbTTUv4KnAIQ2LO4KDYrNIjxTl8RfxcSCfxk1uic8XKD_GiyCQqoP6v2oeJ5Zy9IPZLbsYfSoC3j7eTPQDm1sW1RyaC6M1cp2LHtsdCASxsFrsOK7kOyPhnBxTQwWJrzQsl14TAnf0MUR7Yf4M5zIkZEaJ7FokY1lv8wWN21pMt5ksjy.9Qg2URNHOhoSOn7zEULswBVWiRbISArkvMr54nsJhVAuepBVkoTdG6L0qTKTPXXg9O870CQCYESDb0KDhcOJnGC8FrfOPmof7_IfHqsCBU4vymL8PPyWFlgH7QcOzgNqIEjKgcrUd0nhjOgIID9JFzudf35R0xC5Q3jgBa.0SZZVAyDJoqLw2OUk8EUyBuu1UBkauibmEpLC2YvBaKMBbk4ohLqaj_x3ab6a20.euzEj0Jcf0EzgBlKCz7hN6Sbs2hjIODmFl30QfB2EDCX4xzDwo1TTaAqQszim1MPjF6lnPc_o2X0.Gyq25dAkaf95kIetnlGeywiFxk9BAzKbmoJw5yIk4xopg",
    "XSRF-TOKEN": "eyJpdiI6IklGNW50SUFtYVdQQmZEbDg0S1cvaHc9PSIsInZhbHVlIjoibEtqK0MxM21vZTVWVVYra1ZySVJHWWUybWlObzREUHF0RUNnS1Q1YUYxeDJJSDdhcy9xTHV6K3NYVXBQVVBIOFpQakpLQWRIR0g1aTF4NmdrWWZWcVA5ek5mNk53azhxMHRqMkdweHRoRzRmSHRId2JMY1BCcmJpOFRGOEZaNDAiLCJtYWMiOiI3ZDk0YWQyN2Y1N2E3ZTZhZmE4ZjViNGYyMjAwYTNhY2U0MDUxMmE1OTMyNjg2MTdiZmU1YzU5OTFjNmVkNWM4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImI3SlRtYXNnWktVOWE1ZmRSeW5BV1E9PSIsInZhbHVlIjoiVlpOTCt0MFRWTDY3d3F2N29IOGp3WE5Pb0ltQ3dRYmVyWlFlaFg5VUg5a3haL1JPVmhPQ3Q1SFpJNzNIL0szSWN0UWVOak90ZWdLd0dwenhvZHdIV1preDBZTnlRZnhZMlh1OUF0TGUyMXd5ZEpMY05iTHNQZGhKT01XeUNzcGgiLCJtYWMiOiI5NDFkYTEyZTJiZTE2MmY1NzYxODdhNGVjYTM4NTRmZmY5ZmFhNTM5MzYzZjFmYTg4YjM4ZGYwNTY4NTUzZDcwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "RUJ.Rrg8liM3.p1yGe3HRAYt4FfA42S6epxs9ARHAJo-1791893943-1.2.1.1-s36zlcaqsJN9CXWNJ7Yv2JGGdc59sBVWZMZPNpDu05XQYZhOnCRBwPH5TGF1MKeICb554S4m9P8SUh4aYLeVyyoD9GFtCmXpa6JOiaoX03VoyCPrFp2xf_aybiSXY4uzZ8mtD7NsgZ09WbjRTX1XaLVFY2bSdMkaANzHRuUdO7dijAoMkvZ3UvFPsEyDWBCmsxfhjT62Q2zZ4b.B2Q5zFWbkGTo3PkAJx73Y9eHqBn7VuRoB71Sw3ZMIeDXdygC7m0GcjCbhalGgCM42ilYhDEiqEtecocCTRJYMDGxdiRg3FpTBhNFPnrwC9s1RNmR9pB1S53yUgILRCBD_5U.DaUOmY_rnjzVIVbk1inMz6rgb7mYX5mONjqGc0h3Gk2QpJkNi4gvaCo.WJwcA5YgJEwI3PS6tH6P8KEzet9Edsca2KH8urTUxh6aykaIuKecGDfvx3dZ35u.PGYVj379XZBwBEtHAE6rd40K0k2uDfHAdc3y1y9jkAhByc4QutSdycMdAlMRsXOTS0UTJlcdlCA",
    "XSRF-TOKEN": "eyJpdiI6IkJnSW5ncmhzSEdDY3JFZjBTVkRvS3c9PSIsInZhbHVlIjoiVGFCSkluemREb1NBcE1ybVNJV3VaQmZadldZMjhOaVBEK2xOamxHOEJ2MWpqaVVIQWlhekNnd3RCNzZiaHR2bmUySHBpVWp3UFZGdWQxTUN1dHZWMEZkMHlOYnlYZFRicFg1czAyWUdMV1ZDaTFEMFNFSTNvSEZjY2Vkbi9UOGciLCJtYWMiOiIxNThlZjkyMzJjZDBmODM3ZTBiMTNkZmY5ZDVkMmE4NmZhMTBhZThjODc4NTAwNDhkYzkzM2MwN2MzY2Y5MzE1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVpSVR1NkpFUGtFL3p2NExCaXNzZkE9PSIsInZhbHVlIjoibTVDcGRGNWwrUGZEamN1bUF5ZzRabEs5Zmw5M0tJb2ppaVRHcW1QRDNCNWVDZ2x2QWJkZEdqdmNGRnc5dGp4UU83ZHA2VjdndncrdzZkOGh3T1d6NmcxQkhlN3VjSVJvY0QzTWcrbEdMdzZ0ckpYdnI0bkxnVHNZSUVBc3lEYkkiLCJtYWMiOiJlN2NmYWFjMjY0MWJhNmQ4ZTBhYTFkZTg1Mzk4Zjk4NzAwMGFmOTEyMmY1MjQ0ZjEwY2JhOWE4NDhmYzRmMzBmIiwidGFnIjoiIn0%3D",
}

