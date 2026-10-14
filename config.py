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
    "cf_clearance": "4Ce8FaPH8W3JXmkb77_TEBBQwMv_VOOlnxrTj1CIIqw-1791960220-1.2.1.1-y0s1tbksD.dMMmreHBd.SmWnZbUS7Qx3Qw6IM9QIqnSIphhQiL06TlM4v24fy7Nxm0pgjZ7u9RDj.xvSbkk3dVTIuj6ROpI8yqG0MU4Dju13g.IQzP_ArCuXSTU6y6sQYLaTpOk_d9SWP8dBbtc9OqB9l8imoNWQSyyI70CfBg80nzERZuyoLWibww7f3SKKF7UKjZvoyUtPHNOdQK0hW3i6R9_8ASKmGhQPdwwMHTUO001Q.2p2ylJQN9FlOyFavAMKMwGxh6wWUTbKNIokW3VERq2JdY6m60T10fPoVpTL0pYGmxdxvvDw_x2h2UZAMJVbO3d2hWU5W1dwTbGZqaIgvgJtYbltLKoAoogvre7IncP36Bwrkhs9phOZnW2b6VGuS4T0Cc8iqYA2BAkfiAJgf4QfXK0lXxKQxjQ_rE08JUMWj6J.S7H8Vz5EFROAbMZILqtV1.OL2NOWmGWCDTY1Bdsm0JoVmxO0f6GLmLo.oGio8NPZWPbb15JgnBWMnJEyhYZGrHscB24lVi_5gg",
    "XSRF-TOKEN": "eyJpdiI6IncwVm9vUy96WHBNR2pTVFo0SEo1Z3c9PSIsInZhbHVlIjoiajNqWWx1eXVUeEgrUnFhcUFLdTZWMnNUWkFxMWtjYjJQNURPZXVrMnVpOFgwOSt6MWxkeEl0eXJwbnZUNXplRnpNcGtEY05uVGluTzNSQ2dIazhiU3NkUEVCY1hXTzFkSWd0d2w4bFZ5OUZZckVIblhDRk13ZnZaemliWmg3ZjMiLCJtYWMiOiIxODFiMWJhNjA0ZTdjMmVlYTczMDlmNGUxNzUyN2MyNjE5NzJjYTEzMDhmYTVjN2UzNmNkMDhjN2Q4ZjMwOGExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRsc2FTOTA1NkpWZGhFR3dqMW9UMnc9PSIsInZhbHVlIjoiNWlHUlFKbXJQaGJNN2NrUFIrS0VwdUJKK3NJYjk5Q1prRnJiTEIwaWxCalhkbEJrSWhGbithdm9IN2pGcVR1T3JXMnhQS21zL0FwK3JIaGRPYWk0dGh5Y0pxZndCdGxNK3BmQ01pMGdXOG5LSFFyV0I5K25nR014Mlo5OU8wUUkiLCJtYWMiOiI5MWFkN2UwNTNkMWRmNGFmZmYxMmY1YzQwYzI4MGQyOTVmZTllYzlhZDg1M2Y0NTdkYzFjMmU1YTkwZDUwMGM3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Txp3freoid4QtZNj_Kh.BmlNlyX35Zxe5XtIgMDVbuk-1791958511-1.2.1.1-yqKO5jIFOxRqH9aHuX3Vdt4T95Ph_LZUzYaJKW6wLzQAla8kmR0SAzHKjACVWc6vVr9lI8E4ebFekI7GULOkh9RMsUn.OjLgeR.1ihio833.THTdVd2h5JRl6AvYHoXSZFYn1xP_dx7TadGq5qO9tP9jdm6AI_YQII7K0jX2LwcoGzFcfbFfIHtI135uFfv9kieStXXA97h5zWbPum7ed29ekmtBjmrlyP12zOVCVmA56jKUcRcyhiAaGJtBHk9XpJeQht4K4_nyHxPN7IjFV_rjcfToRw9YO.CCNx9pPT2EKALdcNA8OUrd_63r.uq.HHaEUPe7cGPArV69mglr21rgzAatamO..0XUemIvhsT_Irj6L65JRi0K9hyJJfRLOyPbe2Q16QLY8StEO4eBtSrWqVd86hlKwT_eDY8CzRpd6t3P8MZ28_5teG6_eV6Z2f9R_tquviZ0bGHBhGwkE_uwYvd82vO2o25C8xsRg7fIm5ifUAu9I.FIfZCQrlrodWGfqscTcWNoI7tbAGMUsA",
    "XSRF-TOKEN": "eyJpdiI6IkRFNnZJUkxQQUlvK1hCNlhvbTl0K0E9PSIsInZhbHVlIjoiSUh5cnVhVXMvL2p4cWFhc21iSGR3TG1oZWhGWTdWSXp6MWYyRWlrSkdJazBERVJqcWdrQi9Pd2ljeXkxUTJSemZWbzZRRmVYaXYwSTJDQnhSMWlscFJnLzUyVVR4MytTMzBHM0RUd1RHZE8rQWlhb1JMQXNXanBOY3RveFdObVciLCJtYWMiOiJhY2Q1MGNlZDNiYjk4OGQ0N2FkZjgwYTA3YzAwY2QxNzExMTMwMmIyZDYxZjM3NjZlZGExYTE4YTAzN2NkMTNhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBiR205SzBIdTF5alRmOVEwUy81REE9PSIsInZhbHVlIjoiSmU2VGJSZ2pIRnRlWXlMaHIrOVFTYklLeUNyZFJaWHhMTGMyQzQ2V1F6SEh3LzEvdDBBNGtkMFFpMXh6eWh6aG1wY29UUkRDYjgvWTl3ZnpIcGlQemx3OWNJYXVsQU5hbm5zZi9oc0drWW5ZVjNNQUl4ZitKZmtsQWJKVUpsM2QiLCJtYWMiOiJlNjIzYWIxY2YzNDBlOWRhOWNiNWIwZjkwMzZkNGMzYzYzZWQ4OTc1ZjU4ZmJiNmY5Y2NjNGQ1ZjAzNzQ5ZGZkIiwidGFnIjoiIn0%3D",
}

