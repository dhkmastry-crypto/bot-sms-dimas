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
    "cf_clearance": "y6o52e05cd7FXqxyUnfZ_RpIg38FaOnGPINttydOEIg-1791916788-1.2.1.1-sjXNIc3bOGcSeexyJ9ngRlEwE3grbRpgu4M4ZHP5pno6aZOUQw94Rc9pdHFx5oRXDt469mvmDCZnbGo6AUhn9QUhfQu5gnu6Gh7bEbQc8ka2zgwYYm4ddTFRzCzcT5yKOVL2_JGQLoPjNmnPa5evvwOF1dKuBbQWfjBRqGHIpn95tvXaq9S0GI9ninwdib1qcnwU1K534SHXxYf40J0Ajr5G_mVgtuvHnYJ8tddsCz8ST2Wxb9GNt2pAtuJLFsn.KA8tHqx6.cdSmoUsywqCL.RBZc71KlyQqTm7XjMjE7ncTqWkHiVlHThXOWD_fTzl.eP2coj5Oag7efFqk14DSuSLsV3GISDbjDG4HoUZ9fINS3uLlzmrUEAQ3jjunkvtzMGyZjd.yWzvGyqPOBW5CY6EVnmcG6yqyrMuBvvPGlf_NLKZptODyxQJVJ3lCBY5b1zEJ4BoM5DwWC0jo8Wac2EZuaqb4XhQa4iqOEx2XhedfLf1caGB0PxFCFeqN2h3FZ_obpbMTj9G9DuxEJ8vdA",
    "XSRF-TOKEN": "eyJpdiI6Ijl0WEE5SmFxbnMyTnI5ZitzSUV2WEE9PSIsInZhbHVlIjoiVTFtMHdZb1JZUWZzRXIzWk4zMFViYzBYUUZXdmcrbzZ1ZzRxcGtudVdFK25WSHJSenZmNW1kQTlzRnlzYmRZcGU4U040VmhQdFJUcDA5VWV4MUNRZmRLa2RtOE1nTGljSjkvY21UWG05THd6aVlvdEpCbTRTbzZqSXYzeEkxS2UiLCJtYWMiOiJiOWM0ZGIxMDcyMDk5YmVlNWRhNjYxODIzZmQ1Y2Q4NDM5MzY0OTE2MzM4Zjk0NzMxMWU1ZTJkMTI2MDdhMWY1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik5OMUl4amh1NEdyMlgwdXloajFnNEE9PSIsInZhbHVlIjoiNHJDczBlRllRL0RFR29aQjFLQkc3Z2dlYlozNk5BRnFROG1CNUUxaDRXdGpodi9sNzNxb3N0bmN0c04wOXo5akpveTljUDhDd3gvMzFLWmwwam9QOHRPT2lUUkNqZ0I5eWY5SnNrQ21TSCsxcEZNZlVUR05sYjN4MGNiU0RGbWMiLCJtYWMiOiIxZTk4MmIyMmNhNDQ4OWFmZGIzN2E4ODE4ZGU2ZDNlNzg0NWY3ZTdlNjU4OTk5MTNjYmE1ODRiYzQxZmQ3OTg1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "G2dnO1gKDtGx84XiJiLH8G7T7XRWM2ElwrIL2Z0ukpc-1791916798-1.2.1.1-zALPnw7nysYIxCWxmsi8baHyYMpsBHWqbHWMEeoGF5drYcWeibZgdHMLVr.PhLc78_5Z3m0Sh9M6b2DrQ26NmD_t_tCJaE61BCTOj21Zf_VPgvGLPHVRv1jOM05BZvfL5_lCWdvy.8Gq70sewxn4N6IrWi6crR_TQHadrWZKY3NQioHmzZNDTS61t6LjJGL0PvtV82YgolKBsAbpTi9OQaZAX2CwlhWCXNsyCRpJNDzsxFONgG.gYcurDsROjpUoJ5e9gY8WFq4yCvrd1lN89jVKUfIqSqLfADxAqSA.LC3XscJ_Y0ix0hN6ZdxL6Gl3XQowhAhzyza26NzUMutQKHtr5vQ9PdsC57sc7CJ_DpV0XBdH0IP0YLaiLzlW5iFOEaxhz7bOz_183IVKHNscBaVnOS2G3JlWuXowU2VjhtWMZ46mGxUs7OP5m3un88kzoOfMF_8YNILCt03_5U1j_3bRQ6T2R1DOkV_UYN5aDmAuarXZdIImWLXXnBMUbknZBSlwOjtH0r03powh1E4rxQ",
    "XSRF-TOKEN": "eyJpdiI6IlNpcTQrN1p4MjhmTjBEU0p3MEVtK3c9PSIsInZhbHVlIjoic29kbStRV2hhQ3o3U29qSnRYZURBR2lFZEY2Z2JZbzZqTjBKZVpCYUVnRGUyd05hcDdzQ0w1dHNKSTEvTXAwZGd1NklKQ056TmZ2RnRqZm5tTzEyRWQvU2FEeW5qckVyMEhMQ0tKN1pYY2xOcFZVMWovUTdvaFMrdkhnQVZKRVkiLCJtYWMiOiI4OGYxZGFkNmY3ZjQ5NzcxMTdkYzZjYTBiMTBmYzAyNDM3ZmVjMzg2YjllMzkwMWJkOWJmZjhhNjBkNGQxZGNjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InVjZklmNkdjdTRUY2lFcStFb1hHVXc9PSIsInZhbHVlIjoiYjV6aE9CS3FzMGV6ZTF4WTcvVUxlemxSMmFYbG8wNEp2U2c3aHdZUnZua3hGM01GWUY3K01DcFdlZGsyK1Z2V2ZJVzRvVDkwZDdDNXgwcTdqNWZFdFBPRHN3S0g0L2FHdFMxNVV2WDNDOG9SWFFTcld2akQ4Vmtvc0NwTHowYTgiLCJtYWMiOiI0M2FjOWZiOTkyZmFkNTIyNDAyNGY2MzBhZGJhZjYyYjI0NTg0OWMwMGE1ZDQ4Mzg0YTNjNmU4MmYzZWNiOWMxIiwidGFnIjoiIn0%3D",
}

