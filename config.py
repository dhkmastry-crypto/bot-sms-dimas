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
    "cf_clearance": "kJIBwQmW_v6IkU9ho1vCmp0YFfAPZjU7CA.v7IrJGB8-1792092663-1.2.1.1-KnFYfOaPCFRG_LvA.AHXOLU_ln3KsnbeJSfJI_V8GpAss865dF48rLKgpxCBR.IBfo3DLZpZxZ_qewQ.7ksLRGiSvNnBNqZEPmErqVY.oqf0S1vlHTMs6Rla6.FFKCVOA9mAzSmq3tQwuM4QTDsDk5au.xINiNCxHQI1vMPAm_4FHbKNYXjfG3uI5RNGQfUH7ah4nw3FMeBOioOEoTrj17Nh7EiULx4kFHMC_C6ZFkcS3mEO3tbyfskV0X70OEqd9PGezs8Kv6zeHuUbA4hJ0UZd2YsgufEnFaDwPJ.pfC5J_L8q74c8kcz.iijQSZjpraz0ULax.5IfzGLDSfnGQb9AHubFFNJA.Q97E45aQyhZ2IAv_eSK5qmAXwvgofG4sG_WgKVfi1FxZy.oKGpCALG0SLPND3Mubu0n54XSrMQJ2PBL_bJIeELxObLI4Up3en1Y3nqcz5.tV9fywAm64wSAzK4dPgQeZQdJqPQ.WJW3C51s8Je7XQGuJuaLczlzcpjYGJxz7bCTo9NTLjhpKg",
    "XSRF-TOKEN": "eyJpdiI6IldWOFZFYUZiWGUyN2ZvejY1RjFBQXc9PSIsInZhbHVlIjoiaExTb1RvbVRVTFBGUG9WZzZ5Q1loOGRRUis3T1I0ZUR5Qm41UzVGNGRVZDJTc0RXRE5yR2Zqa3BNaE56T041bm1nNGQ1YXJxamhwRS9hMDcrK3BxKy8zWkE5TmJwakV5dDRuMXdUeGhxVjZDMU1ZMW9EaVM3cjhnREFZSDFiRlQiLCJtYWMiOiI2ZjhmYjc3ZWZiYWM4NWU1YjQ3YmNjN2UwMjEyNTQxMjRjZmVlMTdkMmQ2NjBkODI3NjMzMjM1Y2VkN2E0YjMyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkV1ZllzMW9YSCsyNzRlYW1kU085a3c9PSIsInZhbHVlIjoid1hDU0xWaFFBQVgyUzA3cG91cmx2OVRhVE1kdmlUWlBiWk9jaE1ycU5kYjI1dGhoQndNM3NrZnJkRHF0bS84NjdoMnpkemJacVZYRFgwMDlvY3EzYUtpSWJjeVFobTdBMkFGTDhjMkhSaG9UOUt0Y0ZiZ1BKNmVkRldyZlIrMXEiLCJtYWMiOiJiYjQyMTU3YzA1ZWMwY2ZmMWU3MTk3Y2VmYzRiZWUzYmZjNDg2NzhjNGU4ZTg4Y2M2ZWRmNmE2YTMxNjIwYzIzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "AeMv34_tMN4tAnT4p.wTFMLl4SrXYS2B7ZaQM8fwgx0-1792092621-1.2.1.1-5lzZHhnmPU8L0wnvBnRZtZaJM4vLL92g3pf1X8P8EDGfLkgtTC5Xy0qLqRUhvttexM.iEgJyJp3mtxT74GsUEksAvdD4ShWNLuq0FnL_IqtZtWAVNtTb2gyskaVd5LFizAo.oRbSOptiNinenfVcOP7uSDeXV89a_AbLey4REhOd6GcYlnjYcJKt0G3m6PZ5Mb7Fy.mDOuaKCDVkbb5Nhtj0JXXdydVKLbWUjuBJNDi2S.ddq3ieFiofUJ8IDLtnYQq.ibnRC7.6h6PWGG2.5O9QFvjmvlQ.Qi0nttEr5SbBuqS_dYnHzL_r4IkukJzleAFH3VwF7GP35gJgYi_AYHzg.PkwgY4knY5gdV05vueorD1w7G.dRPH6VEDil5NB8bd2J6ietOcC3D_8UV8rbq9JWr5T9gH0q0YiP83pGTTpiivcu0G1l1V1GNMxbBlpbtK74XRNTtLpw6gPogTgjqU3A0gLoqzgYqcMbVk0H7EbAZqwSBqtyfk0NINPaYtMf3vwvPzro_fHtDIErpb67w",
    "XSRF-TOKEN": "eyJpdiI6IkpHbklBbUxHQjM2S2p5UjZIbnMvTnc9PSIsInZhbHVlIjoiQ3NPdnBjdEkxYnpib3VWeFpyOHkreW1jbVpvakFidndvVTl1SCt1aGk1WlJjbXZnS0NnNWM4T2pzQys3Q3FMTXBTZThMN2lNdzc2VmhKQjRDYTR2N0NkU0ZSa3kyS2tCcTJHZlBvNThiTm9hNUd2SGhKYXZ3ZmdWdzhwZ21PeEUiLCJtYWMiOiI2ODBhZmM0MDRlMWM4ZTVhNjYxZjU2OTNkM2I4NWU4OGQ5YmJkMWM1NjNkMDk3ZjJiYWI1MTFhYTI2MjQyYmQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlIrb2xRSUdrQlNza0hrZURDenFMb1E9PSIsInZhbHVlIjoidi9ITm9CL21IVEVBUVowQUxkMXFmTGZNc2hRSjlXdnU4WWsvcHc0T2tSYU50RCszSXJmbHplTkVQb0tGRDFXcDRoQzJLWjVsTm9ZY1FaNlZDM2lMZC9rVHZYS0JOSkZ6SThPV2pTVFJ6dTF1S09PR2RuUFQ4blZNTjlzbUg5RFEiLCJtYWMiOiIwMzY1YTgxNjhiZWZhYmJmZmI1YTdiNzBmZTFkYTJiZWM0MDczMzY4MzlmOTFjZmQxY2Q0MDU5Yzg5MjY0NjRhIiwidGFnIjoiIn0%3D",
}

