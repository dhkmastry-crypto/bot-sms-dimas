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
    "cf_clearance": "GFFJ9Ks.1sKFGdMeAf4L0nfQrTZvdQfDX.64cIf68HY-1792045655-1.2.1.1-KXbBF9vaHCZGT0tFzXxOcoV.CREE.QnR6h5XPimABFQer8Mm1GClk9GHe1eECy50vER_s5KiMw9cFdtrI4MK44HOJ0aRVukx0.snr2.xtYPFC0cwOB1u28Bckdn0aRYg.VaFWd.Bij6BVHTJYGzEUJsUu7269BiGon9ibFJ_PMP_TfX8gSRtSuxgTYgr32g2KnpjQzmcATNonVO22ixF5SKCQQmLGMW7JmSsiDEmOpCexfHdkwQYS8olvft.U8tCYdFZk6Je40P2EUFt8qT6sqzB5zuWZ2vBTgYpPANF2W7gVMHUEWV_XijvprNhGezzAeq1BYLax760K1XLvi9yls1rrLzgNirzzGhqHZWpQWHTsoXKoMDfroUZrCwiN8j7cz6HTiudHywr2UXZbFa2kZ4MD1mILvMysnNyTvMvXG63oWm9nt6tFKPentqJ0_Z16KUqKSXWRq8517PlVSR4pDt2ceIRMpgv5TYs0VirOJDKXeMgPPYO6.TrGVA0e06zSGcZ04DwbUdDqpVeH2_hDA",
    "XSRF-TOKEN": "eyJpdiI6ImxuU3ZXVjhwbUkya2ZySk1kcU0valE9PSIsInZhbHVlIjoiSloxNzFDVUlyMjFoVE8vKzJaQWtEa1A1bmQ2UHp4TmU1UDZyaVdEbWZaZ0l1NFNNSUsydW5YeVA2dzgzZjJ4MnEvWUtKOTRHSHl5Ui9aOFJKWkRYVWdPOHBYL3JRT0JtalBvUHFWNnljY2tFYmZ0K2VENHZ4S3N4WGpSVVlDU1UiLCJtYWMiOiIyZWZkNjJlNjY5MzQ4NTk2NzAyNzJmOWIxZjcxMDg1ODEzNzZhNWNhNmY4MTg3N2EyZjZhNmExNGM1M2Q1N2NlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZMcFRaMHlRUVAzdkNJamxTNEk0bXc9PSIsInZhbHVlIjoiRFRmT3NsNzd1TnBrQnE4QnQ5WERIWHIwZFhNQVJBb3lGVVl4a2xJcTJvZzJkdlNHUFV4YjBNcDFaV1U4K3hNMnlQUlNkOXM0RVNhckFpbitMTjJ6dlc0OGQ2NHZYYTQxRTQrUDBiT01iVkIzZDI5UlhmZDE3Ni9tZDhydGV4Ni8iLCJtYWMiOiJlODVkYzkxYzFhNGUzYjRkOWNhYzhkMDk2MDg2ZTQ0NDcxOTg2ODQ5NWEyZGM3MzhmOGM2ODJlNmNiNzc3NWJlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "f0fHhRuXAbRgOfp7Re_kQE8hx5eHr6uqsanNd.cKa.I-1792045612-1.2.1.1-S.fGSxbP4QELq144CUvkrn1t0dY_ma2SUzEKbLYmETMk3ohVzREZb4dX5VCtJZqKRaqHZkFVkw4nsxJgJg82_n_0sbfCIs59f9mXnLHYB60AH7lTq_H1TbjT.Paz9HP66.6EnOFVCga2jH.VGeKtXwsAK.jJKnGEt_3wd4sHU3_MOY7mqwKURGE530bj9.qBUoDCuyPOPK.oTcd92XQpPnw1IfXwl6H8_UA.AJosbIZmTmwG6FBonl_j.5aM2aEwwjDLdOiN7s7MoJrgLLi.wGPlkGG2mWQVFmrIUh.U5FDwH7eyYzJJNspLHf9aVD_e1aJYWqtCKdh5yT6nFQQS3lWmfieeAYpOW86sxGHjggdoqenIlfGYCO1Ud3detS0_UZKZkJUVAXhh75undlwWiMWIKu9aLQBzRSS3yxFpxt0URPOoWAUetxdMP9SKfOL9URAbGjT9vHgRKPMAA.xCnJlxenIF90SPPR4sH7EIUKjHtxH4L2xmYPNi.5dGF_86tSFHftEkXLF1LIsevGrkFw",
    "XSRF-TOKEN": "eyJpdiI6IjhtRk0wT2VBVXpGR1VsN01vSnlSOUE9PSIsInZhbHVlIjoidGtPdklENHVqM3d3Q0N2VTRHTzJnZzU2dXV0RkNobUR5UkNRaUpnZTBMZTJCaXdLd0UwVE83YUlLY1RxZ08xUXNaTmk3UzNSS3VCb3BvRDJoVXduKytscVpHbWd6VFcva0ZzMWxzYndkdStjMG1aTi84ODJXczhsSE9jcURQTWwiLCJtYWMiOiJiZjVmNmMzMGNkY2FjNzdmNDA2ZDVhODJlMzIzNzRlMzQ2ZjkyODRmN2U3NGE3NjU3OTExYWQyM2FiYTdlMmNhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjIxYW94dFU0OFFUSlpxMnRQa1N4QUE9PSIsInZhbHVlIjoiU2svck1paDdFSk5UbVloQVp3V2hRT1NuNllMRFpyc0I4Z3pxUXpCaWV5VDg1L0xISi8wa2RFNHI3ZzkzbTE5cHVwakhRYU9MeGlYc0oxL3QxTkErRys4UmxWVHlWdHNOU25lcE1seDNCNW1FN0t5NDlzTkhjaHJKZDg2a2NHNWsiLCJtYWMiOiI0YTM4NjMyOWQwOTI5YTQ2ZTczNGUxYjRiODZhOTRkNWJiNTVkMzhiYzM0YzYzOWJjYjY2NjBjNWU1M2VkNjg5IiwidGFnIjoiIn0%3D",
}

