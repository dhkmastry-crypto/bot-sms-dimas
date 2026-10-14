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
    "cf_clearance": "egPQiywgpYcJwzT2YPEDKplOwQRmfRYKzHxF2dTidgY-1791974811-1.2.1.1-C1V8AenrCEsyxGU7sXyF9OT58p1BzEMl0PKB0NfqeIkXPfb1YipFHRLgzUEiXfFkj4p96Gd2yqutZdjKgkUyyjxOYBzEbB307BoiktpMkwF7Fy1hLnmucA_LXEQRHwmspwZq5aABBwICM.DdryhIb1YMS_RVOpXY3tharLXoBeVhtNGc1ZpzDLnGiffxeodlUhIhYIVnY2OH9sTvgyJXR1_GCqf2P8JxX.U_gWzNFkI25jlBqL0gwEmJ_.7jzSUD9jOOZ8ee22551oh7UJPPHMQaJ9UyQr2LKD5GLWazBSsrt7L9WfnX00ssP5dXut1oDPLRUGPlr3Abrcm97s3hZ84aCe.9Sh6U0oYfbBUm33U2Jhbkumoyr1m4zwWz2zBwPcJLstWFgcaGKgoFBWHn9Jbewh5RUdbSWMBF5.K96lGLZ_r9xd_eViQj2PyYrdoXF4MvDCgB77uzNZ9ISbEmYU05VPbhwnUELjEscQ6hS2p9TkQrEsKWNsih7GsAtkmjg3hZ61Bp.WU44HXRVkzJPg",
    "XSRF-TOKEN": "eyJpdiI6Ik45RmpGUjh5Y21JL2FhWnNla1N2Smc9PSIsInZhbHVlIjoiUEZRalVpWkV1d2hTUzdWMDNVUDUvOXdyK0c3VDc2SElXM1pHWmxjd3o1cGtRVW0wUVJNcitwYnc1RmR2cXJJQXdXNVNzR1k2YzlpcnYvMjNaSlA1U1g3QlBFSTE4M05OR1RFTjNjelFpZnRlc2FzYWZPbjFrV2RTazd5TDBoZWEiLCJtYWMiOiI2MGU0MTg3ZTFiMWFiOWE2NDcyY2ZlZWIyYmE5NzZjZDFkMjhlMzUwOTY4NjgzYmYyNzcwY2NhYmNjZjZiZDgxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjQyMXRvQlByeGkrM1UrSWJzOXI1c3c9PSIsInZhbHVlIjoiS0NBRENGOVRRUk4vbklSM2N1RjJGeExRdnNzT1N5RjRpV3k3R2pmT3ZWNU1DdXZYU3l5SHdVL3NTM0lLZGx2UHNXbVB3VlRaTnNzSGkzMXRzVWtJZ3RrbkdvaE51aGttbHBVLzExV0FIbGNQYUtMbGdNL0FKMjVOdHQwT0lWQWYiLCJtYWMiOiI2MmVhYmIxNWRkOGJkMGZlZTg3MzhkNTg5ODUwYmViNzc0OTc0MzY2MDlhNjU3MWU5MmJhMDhjOGM3ODExZjJlIiwidGFnIjoiIn0%3D",
}

