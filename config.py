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
    "cf_clearance": "TZEESBY1Yt95Tcov9scUpw3wzDydFl8XkEI.OK32g6w-1792116283-1.2.1.1-4kSd_K1Kk6HRSnPlsRU89y.UQzo7ZlfyXK3xcLyLIJLtqS7I.q.RrmXankzJS1PPFaw1Z166u3hc.pLHAoRVhslCjUH66HEj7PQS.4MUJFNTh.qL1gpH_2M1WFraFUfMeYfZ8yY5tFgnfxB_lqvibkkK1rtCXoKIyEZRYlk.rmWQ9b3Z7HmUQPCscqbQ1t8g8CHeH46NA3jG91p25KJJ9GKpm045UlrGy3k7d9HKPzGXj6er9SCRiLYynl7849FwWz.0ZvuXEREcPGm7F8kzCiLv5Lj8.x5XHbWk5YOumZKzGPmPZoe8FmrzptSyTuLQalV_sAIdPJOFyNmsRlGVIEImfUtCiq5l.i7RVnQitf0Ga2WwiJTE4YXa699dsH_hpzt5OI6tge1DfDxAfHV2YRvaTr6HOYfw0RxVbHW57jdudbVOpxICpzaRZbOeGP1c7RvcD4A.TDvTMJqOMrT_nhAR9M4WNjTEVNQog0n.pqHHsHNWq18NnaQEDpNS1O.oW9fSXxEtCa6HI1w9THQ1aA",
    "XSRF-TOKEN": "eyJpdiI6IitrbXBEcUFLYlpWemVUaVhBZTVIVWc9PSIsInZhbHVlIjoiVnV5VmVZMS9EZFNyV0pnWjZvdlhFZ3ArTE1CdnlCTU1mUDU1T3JIOTVYYnVod2JxYVQ4Y3hXSEVIOG4xYXJ0MTc1WWd6TzQvOUMyTHFZMVhKRlF4a2hYM0YxUXRXaU9IRnpUZFhNZTYyQU5vNWdHbmt6ZlVoV1poUHFuMVJDZlgiLCJtYWMiOiI2NWIwMzU0YzMxM2EzMDFkODQ3ZGYwODVmNzcyYWRhZWM4YTBiZGMyMzMzNDk2YjNkNzA4NTQ2ZTJjOTM5N2ZkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxBNTlzNEZBL1NDRnlkN2tMOGhYcUE9PSIsInZhbHVlIjoiVnNraWlWNjJSUVNTN0lwQlhRdWJuUVVtRXcwakN0WXRQNmJPUlpvakVRbkc0Y0I3b3phOUZjalZhU1FSVlU3c0lHS2VBdGxadzJlK3VYM3FLRUtRVHFjOUM4TEJUVll4bXAvSXZYek00c2VpUHhyWHZUSlkzSWZtenMwS3hoN3AiLCJtYWMiOiI0OGY3N2MzZTAyNmUwZjJjNWQxNDM5NjdiMzE3MzkxNTAzM2FmYWE5OTFmZTYwYjE2NmJhYjBmMTFhZjBjYzgzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "QDk0suVnT8dqINedVXLiCWfgFOh5a9Yn1lhInmURpgw-1792116265-1.2.1.1-6f0jI4KkY.eWNCmV1Ri2vE27K6O0XC6nvbYgXFEHnpgGhtSnzKzsZqAITfhoRjXBTO20Dnar4Xvk.2vSY0Cv1SWtXYmzBK0J6hepeR_n98EHyfVhmNEKlgx.ixdeuQGzoi1GeL1hVqjyKaaD_D3tA2B.nhXfpsyiZ._cKfI0oQKoO_CESTqyaSsaqocOz4zXL77u1JJq6FPC70RkVMzPiApKCQLWBoD0dHsWw5746jAyf1jOKOdiAZr90rmVx6o22YRJIAo2tHSyHaDtbyT.pcGIY0sWkkzAJAScVuOsDP.VNO0gTGwC1DYE7RHpypOdazUIiVgB2WC6.qGGl4fNppgHRzfnUVjFweY33BstEd5L2SEbMEAEBsHTp0VXkIHs5sR55U2mqK9kh_JfOGZFjawsQshwkJ4U5ConLqFWbDcgm0Xq861Z1qUiVAFD1Ck3PH5nkRNDE82a6e1vxq6GPuIBtjjZBt1tvjf6mkcx39URUSAehdm5fLy804rsdSVVlE2.LKUeME_h5UqvqfMSww",
    "XSRF-TOKEN": "eyJpdiI6IjRxcGQ3VW1sZGp2SVEvUkJ3YjRvNlE9PSIsInZhbHVlIjoiOTV0L3pBaDRkM2x4QUtWZGQxcUU3S0luOVlHNzJIekd4WHQwcGEyN0lUT002bjRZakY4Q3JpT2dnZW8wTWVyaWVMSlhkcEV0b0FocnhMTUlrYXp5aVBuL0I3RGt5Q21uRENGSjc3YXllQ1YyTlBmeHV0WWk3eTRScnphTzlQTjAiLCJtYWMiOiIwMGJiYTExOTI1ZWRkOGUxYjJlYmRlNDQ5MjE3Njg4NzJhMTdmOGU5MjRmMmJhYTcwNzljNTI5YTRiYTU3ZDc3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkloaGxIZTBTK25GWDdOcU9DUEZWbEE9PSIsInZhbHVlIjoiUnJTYWkreENCYStHMW8rZGk2a0Z6WTdXemFvOFFadk5PLzZHcC9TY3ZMZDI5SWZPR01mdGNNL0h3TTR6T0ZzVEdCS2NaNjRHdll5T0l2cHlFV21kSDYrVkttTGkyemdVWVlrK3N3aWZEaHRKckkwWk5HeVp3dzFwTmNhM2NXLzgiLCJtYWMiOiJmYTUzZWNlZWI0NzFhYjQ1NWU2YjZiYjIwYzA2MjVkZWM0ODQzMjE2OGMzYjVhMmNhMWVkNTE2ZmQwMzU4MGZmIiwidGFnIjoiIn0%3D",
}

