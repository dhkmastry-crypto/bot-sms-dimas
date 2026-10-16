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
    "cf_clearance": "E3w05vhpuQbEroVUOdkorSxKYvlQDVL7greU8Tgw9mk-1792127129-1.2.1.1-.9_8pSJ.iAyvmf9u6h6QJEN.T5ZeQkjw.plLC.80roips98QI8753qKzvPwlifnfzg_p_cKpEEiFSAD_2TF1G81vWzk4tNmnP_wrMgl8s.rM5ELITC7wh9AD0qOM.vaVWEfK_vn7rajxPpg4VT8LAnSyGioMurWmtOsTNWj.CNmhq9txxZITSclJ3xa25LNqxwCI1ipN_mwlL0aY5oNoFsV3eN1aN36XsSdhqtS4OpUVB_ZVCzd3k1KkbxcyRfU89bPeBwu3ZEspip7vkv63ULk0Lfd1RVsL0JVEey7wOxlPc3c0XxT_inlUNhjSFR7R6_20caDDOWpEGAk6Qdz9_CmwlaBgsnMtXcJ8BW4R0vCjfR9t8GOmi4xJJkW4BPl444Ruldi7gZDWxYXX0oObE0X6TEi_dnHm4VrqaQVvYHX4DHosY4vB4t15gW8A42v9S.U2WvzWge8M4Bdp1v6LIedFrBdxzVNZp2eI.ttmYlOQr9iVF_dnROyGzoQnaznbRZg8Z6DzoubtjbC86Tqs_A",
    "XSRF-TOKEN": "eyJpdiI6IjljWUp3NDFnZVl3dkJhOW1XY3pIZWc9PSIsInZhbHVlIjoibnRQcUMxUHpmMkduVWhBdnBsZEZhMklYa0NYZWxhQWtkUDJMNVpzNExJWmtvZzQ4ZlYrNzYwL1RsdGJlM2IyL01QZ05mRU5uVWxrdm0wNXRpZkY3b3hEMUwzOUJ3Mm1rVGFTYkxhS25uOXZyWDY2ai91N1p2NHN0QVhWS3daWXEiLCJtYWMiOiJjODYwY2YxNTFjYzFhODVjNWRhMTUzMDg4MzRmZmMzNTU1OTQzY2ZkZWVmODFjNjhjOTg5ZGQ5YzcyNDBmZDU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImF6SUlqRDErd1VZYjZ5elJRRDFtS0E9PSIsInZhbHVlIjoiK09ZcE9QTTBYaldTdkxuS0V3Y2NTZGMxWW1lZ01sYnFna2orMlZ0cHVKaHErNnFBaStxOVJtUk5EMTJJY05wZlg5WEx0a29zY3FpNG9IZHFVdWhnNURYRk5qbmQyM1h1a2NVem5TQnAraUlEWjZpZGo0SHJUK3NxY2Z6TjBxNGYiLCJtYWMiOiJmN2RjNThiMTdlNGEyZTc0ZDZhNTk1NTBmMzIwZmQyZWI3M2FlNzE0MjhhYjJmYmVmYTM4ODg2MmEyYWE4YWYxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "B8aWvMg7FYkLoQtTsc.CLsVPTKEnKtUq6xu89dqqNH0-1792127118-1.2.1.1-wILu2HOxAPPkDeJCbeW4tVVmZjeWhQuabRX_ZWM_Ss2ocbBT32.ZR80fgaxWLjLjXrw2i3W7ac5uRvSsZ8Qm.EdxBWkQ6XrixbswCO62q25yekDQRwvfUGkJik_hht.zCqBj2_uY9PUwwmlIN.VQ4r.TLcsIbV9ED43ABx86w5IW5PmjHnOoDTpdPSdBoFO8osMkW4AFwHu3EBmRN9p5Q.knbLpvD2yGxx7_VloPyl6dHzaJ83b_KqeMz_TgRazFOtjx.fjMQ.adTl8KD6KxEDbUpimLGUD.9mtmgzJE70VcOC7_BqUqGnr4dXjBuzyS5tw9oKqHecgiXyZ9Ob3Elcw3eFb9MoBFBu6qUJQnrmkVn67vB5Z6l_vQe.IJek8c94qjjrEaVLTfSK4IdSPP7w8V7he9kjVlr7heNqahG5Y0hPdUVfLfpcpwJGpUUdsMivS5lDyUjTb5xazBGBUtae9ZmI4C9_Mm.MJR5BVaVVbSXjcc82.g8vZCmqhADJ6fmzo5Ch_o2dai6C3qs.tVAw",
    "XSRF-TOKEN": "eyJpdiI6InE4QVBnOEhCM2FsT21MbmNQV1gxWUE9PSIsInZhbHVlIjoiMXVDOGF5SHVOR1hIMHFSTndYdzkrWXRxWVNtQ1YxZXdNOGRRU3RTaWIrUTlZODU1Zk44am9BQXpTM2luV2x1WE9FbHBuS1FyMjdqa0JSemhIcXVyZ21HbXB5T2RYbTJ6OTlTOTJSODNMTkUyM0lEVXdPcW5XQUxpWjNkZWZlL2giLCJtYWMiOiJlM2Y2Mjg2NWUzZjBjNjkzMmUxODhiYTRiM2YwM2E2OGUxYTY2NDI5MWY2YWM0MmFhNWQ2OGQ3OGU5ZDdmOTYyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imw2MW1uejdTaFd0WTBNbFoyTnd5SFE9PSIsInZhbHVlIjoiVHBscVh1Sk5kd1hMOEdNZXdreVF6eVJ2UkpkSmxhT2x2ZkViN3lFV3YzYzdPMEhuc0tNMjJrQWdFeDBTRG56SUFNUlZKbkM3cHl6SjZEWjZ3UG1POGV4NWNFYXhKemVhOHdvNGFFZEIxdVhUOXB2WmllckVWdk1kS2NvTnNTSHEiLCJtYWMiOiJkZWI1NjA1Yzc0ZWM4OGU4YmE0NWFiNjEzODM2ZmFlY2E2YjIxYTdlYmZhYjY0YTMwY2I1NDRhZWMzYjg0MTZjIiwidGFnIjoiIn0%3D",
}

