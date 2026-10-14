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
    "cf_clearance": "tzsB4G7Rg5k_Jt5xC.pw6ZWQ85Xf2P2HWoOqQR2goYk-1791972899-1.2.1.1-CRC6Wf_XcLMAWEH7quZYD8AqT77hEi7XaDwjPYlOzl3e.3O.xxdjEDypCqNmhecIS9u8JY62Tey4efGTOIcUcE.8XrWfwKDXpC2geKtPHE00ypwRSAECsbRCqviQHRjLjX.tnLWzs4xdrBVGOj3xDPsQtUvT9yAFdd.bz4FRjd.Ly2gBgIPx0.Hjr0v6YNXeEpdM_ebe.wtMbgx7kUydu_S5zTPdfaNc5sVzJaT3YxJG2f3R2VhNkamYyw05oFE60zXNSCIgQW339rs.sx8lRmGUrkLolryYtQRuDe6dlhw9bUbsTD90DA4r6RJTzCp6RBbkmUPuuqUmhWkdqXgKicfXDsmDsdp7qS9FLckxlAtwkz9Im9hlI.bXmdoYhzM1TbAgg0AB8.nePvnrzVXCD5q8bqoZPBGsEDckCOS.smSlXRYOYFRbc586ICylqk1g4nxsNelzR1N3f27LjTACnH.pmt7l6nb09SHQaf7W1OSinLfzUM9Zkh1dZ2AKUpaXYBKNdIsv24Vf1EEqbFExjg",
    "XSRF-TOKEN": "eyJpdiI6IjhTaUdUbDBSczA4Mys3c25kU3N6Wnc9PSIsInZhbHVlIjoiRXNISnR1RUp1RC84WTR6Y3JFaXRmT3ZoMThZMEZoUnI0U3lzbWlQeW1QYTdtUHFHcWd0M3R6bU9SVUpscGMxUmdLckNVRVdmd0VValdCNmVvTUdpWDBnNzZrOHdqcTNXQzhvd1hwV0FrcFhMRmdvMzI5ZjJTenQ2RWJZOWd0REgiLCJtYWMiOiI5M2Y4Y2JjMTdiMzIxZTMwMzhjZTBiMjJhY2RlZTg5ZmM5YWVhMjBmMjU1ZGMyOGFiYzhkZmY0ODQyYTEwMTIzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IktLbVlCYU90SjY3K0UwZ2JMTk5heGc9PSIsInZhbHVlIjoiZkhQRUZZdHZyQTQ5RFlHdGVFa2xqV3NBeUlmY21XWnFwWDNBa1ExYUdqWHVhSXNvQjJkZHpDMnJwcmlHeUlDckZwRDk3S3poTGNuMFRHMG5BN1YwTjUrOS9wc1VjRlVHRzdLTnZMWS9FcmVNeEFsRDQ3QXJ2MTZ6aS9IVy9Iby8iLCJtYWMiOiJlMjZmZDI4Njk5OTIxZmU0N2YxMThjMjg5NTQ3YjNlYjc2OTY5MzUyMTIxNjMyODY4NDJkOTdmMzI1ZDM0ODBlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ekK5BkXuOLmzoWNen52JRYF9twZtB9uKefGKVBEfN1Y-1791972997-1.2.1.1-APMBjlgScQ53c7SiPIRMGegJ_zuYFxFcYZrxnj0nl.sIk_pWU6m8.eAR2ZO4OT29VrJAY5roEWv3BhLDaGsAMpNDTP07f97Xvu.XMBRG06ev_5puj8B1H_ZpLgQzFMe1GOm9y5Ve2gQw9RW9qswrXKZfVu0UUu4eUWo5lOaQ8o_1oBBFcJVgY57MmZTNLGnPuHQ1B3NL0N.K5TIcRsmazIB3qDDSDJZuwne._n.oFzmdblUTdAVa0VooovoR3WpboUDBbQatxbaTBFJB30OywaFwi2ZvZwpZfNk8_2ivEnlaqfaUJ_nM7VRTdBKe9fl_c3zQtBxh8npAR6RJILQFvMoZuitcsa9pGS_FH7UAKXeNFuImTIoOzJsBTxNomlD_UxnGGDQaJN.f4hKjDdoVV9klnd.HnJLGFJH3o_P20XGixvc_EJhb1K8y0WW2kQOuQdDQ7eTg7IOaHTlbTN3r4LwV7RoKSRJlLkMxcrEHxKUhyViXzz0F0Lqqn9Io0obFsoeJkGZLF3F_9nUdoBdCsg",
    "XSRF-TOKEN": "eyJpdiI6IlhhKzdyMU5iTmMvRVA5dXpmc0VQOWc9PSIsInZhbHVlIjoidmZ6OHg0cWNHR1VybE9BSXhvNHJkeGtpMDJLSTlzTTVobGxsclhTRUhNSmc3WkhVenhjd2lLSCthcGZqN25hNlVvcmdiZGpBZFM2NDlKbE8xZmdmVEplNEdkSC9RY09nWkJjNXdVNDZ2QUZlWTNRUkhNKytFWFFLWEszc3VxT2YiLCJtYWMiOiI5ZTQ5YTg3N2U1YmNjYWRlNjdkODI5MTdmYWI2ZDhkYTM5YmQ2OGZlNTg3NThmZjg5MWQ5ZTJiZjhlNmZiYTk5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImVienZCbENaUW9ieWdDSmZtemxKRnc9PSIsInZhbHVlIjoiUEh2bEFPQ1llV1lEbTFBSlM1bmw5WjY0b3RGTHBwamlhOU96dnZtNzZJVmF3ZEhmTTdqUkVMbW8vTU5qVU9SVldaaWU1bVA0MEY0cjUxWnJ4MFJFTDB4b01LZWlHeHdwVXppUldjR3pzK2RNVkVvOXliNTVIYnJmTDVxTjN1Z24iLCJtYWMiOiJkYTk1ZmUyNTUxYzA0MzY1MmNiZDk2ZDAzMmI2ZDQyNWM0MDFiMDc3YTFhYWNjNzRiZjYxZjhlOTMzOGRjNjNkIiwidGFnIjoiIn0%3D",
}

