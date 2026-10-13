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
    "cf_clearance": "ZGvyh_PC_qeSORLHzYbOLgcrMA3cjegOFgJ20tIuB84-1791879470-1.2.1.1-fMrr3yK3oJ52OGh6ZFK4czUlioPg2tIyaDaQB9iy8RLvwQIlEQ0d3rlZKUZQPwK6AKY2XhVhayYpotq3bhbRcS4ZQzt5KMCg1VbdRmkX6HLBIe9fDgTvGoEKzyZdZgo2gLKL.dgxqyYQzRpY2iNwEsVG0Fp7dHaqcOUgCm5ybrLN9fy8a4ilNGryV1vMHGRBT6wTObN1n2PpjtJmC.l1Kaqg5ljL0nXOR8CL.JgxNXk27hqRaVZMXbp8fQ_Is8sNBR0Da6GqarAUEVWC4LRYNVz8LcdPoFBWzR9edROQFYGj8leXfjvBXna_sxe5XXDEXfVGA6UKQH8_D_T_zdBDOL_6RxOSC2eJHOVqB.jInPXOFBiFuHBNNJxTknl7sJ9X3RrDRye0YMYRsbtBAhATqSt.hS7Tynm2w4KChp8rs1Tjc7cvlLi4.mjSovAylMoSjaEe09iNz7Dguo_I6lmP6gHukPmWGtUguZPgkcViKfp4qFfXM.HQrBW82BT9W78V2t9fo.mehTI6Kxq1KJGR.A",
    "XSRF-TOKEN": "eyJpdiI6IlRrR09WRW9Nb0lWSTAvRXhnQVhoR1E9PSIsInZhbHVlIjoiU2pacERoYm8yTDl5NnpIdVFTWjF6RFE1UHZYVnE1Y3N2LzVuRlNXWkZzQTcrZVoyekxjVmR2UVd4K3BNYkhKNFh5ZGhOc2tMMndVNUVaNHVzOFhaU1RGT1I4U200Y3hXUWtBK281eTNoZE9NOEdRd3dxcVkzZnRobVAxck1SUWUiLCJtYWMiOiI0NmYwMjAzZTkxY2FiNDljYmRmZDFmMjc4MjNkMGM3MGQyY2U2NWUwNjliZGU5NTc3MzIyMzFlYzM3NDg2OTQxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJtV3YxUERUQ1ZIb25JamV4V1NYL1E9PSIsInZhbHVlIjoiakYrZWZGWXFMZkVKWmJ5STNJUklYVXVVOXFKTEFNd1E2K1g1ejJCNkJnRVh1WHZJOHphZjFwcDJGUjJwaFUwWU5SSEtJdVhuc0Y3UG1CdnZqY01Xbm8xdzY5RkMzL1RoS2hoY0N1VEc4WnN0Szl5aEU1cFV4NE01b1hTaFR5QjQiLCJtYWMiOiJkMGMzZDgxNjAyNDVlYzEwYmI5NjE1MTJjOTIwM2EzNzFhNGJjMDMyNzUxNGVkMGNmMzI1NjkxZTZmYzNkZmMxIiwidGFnIjoiIn0%3D",
}

