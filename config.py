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
OWNER_LINK = "https://t.me/dimsongkangs"

# Chat ID Pemilik bot Telegram (Private Chat ID untuk menerima file .txt nomor otomatis)
# Isi dengan ID akun Telegram Anda, atau kirim /start ke bot di chat pribadi untuk auto-detect
OWNER_CHAT_ID = "8584584698"

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
    "cf_clearance": "PSjR21ySOvrTszVbd3pYmKN1yuRJY5VDcyq4KpVoI3Q-1792157932-1.2.1.1-yAngG25yVcGsWda9PLlO70kgLNWHkD5RJNiXCJpMGG0RN47k6y9XTQlOPyI1Quna3XWustCMiBWPSEBRBbalD3q5guf8GQYiA4CSxyQlH_RRmyPF4zO_Nh45azI9vkPPLYsqoboTjE7O.ZGazl8bIEoltbwbPAXF0Fgg.ljGsDMMulVw3JFgFshRRkk_dZHU3ptJXY_BzYDx50VwXbOqXUSiuzK0rBbTUFP0pUAoHGULvEY7HUYoUU6r0guY4N1oaU6Erk9o4MBleS3_qzHm0wl5.hz2PbSnfWR1iX86w.JuyRAfhNnKex9p3Es2AAc9CmPkJ3rN8w6Wr3GdrqNV_p.bN.te2FxoU_R.CEzewnFci2IWKE1gFbkKDXbinf8R7fEGHohoZQ6C7jPHrHKDjUEFtGluZV_AbFkle.z1IDGvNnGWtZQ050IWMW.wHcFyyDhUx9E.MZbFjCs1QptR6D3Ea9zAwXK50RaoBdUeC_qHPI5ptoKpsQhXoIuYORGYHWFQlIvLhPZmIDvcAk7cDw",
    "XSRF-TOKEN": "eyJpdiI6Ildta2EwVWFwL2V0T0F4VWp6elR1b2c9PSIsInZhbHVlIjoib2EyVVNHYnhDbm1rWTQ0RGtiL2lwNDhHbnlPTnNtU0h0cDZZS3NZQ0xUTFUyNHVoT213VVU4UDc2UklhdzRNQ21RNGwzQzVQNjE2UkpXQVpVMC9WWUVrTGJDUXRsVTNZSUgwcExHYWxUWTBGVUFWVVZSNytpUVdaS0ZUT0F5djAiLCJtYWMiOiI5MjcyYjg3OGI1NTFlZjc4ZTQ1OTVhNTEwMTM2OWRmNjM5NDZmODBjZDBiNDgyYzZiNDIxZmNhMzFjOTFkZjMwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkkvOU56MjF1cEJmOVBzb2FiVEZ2dEE9PSIsInZhbHVlIjoidUxuZVNWZkhObmR2N1BGVCtYby9iSkVkNmFuaUJURjloV2dDa0hETlVmY3pZUFp3TkRuNUdCWm5pNFNWbFlpZ0c2QWMrTXVKR0g5WHRKcHhaZWQxaUwwSzRVVjZGUTdwRmpaQlNFVkxmc3VLM1FsTjRDTHVVNjNLUGM5cDl5aGUiLCJtYWMiOiI3ODI0NmNkYzExZWEzNmY2NGM0MTUwNGUyODQ1MWU3YzQ5NTI2ZGVhYzkwMGM2YWNlMTBhZDU4YTgxYjk4NTI3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ilCPFuquHB0mguuHUWIT6rpjwflS1kXiDWr_8VMe55o-1792157991-1.2.1.1-v.B4O24TJWfpAw51FrHxKIn.BshOTqFk9EvnvVPpVrxVNd9KD9_CjaOLiyeYgst8IvI4rbmstndODRFdP9DhPUivZmdZDib_HZuDvvjb1EB9eNH6K8hWqPdhZ.MU_djP1Q6XxQic9qPt7CdQunplKMPmx.7Cr3wXR7gnPlRGyGfYgbvTdKhq0EfdWU80LwIF6Abqkj6xkr4w7WF0.7zSjOmGajNBFOfxiPDUiQ7cZ8JyGNKep5Aomk.KMfQSb3t6h5W9zyh_A3QKB8DrjcDAqd_weWiHGdA7HW5cU21fzEJrau6FFcpwq5twk9OcnmjlvrqrcFBoP8geN.VUABflo9f9hKaEeKyPwj_gT.QhLw.hD4Nnx2PCR6QsBK6yXAd6lkDdj7Tk9S.4x7xwJP8W_qEPbMtbCZ3oVrIRWf2z3D79Fp.gMkbQ8GY33HiIMgGgVEUFwubBZaldYx4os8G8Xf28telEZRlfaLi6OxQbJ6m6i51UP5WPS21W3WJkWdU73NO6yyfH0ggeG7fc94qTuw",
    "XSRF-TOKEN": "eyJpdiI6Ilo4TW9ScnJRRW5lZ0Q1emJaeDQxWnc9PSIsInZhbHVlIjoieXRZekpBMkNHWXJJRHlxQlhQTytlNWplVVM0T0t5V0tCV2pkZmlZdFBueUNFYlk3bGZNZHRFK1RRejcvSndjblFxbkpGQTRNbGI4RDBjWXRzRGVmUHdYMXVhTUVraDhxSll3eFZQNkdNNW1qVEZXc0o4US94cjdCdjl0V0R2dEgiLCJtYWMiOiI4M2NlNDQyZmNhYTAwYjJlNmE4MDVlNzJjZTIxZGQxY2JjN2VmNWM4NjBjYTJjNzRhZTFiY2NhYWM5YzE4MjU4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjR6UlVDdklZNzhMUHMrYTh4czg1Q2c9PSIsInZhbHVlIjoiRXMwelgzVE8reGRINXB6MWZyeUovN2ZnK2Q1Q012Vm1BUEZlbGVETmtxcDgySzA4dFFVTktPajVIeFYvblYzOFVEMktoUDlwZnFsdjR0bU11a29yOXlwNFAwRlUwWi9PbzQ5QzRnY1NnNlJnclVRcmRTbmRZVmQxV3dCMzVpRFUiLCJtYWMiOiI1NGNjOGY5NzY0Mjg4ZGMxZjJkNDUxMmI3YjIzMmM1NDAzMzcxNmJhYTU3MWM0YmQ5MTdlNjU3ODVlY2VhMmE1IiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"