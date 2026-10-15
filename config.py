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
    "cf_clearance": "ZW5fVJuRzDzt77j7kxseFVNY6CGEuZLqjhWJB_3kf1s-1792070953-1.2.1.1-5fJzZ66wBeyP3Fl818o7DGLvWNBAGnSgu80DiQO1QGf8zQ8_vfInluc5OGyLLe4GlOiFcto8j.I1k1IbDaJQ5Xl7r_HT_aOfjoAH.f9ZIYl5CKseT_cmJuyZQz_fNOTeD5CF0daFQbpDBpvz6CZpLfO2mFFWsz.d.be.ioFNlm0kqD3k15UHit_RzI90CT_HExksHnNX7vVtZ96s11GoVvdNLEBFsGP4sK8MYbI0wnAvgaNhIkXgZie9vcrcqXt0LWGwRoP4gEdFocjekyB_MchWhYiso6SA33nYlM1ghM_HD7dtwKgdPYuiNq3.oQhwLuhd6u_ijQlXbWa6dx71HjyvdRCPOmMabdJYD10dD.ZCr6OcaLdXXghMQ8DiWrJB.F7hXfBE_GwmC4eLS47zaBM35FUZQoR4gUmw0q5Hem1.BG.evuQAgAGmkQCPNI56GQRO3fEJ76kuHT04kA2_nAHZQtP6AJonq_XTZMUKRg5QD71P3h9g9myq53dTCskTPDHXb4weopTV8Y.ugkHtVA",
    "XSRF-TOKEN": "eyJpdiI6IkRFRVdyMVhOUGVJSlFSaWN0ei9ua0E9PSIsInZhbHVlIjoiREQvUnJCUTVENHZWS0pRQUZmSVVDZkxYaW16WDBCMmhhZ0psWWVXNkpjRUE4WFY5dUFNc0ZQM1BDbG1lTzNtSVVUSGlUbGk2RVY1MFhBSkhEdjdUa25LK0R0TTZ0MVlMYXozOVhXUUVwTDdTSVlXK0swQzI0ZlhkU1R3bkl1OXYiLCJtYWMiOiI1YzdiMDlhZDU5NDUwYWU4ZWE1NjdiOWM3NDFmOTQzNWFjNTNjY2I3NDUwNjkzNjkyMzQyNzE3ZjNiNTIyMjY5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilk3NWc2emRIY1p3MTQ3S25BSDU2aVE9PSIsInZhbHVlIjoiZ3ZPSWdLRElMTHd1cURzMUNyN3h5REhvOTBsclBwZm9xejJCV0NYT2UwRmN4elFYaSsweUIyYXFNaFVkYUhjVEo1b1VFUkpTeUVSQmpOU2Jod2Q5TlNKUng4bFFvNGpVeFdZRkZxQ2pIMVYwYXU3d3BYRHcvci9TYVl4RGs4ZDQiLCJtYWMiOiJkM2M5NTA4ZTQxYTdkNTQ0OGI2Y2M0NDk0M2YzMmM3NTFlMTliMDU3MWE0NjRlOGQwZGMzNWMxMjY4ODQ5Y2UxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "YlvCLERUX7Q4XA7NpmcLAl31TVA5NvtGI4Ah7YHhAXw-1792070911-1.2.1.1-WBp2nyJGEuov6uohCDtgGA7LYbH4FkzC0EVYcar6UuEM6zCPXX1NnoPcklsY8j9Qj8XFuUu2KZXoPdX9MGQXzE0TDukjYKjuIOKS97z.wtTAxooWrqO3xmiuSI.6CkMqpeyo9cGVvw4mjpvi257KjFTiA_DTZt7YX6q3LYPMkjRwAHB1LJTaEflIzRxiSwxRMqp1kWREI5ZfweA_Mn0l0b5D2zyMcJBQlBfRHsR1HF2en1NxqWggwob2tulAKWHuqkOlvJKHJh18_xyLvEISjZ89P.gY3L.gf3j8Gukg6UvSYC0Qs0PyBoSj6zm9Ey69feu6XB9_7jVYxkfH2byF3lqTgxZFdkwekiqlcpGvLFfQwjII4WcvolOjFuISk2oANAo3aGvAj.QEKRtAHI35o.om0_yJZ12w6d5rtlufVEij3QWFeq5lZ8TNdF9hC4X0WjSZu6VKMDzub2WTnLIV_x1WnDJOSJhrMEZjXacwx2ttTs2EyDf.Fm87CyL_jMXFL2DYjo0NiE5JjkKdbtqVMA",
    "XSRF-TOKEN": "eyJpdiI6IlRJNGJ2MzRFZmJ5V1NMN2txbjFiNlE9PSIsInZhbHVlIjoibTdQTUdtNTBBd1A4aG03NFBlellSUk8zNG1JNVhRcC9RRGhuZ2JCNzdWNCt0TGVrL3ZzUVQrWDlQcndqTUdyRlh6THljb1VXa3hYSmVSRTByYktVd2IxTGhGZWFyRzU1OGdhSDJqZEljcHJnVWwwaURHdmoxWU5WM25wQjF2TGkiLCJtYWMiOiJiNTU2ZDMyMjk1YjYyNzQ5ZmZjYmUwODczMmUwM2RlZGI3NWYyMzJmMTM3ZDRhZDFjNDE3NTk2OTIwNWY5OTEzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImhxeDhMZ3J2c2tSdWdheWdSdEtqT1E9PSIsInZhbHVlIjoiTXo2dXN6UlpzVXpJR0F1TlEwL3dXeVIxNlZoeVV0dDdkVkhxUkJVY3hRR1E4cjJNdi9WMi8wRUJTUFRBek81b3FIZ2N1eGUwTmZiWjVUYklmNENXRE1iQnNYS0ZzY0FidTV5ejY0MlRYS2NnVFFVczhTOEdickpOSm5EampBZm8iLCJtYWMiOiIyZDc5YWNjZTFmNDA2MWMyOTRjNDE3YzgxNDQ3MDFlZWFhNzM0ZTcwMTc1N2Y1ZTdlODRjNjg4OTk2NTgyM2UyIiwidGFnIjoiIn0%3D",
}

