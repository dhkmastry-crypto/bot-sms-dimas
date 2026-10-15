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
    "cf_clearance": "2PYLp.ASv7lQMywhj7KvOvX3o7U7s36Ryg0_oXMNeg0-1792056504-1.2.1.1-yvuAP0J6RZjBaRlYSNb8tKKIGn1fAnEMF63VhYJksJZWlASmEGwMLdLfQtjm.TQ.ArTztO4InGLZqdP1pSfZlT26Hustgp61D1ujKoA152MhK239yV.BHwo.qAUZdkoJuTRSO_f2SznnhAmfoevpEqvtEbATJ1h0Vt9L9L2rEOIZIKZTZCtzInacCSmwCaim4zAEzjnD6vjOtxUUKrqA9NEDX4wjQqY7Smj.nGa4pjEi3eRLWnSwng0MW0I80rZQZlrRjAfg405RuQUzF3U8oHRessCR6qOPgPda39dFpCtUskYUudqiDFSPbehoBlKpCRhZf6k87dCYusRcLtKyxk7yPVTA7MuYM.dQiSC98nOYDZe46FEm40rvdoOogE7zapnRPLfcXCgHhpvX14ToFwiPHAdCVrNh0WQ.bj7UR53WKS_C1xhfdumcUPhvvGsbkwjADuWKvfkJVg9RXZ0GLM3rWQjYyeT3YeOsf3R1v1HqBYgq.xyFnMYM9IAgQKBbHIMBj7O6fSvHGGQVQ778DA",
    "XSRF-TOKEN": "eyJpdiI6ImgrUE5Xa25ZbVNvZTRXbGhLSWUraUE9PSIsInZhbHVlIjoieUdMSHVIdFFaK2phK0FkUk9ncFZEcGVXVWFEc2loUytIbG8rMzhuWVdGUnNyNjNhbFZFakxPWUV2MnFWbC91cEhvVjFrRG1YNklMdHNXMmhwOUhDZ0dqdlA5WDZCcEtyenpEc1RxQ0RhKzMvUXgzcTdCZXhrczR6KytuS1p1RzEiLCJtYWMiOiI2ZDcxN2Y3MWZhNmQ3YzkxZjY5ZGFjMGMwZWI5ZTY4ZmEzY2U0ZjAzYzllMDE4OTdmZjI4N2FlNGJhMTY2MjQ4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii9xYkFHT1N4SG4wSENEbFRsSnpyL0E9PSIsInZhbHVlIjoiaVRRb1VpRnNDOGdROVAxL1l3Szk4a1QzRGpvbFRGOENMZWZ2NGc0dTZHZWl1RzRVbnVSZ29aRU1rUTdvNGg0K21QM1JCZzVSeTNhYVNJbGRHSGpjcW9FRXZnVy96ZTIzcTRzUEQ1YkxKWk9yN1BTUjZuLzQxVEFmWjljWGRSMm8iLCJtYWMiOiJiMDBhZjJhNzQwN2IwYzFhZTc1ZDdiODVhYWRhMDUxMjkwMTY3NWQzZjEyM2MyYjg2ZWJlNTEyM2Y4OTQxMGU5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "kaSjAa2g9R9smibabML.ouLXoL_s1.PorAz2G2BRbBY-1792056463-1.2.1.1-3kUPzr1EKgRzJ0uvLV4oVkBiBpzPBzEgkCRxJ6WcXKSE3qGIIexK61B8neGde4scPkRoTiDOH4p3Ba.cUB6jYlPkc8wn26GQjLGX0isXl.i5_NKfsbWazZ6yIL8Gu9wvEcMsKIRu60FJ4I8lnc.JflkXwgE7Rn_Z35uZTdeZ_VdAvrC5s8d7BGSmrndnH2nTojNiE6jRuwHqV3z.J3nfd8qza97t01k0LoDE3ImJG4jEqtXGZUwIdTX60n0PWEIpw6OdhEp_nPTdrpLZjtJpfKXE4g6UyqtG.V7LQwKJu3ariBhKkg0QvXtdHiaUB4tIjlRQ4q2nriGtVDVsK4W_ERORXTIxB4orUNV6IInzeQh8.y4fs7y8vOsxvAS3mDXUqfQXYxwOimsq57nz5UGlhcZt2zEl_p_pjK4mOK2jXcJl1bAekEW01goxv.DmlrVEfZGnPFAoH5Dm4DKdpA3bR.7WQXfWQxZAFbhSK6uH5LQvo9KTePLgqh2MhNkdY5UoIZF3YUgbXbvJzC9qPvVf8w",
    "XSRF-TOKEN": "eyJpdiI6InhjdDIwNGNKbVZDQWFHMkNQTUxYM2c9PSIsInZhbHVlIjoidS9jQm1XSnI4V3NhV2pxbHRFUkVkaWRVdTF6cjcrbGJDVFEybVRYNEg5akd4a3VObStsd0RyaHYzcTJsODVCUHJnYnVZd0NUUURWZzA5Ty9tRWxMdlhsOTlPaHcwNzZ1c2xGaHRVb2ErUkFiNUk5UHJsdkFXTXZEbFJjRm43MXQiLCJtYWMiOiIwNGVlNzdkMWQzOWIxZDAwYWJmYzMyNTJlYWUxNmViMjMzYTY1MDg1ODljYmE3ODUwNzg0YTQxNmZmNmIxMGRhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhtV0hlbFh6N2RHdzQ4YkJvaGxOYlE9PSIsInZhbHVlIjoiQVVJVnl6b0UyV0ZDSTRPMTVDRzhVZ1ljajFvVUNnQXEybEFEZStmM2RWakdxeXArSTgzNWhHaHdTbksyNy83RXdtVm15T3VMVUpvU2xUejJBalFwU2tueG9HcFhvM3BVcnhZMmF6VGxYdlR2YlR3WE00c2hieHpGRnY4dXp6TjIiLCJtYWMiOiJiY2Y2NjliNjMwZjg1MTc4ZDQ0MDVmMTg0NzMzNWZhMDNkNjE4YWI0MDg1MTU3MzJmOWEzNzk3NGNiMjU3YWQ0IiwidGFnIjoiIn0%3D",
}

