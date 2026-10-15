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
    "cf_clearance": "a2ogArsNW3AMon6R.d_PH6JSAXYb.N9V66OXZXw3w.g-1792074524-1.2.1.1-KTP_JSMeVkFk.X3c5koZrjgKuZKxNY8qrWAkUxR.bA4kwskKHWdUehye1KKUNCQ5JPj3tUPS3HEvkL3WgX51cijgH3RFIck5O.03qiNJ7Ck87R9ViJ.pcUJNsmFyXe1VCSt9H8cA5QuPktN0bwjidDrX7U6LDdrvreaBtA._zKcqHDtO4EdTtzWj1WdDrvC9_LAo8d25Au4Ij2PrT8Ntcg9CAN3YZGrc4gfmXoMOLzle9JgtVlZzutMcm8l3QRHGHJbHQ9BIvTr.ppr9_8_qvz3uv7QxwAgZEUgz3A1oOdDoQ7mBNcobwMrXxxsRm9qDNftQYXpAAiSUMKi6uqqzPDCoN4GTkrtj_sCUtS7AN2cZD.9S.S3FbmXHuI85.2YfxbynnK8_C.hvE1QTseghj9wb4YWokTLuExmnyVxmzCZBZyDEO0E4SWkl8fBuoEZuNDlJTBa7V9oRNLJOG17E2wisiPDDxRePTuTnQZATpfzoDvpi0.kE_CzVo.E9QpWGIMf5UYfZUQX66fgJKAewEQ",
    "XSRF-TOKEN": "eyJpdiI6InhYVUVCSlM5RWE3UUJkVWM1SmEveWc9PSIsInZhbHVlIjoia2Q4bGI4SVRRQXZlKzJzQkRpNWtKVDJZdnYxYm0vSVp4VG1XV25WZURERkNBdnVlaFpBUHU1cGtraUtoV2NNeDJQYk1sQytxQnpsTmVzSENURHFKUHRmQ3VCalpvZ2x0cnpyRUpMMmI3TEpYZXBiU0xZRWVHaUt3Y2FGOFQ4bnkiLCJtYWMiOiJmYWM4ZWE0OTM0ZThhYmMyNTgxMjYyODQ4OTNhZjgwNWNhYzAyZjAxY2M3YmZlYzhkOTY4ZjMyN2MwYWI2OTJiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJzMHA4Rk5pUHNhUmhwMzhxVzhUR2c9PSIsInZhbHVlIjoiekxQSDlHLzdnTFFPNk5PYTRBQWhQd0NHSTE0ODNqM3pEdnA4ZldBeXdvNksrQ21aMWR6d1FuVHVDYnYwZzJXWWNMQk9mVkZwdXIxckJ2czJ6aS9Vc09sWHlMWFZWeTMvN0wrS0tpdFhVZjNYZ1lRMjRBbFhaS1BkWDZ0MVErWTAiLCJtYWMiOiIwNGE0MzZkZTM0MGU2MGRhMTNmMTBjNzcyYWZjNTYyZmMwMWE1NjMxNmMzNDI4NGE1NmNjN2FiMGFhODA2MzcwIiwidGFnIjoiIn0%3D",
}

