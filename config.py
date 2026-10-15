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
    "cf_clearance": "t0vED6CA7Q9qE_B2UzGpnIpyhUMeiDahxrJXIN.ZVys-1792072759-1.2.1.1-XO1i50jIGd6R.LDQgXK_z4u0U88PmuLyKFm02iRiRZNwKQijCy1TiPBtVN8FJGveA8k0cN4d3XGhj2SwaIGHTT_x.GlFI1lDmW71MwRcf99RC3U5M3DVjjjRzznjKZQQjO_SLTrSLBPG7i5_PWMjy.76LuNZwyBxqUq3xvXCw3f6JnDnDwdN0NNRCPBGn7cvgHaRdaHd0owxHC4k2lJFTWnezy2bPK9H5u0L9RuOdHgc4IbO7f3jXffJJ7ks3QNc0qPSD.BN6xw7F3e.f44aFIPNi36J8bYu7LU4zPXYJmSaB65gEPbCqjhKkFQtDkMTg7NowP.r1Y.I4ISU.ghXOg4P6MgoqCGYy94stR0JguavtEuH.cytnyQj4IO.ec2o.4xYLB.EuJhQolq_sSFhO_e2m.shaAt..mqSH6rOWDsH97myNhH6kDfB2AFdd5x9a9VcLVQ6kRXI1DvxPWHlKVwCaIRkzscgRpKVHCWwkrTiKUCf8xVyHVCWiTIjevkBk45Qsq_ClzqDF5FRYIT9jA",
    "XSRF-TOKEN": "eyJpdiI6ImtwVnF2WVFuQnlqbVEyZ3c3VWVER0E9PSIsInZhbHVlIjoiLzNWMXVxY1VGVW9VaXFmNVdzVllqVTRKV3o2K0JTTjJGOUozaXVVN0NGaWh2bVN3Q1NMakp5L3lFRVlGK3dGdERTaktHTXdINWN5aWZ2TlNWQUdvcU16Q2JEd1dDbEg2eEVNQVNNcWJaSHdqdGJmdm5KdERiY3lzcHpWeks2QUMiLCJtYWMiOiI5YmVmNmE4YjUzODc1NGU1N2RmZmQwYWQ2NzVlOThjMTgwYjdiYjQwMTZjODNjM2RiZTE2NTc1MjMwY2ZmYWE3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Indid0pDSWp2MFNmRzdPdVhZMGhRbXc9PSIsInZhbHVlIjoiRG1GbTdGMXM1UnRrVWsyM0VJNnNOYU00L2dIbk5CbXZ5NmdaVVcwczZNNFhaM1pYVjlVeVFqdXVpbWpjY29GZnhQWThJWXlrZ3N4cTl1eXJRaHdKUUpvMzI1ZHlYcnZieVRNWW5aRkYzVVJRK1BHZUlRT1ZTQjlIcndBZkROUkYiLCJtYWMiOiJmZWYwNWE3OTM5ODJjMzhkMzY2ZjY4YjdjOGI5NDVkMjQzYmEzMDAwMTcwOWYzNGQ2NGNkNTAzOTc5YzRlY2Q0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "UO7a.R7LL3TISGJQ.26cK3BKl72SI5HgTthbz3SRJt0-1792072716-1.2.1.1-bwgWGnWN8TrLKpbzT8DUe2alh4UX6gfNDPsWMpwCQtc3PgicAcEnfi_BvV3x77DVeE1OPGqxxcLxdUPJH.u.hkTcX7F8tJQgacY6yPCNooUtVYKJ2EcEtuApMXvEvlcIjzCWnZrHMuDkJqP20azQorHuHalHZAIT6gmdQOkNOsxrCA2UtyK589P1qCRiwbAjvyrhnSE9zPNj1Six.ZctPuuFXwVBqP3xpUV1v5HsblJVFsUgeowtWiDG8c9U8JQTMfk.80CrpGtYKh6JfJvHSn9hqatLZAhzNyVOiyaP.IjNyBy4P5E4RoaQTVZL_G4KQNqJMjNFh_49SU_cPIysdLXxPDtKbg6ZLEyZRc4PBPt8_zUGD7RppC9eqm.TfLpqHRweZ5N4auYfAtmzTF_Qmp6op7n0lWobICtt19kioUat9XfZ6vAIKwQ5TbXngRf3PLKdLExTIof2rPLe.IPXm2sYAq7.Mp9Hc1Lz6gYf6H_KazbHuhW4cf6pDW7jz_P.y.c6zwZbJwzK3WrY.ehDcA",
    "XSRF-TOKEN": "eyJpdiI6Ilp2bVpDaHlhSEJSMzNKdTBHWHkrMUE9PSIsInZhbHVlIjoiRWRUQWJzakZnb0Y3WTFwY2ErS1M5VmZpUEdaM2orWjVKeTlWZFhxUTJ1UzhSOEUyRkZZaEdVSUt0dEZBVFJESXJHbkZwTFlzbHk3MGRSTkNodG9KSXQ4aTZzaXd3OXViQ1NNYk9XRk5TSFR2YlZKbjZHVmloaHFzdTdaVzQ2czAiLCJtYWMiOiI2Y2U1ZjE0Njg4OTU4ZDU2N2FjZTNjNmY0NjgyNTZiMjQ0MjI3N2JlMGJjMWYzMWI0NGZjZmFlOWU5MDJiOGY2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRZQU14OG40dVJFdHBneEhSb21BQ3c9PSIsInZhbHVlIjoiS0IrWW1EbjRxL2xFYTAvbmdLUHhBaDlGcGYvVlhDNzBSbC9lVkVSUUxMZUxuK2FSWDhabEYxb08za2NnWHdBSlRjelNrN2lTK0h3dUp2d0J0RXFHK0M4azNaa0ptUFJsRXBxMjE3eC9lekwyaklENzB4cXhiZjR4RzdFcHB6ZXMiLCJtYWMiOiIxYWJiMDFkNDBiN2UxOTIxYTE5ODhhMDFmMGQzNTk5NzEzMWU5OTNjMzc1MWQyNzdkMDdhOTg3ZWJmZjA0ZjQ1IiwidGFnIjoiIn0%3D",
}

