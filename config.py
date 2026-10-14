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
    "cf_clearance": "zSAxcDk_YvsNsxcfkCdMzt1yxlUjMawJTtKF92ejKFg-1791974703-1.2.1.1-Dd7KrdxirL8.6p_EatQv_R9WxG12JWG7QCjAVrdPOwVJZuOgl9wEIbZiz.DUYHoVyULs6hm4hQpkx9mWELJ6A2oOIrbWvETMK.J.R_0U4a_zwn8FndJW3cZ1QZEDz5ONXV4NeJ2K8XrNuEuzFuSPuL7pF9cT6_A8KRiigprw4QbjzygdAtH0vQGjs_clB8j8oKtgUWfDNsmh128IDPJ.sPk_D0vUfXE5ABemlRaTKg.4Ll4JLNGbfJy9y8SxlGwRzg3BhL232qtO4fsxCbfdfabQ7k0qhVSUoap6SGYRZkuZUeZPRKYy6pahKZRFShJmbn4VUaXmhbnEirq5vYXmX1W2IP1foncLAHiMQXbsXIACbJQvx2qWVXRvrVSBjHOiJTxKKKG6fKUJEg8ZdMcrBvY2S7ErbVaKrWljpJNFD0Lv1rpZqBNFHRKTvbzqd._hi2X5hUCkupucnUNsqZDp7YjWo8tO6obFR5Q5UMO8UQdeGsXoApW4cmT2bwx5o5qvs8n1HY0QzM.fGpltlBJONA",
    "XSRF-TOKEN": "eyJpdiI6ImlBR0ltZitUdVNtUjFFUjd4dUhtZnc9PSIsInZhbHVlIjoiOHk1VjJQUTJ4RWNLWUUxVVJRS1hLQWdhUEJBZStHZ1gyVUNkeFkwUzhnbDZLN2lTNTJLNlBDdE9LY0loeVR0eDVYdVE0RHNYMW1PS1ViSVlvTFVzRnFtdG9qbVdyK1lyRDZ5RFI3UG5wNVZjY0hsZ3dMU1AzRFVhMVBPNjBLZFQiLCJtYWMiOiIyZDViNWI0YzJlOTY5YTM0ZDEzYTM4MGM1NWYzZjVkMDM1ODkzMzQ3MDhkYjgwZjUxNmRlZTU0ZGMzYjc0NTc5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdKcjIwdE9qbjJSTGs5aHRmVHFGaGc9PSIsInZhbHVlIjoiS1dmWGFDRDdvZEJjWUZrcS9CVGg3M291dlloRk14ZWVkT2FaQXVqMDBIa2tobVBmZThVTkNIeWNrUFFiSHZuY09uWnBWMmlkVjZZc3E2bXpKek5EeXdWSzRJL1hBMTBrZHdvekJ0bjBnZkszYkR4aWJxRGI2cHZGYjB6aHJHZzgiLCJtYWMiOiIwMTE5Y2FlODZiMjNhZDBhM2ZjYWY2ZTRiZWE2ZmVkOGU4NmIyOGM1OGMwYTAwZDkxZWJhNDBkOTRlNzE4NjBjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "ekK5BkXuOLmzoWNen52JRYF9twZtB9uKefGKVBEfN1Y-1791972997-1.2.1.1-APMBjlgScQ53c7SiPIRMGegJ_zuYFxFcYZrxnj0nl.sIk_pWU6m8.eAR2ZO4OT29VrJAY5roEWv3BhLDaGsAMpNDTP07f97Xvu.XMBRG06ev_5puj8B1H_ZpLgQzFMe1GOm9y5Ve2gQw9RW9qswrXKZfVu0UUu4eUWo5lOaQ8o_1oBBFcJVgY57MmZTNLGnPuHQ1B3NL0N.K5TIcRsmazIB3qDDSDJZuwne._n.oFzmdblUTdAVa0VooovoR3WpboUDBbQatxbaTBFJB30OywaFwi2ZvZwpZfNk8_2ivEnlaqfaUJ_nM7VRTdBKe9fl_c3zQtBxh8npAR6RJILQFvMoZuitcsa9pGS_FH7UAKXeNFuImTIoOzJsBTxNomlD_UxnGGDQaJN.f4hKjDdoVV9klnd.HnJLGFJH3o_P20XGixvc_EJhb1K8y0WW2kQOuQdDQ7eTg7IOaHTlbTN3r4LwV7RoKSRJlLkMxcrEHxKUhyViXzz0F0Lqqn9Io0obFsoeJkGZLF3F_9nUdoBdCsg",
    "XSRF-TOKEN": "eyJpdiI6IlhhKzdyMU5iTmMvRVA5dXpmc0VQOWc9PSIsInZhbHVlIjoidmZ6OHg0cWNHR1VybE9BSXhvNHJkeGtpMDJLSTlzTTVobGxsclhTRUhNSmc3WkhVenhjd2lLSCthcGZqN25hNlVvcmdiZGpBZFM2NDlKbE8xZmdmVEplNEdkSC9RY09nWkJjNXdVNDZ2QUZlWTNRUkhNKytFWFFLWEszc3VxT2YiLCJtYWMiOiI5ZTQ5YTg3N2U1YmNjYWRlNjdkODI5MTdmYWI2ZDhkYTM5YmQ2OGZlNTg3NThmZjg5MWQ5ZTJiZjhlNmZiYTk5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImVienZCbENaUW9ieWdDSmZtemxKRnc9PSIsInZhbHVlIjoiUEh2bEFPQ1llV1lEbTFBSlM1bmw5WjY0b3RGTHBwamlhOU96dnZtNzZJVmF3ZEhmTTdqUkVMbW8vTU5qVU9SVldaaWU1bVA0MEY0cjUxWnJ4MFJFTDB4b01LZWlHeHdwVXppUldjR3pzK2RNVkVvOXliNTVIYnJmTDVxTjN1Z24iLCJtYWMiOiJkYTk1ZmUyNTUxYzA0MzY1MmNiZDk2ZDAzMmI2ZDQyNWM0MDFiMDc3YTFhYWNjNzRiZjYxZjhlOTMzOGRjNjNkIiwidGFnIjoiIn0%3D",
}

