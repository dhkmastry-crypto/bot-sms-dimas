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
    "cf_clearance": "PPxj2rxuSXEDbbu9fBSmmHQzROqXAhjisx3l9kseJRc-1792118087-1.2.1.1-T_TVaWI7EuXoML2AKfwK_dny5WK0jq.m.waPUqlUTm0_XXwEhE3TJeAdNNVFdwZieGC9qWb.S9t63Cyz8J0Ww9uGzkc9ZBlyRKYPFuQfbHOwXLWFX9BFdKVnZfvEovGDjJTANN83ebRSCJfGC.npziAw7dKwWYqAJBgQ9KguVV1sEuhkEBog0Wt3kWKJqtGDyhPm0Zl.9p4wYCOQcVafJgmpFIfXmuSZe5hoY9xQ6vIJAwQSxNpZ9oFEMZuF6903FNeaLy0e3hpLzkoLjdTU4easipaFC4nj.c13KNBG3xsyRzQxsW6MDRqbkwIyH1wzycVLp0Ihqksayr7k2sHmVXnKDEyH_pSUBTifA2SV67dQmzIlFqBlwzdfPQnGzJZ4bWFVyEv4C2Caut0gzxeF9sajaQiBL5TC86ErOu0jn7C5fLrgCyXgcx6laGR82u1ak2dQYYX7EtoRzTDoh_XQPjqP4O2jZj4Dwe5xsal6rz9ChNrA4edW40z06jtGwqNtrHYW36XI7Cwaym5vvQio9Q",
    "XSRF-TOKEN": "eyJpdiI6Iit2dDZzVHoxV0p3OEFhSnY2WVlQamc9PSIsInZhbHVlIjoicTJWV3BPbmtrVlJQcElkWm5PVVduWVNVbmZTb2dsL2VFM1c3ZlhMTnVkQjVYUThWZ0ZaRHVXeG1xYWhSakk2WFNLZDU5S3AyS2pLcm9OMFhGOWNTN2pzdmlRaUJpK0xiQ3RCREFzcTZmT2ZQUTREZ1liZmgzMllwaDk3UnFzcnUiLCJtYWMiOiIwMDQ4YWFmMDM4ZDE2OGQ0OGE0NTViMjIxNjcxYjA2OTY0ZDk4OGRmODNmOGY1OTJjOWRmYjQ3MWYwZWQ5MjUyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImNWaTFsQ0hQellWaXZ2cSs3bS9ISUE9PSIsInZhbHVlIjoibExobG95MnFYMk9TZEd5RndtRGVQZStXK3daL0twRU0wRjA0ZnlWS2RCa0ZSUzVEdzdmV3BDZUdOV1ZBbUFSSnN4Uk9yOUQzWlIvSENQeFNNYXF2UXBFc0lKNDRwQWI2SVZoU1NnbGdsRW5EUWFvd2dNNVlyZTJxRy9oODRDa28iLCJtYWMiOiJjMDEwNDAwYmI5ZWFlZDYyZWE2YzFhMGVhMDA4ZWE1ZjgzMjQ4N2ZhMmQwNzg5NTFhNTNlZTM4MGM4ZGY2OWNjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "EWhIlnHfnTA6r5YyaKuA0MQJwronKxggUsHxbEgQAlE-1792118076-1.2.1.1-3uS8n4G_Rbc92.Y52NkK6zg7W06l1cyy5q09plFN_MsXl71clU6iJKhUDiRFqxG_peYkCw1V4Zy.lQjKdnS0F5b_Ztoi12FTVKnjXhySjnU_oBMxAT.4OFn0u6AcPgQe4tH9RIcGh96bdg3FsJVsAS2Agf6eTfdq.cWJLAF0vrXJTC57zuE56QyzWc1D4v4KFATAaYPUyylhRQEkTDmYxv_CjszS8984oPkz21Z5iu.xGbx_wmeyJaR5DHpAGf87a95txPLAU4dbungg7VlJXrdbdOmLHbHZ_WKgZ7RNQ12CbD40y6p50hvSUaRPk50X6Up9AyFK2jLJTA3u6y_EQ93ZbsoPP4er0GVX3q_x.RhU4YNFZzVMxPrSqcBtul.7fUI0Hq_7qRAZF5G6oHklYcIPT97R6d448nkm0TzhMMtx2WZiGX3473tI.B1MtuCuTD6guHjBAfmV_Aq99M5ret9P4vAJaEXmQXWCqAVNythJK.E3HZW8R0whJAB7hpIf4l8BdDYSqQnRJOb7DAQh_g",
    "XSRF-TOKEN": "eyJpdiI6IjNlWkJac1lTL0JsaDRjeVNzR0g0Mmc9PSIsInZhbHVlIjoieENBMDA4WDRzUlJtVE0wL1hjcXpISnY2cE9jOVB5d0ZrZ0tWcWxlcHh1SmJXVldwZnNocVFLU3AwVlBYR2VYUWdNcXgzSDdVRFVrZzBVcm9nZXJvVC9yb2M1bWZFaVlCRm9YTDZmdDVNR2ZFdnRyazJzTU5HdWszck80SU9RbTMiLCJtYWMiOiI3ZmUyYWRjYjZmZjQzZGZmMjhlZWQyZWFiZGJjNTA1YWY3NWQ1OGQ2ZTc3YWQ3ZWJkN2FhZGQ3NmFmM2M0MGJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9LMW1USUh4MWp2RWtRYVlHLzkyeEE9PSIsInZhbHVlIjoiOXFrQjRpbmJTOE9XRUwra3JHVzF6Vm5ENUgwbzR2di9kL2gzWWtRSmYzZGJDUlRaQWtxQkwyVWkrY090K25wU1N0YXl0TGFvbjdURXFPNkEvTG9GUDBoT1lJbnI5TDE3cm0vV1E0eWh6b1JpMllnQkxWR2VIdnNaVklWcEJTaXMiLCJtYWMiOiIxOTIxZTNiODU4ZTkyZmJmZTY4YjhhZDAxNGIwMDUzZTdmZDYyY2RiYWY5YWRlMDEzYmZjN2IzMTc3NzUwOGJiIiwidGFnIjoiIn0%3D",
}

