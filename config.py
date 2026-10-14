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
    "cf_clearance": "ijOhz5wC5Bc8XIYJobskzQDHVcSNX.D4X1vNfKjPPSc-1791999308-1.2.1.1-4_hl5WiHkgfp_cp_qnIB637Ly44ou3hMCkkPxB22R8j2wO7SEkV4DFJNlGA968OS1JPRE4aM58IuUZAGisMAMQnMuTW3XmzOChhBL0I7iG5tmjufcmovnHINxBgAN1Zqqew0NBddz7wTO3uqT0WdIYkJJaQK9MxGx90nf0S6q84er1hVQ3wNsAtJ4MHOMiSo.sBWW2pQSLcna40gKDvy8mndZOsOE4X15YtA4IfB3DgZm39h0f8cxiEEj.j4H7NDibP6a266jUKnyZx6dJ0mXmigXUkmnzYkrEh5N0AJl7aaoioypkE5qEMOGIH1xhmQKi9xINPEH7MUXIVNDb_DssBZk2TJgv9JVfq2oZHJJhReZ7gLAjC4uE_B0j0baSvOul3XUFVI56jhL.zH7uLxEUGFtOctL0GlUnveg2F6pNgXzxsuNgpYlavN_wGF..jhEOlQ5yjDfT.sTCaNKhCYZEX211iO_am5bsw1ZgwZEUzn9644qDWCsm1S2paIMx6x9A285pksJyd0kruz3rmxRw",
    "XSRF-TOKEN": "eyJpdiI6IjdYS3ZHMmJjd2hvc1N5NFZrMmZicWc9PSIsInZhbHVlIjoiMTFmSHB3RE9QZkk4YTh5ZGR2d3hVblRobi9LamZHR3ZPMWFJdjN3VHJKWCtpU3F6anR2NGw0ck5tNkRsL2s3L0xuWGxqMHhHaVg2eksvT0VKTDFTT0hidWw3VG1vcGtkUnlmOExlaWZQanllS3RKL1VMVWhOMFZOWlhMdG5oUy8iLCJtYWMiOiI4MmQ5OGU0Yzg1MWMxODExYjI1MjkyNWVjM2M1MTY5YmU5NTAzOWY0NzVlMDQxODFhMzFmNDE2MDVhYzllZmQ3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJpQWNRcXdRcHpIUlRHSWoxQS9leUE9PSIsInZhbHVlIjoiK2cxMWxQZ0RhVmpuZDdLaFVQY3R5KzBBSUxPMCtQMkxXWm5OTWcrMDhpTFA0TGR5dnRoZk5nWUtpSVdZV3QrWWRtekhXTWIzZ0J2bWVPeUZiVVFVUEpuNXcvaGg3dFFiMzdoS3lkN0JYR0szbUNHQTdmYVpuNi9abVVnL2phaFciLCJtYWMiOiI4YTdkYjM3Yzg5ODZlZjcyMzcyYTYyZmY5ZjFhNzM2NDJjZTRkNGY4ZjcyMDZhNDQ1MTFjODQzNGE2ZTJiYmMzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "vlalGDlcxbxy9jCX_mxe4eWws6LHUcfMRz61cYtOvjs-1791999317-1.2.1.1-bHktQwGOvjJzrSx5S9WrYZK.EXsY.ooP1SPRPi9G5rUYPLMdeEy3xySJbJCMfQ5wjUsElneXYvzbPcgq02ZEw0TWtp1lirAQgt8mqjsIappfj9Q6vSBPQXfoVO6tRIuwLxuqBZ___1Ka39PBUAhynk0XtXgnTpw.18ZrQZXnJa9MSde__kaYXO8bxCQ_KUDUO5ZzKgl04tCX40uRmjgKYSg1V8Bk4M6NekQ0ujBwJDuAaY6nKx.3njN6ul9Rtt8nlaJZjNSjoAc2yVFLrt5Zjjr9TX7qYCNeS0vGpIAhC6zeNVgvo.oQVATZPagil1S6pvGfqskEfI.dhtRpK4aRROtmCz6DZx2Jc2KHqdGLj0aCO51sE4FS9YWqVFQSlOfiumFVSqgIvKDC9YIMxzEj5S1wGVjJ55AhW2d6siNiqXaWn_kc46V.8LIUXcSSiGfYcLGqs2H9ag7InZmAaRhRkiqKLsGpiYMijKIEBcBLJbevZ0ked698vDpZT4hgjSoCFjxfUUS2Q46pALS2bSKAWQ",
    "XSRF-TOKEN": "eyJpdiI6IjlYMmJkWjZ5VzRnTC83WHkxQ2M1OVE9PSIsInZhbHVlIjoid2hWYXZEVTM0S3R5WG5BUklyTEVzZmlxRWJqcUZ1czEybjNIbVk2TVNlZGk3VkpMQjZIT2lRbHlxdFV5cU9tM0pvU3hjL0QwZEFuVkxOYWhXb1hQQ0ZpY2NyOXFHNGdyUXFPY0d2WGZNL0dvZTBQVElIaDRCWWlCREgyaTViSUMiLCJtYWMiOiJkMWUwYTZmNWFmYjM2NjVjOTgzMzlmM2IwNGEwZWIzY2JmMDliZGFkNzVhYjljNzk1ZTAzOGY3ZjhjMmU0MmRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IndPay9IOEZTRHlWekU5c2xMK2xjUVE9PSIsInZhbHVlIjoiQTkvVGZDQlVtK3NVbTNpUk9lSmNZVExwWERyV2UvNDJ3ZTlXRzZDK29aamVCM1NoUTV1aXY0TWJaUWk2MEROemx2MllVb3BwL3N4U2VwY1RldHhpTWo4Uld1NTF5MmF3bW1hbEtuUzFrQUdzWDg4TitHdnloYkRHQTBZVEJ0TTUiLCJtYWMiOiI1OTkxZDE0MDhlNDE5NmRhMjYwYWU0OTMxNDg3MjFiOGU1ODFlZGYzMGI4ZDdiNjY2ODFhNjQ1NDVmODUwNzlkIiwidGFnIjoiIn0%3D",
}

