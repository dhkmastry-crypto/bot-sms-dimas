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
    "cf_clearance": "Gt1pVzmr3XPPASXnt21DWE6gPqj.NHSrdCd8OvNoidI-1791983783-1.2.1.1-I2Bp6wbVZNueQLcr19LV6hOpIiqWW.5RWaIwOAoMsgyXV6U8gvxW35ZcwfxInOx7jkowcR3eyBl6K_QJ9X.Ok8Ucf1pnPYGpFez4sPrnUKPdzt0VWz0b3gJPvoP.kuZtZbZ91IXqsb4F3wCGtttTUc9HlC2m6tVwzji71ImKzTLKaSobImlzWZ4_vcqh7P0tQ9CXGgwUvv3oCkpuGdFSuDagFbu2iV9_L_BsuYBPop8sWknWi.bldULy3_AoCr8Vwneeqri8_mxHrsdoqL52E3mtQGG.GvukgY1WqrhZ.6rrfokq10YOoIoX7HTnJ_F5maQS.rBGUmyjGWJHEzZ7x76A1p6_.tUknzdxFDUY5Ez1neV5zov3PUD5EjXp.EGLOhLyh1gQeF0F9cADfO87rnAfJDeosdHEXGTKGnMgnvJfbJ4PY.PIX3hDRfVZtpHwh2RRExyjnH7Sp9OXWSl.FlUqPouCLnLXLTEEuWcHIm0dm6nKNOw5ud8WYyMdblVEgUTXMvEEkUiO9F4j_I5VGQ",
    "XSRF-TOKEN": "eyJpdiI6ImFPcnFsLzR3eUpkR0hMZERNRDFVL1E9PSIsInZhbHVlIjoiZHhLNk9CNmxFanlrMjNZSmxPTkpIaUFlcjNWbTlQUGFGN1N3dC9OazZMdFNIWW42T3dydlFQMndMcUF4TW9icXRoTEM1N0oxOUR6Y1UrcEVhNmxQcmd0L0VRdW1kYWlqWnJmNS8vWldiTmdCOERUb1c0QkhsS2ZINUM4NnowWUoiLCJtYWMiOiI1MjBmYjM4ZDUyZjkzOWNiYzFkYTZjOTk4MTAyYmNmN2RiMmI5NmNjZjkxMDA3OGQ1ODdlNjEwYjVmZTg1NWQ3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImlLNTlEWTQzdkEwamdYa3d3eHNRa2c9PSIsInZhbHVlIjoiZTRrWGd0WSswc0hWcDNzc0pRaE52dFlNaDVyazBKTzVVc1pLb01BbTEyUnBzd0VLMXhEalpDcHZCREwzNVpBdjR3L3d3dVJ6WXFvd1BLOUhDZ1dNYXNMSEpabC9mRXRuV0t2cjdsWlZTZ1h3RHl4MlEzUFRzdnlLczYvQ3ZvNTIiLCJtYWMiOiIwZDVmYzIwMzc4ZmFjZWYzZDBmNzE3YjM1ZGRjMWExYzEzMjA5OGE1NTFjMTA5YWY5NmU5ODI0MzVlYTkyYTJiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4FF_23_5zFZh4xmv3AQSlLz2o3Fp7DvHUKD._iWPdRo-1791982042-1.2.1.1-msPHBX8C3pR.rnMJYxN6A6FviQL_MMA0gs19cSl2qjtmXYArnfJdZvmIX6YRZwgds3h0HHSc2Bx7v_SLFGVCUELk4hCKaAaM1JTdXMw0RKBzlUTipAiu0UgAzW6VLPia8fpqlzRVjWeSoVyhU49z6zS8WCNdLgormiusWqSsiX1qZrROm7e0mqYHAH3B3umnAR9am_2YUfpmH6rMCOx_ohnL8BG9ImyIapfzkLIa...e6M.lD798niRS7LyBd_eTfuA4EXPFVTFx1k5YdujsnrsWCPU9XkpBOHBoBLzW5DVup5CDf5EmSH2dXDBwwJB68hFyefWY2bm6FqsbH6LejoNNeKJaeS12sE02q6I8PMqmNw.Q2HwvNfqf8YWvPyK7xiF.MeMGDw1F2PH713dIG3LKug6RD7FanU3E8ywPKLtFhkN6w.6QEpAPCvCYnWpN3zj3NDgx7onpRKAsiD989_pI63DikyHd.45RJRPgDfzuSfiO3IG3bK2F20HkIdm7euP_ZScTAtUaf7D4KPSHmg",
    "XSRF-TOKEN": "eyJpdiI6IityUmxGcDY3UUxEVXg4V1ZvVEtBc0E9PSIsInZhbHVlIjoieE9TR1BQQjU4SVhyWThDbW94aFNkRE1iWHZTdTFtc1k0YllHRURITlBYVE1DanlubzNDUWZOMWxndWdtelpYbjI4YUpEUXVhTEE4ZjJlMGIrcHc4a0hXTWNvQWhNZU44SkVUS2JicXNsenNXWU51Z0JBNlYxdE1wUWVmV3pCYVEiLCJtYWMiOiI4NGYyNmRlOTZhN2E5NTA1NGI3OTNhYTdhYmExMGUxYTYzYmFlZTdhYTFiYjNhZmJkZDc0YjRhNjk4YjVjMWFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InBGMjhXR0tBblgvMS9zYjArbC9TZkE9PSIsInZhbHVlIjoiSzRJdHBoUEswRVlkQUNaaHdpOHEyZXF5RDFuSFljcEthUWl3cUJJVzZJOWFsMmZuRzFpOU5jYlhheTdvbHFJb2dKT1MyeGtOQ3NqSXdSTlk2bmhQclYrNTFmL3lBeWF2S2x1T3lhUExJcVppUmp5eXdGdGhFN3JENWlHaUlzdlAiLCJtYWMiOiJjYTJkNzQ2Mjc3YWQ5ZGJmOTE2OTg2OWFkZTMyMzdmM2M3NTZmNjYxMTE3ODg1MjE3ZDA0MTI0NWM0ZjFiMzliIiwidGFnIjoiIn0%3D",
}

