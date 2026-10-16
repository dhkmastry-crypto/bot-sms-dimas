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
OWNER_LINK = "https://t.me/dimsongkangs"

# Chat ID Pemilik bot Telegram (Private Chat ID untuk menerima file .txt nomor otomatis)
# Isi dengan ID akun Telegram Anda, atau kirim /start ke bot di chat pribadi untuk auto-detect
OWNER_CHAT_ID = "8584584698"

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
    "cf_clearance": "psckvwW1lm2rOVdaP9BfCzsVducYe.DbEVkQgo.5Hmg-1792148869-1.2.1.1-zH7hHNN4xcf_8DsMxJE9GvmtP9Lmfz_78f0dERZ.SACl3wOsmV2dNM2oi9G5BpcWPFWNVI_t3eKvOBL1eNZ59yCIiW3bLOnv0wCTU8GsZwxjWvdYJRoKfJukePpQ0CMb.jrYzokm87.vZ52zZ15hrEmGi34WnSRPm4Z_ciPk2cWQoCd_QbjwOhMr0Ur7sJayUqQ5wkn__3kN24ZAIItu.UKKs6yfZ1XpMG66VEUbshfk08shNMcekFu70m.8CSA8Kzux0P6jsmGqJjXQg9DW2ZKIuwWAlyuZX0NKqwG8MrGMOosoZPA.NaGYcd4XHCf9cT8pm6sOeLxUNfO6KPE2vXoCgIjVB4FBYhdd6JEeTgfywCoo1NC_eUKMAYH.rtKT2hKzzx1mA9S.Uw_C5kJD.YWmiEp.6FYKdyRflhzx7M1I49eurtcWpMR7PsHDrtn6xi5j1D7_87wlsWy0czrbCrqZTi1fhPYhJCqQnZzCiOzD2IKYzHn10yHQ4beFe7mY7hS.koJDazeoAjRz2YKlYQ",
    "XSRF-TOKEN": "eyJpdiI6IndHdHppVEhzTndqaE5OalpsSXp0Q0E9PSIsInZhbHVlIjoiT0o3SHg4RVlsaTc0Yjd5dm5LVkdDM0tiY0c1S1NhNmxEL0Q5ZHhqazE1R0ViVXlsM0lnTnZ3L3gyRlFPVWlKNTlSN0NkT0RpQ0pyZGdBYXl5UXZqSlhBeVJHUGw1QUtpaDNTdmNBVEFqS1pSUW93ak9hTXZvcENicktEZnFoOVciLCJtYWMiOiIwZDFjODcwZGQ1ZDg1YzQzYTQ1NzI3NzA3ZjA3Mzg2NDIwYTNhYzE0MzA4OGNhNmM1NzFkN2ZjZDJmMzYxNDZlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlpRT09KQ0R3WjhWVllQZC9SVkN6aFE9PSIsInZhbHVlIjoiWG5lQjhCWjY4YWxaR21zOHk0cnlEMVF0RTFMcDdscXBaUk5ob3NKZEU0ZWZJTndCYy91L1RHTkFvY3ZFODBVU1JZSWR1V0NwWEpYaFJvYWtyUk5aT2VQTm1aT2xrWEx6ZURKVU9HL2VlR1lKN2piWFJzTmEycERlZFhTWm9kVEMiLCJtYWMiOiJjYjdkNWEzYjM4NjYwNmRmZTg3ZGY0ZTg2YTJhYWEzNzc3YzU2ZDNkNDMzNmM1OWJjNzhkMjVjMmI5MWExMjU4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "KrVi4CNLAcjzeWbwH84DtjSz9RvVZN5RsCu1dDgDVtc-1792148883-1.2.1.1-QNitZQ.v.Syms30LdoAVWiM89sMTtlQeD3FrsWiTrnbnt2cRR7P21LscJ0f8EbOPOqh5ZGi.kbWieRDA9Jg24zETrIYEy.Tungn4pBtA5.gyOOSYcyLR2ewRerytZLcY9LCkUAg.nBottAyDtbSyCcAkmrxlCb_ymmnJbV5qYb0sBzKBbSX.Fi26jux08vkGQ3W_qMjygIszyGR7C1BwD9RhFtBRCrAcVSLAMq0KMcpl70fQKBnUQR2hwxh4ybdmW5efd2l_Ax9H5HQdOcPlO1QQae6iC0Xn0wEOamsyJ9hOwt9p8Vv8CKMKMuM.sPQRK_BHEG.pFC0awu5ypN0TFWaqI4EKWsbi6f_bTyvMKRvcoZOrJat5TVhTJcFERlGQGY04OfhYbPHvsD5P5pqmF0RAxYcUSdBnPBW9viEj95cyEqvf8eUE_h6OGp4U8JVcuojFGK5JSq0_u5CtwkrcMa_MvVo7Ab_wMqSY3m9vWBGdOW7Wb5cjVxAv0QNS55WBNh7kjmpEJbvt9K80dR130Q",
    "XSRF-TOKEN": "eyJpdiI6IjhldGJPZHRQYVFZUU5abEczczF0OFE9PSIsInZhbHVlIjoidGMxR2xhWUtIZ1FiV21XM2VKNXpwMGF3SW8xRVppSzJ2cFVFN0lEbENMaHFqZXB0cEdCdUtBa0NNTm94dUlpaFF3VEtXMEdXeEtlcStVZWx4QUNNdmViVEdWSnNITEhTcktEZ1QvWkRieXQ2enNhVzM3dDkvd29YU0l4YXNzRzYiLCJtYWMiOiI4OGNiZjRmNzM0YWZhMzRiYzFkMTU3OGFlZGRlZGVlYzQyOGU4MDNkNGNmODAyYmUzOGY5OWQ0YWE4Y2I0MDYxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjI3Zk5FeWZidG9xVXo4U1VVbVl2MUE9PSIsInZhbHVlIjoidHFPajZnSlBTcDZDNC9ENklsQy92NGxic0l3YXNUZk93RmtZVCtxZTlTWXd3MkcxWVJualZzaDA4bGdoNEtSNjk4UThjaVA1SW9KUExrVkMzblQ4OTBGdHdhRy9hcHhFa2lzUW1RNjRoUmdwNGp3UnJyWVIvNmJ6L0RLcFYvZ3QiLCJtYWMiOiI3ZDk1ZTUxYzQ2YjIwYzQxYThkZDc2MzdiNTBmMTAwNTMzNTYxZmU5ODVlZTFmNWVmY2Q0NzgzM2MwYmI4Y2YwIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"