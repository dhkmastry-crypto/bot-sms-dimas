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
    "cf_clearance": "2u_CaizP2InLSyvSQWdicnPZLGpda30K84MhJJk3.y0-1792121705-1.2.1.1-lUeqp4FXaxb.EhUQn5VQ5nxh_.LUdRrO3Qm87ou27jbVDP5s9BlnPlg3WohxUoHNHLZ.1fut9264jCnmoErP70Hq4rabxG5cI7BB5MjkNA6bM6jAQ4eZef7M_GvEiFEmZQKdOwNQXvHO725ke79iZvAUDWzAKyh4rGuda56EbC86FiFPlPh33MyI9tCJJGuBtz_5ynVNZCiCygjolSGX3v0lsPdIgW6kTJ6Ce74dydXIbvFJNUp1YiopEldQP8rOncslFDn011kV73Ra1JQLICLqCXH6oBu_UmdUNt3iyFEXjge5yPguCdKbG1kyVUrWkK2VlXc.UcLZCpbfgV0aPTXPqkOngJ2eQgF9EjvTkxUj23OtUSrLyLPHTfLsCf7Nsf7wthgGDuOzmi1tcQRhLfsh831iqMX6Q7gRZmJetLlmzop.Yb2g3IBh6oSzhvGj_wDgDNQb_gxMSllhL.jb4nirQcns2ysVPGlERVRUrwF_fveVBB8DO_7hy7k6FqPDKIskQj6BiIGHYGpuOv817g",
    "XSRF-TOKEN": "eyJpdiI6ImMxRHk1cE5zc3l3Y04zcDcrM1YzVGc9PSIsInZhbHVlIjoidGc5MVdkYTZVT29vdDloM00xYldyT21ZbDVFdjYyeUtoWURHbmR0Um9QaGh0RFY0VS8xc2I4ZXZpRllWOGpkcFI2MVRIZWlLbm1UZXV6dGYyVzllcEt3MjUyRXdVY2srYjRVeEcxSWFmbVdMTndMTVBaTDB6MmIvR2FvbjFXTXMiLCJtYWMiOiI1YWY0OTA5NTczZGM2YTI4ZjgyMjA4ZjY5YTVjZDQ5ZDZhYzA1NmMyMmVlMmUyMDM2YTU3OWMyNjQzMWE3YWE0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZXT25SZndMLzJmeXFWVGU5OE13Mmc9PSIsInZhbHVlIjoiUDZuZks2c0M1akxXQXlTY29ZOHIxS040YlEzMHhNWnJ3SEljZHczTHFDOEhIU2ltN3lsN3YxdWpwT1VDYkZFbmZZY3c5VXk0bUJYUFVCL1hOY1lrcHlLRkh6Q1FJL3FGWmgxR1R3S3B4M0dpZTlQUm5pR1BqZ1JMcjY2VEExNUwiLCJtYWMiOiJjNmU4ZTJlZTFmYmE0MmVkNTFjNDY5YzA4NTQ2ZjJmNGQxNTU0Y2M2NzBmMTlhNDlkNzgwNmZkZjQ2NDA1ZjZhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "mVKH1fD1ClwsQZH3Z2uq0ZnMR1tAhPxEk.JZX_6hAhI-1792121684-1.2.1.1-Hq4tcAeQ.yuyqHc6RPEJkRnHKLJBG5L5xKEr00P01a9pzmRRwr.sGphB2aDIpzTJ3IUoPeeLMiASHln8A3wcnh86HgHRnifssFDPgO2JlJVVhzX_Lk_vvUjh880_In39auSmm8mmmr80zoiAJ3vMDjypI.WBERqd4pZy6mrjuQPyJlxUC8cqvjBA4NQvKbN5ApSTP0RH5eo8PHNbL17kUHIatTsHhaGnouP6Vmu0h4_yHTJajTzwt9TVdfrU6uaGLeUSC1M4ZoqxYxORLM5.vedSb6PI59czJIK2pI_zkeiBDn_3_UPW58RZLEKwncRkBhH8GUg8b2cMUaxscqeSOcyzHCn6rvpBooCjH8.haX7c3030WkQtuUyJj6kHZP0CkURNXGb801c90.sggeXjs5WwSoGn0DGY1cs3EcSUt_CBJfrl08lh9nFA3OK.2vu6UI2EmCDAdIK475umOO6slDE0H00dTIactz3RY2oX5YSFZ82u0xxT5oBddYW6RdwmlxBwTmHh6FaVVBNPK0FugA",
    "XSRF-TOKEN": "eyJpdiI6Ii90VTFIRW9JYnVhWktodEI3ZUVtL3c9PSIsInZhbHVlIjoieGVqWGhoZjBRZlpnOVNWOWg2VUlTTjNmNnpQMlFnNmpCTGJuZys5c2xBUEZKWjQ1WDIyQWU1bTdia3VYdVZDUVNrUUlKUDdJb1FPSHZGd2hyaHhrakQvZDJ3V1F4cTJDUDU5TEM4MFFVemZxSzlrL1dCWDF0SjZuejREWGtnckMiLCJtYWMiOiJkYzA3NjEwNjJkNGJhZjdhOWY2YWRmYjE5YzUzMGVmYTU3MmY2YTI0MDZiZTdlYzczOTgyZmJkOWNjNTNmNjk5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IitUQnd3d1NDdWdyUXppMlppRTBEM0E9PSIsInZhbHVlIjoiY1NkT0dzTUtkUHpUQURpd29Id0FqaDU5cGNDdXpTbjM0WFdiVmRsc0ZZT3NUMzQ4UjZNM2IwcERIL0RneGE5M3d6Vm9lemIzRXFZUGNJeXQvRmVqbTVIQk02Y29IZlN1SHpqY3pPbFpzWk5TdEN0c29nZjZXeTdZSlpJalRjeU0iLCJtYWMiOiJhZTMwY2M3ODIyZmZiMjliYWY2ODU5NjlhYjc1ODMxNjkzYzFmZWFhZmQyY2MwODI5Y2U5NDk0NmExMjRkY2VkIiwidGFnIjoiIn0%3D",
}

