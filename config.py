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
H

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
    "cf_clearance": "u1dRBa1FnT6uFY.Jj02LUuj.TKgFKEWdwmjkuTgZh5w-1792147057-1.2.1.1-QukR01055LgfBGZLiAF86LZJA_mafJMymtQBB.XqM8SIdpJdbpRlRrR3ewK41NOODHkfpgk7tVnwNGaPHPSEe.UX1DBJtwoj3W3qhGfv8ot8kvFGpsFJMAR6lUfpe_ixlvvwK.xILBGCm7kHec0ZYp5RFCQRmFm5yaQZS9TRSMHC6OOLPZVTfO3AhaUnaF16KS8Z7hoBuZcIaBybxVxhRvR1t3jZ78S4LTmDdQ723FK_6eApyShgHF2MdFUdvQ7hv_YSw_chjiVApVrR0XJwvKcRz5.wrDYmjxJTkfRuw0sh35FMMgXIuVQLvvc7_6QZ_Or1CXdEifFh0NcAKDE9NPPEPT3nYnS4mM2Oo658HKI8Nicd.f9kA8AtzidaFxc..TP8u.7nYbfCxRMduhB8h4GYF6mFmrie7FkvK1itoXDklsuOF_1Dj3GKrV90Z_t672LJFPd4NLG5IwBMpiQBHLJQBnWi76vuWfcbYYVsXpG.sUIEQ_qbfsa81iJ7V9Uzqu.cwlawNZhlPM5w83tw2w",
    "XSRF-TOKEN": "eyJpdiI6IlZqd1l0QUxIT0R6ZnVOdnVYQUZoRFE9PSIsInZhbHVlIjoiSzJOMUxub3lxSFgyelZPbjRVeXlnWkJBSFBqTnFCcytxUEwxWkY4dVpyNnlscnRmVTV2NmNWZFRHZWcxRHh6UGxLRGZJellxSmpDeGVUc0hkamI3MjVPV2dRZVhobWQrQkVFRnRmUlg2cjdxNHFNN2VnN2plWWhEVTlTSU5xaFIiLCJtYWMiOiI4YTA4MzRkZjZhZTQ2ODhjNmZiYmY0OWIwNTg5MDlhMmY4OTE2YjY3NDE0OGRmYjE2ZmRiMmJiOTJiY2NlOWI3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IktsemVmNXNCKzBLcHUrQmI5clY2YVE9PSIsInZhbHVlIjoiVVlESlNoSE9rcVMzS2hMNy9HdG5pRkpmWFdPb0p4OU41bmlHUGdtYW11ajlhK00xQm9pK0xkVzZOVlYrV0tjK21XcTNaTkFyaVp3SWJweVUrbUJxczNta2grdHk1YlBFQ1B4WWYrbE8rLzdSS2Z3TE5YWks5UFZTMXp5V2dVNW0iLCJtYWMiOiI3NDNmNzcwMWFmODAzZWNlMmMzYjFmZDcyZGQ4YTI3Njc0YWY4M2M2NWEzNTkyNjZkYjQ4Y2JjZWQzMTNlYjRkIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "3Uwp_Cxy4OJIys6hh4iG954oTNypgQWApV._pucdsO4-1792147067-1.2.1.1-t4tV0eIFysPtJ2VeFJ7JBP4RZSnwBiWdQgnmIlmtG62wnorwxRGtqXsHE7hw8wA.FPxA7hsJwis4UxwOc3Zs7occucs03a73ANZkhcu5PwWR9zhOoGAipF4tMs2ViN2FifQCVpE6vZFPm13FHQozBEVQugZCTklvvMjfYTV9R98i8FuVOzaDQ0Wn98Ceja0zmb3nRQ441Yx3AHnnE.4gvVOjT2V88p30MPyZCIikIdKrayMGfbjZmIWQN_EFrWejoWQKPlMCp3cUF1Al8PtMvHhGfP35UWfg6m3P7MXC6CGDIoNgxK25Eul6Eqem6QUSeYiRrfe2b_55VREYitP1OukVRNt_suCMcAPY_C8QXkdECz0m42kuFe67vHYl8BXEMGwcjU.PGes.YB.GDa4zHIaiXe9Sl9O0R.1XjHJNfYkU_1sKy9gPO_TzBvsqW8n3kVv3wcFw9E_WL3zhJmwdLL4LIIplFupr.YkPR.WdXd61TuiHpuXc.tAyystqp6K3aGRKjAnJprsdqetzNrKkHA",
    "XSRF-TOKEN": "eyJpdiI6Ik94WVhwY0w2bHFXeTFpQnQxdDgrQ2c9PSIsInZhbHVlIjoiM3hJU0xJQXArV05MelVjcEY3TlNZRkMwOTJPcHgvT2VKbndIejNnZmQrMnhwaFR5MnpUemxZUzlERTkrQkFDUGllL1BacjhYNy81a2NBSTl5b25La0ZGNi9uQW93c2kzQUdVUFd0cUZ0aWVXSlEwWkl5NDJGYlp1UGpQUmVYTHEiLCJtYWMiOiIxNjE5ZmQyZjA5ZmU2ZDE3NTU0ZDM1NTg0ZjAwNmI2NDFjZDdjOWFjMzY0ZGE3ZDg1Y2JhMWM1YTkyNTNjMjI3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhmalZNQWFjVHBlSkg4Mmd2eVJ4R3c9PSIsInZhbHVlIjoiZGZvV29ETjBtL1YwUS80UXFMa2NSazF6Z1FYUlpMQjQ5UXFKRXdSTWFWaEQybVBvZEZZRmt1ME1QVlNoa3NYUStWb1pyS0JPbldTWFBCVTNBYXIrYm8zclNRNGtsL2hIVkt2YVljaDl0UDVhV2lGVkluTTR1M28zTVVMY0l6TEkiLCJtYWMiOiIzMDNlNmM2NjI3YWMxNmU4NzAzYmZhNDM5ZjhkOWViYTI0ZThhY2U5MTc0YmU1NDRkNjQwMWY2OWI1MzI0N2E5IiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"