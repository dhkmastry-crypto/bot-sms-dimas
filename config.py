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
    "cf_clearance": "lsJF6drXhQTdnOAQV0Eg6enluhP2qROhiJf7ArdsrKo-1791887334-1.2.1.1-YccPUtp7sGaB1s.emVfdMWwUgPPxms4qPYQlobwJcw6eCfBZJaX4wjSTTXnkKqKvxTandUWQYbmQiRfV6dk9ZX9heofaJ0ifc8Q9O3Ij_Dd0rENGBs8PbB57XrfngVTG3Hv8i98Tuoty2L2esvkATnUVe_EgpeirUYPoDjZ2UhEiirL.MLinvNfMjpz4sXR4aGUnL980XZiWfU5tF5QeMW14Ut_Qma7rF1vKzDKmyfnX_ulspPgOMzpmbnVje_C9FGFYlhU_WAokbxEoMuZ4eYKQGWRJutweR.brI7cMSvZX3jLogD5ZJI2AQD7_r1H8dMRC4qXsZhAnae6qyiZYX7ErjRHA9U9qR3_Kqpr5jgG7FvQDs9vFQZmKXlxGqX.QQaAxZ6g9d2IF5LcwTKw.9HmqPpx4_sIpoV_s0VHuhzC.Giqe2zuV77HPEMdZs7qpeAoSf1PLaFOTJ_I9EatIfYOq4cIBZNMcGjJdwrdNqgsp1YrC9tMzNE_zSy7hjhzX8B4IZ8.1x_fBEp3PzVmcow",
    "XSRF-TOKEN": "eyJpdiI6IjVuK1M1VmhoQWZ2NlNZblA3RmpyNXc9PSIsInZhbHVlIjoiRG1IcnduakltaXkvQjJ1Q2dKZUxSVEZTVkRwVGFlS2hOYWRjVVlVcFN6WWZGY04zTEZnSGQ2R1I1SEFNM3dUdG5TQ0xleUFpQXZpOE9EbTlhS2IyL2VQMnpaWURlU1JPTDRYMkZCVGUwQk9oU1kvWk4xaHRnVmhQSTVnTGxTbmIiLCJtYWMiOiIyNzVjNjM0ZTI5YWYxMDBjMWNlNDVmYWM2NDQwYTBjOTQ3Mzg5MWU0MTIwMjlkNzZjMzFmNDMwMTc4ODRjY2YwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZIbFA4SzF5TU5tSG5aRFc3SzhMM0E9PSIsInZhbHVlIjoiM0JaOE5kSmcraVNGcXRGeXp4QjZSZjFuOXdTbE1FY2RnQ1FyOXE1UElJUzM1WVFRUmdMS1BGdUNDcVdHM1ltSzRnN00vSlo3d0JVUSszOU1lekdybUJzK1BGekdIQi9NSExhbGF5ZTErOFF4OTNaZWN2bVRzRStDSUVrMWlYdWgiLCJtYWMiOiJjMWIwY2Q4YTU2MWZlMmExZjA2NzQ2ZDgzMGE2M2Q3NDgwODNhNjhhYTRhNzNjYzkxMDIyZjJkM2QyZmE0OWI5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "O3_0zXIHniMIvc52PRoe3furf1B03wxz0aRgLN68OSA-1791886702-1.2.1.1-fa.QZHkNRETk5qMoERvQNi.Ge1cWe27VAJuNbnVPEo4rCnh.xYQs0GdB8C8WKzGzak_37Pm0K3GS2HMX_fLhsS18jhweFLBU82nzxVGb2Oq5Teb7KibU0fxYig70Xcka369XWoDBYAk1292s_vH1GXSXGG9y7PhpWIxifZD7Tx5MCQZhSkElm79iQAq0iohJAyv.maR7gnuU92OMlK8vFMbA1Jq2V5_NNLeK_szt.eKqXSfrDiipBS9jW32P7PtlnNSQw8qjrFn4lhT9vIf0APXPq3eRvbnaW5_9JrjNVhTFou3mwqvPMRG0ryzYI0PQzpIaUd.CaV90l4oKpuF2qROLZObCd_nAnNZDP.L3s2FZj_HSxi7lEm4FBYBrtAvqafqfRFqosiVYSXJouYZTM10FZF9Lizm3edOWPWN1ZyqVya3HLx2UIOhRDDbiEH6ArKExcaD.9wucicfVpj7UEtDA5_ZZ4ZXf6OvQ.2JaekNMCA7zg8QpaasPGI7Wq7zO0tBOwTkcAdw8jYhbMhGgoA",
    "XSRF-TOKEN": "eyJpdiI6Ik5rWCtTaDc3MHMzQ0hTYk1ZSzYzQ2c9PSIsInZhbHVlIjoiYi82bzRWRHRLbm9VL0Qza0ZZZXFESkZMRDJMOG5aZnNwTFdzaGdhZG03NjRWak96THRUQXJvYUZhTGJCaG5IQXFEeXlWTGpXdFIva255U21xOUsxVHI0VHFnWDJ0TE5BWkxEQy8xbU44TmgzaE5rSmxCYytMM1pPOG1xY3NwSGUiLCJtYWMiOiJlZjRkNDkyNjA4NGQ3NjU2ZWJlNjA3NDlhOTdkOTVhY2JhMjg0MWE3Y2QxMDQ0MjkxMTVmYjkwYjY5MmY4NDU5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilpoa0dFdmdOdklEL2lQbkRmQmpDd1E9PSIsInZhbHVlIjoicjdJendqTlo3N3hpVnlISStoSmM0c0VpTzlwRzE3Y2h4VWVnWHhqRHZCSnkwWWhCYmhqMG1jMDZCc0tSNGp0VUkrVnBWT0FyOSt6d0Q1NkREd1I5SCtEVDJiTjZtaFNCQi9kbHg3WmdHbXRTZFVRRERlODVEeFRXVFl4S29BZEYiLCJtYWMiOiJjZjY2M2NmNjI3OGE0ZjgwMDI1YmI1MTA4ODRmOTc5OGU3M2IzYWU2Y2Q0OTBmOTdjYTdmZjljYzJjMjIzYWZjIiwidGFnIjoiIn0%3D",
}

