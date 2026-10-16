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
    "cf_clearance": "HZKHAmFyJFxGEcO8bDuET.J2oVoaZDqgpalJ8qokOas-1792128943-1.2.1.1-_nh.OxKoUqqp4aFkwdAo542LFKO_swQG6UH7DDwmYKxxQdxyHfLnljgEOqu9YZRFhNqyKWG97jdthZ4n5olQrBM8LX5.ZTxZF8Hd1mCMKmq1_cumTsqZoknnP8Y1jUYjl9rSEzuzJRARVfquQ12vbMBSR5qdPvFF9ddl0M0XOjqSl1ukaLhcrKqcQd6bPugEh7UKnWvByMvc61Gs0_td0VUol8n.8VRGvme8GYX31vlhX.zxmV8fWxiv2mxqYDGSMUj0g36C4Le4xiDGv3FPqSVX0bfFJI87yeYXLUs36bnSNlAXNvzC5czRhvEa0jOoG6KTs3T7gJGgav3raFlx.ulnQWz2kr3nV.KW3HZ6gUnGmp3v515BIVwmaytxQvMJAV80f2KBwv3jcvNkNqC7DVWl8nDOof41I_w7QAIt1hSvs5QoR61wp9XV.OzaCjlObjvEuqYCgh2cdMfV9baWMfbwTbTGMVSD57ZECE6vhUbUU_WRfNPxKz8tUqrTo5a3GAIHRdNVQTMB87QZoqgSiQ",
    "XSRF-TOKEN": "eyJpdiI6Imk2VnFtQTg0eUUvdk1EdVA1SUNGS3c9PSIsInZhbHVlIjoiWVdHbWpabkdVUGtIbUdSa2E5c1JObU4vTUhSbUF5QjZWbXdGc2pBeklUbWx1VUN0K1QxQjdpMEIvemR0TUxrK0o3UkY4amtKVWpsMFlqRmxEbVNQRTU3VkhtSUJKczdkQXlsOEQ1VGQ3K2tFTHk5NER6a3Z2NU9vUFB5TlhuU0giLCJtYWMiOiJkMGFmZDY3MjlhYzI5NDcxZDY3NDk1OGUyYTNlMTM1OWZiNDk0NGViZTQ5NGYyYjZiNmRiYjAzM2MxMWM1NGFkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlRPNTF2eGVPclAzaEM3UHFVQkVVdGc9PSIsInZhbHVlIjoiSGxhekJBNjdBQklRelBJTkdGWDZITno4c1FaYnVKT052TncyVW5iNVFMUEc5RkVBakw5ZE5pbm5RajEvdTBSL2VrdHZkTUxPVnBrUmoyb3ZOaWllSTNkbTRrUjl0U3JoSE5pclJnSWJrODVhYXVlemh6UnVPR2xlL1VybjI2d2kiLCJtYWMiOiIwMTRiYWI4OWY2NjdhMzBjNWE3NThmMDgwYzZkNzYyODgzNzk3NmEzOGQ0YjY3ZDNmOTAxOWYwYzkwYTNlMDBiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "lev.g7tFx6YhOiJBN34Z_kvMTDkis39y4pSP5Q1FZ1w-1792128930-1.2.1.1-kTy0aE26nYfe1g9AYwCo0P4b0cvi4K1YqnjJqCcw_a2J8EObOZUEyfXiRdJ0aV8ufaGywkN0xeD6mQHldkMPsjv.1Otmy94LL0i3d1qo._cFABPtgGDo.OvcaS_KANZzbEEWHnmR8MiKB.E8uYZrn7lEeRWvYLbkcnuDB_a.m.LWMXrBa4MH5gFjw5.Spj.IUcW6.VZHRPEEI6BmrX4OMbmulw8CmuMsQLyf5kJoF0M8ZVqkigE3XLnas1VO5Qit2nwDYTtE7YlY73snPD5DoMVc_zK2tEsSULr44oaar7rpGolYw2rbExMoL0r5G_1CJRvQO6I6bXoMH6T7Yxk4.om7I5zJliQerPHhVqEHjFwhwuHT2TmMctUqD5o3z3w8u9IVwM8xD7.brs1XaivBmurKhqIoVOJazBzZ.5bcuTvV.3fOHrEV.7.gtUiZd.5y1KCjC_bhet9_cVIKpXky6SS5qyfNk_W.sG_fvWppsY.2hIKNTqzogD8YK2pN0i4Xhf0527pO6EFkm0aqCoyeZQ",
    "XSRF-TOKEN": "eyJpdiI6InRtaGpoeC81cG92T2g4SVBmdFBCNmc9PSIsInZhbHVlIjoieXQ2Z2F0V0NHcERMNTRBNTdnZjV1UWdOdHZzVjdUTWJwdFVzWGRZSXRLTDdpaVczdjdhMTgwZ1RIOGMxV3gyUHpGdjVnd3lXTFFYb01rdVVKdkJVN3BXNDFOUGNJWVdQZkwyN2d1VnJhSkFBVU9aVTEyNkNpbVlFanpHN0JtajUiLCJtYWMiOiI4MjUwOWQ0ZDZkMzg4YmU3Y2YxOGIyMjE5ZWQ3Y2U0MWE1ZjEyNWUzMjhjMDU5ZDc2ZDViMzMwMjgyNjE2ZjQwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImZSMmNTdDlJK3hzbnE0clhuSDNlUVE9PSIsInZhbHVlIjoiVTlIb3BPR1BQNXkrWXBRQTRBeUlTODNHZkN6S3cvSTRsajhxbWJ6RjdmN0c3dXF2SUoxRGRoWEJuYyt2dFJnalBnclFUT0Mva1QzM0tUYno5OHlLdk9XOW5BUy8rS2xad240bDhmbmNyekludlNpdnNRZitZSGdmT01nK3dRa0siLCJtYWMiOiIzNzgyMjViZGIwN2MzY2U1NTliOTI1ZjQ2ZTE5NmIxZDM2MTAwYTc0ZmZlOTg1ZmRmNTcwY2M5YTIyZWU0NzkxIiwidGFnIjoiIn0%3D",
}

