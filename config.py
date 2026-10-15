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
    "cf_clearance": "t7eQBiJFWwNVA_OpgRKCDYEKPX8FIqQmin3M1gxTj_w-1792074567-1.2.1.1-bFGRftizVuieiL9XIa4fOPycO7RQ7trOr.0NCyxVwWAkIXl.hXuUyim9HNF4P8l02sVJEdr_D8pm02QoXpFdKQpjHSVwEESGsxgH0Py9ajzUp8MvztGpxjY4T098X1suecjzwFNegVXMfujx.RKZaoJ6mscFg.d1XuvO9WVxp9LNmMuHpO.62RQRWG2P3.Syr0FPpx_PJt1Q4FHLGs9i2EEAh_5vhXCmqU0rImgRBk60iBMhwgkuvJ1VtaZl0lggvjxw4HTSfXJ8QQVy4fCZ9ivkVwGUdDkxRxM3y7UeEoNVUk2nqklE4vO3iuu.AFooIeBzNMfghTNrfm6OAoXviDlNzUJsLKyXNPLHhymngK2DmuFaVxnmtmaki3ktrnIuvo_AOno0Zy9UwoTZiyM3PkggJX1xlVKY8897JoRmSmWAfFAf_WWKzO9zDSNchVND6hl6dBqjac4gezvIeJxGJiSJPd1GMX7vHYONnuHj1482GAkzxvFd6hnyQfjoFhCkrz9iru_3VRwYiEuMFrK3dQ",
    "XSRF-TOKEN": "eyJpdiI6IjU1QmdFVzFQNFN2ZE1BRGorR3k1Tmc9PSIsInZhbHVlIjoiZjBlRENYSDVUNG1FcmwzYlJ4K3NVUUNFUTd5SDJSaHRlZVZOR0l2bjE4Q3VqNndXeG54S21ZcFc5MEZkYjR0dmxIcFYzVm9PZFpFb1J6T1lSemtKTHNsQWlMVWpSc3d2cmhVWjRaUWZ0RGpRMjlqeFZSaEJyaW11ZVB0ak5GUnEiLCJtYWMiOiJkYzE1OGViY2I4YzQzNDI3MTdiMTAxMDU3ZTQ5ZjcxNzFlYTFkMzAzZTAyYzQ5OWNmNjRlMjY1YmZjZTBiMzEzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjdpYXlaakJISVBqS0hWZ21CVVdiV3c9PSIsInZhbHVlIjoiTHRUd01lT3VtZjV3amZlMCsrZjhOUUUwSjJUbGFmRVI5SDNFaXpjTUZldXJTUnozNWZIRjFlNUxTR3h5WGR0WGZpODVzNUcvaUx1a0VGZ0NESzdVZ003QVVKZGM2MzhRR2JpY2diaWxxdWlHcjJ2a0t2dlpBOEdmQ3VkSVJzRlAiLCJtYWMiOiI3NWVlYjNkMDZmYTU0OTZhNTQwZDkxNTRjNjQwOWI1NzJhNWFjMTM4MWY3ZmVlNWNhNzFiZjdmZWE5MmZkNjBhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4Psh0XCDRid.Uuw801JNQ6nI2NyYAmRmCZE1nsSujgw-1792076330-1.2.1.1-C4MH_JHds_bJYmbNmK3AYI6dmx_ZR6frHtpGU_Y1j8.TwxFARLRoYZdT5fegnFeFEH_iL9H7sbly5jyFCYLlPlT0GvpX8.pe2sxqyifHFmXsdI0tVzQo26Mpg93pqllabtKjBbXewUvSnwL67CtrRvC1yhdvF98vQy3WT0TVXZJ1c8OeGQhtJoZOEf.WwlyLj6F_rHeoB0M4FvXpL9wydXQzXkYJAVT5yE8CEAX2HB12u_K25uqaCrY3RzeGd0NccLNi2wN6OIey9cNwxHucTZodU82191bqYyThWiKZ0L9nueGwUulhrUiZtySgwhu5XddfUSTYFHPrWSocrEgM89tCne_EJT_UbYW1gCRBG8B9Jts6lqxwksmPFg6JZFvrer5qXk4u.7vZGuG3CdG5sVT2i6lAKU2FpjLd7QpFz0hYfBs6QyaYNm_hCtmuinWR78jQLCZsIxq_4eG0ayldGUfPGj6SzNysewttxiDGthRLDbaCxDZy.oTCgjxEn6qYnArZOdgj9w24h6l3oYS6iA",
    "XSRF-TOKEN": "eyJpdiI6ImhEeHJoRWhtMkRvbU1qeDl3R24yV3c9PSIsInZhbHVlIjoiY1lIVmhnd3czdDM0MzJmeldxTUlSb00zcjNua09IMXVTNEM1Q2krQ2ZBWkdDYWhPVEtFUDJJWUNSR3BWdjQzR1QrYWYyMlViRVpieDMzNEZYMFhiU0hvcHBzVzlFUmUyVURPcE5SSDl6c3pYSUxZQ01IZVhSaXlseDkzM0t5aVgiLCJtYWMiOiIyOTkzOGE1OWU4NzcwNWVmMTgxNzAwZDU3MzA2Mzk2NjEyZDM2MTk5NDAwMDJhYmM1ZmI4NDVmOTBmZDRiYjIwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldpanZudDNPeFBCTnhRVHdPbjVnMkE9PSIsInZhbHVlIjoiMEpnWHlNcWRMRjllV1EwUkVFY28rNXk1ZFFyQXZjSHRmZXhKbXM5RWxoUnZibWVyN21LQ3Awd0sxNkdZTTk1ZElsOUUrTnpKaFl5ckt6U1VRcXllZE1reFljMTYvaU9GMzlPbWljSFFQa0pubjBQUXFqeTRhS2RQOVRLVWozYUoiLCJtYWMiOiI0ZWU3MWM3ZDJhMWVlNWNjYWZmZDg2ODhjN2IyNGFhNjUzYTgxOTA0NWJhYWQyM2ExOWQ1MTA4ZDEwMmY3NmQwIiwidGFnIjoiIn0%3D",
}

