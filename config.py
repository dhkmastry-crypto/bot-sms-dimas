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
    "cf_clearance": "kiIYZ0ip5abU8vJyu7mmNirRT2gAcLEmQWbBzgRP2Rw-1791956599-1.2.1.1-BIpbnp8lctJ.m3OqZ_m.113qYoRDuqguSIcDaf7mbd8rh.7Lj6DUU5ZwSo6UoOShQoFlEWRTRKQYHeQKLsgab9ZgZh_qrDt8Kf1VdT6R_klXGxJu1uTmVRTMU7KkzIvr2kvfSXg80.sEXifCYFg.t1TXLSX103Dz2gH5eZT.i.gVWlAru1dGVyu4MBqFRd2Nrr_hrus0TcaJU4FEBKgorYSzv1aT4Ixs_wOGomoM0h_7YRZcvGJdoByx6fTI1pdHkVOSCIaGqjSNcluGYvdU8DAaOKRUCvM9l1H8aSW1xzFK1Z4LicE8VsoU5VMrHpOmog1E7XOWLWxG.0MXUAyiLXhsT71wAu5HheDu9CI6xvAGzqmJUZ5hnJgf9C6JOcGEg3FyD9s_rmDK5E5wuxGLNPCzu1nT9madsppRg7bEAwauC7lPY5VbFxIfyoZGDGvtfx6X0AHwKi4qjqRGtdS18nwFBqVZTz1idOdookKkDP0EfA8rnIwNWXqfsJmdl20x1dWb0QfD7RbWhxrQ1aMDuA",
    "XSRF-TOKEN": "eyJpdiI6InB2YWlnN3NwV2RvejJNZjBZRm9WbkE9PSIsInZhbHVlIjoibG1tayttTTNlcWNkakZ5ZGlWWEg0b01jT0tFR0JEbUdPL1kyZ3cvUGROQjFkdmJZcy9YN0ljMjRDc2MyUVorWm5FanN6Wm1mYloxdWpNeTFMR0g0NEhtNGdabFNHYmRCVkdHbDRzSlFJcDlrc0lpVTF0SHVIQjdYMUhiSEpXb2kiLCJtYWMiOiIyZDM5NzI3ZWM0OGMyNWM1MGJjOTYxMDdkZGM2Yzg4YzliZDBhYWI5YWEyMWFhYmUwMGI3ZGVlNTQ1MDEyMDVlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InQvelBQdmhqbjdPZTdOSDZaeHg3bmc9PSIsInZhbHVlIjoia1I1U3JNaHV3QXFta21qVWowUUJUbjdNRTNBY2lyRWxXeE5wWGUzU295MlhnUE4xdDFnSkZ0M3B0eDA0RDgxTGl0VElqaHZhQ0tYWitKZEpGdlpZaC9YMjFndkt4QVNDdWdLcWNrUHpZUVR5TjhDR05BelNERmU2KzJuRTkxRGUiLCJtYWMiOiJhZjUxNTA5OWQ1ZDAwNWFiZTA4YjNiYTBiNWIyNThlNzNkZDY2OGI2MTM5OGYyZTI3NDJjNWI2MzBiMWRmOTJhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "9n8l1OTgB01qyxgqoWF65F2Bbf680TvofVqpR2Wbpq8-1791956697-1.2.1.1-zGe96Dw07yff5NtYSfHgNDadUvVS_jRzJKvCDuV33e3zXad4KWCJCOYUAuDsIxSaVojeKkrqIVnzyPum6S5Md45IoU_C_QyCGvhoWV7KaiQjWciosvHJrtmx1I_Hgwfj90ysTEFzO49GltfFPFoHZlwxzD51JUWPahOA1SghdMeNf_T90APtoAyDHRCeEFDTPvw5eQOUuwZFf1cd80BGVTW68uUmfNSN_o.jgxkEvAhArXcbqcTDiqvX2vb7I71j19HMwKcWGvLDcoA51HuT.0ePKQoC7bdi2AJ_S0AaIukfeCjLCLoqBBn7VW4F1mPIdStKQQY5oTqik7jDNaZNlh20qGVXc2uV18sU6yFfW11cF4k4FK320tsz.AS5kIo0lK_GSSUMI1GCIUQMahJM50sHiABseq4A7dBnE8AMPq8uBE5KMKv.cD0UVB.Wmyn2atdM.xRnhq0OQF_76Nq2uBy9yk5MAIy_Xm_bPQUY2sHk3tU0UDVEdTxMlW47FGSyV4uVvt_fREspF_SqspeC6g",
    "XSRF-TOKEN": "eyJpdiI6IlFzN0UzWEVMVnpTNVc0WmJLYjViR0E9PSIsInZhbHVlIjoibXNNS2JBcndRL1hjUS9IY3NFVmlLdmhpSlBSTktyaEI1WmpLb05FK1VZdjlRZk0zNHhTcG1ta1lLeWUrVGREWUNXWUo4NCtjUGorMmpsMURwOGQzQyt3YXkwY1h0V2RuM3hIZ20vK1hWN2I2OXJvSGx4azFXWmZ1dVJqa2N0R0giLCJtYWMiOiIyODA0YzVhOGJiNTk0YTYyMmYyZWRkMGNiMDRmMzk5ODE4ZjBjMjczNTUxNzA1MTc4YmVkZWRlNWI1OTIzZTZhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBreUtEOVBHNi9IREYzN0h2T3VSTGc9PSIsInZhbHVlIjoiSUNwZ2lkcm8wME1wdXFlZGlMZXFzRVl4Y1R4RG5TS3Jla1Z2ejRjaUxMcVQ5bXJITFBIdnV4QUxsMDBCd01WSktLblh1eksxbWVJc2sxMm5yV3JEenM3eDFvaDBsTnVpK3pjODYwZHRoamhvak9XcFRRamw0QzFZaG1va01KSXkiLCJtYWMiOiIwYjZlNGY4ODNkZDgxYmNmZDYzMTg1ZGI3YWQ3MWMwMTJiMTJiYWM0ZGEyZmI4NmFhN2MwZjY5NTNlZGYyZmFlIiwidGFnIjoiIn0%3D",
}

