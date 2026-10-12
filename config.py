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
    "cf_clearance": "hyE_z5_F1r6PTC7s40kQF3m25p5nBjKAe2_onuRcjOA-1791846779-1.2.1.1-zFiV5WRHsdAJOpQeFjP3gDYKOcZAOvoQihuCnnRRCz81JtqlIZZ2u5.lJtgaSE0NbVvTF8bY1DuBkMenBKenlJ8y6x8cHROyFmtkDaycAJByL01b2f93sc9vuPVdy7vjNE1ZEDTwOxho7wKxS87F7OFyI.ymEgi_P2hY6yQX7aPOLZyY4jFy1xWLozLUBgRVOv33LMzv8beTeMNUmyk77VVWlMrj3Tf2QkWP21W8qfp2Eom_8rrePWoVh7DEwD63qVhP303BJ_u_CShhG05lCwKCTPU4vkjYRgKcjUODEUxTqgS1DTmm2xlNryE_wTT8TzqHdw2gFSLbDUvIhbhIkU64QPSmtPlN5HBE5IiCjVdSU4oujUNqXu99byqPf7qwrmyUiWSYrWbumTTlX5WdP8aeAyLrhIw262xWRqtSazfsUDt5L.RJK6LcJZK.zW24clPOctoxWNPZrgmN2xGpXJ1NwEeQkN9H89uYyJWyL8FONjNp_SUsUWpaBvqTifkhHwreSocjwvlPOx4mWyNTaA",
    "XSRF-TOKEN": "eyJpdiI6Iis4MW5CcDdhdUowbjRtV0RsZndmWEE9PSIsInZhbHVlIjoiRmhFWVdSblhSaEhKZnRzanJzUGlLZWNsdmNOckk2dCs1UDluTkdXNXNwT1lFSGlwU0wyK0o1MEVIb3kyQVBVeHJTdFY1d0Y5SENGZml3cDRnNkZCY0Nkb0dSR09KeTdLcjB6NWxoSklzVlBzMzZrckJIdjBkNGJvUDJmSGVPSmoiLCJtYWMiOiIwYmRjYjc4NmY0OWZiMDY1NTBlMjU3ODJkODgwM2Q3ZTA3NmQyNGZmOTE0MDRlZGZmOWU0NmIxODdiOTAyOTAyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik54eEoxNjlxY2puczJndWpUZk1Ibmc9PSIsInZhbHVlIjoidWdwbFVzUHpzQk5wV2JaVFJUdW5JWTQrNnRKOHhMWEI2NVNpTFRxV1E2U2hqYU1GSDVCUmk3c1FmWWhtcHRuOVAwNDRjaW9KNW9tdmpzTnZIbVdIYk04TUpoZ1NoZlpNQjZSYjlnOU01aDZlTmNMKzZNMVpVa1c5WXZkV1BmaDIiLCJtYWMiOiJiYzMyZmIyYjNjNjIyOTg2YmZjODJhNzE0Njc3MjhhMDFlNGU4MjE5YTgwNWVjZTE2MjY3YzdiZDhkY2QzNDQyIiwidGFnIjoiIn0%3D",
}

