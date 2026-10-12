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
    "cf_clearance": "_bmW_60LWeliLg5QEeaolddJdzHoaxEvo1DWMjf.oNE-1791831259-1.2.1.1-gYpDZ02RyAB3JyRAW1KFrwnuuUp74CFlsnfSkdkgXeniH4pDKN9HihkhtypJ42mfV3p8eYnUl8pA88Nuzi9TwvL.rZYRyM_1R5P5D9DltKz0YmbTYHxbddFH6O4H4WrIACyPO46Kgk5t2HMRT0IZLZlCZsGKNDvZ2CzFMazJkcO.cjiRrWKA8dHt..FJ51h_.cDMaP7QehmC8wVnFcxFaGMgnhDN1GFIw5FvPVS_r_lPTZ.0RuKUp2Wf.D5Z9rvOAYqOwYQYCMSpRTB4S5LRZbXNuSRxKgvAs4zMVGUhmKzq8QEOCHOqKOm0N_ftbxm_EYrABr8Bg5uYhgIOxiHP1z2TYZex9NsHwPt1LShdTsvUtVa3qLL0GjcxuIz7yWHiNWTKbpwawG52c9.uvXayGgXz17.hiA0JH39aeELZEoWHC2sUtSNurgkmyR5Su5RWI.eh6TO5pGT7p06zFgST3DPs63DkwsFP6bulP09bQ2V77UFKiaNnVf81WYZ.Lyuo__F8_JtFOWMBaY2t7517qw",
    "XSRF-TOKEN": "eyJpdiI6IlZUVDVxVEJ6STJaVGxzR29xT1Q3RWc9PSIsInZhbHVlIjoiTWVXQ25IZ3BXeHJWVG50b2J6Y3dtejNGakZMQnFCcmFSdHBzTjF3bVJOYTdmTUFxSVc3alhpSXgwbXJTVHFuMTZCMG9uVUF2b3lFaVAwcnJxTmt6c0JPeUo3RVZyUDRISldKVW5YUDgyRkdzTXNrcnJuMTlIOE5IaEJBZDhodEgiLCJtYWMiOiI2MDlhZDlmZDk0ZWY1YzUxNWY4MjAwNzNjZTVjMzVjMjkxYzM0ZGU3Y2VhZTk2N2FjNjc4YTRlYjI3NTg2MTMyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InlwQWdNRGdpTm1MT1RMSHVGMGtqQmc9PSIsInZhbHVlIjoiYmE1aGNrT2c4T3RMU3ZObk9UUDhwZ1Jpa1VtWFpHMUdybmcybUVIaFlVd3hnbWN0aEpSVU54dWEwN3hDcnNGYmdwclZIUDZmMmY5MEF0ekFQWmJoZk5vbWZBL04ybHJpSnBtbXVQeFBRL2tVeUFzaWY1R0xKWSs1WUtQS0RmQWIiLCJtYWMiOiIyYWFlZGI5ZDIwOTA0ODBkMjQ2MGVkNWJkODQwMjY1YjM5NmZmZjI5NDlhNzJhY2NlOWFkM2M4ZGZjYTljM2Y3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "K6yW3LrVuejPgKASYBusjfeKNTrdhSkKVCE9.OVCEFQ-1791832223-1.2.1.1-TikmQupySYSXNRaxHrQ_NVb2.wcPWv8.CYtx_vm.wFar0osSPPWWwtR9G.M52nZU1lPoGKm74eCCdla7O4rKeJH.h1VedBVHaxzL2Q4qdvIzIhGJOgLkkm9CqRGKDIQi0kn.6GCzkiuUYrBh4.t6gxRH.b4QbQWJd5L_e9aTahJTvV9f.4GnKn3c3SDRNVbSLpjJ4XJfIwpNE0mfZCfygSKH_AbT.JpTvarU5P9Uxzr0I0LBHSeBKZnd8wIshvikFJKuVUkgJtOPP8evi2BohUlaX6MjavXh.824_zJ_dbBoxGfiikECpgKSvRh1r9Vb8JnIYt7p9eRqEMe4vYMDD8qtZUiWwCtilw1IV6hednj0Rm9AKYqObWttoHtrFu5ZyGgDB1Tm5VKvyoyQd2v2IhbMT_Zs9hlmggMKd0a0giM_q20bGGMr6szMVa_YJQYh4jij.eiCe6gkozff7IR_K9K0RdzVc0UqRdeAWAlAu4yIASjaNuhRKFcuwrC9altZsBVXjemFc8kT0ZtFIJigWA",
    "XSRF-TOKEN": "eyJpdiI6Ik9IMm5pbVdOMHo5VHZCa0JuM0NNWFE9PSIsInZhbHVlIjoicDY1alhqM2VUQWZ1dUVQektVaHVJcFBtTXRaSWpJaG5hd3RveDBhQnovQ0ZrT052S1FMTVFGcjl2RHFJQmFlSkJwU29pVkhoM2kwSVFqWnlMaXNaWHA2SkZzNjFva1B1SHgrR0J5Si9hRmtPNlgvNGREc1FjWktINGVzSzMyc3IiLCJtYWMiOiI4ZjczMmM0MTYyMzlkNGY5ZWNjZjk3ODM4YTY4ODM3YzE4ZTYyNzU4YjhlOGVmZGFmZjI1YzZjNDdhNjhhMzc2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkdtOWNTSGhybnFYMXB2RUs3STFVWWc9PSIsInZhbHVlIjoiRkJmUUhMOXpyOUlRZTRaSURUNlpsWENkZmNiSDBDdENwOXVDQmxyTms2YTRVNHVoNmxYOEd4NW5scVdhZ253UEYvcmIyZlMwVlNNQkd1d1Vhc3liQXlDL20yVzZXQks0OXNpblAxcDlTeGcwUkNwa29BYWhpMml5ZkkwaEFuR2EiLCJtYWMiOiI2N2ViNjFkZjY3ZDhmYWRmMjM1NGY2NTdmZjkyMjA5YTViOThlNzEyZDljM2EwMDNkNzc2OWYxODBjOTEwODRjIiwidGFnIjoiIn0%3D",
}

