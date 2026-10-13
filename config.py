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
    "cf_clearance": "nCoekUf8A9AVV9kkHycdX.qb_vpDVClOwHtaBuq.E_c-1791927650-1.2.1.1-fMQ5h2C12zzk4YX3ilcaSevvXNjnBzmoKxmM4eYD5DMXhkzTdz2XNLKy6f4_lyOq.ejNXnjxKxPwKsyN7PyBT8b2B3RSgMKsYPCSQHjj84RZWHKwWdc83rehXZIjJhuaEfZF74gTubVh0k66NjrkqvHdSxWbng.acO1sJDjwn5E6wQEHv0Pn1EHP5El7GnOLCeRo2BbhQmO6fYBaQYn5rqv.T4ag3slejD5iYeXXm14irEqHn8Rr0UyLkGmexI1j44y9.7J2LRhwZLGuMEIPdsuXEIlB2XTgTKdwDpK3ItBwoGo.uAxeOXSWkbXvYZD1l4Zru5tWxhhxAJ8GxQ.eYMRYsNs4dgCAJRe7zkX0b6iiD_bCMKrwXn.xntc.oVb0UouQT1aCVv0AE6wLESLvVWDItHxEbO4FQ4r1MBKt9BlU.lrA9NrV9Hf6QFGUYgqIuLsTBFdYhtXr8iD76wT4DUgAt_otLAInBVGfQ3ZnOycAVYg9CCH1_W4oUW_XgZwoC6g2OK529gIKNJE0oYMkiw",
    "XSRF-TOKEN": "eyJpdiI6ImZoKzduejQxU3U2RVF6NkF3UHpNN2c9PSIsInZhbHVlIjoiV1dOZ2hXcWFYZHVmNnRqVDRHaG9YSkwyQ1FHZzZnYktGWkZtN3RVdmxtOUZjN2NkVXQvcjVGazFnaXZkckhYdWM4VjZHT2JJcVlNeFlPa0NrRlR1T2NaV3hLdzFzV2xJTjlFM0dDZDBPK3M5UFB1T3dIelptT0J4WmVGamF3b1UiLCJtYWMiOiJjN2ZmMWU2YjZjM2MzNTNkNmEzYjYyNTg2ZWFjZGZlNzVjOGI1MTBhMGYzMmQxZTQ5MDQ5Y2JlNTMyOTExZWJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IitrOXZEYWpSK2t6ZnJEWHlwaTRDRVE9PSIsInZhbHVlIjoiYUpaa0Q0VmdFL2ZpMjhIeG4wOXNRWU1SYSt2czI2aTR3RTcraURWcFZCREo4cTFoZ0c0d3kwdDlLdW5PSENUaStEdERmYWxkcWpWZ1VpOVhWT1VYYWE2ZmR3RXpIYUFOYUNTb0lpUDFlUmp1NjQrVDBYMzdTRDJmemlLYVZacnUiLCJtYWMiOiIwMmNkY2YwMGM3MTFmNTI0NDVkMDdhNmY5MGQ4ZTNkMWUwOWQ5ZTNlOTg1NmY4ZWQ4YWMxZTY5NDlkOWM5OTQzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "5DvdGkZ9_1Wcl13CN_hs7dZgdnwF9nyMTclmLkTk2hw-1791925851-1.2.1.1-uZKk2tcFx4wF9w.f6KmGgk1bdf_YGDG.KdFDrEELJzHXow2bpo.dUWV4RRaSuakKXiVcih1KyS6rvfAMpkFZdBLn0Rruom2GboL5x3RSrmMluS1gSLbCo.qFlos2dm4mttujhhSe84jaQvdxlSeEs5zd.Uf8xwQU9I0iA99UuFqJWgkfzxJlwu4oZLGdhxfSw.coRCdKrq5N466vGoYC4rqfuhynr5afHr5GKVKz6PHs8dWmnTejBfjV1VXmAdRjvNmcyZB_LtOCs8Z0O75heArhZ9hgXRFBgrqJFY69eY6pHBnsDmpGgaPYioKEJxzqhCm4lUq_arb8PeHgqOcRb8_R1QEh36NJba0Lo1Jg_2lIYUFfHNvgUukRLkbk.u7zujeRwUtVxE6rFPXs4Pu6zqihXPbeE03_HDg_cGSkaB_s75nRSd4ksuGO8ppfSy_EI1djyVoihAzINbLjhI01eoCwJDjzre2Bu4x3eFqbnnhRZzGxov2lbNdYSAAF8erNpzK5QUWwyahBxkFrS3vOIA",
    "XSRF-TOKEN": "eyJpdiI6IlFUVGxORG9QV0ZiOTdaak1Cdnk3bHc9PSIsInZhbHVlIjoiVnB4Rmo0OGh3ZnJ1VDBjS1RDQzd5SEgvYWU4TjFTZDJaaGNsa0M2M3NFV1JmS1Z4T2ZIdkN1dmRzOUVhV2REZTBHemRkYjI1RlRsRzVZT0ViajExZDYrcUs0UHJBQ1haRnowTGZKcXRPOE1SYzBPcDFieG9KdlcvcHdUVng3cTMiLCJtYWMiOiI3YThlNGQzYmYwMThkNDg1ZmIyNmY0OGVmZGQxMWI5YWRjZmIyYWZmN2M1ZDlhZDQyN2I4ZDZkMGIxOWM5ZjhmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdCYmJienJidy93TWM4ODU3S2NOWnc9PSIsInZhbHVlIjoieWVSUDhkcnFvOC9Ed0JMNW10bW1QWUdVOWYvYTB4dXRIdkVJeW8xMzRnZ0Z3VkRPMkFRc0pWb2UzTFlmZ0FMeklGamN5MjVYNTdsMUYzYUIyeXpUKytEYUdkdjNTTTZIdkp1R3o3cUFnSVNVN21XcWtJdTB6NHJZbkdxY3F4bTkiLCJtYWMiOiI3NmE0OGU2YmFhMGE4MWQ3NzNlZjg0Y2U4OTJjZDhjMTk3ZTQ2YzJkNTg0YjViYzM3YzhkNTYwODkzZjk5ZTZkIiwidGFnIjoiIn0%3D",
}

