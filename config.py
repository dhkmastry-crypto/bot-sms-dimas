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
    "cf_clearance": "vJIMGZGBqXY0ENor97Lls39XC78CDRE4aodH9CCgDZA-1791920407-1.2.1.1-.dmbpTaZnVV7UHn3alb_CIaq1kCimWSoMJIYC9IbJH_vtV_tbcxfpP4AC5EB91Cwl6ToWjaY2poiX3194Idhj28qUmV6donWMiY6iOzdpc71ldtyYX2Vdx.yUqj34Y6h2xeEYNaxz5JUqsbu_gk_yG_1aee0v.7wv7VPV90OkxUSXJd_TGZPKTmGbZ4qzqm1HYWPtTPGfvqpZoVLiRvYef6t_s4RqbXbBCJw26g0W4oyGbH0WL7XYdHVIXiC5w3NtDVkBThxsZ0b98PpCgbLVCvHEYhfRw_gUiaHIKKsMyGfVShVKfMxtxAQ8M3dtGp1JDsYvooC_LuTjVQkmw8QVZGrTpp5Fuy5tjUiaeN0.5gHDIl9VOSFcVStJ7WFquibIWXUSR1_y.c0f8p81ImKrGvLQ3NDNYQtXlap_i1zYKDPM0h.vfGSFjmlR0Q7VRt1HP8pu0bKC_vmYHzulNKk_59FbmqKCAzcE.i8a.Ll.xjmBmFSmVRXbhxJlT4NZGPoL4smMsXn0hyOjdH12yqeqg",
    "XSRF-TOKEN": "eyJpdiI6Iml1Q0VjL1cyanhiR0NFZ2lwRms4Vmc9PSIsInZhbHVlIjoibXdybnJYdFpja0dDcVJSbVZKY0QweTM5dnB5QWxFTld4K2JkbEU2bU10SUQxU0R5YkJBK00wSTBNMzd5Z2NYU09SdXpXQ2dsRjFLVDNndzQ2NjlpR3NPTEhTVUZ6Z3RMbGJwYm1TbmJtNHFQdVNvNGVuOFRRai9iRE1hd1ZJV2IiLCJtYWMiOiI4ZDUzZTljYzczMmVmYWZjNDVlMjI4MjA5MjU3MzQ3N2Y3MmI0Yjk0MzBmMjZmN2QwNTY4NzdmOTc0YzgwM2JlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldiVVJRei94SFJVWUhzVWk3c0lFTnc9PSIsInZhbHVlIjoiaDNhUHFWdlUwOEVhN00vcVBoL0VBTEZsUS8vV05MUGdFSEY3MHh0MXVUQ01mcUQrZFFuOGlzTEtLaE9FaWxhVGpKSnVBV3UrdFVJQ0dnQ290UldzdG1OQWxxTVRMS01MUnRzQW52QmduNldyR0NvVm5GQ2dISjRlak1RQXgzUlgiLCJtYWMiOiJhMDdkM2U1MGVjN2FlNTJhZTAzMGE0Zjc4ZjEzMzk1M2IzMjI1ZmU4YWRkZmRiZDMzY2Q3Mzg3NDdlYjhiYjM5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "HewLC5IUSAE9KjaAON2A.SfQGr87IQJJTK4nam.G9FM-1791920418-1.2.1.1-dM2DEx1Uev8oMAk44l_4FV96cRJxnUNPWoGjKkX771v9Iiag7oW7.wbCIgTrpJMwVUDaFUSEmWEWVevZmuD9MfCjMJVivnza6SFgOamQzDRZGjrmTUwtNAbP52xdQIj1JBWkH3JHOqEa7uZtU4tVWjdIzyz6Z7t0SBZ6UMC1wqZo4kUJz3D6YnSQ1T_7luAzaS6eVoXDhckYYV1ZYfm0VmJ.KfAjNGlplARz.ecBJ907zjpcYfDPzjaBeU3EoTqya8ruBhO5QREipFQKucSwcMylc8agkdEcjP5nmKPamDdGkD32IKu4Z1gbgeQoOVjnD1zI9z25T.R2sBe2K5SahP.ng8zyVJQCLFbgnUXo7hBeRf8klyX8bnOBmDO1kz1e.NHt9XPyf5k9h98eWRk8fKnLIVuctoui2puoJIiSe3qDn1WmORDUFoRMAPpYUia7_CAM_fvTSih2VV4bf4czMO6_.ADjVXccKo3Mflne5jgTReTXexweIb7.bvDyTOWIERSeHapDY8BXf5DX5jAExg",
    "XSRF-TOKEN": "eyJpdiI6IlJzNmQzSUNsdmRiTkhrU2ZDZitXUVE9PSIsInZhbHVlIjoiaGJ2eHVEUHJTUitwa1YraEFjMnV4Q0FaenAwK2s5K0FtMXM5RDNmbWM4bFhyVm4zMDlyRzZNQ2FqM3lObldFQkhZbXZVa2NQMnlvOUFKL1FXK0RFa1cvY0RUUHlFcmZyWUxiUUcvN2NuOGFWa3pBQjVKNGwvY1J6cG1oODFZV20iLCJtYWMiOiI0ZjAzZjFmMWY3MDA0MDJmYjExYmE1NjZmOTQ1ZjUxYjJhOTc2MmFlMTIxOGFkNjc0MzE2YmMzNTIyNjQwMjUwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9wSjBPQkp5V1F5cVUyOFh1SEQ5aFE9PSIsInZhbHVlIjoiMHk5Y3dIdFdQUGhHQ0h4ZEx2S1dKOUxxS21Bb0k5VHMzWEJpVksxcUVrUlZXVWZ4dm1EVDNJNURSRHFVelNiTW1QM1B2VHFRR2RYT0VEdGgxWlJCZzA0OWVxUzhaaGc3eVQ0WEFQRFhmUGRvYTREY1hzYW1YaXhzZTJwa1IvVXEiLCJtYWMiOiJmMmI2ZjVhYjc3MTU4Njk0NTBjY2YyODk5Mzk2NTgwYjYxMDAzNWM4Y2U0YjkyYTZjZGJhZjFkMzQ2ODExNzVhIiwidGFnIjoiIn0%3D",
}

