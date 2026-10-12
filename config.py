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
    "cf_clearance": "tv_IX5n0QJZftzrAT40Binhxd0OoeU9rpcDJAZG2OZE-1791833063-1.2.1.1-cLed2DoRDgVTaSXy6J91nbccMf.f5q8VGbmOx77PkL1XuZG2gYpZ0IEGHA4UJTcdB4F1dmqVAv5VFtuV.Cov0kQ1teBz8T7cXlIcdx.AJCBfCbp77kREJBHFHqTY1554u2IGtdTc_EwVv5krr8aYn8o6IMXZmKSbGiIVLK1.xiQ9KtBVqqei3pyCAaC4wBAdOhp05aTmtYeyljdlVMjlv9fJ43OcIXb3k.NgCTnSfmggRllwioIITnWXfbG0C6VMQl7bIXEickyS2ZiXzBtzuFYt2bZcTBe_DjsfLzk1HLjVOc3rqX2Rk5PeNqtzHUS7DGRwZPNYT4N_wj_mvHCcbBPaMzB1Yo11LALVdOBFiLyKH4lko69ypMkssvsxheud_J7HYagAQy_KyWfo8ajGXm7E1x4reV9DJJYW_ZIP1pY2Nn1yT8dLTekh4Caa7EcsM4_OvC5NKS16_VKdub7mQrXh0z16R5NGdOhumXbylh0djiG_D1sysO.8WT_pOXwSlOJx06FGA1E8t2LAMk7_9w",
    "XSRF-TOKEN": "eyJpdiI6IkswdE14bHIvMEFvcnR2U1dSdjhnTGc9PSIsInZhbHVlIjoibWxDU3BVYkJhZEV1Snkvc3dYQmhvQVVMRzNCSXJxY0JRM05Gc1crR3RrNzRvOGlDdkhmZ3VWcXpGc1REakRkWFZKbzd0c1l6d0pud3Q0cWFZRzI5ckNIWVBDZ21rbmJ3VS9VcElMa25hMDJDYVFvcWVHS0NERmE4N3JpVzZicmUiLCJtYWMiOiIzYWI5YzEyODE4ZWFhMGZhZjAwZjBlOTUyZTUzNzE4NmMxNDlmZTgwZTZjMDg1ZjkxZWJjZTdiYWZkZTkwY2M1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlNHbjBtTTVldW94WEg3bWRRM2NRSGc9PSIsInZhbHVlIjoicEhBeGtPL3lhVi82N1lhZXMxU3Q3NWYwQlhQc1hjVDhMNUZRQkVibkZZVXo4eTR5VGdNZXVzbWtEUnZaTWtlZzQrSE1LaWkwSGQrTFRjdW1jaFdFbUVhZEJiVDBvY1dOMUdRTlFOYWRFYU1Kc3p0QnpuNTBPVWdYK3lzZm5LL2wiLCJtYWMiOiJiYmY2MDY2ODIyZmRhMGY5YTQxNjQ0ODI5MjgxMWNhNGE1MjI3YmY1MDZkMWM0MGU1NzRiNjUxYWEwMmY5NjIwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "WExm14F9VMyzXDNMT_X_os6GwhJq.ieLNppGoykGNSk-1791834033-1.2.1.1-L8z3uumVTayfG1WMSOYpDDETnhl6UJRx2fulxXopxPYNN9LluBLWnSJaulTa7dMnXrObTiLhJZpGvSNdlCP0ao6IvuH55rC58q363BxRO0xq5hMTOs.6N6ePdnWSOgAF0KvN5aA5vOM.OVbE.N78LUPkU.Vn_1XZ3BjymLhkHFkBdiIoaGtrfM5nek.MdAo2VPvOTtueGobra1Rp38aqVg_hO5mzyJiR3KyQPAfa19xqMzARQwnBFgzH4TcXtV5MeoGmRlZ6DGnnf8lFGV5RCQ.6vzEn6T0vaoTEIV1zzIrqsYMOXdoHJbGxPLMNilZSp4FE4RHUy8dbCIi_rDQKZEMLOFajfkt4Vn3naJN363JUcQCgpB0NE_zE2rQFwWfwHtQejfxBcdQCKjsb.aftn3Z5FEmHngzdWgVFLsFuKJFhqd.NlVjwmQ0eU8UfBn8D0GOwAedCKWlOcQqFE07GXCdrwxYd7iMv.SdcQG1.FhtNWqbLYlFKD4ry3r1A6hMbC9X7RzjZBig9twthP.q_aQ",
    "XSRF-TOKEN": "eyJpdiI6IkVYbmd6RVFoMzViclVORit3TStmR1E9PSIsInZhbHVlIjoiTVVaRGk3UzljeWFHUXFrVWs1MWZFV1ZHVThTT1pMTEVsbHptS3B6M3AzRUl4cUtFeHJMZjR0OC9aZ3M1VmNkYUg1MVVqNzI2NnVzZGYzQThLTEpQKzdvZjNZQ0thc3RNejVtaC9SQzJDY3FkYkxOdlBlVTd6b2wvazUxZ0hQTk0iLCJtYWMiOiJhNWQ3MmJhZTcwY2U2ZmIwNGM0M2IzNWJiNjM3MWYyZDM2ZGU2M2U1ZTEyNWJiNTc1YTk2MGFiZmYxMzc2MWIwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imw0QkZGcE9QTHVOeElLOGFWbFlYdUE9PSIsInZhbHVlIjoiQjNvSHdqelVlQysySzl5S2syRHQvYVE5QjcwSHpncnpXUW92cjhvRUVkMHNBM3BFMUZHbHBOUmplS1ZLdFkvSmh6cnh0RmhtUVdmaGpOaHhuYW03UHIrWW5kYS9FejVRbkZCU21rNU9rd3VLT1FXQkhBejVhQVZBRGNiMzFXZmYiLCJtYWMiOiJlNWYxODlkYTFiZTAzM2VkZDRmNTAzM2NhYTEyYjdmNWFlNGQyZTUxMmFmYzZkMDUzYTlkOGE3ODI5ZjgzYTAwIiwidGFnIjoiIn0%3D",
}

