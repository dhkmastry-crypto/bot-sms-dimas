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
    "cf_clearance": "LDJqWm4TytJf4h13Jxt9DrRDl8DCdJ1_Q2pKe89Dp60-1792040983-1.2.1.1-4XugI2aNEyhCDZdEWnqdV9VF7Rm.wNmH93WttUSMUGjp2dj.eI5bH3Zqxhn3kBZ06zCc0hDR8564itTaN_fTEMKV_E7lvR_kZjoZHloYZZOI62boASF9qqbF6FE1noXcy5BQ3M5dj9lHwCBe53gxCHro0SP4PNS3Gooc4Lh04Mzgc9rNtkqbYJbRGS4zDX0ShsrhVNu7l9vBGouhN2pF66DJjZfJS3Ne452h.9k7rMLC46BU.ZxA14pZnAM2rgIxC1RajXzfG5eKW39Mgt2nLMwp9iSuyUTwJkX3VHbtK46jzgp9EBVUH0owUVFIIyTA_o0zUvWvWMW1yzOUaW0b_qbT5uOkfpSEFodscUXv1xZbDOfuupttY88I2uV6lKqiOJDhqhSsBC.2jmkaCbfHkZ7WPyKvqJeFzYvtamoYp614c4yQGCZiLucIuedMqE3nGtLfWFsccxINETsq0bzr7M2tQXqw28McR6xcpUzG4.0vJzdx3x90pe9ArwLMDc0aBVzQCJ8WfCXMaB.9iF5RLg",
    "XSRF-TOKEN": "eyJpdiI6IjFsSDRGYUR3eUtQcHRtQVBJVVlXYmc9PSIsInZhbHVlIjoiODlRWkNsZGhDbUJoN2ZPL0loZTBUVXRMSmQyWEN4dmtsTWkxSmdEZ1JwV0Q4TEhGYXVJN3ZpQ0k3ZUZ5UE5rWjJqNU9ZaDVDeXFOK081N01uUWFUbTVPMkRSMUpGbzRHeDJnNk1NYU11MThoU295MVlOYXNvd0dHYUVOOE5DRWciLCJtYWMiOiI5MjQwMWMwNzE3OTc5Mzg1NjBmMTBmOGJiYzk1NGI4MmZiYWVhMDI1OGYyY2Y0Y2MwZjM5MTA0NGNhZTRjN2E0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9sZHRqTVNPdVFpUDBPbjM4dW1abXc9PSIsInZhbHVlIjoidVJNTmNYeWt1TVJTbFlxdHRyUkFPSy96WndtUFQzbTVIWGZhYk9nbUkwSFFPRXBGSlZlUFpmZG8zeUR5MG1MWTV5TDRYbjJ6aXlsbGJqV1RTRUlNeENjMzdrejRyQ29lSGtkM2pMOE4vMEZaUFlwdXREdUZubFROZ09MbnM4ZFAiLCJtYWMiOiI0ODY4NzNhY2FhNTk3NmNlZjUwOWI5MGUyMGJlYzBmZTY2NGNkOGZjNmE5OWI3OWY2NGMwZmFkOWQ0YjM2YThjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4aPzIHhCeF5hH779ipmmTi3E.fLLgyiR8pIozeLk9cE-1792041015-1.2.1.1-dwqvrgUAy_glkF_.i_BsPePJtkOBCarzyi4gK30mIipWJd0fo2.nu3JzT.HT.HTjDl1WG5JN82ssz.ar8dJc1C6oI5Pju5gvsAmOZQR5bkWKQb.zAp.2.z9rWUc_eAXzBcR9HmMAfpButg6kQg3GaqUpYsu_p3XKd2J8f7kbD2LAaZBln6RJzboreZ1OhFEGEhUBal2ZavHvKLWEgyljTKb7szYinqat.U_f9.e51ZoFbP92LU3Onm7Ua0zfpVZNezxRCpl.M4.6J.hr6xpZN0DfA9liHmXjkkSQo_0DRgQ6QJ9E3BW8LbU8nvtdGQTffaX5.EKFN6Y4GTYeQbCFIuCr3BpWQxfjQrflEjfyC8Q5ME.BChznki89eTGEx5bK9wyXWuFGBKn4pFd1Xhq8emzgKgw3HXJJPr2WPDGd54KTn4Ai5lWxdzWdIk_I5zNaH6dcsuKVZtuwKrTvpoqejhMPJUSan.HJbN_lUMQlHGHgc7RS.15gnPCSdN_SWfjHAGv_HC3qkagSNzCYoKwDPQ",
    "XSRF-TOKEN": "eyJpdiI6ImxTVnpUQzdqM0FiQXhLSWIrWVVGS1E9PSIsInZhbHVlIjoidDdpOFhlL04vZEJJajl1a0E0OVhyT2hiTXpXUXkwVzhSQkRPS0RrNkZnN2hXZldpL2ZSblRJRTRmcjB2M3NFNXgwSFZ2ZGZLU2tBVGdPQ2tYeExXM2pYTFhQV2NjMHNTa0QwcGJkekJicldqQ213a0pIcE1oM1QwNnA3ejk4UjgiLCJtYWMiOiI1MGE1YzFhM2FlNDcyNWUxODlhZTAyNWQ1ODMzYzcwMzBkNjhkMGJjODhkNjYwOTVmYTQyYmU2ODhhOGM4ZjlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9lZEtoNWFHV3FlaTBVaTdDSlR6aGc9PSIsInZhbHVlIjoiUU5RUGtoZm9pQ1ErZVNRZlR2WHozTHBNZ214VEtJc1VQMjlpOFBMTEo1YjNkTHZUWG5XVC95NnJjanl3ZUJTMHZpWlEyTjJwNlNjK3VTTFhpNU8xaUh3R0hVNzZxS1phRGg1K1NjLzlieHVuZXhjOWRreWc4MEpZZTdJcVJUN2oiLCJtYWMiOiIzNzVmZmQ3M2M0MzdiNmRlZWU2OTZmOGFlMjViNjc2ZGQxZTZmNDMxNWUwNjM4OGUyMWVjMzk3MWY2ZGEzMjAwIiwidGFnIjoiIn0%3D",
}

