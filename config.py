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
    "cf_clearance": "xorFWwaD2pAP5miNngJOmSIW6R8dJO86dquR6iRbAEw-1792022860-1.2.1.1-Xp8xudPOt2UPg0As.y7H9fCrcm8HJBhEKD_juAk6zWSwWrCfp6iD20R1_LXpTY5C578mj5Nt.QYyVUykB1pSscHwxBQGx7iYvt4gqMXzHdwgkYFH8ScqgNB0mT4qGkfP_qn2Cm2YE6pN8CipX3xjGODmiQlFFUvYB15UjAg4DpaQohtfXiIeB1_oJQbCU_3Un.ySE2s40cQAVoGH9QpMHoyU9LRlKRjW3PSrejahrNIjklrBm2byAsdsrgcEghytw7s3U4nnXnL8WLNw1OOH..24_QyQ5pL4paIXvcMl0WfQpPiER6laYnxHduZKSWUCaISZ2v2FxPNBMvRL3Uw1Xlhp49OTPjnkFx_rGZIzSuSzPQnPbqR3d3uqiGGDTbMP7gtY9cOFHrzOK9g2z.RFmX5oGeg2BRVeOpbpcvScmXTmTicx54o_5N9mjA7dWEdpktqulHIaOJBnjb4ypmUeRBiYQlm6yxIYv1UFkdVm7Ta0X3_xC4H7KWH3YsAHkmPSsqTSetHyviHvL525vGvtkg",
    "XSRF-TOKEN": "eyJpdiI6Ii9FNDRhMmZhL2FFMnVtQmJIdUM4OXc9PSIsInZhbHVlIjoicDlGbU5oU2c2eHJsTmxMZkQ0NTFWZkZKZVI2MDNxYWRzWTdsVTJXaVB1WStwSTU3VHlCanhIUHBQTG5obmd6bkNCS2dYSUFYUUxYU24rWXB3NVFPemVJMnQ3MEFxTXhNVEdhY2ZNbTROc0ExcWlFZkVwdEdCcnlMOEhkY0VqTWIiLCJtYWMiOiJkYmY2MWVjNWIzNGUzYTc2YzgwODgwNzI1OGVkZTlmNDlhOTY4ODkyYjFlZDEzNjBjMDFiZDg1NWJkYjkzOGQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Inhha3lybVlhNjU3OTU3SS9YdDBkUFE9PSIsInZhbHVlIjoiWXFiVHZCNktMWWE4VDNHVGdwRGFlTTNEK2ZwSmkxcTBHUUFaMjdzUVlFMXFsRllwQ0xtQm5RVlUrVktSUkZaWVBjL3pyQkp4ZEFOb1hZQU9oTGw1azZUbVRIVk94cW1kSTd3TnlNUjNsV3hDSUtpYzlaRzZVWTBTRGhWb3Y1RjIiLCJtYWMiOiJjY2ViZDI0Y2MxMzVhOTBkMGUyMWI1OGFkYzdiY2ExMzlhMTI5MjUyNzA0N2JlODk0MjM4MDFmNzhlYmY4YzRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "R.MwvYybX_Uidkv6loy3fG7Y1jDvVWhBLzgcLpyrn8g-1792022849-1.2.1.1-cRa9wSs.s81lfSqluHNjlxF9qJfXuyZQC_1YhARFVX5WhlDTcJ1BRUj5bvWNuiLI_oB2yCU_UVgAaJeXTKU5.pbhROLyaov4ncxUTOajk0nuTs6jvelNgMHdpRpxvgQqBYeoJo95gl0FupOk8zRfjwVMj8Yh2rGh3Gij9w1Ejw.r65hN6yPuBptVmKf4vXJGHRu0IpAnx.nc7Es.NDZXloXvB9yWZpVUv_phL20Lc5It_EZ2xXFRLm5ArbAL5FREUX3N48wv6KK5UzQpcC.7IODpq1kUlCpPI6QTEZbOrAYJm8fE2pZv5L2KBwUIkk37jQjCNzedST2mXx9nv7gX_ZynFNHIvaQvyVF7sxTAOPyOxFsfS7N179GzPwQQ.r9RTX3PQ9kZE6.F9tqHDsCDvC1_zIniVQFlSCZnyOc8gD4elbznSN3phGhwBU8xmfV_AxshMOjQT7aYEIEFzNPrQtPJ47W8LzAMic57H6eBbyLjZ9qMiKXoIMn6tTfVzxeSDSq0dOEB7DZZH9bz_Czt4w",
    "XSRF-TOKEN": "eyJpdiI6IjRPQW9HeG1UUGJUV3BxY1VlUEZudkE9PSIsInZhbHVlIjoiK1VxNkpkU0FQM1hhQ0dURzRFWktzaXV0ZG52TDNhdWVWdDA3djJ1OG4xY0tZeHRySUpmSmFyU1hMMFlZZ2FWWkJkNk1YN2VianlwWkEvbmlMRU5iWUdydTFmQjhuVmQzRVBxRHRKakRWWDJ4UVFNc0pqRjZ3V09MT3VxNUppYUYiLCJtYWMiOiI3NDMxMjcyMzZkYTQwM2VlYjU3OGUwYzBhZGRiNGYwN2ViYWNmMjI4N2JkYmQ3NWQ5MjYwOTU3NGYyN2E0OWFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjNNbmk0QTdFRkV1U1pVTENZRWxoRGc9PSIsInZhbHVlIjoiU2VXaVFZNFg1TDRMV3J0NUwxV1UzRjg2czQzOFJIdHRMWEF1OFhOMHVVNXpGTDJTZS9ydERrTWV6OUxkRmRublNkZk91YlgzV0VDYWNQZVEzcXZwVFp5K3N5QzdUTkJMZGJTV21LVWR2ekNuYncxK1gxTWN1b05lVVlXYW1pcHkiLCJtYWMiOiI5MDkyNzllM2ZkYWIwYWU2YTJlYTFkM2E4MDFjY2IwZTVmNTM2ZGIzNTAyMjJjZGFjMzk0OGU4YjgxMDAyZDEyIiwidGFnIjoiIn0%3D",
}

