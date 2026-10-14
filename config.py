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
    "cf_clearance": "Eixb2yHes1ecDp.HDLUMHL3qyNl1DCe4cpIuKekBHn8-1791967459-1.2.1.1-jsM2bPV1eMEkndkIVd9zVSo3OuGMr8gvxMIStskQNCd6JpDX8GlwBckFe1mTid5_O8vFRu_HpV6_2hTPKFVYjmsZv.LWcFszhiCO65wG9oNApfCA1k0Tj1lSNBYwFDCRIjTkDSxMM7JGPpF_wITdffwIEACWzUXzauWEwu.e3u5VZXbHsag0IcGWpOLYsm6sVfZ3cUHAJRNqSJ2TGPYOpt90hNYO.Wd5W5djMXdW4naHifL1p_Sa4z1VuJj98DETlEhowSeZfTWCk2XowFYLZDn854yhR3Y34DglKr9ERe8_TUoZZ.5JSJsodgEXpnbS_ocr4FEke3BbX5qUGuejY7Nlm4QEJPVNQqJLIpxlrRpB05NNj6fY7tyMP9QAWE5ejSU9xYOmxM0qCOYCOAlWjhdWrYnYT0HPGjJtIoA7nNTy469ULLU3PydWn3OZV06Z8XGXIMxSVozF0hQiVcA.WfpZ83IGKYZ3Pzsztil8QwYtOcJEjvdGvmmIX107H_skRNj2aZOzXA8x9j0.vOqzFQ",
    "XSRF-TOKEN": "eyJpdiI6InBiTzNtenZUYVp5MjY4WDdneHkzL2c9PSIsInZhbHVlIjoiUC9mb3VMV0pGalp1WG5mTWh5MWdOQy9ybjRPa1JMUEtDS3BLek9sdWJkZ2dCRTFibHQ2Zk9DaWp1WTZrWlFtVjBrWFR1dkY2OEQ0MXcxL0xweVZrMTIvVEE4ZXkvaGduaXhHa3lOZjFJb3QzbHdjSjRQdE91c2JCZDA0TUVsRG4iLCJtYWMiOiJhYjIxOWYwMGZmM2JmNzNiYWM1MzA1N2E5NTA5YjA2ZWI2ZDc3OTNjNmFhYjA1NDBkMDVlYzdkNzcxMGNmMjEwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhVaUhxajNnQzlpeHVFMVpaUjBlT2c9PSIsInZhbHVlIjoiMHNydG5WeTNwTUFrVGNMT2c4UHRObDU4ZndxS1BaVCtnQzI3b0Uxd3p4QVVrVVh0dVU4YkZCaVNJVUhEVFB5WWNJbTY4THJqeDZUTGNieGVkSFB2YXFiN0lYdWxkR0laQU1ERnc2ak1HYVVyb3FMdlF5dXZhNTN5cjNPZTVqeCsiLCJtYWMiOiJlMzY3ODgyNGZlODhiMTM5MGUwYjEyZDcwNDRkNWI1MGY1YTZlZDA5YjYwOTRlMGYxNDA2MmFhZTE5Mjk5YTE1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "jR31xyELaA5Jm9KMhrPc8rOYOI60QuFhcRZFGHQTwjg-1791967557-1.2.1.1-kJ0DwyRT8RRt5fRKXJKgMbBjD74k9_1IbDfu1ztlWU0XoE_0w2THgn15ATvoFED1tWz2yuTUpt3.AnzRgL.8yLxMVSmyOlB3SRNVuxdGXaCvZwu5yiXBDRNmEZA4zvA9VM_zXsP7LHoMO2heVzB7mzCUFJI65OpoRRpQq2v880z2tTy6oTe9Flq0K8x_3X6ieVtp4tGduV6m_F3VBTct1xxZzajkf8mIsHKimOeykZ3N19PnHyWanFCdq_E1ojA3haDd_5ytrOoHe5LMqbzwSyoazOZnApOELcVX1sYGCGlcT1QB1CrQroHvTBksv.Xll99HC.z4sNFlS8YXrOE8csUW4.cQqd4ynMtuV7LNXm7piGVvNtovbR1p4GAHxhKQW1MGE1IlsDBCJFaoYMZOxOmEPaT3GKyGtF7Izc2fOY2YDtOWmlTw0oP7wz_8u0drpSU7.8OpKtvp9ig9KfmOwco8ubS0bskKAqb.l0lhRMWy5MhJLHUpAnyqVheCAlYGuJ7ke2Tc_Ed3cCEJqHrWAA",
    "XSRF-TOKEN": "eyJpdiI6IlVtRU5FRzVnQ1R5bHBZZHN4VTJLYUE9PSIsInZhbHVlIjoiZm1DazV5bjcwcURoTFJTWUpES1JXaXU3aXAvRTNKZGpWVy9CTHVMdHdxWWZLTldnLzNuWmpkWUh2Y3YzRHJLL05LSE1TdkY2b0xnNzlzMkhaKzNveEJ3WGltRVh1VjdPSzZwdkdhNndQSjdNQjJtd1JPdy81NWFSYWRrN0RkdSsiLCJtYWMiOiJmYjA2Njk3ZGYyZjUzNmE4YmE1NzRjYWQ1OWYyYzFhMGU3NjY2ZmE5YmI1Nzc4NjE2NWIyNzk3NTk3ZDdjNzhjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJXTlZyMGRvUjVvUGlXY01ISHVBRFE9PSIsInZhbHVlIjoiNllWU1EzSmlwZlQ3YVlYV1NjVW1seTIvY2c3VkNQV0haY0JVcTFsZmNEbFdtNnNDMzJVUmYrT0JsK3FJYVVidDZJNGRWdTQxdVUxQzRwY3cyUHlvdW1GNTdBbTBqWGVUV2U1Nk03Nk5FYllaVEJwT3d5NUs0Q2dVZ2pUQTJzWDgiLCJtYWMiOiJiOTQ3MGVhZTI2MmU5ZmM2YzQ1YmU0ZmYyY2UwZmE1YTc2ZjY1NmJjMmM5MzMwNGViNWQ3MTc1ZGIxMDg4NmZlIiwidGFnIjoiIn0%3D",
}

