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
    "cf_clearance": "FbFPQ7AqBiN_jlPbge08y0xwYFOf2VhlhhIxInJTeTg-1792001117-1.2.1.1-iQDWGan7hXqHuOFuUeB.kT3YYuRdF.NqoFYdCAP0IzlGHLogLdad2UGyRQ7aZ6AUvLSMtJjzVobnTdVUFz.O8E9QQFGZmhvNA54diWFQ2jckOQqjqa2k.I5LOlrihYfGDausvaRwQDpYrK9UAmMiTyBOYzwEbacZ.9I_p3JXkpZdWT5TtqWAxPOdkPYYKdaqQzBTCSQqxmxylflwPGVGJIuosINq0wO_RsS7y3qLb9FNR0DBziX2f2auFcIp7nqAQ3BhIapmWL_yOg8huaGBtvuie9RsNM.quPJpj4rapvP4RKNfAooZKXRzxDLoE2ZZ9sjUaCB866VJj1dAgc0UNgxcanS3WAbH3trTXvARe60fc.IDvXC5QwL7jrLb94FQvwS6.GSiHQKMSBwo831PfDqe4.CZbfeNjJ938r.yziQQHBms9JfwiD._UWiKbE53zfcg7BoFHVNvIPQoWzi9AbTleduCUgcWtZVImGLrU63ewLJRxPQLxn1BD4ltdaIWzQlxjczm1wKi7SBbte6sQg",
    "XSRF-TOKEN": "eyJpdiI6ImpkekhXNHg4NVBqZnBndmhNRE9CaHc9PSIsInZhbHVlIjoieW05d1QveTlIeENOb1ZGMnFKQjUxc2EvTTBjaTI3T0N4bllxRTVpR2xLeGNSVUhFNUUvTzNOQ2szYnhtdmxtSndWTzBDOVlUY0EzSTV0WTJrOFg1MmtYV1RQdEJNVTUrYmloWUxDajZheHBqUk5JMHpqTzhMRGFsaW5vWkhlMm8iLCJtYWMiOiJjMGY1ZTczZmNhMmE4MWEwMDgzZjZlN2RhZTBlZjJiZjQzMGY4MjY0NGQyNGVjMDU0ZDQ2MjE4MTMyNTMwZWU0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlBBWldDMUFVbDJPTlRhOWUzR2JBOGc9PSIsInZhbHVlIjoiQmNDcHBCWElDdWp5NEJtVFI3TnVoV0l3YzZIeWRnTk9MQnpZQjJrdmpsZ2JNUW4vTndqaVZwNDR5a0pjcEZCYmJpYmowRTlGQnRoZHRPZmMzVElHN1pCM1RORjBralJkRm4vcG9XMzJlRnczdkVGTEkrbnArK2hqTHY5cXJrWTAiLCJtYWMiOiI3YWFjYmQ1ZDQ4M2E2ZjE2OWU1Y2Y4MmYzZDk2MTdkYTE0ZTc0YWU2NTgyMDI0NWE0Y2Q4ZDZkNGRlZWUzZWZmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Qnvqp1ENTZlDid4spkpgKwMuAkP5p_5OkOsPAewzeEA-1792001126-1.2.1.1-iRZlSlgc8xwuqm0d2rw1IhO4duLkJqBnz__5Z4Z6pl4xYOcseVGAznifruy51FOrZ5p47KNlgNzZN6m2cSL8.Vgs5RGgwBexQ.oGKkKH7UN2vde_sBVH3RUOdGqbE8ceem2BitfM8_XhhtSMh79nJqlIZKUAlg0HFs0AesSz1S9.yD6faL8FjnGWBNb9ad5uttE6lICf2H2qO0BSgtgOJEpm_quvwk8CWuR_H6V69z44STSeN1l0jcGaj0PX4GlLnazymh.Ts8nm4_YEIdcudC6MIiakFF7M1YwPo1mXU8ZBXLhh.UFqMbLTtmh8l9ISKB4WsADBW4ZgKfVsIRsSgx38E3yHmpVtkGQc8E1whRkyv61fuoBUtxB6iJj2CHPXU3gGN0cdcA0OiuWVqu033OAbXCxpkfAY_bt6BVlY5mZH1iPyiopneO8MAqagTfqTWG8z5W0UCAAFGlId63ueqPL.cofs7fLTgCSiqoDeDIHYka5MYBWmVkncxpbqpsN_Vc_NukK4d0gXFnfR77sbbQ",
    "XSRF-TOKEN": "eyJpdiI6IlFyUVpmQ3FYMWN4VXVmWFNqU1FtaUE9PSIsInZhbHVlIjoiL1VOVDJYb216M3Q3OEdXSUpLUDR3WGJmeUg4MXh5K21xeUxhbkpBNHNNYWgyQWJKaDZxeklzTFlBVGpoM1d1S2FYVmdQUFJYamhPZ0RuMnJNRVp5Q2ZQRnNsbVRXM3pSaUJBemczMW1ZemdBbCt4dFUwUFJ5K0twaFJ1VWdNZisiLCJtYWMiOiIzYzNlM2M5YmViZmRmNzE5YWZjZGIyMmFiNTBiODNlYjVmOTU4OTg5MDU3ZDc5YTE4M2IzMzNlMjVlYzg5ZWE0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkszRFFrcWJiZGJVMzRWTEsrMTdHMUE9PSIsInZhbHVlIjoiWnJHZFYwZFM5M0dvMnFwZi9UQVJ5YTJldFhBRDRWL2RQaUJOd3NmbjhHM0xRYnhMcTlScjgrZ1kwTnJldWVPYTgxU2RaclBBNlZxYnBrNzlsL0hsVDJkekdPZVRDaVZjTWQyVHlxSksyMUxEdXY2bjFUWk1pSHBsaE5hRlJIb0QiLCJtYWMiOiI1YmMxZmY1ODNjNGJmYjIxODMwZDZlNTM0ODg5NmMzNjQ4YmE1ZmJmNTZjNmNlYTdmOTI2MDU3NTY3ZDAzN2QzIiwidGFnIjoiIn0%3D",
}

