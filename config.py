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
    "cf_clearance": "mUsakqbH0jWsA5OAb54GJymtHvKfUKoXo6fqDf1JsZQ-1792058308-1.2.1.1-3byqiULVxNukMm3EyOoXirkR7ZeNeNw9xZqeN4cmcGwPsW47eYXLw6wb0SBL_FX4_IypQtLqksKdG0Rdtmw41AxY_fLj0jwqeJ0qfDCFE1u0dvBaHFN1P6KeBKiQfslEPeugpztK3i2KFGmpYRUAnLm2_GMP307DZrk0zBaiw3ieWId_VWQUuI50F9HwlpgqWW4HAw46MRkOlXYXg9KKarztpnLDOF_H0N.RT635pJoFsaNWliHQgeo0_EExpQ3TJVfPRuFK9d6Awn6lm.5Zgu1Zc8wiAtLpvMygwcmRqVKZ5jp4lxIc..t9hZquyyCedIJEYo.lvorFhB2C3X22isdU_GViehEo9Cb7CTRMSUkg0Te0lg2P74dO_CcUCWbHgGTZRuDpHtOTpPUG1fEyjrFBoqMlu7shh4QDPfN3M4qHqscUx8zpbironj61YqZdhY99ujZM5PFjVOcF6BFHD8rOAJTVCSILON0d1Xonu5OcAMSeK4iFkH02wGZe.5Drv8_QzKKALDaW5GZ0cQ4b4A",
    "XSRF-TOKEN": "eyJpdiI6IkZhNzBvM21acFF0d1lTbndHWnJOMnc9PSIsInZhbHVlIjoidW94SEprenZ6Q01rQmxncmkvT3ZGcm5oMDlPb040aHFDSi9lQjR2VW1DS3JJeFJNUEFmZDFpdWRlbUorb1FsbDYyaU53VWRibWl5STRmbm1iZFhxMXJPMy9WTVBndDVHYzdUd1VaSWtGOG5xOUlRdzU5UVlZTG5Hc1VnaW5qUHAiLCJtYWMiOiI2YjIzZjI3ZTkxNDIxMDI0MzE0Y2NiZjIyZTU0OGQ0NGU0ZTQwY2JkOTQ1NWQxMWMwYTU1YjdhNDY0NjJjNjdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjR4SW1LRXIzK1d4QTV4Tm1BYU9iMlE9PSIsInZhbHVlIjoiTy9rQlJLaGNXVFExbmZPU21VYkxKaG9rRGsxSUsxSVpWRzRBS1lKSUZDcUdjQndJOVA4aVZ2Ym5nYUVLRHBvZEljVGlNRGQyVXhTZXFkWnZpRFhMc1h3U3g5V041SkRyV1RzbXlQUkZLSmREd0tPU0ZuREVqWEhFTHhnYUR4YmwiLCJtYWMiOiIyMGJmOWQ2NzE0OGNkNjgyMDljZDA1NmU0OWVhODYxMjBmZmE5NzJhYmM3NTQ5Njk0MjQ5Mjk5MThlYmRkYTA0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4zxKZK3Ql6NIf4oSumgwmiLxhhm3QXDkljPSI8LiaKU-1792058267-1.2.1.1-ELWXm0CcmlXfpasu92eGiL.u3WwIV1Casm4Gp67PrEC67hFyqbLX5t0Jzp6n53BBB3ksRSnI79BWWNEp8N_1_K7U6_qc2NErYeGxoozHkksq6.VjMuTjdr72.38odfnZLDWnUnXAdE18iaXVReCCcmj8.TRM1rP83qm9PsAbOYmgXN7f_K5BuC_vIP1fm1BEBizQ0XTJszN5wxoB0ZK0KJl8aHY71WAOPxowp88P4Vy5BkdsL4ht9jLZPXTSpXEaaJuQ5P_z4R2mi.4gFpJ4Vv6u9kX90BnwNye2uEGZ5qycFKAo2qmMRCQvFhxCpnO6jLZS6llo4H3YxWjcps.FKWjdjVKxV7_HJgeZc7WLM52qjq.6rBDwt1U4wcyxWvlngOAsVg_H02yTanWdQji6zAMQomPQ7kx_OeBphef2vRjG.3hIES0uU6kn9.Q3aBRM9vTFLDvdiRZpzHcYICytNhr60a_22.2S52ymcIBWw.h_d2sFbFesafqScPpSsVu5GWJ2J0CGq8arRetQ9oNYMw",
    "XSRF-TOKEN": "eyJpdiI6Ilo1M3pCTUhZSWoxLy93YmlFSXhoeVE9PSIsInZhbHVlIjoiL2lPTldKZEx3OWJkcHJGcnZ0NjdmdThwUmRtVk1RbTBGMU5nY29VRU1QR0x2N0Y2SVRkZmd1THkrcy8vKzhRRzFvRnFaQlV4amQyOXFLVkFCbEIwVUdXazhmcm1STTFHTnVEMnJuelNjclYwbmFDbFJDRVlDN3pPdHZWRXBHNmoiLCJtYWMiOiI3ZThkM2Y4NGFhZGE4NDdlNWFhODQwOTZkODQ5Y2Q3MjBmMzZiYTViNjcyOGI0NzM3YWI2NDc3ZjViZTdhNzI2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFtc2FycDFvV2dTQjNUZnRDbkduQmc9PSIsInZhbHVlIjoic1dBMmZ4YWdOckNDTXhZQUZiMEorblNmeXFUdzhXUExCNm04UjR2MHE4emFEcTFmV1BkbkNmaXBnM25FTnlNT2ZCKzZIR0JyZk5lblRxYk51YUVDc01VdUptajFkOTJHaHc4KzNHNEFPOGYzVFdUbi9RZHZ6djdSN1NIbmNUMk0iLCJtYWMiOiI2Nzg4YWQ1MTJlZDdhOTY4ZmE4MWIzOTVkOTE5NjRjYWI0MGIzYmE3ZjQ0YjcwN2E4MTU0MGRlOGE0MjQ0Mjg0IiwidGFnIjoiIn0%3D",
}

