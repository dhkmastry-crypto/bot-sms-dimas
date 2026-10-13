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
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "7C5kud7CbfkUtScgm3ANpLCfLmnjI7YkDrH0SNmV.r0-1791874659-1.2.1.1-UKBW46Hi9TMIicMeVjnyh9OmDriTvCvsaytqDw.ahV9uZVRh5KNoHhzfxYRSCKDm1DPZRfSPg_kWC_RxkJ0occnYD66H1ddwxxcHIS92iqDpJnGluDluTMnnv05aWAsOhZ48Vc615y7dxPPB3bFNNb64kHL7qX32p6CybsJNkwWHk.WTSIbvjvTuCF1lWEw1uJa0RoP_og6lvYOXbPp2IS0IIwkO6lwRg5k2_TGZjNOXMVKsIV8jHsO2pqyyNLG6JIZnQ9078ye7QmkvFr3CpzzGOpM2J5jiNuyIp85KFvJEoFRN4TDQGkSWyS7wDNpgNqhyLpMh2CoCGatjT8VgHlts9HPsI1r2cUjVYvC_57cz6slY.ufqXLHE6Q0kdQDN1wkR7_DszFuE5gSB76f7BMv.1pni4Zck3u9QBZXmfC_LzSFxzrQ_n897KJePLw_vS73dWvvmRyoZdcWK_Q7mSKSwoEki.6q5swCC2RDaW5F6Ty2dpYx4ud.L8Hi1ZQ06rJLN6tAc64zXJsij55i3hw",
    "XSRF-TOKEN": "eyJpdiI6Imxaa1ZZQ2dvYXZ6R0c1MXlJSlRrd1E9PSIsInZhbHVlIjoib0VlMm5KTnV1VFdsaFI3dkVZVThvWkxWeTNEZlM1bDAzQmt2WFh3UnY2dFovdERuTW1wcmlMNXZ0UWJxRjg3YnoyQXBFQ3FXMGNsRitPYzl2RzM1eGtOR1FxZW13Z1lXNUlZUitOVFJjVHY3WUVHWXY3ZkV0Y0xYTGpXNnQ2M0IiLCJtYWMiOiJhYzJjMTkwODI0YzkzNWQ0OWIxNTJlNzZjMWQ1YTU3NmMyMjkwOTVmOWE2YjYxODY3ZTk5YzZhZTI5ZDA5MGRhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InMvUkR4Z3Arc0ZGUzB4a0V0MFI0VEE9PSIsInZhbHVlIjoiWHk4S2ZrMnY3UGFkT1JaVHRUakM1SXNOOXlWdElxdnVmUFJaVUp5ZUZlZnVLTXV6c09rRnZsWDBTYUQySFZ1QkF5eExRYVNmQVVlQUtSZ0dNaVlld0tWb2tQbEx4cmxWSGM3S3dwekIzVXNxMUlLVUFHY05PL0xUZjhtb29ZQlEiLCJtYWMiOiJhYWU3ZTI2YjVmZDI0OWEzNmJiNGY0ZDVjNjBiYmVhYjUxZTJmMzM1MzhiNmMwOGZkZjI0YzRlNTZmNTZmYmM1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "uUvYBsCFdKK3RYq5VTqBXcxilf6uKkttCOSf0CEfBBY-1791874055-1.2.1.1-y18o47j3mXWgmnhB8Ci1..iA.kVMlK9BudgQU2kgoX4v5oFD74FhsrcKifrsKLlfwykZHslLrU7w6no3ItmenEQVcLCxk6Ma_AXZ9JVnqi1JOKm64dL4Wiin7wtOcQQd7ZPlLl8pl9NZUWGjaHchlxCFqEQQyaJmdRSK26EpA6C9f0DUoIf29lEFgjuH9jcLIcnPMjwpsmmQ9JFI5TUEx2MHp1ue_gaz2c7n_ZYmJHIHLFkmB2fiw9p0EW4gjoJQqI1ZtB9f5CUTLxPf.CNl0w5K0N_HW3ZL0c9uiD_33JNuQdLPOHxXepdHXeXQ6n_P29LiPsHYSJwhaim_kARsBZcUYn72aSy_s0RkKH8zRLvsBZ6ciVEdYwOCdYlKLg2zu7dgwBFgUJF81MuXw37MPP30fMzcvXUGNFWqlF6BHfQBTvJq2VlH2Gn4qt_HlarL_3qMmRGe8kK44tuFNylpQqHf.v05oamo.S4O5sM7SjbJXuKLwZWX75cdiS_LvZn3GxlCHEw0SiwBhZAzU3g4qg",
    "XSRF-TOKEN": "eyJpdiI6ImRYZFlSVmtMemJQWHprdW5oRlZ3V2c9PSIsInZhbHVlIjoicHljWCtkMnRpOU1TdDArYkRtcEhWZlpERVpsa0pVaW9MRFpza2Y2dzIxcXAwa0NiaitRMWQxeHNZOEZKT2FPR0tTVm9jRnZrRjBqK3VpY1RmUTFSK3dsQzc2RkdzbUQ1Ym5oMUFmZ2xzTGxackJONGhwL0RHUkYvYlkvc2tOMm0iLCJtYWMiOiJjZDI4M2U2MGE1MTBjYjFhNDcyNDcyZDc4OWQ0MDBjN2FlNmEwOTFiNzYzNDYxZTQyNWYzMjE5MzEwMzJiZjFiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9pYm5BRG4rVkY4aVNjSEkwVEFwZXc9PSIsInZhbHVlIjoiZjRUR2ZOcVlLVjREYTBZVjIvZFBQVXl2eHRYbGh5ZWN4VTlwQ0VXMU9leVBFb1dTbjNORiswNjZiWTNIakN0UGNWRmhqMU9ERzB1d2taS2pFcnV2UFBWbWh4Y0J5VG9XTk84ekhwbkdTZnlmck5jN2NXd0RyUWh1ZmRTQ3hrYmgiLCJtYWMiOiJkYjFlZjFkZGY1OGYwZTg0ZWUzM2YxMWE4NDIzZGFjM2IwYWM2N2UwNTk1MzVkOWQ1YzY3N2QxYThmZjQ2ZDVlIiwidGFnIjoiIn0%3D",
}

