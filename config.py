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
    "cf_clearance": "XrOHJ3HXzUA0QtYYIDZx3dDrkYJ3bQMX5h6A_LfzoZE-1792051077-1.2.1.1-T7GFeT4nSC1fhCij5Jhnb90Ey5uk_kmjlIToay0Skt1nb9DzBXm7cCbB371fmT.1folMYtLeqblKLnrWgwAy5a5FQfykyRwDH.jxJ4gBDsMhrAQrkmJXP6kvgMq9dSM5.a.M4a.Fxr0ZEGJOYeOEk0qb_TK.DsHMVwog02APbDWHkWMicjP6LsUQfnMYOroRoOqB7vfpSyzGr6b1ji0tzMkjd_Csem9MDY2jBQ2sbXr.TjP60D9p_5iEar1LY3Tdvsxdi25a9YfSzhsOsbRXtJoSfn0aqCc6uFoSzofXNRqUX20n9aBBg4JdOrXievDxyxLDz8gXObCkfkLpEr7OgUXcj70lZQvqj8QW6hsfHG1JVdJHX4sRWar1kuE0YXDD6VAfiwlbpvs5bYOZE.FsDYge_o4NogjMuE1SryUK4ofvct7AYUnPdo9ilcU_UPGaFDLL7WmpOcgdIhKk3pcXe6wfJS.YISGFZalu970KNXsyoBvGBgiAOP7_5eu87.b.f75BctGqlxIBAYyfmkBTUg",
    "XSRF-TOKEN": "eyJpdiI6IlRsZmlTbVpVYytENzJkL3RlSnBremc9PSIsInZhbHVlIjoiZlVwbnlQSlVnT28xbk5IeGxoTDhoam9mSXNHODN6cDNEZm1CaHdVUS85WThwcURLQnhOd3dRbGkyNGk5ZUd3b3JtR085ZU12ZjRnQ3JqbTBkUjExVmlqdGFyTGVoUHdyRlp5MlpqSzBGcnlXTEFmWWcyZDFnR3JzUmIyaElVRG0iLCJtYWMiOiJhNTVhZWEwODhiMDMzOWZkMDI5MzRlYWRhYzBjNDJiY2E5YmRkYWEwODdiMTcxZDU5ODUyZThhMTlmOGM1OTE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlY2d0Zac2JKRnY3ZWZpY0cwMjNRN3c9PSIsInZhbHVlIjoiaWpXUU5FdGlkdmN2Z0Q0cUgvbHdxTWdEVlNtcldYTWVRbEZVeWhQZ0s3TU45Q2dITmZuTWRVM25FeURseGdzTzZNUkYzMjJTcThLZjFUZVJSVk9Xb3d0VkkzS3paNlZCVW5PS3dwOUd5dFZacTFmQWlwb2hyVUhqcWp0MEVFL2kiLCJtYWMiOiI4YWI5MWIyNDU3NzlmMWI5ZDM3N2U3OGYyOWQ1NDg0YzkwNDMzMmNlYzU1MzU3YjQwYTYwODY2ZDFmNmJkNjEyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "blq7NsG4WbNLbCJEa1299LEaevtFE7IX3j5v1cNFnsg-1792051037-1.2.1.1-MBt6dZWzM8l3qNr4gCup.qhDXcc1J71jphD5aULRAOJNCqpiMBaHcmaKapnXvUTbvotRUQf5GoJqZOhmBglxn8Bdt6PQqC0MC46FWwQOob4x49rvursp8SdbGeP.d7PSeN09h9NjjBnk_KK8TxHYfnHDYVXiqwPkN1yB1y5h.BRr0xgpUhyuyGpYehSGxLFO.CoiXa_hj32r0.0qfvSQ7SODM78JOkLjdwU0TlE.yFZhUrL652stT38.ZOdrwM_6S0kY6sDwDUPkS3Fo0pSdhoWoeFm5ocl.lQFi13E0y2iEk5sNqaV14eShCx0.tvkriRR6izJ.RA_wgZzlRrPK.XfzCydZfLpfif_Rn139c_8of1gklFjHPn6dxdA9Mr4ZArMgfEnWprzynPOpvALVCE6yd7Z95oJ2G_cfUR0PfHxMOOeyYefGYqKqguCSgEr7kEK9KrMSf4bdfWWl8sdh3ZLCrOvvZw6IDBnD7ajvHmkm95OlfF8lyXVdCNlV6muV2lVRGscMa6NkH8XAU1nI8A",
    "XSRF-TOKEN": "eyJpdiI6IlZtOXdOZHNFWkJWVy80a3hLd0s3M2c9PSIsInZhbHVlIjoib3hzR2o1UXNyV0V1RFNmMUlSYThvTlYwN2V2ZFpEY0tVUU54Q2c3QlNFaU51bjNOZ3ZudHFrSU9ZOWE5MGJTNUVXa1FKV2dERlBXYmliZEd2ejZNZGJrR2V1MjZhSmhMOHEybFV0V3JsazRPZ3lpSkJNN0g4RG9LOUhSZXF1WkciLCJtYWMiOiJhYmZhY2IwMWI0NWVhNzgzNmJmMWM2NTYwMThkOTYzMTZjY2VlMjBkMDVmM2NiYzBmMTY1NjBiN2M2NzAxODhmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InNTT2R6Q1Q5WS83OUNYSlNWUW9GRHc9PSIsInZhbHVlIjoiR3JFSVQrYkFYdFlvOTJlcjlEVDVhWEl0WHZHaWUzVXZ5bW8yOXJYZGVidnlvb3ZZZXNGYUYxc1ZMVjRhUGs3WU1BR042WSt4dnJBVDRhYUVjSmV3WVQ2MGZKUElXNm82UzhacUlxQUViQWZJM2pIQng4Nzh1cFY2RmFHZ0VCVWsiLCJtYWMiOiIyM2NjMjM0MmVlMWI5OTA3NTIzNTU2ZDYwYjhlMzJlMTdiNzI4M2VjZGM3YmYzZWUwYzJhZGQxZGRiNWZjMjczIiwidGFnIjoiIn0%3D",
}

