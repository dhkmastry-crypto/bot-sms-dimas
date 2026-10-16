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
    "cf_clearance": "3Uwp_Cxy4OJIys6hh4iG954oTNypgQWApV._pucdsO4-1792147067-1.2.1.1-t4tV0eIFysPtJ2VeFJ7JBP4RZSnwBiWdQgnmIlmtG62wnorwxRGtqXsHE7hw8wA.FPxA7hsJwis4UxwOc3Zs7occucs03a73ANZkhcu5PwWR9zhOoGAipF4tMs2ViN2FifQCVpE6vZFPm13FHQozBEVQugZCTklvvMjfYTV9R98i8FuVOzaDQ0Wn98Ceja0zmb3nRQ441Yx3AHnnE.4gvVOjT2V88p30MPyZCIikIdKrayMGfbjZmIWQN_EFrWejoWQKPlMCp3cUF1Al8PtMvHhGfP35UWfg6m3P7MXC6CGDIoNgxK25Eul6Eqem6QUSeYiRrfe2b_55VREYitP1OukVRNt_suCMcAPY_C8QXkdECz0m42kuFe67vHYl8BXEMGwcjU.PGes.YB.GDa4zHIaiXe9Sl9O0R.1XjHJNfYkU_1sKy9gPO_TzBvsqW8n3kVv3wcFw9E_WL3zhJmwdLL4LIIplFupr.YkPR.WdXd61TuiHpuXc.tAyystqp6K3aGRKjAnJprsdqetzNrKkHA",
    "XSRF-TOKEN": "eyJpdiI6Ik94WVhwY0w2bHFXeTFpQnQxdDgrQ2c9PSIsInZhbHVlIjoiM3hJU0xJQXArV05MelVjcEY3TlNZRkMwOTJPcHgvT2VKbndIejNnZmQrMnhwaFR5MnpUemxZUzlERTkrQkFDUGllL1BacjhYNy81a2NBSTl5b25La0ZGNi9uQW93c2kzQUdVUFd0cUZ0aWVXSlEwWkl5NDJGYlp1UGpQUmVYTHEiLCJtYWMiOiIxNjE5ZmQyZjA5ZmU2ZDE3NTU0ZDM1NTg0ZjAwNmI2NDFjZDdjOWFjMzY0ZGE3ZDg1Y2JhMWM1YTkyNTNjMjI3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhmalZNQWFjVHBlSkg4Mmd2eVJ4R3c9PSIsInZhbHVlIjoiZGZvV29ETjBtL1YwUS80UXFMa2NSazF6Z1FYUlpMQjQ5UXFKRXdSTWFWaEQybVBvZEZZRmt1ME1QVlNoa3NYUStWb1pyS0JPbldTWFBCVTNBYXIrYm8zclNRNGtsL2hIVkt2YVljaDl0UDVhV2lGVkluTTR1M28zTVVMY0l6TEkiLCJtYWMiOiIzMDNlNmM2NjI3YWMxNmU4NzAzYmZhNDM5ZjhkOWViYTI0ZThhY2U5MTc0YmU1NDRkNjQwMWY2OWI1MzI0N2E5IiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"