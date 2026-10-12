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
    "cf_clearance": "XF.1ZcpD_QaUsEULjbDu8TtGYfNYrwl.BAA8sZikiTw-1791836684-1.2.1.1-kCwC0i1kuM8Q1lp58hKROHKHX38xLVIqXIQI0wDfXiBJnfCeTes2alX7MksstE3L26PZr8A5Wa6SWkWy_2CtYQBmFT7BXxy7qopA34Kj69aPYazQBcfKeGWeQagLD.2AZy7DS.qBdqYCnQbddEFXJ9CyVFZr_HamdhFVxcQX5nBsTHS62Hd8.wDiTRnViqhPH1cmH1rwlAzlK8Vt6OrfBET0_tWQA4zAYJajrrkDfA1I0oZBN19QuxzQq5ieqdrc9u6C_ajRug_bxaJ2nchSuMQgDmQp6cSIlMH201f9nVuhnX6akEAbEReS4znjSgh8ZannMs2JtpZoW50qMRadGcdLKlA972hEPF.ZFpjAy7Bk4TD52UZXo22VZMLu0GDLChEZnVqnhHVOOd6dJcWfo2a1Uo7DbR2t6wVLb22Oe_10gc1ojE7ju0Pmaaf8.xljl2PKzX6ZErHzhW8ic.oVH2cQf6XDc.2NHO7G8cyg_DrFiWLKb2dSg39WCH8F87a5e3B.AMztg.xJsdg1XfYauA",
    "XSRF-TOKEN": "eyJpdiI6InVFZ2xsbnhvM1djTWVpU0hSMGs4b1E9PSIsInZhbHVlIjoiWFlPdjkzUWEzbFgrall5eDdBUFNqcm9BYTNwTDZkTFRaL0ZiZGtuM2VnYjBacDNsWXZyaldJeUloZGI2U0pNNUROM3Q2d2RQRDIrL2pDSXhmVVh0bVBEWk5yeCszWGo5Y2tSR3BaUzNKd2tCUTNJcUpiU1NSSDdiUXVPQ200YmMiLCJtYWMiOiIwYTI3OGI2MzhjNmQyYmVhMDFiOWY5ODQ1N2U1YzBmZjk5OWYxMmRiNDczMTNkZWE0ODczMWJmNDIzYjlmZWQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxhQ21JZGJtaThzWjZsUXhSejBqVUE9PSIsInZhbHVlIjoibFF2YjBHQ1c4b3BRSnRUOVhUSkpDY2NnMFVkcVVRalNuY0lyRitXc0pYaHc3MEdWVmhvQ01oNWZYVnhOZFFKZnFrV2dwd0hLcHRtbUpQSnpBZnIxMmxZRE0zdFBzRGozVkNNWHlUVDB3OXZJbGQrUjYzWFpzelpBbDBjWUxRamwiLCJtYWMiOiJmZmMxNjQ3OGU2ZmZjYTk3OGU2ZmExODRmNTNkMjEyZDU3NDU5MWZmNDE2MmM4Yjk1MTQxNGU2NWI3NGI1OWQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "NZM4rFnzvZiyJQR6XG53Gx0mmwgkhYXi5NfWoHWVrR0-1791835844-1.2.1.1-DmI20ifpOyVwYTY_tn6zn_mREAGx09TkqR.f5rmzK7vCeO5UoGQGEEzzDg5VWY7pd84aA9iFKhfgxDe7ebfZort..zFph1sQZfwuiNq1nkr_IIsEd1hRMZHAc4S.bbyBEA00rEB5CU2Fgndvq1KPZ1SJG1VwyPwfdtyxJJBMEtoOrh_j0PduQPckD2z59A02KJVa72I5VT1xJFqXvEi2aaTrJ48AoQXHS2bi_2VhGgOSbaGtYK9g_5MR.khtaT994KPEbxXz47lHzI_1W.ISNnZdbKNLa0UmIPrb1Bk4WuHg5.DuyOecg0g_L4318_rCrkVaN4HbWtcYFUApivHbBoqAA6iP_.xPJbKyRbuq1b0yxsxbZJ4ml3azKO8g1CKCBWW5.c2zVAx4JV7NQQzTF9YI6P7d4JxoXZ6Rqm6hf7dKdnHDsFRWDtnRtg_4wC39HZoRRHajglrMT9YtkJ.s0cHEvgEaFCfwdGs5zRyob97CiZiG6u.Ia057TFgqTxaND0VEBJccEDtxL8nHcPQjaA",
    "XSRF-TOKEN": "eyJpdiI6InU3b2RXTDBNKzkzc1lBR0lzRWVKUmc9PSIsInZhbHVlIjoiZzB2TXMvbFZoRWNITVhkWHVXMStjWm5zZG15YkFGMmpxYXRLWHVweUNZbDZEMENSaDVHK1h0a21RMFdINy9KeFl2WE04QXBxL0FxaXMzdWVRT0FjWHR5ZWhEOTJGUk5RSE5MeFBkb2w5VmhzdVE1UGllY29wS3ZzeEczaHR1bFEiLCJtYWMiOiJlMDQ1YzcwYmU3ZTVkODBlZTI1MDM1NjM3ZTY5ZTgxOTdlOWJjOWJhZWE0ZDVhMjc0ZTBiNjhiMmJhZWZmM2MwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRZTkNWSUlRaXNzYUU2MStqQnNOMGc9PSIsInZhbHVlIjoiYVdETzJjenh0Nys5U25xSFlQZDQ5U2IrcU9vLzlmc1FVZGhEcCtmOWtyeGV4Y25Wb0dNa1pEdDQzUGZQVnBhNE1WazdKLzNZSXNzeGpNZlg4amFoaHE3aWdZc0FlZ1JpSEFDYTZMUFlKN016QklLUUIzek02Y0dHUm1YY2RhZ1oiLCJtYWMiOiIxYzI5ZjRjNGQyOGU0NTNjMjE2MTk2YjA3NTBkMjI5MjRlOWI2YjI0MjM2YzdmNzVmYjBjNGVmYWZiZTUyMzg3IiwidGFnIjoiIn0%3D",
}

