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
    "cf_clearance": "HtHW3E7EN9PCOmzPk3SUMpGb8vmhRBZAmvYYXr7SdoI-1791954796-1.2.1.1-9Ui.mxfO4n1fff.HMruGEt_Ni8mLbr.aeqs4cxJ9X53cPIcKMj85kC2jDL4sK_P1f2QU2tcE6PZXfZUl7ia72.sGQxF4f.R.FJKInvupizWLGouqd5FSbVGMoPyaQU.U2oF74pRNy9qVCvLPFSPX6XXwBs2zKxBHMwTcOxGb0a0nGegZPTYOumYCu9ercD1dzbB46qUQomknOI5k0oV5Iywua7bpV4z69eeoPcfdCFE55AWJu.jlNZ_16ZuKN7ndB60QXOCgJ6A48O4DOoiVJ11y_u5c7inXfUowlC0dYBQ1xCeyvNYTOdrznV7pdVgZX_Y9M3EDFDMRkWOj9mdCTAztspuXn.vLPAv_rGuYV6abKd5N27jnMT0JrrDGxQmrX.9_qC.NvhEbLsVvZ6QT2u6VnLFv6Ct0Gwz8JFmy2Pc99lMypUj0p6fzmsMaXvyp4xO3JfQVkbnNypZjZPs1WgTywGXiZMGuq.LTsDnZvl.GO6UYlpoTJkZBLNLercspBw8O1SyBtVmgeY3uBQuiOw",
    "XSRF-TOKEN": "eyJpdiI6IlQwSTJsendwMSs0K0liaXBQODc0Zmc9PSIsInZhbHVlIjoibFNvMXMrNUMrZDZpck1CMXpzdTloY3R2aEV6OGNpT1hqcGhlMm1XVnlDR1plS1NiNXN1QmhSbktkeEtibWdQUnE5RVhtY1NqZzdqbXJSdkxqa0kzOW4wZkUyQjczeXRkYUxtSFhNc0FjMW0xZVcxZWxrcm82NEo1Z0NUaGlxdHgiLCJtYWMiOiIxMDA0MDYxOGFkZWNhMjFjMDEwZDJjNGQ5ODg1YjIzOGRiNzZjODhhOTFmNzA2NGUzNjNmM2M2YzhjZGM5NWM3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJKZGRXSWpRNFVwaGE4M2xrNjV5Rmc9PSIsInZhbHVlIjoidVlBZDhjbW9tQm91dVRWeUEvNS84dnJYdS95S0VXLzUwSHd1dTR3d1Y1UTJMUklEbm9DME1ZWVF6Qys3TGFEZmVoZ2QxWHE3Z0Y5NnZVay8yNkx0MnBrejFtSG9zcDVPdWE2L0xjd0wwSGdiTDc2WEtJOWplMThQT2tacVhtZG0iLCJtYWMiOiJlZjBkNWRiODEyNWY1OGJlZTA0MDI0MWFjOTMwMDAyMzkwN2E1MTU5ZDAzMWRlYjJhYjg2ZGE3MzFlZWNhNWRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "YC9DO3w4iV9oP0OKy1mhfbekZomYhSVyMKyp7815NrQ-1791954883-1.2.1.1-G7wkSnznp4byPkzY60VGa89c4ZowaaVG8KXGYjSHBlXl7dq3tt_xeYvrrddxhm4zM5ZtB5txxk7.QQDsCH76.JzhDcuSO0sHB1XpG7_TRVS50Dd8CdVsUy_Q7FAVTkNldtqIeci7UG87A35_ttqYI5mp9fvpgXCP7m2LwQvaImeE74Bl_vynf49b2hc6Qbj3CtyQqSoCaFwbwcMSFi7KN1K1hiplcBa_sUcaZjUtZWQQR25hqCvTonzs8OTMRK9ewDe2REgqT4.f94FnPqhHWeKEFrlw0oE4RGovMB0RG6rsIsepeJy.u3OB1SVDXqZIPJicVFVK3_LPljinzvo8RPDk1583PuC6sbr7.aPBpBC7Xq_VTrB1iia5cn1Bx6wCMlqI6CH5Fpz_6ogsjGPdK2KTxxFqwiy02Ae18DE32JXRa3z32CJm3kP.XZiYF3VkNjAsAmImqCSnU3eZibJNnp8VSMdG8ITiCngBrrCfTHMFbHjs1a7Y2ePwUCVMlbhoNaD4UtQbRGnWCCKTmG4BmQ",
    "XSRF-TOKEN": "eyJpdiI6IkZZYmg3VVRvV0syUzUybENBOG5TRXc9PSIsInZhbHVlIjoiTDlqQ3hBTnFyU1RmVTZHTTBnc1FlTUxkdVV0bHRDRi9NZmJKYkxUV28zMlRSNXl2OW0rcEZGdlBZWHExaXowZWNpRkVFQ0lJbjRTRkwwTU03U3FvcjVtNGdiTm0rWUpxQnozbXdPWEFZNEFUZ0djcjljT0I3T2RTek4xaytxSlIiLCJtYWMiOiI4MjMyY2U0Yzc2ZDkwOWMwZGJhMmNlYWE4ZWY0OTUwYzBmMTBlY2JhNzRmNGEwYWQyOTAxZDhjZDYyMTEzODBlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlE2SnpQQjJEUGhlUkIyTjE2YnVzZFE9PSIsInZhbHVlIjoic3djWG5EcTZVY2hKU2ZOTlVUNW1IN3Z0Q1JiUEpQRUNuK202Wm1wdjJzRkIrSEZGMDFTcTAwb0JWS2VKVHR2RC9YRmtXdHJnZWo3UUdFOVlhTG1mZUZ0MFo3aDExaVgvb2FxbGtUNUFGWkxpMzBEM0lXYUZPSU4vQnFHbGRqa2YiLCJtYWMiOiI0MmYxODM5YmQ0ZmFjYzkzODkxMjYxNTFmYWUxMTQ3MTg2M2QwNjhlODlmY2UwN2YxMmVhZmE0MTA5OTVhMjU4IiwidGFnIjoiIn0%3D",
}

