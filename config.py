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
    "cf_clearance": "sSRyEO8PojQ0o96r.yAmyM7OCRqYEGruQqUFg5pMRqM-1792031924-1.2.1.1-.21PqnnB47nRbGyb2KIJCmjVfoIoJPnNZ4MYQtGLijDvHtcxNfiy4t3O979Q7MGdp_J7uGVqWoQOaLrI4K0p.3haTB6zz602h5QtwhDSsBc8jxvHD5JUH2brJrpbi4fiGNjPUvPSm8lvnxBiMRyBL2fexhvKzPbZRnGyTxN.akqTCphhzhn9CdQqqUiIZb1BW.hR9gcqM9AbteczfXCV_ArHZ5WPLjrVO1HR83mvlHlhNDlxeeCFUjXjiaJdXbZq6eAyByAzZ3iNrp8rqXkio4x4gxTJvdICxH9zb1mAB45WC5NCr9AeW2_BKM3zt8A3AcgoqMTTI8phGRbk5dNaRgm9LYbCK90QjLBeeKC_TYmsAgdPEwZO_EneDUjAg_V_DDxpppOlxGn0XpcRHY82KMdrdDHQZGlLaTZX5BnOWAT3EFS1.GNGmoKtZO5i9VE5J5qjShN9oBB5m.hSgziq0M9RveGjqf48xNdsKjFWv3HOwzRsYrtBPtzOBmdkW1v7oaCzTOWbLmxVhUpvXd5kNw",
    "XSRF-TOKEN": "eyJpdiI6InY2Nk5XUzF1bElFdFhtTHJvTkpJaFE9PSIsInZhbHVlIjoiSU9KWEZJWVRkSEp1bElUbyt4R2JESkR4aXlMcXpKNEtHaUd3ejNOWjZ5eStwVTM5N1ZHUVk4dUI0MGFCdTRmZi9IaG4rWStjZDZrdU04TEJvN28xa0ZVTkRsZ3U5eWpFRzFndlZscDRzd0dGWXp1VDFqbnY3MFkrU0Y5a3RGYmEiLCJtYWMiOiJiZTI3NDZiYTUyMjQzMThiNmMxODhmNTM0OTYwNDI5ZWRmMDVkZjQ1NTQyOTg2MmE1M2Q0NTI2MjBjZDI4ZjQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVpMlBjcS95VkhaZDlOVDZwcjUxNGc9PSIsInZhbHVlIjoia3RFNEQ3T0NoVUhSRHM4S2ZrSmh0SUNPcWJDTlRRaVpWa1czaXVzVEZVRTZxeWlEUFBBTHJ0YVc5VjRCOUxOMm51TlRrZkVRR1Y0MTZsSVhVZHNwWDcza0w1SFNoY2pud1ZsOVV3Tll1blF3MEE2K2RUaisxUnFhNUV1eEtZeTAiLCJtYWMiOiIwZTE0ZjA4NGRlYWE4ZGUxODlhYjdmOGI5MjkyZjM4ZDg3YjAwNTYxYWZhYTk5ZGVlZjAzNWMwNGI5ZGE3YTMwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "qzrIJpOhPvfyGCQDmDjwlkHzQD3MfbWTPk3uWccc7bA-1792031914-1.2.1.1-EJ97jCp5elfJ0Oe_3KTcqn_OmSWPloz1Mzh_fw4ATBicI9rGcyN8xjdylg5Uj239UmW06SATfp4xq5aqvciCrDAyQWKJKUJXp2B26S4YSwWysGbcEtj.r4L79b_NqkSjfqHtZ3O481glALWTu8DOzhQ8KRH4H4jZk96Kdaax8mFhFFk9gE8vq.ydhGMR_0Rn86BVRi4SM.5u__oe7EpAXdUsUSSp1PTjRKQY21ykfxhai9BIwn2R8z.2SS77mOpQejL5cUOFwESPj6HxuriGUH.v.Un6QHeFdvZuMNcx3rNy8mlkacpodydBcZinnSgVxt6C1ScRcH_CcKMG1qSpxYazTl7zjX6_pwxd7iJXIU11GdN7VE_vi7Wb3H.uxFxdwHcDZpN56OE9CMq7wTmQ3fZyh_kJuTaocESB9o0YJVVVSUucag0u.bbD9so4cSlzZCDCOb.eOQ5UrdJfxysfQLtF5L5VJPGTaRG.dJXiGUB24czSPEOBwME9fRUFXZPSets6RXqzkNJ6IRYwSkqsBQ",
    "XSRF-TOKEN": "eyJpdiI6InFxaVFENEp1eUZoQjgrUWluMkJhV0E9PSIsInZhbHVlIjoiM0tsUlUxL0xvWkVuWE1IN2ZWU3hvUkxobjFtVkJSdU9yRzBFQ3I3bU9lb2JzYWU4N3J3czVidTZhWlZVVmgwY21kQWJNeS9LZThKSU9lazFXSW5WbG54RytLQWhxT0VKK0VKaVRHd0poU3lKWGlFbWFMN2lkOWdiWUtzL1FJd24iLCJtYWMiOiI2MzhlNGVmYTIxM2ExZGYzMDdmOTQxYzFlMmQxN2EyNzUzNTk0ZjljNDgzYmRlODE1MWE0YTZmZTBkMDE0Mjg1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlJHN1hvdzBiTjR4TWwrTUwvek1Md2c9PSIsInZhbHVlIjoiekdFendmVUpNMjI1ZllQbWg0Vm42UDYvajM2aHZZajB1T211Y2ZYWVVQb01oaFh0Z2dZb2JHUmhlSVpiK29ybkRuY1F1SGNzcVpiRjVvcTIzRkZKVnZtZEtCekdPVG1iWEtsOU5DZGU3WndEaEM3dzd2OFpoNlV4UDRGbVEvaDAiLCJtYWMiOiJmNWZmMjA4N2E3YzgwZTRhZDdmMmM1Yzc3ZGM1NWZiNDcxMDY2ZDZlYTRmOGFhNWI4YzhiMThiOWU1M2Q4MmM1IiwidGFnIjoiIn0%3D",
}

