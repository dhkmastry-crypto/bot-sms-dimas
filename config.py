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
    "cf_clearance": "a2ogArsNW3AMon6R.d_PH6JSAXYb.N9V66OXZXw3w.g-1792074524-1.2.1.1-KTP_JSMeVkFk.X3c5koZrjgKuZKxNY8qrWAkUxR.bA4kwskKHWdUehye1KKUNCQ5JPj3tUPS3HEvkL3WgX51cijgH3RFIck5O.03qiNJ7Ck87R9ViJ.pcUJNsmFyXe1VCSt9H8cA5QuPktN0bwjidDrX7U6LDdrvreaBtA._zKcqHDtO4EdTtzWj1WdDrvC9_LAo8d25Au4Ij2PrT8Ntcg9CAN3YZGrc4gfmXoMOLzle9JgtVlZzutMcm8l3QRHGHJbHQ9BIvTr.ppr9_8_qvz3uv7QxwAgZEUgz3A1oOdDoQ7mBNcobwMrXxxsRm9qDNftQYXpAAiSUMKi6uqqzPDCoN4GTkrtj_sCUtS7AN2cZD.9S.S3FbmXHuI85.2YfxbynnK8_C.hvE1QTseghj9wb4YWokTLuExmnyVxmzCZBZyDEO0E4SWkl8fBuoEZuNDlJTBa7V9oRNLJOG17E2wisiPDDxRePTuTnQZATpfzoDvpi0.kE_CzVo.E9QpWGIMf5UYfZUQX66fgJKAewEQ",
    "XSRF-TOKEN": "eyJpdiI6InhYVUVCSlM5RWE3UUJkVWM1SmEveWc9PSIsInZhbHVlIjoia2Q4bGI4SVRRQXZlKzJzQkRpNWtKVDJZdnYxYm0vSVp4VG1XV25WZURERkNBdnVlaFpBUHU1cGtraUtoV2NNeDJQYk1sQytxQnpsTmVzSENURHFKUHRmQ3VCalpvZ2x0cnpyRUpMMmI3TEpYZXBiU0xZRWVHaUt3Y2FGOFQ4bnkiLCJtYWMiOiJmYWM4ZWE0OTM0ZThhYmMyNTgxMjYyODQ4OTNhZjgwNWNhYzAyZjAxY2M3YmZlYzhkOTY4ZjMyN2MwYWI2OTJiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJzMHA4Rk5pUHNhUmhwMzhxVzhUR2c9PSIsInZhbHVlIjoiekxQSDlHLzdnTFFPNk5PYTRBQWhQd0NHSTE0ODNqM3pEdnA4ZldBeXdvNksrQ21aMWR6d1FuVHVDYnYwZzJXWWNMQk9mVkZwdXIxckJ2czJ6aS9Vc09sWHlMWFZWeTMvN0wrS0tpdFhVZjNYZ1lRMjRBbFhaS1BkWDZ0MVErWTAiLCJtYWMiOiIwNGE0MzZkZTM0MGU2MGRhMTNmMTBjNzcyYWZjNTYyZmMwMWE1NjMxNmMzNDI4NGE1NmNjN2FiMGFhODA2MzcwIiwidGFnIjoiIn0%3D",
}

