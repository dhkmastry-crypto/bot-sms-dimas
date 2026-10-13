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
    "cf_clearance": "VzUc6bcAzPVLoo8MM8Bn4APJxD73Y0pBQAaYhadiVG0-1791925840-1.2.1.1-MFc4kGpUJaW6T8cGNuFBoQc2iAv2bqo9o.bMneeWAz3bsFBBkc51CBzV82a9Kj1gHWUqMmTZgIfIUoZFN9K6qceAwCAljsNuv97CiGQ1ViSD7xhg9WAcMWjfMWhhW8fE2yioWdgH3I69XS3lRuyLAZBDbhNoJ2bmGGe5dWH0G3fzmz0Bo4u.l.mGIXK.8CHlgwTiYDm.SI4SH9Ph6UlJSkyR25ec3Spjkshyz4crzGeoVf.nBhkvdyEJulBzxIv7FAWvqDcoXyGBkwY0UVAAFkxduxUN3h7schnruCMHR32Hd3SsMANmOHf99WSqDS715QDLYC636fJqhDxvY.JSl_idzIrRl7hznDMIx0lEly_4FViJgogCSOrxJ58.PrWNMOWbMzaY_O0k5lg13pzfBELHH7SFfD4mfEEbgddMqVZuKAZIeDVzEZjqc2ZiJeS89IF2E26OgIu.ueWjR7RT6ci0b0YaVTgCIDeEtO_HzYrImdtfb2YqEToaDdz08FLm1Uid88dfByk_l49CeGgafw",
    "XSRF-TOKEN": "eyJpdiI6IjNpSXRzZFRDSTRPblJ6aTNqSzJjenc9PSIsInZhbHVlIjoiMzRpRmJ0WW9IeVh3bFlqM21VL1hTbXRPMzg2b1ZPY2s2OXhIcWw0WTFZaXJkdjI4c2x6WThwVUl4Z3lnTlJhOHNwb29hQ1NmdUswSUdueWJDdExxV1ZOVkVVdzZGREYwYkN3bDJYWmZvdDJPVm1BTTZSNlRiczNNdTVOTk80OUsiLCJtYWMiOiI3MjUyNGNmYWVkNTgxZTAyZWVjYTc1MmM4NzZhMDc5ZTEwNjA3YTkwM2YxZGU1ZWE1MTg1MmE3YTk1NGMzYjk0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlR1NDNoT3ZCcG5KTFB4ZDcxOUVCL3c9PSIsInZhbHVlIjoiRjFDL2dCSjJEVGFUcTV0WGgwU090MUMzQ0lHRlQ5djRUalFBVWhOZ1J1aW1SWVhQaitoeXBpMFdLSDI1WWhvdmdOYS9kMG1kNDFiSlVVSG83MkNzS0xVS00yeVM5VVdaV3JUZVNiRnpZclo0R2Y4Nk56UDhYd3ZXcTY4aEt2TlkiLCJtYWMiOiIyNzVlZDdiMGZiYTc3NzkyYzY1ZWQ0ZjIzNDQ3ODczZGE5ZTAzN2VlMzk4YWFkNDIxMzgzZDA4ZjNkNzkyN2I0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "5DvdGkZ9_1Wcl13CN_hs7dZgdnwF9nyMTclmLkTk2hw-1791925851-1.2.1.1-uZKk2tcFx4wF9w.f6KmGgk1bdf_YGDG.KdFDrEELJzHXow2bpo.dUWV4RRaSuakKXiVcih1KyS6rvfAMpkFZdBLn0Rruom2GboL5x3RSrmMluS1gSLbCo.qFlos2dm4mttujhhSe84jaQvdxlSeEs5zd.Uf8xwQU9I0iA99UuFqJWgkfzxJlwu4oZLGdhxfSw.coRCdKrq5N466vGoYC4rqfuhynr5afHr5GKVKz6PHs8dWmnTejBfjV1VXmAdRjvNmcyZB_LtOCs8Z0O75heArhZ9hgXRFBgrqJFY69eY6pHBnsDmpGgaPYioKEJxzqhCm4lUq_arb8PeHgqOcRb8_R1QEh36NJba0Lo1Jg_2lIYUFfHNvgUukRLkbk.u7zujeRwUtVxE6rFPXs4Pu6zqihXPbeE03_HDg_cGSkaB_s75nRSd4ksuGO8ppfSy_EI1djyVoihAzINbLjhI01eoCwJDjzre2Bu4x3eFqbnnhRZzGxov2lbNdYSAAF8erNpzK5QUWwyahBxkFrS3vOIA",
    "XSRF-TOKEN": "eyJpdiI6IlFUVGxORG9QV0ZiOTdaak1Cdnk3bHc9PSIsInZhbHVlIjoiVnB4Rmo0OGh3ZnJ1VDBjS1RDQzd5SEgvYWU4TjFTZDJaaGNsa0M2M3NFV1JmS1Z4T2ZIdkN1dmRzOUVhV2REZTBHemRkYjI1RlRsRzVZT0ViajExZDYrcUs0UHJBQ1haRnowTGZKcXRPOE1SYzBPcDFieG9KdlcvcHdUVng3cTMiLCJtYWMiOiI3YThlNGQzYmYwMThkNDg1ZmIyNmY0OGVmZGQxMWI5YWRjZmIyYWZmN2M1ZDlhZDQyN2I4ZDZkMGIxOWM5ZjhmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdCYmJienJidy93TWM4ODU3S2NOWnc9PSIsInZhbHVlIjoieWVSUDhkcnFvOC9Ed0JMNW10bW1QWUdVOWYvYTB4dXRIdkVJeW8xMzRnZ0Z3VkRPMkFRc0pWb2UzTFlmZ0FMeklGamN5MjVYNTdsMUYzYUIyeXpUKytEYUdkdjNTTTZIdkp1R3o3cUFnSVNVN21XcWtJdTB6NHJZbkdxY3F4bTkiLCJtYWMiOiI3NmE0OGU2YmFhMGE4MWQ3NzNlZjg0Y2U4OTJjZDhjMTk3ZTQ2YzJkNTg0YjViYzM3YzhkNTYwODkzZjk5ZTZkIiwidGFnIjoiIn0%3D",
}

