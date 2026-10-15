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
    "cf_clearance": "qWCXOVBdLt_tZ2okh.GVP5W7eTsS54yjq.tbCmQ1rvU-1792061923-1.2.1.1-Dk.3YnIUyQSMJ4y93HYbs7iA0KJZjxRpVB31KlEN6q.I6IiH48A4oOoxJZBxJC53y2htH6CWaKf0LC1X0TIXiOX2Q_siAQ6uZQTc0KHnV7rMnA_Xe.FDwAnrMgN0TVMMhv9OAum2UYBZ1UJK4CnBg5D40XNwSqD0VJS7.g9E5QbntOnAn8ukcORpoV2ntZUz57JIQsoXCEYnpP7EMvuu.NNzxu0wCw13u9Gt9RvI8E_bBtefmVnC7Pgf3lw2gnUEzmiLTlLY8VgYZ3lSfC9SudXqUNLsOc3MFZ7RUrRSXFv0_vOSxPK09IWNa6ARp7SYg4B1RIqzwHjERRsU6vPCwUsjRNRqH864f6pbUeZzVV_P1OW8QzHaept_aQN_6zkcmNHJTUQIyhiE.SScMVMt9YTioMQk76EHAkXYoQv0GDbF_JAEFEsXe0DyppHaQg.R2QZsIXxZoDZFQeWrH7cPXgieQJtPbd9nVNxZ0K7HxtmaQ5lK1nHBivQ5IvZpX_XxeYxGSFH0wxZs4DgGfLPkOA",
    "XSRF-TOKEN": "eyJpdiI6IkI5K0pqSTRQR2JUTG8vdHpNeVAzREE9PSIsInZhbHVlIjoiQWdicVdFZFRnbk9mZ0xuUkpNYXgxQmVuamhHVWxjUXBFYXFQd1ZnUnJtL0FHWWM5L2N1a3IzWFJDeEhPUTRYY1hnZGRpL09JaEpnRy9EOGFFNnZjRjZUeXpDT0R6enB2aURSdEQ3ODN4S1RyMHJuNFhUSGROQmhIK2wyWlMrbkgiLCJtYWMiOiI3ZGY3MzM4NGE3ODVlZWM2YTM3ZDgxZTdkMWUyZWQyMzA5YmEwNGE5NDA1ZTBhMzc2YWE1YTVkZmMzMGMyYTgzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik5UaDhDU2JhbVpWcmVwTGxINlQ5dlE9PSIsInZhbHVlIjoiWnBaajZnZ0RmOXVOeWJ2QVQ3bndpWDZGeVAyN2liSFlGSmRuYm52SjRWM3dLT29pOU1nWlQwTDNoVXR0ZnA2bTVXYmU0d2M3cE5YSDFnUHJPREYvYkpPRlZWaTBGQ1EyMWpuYkhleW9jd2FEZTFDSkdycmpsZ1VrMzE3ZjZxa1QiLCJtYWMiOiI2MjY1ZTM4N2JjY2U3Y2MyNWMyYjIzN2VkNjM3MTBiYTBkZjZlYzkwYWMyNzE3ZTE4NDFmMTljNmMyNGFhNDU3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "3cyU1ePU2kWCPaakv9XsX8DJnVqUIHT9RQ7rlyfZMNo-1792061881-1.2.1.1-woz.JBzLgD0.EReri5BR5OxtJVySiGWl9j7TMIII3WXuOqDrBrjU_ZotGsi1qSqav4fO7._1cxVKGZaOHGGAdDj6m9EyTuQGjxCbXosglqYyUKSoGCsmhLaex0XksSoz_OjnoK4BTDwmr91yCC0zuxZ.tiZm2YyVWdnsZ.UsTFQvXGywMnv6RC3tcubOnV5llrLiDZ2cCI07kh_q.WgfxspTqPXNeRZacuGkSSfuyAwld3kKXE7nCr_Ick6Enik3AlWdvUXr_l9mLsHh3bgM.Q0qiA78dK6JMosepG_34PxKGfPqBgPc7FIH1QXUVdOOJmbQYrR9z4cdr3PcLoC3mGs_jQ1v6dAXnAO74VY5ASE.pVbCVGYcMSulmWrqIhBbryRozrRBg03GLp2X8CVGVMc.hECbBoFPBOe2NcrPEoOF0a7pLmQWloNUrdMk0iieghWcc.uVxMly0LVfxNtIk7q14SFbUdXxG2fZt53VcW73w18nmha93Q.oGtwNfVXpXqjVOaaQ53nVtJpCcu86XQ",
    "XSRF-TOKEN": "eyJpdiI6ImZncStPZzZoQmN6SXpjK3ZvVkxSWmc9PSIsInZhbHVlIjoiNDlWOCtUcGplUCtudENUTlR4MlorNXNhbTlMOXFrZGp5ZW9jM3ZVbDAybDZjWklQQ3dPM0JmdENaUEZpbS9abE55RVVKaXdJYVdLT20rTE03TjQ3WUhGczBKWWtDT2o2ZUM1TlZHZVpLZXB2d2pHTThEQ1JCbEJLdVNvbTgxeTUiLCJtYWMiOiJiYjQ3MDNhMjEwNTE2ZDU4MmIzMzE5YjQ0MDYxZjlkMDkyMjdkYTgwYjVlZTY3MDJkMzg3NzU5NDkxN2ZiYzVlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldCQUcxaE9xZENyeHJSeVdoVEZSZGc9PSIsInZhbHVlIjoiTHpGVUtabDJCQmhzOC84T1FTSnVnVmQyL0tDb3V4R2sraExTQTF5TytjR2lJWHd3ZVBxMThvTXJSdHJGaFNPL3plOHp1ZUFtVTlCOW0rVHh4MlNPaVhPckgrKzJ1YmxtcldlSXhsMG5HU1YwOFE2STNxOGVqRUNybTA4bGFKODAiLCJtYWMiOiIxODUzMzQ4MTkwMzcxYjU4NWIxYTkwZWU4YTM3Y2NkZmUzYzcyY2I3OGNiNTA3YWI5ZDA1NzhjNDI1YTc2MmU2IiwidGFnIjoiIn0%3D",
}

