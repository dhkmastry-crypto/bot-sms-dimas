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
    "cf_clearance": "FILcWcj7.8RvlHN.Mw3tWwwyGdfz5t8GeRTWvdpRJ4s-1791918594-1.2.1.1-vqLKfDkRQL877gixZdbC.XzwjIcUH8lcLLv0fA1fHMDagwjRNMUTmmHE91D7JuFQrVobmCNxkcH.y2iiD7mtJNnMHScCioM8Hve9jP6LvbMX6c4MRMzbgwC7NAR3czIXC3MptzfSsESatYJz1dSevPiHks78ZFmVkUFYW36V62WIXI4otCfwx5PL2NBifO69e3LAv9mBSeFRprSKc2EZSMX0JwUlceKJartuh.IoZgrj61wccBBybzQOfhRXBSTkr3ep8ahHZ4UXpC2qVf3voA9sMSe4zTy5BQ_W73ArKBvNHg3FddaXw2GKF6pS3wEnfeG9kcmN2iRTnBYsfHK1wcu5iisn0kAMR6nMlKl5rUugDKXJ4tLE.1gQ5ToXGaF90toGqrc0MLo0wXzfV3iJRSrkZr66uDI9ZtAdB_BSkFm__48PWVKFRdXhQ.yK6etE5KNwc1cvQ_nVFlRRZNlKfms.P8QdrWQPBDbsoNECPzV4p.esl_ASykC1K4RB8VR78f0ZXiZbEOIX2xUe.rZyvw",
    "XSRF-TOKEN": "eyJpdiI6Ilh0cWErMHdjRXlhMlAxQUpsbTVnNmc9PSIsInZhbHVlIjoiYzFFUEs5Tjl2S0NyV21xaVhqT0czbkprYzg5cmFJMklNZ1Y0T3A0cnJxMU1CdXZ2RkFHTFp4R2Z4a25nMmpwN2NJcjZaV0xaYmsxRjFrYkxTRmVLdkZhbFNzVUR2US9iNk9ueUNibkZoZjFKSkxnL1RqZ3Z5cVdraHBYd0pwbjQiLCJtYWMiOiI5Nzk1NzgwOTRiYzgyYTg0NzQ3ZWQ2YTMyNzgyZGU5NDc1ODVmMTNkZTBhYmI1M2M0MDk0OTk3NTczMmZiMTYyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFCNzc3TmV3Y3d6RFJYdkJvajl1Q0E9PSIsInZhbHVlIjoidGFmazI2MEhmRmRwaHpla1YxTXg0akl3WWFmZ3pHS1UyRnYwOGlsa0Q0NVY2WlQzc1dRK3QzZ3lKZFI4Z3lSVWhYNWFPV0t3bHA4Z1ZOUlRsUkw2MlhwYTFudGl2YWRnVXVDKzBiOHFOSUtuRWVUeVkvdGFYNklqZGw5WXdxMXoiLCJtYWMiOiI0NzBhY2Q1YzQwYTZhODM4ZGNjMzUzZjA3YTFhNDhmZWM3ZWVhMmM4NTIwNGVkZDJkZDI5MDcwOTliMjg5ZWMxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "9Yg.LrdmTDIYiVBpnxV7nBV.7vF5sfyo1ER7JPiE3oE-1791918605-1.2.1.1-w4mTT9k7fzMofTebvCOo8tYqNcR8_Ke3v15lbsyl8D1y7DYytaaMljNI81o09c4CPi6gPuEFWilxtbVS5xT7C3LGuBIFT6buniYYrJ_291z68NeA.bx5TWlspg2KoNOzuJfEK5uDU30PDEYfegNP3qzgSuTU79XMoNcrDIcGmPEXmLKNIGiNS0i1ceDmYsvatilO4UGxoS1NpAebDKcFHskseFPOwp851USjqfUUb8p_Du2v4Yyjy75az9.CaQ2J4GwtrOY3xZVyug4PngksYEPY2av9FIeLipuagIrEnkjiOVRDczGyNx36lm0ShY_79QSGsOiQ0oncJOnhLBQ2tFFWDO9WgZfqVK7SNGEan4_q2TKiib6xg9sK3s6.NT5wJDSJQjs87YH2DEqlIwGgvk9cMsYpKg4HVCTY6NWvgiyGJdYHvOYeEl42ngGI34U9DJKE2gUD.DLeTh.RsLhtjEK63u_x7Tua2xXAXFha.6MQdgx1DMNRxcFQYvcts5_kxkrrSI.NPfQt4oZi0pzsrg",
    "XSRF-TOKEN": "eyJpdiI6ImZmSjJ2bHlUM3FEYkNyWFVRekF4VkE9PSIsInZhbHVlIjoiSG1KZ0VtY1JWWmR3c1NEV3FWL3J5WnVhMWYwbnhqaHZ2V0ZwSFZKOHJNTTM1Z3BISTNMMWhUS2ZzUnhITFZPRWVkL2tqb0hSTk5uODhmVVFjZW1jSE9OS2FadDlaZEFFYUZLcE5IUFRUdjVSeGo3QzJ4OWpiYmRkd1BnQkdwN3IiLCJtYWMiOiJmNTFiMGY1MWFiODc4NDcxMWQ0ZTk0YTRlMWRjNzhiMTA1MDYzNDRkNjg2NGM0NjljOTVlYmVkMzQzZDNjNGJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im55TVZ6dnJ2akdrUC9jOGhFWDE5Q3c9PSIsInZhbHVlIjoiWTNDalRLU2R5a0s2YUVjKzhzVnl1eVhGbWFXTzRSMkZuUDdYU0tTN0oveStySkJ4WjQrL2E3QThaWmdmN2ZSWVF6RUoyZlFLY3k5STlRbFp6UnVBUSswMFRSdFVZMmZXSldwRkdwa08rMmxxSko1ZUQ1V0RaYmxuRnFkWTBGaWsiLCJtYWMiOiI5ZTcxMGI4NWE3MzU0NDdhOWIwYmFhZDAzMDI0YWUzMmQ3NWZlM2JmNDgxNzU1MjI2MGRjMWJlNzM1NDBlODhiIiwidGFnIjoiIn0%3D",
}

