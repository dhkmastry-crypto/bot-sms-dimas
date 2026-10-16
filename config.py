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
    "cf_clearance": "Vx9FG8GCCm49vXEC24jPXUZYsw8NfhgXtMnu9GkEPWI-1792130756-1.2.1.1-sOWI08Fr7ttkeGZbo78HwDiJSgKPREN5ExCmuqUnRdZLhJu0boTeKraJmCxUxfNpoQf2fnh0metzktV7OKpWicndH_8dm7CcyjrU_UCvuju1dKliwrz5jswxd_ekWl70oDFl9ozGOMSNPol0PoUFWOx14JMdvBhUMLLXampTzTG_Dz1raFuXlWLaQqOguQ6QkruKgT8tkF4nMRRd61BDtazqfmSLQNJDrmKYDKZs9fBY2aV3bnul9ZvieTgqDbRhDz4thr2KKd3MyQMl0.U4Z5nwBDlqkQBqHj8EPBJykXQbbj5RHCDoglmv_77yhVWdnkyrBT6ji67ckS1BDo6OOrLE.pXmRRLKyvW3CIukjHXmMLI36rZuOi34dP5I_YgD9c_u3WDlNF5QRvp9XpVIWE.KFdkphmTUa1fW9PC9VMg_bRmWQ.cUNyrh3tE4nXxsj8WESILlvcigO_7tG1DZB3a.x9OeF8Te6wFpUnCk4vHJ3zFVV4cOjlgRYEivnYDnsLd2xM6z_wi6i50a3TI5Eg",
    "XSRF-TOKEN": "eyJpdiI6Im9lb1lFcnBsUE5CUkdpSXdOMGlLZEE9PSIsInZhbHVlIjoiSkxlWnNWNGFFNFZOU2w0SjJCdTQ2RnlJMGprY3U1SGcwUFJNNEoxbjRIZ2FaVk1sMmNuQi9CWXd6Q2sweUczNkUrSUdmdGRLam1lUjJzeXNzY0VRbFRRYmszckllU2U2MHFFMVdpbm0rdkZXK2swN3FTQnN0WU9raEFhT3BFSm4iLCJtYWMiOiIxNmY3ZmJmZjZiNzdhOGUyMzU1N2VmNjFlMjAwMzlmZmZkYjA2MjhkYTM2YWNlM2I5YmY4NDhjZjZiZjVjYzhjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkYwZ2VVWU5ZbDRrTklkeUU3MzFYTkE9PSIsInZhbHVlIjoiN2ZucW9UK1pqMDBMWk9CSnRzeURZNjRLRmN2Y2lTQnBSajY0Mno3MTJvanM0TWlBMVArMFAzOGQ0NWorZ0hMVHliaWdYMGlqQ2czWEdkYWZtR2ZrSTJQaGdNbC92amlIMUpQZUp5dGdwMGlndmxtY2NaK3dscmFBQ1hXYm8xZHQiLCJtYWMiOiIyYjI4ZTc1ZTc2YzY0NTUzNGFlNmVkMGNhNTZjZDUyMWM1ZDdmODE3MjU0MGY4M2Q3ZjlkZTJjZGMzZjUwM2EzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "whdaF1bcNA.t9tTk.dWczJIBzp_yJJHbwzdU.Ib8xaE-1792130735-1.2.1.1-sLqza6by.USBG6mFXV7c5Xln0czA2TTnggz59OYpuqx7ot0CGx41eZTegbxxW1M7UQephfeeAhps0nKyQBcARSm6siiKZlY2W2ifhGBzMchzr9ZBvi9jakGQl1TPCn5BX1UsCVvsz4GuSUFKNkJ8VNOohiGpO.MoHoh.czAUep6Z05gz92wFJ.rpTCNFQsY41qNUsYg9ngECdywWSM7rhJLGxD_DlxB1WAjYGiDkc9g1aQPaknacKFEqLKTA_aSREdVY9pv5lxJ_8XXugyb5GyxIEDbLhKYolSuBqnVFwhThonCApHUPA7U1jN9tyBbG90SyvHsIk2kNEtlUjVjifrNqewfXL2brT7yRE8lrv7AKwmyHujnIe_p_ZpixW1mum0sIw9_.kKxPPGTEjUztFeej8zUE2XoAMCq5LrbSaku_ZuKw_xe8WXlFzEkJn3Kxpv2n70kEXb8RXilZ121qZCwUVhr8nupqQ.0zlIHXS07up85izujFuxvs6AO9nPRDQAXKjnd0eHsZnyJvehxw3Q",
    "XSRF-TOKEN": "eyJpdiI6IkpZNUdVMFZLVHhNTk5DOFh1NE40RGc9PSIsInZhbHVlIjoiWlcrTkw1bndmMHNQMVVZY3JYMHowRHFzazlJWDFJL3VLSyt6SC8zUWE5TURMeEJkK2JUemJZdlZEZTNRMzJ6Q0QzUkUyMm8yUGgzTkJ5WWJZRlFzUEFPWGs5cGVMa3MrZHM5L2tVVGYrWWRlOGtMcGRmdkVRREI0NWdLVnhjVmciLCJtYWMiOiIyZjE3YWQ0ZjAzODhmYjllMzAyNTc2YjY1MDEyY2RiY2FkY2YxNjI5MTZkZjNjOWNlMTVmMmQ5YWQ2Zjc4N2FkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRkQnN3Uy9iaEtqWEg5OUN4dEhzMmc9PSIsInZhbHVlIjoiVk1FWGRnYWg3d3pQTVNtY2kxOXdqb1NzaDFsRlZiVCs0MDRudEp3cWpQUElWZTAvQ1JtNUhlQ09TSzl4ZXdRVDRZNS84SDcrVXFIcEtWZVQ4dm02ZVlxMDRGSFRVdFFEMlZRSHY4b2xLa3QzYlI1NFNaUkdMZWVGeEVIam1oUHciLCJtYWMiOiJiZjcxZWZjMjViMmEwNjM5MzFlZDRkNDFmNGY3YjM2OGI5ODE0NThmZDgwNjhhODc4NWZjNmM3Y2M4OGM2YTcyIiwidGFnIjoiIn0%3D",
}

