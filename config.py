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
    "cf_clearance": "_p6P_4bbI1I3FWO4k6TMv.AGRDYqxtw1lbdUCU1FR5Y-1792078181-1.2.1.1-rLmQQ5QzbT8oRBgt6TOFTC6CIW0UMtq2sJAfXXxalYzRQ3re3THBltdVXCj0m_qxeYUxZbjPPa7pK8sa2UY__OThveVGGDsH4txjuRf1fFoLajUvoSQsnKpLqKqdCXEZcC1VYKHK5MFPkhibb7Yl65zJ_lidOgjUopLngxO0diEi13xMo9K5Hn.sY.Bm6R_Jqqx4WunD.AcAd36Ehn5CLVHmZ_wuEA8oRRYzi2izqH2nIC2z9gPSH1X6MTPdyWdQQMRwN0b2SuQEtjm75n37O7d8uA2636ChP0jMLFSjTDdTtGoY_q9.ilyVIST8_0IBpw79A2ZVuUX.iYJI_nSp9DIaq.gTCEQlxkuCLSv_5yvAE9cdt3rWG_vDVGa11Pz1lQScqx9nhCLpCXDPTU0KmoEXiR7DegQ90Mqlb42P7Dx_2OI3C3XiXIlracew00Sk0NqVHBk8x6mSvPVfuIEUHFlW0OvK63KvUKV2.a4KwyKqYXjxh0hQiujzeehxSKyZ7Kw.WYa42cmdAPxM47WfjA",
    "XSRF-TOKEN": "eyJpdiI6IjQrTnhpVWtRRVdTd3NTWVBwMDNpNVE9PSIsInZhbHVlIjoiVmJnZU45U2gyRkVqQkdiUmhoK1g0MzUvRW9tbUdZamlhY1hlVWJvVHNnVGp3RHFueGFkbXRhMmhqazJTdjVLaVdmNHpManFGRWg0aWhybDVBNEMvaXZlSWlBMnFQUSthTWpLMExGL1RNU3ZuQldpSjVxRzNFTkdmR3RKckxHOHEiLCJtYWMiOiJjMDk2YTlmZDczOGNmMThjNWI4ODkxZjJkMTNlOGM2NmY1ZDRmMTI3MGQ3MDY4NzBkNDYxNWYyOTI0NTQzODVhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilc0VXNMK0tuZ2FNazRQd25SYWZiMWc9PSIsInZhbHVlIjoiQXRFV1Y3ZWhRR1Rja3dyaW5rQURCMk1pbnZpZ2VOeFFWcEZDL1ZvZ1BlWHpqbXZrUWg5VE43eDlrL25ocWpJTU5hZkdhaldKVjFVK3hBaloxSk5JWEJGRC85b2JvUDJqQzltdGZoeXhkR2I3Z2VDVXJTR21HTE9tWFd5eXRES3YiLCJtYWMiOiJlMWM1ZDcxYzAyOTJhMmQ2MzFlNzQ0OTlkZjY1ZmU1NWE1ZTM1MmFlMTkzNDFhY2E1ZjUxN2I3MWY5ZWYxN2VjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "lPOWZ_L87EWdF0tKEbk8ko_Ma2pMvlO3LWBbc8gJ2bU-1792079943-1.2.1.1-7h_ImafC87ExJrAFnzV_nFQS4Mv5E.Jf.Ow331_KRx0XQGC6nDnXx5DbTdwr9MXYgKCc8HLD1b0Xun62l7xXewnYVSTfgkmVzni7wIrSo4zsxTo9yRzgvLtrmc38poeXH0aiQosTAiGSwYuqjuogz2BtmCOyPzUkDkfVLO6U0A19ghNtVJA0tombqYHoGy96b1UXTq9aNrChownvKLPMORFqEg9Hjbmkg9BlULxS9uX2wvo0B_ckyTlCaL1iCrSUxgWvfLFb37MQzZJUvOLN431DQKovKl9Jix67XMybacXkLvK6LxyQyD0fJJ125acjxxyODO5fyjZ26AR4pShPSXBt8HH9kHzWV5fPtRNowEzInt3hhPiFbmRYb9tv5mmAaR.t1VuF.xEy9PWv7xxQ81HJudjeSRVTDcvbUmr_I0Qp5CPdiaD._GcnqRyA_DC9lfU3G..mKkyjZBS1XX60vH1C4Qi4r10UVyXLd.TcLUnOMOTLXOUi6W96MlWtoVlBx8fmtiUrolMrfm5G2MU6.Q",
    "XSRF-TOKEN": "eyJpdiI6IllIUndmeGFuOHp5cTRrOVJZVEZ3NGc9PSIsInZhbHVlIjoiNXlLTlF5MzNOWlNvdkdON0hmZXhYTXIrYmdrRWc3V25STlFjaUFnbFpnTmc0N1pienBDQmVJZmVJS1ZJWWtEdzJ1V0YvLzYrUThmcHJtdHNtbERGVlZLcmU0TkUzR0xIMHdUZGhHK3VxSm8xMHBQSElpd1hCcmZWN0ZXbUUwa1IiLCJtYWMiOiJkMmE1Zjg3MDI1MDUwY2JiYmI0ODdjMTI3YmRiZGQ2YjdiYjFkMWQwZGEyOTM1MDczZDFlOTExZTJlODI1ZWFlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkhGVmNWY3QrYWFIVVlNSzlpcW5Tb3c9PSIsInZhbHVlIjoiYmF4dVJkZ21xRjdpSk16ejFiWDV1MmdPL28xWWtmVFdGQmhYUUozMFZNVGtxTmt3TnRzYmdtRDNiV2p2eGxpL2NJMm5yMnVpQ0dhU3NWM3FueWtrRlZhc2xNZnl6dUxjZGhCQzVway9qY0w4bjVvZWVyc0hyMUNIS0hibmJRTksiLCJtYWMiOiI2YjYyMmEzZThjMTk2NWMxOTRkMGQzOTA0YjdkZTI3YjYxMjA1OWI3MmM3M2UwYTZlNmJmNTk2MWY5YWE3YmQzIiwidGFnIjoiIn0%3D",
}

