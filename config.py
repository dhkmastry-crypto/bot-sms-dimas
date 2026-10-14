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
    "cf_clearance": "4teh8T_8fDRP34E6Ahvmra8OOYi0dmYUd1o_mHksvOc-1791958413-1.2.1.1-bdeFCF.zwqst4QvEiIQzFlz.ZyZlAPqpFLSSusO8RRSnd5ugPvtPEr55dPNMUFhnotmbMFnVlRi58ndaW1k8AHTBet3JHrvgqWHYvYLPauivrj3B6T05t91_9yY_v6TM8N4GeW1OVX8EHeCHKDbXwVljgsdPotsozFfNwI7Gg9cO_g9GM1RQj0I22HlCc.DjWdWLaJjt7lUovhQqs1zbbhqFIn0iPoRLuXzPoeRw1z5YEHLgmjsglL2f166GJ3kHFj73y0laNXadSIfARq29l4ktjN_21jKCasMdiV_oiJamtB9o97_gZkHhkrSLHOhl2.FEixaxM7qP5cUBrJr.a2HPxLeM5BtOjEyZLu8X2dFBIdVYWdCpOhw86LLjAfzf7gwGlIBdMpW_DCIzW7VELmzS8lCi4mpYzRV5y3j4Ua6E9_nmnG6izdmfFPPnWvGTOZUxj6letmb.LVMwrvNCm0DEU0fdSwJ7getwy4AEDwFqP3ZQsEvmAxFbjfkl81k1NDc2kXI1X54Ta359vOntzA",
    "XSRF-TOKEN": "eyJpdiI6IlkrU0syVnNIV2lXcXNZZHZ1YnFudkE9PSIsInZhbHVlIjoiTjF3WUYxK0dLMDl1YURMb2JueUZQcENRQWdTZkRSRjB6Z3RnT081aGVpS1o2c2UyTEVkbE52RS9FVFdhcHBpOSt2QW1idTFncnBKa0FoZC9rK0gwQ21EVTBYOStaSTdMbFgzVVM4bTYwYWdpUnJTOXFkaFFldmxncmNDczY0ZzYiLCJtYWMiOiI3MTZkZWZmYTEwZjc5NDhiNDQ0OTgzZjI0NWY5MTJmODAzYWNkMmI4ZjIzOGM3ZDU4YWIyOTU4MDcyNTgyOGRkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZJMTJtVm9Dd05sSzQvVTF0anFuZlE9PSIsInZhbHVlIjoiakRVUi93VnVvRDQyUW5LWWtYVnllT2NmNndGRnBpVTBaZE04Mm5pRXU4RDNBM3NMdzhvM002dkJVRkU1NGhOVkhMN0k1MVkweXVYY01hbm1vekZTVDVUTmNGZnN1KzNwSUVEakdaL2lsK1VVQUNEeFNqSyt1cXdEdU5tNU9iWXkiLCJtYWMiOiI3OWViMzc1OGI2MjgwMDg1NjE0NGVlMmI4ZTUwNjZkMjIxZTAxNDBmYTcwNjUzNTBmYTE0MDZkYTE1YjNhM2Y3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Txp3freoid4QtZNj_Kh.BmlNlyX35Zxe5XtIgMDVbuk-1791958511-1.2.1.1-yqKO5jIFOxRqH9aHuX3Vdt4T95Ph_LZUzYaJKW6wLzQAla8kmR0SAzHKjACVWc6vVr9lI8E4ebFekI7GULOkh9RMsUn.OjLgeR.1ihio833.THTdVd2h5JRl6AvYHoXSZFYn1xP_dx7TadGq5qO9tP9jdm6AI_YQII7K0jX2LwcoGzFcfbFfIHtI135uFfv9kieStXXA97h5zWbPum7ed29ekmtBjmrlyP12zOVCVmA56jKUcRcyhiAaGJtBHk9XpJeQht4K4_nyHxPN7IjFV_rjcfToRw9YO.CCNx9pPT2EKALdcNA8OUrd_63r.uq.HHaEUPe7cGPArV69mglr21rgzAatamO..0XUemIvhsT_Irj6L65JRi0K9hyJJfRLOyPbe2Q16QLY8StEO4eBtSrWqVd86hlKwT_eDY8CzRpd6t3P8MZ28_5teG6_eV6Z2f9R_tquviZ0bGHBhGwkE_uwYvd82vO2o25C8xsRg7fIm5ifUAu9I.FIfZCQrlrodWGfqscTcWNoI7tbAGMUsA",
    "XSRF-TOKEN": "eyJpdiI6IkRFNnZJUkxQQUlvK1hCNlhvbTl0K0E9PSIsInZhbHVlIjoiSUh5cnVhVXMvL2p4cWFhc21iSGR3TG1oZWhGWTdWSXp6MWYyRWlrSkdJazBERVJqcWdrQi9Pd2ljeXkxUTJSemZWbzZRRmVYaXYwSTJDQnhSMWlscFJnLzUyVVR4MytTMzBHM0RUd1RHZE8rQWlhb1JMQXNXanBOY3RveFdObVciLCJtYWMiOiJhY2Q1MGNlZDNiYjk4OGQ0N2FkZjgwYTA3YzAwY2QxNzExMTMwMmIyZDYxZjM3NjZlZGExYTE4YTAzN2NkMTNhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBiR205SzBIdTF5alRmOVEwUy81REE9PSIsInZhbHVlIjoiSmU2VGJSZ2pIRnRlWXlMaHIrOVFTYklLeUNyZFJaWHhMTGMyQzQ2V1F6SEh3LzEvdDBBNGtkMFFpMXh6eWh6aG1wY29UUkRDYjgvWTl3ZnpIcGlQemx3OWNJYXVsQU5hbm5zZi9oc0drWW5ZVjNNQUl4ZitKZmtsQWJKVUpsM2QiLCJtYWMiOiJlNjIzYWIxY2YzNDBlOWRhOWNiNWIwZjkwMzZkNGMzYzYzZWQ4OTc1ZjU4ZmJiNmY5Y2NjNGQ1ZjAzNzQ5ZGZkIiwidGFnIjoiIn0%3D",
}

