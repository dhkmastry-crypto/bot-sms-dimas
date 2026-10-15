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
    "cf_clearance": "D3yCc1z.ERc2R5t7RA.wtQEXHNMk.ExAQQsTrEcAbiA-1792078138-1.2.1.1-5nDJ_rY7pbEnijTHpLVg.wwhQqSJKQHhQNnMgGkSLCIuMAn71.m7hz3IIaLiTBwr5GZ_7aimyM1m0_wi4VWeS.VTAIvsxdoMfMGS5EUw9gmuQIHPW8nXhA7Y5OQRjBCQVW_fLN5nSRay36mFg7MD9qjwNkBmpYWr3fkNeGQKnWJFHnvmN6WigIZQaRqk8Nrxp2uAUlnZOJmTM9iI6tZVKS.HBhyxZJvqSEP4PJ_oQIiibdxmNQS_xKC1_SuirppJEM2Cy32Bh49cnpQfiI4I2M9003DTB_ETFILEjZ6nQ326MuwrRjCa_kViQkNQMcxtESkESu05GDs9g7oQ19BPASD8ytGcM4bishJuZ1tzr9eKGpaDaVmBi_yVLsZ7W5ENNhk8eDTH85jYnIlE1b5bDba_PRqX2BvG6neKaRQR8MqivqwnSOQYShsubqzmkvoxOZbeTklG57699YP5e0DOsGoJLEcg6HP_MDbnAbuQyYomtlbYXvUtEADX1lG13x7MoqvMzzVWmJJlpViVJ6iFKw",
    "XSRF-TOKEN": "eyJpdiI6ImdTVzJJZElIY0NQSk51UnJYbDVQMmc9PSIsInZhbHVlIjoiOEszdVQyUVc0bGh1aUJrUi81RmxlT1d1akdkOWV0RzlzbCt0WFhqV3l0ZVRzTUpHNkU0cDNsQTNpLzVCVTBJSGwyVy9SbjRCR2UyNW5RZjU0YVJmM2d2OTQxTU1DbUM3VXVjL0VCcVVpL1QwbzJwMGh6c1BCd1Q3RkszSEJMa1ciLCJtYWMiOiJiYTc5M2YzOWIwZjNhMjMzMDI4YzY1ODIyY2U0ZDk1NmJjZmJmM2ExNzU0YzE3YzcxZTBlY2M0MDcwZmVlMDhiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlNHNU5HYXk3bEM5R3JTbHdSWjVJU2c9PSIsInZhbHVlIjoiQkxIa1pnSFVXLy9XOVRxWjBtVEdCWklSWU1GYmI1QTJOZ2JSU2FkVCtVekVlVStJZFJwUnkzeEhUNTZwWVdwRmloYW5kU0RvSWRsOVFsY0VGSzlwa2hsZ3puczd3a3FKZy9JU0E4cS9XU1lDMW5qUjRuY1gxQkxVTXlPWndaYzEiLCJtYWMiOiI1M2RhMzM5YmQwZmFjMTAwYTY2Y2U2OWU0MDU3YWQyNTBhOWM1ZTdiMDg2MDgxNGE2M2Q1MjM1ODE4NGE4MDEzIiwidGFnIjoiIn0%3D",
}

