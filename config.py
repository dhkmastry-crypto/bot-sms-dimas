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
    "cf_clearance": "Vn1RrQzpFmjC0a742sZLYoVPKvBlg3IR3Qz1mw1HXks-1791931279-1.2.1.1-gyg6VpDW6QCFoTC9S3oRArUcFFkPU5Je_ZoLdXUmLyHWwTtHcO.4oNm2xNN3hTL4npUu4cDw31aDF3xcfp8MZpeo9vaHdxtMeuCmRqai61mNYwXpD7MtpDpv5h.oh4QWF9..rp9B_nFa1sGUAfGcFS0Jexj9JQAU7LJxg5DClo3k_oczUzA80aYncDOvnHYFdqzkBHi.brJvEvTehRcaEAS_VXUimHsNS56xr_BzvumBVl3OoH_YgBHVbYzBwTJiMaD2D7xIrX8OOQv0v1zVXgJCWMVhSZGal5ngz_Iy3VU8Dcf3jCBqnxbiceNNs1ogbD2MsstAcp_DpTEr9BsGBYTkLtgLwYy9kDDLB4ovxNOcJ5ZhQ_7OtWoK._f1ohq2wJ3iPaGRcZTb3w5C1edAvWCLnlzz4peGjsrKgilgiN0EPTKPEveI31F3W1wJs2Kyf92PtkI80sJILuycZ4GmGXSaTXqmz0ZTZIIS5tONKaxtYmjROIfWV6uo3nXwDxe9mcCM3Jnui3dfUeMx2iyZTQ",
    "XSRF-TOKEN": "eyJpdiI6Ikw3eS9YQ25yRnZ5L2RUN1VxdW8yVWc9PSIsInZhbHVlIjoiU3Y2T09XeC82ZGxSR1J0M3JLdVlpRWwzSFlqczNLeDQrTXlnRnNPYS9XSm1nY1IyMldYOVVyZ2x6ajdqTERQSzdnMXVCNUpGeWNzNkV4Yk9NNXJ5dTZ3VStBZGtQMitVNWM4MU4rWDBoOTljOTlINk9JTEpZMnRKTERKSWdaUmgiLCJtYWMiOiJhZDFlMzRiMzJhNTljNGMwNTVjNWUyNDJkZWMyZWJlZTQ0ODEyZWI1ZmU2ZmZkMDUxYjUxZmE2MTAzN2NiMTVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkhFV1h2TmxiMkNxdXJyZjNxd2tqVEE9PSIsInZhbHVlIjoieTgxV2lyUXFIZHRiMkQ5bjFUZmZrL3JDOTkzR1NKbkVGOGtpRUc5TzYzWkQ0YmdWTFFkMFMvYlFIMlZJZm1aSmY4WXNHYWlPTytFV2Fsa0QxNER0TVVlNkpEYzVKNURQQ28zRTN5MldHTGFmUjBlZzc5aUJCaDNveU05NTNiYTMiLCJtYWMiOiI1OTM5Zjg2ZDRhZmM4YmQ1M2FiOGYxNDY0ZWZjMjZkMDY3NTUzNzMyNTc5MDE0MjFjYjJmYjRmZjliMzcyNmJmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "MbTG0GT6bxpIJYkuWWaM.qV3ewDK7VrLU4NvRpQOPWQ-1791931269-1.2.1.1-IyGtngrdC2cyJ.HtsJNPS.9rs_5CXkDmo5JI0pCjT4sm5wW7au_oeGndPrrgIOtIklPYyGzcXp2hKS9UkYcYfE_LhjtqzKEZv1DwN2UT4cUp0h78bCduALaACheRRBIhmEvRodCbp7aZlj.bdgMsFiEPTze0MzncOZt1.ZGzVsQWBl8Hj5KaATk5ZEfAf8k0Bmt5jTL.MNpiz1p2cd_NH2DbAHPQLAcaPB6_YXKQviEmUlROcg02RBJUhG1d7iUlNwU.yYuSSKwu6duK9yhMdiHQB1zil1AW1DZEyIYmoRHgC.2OgR0EAOq5cvUtCB4cO_mH_JNarwpR2JwF64l7Huv5ESL9s1wn.fAqbb43dmdCwILEW_Z_aoB4DrJAHX3eX6Z1gSx4b2Vc4XDZJ3kE5bJIGwLAvULQS9LPfV18ej9pD2PzTEjA3ahUAnz7DM7N9QQYnuEBrg4P4mJbE6PNZ6KD6EmY3BbQGx1B38kQ_fS_CnennsvjV9bDav8.O84Q2UCC6Xp_96Fd_cPNWnQMOg",
    "XSRF-TOKEN": "eyJpdiI6InRuUEx6YXlTVG8rUzBtNkNXREZNY1E9PSIsInZhbHVlIjoid0FsRmNHWWZRMTBuQTgvM2Eyb29zUERoK0RISWJlcVpMOFlKWk5RUTBiNG1CbkFWMFAweXU1eUVmRVpGTjNQN3ZCUlByeTFQSVBMUVA0VklBdmQ2dDBEaTlKcHQ0eTAvM2hjQU1mMVpIVlp2T1YxcVMyY3llSkI5aWhiUnZrck4iLCJtYWMiOiJmZDJiMTQ3N2YzM2E0ZGU4YmE5YjAxZjEwMWE3MWIzY2IxNjg1MjQzMDRhMWY2OGI5NjM5NDFiMTFhMmQyN2EyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlYrQlQvdWxlMmtkSGxVUzNmTFFLR0E9PSIsInZhbHVlIjoiY1JWOWw0OEFMc05xYWlCUGhNUTVQYkJiaXdlY1pQcVFyREdRK0gyL2NIN0pqY3RZM0h6SzA5QkhBWmpOYkJHenFuekR3VzNiSm41d3F0UXpRcERoRnE0MFliVFdESzJCMHhoTnROa3E0YUhVVkJlSEkwMjYzODRjUDdTV1J0VVQiLCJtYWMiOiJkYzNkNWM0MDljOTkxNTY0ZWM4ODM1YmU5YTg5MDU2YWIxNTIxYzE1NGJlNjY2ZGFjMDM3YTgxZDQzNzE4ZDRiIiwidGFnIjoiIn0%3D",
}

