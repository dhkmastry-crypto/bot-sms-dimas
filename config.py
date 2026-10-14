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
    "cf_clearance": "hEPveNB5ijXLWqB_xs57w9wUYbiWtJZUL5.p0B5k7.U-1791936712-1.2.1.1-K2rxsrBdSkpsaxZgzT3xy_ru3Ec9D10WwhFAGAaB8_bdPpq7_Vkmg1Wz7ovI8lgLGmYUL65qJLYK3sR2lgWIWtcA.icPJV83e_VlDgLI8dWgPw6dVSNkg.IYya2CngnaD4PMzFV0huj_oAukT16Bl42K_7UF9Sjukr28RcAG9Vl0vRIw0cuECF_90DKSjAsSXCNHSKz3SbxnbxUgB5QIPhw3TuTyQT.TS3rxwQmz5ZN3nRhHpL4oKt0xEf43AJkDw0vkfYUVvvB9UvMLcxez2PnNchbA7NsxH4b8nnB4Lh5HQ6SGkcCpF2ckgXA.sFcIBHOD54LA4sqLFOf2ziUtaRkJrotGNoD1U5aopqtLX2IRJmPlIX9jRsSIN1VHHrqxKWZnct9s62v4vOQjtHcj7c1HMa58WESIs8K_ZZb4pK92NDpcY3bo5ghEjuEe4ALgi6iyqPKFQfEnPjVl9VCCv7CWF5ZMKhhyOSMOHUC14qgdbils4RsUMs3DIlJq4e.ltPtyRfHxFWDRXDtrY7JPOQ",
    "XSRF-TOKEN": "eyJpdiI6InUremZJZ3d3Zldpckg4QVFmRFAvRFE9PSIsInZhbHVlIjoiaHp4TTFVR20wbVQ3NnY5NGlvcTgrVUJ4VmhWMlNoK3lFeXJ0ZzRoS1pZaUVWTllQb1FaTmlKTlI2UVEwTE52cGFBNnF6b1hEUWF4RTVzWm9sQWJuc3VKbXovNXZhTGE2bHh6WURLVm5nMGRZNzFaaGtMNFNHT3hWME9HWFdpbnYiLCJtYWMiOiJiZWE1ODQ2ZGFjOGQ1OTZlMjJlNjllYzhmZTZmMzRjZTMxZWZhYjE5OWI5NGNkMjZjZjJjYTM2YzAwNWY4MTUzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InNEWHQxTmk2ZHVSVTd4NThaZ3lvcnc9PSIsInZhbHVlIjoiMWJPQ3hIaTRPcnduU0Q0aVFqNngzMlFIUkpQZUFGOERMdVNIbWpUV010cytpanlieDlaL1VWRjQ1c0FTQlRSVHhrc0VWRVJSSHI1Nk5HVzVvNmU5bStndGEzUzdnRXN3dkMrbmRwSWpvYmRyUVM0ek9RNEVlK1hyS1gwSnN5a1AiLCJtYWMiOiI5Yzc0ZTlkNzYwZDJlZTlhNTRlMGI0MTU2MmI5MzdkMzU4ZjM3MDhmODkyOWRmNmZiOTBjYTI4MDNlYzZlMzQzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "pfqeztMivE9hIHgpymi67k_7fZezSWrl6kqEUEPRC2k-1791936696-1.2.1.1-vtYLEU7Qkt.a3UEZa.8nJfa0Rs1GojE2E6vYR9pmzdrA5FVzGEOSCYyaLfRJcypaPzyawsf7wrXOXh35EQhAFmTZNuY6ujmvmqQKcBtMd8MThagDfO_AAI0xcSSYcb2EFtf3HCX5iojw_tgIhtvhTl3XcFQBJp3vEzn89EBpbBDIxbxryVJYhefrtgTxmJ5QL55AVNOEnIdl78JkoUjLZtarWbcX_pgdocihFkxsPxKcGagh.iTIzvK4In7ZZPqt8WDcyZEJY3.PtUetGHkFn1miCSK0vKYhn.rJt9ZMCIKxmPxuHAFUEPMOqNp3Ck1W4MF4SxKRBkUmLfPN6sbEQ1Barl5Kacx0utynPhQa0N6oQbZvdXqzr6mihEZf1NTW2XjPLTlRikBZspdX1Dib_tClpD1NED4MNe.vOis9g0QyLpk_FndmC.o9.Ff.taePMnqMXVNl3axs_Iwu895vy2EqeEHyhesqfx23GlN12US_jlnxckmACkBxmqckLbNxYRdIPfY7ZNcMkDjLpKo5Zg",
    "XSRF-TOKEN": "eyJpdiI6IjBQNnVFSzFHOGxYWEY2RGJQOUJiR0E9PSIsInZhbHVlIjoialdXSnBnZFhjVW94M2pmd2dZMWJndHdTQkQyRE5YOXNDVGdvNW4vTWhJY1d6Lys1MUc4UG1OL0dnOFl6alNYcStMRjBuZCsrblY2aHNTQzQzZHhtZDRiT0MxeHNYdWxRckhhUSs5VEJxT3RFRWtnSG1hUGpvT3dOUWRGNCtRTmEiLCJtYWMiOiJlZWI3ZDFiODdkOTc2NzdkZWFmNDUxNjkyYWM2YzU5NDk5NjA4YmY0NGZiMjJiMjExOGE5ZDRmMDM1ZTZhY2NjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imt0Tk8wb3VEZVdCQWpDYUR0RUdRc2c9PSIsInZhbHVlIjoiVHZzbFJsb0lNcXhwR0MxekZkYURkU2VrbTlMak54YkZoV3JtWWRqdWdjandtMWRwL3NrMEdYbEcrclo2QkN3YWxjNG54M3I1aGlnWXdvVTJZM3ovVFpCRitYYnlxcFd1eU03Z1hMWlpueGNDOUY2aVJBQ2hsOU13eGpDSjJXay8iLCJtYWMiOiI5MGUxYzg2OTQ1ZjhkOGQ4OTQ4YmQwMjZiOGUyMjU4YTgzZGQ2YzcxYTY2YmY3ZGJmMjc1NmRmMTMwYTdiYjU3IiwidGFnIjoiIn0%3D",
}

