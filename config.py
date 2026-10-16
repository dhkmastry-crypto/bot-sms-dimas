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
    "cf_clearance": "7wwjnt5rPMNpHNHfAYir4YPJEbZpg.bsCYEnZSurcmo-1792154305-1.2.1.1-QOcRu.SwH9mxd_wD1aB2iEHdqyeThKnf7QR8GAz61OgYzCJHXyYC6Ba58UkSHPsKIFrMpmUivl8YxAYTkcyFWRCAa3t5NX_mDcTQkLp1IWT2vTlDUebQJYMkAaX_V4rmX58e.BbbQZkpSmfYtF.0yILTm9bAPrblp7p5PIFMkNup_SMs5b3dHEVpbvrWFfYpkOZaNlKNGYybttkoym.lIprmTs7ZyWymHeg1p2HN58e2.ohKnl95e3Jh9DbIfU0CA5JL17eRXyDZuFlJbS6iklWE8l2X7C4TBZ7TF3wW7ub9kugoEQlo3.0ERDPbOiLn2FtS.EMidQOeVNp2fWokuGH0bYgvA8.01NVB2NWYUKBu2POpuxhMvC4lu7jhTEDo1llJmz.6IIAApZQ4pclD3XuqNmojGwTDid8ak7m6Rb7mb6QX5qXF45PAi1LIqTsaXLkpU7P6i5DnKKxO7HnaGe9AjhH0EAQjO0caoq4vrTM7.aa6CmpsafOR1XlD9walE1nOTbZtaGmTWYvv46w32g",
    "XSRF-TOKEN": "eyJpdiI6IjllY0dzajlRV2NTcEdURVM2REhUL3c9PSIsInZhbHVlIjoiZlZFMFRTODdzWlExYk9IRGxPUlJXTy9EWUgyb0RDa1p2Q1FqdDhnZ2pzekNIa0JOS0dRaGQ4N1JqeTVBc2VrbTdTVmhaRlJSMjlSaFlHVWk1aUVkUkVTWHBoTnI2TGY1N0d2RWo0bVFwaUdPYjN0ZkxaaEcrWXMvUEJEMytvMnIiLCJtYWMiOiJjYjIwM2I2M2M1Mjc5YWEwOGM0OWE4Y2UwNDg5NmYzODExNDg0ZjM1ZGZhM2FmNjk4MjEwNzY0M2QyZjNjNjA2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFOSXoyVmdoVFlKZ0tiQjB2MERUNFE9PSIsInZhbHVlIjoiSDFFTm0wNkM2eE52eEM4TERGQXhJcjBPZ0hXdk9lcWtzQkVtRnRueDBuK0QvKzFoYjFOMDNQSlRYSm5DcGNhZ2htVDRpQitoRXJoekQvWE9HVVlVaTYzdEpWalNTRmJvVEdpQkErRCt4Zjk1YzYrRGVJU1FoM3Jrbm52RzdYZmEiLCJtYWMiOiI0ZWNmMmIzZWEwZTU3MWE5MWY5ODY2NjgyYjgwZGQ4Y2ExOTBiZWE1ZjE2YzAwNjQ2ZjhlNjkxODgxZTBhOGQ4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "b8ROV8vXxqS7IDuMJEUGYw41BVOEZZgfoNChKDcYNlE-1792154324-1.2.1.1-Hyv82vOlbwddEuar0BZBRRjE_.VBfYAb0QOZVxWqhYApsgYT56VGU0sgQNbJGsZIiYOL_Kq9rYqgR54TTk3mbfTxUYVQANx41g6EzyN9sRX8bXuuaQYupeYqFZzVg.tCTTXP0V6pZo4q7dfUpoCeuA74OJJILmDTeEC49dqqoBGZnOZKga2scLzxmiM9gpR2gwLJL7bjBu3wCdEfsuc1BZlq4iPweDOyjJGmkPho4heQzx1JIj8zcLka9haR9G.BDIYQHtvZSdHPDNNC5qG31XJbLWkAVA1G4MATAm3LC_m2AzYLLc17ZXT_YdOZttmUF3tX7ISphPFrMXeGdsmSnMFDW4SbGjO1uhrX6bmXt7E9rdgDD04t.jmeIhbzdhRqjjMbmkY8nSsJ835y32BQ08049Fj.k08Nr47UDtibwZ7T87Oatm6qW6tgHMPr649OgJzoVbd1bco7h2NTHFhdffRdOZGSYu197DnUvZZ9uADW1b54FINcq9YTz5ul_EyYB0zzcDrCKSPPOHZ6o.9hTg",
    "XSRF-TOKEN": "eyJpdiI6Im1BQTlSMkpKM1IxWnh0NTVHYnNRaEE9PSIsInZhbHVlIjoiR2EwMk41bkxvOEo2K0RCMk9YZkNTclNJTlRCd1lVRG5OUHZmaUZMc3VhNWE5ajdUM0xVTGt4NU1zREM0OXgzVXdKNUFaQUtnT0RQYmlTbEJvVlVHNVNDREhjcXFpb2JTZ2E4MmRtNDlPSUdqdjBkUldpeVM3QjREWDhucnJvdnMiLCJtYWMiOiIwZjg0YzhjMjhlMzZiOTJiNDMyYjQ3OTQ0MWQ0YjNhZjNlZTRhMTVjNjlkMzVhODUzNjUxOTk5OTMxNzk4MmE0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhESXVrTEJpZHlkeWtONHU1bHVpemc9PSIsInZhbHVlIjoiSWszVDVVVEJxSlp5OUF3aUdNQkpZbkt2RkJUcFRNU1NKOVE2bU14VFVJbERWTlN3LzBrVHhTRHcrNjdIQUhUWTRKYlZTMmdqZUQ5YTFsWGorNVdnWVRFWDdqbStMWE1pa1dKNEFmd2Q0WXlYV0NxQ3lINStBb0JWVXZwUXoxU1YiLCJtYWMiOiJiY2Y2M2Q4NzY5MjA5YjNiZDFjZWNiMDhmZjljNzllNGZmZjhjOTk2ZTE2NGZkYmZmYThlYjk2Mjg0ZjVmNWVlIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"