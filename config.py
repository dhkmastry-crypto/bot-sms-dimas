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
    "cf_clearance": "qs.LHtv8OAxJQMmGmKHWma2.8dSo.rb9DK9MVKxyRFw-1791872852-1.2.1.1-zcIAxNUM.JzWjmHr.swzNvP1MUmJ9rSpQhyd7bbzmXipGnUZohXpuPN30WjvkQJLhMNS1jNHqcfZXBjMwvPdegLxIwqvBluV1Hi6J4hXupFlyZKqOiAE8tFY0o7puWkAgF1TjWe6OlkRrjmIIk4Bl6sXPRbrEF68lpXpsxxs8JNXTQzXFgrbDB.Hc0._wH71_RgaZBWJ09MUazG1Td9u8QEMVCxZxa4cEIJ5BeG3W2QhUr01bMyKldyPgLm38I_UFowBJ0k7XE3bmJ8sc2NFaJCKFpyDridPDgST95ra5IfJ6yix8aSuKYRddgYvlBaLDynFVmeECDmgIUqlcvdwLRNMOF1ZVJwtKOa24uG4RP7vfHlRbypPByLXpg6q7KZQCDHxE4qS872mkkLxEB45JvN.s1PxJMqeekpa2FovhEtf6KZCE4NT.VfflUax4oc6322CEZPtOmLxZYl0Yb4b3cAnHR2scCScTdXfZrFB3PlZP90yfmt3OLthu6vGxo6riSSbjMNK0..VlAV5vorbuQ",
    "XSRF-TOKEN": "eyJpdiI6InFRUW5ZM3Rmd3RwRW1jcko3b1FNSXc9PSIsInZhbHVlIjoicTVVTU5MZ3EzU0R6dkVoUldiMTVvMWZvYURaelFZeTVOa0JVa1FWOVJMZjFvVDZuclJMdGRZblZXYmpKZ1FIOU1ZNjdUY1A0NHFXWXk4QkNSNE9KM1JoM3NmbzJvYXlOV01lK01KK3JCdWZGTVBaVHhNQVlyRDIvQzRYWGp3ZnYiLCJtYWMiOiI2ODg2MmQwMjI2N2ZhNjhjN2NlMDdkZGM1ZWNiZjYzNzc1ZmUyOTNkYzk1ODgyMjZkNmE3Njk0ZGE4ZDE4Yzc2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImhlMG5CZmh1WEdOcy9ndFJneGxMMUE9PSIsInZhbHVlIjoiYjAxZSt0M0RIMTNqME8rWmp0YnZuMitzQzI0K2JKSW5OZ2M4OWwrV1Q4MytHOVVheWlIcDB5UytZUG1YT0tVU2lIKy9hK1paSHhVTGR1NTNGQVBDUnhKUHF5RWFYcDM0c0liYWZTc2xuLzNyNmJzdk8zcmM4UW1HeUxLREw4L3EiLCJtYWMiOiI2Njc5YzFiZTg2MmRiMjE5YzUxNDcxYmJlM2U1YWJlMTQyYzE2Nzk0MDNjMzYwMGRmMjQwOWI1OWNhNDBiNjU1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "uUvYBsCFdKK3RYq5VTqBXcxilf6uKkttCOSf0CEfBBY-1791874055-1.2.1.1-y18o47j3mXWgmnhB8Ci1..iA.kVMlK9BudgQU2kgoX4v5oFD74FhsrcKifrsKLlfwykZHslLrU7w6no3ItmenEQVcLCxk6Ma_AXZ9JVnqi1JOKm64dL4Wiin7wtOcQQd7ZPlLl8pl9NZUWGjaHchlxCFqEQQyaJmdRSK26EpA6C9f0DUoIf29lEFgjuH9jcLIcnPMjwpsmmQ9JFI5TUEx2MHp1ue_gaz2c7n_ZYmJHIHLFkmB2fiw9p0EW4gjoJQqI1ZtB9f5CUTLxPf.CNl0w5K0N_HW3ZL0c9uiD_33JNuQdLPOHxXepdHXeXQ6n_P29LiPsHYSJwhaim_kARsBZcUYn72aSy_s0RkKH8zRLvsBZ6ciVEdYwOCdYlKLg2zu7dgwBFgUJF81MuXw37MPP30fMzcvXUGNFWqlF6BHfQBTvJq2VlH2Gn4qt_HlarL_3qMmRGe8kK44tuFNylpQqHf.v05oamo.S4O5sM7SjbJXuKLwZWX75cdiS_LvZn3GxlCHEw0SiwBhZAzU3g4qg",
    "XSRF-TOKEN": "eyJpdiI6ImRYZFlSVmtMemJQWHprdW5oRlZ3V2c9PSIsInZhbHVlIjoicHljWCtkMnRpOU1TdDArYkRtcEhWZlpERVpsa0pVaW9MRFpza2Y2dzIxcXAwa0NiaitRMWQxeHNZOEZKT2FPR0tTVm9jRnZrRjBqK3VpY1RmUTFSK3dsQzc2RkdzbUQ1Ym5oMUFmZ2xzTGxackJONGhwL0RHUkYvYlkvc2tOMm0iLCJtYWMiOiJjZDI4M2U2MGE1MTBjYjFhNDcyNDcyZDc4OWQ0MDBjN2FlNmEwOTFiNzYzNDYxZTQyNWYzMjE5MzEwMzJiZjFiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9pYm5BRG4rVkY4aVNjSEkwVEFwZXc9PSIsInZhbHVlIjoiZjRUR2ZOcVlLVjREYTBZVjIvZFBQVXl2eHRYbGh5ZWN4VTlwQ0VXMU9leVBFb1dTbjNORiswNjZiWTNIakN0UGNWRmhqMU9ERzB1d2taS2pFcnV2UFBWbWh4Y0J5VG9XTk84ekhwbkdTZnlmck5jN2NXd0RyUWh1ZmRTQ3hrYmgiLCJtYWMiOiJkYjFlZjFkZGY1OGYwZTg0ZWUzM2YxMWE4NDIzZGFjM2IwYWM2N2UwNTk1MzVkOWQ1YzY3N2QxYThmZjQ2ZDVlIiwidGFnIjoiIn0%3D",
}

