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
    "cf_clearance": "CJEZED41xnxE55huz_9j_SvQlIpY4YY0kLnypu8mRYc-1791892133-1.2.1.1-r7yr7wBnmRLx1XlL1OU6lZHqx3.4Q2l4o_Hl1QyviX1hXiQ1DRuBvUe52SHalAkSdlVJcty7uCRXHjQuqIttMyYzdMUSUsca3nvgS9SQYh6mR2YBFc0hmoqRF1OhBFekubE0ShpeHCsZMZaewd4HJ28mw4PZrQTqhzkVxujqJW1ieN_Yuhp6idSvaQGmq_0.1bOICy1XIrpmRRCLYQQgO5TSaHY7Po.TJL0Otg1u0MG4Fv78IB856sXUpLZqLIoJT_Yx6_Ez0Y8DkeTOVnLoviayhFy1KY0fjRg6cz3pjsR1Tkn6AnuAkBufBZhMns81MEUSPUZk7XDoc1m4j0zKQ9xf2Lmsp.pRORXLB3ETj6C4vfL5ubXVtsNAcUXY.P5EKR3g5isMC9IUFw83ncDN7.QaJUhQJMobhquJSImg8tl5EpzsEYIS94aY3sVh0JMgB.DczpO9UPOmlIp0OnUtMQSXV8LM6g4UxGL8PHfjotf9qqnfNRJydx7j9JlydsZ5wLVNyh8db2yqkXyegTGwsQ",
    "XSRF-TOKEN": "eyJpdiI6Ik1rZEg2RmxUd1JveHoxa2xBQ2hHdFE9PSIsInZhbHVlIjoiR3ZwUnZWa052RFkxT2E0WnBzRndieTZyMS83UkxOeVovY254dk9XTnlIWDBlWEdSN3I5ZWhIc0Yzei9naE41WDhka1ovSUY1Q3VIUVJVSitpU3daWEw4bElHKzdqODZNZ2VacEtkMVFQYVBZS0JPTE1BLzBPbU9zY2F1c2FXT00iLCJtYWMiOiJlOWIxNjhlZTU1OTJiZmI5ODNmYmI2ODFiNjE2MGUyYTE4OWI2YmZmN2UxZDYwYjRjZWM5YThhNjI4OWVhNjE4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZ1Z0JCaXNKWEE5bmg1ZGRGeGcraUE9PSIsInZhbHVlIjoiQ203NEE3TEJSanNNMzBDWG84cFRKSFlNM3pjclpoOU1LVUJTQm13NktUaWVjWE8ra3dNSTZxZkx0U2tpZG9sdDUzbTl2Z0x1dWFDK1dVUnRaTFB1WWFYcHBzTVAvMFlJaTczNFcxZCtNYWFjTzA4TDhTU0tPNXBsOXNDaUhhY0wiLCJtYWMiOiIyODVmZDlmM2EzOTBmYWVkZTFiZDdmOGYyOTkyZTExNTljNzkxOGQzYjYyYTVlMmY2YWFlYThmOTgwMWZhZTVhIiwidGFnIjoiIn0%3D",
}

