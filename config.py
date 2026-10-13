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
    "cf_clearance": "n9MWQO8iNTmf30407JnSgd.KfKLHPW2e1YADELck_yM-1791878287-1.2.1.1-gBkEXuI2aWsdOAk9LMF1eR4WcKEbkjElcvfDlD4cAwja4neePNu1PElbQB10q2Tc23cA7WjNZwH29vlZrku4dhjTBK95EZ8G.uwQc8DbxGn9hnsLQE7.657N_w8VuuXJy2lGUf4_JoO_PQrjwHCOoLHR0B5XbaVCNDVFZuxQzH2zafzKCkybusLmHwaqQFjf0Rl9.mUN8ABS5_WjAS9CDaZoxAU7nqsI9BI8H5bY2V6jIC02qPWdHSXfSuhXOyRCFy3b7i3rDRLuy6icbnELeGzIBY9PVD4WGyKYbhjuFdIDdTfbntPbFM8vy8nvYnD5s6k4YZ4aqSsJOwLmy9yxUJNLq7mbxAL.zqr9xojTgjPJk.oRoiD62SypbDA3ERbEnddxgwYG7cu1rlW4eJX2rBbaFjiYbTVhxnWBOWZvpfei1RvPa3UlZLX17DcRHaypWE6qMYxFFPsP9Sfe5fBdZRtEXK7EQGt3x9ycFmQxHz4m2AlubW1RvJIxtCN81Z4xlhswWoJpiCHQsyQSMvFVnA",
    "XSRF-TOKEN": "eyJpdiI6IkNpMVlnTVJTMSszNUlLb0lsZllSSnc9PSIsInZhbHVlIjoiRW1ScW90WHREVDdscTd0ME1qZi9QejZpOFdRL1ZEVmtzeVg1LzVtRXl3MnRaOGxEREN4MmFQb0hLQlB0V25GbGNmVUJOdjF3cTZaRmtwUjc0bjA1ZWFKbjNNek4wMzZYTGVRcTlPYXpXR0tHakdWN05QVSt0S3NaVkszUnRiamciLCJtYWMiOiJiMTQ5NGNlNTJjM2E2MGNhYzQxZjVjOWI5MjBlNjJjYjU0M2I5YzExZTM3Nzk5ZWEwOWYyZTIzOWI5MDFlNjI0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhuYmo4UGRuOHZXaE9qcC9nTEtDVmc9PSIsInZhbHVlIjoiYmc5dGFvQlIxV0liODRmQVJOU2pRdlZza0JuKy84RWd4aWE1c0lXNEoxQkNxd2hubm5CYzNGTjhvWXY2bHM4enhpclM1Q3Q2NWdFTW5lbTlrdjBMUEg2Sno0dlIrOS9hRmNZS1czbnZWQTdwZmNaQmFrS2tlYVluRklJUm5Sc2wiLCJtYWMiOiI0ZTJmOTcwZGMzYWM2M2VhMTRmNzA5NDFiOTU5NmMzNzgzNTA2ZjBiZTYxNzEzZGIyM2VlNDFlZTJmMDQwYzRiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "uRoFpUZ4N0U.48knIlDVf38wdfFaJEJkfigotOQUwJg-1791877664-1.2.1.1-UMCJmIlWPg7jjd._KfATDA9AHna55gD.yhw4F.EA0tPnBR6hWum.CoUp8OnDAGjiCQQq8xgETxVcn79S5Kd1FA8M7qFlr7mEmeTuT8fsmUyq6ZUoX.k0vR3W6d9_jpLhFECPK_Q4fxtGSOW25GxMK3i3qHDtZSXOJehzGF__1EBrgvVwKt_wukYy9mFOpMixGrNpeLUT_MNTgylvmm2WA0RP5Ru9tiiR3n864bANsuIfbCQxv.Ia96ik2N_QyXDi__nYCJJx44Js_7sl5yL5lZakarN3jvl_mhP0nG8iCVk4_yIBBmT10S.Qoz01bBztUBowtxW61MbpoSDPRH9eLsaP3J3keXgt0RezgLoiFsb4R9ARz8jn6yhDyWt89.wJTTBSCpIOxmnhKWH9MEQCIC5LGoxpbq7XkUbNEgNkzIyQPCyAiLMIao9ZIkbTPA.riaT8nxyfl.gE78sLGH_pNrbL92.Jn4Bg68nsDDixecIQk4AqERJvomcV5Xth7bY7zT6x4gpAJYH9I18C3GI8XQ",
    "XSRF-TOKEN": "eyJpdiI6Ink2TjdudTdGTTI2OTFCQ0FDMm51aVE9PSIsInZhbHVlIjoidEp6WFg1bjhTaUlDL3M3WkVyOEFFZW93d3RPQnY5MFkwL21iMTFUMVlrRFk4aDhQZVc4RXdYdzIxVm1mc0lLMWZNbmE2SlpUWlFUb1R4aWpYeEt0UkpFR3Z5YUIvOGNTMUcwM1dRVkJUZlo0U2ZzZlZJaVlDWnpvTFpib0MrMTAiLCJtYWMiOiI1MDg4Zjg3MzdlNGVmNDk5ZmFkZWJmZDkyYmIyMzAyOWU1OGVhOWY5MTk0ZWQ4ZjViMjUzYWE2YThlYTVhMDMyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRNTkppSXgxdm9NZDltOE83REErYkE9PSIsInZhbHVlIjoiZ292ZzdrR0EvdmZEUkdvTi9ORnFBT1NHMWhsbHUyY3ZPd05kbjIwUFQ3dFNSNTRvOWozZnNIeEVCblRocmlTbmRpd0tzKzVmWFZrZThiM0FvVHZYYk9DWjJDMXd6eks0WGxnV2hrVUV6UllHSWd0MG1RS2s2UlVubnYrajNvYWUiLCJtYWMiOiI4OGYzMzRjMDc0MTE3OGY1ZjAxZGYzYTNjNWM4OGRiY2ZkODRlZDQyN2EyYzQxOTJlYmIwMWQ2ZTg3YWY5MDJlIiwidGFnIjoiIn0%3D",
}

