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
    "cf_clearance": "5BIwZYeSg9rZlSXsr6uJCND9UoZpV4ldUAl7vw3mgxc-1792090851-1.2.1.1-mZfjWOJ2u3ezuBLua9qR9fQxt_0Iv.jc2iiKCTd57ossTSbXdh7JODZRLRsh95fwfcA1z7YRSE1pXKOTv00P2Gv4Hs5W8nqigqKPd9dUEXJJrVpTjw.6zMeVAu8a7277Fu_urxLMaN7FDzpyBrpdC4xDDSep.tW0qduA.lyBKVgrWGdT41eU3b7eaccENAeoAFnb15rsnP8sfv5HXLodTveSUL78vMhECfWRM5YxpIvzY7g0md.MveIb5cGJ..T4_623ESRuEnPxuASEey0WeYEZnAeIbqnk74mahm6.pnqO6ogsW23f4jfN8BaiMymveV1NhDBuoTV1eQVCrBXcxL39nEucM3dhckblNXwGpgIuKsnRONLXCx01aiB.tNP3xFrMEAmKGd4oWuomOtI1MV2coNW9ZgP8pHxod9TOaAnf.hOjiECaaQ1MLUjE8T6ElClIqoQbjq3hyiO8Xl0Hl3Kg6ZFQjtQtlwxC8iMhq36PDFobVhVlme_TsMN86da9_fq7ZVn9vTtuO27H_UozLQ",
    "XSRF-TOKEN": "eyJpdiI6IjZKZDk1M3NDRGdoZk5USDFQMEgwN0E9PSIsInZhbHVlIjoiOE1jOUhGZWFSczhnQmRrM240MEpOVzJnZ1ErY1BDVFZVSnhiRkhPc3Nkck4xdmZPMlE3RmZzU2Y3M1BlRkVxVkp5aitVbklvQld3Nmxhd0QvOHUxRFZWK0R3MjgxUkFsWnhZZis2UjYreDJXQmIxSU1QblFjeDRsNThpcHlBcGUiLCJtYWMiOiI4YWJhNzg3MGM1NTI5YjEzOGRiMjQzZmQxMWQ3YzQ4YWVkMzM3MDgwYzJmYzRlNjRhZTc4MGNlZjNmMDc1ZjlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJCcVpOV0NLN0dNcXArT01YR1Q2dVE9PSIsInZhbHVlIjoiYkk3dUY2c1hkaVZ0L25NQ1JNOHFBSW5YZk5Td2NTNXNiVjFvdDZISXdZNmx4OTNMUE5WcGxlT3NvZVhoSUl2ZVRuMWJSdGxnZzZXdk5GUlpCK0piNkRYWUpsYlJmOFhUUVlGZUhEeTBteW9jTURGNGpIaVhQdWVzcFBJSXViWnIiLCJtYWMiOiIzMWIyMzUyYzg3NDFmODEzZjJkMTRmY2VhMDkyZTBjM2VlYzEzMzkzOTQyOTJkNGQ1MGNjZDBjNjBhN2EzNmI1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "alM5KHSWXlBOt3h3cZCyaCnG0MxxLt6lR9eyI3ytJic-1792090809-1.2.1.1-QJpp23jFXMKbIVKm.UZe3YwFa7ahHLaelG5upQVRNjLCDpM8nx1e6MbZYehD80K9TpWyTWOxxLzeDU1LT5PvIVDn8z1TaSTRI8IlbpHifJERge5w7m7zNQaNGkfbrQXJgSXO9GfswkxjOdlA7_3OIY.TNA8S9fkh5FkRyH3b6dlhLA3EMrm2SeDsLEeWuMmleamUxVbETcr9RAFxrASpQRaQYaXFnpk3hPyFWb7gJR2TPRCNNS83vppx4CwsLZVlUv_Mf0VlFPzlETDdGozXbd0b5KNNAE2c3E_S88LFkh6FH1BLHT_zuyut9okgxH2SPDoMe6ah9YWOMM6NkvHxNDbBHLHQORf.Fn3iZcD_QMVlrqbDis3.SD6dCgRQB1rFIXDdQiMwRNH1LTLkwgOHC1JB8XA6iYAMt1mfjH1Uzeb4KYIzZwSz5mv3YoRNAuP3l5Mx41XTX5g2wliO5fLSbHPQGzedPWJ.5BIQlTEbgApCfLO3qCPA5rurbcc0Z1rZyb_Dfptv6z9u29iGkHj3Qw",
    "XSRF-TOKEN": "eyJpdiI6IndHVWZnRkVQenpFenA3aVhKNkxQcWc9PSIsInZhbHVlIjoiZ0FmYzRRdFdRYm43MnBNVlA0Unc2MjhSVFdMUVRuSUkyK0VoU2hYRytCb0ZkcGlxT1FqeTBsMXVYc3IxR0taWFg2SXRqQWhnLzc5Zkx2d0NOSk0wUUZsQlBMcW1UWUFPak9NdnFZMm01OVRxYjBIWGp5anpsZ21iOWxnWE5lUFAiLCJtYWMiOiIwZDg2ODcyNjVkZDc5NDFiN2IzY2EwYWMyMDc0OTQxMzU1ZDQwNGRhZjlmZTgxYTVjYWYxZWNkY2RkYzgxZGM1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFMaGlEdjdFRUJocXFnSFl4dHJBZWc9PSIsInZhbHVlIjoiWjZidFFQM1FSMHNlYmFYNGtVajJ0M0k5Y3RLbzRXdVRpeFh5YVFFOVVrQlE2bXlENk1CcXJVS1ZKZkV2ZnVpWjhjOEdjOTBYYjY5RWNPUlQweWVUWEhTckpsRG5nVmpKbjc0OEdZTjFEZW1FV0c2U0VMenFaMlYrMG5pb296bS8iLCJtYWMiOiJlNjI5OTJkNTRlYTU0MjM2M2E4YWM2YmFkNjJiMWY5ZjA5OGZkODdjZjI0ZTM2ZTBiYmFlM2NiODEyYjJkYzBiIiwidGFnIjoiIn0%3D",
}

