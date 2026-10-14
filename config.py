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
    "cf_clearance": "t1jJGB5CAbDwWotf1_P2gXMbIzn4aD2elylBYq3BXsM-1791971184-1.2.1.1-LubuKqIZUxjcZkb_oytaphr4v8YobVgpd3Gcb2vhMt8elkmaO4E4dL0MQ_2hNi3XUKegCI0WrDT58Ivmj7H1XjNxnIj2DTcnfXppgSkoIFPBV6Q0yVg8iQesGf4vhukHyd4.f8WO9scuz36bDYFJRQ0DJuGOTQQ_DecsEFCbYwGbVCjmS1yiiJKxqoDkMSWTD7AVMD.IH5gRXvR7AKxaheH41yO9RnUfgH0xME8HJt9l6JNUOIZL1d3G3gsPdPelSUk_OXR16LtShnjA5E4pYqSghEI5i3ZfaKRBvr0Enf8Z7NtMtxtUvG7Pg_LGrQckKuuziZPJD3l7d_cReu3syDhfhgUzo1_7F7I_1GbzW0lbJriQh.qqN5zKeunipkcd2N7L8qGrLtv7JGCA6geIE6gl6gMm22SxQSIx9OpsjItMo2wkDGFEGsJkZe4mLEIxTSRpqteiAQGASVv2iHw2gyeG4XoND5g9s2p3YntSnnTRjq9qzSGsCcnAr58qW_IltseAoYxWMwqJLZ9XauLVug",
    "XSRF-TOKEN": "eyJpdiI6IlZVSlFqMGtBUWxxeEdjQ0JuaVkxUVE9PSIsInZhbHVlIjoicW9sbm1aYmczRnhNcUs2OUIzSkFTcitwUndqVndReXZYaU5oNUVmR1pwa3hwQ0swN2M0UWJOMkxBOEhSaU4zN1BtejA0QTRDS0xDVEFVSENzdUx2eFhNNXMyejI5Sk1zMy9mcVZWUUJZcHQwS3BnUHRPYmZMNEhHYmxuQ2VXR3YiLCJtYWMiOiIxMzJjMmY3NzBjZjU5MzU5NTFkYzAyN2Q5ZWUyYjNkOGNhZmRhMmVkZmNiZmYwZDJjZTc1NGY0ZWI0MDFlMDliIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IngrQVp6VWFQQ2Z4WEtvYWZrcGJUMlE9PSIsInZhbHVlIjoidDA5ZWhmM3NEVS8zRVJOQmw5bmsxYzRma1dXaGFxNWl1aFlXcGhvaTBRNjh2NzNoMzVLa3RmMHVDRlA4N05PU0dwZVpXKzB2VVJ5N3lDdGdvY3h4M3VMOHNKVmp4MjZlOFRMVVp5dFYzbmt3cUIyWkg1Z2orUHVxaHluNVdMbDYiLCJtYWMiOiI0YWU5MGQ4M2Y2N2E5MGVlZjJiYTg4NTI2MDQ1NDg1ZGQzMzlhMmJlNjQzYWQwMzUyYjhmY2YyODk3MDc0MjdiIiwidGFnIjoiIn0%3D",
}

