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
    "cf_clearance": "zmT.lEyp4vFoZEHYzSHHSsMGVuVevZOJcZ8QoGJiVrw-1792101725-1.2.1.1-NSZV09kpcS1P_.ubTpvce4oIZKG8QjewlQGu9LKYWhcvQULwV_JlLboyvHYRh8wdra_19kXljoGn5EKla.CAS3UghkRRI1xYiK.datlV.U5Uup91YCfXCBbHBZrByxbf.LO8hnMJUFnTQX1qjZOCYUzlm5rLqprgJsrp0tWJDp.3hIeypQTtIVQmVZQR4OrjEUFQyVfmsNsWaRvw3tKsOWAeClKsaqn4bG_Zezx4JKMYMwx3jp9.jPJMJAk4IVd2Z2Tu3GkTy8eHFLZk2qdXPFTfWxz5NER0xo84s9jRFjFhpVmGhCU.i90KjymAgwJgUXBfnMPad5D_yRNv8NUoIRVZDhvIdOJjIuz9aZPkjPcO1jbV1zB.AIEZCR3g829rpblxXmdGQGSip6dLuXsO9jJColyu7JVPlwnf2LOBkdxAQLZkE32vq1BXHap4xZvonU1cQJpKI8D5cYXXy7paLMpqDDMoPI2xC_O4NpEAnN2P06WFLkPejQNs6EFoyiOopKjDSKtATZWBtqJQ2mFnzA",
    "XSRF-TOKEN": "eyJpdiI6InNvKzVKMXNxMFJob2xOZWtFTWpxeWc9PSIsInZhbHVlIjoiL0lGcjJxTzNmUWhVbHJDVlJBWkUzMnAzdHhxN2lHdTlVTkVUYm45R3BQTE1LSkpPcFhEZ0lEd241L0NCTE85Z0Y5WGpUZkVyalJlOTdIS0RHa0dSZzUzajZHVjdDdTBIb3VkeVA0WEd0UlFBaUpIRlFUS2hWbVQrbDI5QnFMQ0wiLCJtYWMiOiI4NDJkY2E4NTgyOThlYTI0MzZmYjA3N2U1MDMxZTcwNzZjMzhjZmJkYmNkYTg0Yzc5MzdjNDk4OWVhNjkzNWIyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlJRTWtzZEFZdS9Wa3BzbUF6dy9lQXc9PSIsInZhbHVlIjoiNVcybHUyL2dySjRKY0F0QXdSbU9CMmxMSTVCMnJCdm52R25GSGIwR2V1Mk55Z3M5cnNuSGUrZ2NQY0NuSy9oMUdHOUdiZU10cEY3V200K0pGY3FDbEc4MW5HbTUvaGNVTGVtMFdlVnpsUlpEZlRXT1kvTkpPcU96WDdyYUY2TEIiLCJtYWMiOiI3YjNhMzIxMzMwZDkzMDgzNDI1NjBjNWNmN2JhYTQxMjRlZGMzNzFjZmU2MTg2NWM0MThkZTVkZTQwZTcwZmEzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "uskA1iPaJp4f.B_WIIJoiCqr525rrYiHOC0A5cRCSKc-1792101767-1.2.1.1-_tBmqrZ.3ZIqSQcdUQJup07PtZ99.DOFgwZUqwtf87YNsbWnozVyO58TLzyCSXCxgmFsjfjuhRjmRN2H4hCsBdzHMEMzM277GlaC1Rl0_gVb0cB.qvn83BuzrYHaH24xAbF6Z_4KvRFkK_p1E496gJZpL_Z4P2L4X3wt.0CTcTh6Zroit9w2ht8qt8a_XwIOQGSfrWv5upB.vukAPfuJMfnPL6OhtjTYkhDbNup4X7cMoEogeWPNOU5D.n2qShz_jica8HYUcDVsFnSfFsGomfQs9Aa_KOFCSPPa541P2uGZbHEmjlprpqP61d48sc1jvI9x7nCtuBCLBDoAYK0KBPQ3GXQir3MMySqlie9JSKZkQkP5iwLpqcNpQju9Z5nPel46yxUDO_k_qaJXib9Xic6mlJ9JYDwxGzCOWVHSFWZ.wtIuD5ntH_obm6xz37QZgbfyde6tvwl4lhHeZDSW4B8rNEtcG6AW_fyRVDuIZ7dXWAAuJ0S8_7ZGEbDEf3K9yEq03Jj.iSQmtlBExkrXmw",
    "XSRF-TOKEN": "eyJpdiI6IitCQUZQd0FSSFc0V0l4QnFVUWc1TFE9PSIsInZhbHVlIjoiWXREbUgwNUlJb2pPVFFpTElKSlZxb1A4dnBiVHNqZUN3bjk2UUxKaU1sYzk0SUdCYU5qa2FpS3psN0lMcTRLblN0dlcrVFF1UEw3L1hpNmtYNEpwZkRUQzZxZCszV2I4L2o5SklrMkhtTCtsZFdXcURXNGUzdGZEeW9VQm9YZWYiLCJtYWMiOiJmNmFmZjUyNjc1ZWE0YjU1OTE5NmU1Y2NlNmZlNWJiZmQ1OGI0MTgzZTc3YzYxNzZhNjRkZjIwNmE1NDg2YjAwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IklEZ010UGh1VkRtSG1odDBxMWhUM3c9PSIsInZhbHVlIjoiQyt1SGZlTzdSL3FDKzViby9WSzR4bmg0YjB3dzgyK0NsL0k1bjl4S1A2VVljVFFuYTBiRUdPcStRQW84VHphMmExbUJuc01QMitzOGU5WXVsZVFFS0JIVEpMYSs4Tm0wc3FOMUVYU1ZPR2hLQnlKbWRaOVYwY2JCYVNST1JiUGEiLCJtYWMiOiJlYzA1MmRjOGFlMzllZjgwZWEwMDMzOWE4N2VlYWFkNjlkZWQ5YmE5NmQyYzExZTg1MmE2MjRmZTkwZWZkNmNiIiwidGFnIjoiIn0%3D",
}

