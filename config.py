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
    "cf_clearance": "CqUjQ00bkA1elOyeA4tl7qFo0aM3gjUStCl274mcM2M-1792060118-1.2.1.1-iNl7fHFOvlctLENbDH55yU1Tre04Gx35BcxXdlRGPFvzrke9LSRCRXqeH5VpqBMNjvodZn8UA7FLNVaIpTc4i6XTRB.B97sZ.RQcTExYZ0GkaBqy8yvN958gB1k8yxps2s3gkwgl4KrPUhWmSQ6VlgsWCr4HHobKVu7yhU0k65GuqhpBBgCNw5jJ3arqGyUyrABCR41_F2dbzns22H_JFURwVwh2Jn3R3xiHuAGakR6kwNSM78Ex1KBNkYefJEwYRgDiS90sfPPTJmq17kj3.cGsq08.ZileOhVenhPhbnbvCHRZogAtw.eekZMNInaCryHNwSVSsbdqmvPnZefdg4jc4rcOhBKe4WSdlBOTXa5JHWj2PD8Huwvj3f3_KeOmhnAuBw03C5YsphaFGsdoZQxyY4xfgfHeUmgsg7tE9Zi3gv.joEZlp6z6_AIdK4rMG7doMbl2B6fGIcVbYa06B8xAi8AsMoi0jYK70NClT7l6lrN38MsL3D4D3TtwfPoKF7YdbvdtBRdWNF9O9riChw",
    "XSRF-TOKEN": "eyJpdiI6InFXVmtXZkFGUUhEOVpETC9FbjRVQlE9PSIsInZhbHVlIjoicGVyV1NWRDZNdXVwSU5hZ3lFdTZVTlgvZjd3b20xc29XZ0gyam5FaGVPSVczeS9nT1FjV0FKbkJvbk54cnNZbFlmWjJQMm15R1dabmJjS3NWTmhMc0kzaHJuVHhxWTZMN0d0VllWZlZtQ0tuVzVkK01XNHBySFFSbzI2N0tJYlQiLCJtYWMiOiI3YzA1NDJkNTU0OTljMTQ0ZmJmZWEyNzBlMDQ3N2NmYWY5ZWZmZjA0ZDE3YjVlMGY2MzZkZWRjNzBjZjc0YTg0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im52QldHQUxsMmpZU0tCWmV5NUJBdGc9PSIsInZhbHVlIjoiZ0xQQmd1Q0dSQVp5MklqWDc0LzBYTGVMUzZFQmxtd0wyYWk2YmZuNjlrQi92NUs4V3loNFFoUFZwb29oQ1pCVHVUeVlJZ1J3QkcwejNZWGZhei9EUDZ0UFl3NWpTd1VJc3NXaTJDQWxGV01QeVJSTWlsSzNTVzJmbVR0WWI3RXAiLCJtYWMiOiI0OWVmM2E5NTc2M2ZkYjlkMTJkZjk0NjdkNDhjZTJkYTRiNDA4ZDVmMmVjMTU5Mjg5Y2Y2MTVmNzFmMTgzMGI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "3cyU1ePU2kWCPaakv9XsX8DJnVqUIHT9RQ7rlyfZMNo-1792061881-1.2.1.1-woz.JBzLgD0.EReri5BR5OxtJVySiGWl9j7TMIII3WXuOqDrBrjU_ZotGsi1qSqav4fO7._1cxVKGZaOHGGAdDj6m9EyTuQGjxCbXosglqYyUKSoGCsmhLaex0XksSoz_OjnoK4BTDwmr91yCC0zuxZ.tiZm2YyVWdnsZ.UsTFQvXGywMnv6RC3tcubOnV5llrLiDZ2cCI07kh_q.WgfxspTqPXNeRZacuGkSSfuyAwld3kKXE7nCr_Ick6Enik3AlWdvUXr_l9mLsHh3bgM.Q0qiA78dK6JMosepG_34PxKGfPqBgPc7FIH1QXUVdOOJmbQYrR9z4cdr3PcLoC3mGs_jQ1v6dAXnAO74VY5ASE.pVbCVGYcMSulmWrqIhBbryRozrRBg03GLp2X8CVGVMc.hECbBoFPBOe2NcrPEoOF0a7pLmQWloNUrdMk0iieghWcc.uVxMly0LVfxNtIk7q14SFbUdXxG2fZt53VcW73w18nmha93Q.oGtwNfVXpXqjVOaaQ53nVtJpCcu86XQ",
    "XSRF-TOKEN": "eyJpdiI6ImZncStPZzZoQmN6SXpjK3ZvVkxSWmc9PSIsInZhbHVlIjoiNDlWOCtUcGplUCtudENUTlR4MlorNXNhbTlMOXFrZGp5ZW9jM3ZVbDAybDZjWklQQ3dPM0JmdENaUEZpbS9abE55RVVKaXdJYVdLT20rTE03TjQ3WUhGczBKWWtDT2o2ZUM1TlZHZVpLZXB2d2pHTThEQ1JCbEJLdVNvbTgxeTUiLCJtYWMiOiJiYjQ3MDNhMjEwNTE2ZDU4MmIzMzE5YjQ0MDYxZjlkMDkyMjdkYTgwYjVlZTY3MDJkMzg3NzU5NDkxN2ZiYzVlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldCQUcxaE9xZENyeHJSeVdoVEZSZGc9PSIsInZhbHVlIjoiTHpGVUtabDJCQmhzOC84T1FTSnVnVmQyL0tDb3V4R2sraExTQTF5TytjR2lJWHd3ZVBxMThvTXJSdHJGaFNPL3plOHp1ZUFtVTlCOW0rVHh4MlNPaVhPckgrKzJ1YmxtcldlSXhsMG5HU1YwOFE2STNxOGVqRUNybTA4bGFKODAiLCJtYWMiOiIxODUzMzQ4MTkwMzcxYjU4NWIxYTkwZWU4YTM3Y2NkZmUzYzcyY2I3OGNiNTA3YWI5ZDA1NzhjNDI1YTc2MmU2IiwidGFnIjoiIn0%3D",
}

