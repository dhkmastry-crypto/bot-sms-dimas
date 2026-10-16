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
    "cf_clearance": "bYEm1bX1l_PbhxHYV6qTLNUwaGlhjnBMskLTNSqTIa8-1792110814-1.2.1.1-6RSdYTr_8K47.XxlbKX3Dd.dDzey9umkeUYQS6loFQSwSmsDfXFD8Yz0HjfrV691E_Gv5O4OaplDY3SM1_tdolIPiKjJwHAf1vkAPtHd9kCp4sm7wdZqAgdQrF4ZhCjog0.HFv7b8ilwYrapPxIclOFnLP8nkpGadZKjFMAov2qRRdypqNs2CLF7J1ccElkG.BhcDnwT7fTo.okqaXR6CYuD9jiEu__dvrljSbwWKKzVsdPXc5tBeK8wT6XPp4ALf3pzGsbVfP2p2lqsn2zjBQOz8_2Hg5Jmcc4IsOedI6smSWRLK7T181KgiACcNFivkHtmNEF2Bd6i8.sAs2lX23MSHhLt7t1vottNcM6xxkwoKsRRlH4w7I4GWYX7h7.0ML62UzyjgvO6S5qOH7i7cpbaJFNEmwQ1TjG6jlmtCxbOrSHTBcjiueJeZEkF4gGfIjpYL.L7iCwfoLx3nFflJWA48ybglfH7Uuzja47IpvhH5CRonAaaL.vSblXp845pG2YzsPNVcBmEAIGtP0oO8Q",
    "XSRF-TOKEN": "eyJpdiI6InNWcjljcENLdUpXS2NVUVpBaDdjZUE9PSIsInZhbHVlIjoiQmwxRFZ6L3o1czdLVW9Yai9VOFR1bzErZWFyS0tSemJibkR1akoyWktycVNyR1duSTgyN3gyQWVoTVNza1lGZ3NIb2hHYW1pRnJnRjFSTUZCTkJhU1dwVTJ6TXE2UitYSy94YmNxMEg3c2lsakNyblRlNVpDeVJhaUNSSGZpUHoiLCJtYWMiOiIyNzA5N2ZmYWQwODQ4MWYwZjliMjNlOTY5YjliN2UzZmM2YzQwZjcyOTdhNWQ0NDQ2YTBlNmYwMDgyYjI3NTdlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBBbDc0TUkxYnV5dEFJd1gvREZ2WEE9PSIsInZhbHVlIjoiU2pKT1BkcWhIZ1Bjai83blpRME5lZTlNSElwc2N3U1U0a2RyNTUzWHdmMlpTY1ZKYWR6bFZJL3pUVGY1VDJKTzBBaEpqNzNmYXlJYzBQd3QxTXZTWEtnenFLMnJWUjZ0akVDUm9oRVhvNllJRFFJRUdLQ3NYdEsxVm9yOG54cFQiLCJtYWMiOiI0NDQ4ZDY3MDM0NzA2YmRmNGZjMWNmM2Y4NmQwNWI5MWNlMGRiYmU5YTEyOTE0MTBiMzJkOGRhOTRkMjVmZmFhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "uAqyZ5ZqZ7nBcr5WJogOcGmVpILY4CjqEX5GUNWvqp8-1792110825-1.2.1.1-GOwOeW9AM8XWIqVfEqf03XvlOJMjZjRWTxL1H042xrnUJ1D1rmkutxOR0knRAH0LsXyvf1nfnlrMLWKZozlmVpVnr43SfIQLPSGfFSNvzdZ.cExjiX.y.8bjz9CymUgjUY2F81iQ.uKp0uWMSaZowlay19uDBAe7WeL8X2xY7cNfr8Q7PAdWjv_0fKyw03S6kdM.e49G_kpsQn3_Ag5.BaxalGFs2hnXgKtaGXlIDiQoiNzTmW16m2gDJRq5t65Zzvd6eBfIqEU4qYe83zFCSYseeAXF1KL3ZHfgqj6EGhXukzPgsDddSwmvv8gN8IT9PPAOkFD9Qeun1lYhM9tcMp4ckjzRLwFdx7WnsySKw2G84gC99oXayhVOVEjCP96TxtvhefbFFLck_0XtC.OD8SlRLzpnrbr0yw7ZpImWHyP3gMSwQxTchYTXFESnJctS7HcflF4v96fQjB6IsKfpBuY.0iORfn8dVsQIvuPvydA3MRoZbmc5WCUD9MZjNmXbt2THvyhTqyOSRadkPvDWmg",
    "XSRF-TOKEN": "eyJpdiI6IlFKMFRkcklpVVZaR2FYSHYzWHFsbnc9PSIsInZhbHVlIjoiQWlYWGsxL2x1NDgwZnVaejJqb0NUc2pOc3M3RHdoZ0VEeG5rYUJ0SXhSVm1Tek9JUCs2Yis4TUowRG5ZTmdFdVhtOC9COFV3MFVxZW1MVE4zYkEvRVpFMDU4YUV2UFdLdHEvL0RrREdZSjk0cm1lRVdKdGVwaTFlZkpLelZPR0ciLCJtYWMiOiIyNmUyMzRlNTBiMTEyNjc0YTQ5ODI4YmFmM2FmZjJhMTU0ZmRhZjJhMDg4N2U3MDNjMGRjNmIzOWUzMGQ4ODRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik80b2JSRzZISHJQRWFXRlBWcTBvQkE9PSIsInZhbHVlIjoickFqelpsV2lnRWp4YU9DcGdyaitMcnFCeHdoSVc4TFFDZXZSK2k5SmhTMnZwWDV0NVR2S2RTWTNGSkRkLzRxUjdSckorWVBKNmVGZk8wYkdESERCUG9DS09aOXVxcHllbVVuRVFzOXFzN0JYTXRKZS9LbDZiaC9IYnZJMnhaeTkiLCJtYWMiOiIxZjc1NjA1YzQ2NzdiYjc0N2MyODhhM2E2NjA0NTljYTczZDEyMzNmYmFhMWRjNjM3ZWIyZTg4YzczZDk5ZDU1IiwidGFnIjoiIn0%3D",
}

