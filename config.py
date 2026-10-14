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
    "cf_clearance": "DoGTekQOPb2dY3cj4dPNeWcyQV1Emw7IQVp01Csol4M-1791938519-1.2.1.1-A.WTuJelUdZrVeVa1_F7xzNmZZyYYUFIC.XEOIr39QB9aDmQNM7PUA.wLFC7c.MFhDDmjExYIH1Ehm9049I2atUoILezw20NFkQxCabALQsGUb03WLaH1Et9FpI26VxVnGS1FEvJOJCfzWR9eCfeBmzpqEcW3DhTNwW13qUnhfPrdudYZePGe4ngMaVNvpYzF1fXQHwfzgerZR0_XaMtQP8RgEIGlP.YvYuRrtZMy7VfsWGkawDu9D0RdCgne31ND9X9huYuYYgjVN7p2rZJzWRHvJfNhxxPZWcKslFs0RaPehYJ1fVoaqyBYwsj_x1ze7bRJYOMJBYTG_S_JUfz5ZpD2Jd6PfbUCGjta2BLUBilTr067njT7gJ3NVtp6rS.XQBlAGrSAdPuv5KdcApPgKv9Sk7rh91A3mGf9eVxXy.c4SSVo8H39C10cfsoWuHJBz9ZdGvtodxh.3W_eYRpQg1AOI.pmdwTourkYi.jE4H6A.0yjoi9xOKVWSRDGhog_FuLPj0kVSkQKmRWs5koIw",
    "XSRF-TOKEN": "eyJpdiI6InN3VXNtVS9wcXJtOUJRVC9IcFpleXc9PSIsInZhbHVlIjoiQjN3MXpod1ZXTWh1b1lUVngyelJHSkgreFdBREVNNzhDdEZqbXFiUXIzUjJ5NzJ5aHpzUm5PVUVic3p4RnFta29FRmRybUVLdkFHYU5xUUVLQXpENi96clpOdlowMUJkdkIzLzdNd251Ty85WGNBekhkSnJDZDhlbkc0Wnc2cTUiLCJtYWMiOiI2ZDFmNjE1YjFkZDUxMDhlZDEwNzJiYjIxZmQ2MTFmMjAwZmY5NzU1MDNkMGIyYjRmMjE4MjJlOWE4YjM2YTFjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkovMHArWnpBRE9naytUZnZvZFNER2c9PSIsInZhbHVlIjoiT3FQOTFXZDB1cVIxVW4vWXUzQjEzZDJSR3QyRG90cVVnQS9KNVkrd1ExbG1ra2FwMVNKUWRNeHhvMzFncEdscjYrRTFoRFRydzlkV3E0QnExQUdLb1Q4MldoMjVlWkMzeVQySWlaOHVQQVJ1ekw5SW9Xd1h0TmoxamFjeWdhNlMiLCJtYWMiOiI2MDAwZGY5MjMzNzA1Zjk3MmJlMTYxNzY5NTExNTg2MWY3ODQ4ZjA0ZDY2ZTI3NzMwOWJlMDYyOWI3ZWJhNmY1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "nOLG7vpWDse9ESCk7e0OeR7yLtnoofQmUNdmLobQazI-1791938508-1.2.1.1-IWZq6tTZuQelyRm2ZJgY2hZFsTE4F4H7aL62O2T3hN2TGfxgKBZOqXypAPOvWNslc..E.rfv.kEZjtL10zUOYGchbAN33APLyc46VbEkN2fk7b8LX.2LtpqIhBydZ6U4Gb64t5pMPZIEfPJo36z.uuEKVlRXIcdT1U_dxBW_S8FtQAtLcjY8bImQhnvu.C.yAuCvgFu_IMsJ8adNW_B1IWmi_WNF67IV8WBMyJVpiJ_sSZ7plqIytTIoSwY4ZsLQQ2CApJGv5k06s7q2_5m2XFbVbPUFJ8Aa7CpExnJVcElJyawROOmdU._OdVeymoTsHaT0S2fRMqo8tuvb7HjF2iz1jFRwAVKgaMFqmnDpT_YQWWdY9nexkuuvkfPB9sMbxAAeTnou8JZyN6eMwLqwQUBpi7iaFmkIOXg.ig6fsZTO3lbf96pt8lzkkRrXJdIoY6UqcvDj_bVKarQ92tEMaZUS.K66ImqjH63nT3ATcgvQn4amv7gLbEDEiEtWEpndxAoEeoqilz1nzBbtTADoAw",
    "XSRF-TOKEN": "eyJpdiI6InRJdHgyb3hTb1NVNVovMlg2d0RkRGc9PSIsInZhbHVlIjoieW82bVdhVEhJMzNxVThQS2phRS94QUZKdXNldnhqZUticmxDZFJIeWxoemZmMVIyUEd5ME9VYjlBaVRITm5NeWMwTjJDeGs0OXcxT3lMcWRSTmdlSTFNUmV5OXREcXYzQ1FadWp0Y1FGUHlXT3R0Rk1NRVZwTGNjQ2o2YXJ6Q24iLCJtYWMiOiJmNWMxYjZjZTYyZjg4ZGQwZmEyOWNlZWI5ZTgxMzFhN2NiNzg0ZDU1YWRlZjU0NzljYzM0ZWJjYzUxZDAyYmE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImN6cXRuVk5adHh3enRxck1YQTRZcVE9PSIsInZhbHVlIjoiVUVWbEtvY0MrNHdlVlBtS010Tk5INDUyWkZSQjRKZXpqendqMjlSalY5MU5qVmRXYlhHSzd1ZlcvelNyNDV5RXVBSHRKaENZaUh2YUNkWnZINm1QVUhxT3ZpRmtzVkxXdm5DS0FKbFo5NHgvNXJCOUlNQ0NjK3pUUEthK0VNUDYiLCJtYWMiOiI0MTdhNWQ2OWQ0NTg1ODE3MDA5OWUwMjgxMzhkMmMzMmVkZjkxMzU5NDA0YmMyZWU5ODgyZjcyMTNjMWRhZGE2IiwidGFnIjoiIn0%3D",
}

