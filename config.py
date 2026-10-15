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
    "cf_clearance": "KLrVxzXIZCGW2aRbawzPv6NqNzDsCxa4yYBB94wEPoI-1792085413-1.2.1.1-knpIiQQmNbkpu2S.lnB6okrff1PIakfTlP2cIU42qjYnEPirnjm6oKYTgpzfA2eb5Pz71b0LzNOmmTp6p.Ma1EJ2ma_m0ZG7Y.hFN5zfG5Z0lWhnCTpemtcYsWKhna9r2u7rqcHRVe7dqtqDtSwMVea9zBWZ4cZvV9gZ9F56AMRhHkLoM7j1x1im6qFp3tKIo9sVOfgrAMgTXycvqd1pHktNmURwqNdrvWt4EirYC3Y8xi6GUuvCfJIBkbTvyTR3F3_AjsgzTi8K3BegxcDWP_kXto.E8ngnm7.TUPqOap7XagsO24eJ_KDjNGsZVD2f5TpaVUZwo5Ijey8Qcd6ss9C1yfRps5MuBbzul9X8JUt7UpT5N2kRGKGOcDziNndUWFfM_V7dttZg2ylf1GXQQWgQ4UTj4f5x4FJXNkYJ4d.HBlLrpKJici7whTAnowbE9h7sg6waZi45Ux3mlXtmW.ldDV30lxqVebDarNX_kw5QKH6y2hNgpUHVBrAAuMQWxTbbaiLXSUFaEhZlkaacLw",
    "XSRF-TOKEN": "eyJpdiI6IlNobFcwd1FKSkNxaitiNDA2WU8rRmc9PSIsInZhbHVlIjoiYW9TVUxLOU9wNTNhUGhDMDA3WStvdE9rOWpoaDVMQmI4Yll6Vk1Oc3ZQOHhrSzh1NVhPZkpYZHU5ZmVYT2JOMmdBbFlDaWVFWlA3bzRtdk9RN1FSeHVmSGVmRFRKKytKOStkeHZxamFvalFVWTg1UzNtaGhPN05ndWNQL0grdU0iLCJtYWMiOiJkZTY2YTYwN2I4MWIwMWM4YmJiN2EyYWMwZTIxMTI0NzkzOTFjZTY4YTI2MDk2MDU0MWMyZDFhOGE1NTY2YmM5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imh6UGJ4UjliaW5jZDlhMWpjNXc5SEE9PSIsInZhbHVlIjoibExYU3Nuc0Z0U0F0U3FMb2tDWkw5M3dreVVnYzBYRy9zMVRQbmsxWXVHbGkzeElvUDBGdmZYbUhiMTFNTWZ6SkkrSkdka1BiVXltTG5YQXlJSzVWY1YxU29IM2JRTTR0UE55TUxGOFpJTlNoTDlwTXhscDlwTThCTE5EQTZ4aVUiLCJtYWMiOiJjZjAyZTYzNWJiMWQwMzI3MzE2OTA5MmUwMmZmODFiMGViNWRlYTc1YTRkMDIxNjJlODE3NGI1Yzk5MmNjZjljIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Kv8KtUATwqW1JefNrXuHKbUSCcS7gTu7brCApGaA7Gs-1792087183-1.2.1.1-zgfZYdQK0Iv0aPu.05skSPPJ0xo0cgYi9bd9DNKJQtTezqVH5bvKcGY35Qe_VYW3RK77_IISuoewigo6PqwsmSNyD_n0q3E0t6dX6HXH4.VQInW9IItV4N1ZyyjkCggmj5lIhaGuJo9yQFWETxEE_63xZwRGa_l_JNAsNf9l5toxDIOOFLc94abvyIxIy4lvQp8h98voMl0rdDFDGoirsd3WkdZc6wmmvlIaTr8U42GYggrrEIFSyoDvxaWNreoi0QF7ussnr.XrZcDQpclC1wP9iE9SkJeXLc.pr6YwQz2gUE1nb1mREWbSQ6Tbo6jM_TC16lZFN_HKee6lILlfNnGee7U7uSOG1kTmHGU6xV3kDIuWYyLqU32YKHb9t88kI5lTRl0cTz7T_sXnRojU8Bh3CnJ.d0k1kSZR5Xs7fFUucj34QWtXUktZFvnO9UesPMMcoP.c8.jblf4SXJItc4CBZ1zdslIa7SuTVQ8PaRjMq4zgJhiqOy5oYO59lVTY1pyvN3nOpsrHEd5AZwhV7Q",
    "XSRF-TOKEN": "eyJpdiI6IlJ1bGFGc3dhazM4MHJiNHBhbys3R0E9PSIsInZhbHVlIjoiYmxFcVhTMzJRbnh2dlRpNmVnaThGaFdVQnovanZtK3hGa041NnZUbGk5Q0RUU0pIZmFKcHp4ZE5jZTh4WlNTVjVVZjVhUzlkemNjK0NZR2FzR2dybGpPa2xmSUlIWkZlNmJuWkhJVE1LZk4rRnZTL0FwRnZiS1puTUZObVQ0alkiLCJtYWMiOiJhNmYyNDc5ZTAwOGMwNzU4ODZiZmRhNTNiZjFkYzM5N2YzMGM1NzAzZmJlNjNhMzlmMGJmMDU2NTIyMTExMWEzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFhSnpMTTQrcjlNNlVoUDNyd1ovaFE9PSIsInZhbHVlIjoiY2I1M0FodmVnWENocExRMXJ0NytlNUJuOE9MekI2SzlsbXhNbkRZUXpwVDQ5Tm9JZ1JWRE1qZjl3Ymp1MVFJLzhVQkF1c3JWTVVzNFRBbkxJak4yWm5Fd1NnSUVUelRWaVdKdEtQZ3RSTUlPOHpZNFNmakhjbWNFQzJwQjE5YWkiLCJtYWMiOiJmZWZiYTYzN2NiOWIyNTJlYzQ1OTFjYWI5MGU3ZTk3MjY2N2ViOTkyMmU0ZWJjY2IzY2I3NTI2NTNjNzlmNmZmIiwidGFnIjoiIn0%3D",
}

