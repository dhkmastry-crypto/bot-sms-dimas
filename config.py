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
    "cf_clearance": "OttS.eS6vUFzR_rFz9Vavo8kYkmwAmcL1NaxnD8d_vQ-1791942143-1.2.1.1-x5YIEjXDOVsQZqmt.ZugyRN9i82FcY4MbcCxRs2WummwACsd0tu6xBCHEa2CKTc5yRZu6tnsqA8VgPx_ux2biC9HcATWH3xrhWr51at46vSnD03sBpAioOqKIlORq6zu44RpCwtLVpnAroZw0INVPWQz9amwyQLutF07R8751xUPA1uDmfKfKm8Bo1tSjCbjdU0p5hRn944xkya2SZxJI4eLtSdQb_O00hdUyy4SSF2hW8wI16VaZRwBblE8wB7H1I1nIpFpakCrPctCUGg4Qr5R02fB2Yq88KBRzSj1Uw5Vn7QhO9XZhz2J1ItDg6kyfw1beRP_P861kkQsv2wvJbmIkHFqLwdFwAi0awfMkbs0ojg6PN.nyIu0Lf5t.eva.kkQuhoMHDbjV5U.fNchXbT0ho2t87En7jDZNzyDus7_7p5YhCO0yuAoREIlZ.DTBpCewPaGDqAu6RHogJG1mWG2vGsvpCvPrpqHalogzSvi0NLrJnb0E7B7170rUXkMbexEn6l70puWVp.dxkD1SQ",
    "XSRF-TOKEN": "eyJpdiI6Ik9TRzNxWGNYQ0lXdUVNbzZpQURQRlE9PSIsInZhbHVlIjoiRWpmUXJWdWpqTklNWUhjeWhiR21MS0NCWkVzQUFwYmw2cTkyOWt5ZU5vc3JUYlZubWlERkNnRkJBUTdOLzIwMTAvRUFCU05XMlA4dFRIcWs5VEptWXVlQkFjbUZKbWo2dkdBcGljamlabU9iQTl4TlZOOEwzNkxPVDdoTDd5dVEiLCJtYWMiOiI3NDVmMzQ5NzZlMTNiYmI0YWVhNTQwMzQ4ZThjZDQ5NTNhOTc4NjBiYzdkZDFlZDBlNzBlODY3YzdmYzdjMWQ2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1RamNGMEh1V0NyK3dYNjJHQnVUTXc9PSIsInZhbHVlIjoiOEEvUmlYcGg4YzBVVnN1ZmtIanlyb3QwQjVwc0JlN2MxSHVwZXFzL1VyWjRUY0VTUFBndDlkZkpnaEI3R2ZZamJlRE9aMEM3NUFjemxsRVNmNWcwVFZNOGpNYW82Q1ZaWGY2UUwxbHcxRTlMR2lXaGJFcG5Pa1ZLMHB5SXdZUloiLCJtYWMiOiIwMjhmZWQzMGQ5MmUwM2FkM2U4YTQ0ZGRhNzM5M2U4MTdiNWUwZWZjYjJkMmRiNzRlNTI5MGZlYzZlZTk4Y2U2IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "T95m2BTX5.6qLhw.sA9Tc75apUr8ESkwGDLCCMWmKx0-1791942175-1.2.1.1-t_aVc71QzkiaIKnVHjXJY6ogUjEK9PRisEiazl0trg8goCJlop8nR_jj3mfaQc2oxJkFEPOKohhG9T6HpEnzcZih8yvqiUKjybU_Y23z1xO8VEV17q8SyPWpECrJ_1AGHWOPxbub.sOjkCBXN_brljNjon8YxUn.8T.O9lBzwaf9nrTIN1c9vo2D3Z_6CyGNd2Z2LSUoq6_al1tC9AXqA0kqxJGAcx7cCY63FCtzBXlwPEEhtJNFHIWTl4Z5.a4sNeRU4KEFp7GAle18wjCZXZ.VIFy3RClS5gUn3T5K6PEHmG8r0M0ht.mkhE8lLao0z7QaSrIwR9_YGgOrKdNb17ExpTe.WiOnLB3s21bIply1snmYe8AKrXTRDbPEB4zL_Fzmg0moCMkqB4SAX.Rmum20X4iqkuP8.7_JgIOpPJ5qAJ8ha8R737cq6KQxtvTrsx0mQ9nc.XSll7dIK3QrL71n5QofruI_4JtVdOJFh9SovQbdMUew7ArQR64CDiRAjI6zU1hPdMaTI.woH8K6zw",
    "XSRF-TOKEN": "eyJpdiI6ImcxSVBvb0kydWRlVXYrb0pzNnV0eGc9PSIsInZhbHVlIjoiQ205RjVIQXkvaC81Z0t4aWo4aldnYjNpL0d4Mzg4eHdiR2JyUmx4VzkvUHpFb2xlaDRJZmo4Ry9RN04xR3QvdDB4enUrWVZ5RjI4bWROa29CSVFVdDZWbExIWERvcExoMTN2aW5KajJibFZNZ2puWDliRmVVQkFaRmM5cGhkRkgiLCJtYWMiOiI0MDA3NzliY2Y1NThlYTdkM2Y4NmFlYjEzM2YzYTJkOGMzMjJjOTRhM2MzNDVmMGVkZWY5OTRhZDYyNjdlODk5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhOV1ZTWDNyUldnMUMxbTJKUUNqMGc9PSIsInZhbHVlIjoiM29SanY1U1FIUmgzVjZVN1VuTmk5WDVlekpqQk5XbUxpQlZOeTZxQlluejk4bm15c3lPVVRjT1dCSVZuUFkwQ3laYUgzWk5yZDVWYUVHSFJBNkxGdEZDdTZLeDVCRS94cWNrblZsMHVFaktuVlduVldLTUNwU3crTnlhOGNHNkkiLCJtYWMiOiJhZjdiNGU5ZThkN2Q0ZmU1NzllNzExOTM5ZGM0ZjU3NDFkNjgyMzZjNjNiN2M3MWZmNGU3ZTZhY2UzNjllOGQ5IiwidGFnIjoiIn0%3D",
}

