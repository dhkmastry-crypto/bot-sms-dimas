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
    "cf_clearance": "T0NwBAUMv9N7Bc_sxwb9tflq9Zt0LkXlfV2P.vBfyB8-1792156130-1.2.1.1-yKlLr5rKZyiRQ4hbpO_yJ0Nz9U3mN9PlWOTw4NDywclhjs8MX_KEqmW7YXbx5zM1.mDaFa8OvhSeep7Ua0PkmcUXuguLQVxShM6ZCaQQOfRQFrtufU2xbvVMc4DQ6n6zpF.KnNjHOfrwf9z6y992.ZoELs8hcFH.wcXwyFwYscmgECq9x.Vi_srn9MOxO8rGzoDpu8d33CsWizUY5R6SsJbL6rItghKoxxHMyJPlLuCXKCrTBuHnXgBigMF0ezPoc_7asWRw.h.55VMKXUoPWn75sRUhRWWBHYGhaQQqxcKmzGDxJI9PwE0RZlr.iyz2N7DtUAvG.xxv7.74e3WjQnxt6eu_VzEalt4jGOp_a61m.QDPUPnooWKISzAef0mG8lF4XOfApDWP8ZtDPTRevFlftdIXnssEr0V8t9SdQL1NTpyvD_UXyXVwn4xU1ExYA4m7pgp12Aq0HutXMbZaKcfmVcyc0Q_6T.grgkp.AYg3ET5SVyDbZlDoLO5g9mQxumVbxh8cU4e3UzgDiSJcmA",
    "XSRF-TOKEN": "eyJpdiI6IklIaUJleEdQZDhxdkgxMVZUVXZuUXc9PSIsInZhbHVlIjoiLzFSVDdGZHdZRmNNSmVUUUhsQUFuYzFaUndtYkxyYUhVOEJYcVpBdDRWc3RQZWtHdVUwZE1DZjZ6R3lmRVgyMmpxNWhVT3o5Q2FPUGFwU3ZHbU9YeHdLUjVMOEJxUENRb3IwUGJMbXVxTjd3cXJxK0dFSGh2cE0wMHZxVlZpSi8iLCJtYWMiOiI2NGFmNWY0NjNkOTViODVhZDJlYTYxZjM4NmU3M2MyNDM0OTE5ZjRlZTIyOTJmZmMxNzhjZjI1YzI0YjM2MDU4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImNKOWxtZWxNaWRWKzBsVE1Ublh5emc9PSIsInZhbHVlIjoiOWVTS25tKzRMYktRc2tnaFJTWXlCY2lOVVZsMVVpOVBrRXNIeE9oTk5NSndzM0Z3ZnlwRWY5WHFURks1SHl4YXNwSkpjZGVTZm9vTWNyQUxCMG1NYmVVRzBMT0RKVHJZNGk1MDBIcCtzY3FaWFF3a242THNCQU0vMWZ2di9qRkQiLCJtYWMiOiI5OTU2MDJmZGNjNmYyYjBiN2RjNTNhODcyZTZlMjEyZGVjMWY3ZjI5N2ZmNjgxZmU3NmEyNGE4MTYzYmYyZjFkIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"