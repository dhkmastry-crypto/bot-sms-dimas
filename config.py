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
    "cf_clearance": "_Ab.yGfaGc6QJSTxpAGJHDCCe90u_C6laNHQQ_n8abo-1792004781-1.2.1.1-8rdgtJwBS7JlE2rbtw7BzhyBj76bPwDLOV77QNr78DkEiBam8vmoPS7a9xYXFn.EGDyeZsvhQo_b3169rxkmyXY9sQw2uqI6JAuU6Hxv4u_X3BrnEgVBKsZX4PnjBppqHlAdtofaALm9jgvpDj8J_jS0bGHSjSw6qHhygALciQb9P9fSEE9EAM00piXy9LaKx9neVGWAYHys7kZWnCdg0vUww9LQi2nsqL7ojCshBxMEty9eWTO.yQiMdLPTh1uEW2oW4eM1fGmsx.PZ7yHdLUsae11.qzlPqHs_Zl1GHX7CbUKKHRFncqmPi3nk_aVUkzxaD2meODdDR5IrqGddIaMMYgZXm.QGaHQbMXhh7R6N6Vhm4wwqYuR_4GqykUMn_33JaEiQ01v2jwiKlZM2sZxKZPNFWqpi7VTysYorrLu6BrmmtxcaqwMFG9KeyMlrM04JuT_YQ_4ABAVvQ5Y..NFrQhMJFKasO_3i1TJxc9.VLNYuBwNmwmkzdcExMaeFWRuD4gFYROMjZ8J0lN_ZbA",
    "XSRF-TOKEN": "eyJpdiI6InROTnh4Zy9qSStwaUV6ckg4bElGZXc9PSIsInZhbHVlIjoiaVJrYjNmc290RHBhSlBhT3RBckt6OWlMcGRyR3p1TG02dThlaTNXZDNqbmNINlQ5Wm4xM2lWaURlYUFNbTFhSHBMZldZUVlzcXhlb1pPNjNQVDFISDdLQzhrSmp2bUpjeXo0R0V5NHVDcXlZTjIvNVRZVmJ6TnF5VnliM1ZCN28iLCJtYWMiOiI0M2ZkMzViMTM0ODJkNzFkNjU5MDIzMjA5ZDYyOTc3MzA1YzNiYmMwMjQ2ODk3NWYyMjlkMWJhMmFiN2FlM2Y4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImVmWEh6NXB4SWlFZTd4ZDIwbi9HQXc9PSIsInZhbHVlIjoiWFVCV2dCUnlOejE3Um9mcThDTklCU3NqU0dseE5Sak9VVW55NHM0anh6dytxd0NOdU5neGxoNTJML1FEYitEb01pLzAwdDBBZHNYV2U1Y1E2UFRZTjk4MGJqQThZYjhQSTN1NUptRFdxSllVaW1YUnY3cnR5UmkyMzRKcFR0VzEiLCJtYWMiOiI1NDk0ZGEzMWNiYTc4ZTY2OGVjYmUxY2NhMTY3MzMzZGYxY2EwOTk3ZjA1ZmJhZmQxZDZlYzBhZGQ0MzYzM2E0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "yc8iSW9LOKRRfYZ04Si.2WnbS.3blMjHpQGzVZWXT0M-1792004748-1.2.1.1-LsrLJ88lgj3kjEJiTF_0SsdZE57DD.pEmr3lex_vqM7U1KjVn3BFLnAV2DvGWW5M_MB9UnZayte3n4vJOIeqkU1cqh9cSXt2XtwUUXNDif7n55hOwAfXG2N9i2And8AvJGWYgselB4CRSj54iBysFuyXCBbBtBZjc5f3_l12cAU_HRaIM3x2bhxn5OfZSahrJUjV1gmTcf1FAOcZthISicTQTkH6.0fbUTdThAT8bD_UTIJVYM1adq.pSVMPE0OM6sQ5Cs6jTq8qPLanlwWb2qv32cWouJKLogLr4SwtgHcQ0XN2LQccQ0PWqjq63IlmtBzc33Ysmot0abN.LFgL5BqUIcq64EUktyXbeEFfLwHvTqH1s55v1rrvnUk73oOfM5xyKEVH2MFfarXcMgeurhSsXD0uHsUjVr92nW_yGpix0aO31yumUErr746mZ6WjFBC8TY_dpYOAAWpPiSJSwy0cxLm99z84bkqj9Z0eAOC7wE2jEqLylSpvoxMDqI7OIVvXG5elI936W8bJJx5zkg",
    "XSRF-TOKEN": "eyJpdiI6IlpsSEJJSTFpZDFoZlNnUlE2bUM0ZlE9PSIsInZhbHVlIjoiVG9PdGJsTmZDQjMvWE9paWcrQUszakxtaHM3aS9rRG5aNVEvN1hYUHdpNFpWQXU4blJxUUlGeEV0N2ZQU3JQSUFLRjhjeXpENDFZV1FTRVJ2UVM2eWJYSldEd0pGVlpOV3dIOWM2eUh0cm9RMjJZdDgwNFlRQWtZNk5VdHBCUFkiLCJtYWMiOiJlNGQyODUxZmVmNjVkN2YyM2FmODM4ZmFlMDFmN2VhZDRkOWQ2MWU1NTM5MjcxNDY5YWZkZWEyMzFmMWRiNDdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVmWlNpbm9Nd2Yrd3IySzZKcHZvcXc9PSIsInZhbHVlIjoiS3BrMUJuWDBYd0wxb3pzZkJYcEFtOTlmeldQN0tTbVJmaUUzOFdSZHFrcFNFZ3I2dGw2OGJpY0ZiSndCRkVGUEQyOU5YTFJqUkhTU1lwSHZKQ0NuVnpiODFSTnZWZWUvSHFjRVhDaDFycUh4eFpNUld3bkNhVkY0NmM0K2JLUTYiLCJtYWMiOiIyZjI5ZmRhOTlmYTNlOWMzYjc1YWFlYjJiNTZiNjY4OWI3NTcyYWQwODBiNzc1YWNkMTkxNzE2Y2UyMzUzY2E4IiwidGFnIjoiIn0%3D",
}

