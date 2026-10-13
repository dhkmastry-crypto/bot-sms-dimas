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
    "cf_clearance": "8ruGL4OKxLUcNMHLYnSyo3fOniYg8VQnZlIyZvtU9.M-1791934906-1.2.1.1-YKpjWFNpgHQ7612OsPVe8YMuM7xuY1g0ehhsgKGWP7qWRmSWWwVsd622CpqJtNrep0GKxhrbsi06QxfeKGigOjpEP8W7wteqFOVTRodJjVrCmjz2i1DpM3izS.4oY4bUBgxjFxBwCeXoSOHgKey4HMQjh8Wg1d.gHzT0mLekeioGQ85EXx5fon7CiSHb6c8aRdx8DZbvbaMm5ItaVMwprWWMgCdCkfInHbWZ_gpa02XORnKo7xQdhffsGBHDzqd44uTgIFQX7GNXSYNCS0rFJDKtbL8fvtkUVaEgXoguiErEDJIT9iKRTKeBcpj0GnyuufxkoBvJRLRC9vxN8AXZ166HmyRrhjgloBmaGVa8Hl6CJM.2KPx4kP.Mlu62gadqHPVKK.ki3jTYln19lAthVFsfHqnRBr3FJLOjRhleOZlTrx8vvA131V0B05bWz4RMD7A1.OWthEO4tCCwvbvKmNEMyI.guutEeKEMqaqrLEPR62By6sV6PhAszB6dum0BVvi1axBMSRxJCWB3G.XuSQ",
    "XSRF-TOKEN": "eyJpdiI6ImNJTHkxajEvMmc5c2xyMWViWXhOU0E9PSIsInZhbHVlIjoiWmhGZ1VvNUZrVXVTMWUxd3pXOWozc3lmcjBTUURwU2RSdGFiNE44bDlpZzA5YWg2WHhQZDh0U3haeDdEWkJsZmExUDdpZEdGemhVcG93cXJidU1wdld3RVlSdUZHa1ZlbjlnSFVONVdwMHlFYnVzNnR2YlJMZkQzcGllQTVMZmsiLCJtYWMiOiJlNDY4MmU4OGU2ZDg1Y2NlMTQ2YTQ0ZWMwNTU3ZjFlZGNhZmQ2OTE5MzA1Yzk2Mjg0NjczMzNhNjRiNjg1OGU5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InEydGdyQWVrSjVZd1RtL1p0U2ZlU2c9PSIsInZhbHVlIjoib1ZLY3N4RW5Zb1J4TDdGSVFoeXJ3ay9MMjhvZ3YzMW9MSitleC9sTzJRbEUwWEltaWNuQlRYZ0JUMUZCcC84SlE3SHJVdXROYU5vUlI4T055VG8rMjlRWVpDeStUUllYRGFhWk4vSHBHOHVsM1FlRitza0pkbDdabHQvWUFvd1giLCJtYWMiOiI2MGQwNjhhMzc2MTRiYjczNTMyODhhZmNkZTA5ZTc2YTk5YjAwOTg0MzA0ZmMyZTQwOGZlMjM4NzFhYTcyY2Y0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "VDOZA1gre5H3VnHywARhPcMPKHKMvE4inGIZSiqR6L4-1791934885-1.2.1.1-KIZtYnFswqxepitmYm0mgaHaSc8QY8UV.MQGcvvv1i_dV9huDPUb.U6TS0TQusrmg41Zb4DnAjNyVErQOe7lECCA3WVz3pn_pWRsPs8_2bCGbZ1lJir.Ge4FHmqxrYKUMs5wSSVJKF8ZspS6KGGGoYvR8LQqRcJU1DO1Lgueh_syYSG6bTNYYlvWqE.Bk_WaBmqnhIFvmRCosGOeEs4K8AAWjTZ9qYeqIbPTUxcs4HJHvlbmxQEer.z2PpjpiWvBYpJICSh7h6iDCkgXORhq.lBQrbK_LlVmFpqKXcAPgGjh17IOKI5RpCamS0zEhL1usvz_jQqGNQKULn8I1GE53v0T_yYXp9fqymR5j4YnlglhImwZ79HCdOE4N6tVJ7p9y1mB5XW1CrThjT613DR7d0MyCAfoPX6jWK.Vu0z2PonD.6hYBNGaLakok.dOTV.fJTWAAAWRlJ4oaMzOjy9LqAHbBJNY4ShfWPcDDMSTBhh4Cai7HeE6prO7XdMUU3Ra5gU.zM9Z0FpFtlW4J_be_A",
    "XSRF-TOKEN": "eyJpdiI6ImNMSHhIZENmL1RIeStYVVZNY0czblE9PSIsInZhbHVlIjoiZjRGbHZBUnEwTEtZdngwRmxTcHE2aktNdVdvaHJKWnpqREI4Ukw4eDVEaWhuNnFYenRMQU9xSTZaN3VIK1A4d2kxRXRuSnZHN1Mxam8zcy9KN25rY2FnUmprQ0lTL1c2cmVHVnBoc094VS9pdXFzVnFiOGRiZUFiU09ueUNiWjgiLCJtYWMiOiI2NmRkYmQ1OWVmNzQ2YzllMDgzMWI5MDUzOGJiYTQyNWNiN2VmN2IxMDdlNmYzNTJjMDM5YmFlZjkzNjJjNDkxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlArTG9ualhLdXBJZ095U3l1ZDZwNnc9PSIsInZhbHVlIjoiaHNMcEFPeU41emFUTjFTZVQxcFVPTDdxNU1BVjBpVGhZNlBtdVhvL1hYUUt5S0kvVjg3Zmdzamo3MWJVa3JBK2VIVTRLNkVQWCtzVkY0SURXWDgzZzNKcHN4RWpnRzU5YWlzOVVlOXFseWhvQ2VlcUd1dkp3SzBsNEhGcVZJSWYiLCJtYWMiOiJkNzc0ZjdlZGUxN2JmYTU4NjJjNWQ1NzlhOWE3MmIyNjkwOTMzY2U4ZmQ1YjhkMzAwZDliMmNhNjY3Mzg1ZDVmIiwidGFnIjoiIn0%3D",
}

