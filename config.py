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
    "cf_clearance": "K6yW3LrVuejPgKASYBusjfeKNTrdhSkKVCE9.OVCEFQ-1791832223-1.2.1.1-TikmQupySYSXNRaxHrQ_NVb2.wcPWv8.CYtx_vm.wFar0osSPPWWwtR9G.M52nZU1lPoGKm74eCCdla7O4rKeJH.h1VedBVHaxzL2Q4qdvIzIhGJOgLkkm9CqRGKDIQi0kn.6GCzkiuUYrBh4.t6gxRH.b4QbQWJd5L_e9aTahJTvV9f.4GnKn3c3SDRNVbSLpjJ4XJfIwpNE0mfZCfygSKH_AbT.JpTvarU5P9Uxzr0I0LBHSeBKZnd8wIshvikFJKuVUkgJtOPP8evi2BohUlaX6MjavXh.824_zJ_dbBoxGfiikECpgKSvRh1r9Vb8JnIYt7p9eRqEMe4vYMDD8qtZUiWwCtilw1IV6hednj0Rm9AKYqObWttoHtrFu5ZyGgDB1Tm5VKvyoyQd2v2IhbMT_Zs9hlmggMKd0a0giM_q20bGGMr6szMVa_YJQYh4jij.eiCe6gkozff7IR_K9K0RdzVc0UqRdeAWAlAu4yIASjaNuhRKFcuwrC9altZsBVXjemFc8kT0ZtFIJigWA",
    "XSRF-TOKEN": "eyJpdiI6Ik9IMm5pbVdOMHo5VHZCa0JuM0NNWFE9PSIsInZhbHVlIjoicDY1alhqM2VUQWZ1dUVQektVaHVJcFBtTXRaSWpJaG5hd3RveDBhQnovQ0ZrT052S1FMTVFGcjl2RHFJQmFlSkJwU29pVkhoM2kwSVFqWnlMaXNaWHA2SkZzNjFva1B1SHgrR0J5Si9hRmtPNlgvNGREc1FjWktINGVzSzMyc3IiLCJtYWMiOiI4ZjczMmM0MTYyMzlkNGY5ZWNjZjk3ODM4YTY4ODM3YzE4ZTYyNzU4YjhlOGVmZGFmZjI1YzZjNDdhNjhhMzc2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkdtOWNTSGhybnFYMXB2RUs3STFVWWc9PSIsInZhbHVlIjoiRkJmUUhMOXpyOUlRZTRaSURUNlpsWENkZmNiSDBDdENwOXVDQmxyTms2YTRVNHVoNmxYOEd4NW5scVdhZ253UEYvcmIyZlMwVlNNQkd1d1Vhc3liQXlDL20yVzZXQks0OXNpblAxcDlTeGcwUkNwa29BYWhpMml5ZkkwaEFuR2EiLCJtYWMiOiI2N2ViNjFkZjY3ZDhmYWRmMjM1NGY2NTdmZjkyMjA5YTViOThlNzEyZDljM2EwMDNkNzc2OWYxODBjOTEwODRjIiwidGFnIjoiIn0%3D",
}

