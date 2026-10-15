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
    "cf_clearance": ".VNoc8ySnggaMHhQaYDwOEiqVMMAd2lqUtpeL4CBSBA-1792043842-1.2.1.1-.9ygW4C5qbeTCb915LXRVU5UNc1YnUip6bSFRDCQXE729jFmFHyjF37qW.UabToa_QkBIXWs_49AWdKKQol__1ZE5nZfJKLM14blssNdD6mkhPZLXBy5D2gpvlwl_tPu0_mBqljPIKx58Kz6Ll85PtuU43De_Rb0Sw6wP_KY2ivX9pPBWy7qtlQHEi5fYhotbZ9ark8UNE84XLHlzs7I1aFoy883ctGOWMiu2iqbAFwwS5VfHwRngY_nJpXlHDLvZZVzrGRxZ7XBng4ziOcKS7i91l_pTPlPBXXZ6.coT9JXcHuOHuH3Ck9fHJ8v7TI4HL7iAbu71MV2mCzUreyYcu3m9qC2qQKgD43.JWDimt3S1N2rV.D6ClhVqkqJ74V6poChXrA2OCYtSn8RKYK1SbXkrZsS12nvpWIJ5A1sxywWqWTebZd7CRtW675mAPMfCmBkhd_niUkqtm.TDM78PgW5.H7g56HhbQBnMsd4aotRlXkmrv6gpz1H3D.4pHTc1OpxL3PIRIYKka_GoQw51g",
    "XSRF-TOKEN": "eyJpdiI6Ikw2T3Z0Q0NLRGNpM1E5U3BPVkViTUE9PSIsInZhbHVlIjoicW5IZGk4cE5admhvNnhYSXp1dVlRVTVlWml0RE5XT09NRGx4eENHd0YvRnZiQTIrdjJuRDVoUnIrM2Q3dm02TkRQaWs3YytpTUFTTm1DTEJabGkraXphNEw0Um5rT1ZidkpqNlF5eWwzWkc5bzErcUpDcmFhd0hSQmZEcnZCcDgiLCJtYWMiOiJiOTNiMjEyMzA4NTBmMWI2Y2YwNTA2NjhhNzhkYWNjZmNiMjVmY2M0NzQ2Yzk5ZTdmYjM1MjEwMzY3N2FkNjUyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkNESksvRS9ZSTN6S0c3VXpHZFZhZHc9PSIsInZhbHVlIjoiTjVjczRQcnBoQTVZU0dldDRxeDNtZW40Zlp5N0hIMGgwRkhPQUFEMnhqRmd6dy9MUmFubzN1bCtJd1puMWhKblJXekNsb3laNVpueGh1b2FwY3RWYVk3bHFlQngxenNMOG14MDBMLzJPUUdlajM2bDlRWDUzZVZHWFZvVFJ0VG8iLCJtYWMiOiJkYWY4NzViZjJlMjJiM2U3ZmNjMTVhMWQwNDliMzE3ZDdiNTdiMGJkYzA1NDI4NDMzYTAwYThiZmRiYTljOGI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "EnXu3Mrem0.ZyVfoMYeCqFq.lMxP3cN89BPc1LesiBU-1792043799-1.2.1.1-X947JZviFVpkxogHdUfsqsWsnSIoLYzMRlNuRHw1lsRt6nJ83p.YmkUA.5gRycLGj6l0xL1oKo40pvGM4BuQi9slOkTcOUWX.PdlHArzKk8SRkNM0pmKU.jPYx6T6ef6WMJsjqum7UgfQOU5qz21xH1Kbd5TgpNx_qupTrmDs1gsFj6fSrPvBpytxsMo_m4QlyZfu.UVLjnuLAdbS6vCq2NPqTY5zx_OHtpZRclTAk3PQor8GJwmLA_ijTZSodvCAL8mR8A7MIZNzreGkw0tulBm4_cHEBtVfT6o2_ghLpiavaCiXMo2JUb5OS_voD1gI96TvMa9zu_UaTY3.wJTcPfVqe9Bss6LikRvsz4PPCL.RSJQHd5rbST4a.kxkCeECXlHPNJRrhqhDtFEk6MqlOGwIgfV_sHILnUU5.XRf0WpXOaTgUFnDLLf3qyofHU5t4mmyoYYdFpS9GKBqUeofCdt.ZMwIhtA1427TPNz9MBvFemCNC0n6AWrygGw6HwJQrk8qALlRIiUQLRCgVAMNA",
    "XSRF-TOKEN": "eyJpdiI6IktRRi9nS0QwRVVUeWNOd3hmd0p4eEE9PSIsInZhbHVlIjoiaXExZjcrSHg4TmpwbFowTWVBL3N6Q0h5Q0hIdW9KdEZBaC9GV2ZBWVJhNUdYNmp4aUNOTUR0eFdleFk0ZFRQUlFvT3BtbW5ETXQ4ODhodGtQMWRCTytuM0xXbkpJWXVNNlBwVVo2WHlYUC81bVlaV25CeDV4VklvNlQ1d09OY1kiLCJtYWMiOiJkN2VmNzExMzk1ZWE5MjhjYzY0NmRmOTJlYmM0ZTMzNTU4Y2E0OWRhMzgxNDRhN2M2ZWY5NmE0OTFkNTk0OGU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVtVkxyeEJGUWtFTlZHZTdRWEJQR2c9PSIsInZhbHVlIjoiK2NPc0Qwb25HUEdnVkR4Q040K1hhRFB0clZscWtQVzNXSEdzTTRNWkNldlhRcFVQYjd3MHF4NnQzUTY1cjJ5b3U1RnM5aE1pcElvbGswTktXSzR0bE1vOVExam5pVlhUMk5hQjBjeHU1enAvdzlrazl0K0lwd3lSUnptenQ3ODQiLCJtYWMiOiI0NmNjMzAyNDg2MTc2YWE4OWUxMDdmMThkNTBjMzhkODdhYjBhYjM0NjYwY2E3OGIwYTZhYTQ2Yzg0ZTE4MGNiIiwidGFnIjoiIn0%3D",
}

