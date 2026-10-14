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
    "cf_clearance": "du596JagXKcd4iXaCGF7aPifizZj4VOWN5SeJFff5nc-1792019244-1.2.1.1-y5mtrqh_PhQra1F1GM99RoIr.0YgCo6gRyI1_kGCuxzfu6B6goIxeC.aW4CpessxuQ1Ti9e_z5gwc_cRD_AJiPmbeMWw63gMWeTVFaVO05.sX5HdZxzA92.japxRz4HmMirYtnLXJxI_1_ioYupnyFopjqbqVL1YHv0RoXYjVPNAH4.nuots2drTXJNeNxvBLSNi.SwLgMB9KjY5IivbmFMBgto6QRHTDsysAyj8zU_poQlXG3cFWEGwo586zVijxFrzTH_V5qsOoa7B2yjmV4fRVErmDBIHFMGJDQhEqkvLwJMdQjvMxeviYrXGhCQzojuCElbctCn9vKYqEkL9Sh_pKNMj31Xc0FWT5tM2CffDYlC.7vYPJ3iZVB_Jr9l4NC9ykKpF4t_UGBAnDH4RpjgANM3mogb5SbRkF1RtvT8KZwZpmsnXpeAMl2lUJwb__pKqnC.wd9Ym5GC0yOY9721nxoEsOk6UqA2gYNr0pTHipoYCjdLqc9UBN6wTSFQXiG5fJwKqyLnyii3U5FVHqA",
    "XSRF-TOKEN": "eyJpdiI6ImV0SDA3Zk5ISVpHdlUySjFYMGJyTkE9PSIsInZhbHVlIjoiUzh5bUg1LytWeHRDbHRJbkk3b2s4a09LWWs0ZTBiUUx4aDBJV3J0QXdPdXZyNnFwK1NkRWp3bzlXZGRWQjlaWEdKQVNZdlhuWjdZZTlIemtwc1VFU3VkSHBobVVrRTFVcFExOVFTT2MxKzJNVlVxUGRPencrOFJNMXZCYW9MUVoiLCJtYWMiOiIwOGUxZjk4ZWQ5MjczYTdhM2UzYzIwYjI2ODk1OGYxMWY1NzE5NzM4ZjBlMzdkNWQyNDM5Y2YxZTVlODMxM2JiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRjOXZ0UEJFMGNLN3g4QkcySVNpWUE9PSIsInZhbHVlIjoiaVd1R0I1c0V2dWIzRHlJbXJpL2d2eURtd3F5YjBhWmRWVjREZkpFeVUxQ3NqSnQwR1BCZUtldTI5cExPNGIzbkRKYVFaWUYrSkJyOEtNWElyQVZIZjZMdVNLaHZvdTF2bkNaUHNtSWFjbE93NFZnSG42eGNwK1o3QkdLUmNMbTIiLCJtYWMiOiI3M2VjODZkZTBiMWE1YTc0NjVjNWM4YjRkMzIyZmU1MjMwODA1ZTk0YzQwMWIwNTI0Yjg3NjU4N2FhM2ZiYjEzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "XujleGZ8IBJrxX60slLSPpZ5VOaPDAddt64MahqfJMY-1792019233-1.2.1.1-Mi7SgXX1pcNyOi3za377hhB_YqssnLt8phGFEcji_kMEhipYmAKjXUN23Fuz81TKS3SqvhZz3eGnXNMlXBixAlrQZxRqPRRaxp5At9qEEjejX77ekVe1ixictaZDngPVz7t7njBM02cHQoUR_mmsFJKXy25mgwZvQSlqdWylZWFXkPfSimXLfrDw6iRdHG_Syp1Eu.XcXogj0V15FDw1qGMwEi0eQb5suQAulS_zr.BLvKkOE9VwMH1cXnhgg0tXDXLGAg6qWyWI5r29_LozQeIPxzlgQyR3q5GpC30h0Iz7cwkuDhwgAg5E0DGRnAWBOkIVFUfS.uKLT2KQWm7dcLaTkGWBos8othc2aZGoNhWx37SfTKDoprFkF3YDcyQGwGyfo.5WEqTgQ3owTHHdh91P9C1P4p8nPSPNL6VmhaIZ_E4VXyi.M3llKEQeCfeH3U3RRiuhDOQNiJTueKlcejGpVE1z3jXiYyxt4oVrM8psuNpjM3jbWVtA.Q.UU66NVzHGm3lJNpXhZF2fjDEJRQ",
    "XSRF-TOKEN": "eyJpdiI6IlM4K00xR0ZkTGlWTWEvc1dzZ0h4ZlE9PSIsInZhbHVlIjoic1lPNXFONnpoS0VPbmUwTTBGUG9Sdll0a2lYTXdaUkI4NXZBUDBTMXFjQlBGcVIzL0Z6eC9mMnpxQis2bjNrZXRScVpkRXNxUmpwajBlemh2Y2kyUXk0RDE2VkJoRmFjeElwQjFVbkxzSGVvTGJqRE9PSFlyV2NGY0tSVWl5QkwiLCJtYWMiOiI3NDFlMWM1NjYxMzIzOTc5OTk3N2I1MzY2MjU2YTY5OGE2NDg5Y2EzMTc5MTVlYzkyODI3YTQ5ZmY4YTRjYmE2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ino3ODZnMUlSN3pocC9VdW80NkFDaWc9PSIsInZhbHVlIjoiYW1lb2xZVjRuNmgybjlVcXM0OXovSWVKZmRaNER5amhkejZtSHNmN3NtMU9wMDlBU1pUckpEb0NUR2cyQTFYaWFuSCtKV3lyMVoybUUyREZqOXl3V3lQcmxJQmZhTEsrb0hlV1pkZzlPZURocU5hUExwSkc4QXB1OU1RS3l1ZkMiLCJtYWMiOiJlMjI3MWYwNWYzZTZlODA2ZmM0YTM0ZjIzZWZhNjliYjQyNWY1OTY2ZGIxYTk2M2M4Zjk1OGZhYjY1MTgzNjI4IiwidGFnIjoiIn0%3D",
}

