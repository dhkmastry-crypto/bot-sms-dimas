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
    "cf_clearance": "mIJ41TBNPjsvIlGcafrzYjQkpNzVKbVhuzEBO1rRdmc-1791847540-1.2.1.1-3QPM_1newUWdo2e.QAOobc6KpAc4hG5JPUxUiJ5OlWLS3W6usathQH8mp21Y.r2MonFaGKRPetEK2kknqlud66HNykxsNSZOWWFqFKhRiXmbM36VdaDumB9CeUIUa1NogduIGi5Bv4jkNoWrN8fpeUOncwGsM4zA332lrfZ9IyPxh6g52gEdoARugNUwWbERM0hv30LLfD_boyyBM7tRk5bU8S7nCah3kR.7pYzP3n9oXZveJv.pvZjAdmGQ2rcVo5b3zOLdN7Roescbw_H6tP4EUmJ8_eJFgsbkBrplA2XTFXaF7hXu_b1ZnkX6LEiDM272emKlP7iyXLRHfvY.WZTNTCa4Pxv.kVhDiZ_s160D_x_S1fKG9MUhuburhUidIbr62MmgweH2T_Mo3PmXDKT_AaApKB6FxKyeBFR.egTRqq4iHGKtZMEXtSiYaRqwtnFLclZBIadPFU71MS4wyaovMpyxmobP.TcqwXQMFQSCGUEOgUVA1UcG2GzhpOhWCD8Acz8643xZ5zzz_OrkoQ",
    "XSRF-TOKEN": "eyJpdiI6IlJQUUdTU0FyZUJtMlBQaCtjVWk0SlE9PSIsInZhbHVlIjoiNUpxbzVYTlAyai9CcTQ5d1VFa29qZFEzT3kzK05UTTYwR080OFI3TVJzaVhMaEFZVkJHQytOMkI2NmozdCs0d1BHOXZ0WTRZSFNwVVhva09Sbk5RMndkTlBRbGxZZFJHYWl3VW5sRVJTU04xS29saGNkRnNCNGJCVmxlbHJLbnUiLCJtYWMiOiI0MWZhNWUyMDNmNWZhNjNlMjcwZDFhNDY2MzIwNTc2MDhjOGYxNTM4Nzc4NWE0YjEwZDliY2Q4ZDM3NmEwOWFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlUzZ282TnhJOTl6NndzR0NWT3FIalE9PSIsInZhbHVlIjoiRVpOU1VhZ1BsOFByaEVjZlNjRjl4S1pSY2RRSUJFelpINmtya01aWG44OVdHL3VXWUt0RkYrUGFhSkQ2dFdtQ05oOU5ZaHJLZ3VIejZDdUtJcjlRTklHbmQ0blVNYXk5Zkg2RnVZMWNqL3J2aEtjVDhjV2s5NEl3MDhBTWNNS1UiLCJtYWMiOiIzNzZmMmQ3MmMxYzc4NjM2MzRjODJjZDlhZTJmODU4MDc1OWI4OTA3YTQ1YjljOGNiMmVlZWMwZGYzNDNhZDZmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "1BoWtKilLtQtwxbpvCr_4qQrtVN.6pz3FWiF.CRcIAE-1791848699-1.2.1.1-w9pdQWYFHMuCaqXzu2t7FN7FyD0DX7tY_z5MI7KBryBkVFK39voV09DK6A6wJsvY11obTEw3dyQrBRbpuRRwa7NyJTXprf2qZhglcbfNHZJ448XLFKu.LroYJ3PPCW6EwzP7a_WQiHxAkwuuZIVMjps2GcZfdeNcWbcGvErKEr.uKBlc2OeARFX.IIOWCqIaueqrw3RQOn60TkrB33UhYbzsw9myCyGtoPqNa3Nu7YKLkRXt9Lvfm5X9Nc.lsTL4bG1XXyPZFJLK1zRl895B8d_OcCLKyp6KboPOeItlu8NJTwKiTtQK7uwi3m_w8em42HnYtBmRa7PDw1UXa29nhtPjiTIF41Vfdg5Kd3k0ttI3ufpiz37gv7xVPLBiFxm6Ect3b0cCyWhUS2OYrt1xwRC12VwW4CsZtEVVSPydXYqEBj5nzrzgZlvu.UiJJPPYuYfqCuKSEcr1rfn3U7j8i7V677XCzh_wZlW9W_uuC4LLoHe8Vto1yhR3ECOHA7wT5OOom77FX8ZVjVqCjDYELQ",
    "XSRF-TOKEN": "eyJpdiI6IndONy9nOFJua3QyUlhyZWFERllrdXc9PSIsInZhbHVlIjoiQlNDTzZsN1NWNHRjYTFZNGNmK1lJbC9semxpbDk2MHVHZCtXQUxwc2ZQNmtVVUhVelY5dFcrOGZsb0t6Y0VqSUl3bSttZTF5NFh6SUhtUXdoRkRydmd4ZGZtTTdnc2xtd3hMaDNSUnF2dE1qa01US3VnSW5Ld3JLVkNUY3Uxa3AiLCJtYWMiOiI2NDEyMDI2NTFlODY3NWNmNDg4ZmI2ODZhZTMwMGM4YzVhY2I1ZDBlY2FkMzA5MGMwNGYwNjg1MjFkZGIxNDVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdYdFVYVjNxVlNYU0lEZk92WWNucEE9PSIsInZhbHVlIjoiUnNKZnc3SFlKMjh5Smh0WWVidjlaS0hrSUdJOWYyWkRqZ0ZDVGdkTUJuVnpZdG84K1o1eWZXTS9wMEN0TzFGY2J6bEJpdDdOMkE3OHZwNk5jMVJDZHRqMHh3NUp1V2NZTzJQSnBBUENPdjdvV1JRMHpEdDVnL0hxdnl4cTNvWFQiLCJtYWMiOiJhMjI2MDVlN2Q1ZWViNTFlZTFiYzk0OWZjMzU1ODU0NGQ1N2EzN2JjNDU3NTQ3NTNiYzc4NDcyMTI2ZWFlMDkyIiwidGFnIjoiIn0%3D",
}

