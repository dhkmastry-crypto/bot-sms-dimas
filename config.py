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
    "cf_clearance": "OJlUqOBxy1BxvL2oVvP8XervcM3Gw72z9KHc2uB.bRM-1792013815-1.2.1.1-eldBd0ZF0PdvqeH7Q3MMg1XrdBDlE_GCi__oeQlIeQNi.eNiUP1SukY1zKS5eCQiP6aS3I_VaBQO_Hb31qlJd7m2vzxmMng6CQtoG5tcO8E7JggaiMnK2riqBMAYu8cSWO.7OyUPIYePrfQFygrDBsf.n1EL3iPmRIXapFWKfGtnEMwCKSCjrw510SJXzPLk.HHevvMC..3t61e5JZiQVNzIEY66tjEtLrScJlv1xXcz78t6xt.ZiU6jLNslmys6EsSmlUBEpRBHsRFlmQWEhYsP6I2pa0N1gQNp5Bqh3Cx3.FD3uLOGA3pRVobSgYS7mHbECnsyLRf3hoB1y5GFU7PUmPHuizu9cliqUUtXOASlhFxv4mdYIeFWD42YryuaBsKu4Vjd8GIy8vQ7E39._GmDywo7KWRK3Rl13WnjU_0.nFnw6kapOhHs4cM1TIeY3Ifk4t0FoqYwEfi21SHjctAJc0GDRoMHNpXK29p468XV9zE2gKoejAR9bZlFgbe4B0ETS_kZYjQY4l041rFGfQ",
    "XSRF-TOKEN": "eyJpdiI6IlhJYVM2TEJhblhVeS9QR2d3a2FGVmc9PSIsInZhbHVlIjoiR3dtWHIwV2hGdVhaZXJIdTU1T2NSMzE2UU5CbU1jeFhEcVpFS2JEb3JkaHZsWjJ3TU5HcHVQb1FHUEQxMW9hT1JRZkhOSDVWUFFGRGRXVUlyOXdMRWw5aDBmWG9nUENaTFVOVDlWRTBaTy9CZkJoNTFjV2NXclk5YjdiNE5mSDciLCJtYWMiOiI1MzY0MzBiN2NkNDJhNDYwNGZjYzU1ZGZmOGM3NWIxNmY0MGNiZWUwOGJlZWFiZDkzYzdmNTE1YWQ0YTMzZmQwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlMxSUNvRUZOOHprWWZMT3FwOHBNdHc9PSIsInZhbHVlIjoiNFNGWmtYYTQ3dFJSb05Wa3hSV0FhVmZtMVUzTld4UHQ0am9wSkx6Y2ZHamZ0cXdzemxvWTQ1R1kwakJPY1JNTEFjb0QyWmV6U2dadEJ2YWpHems1TFVyQ1NXK0NBSFZPQk9aekV3eVBDeUVPWjhVOTJacEFObTQ0cENuMGZRNzIiLCJtYWMiOiJmOWQ3YmFhMTk5MDYzYmUwYTczYjY3ODZhYjA3MzVhNzViODYxOGE2NzU3MDgzOTNlZDhkMzJhMTQyNTRlNjMwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Md1CqTvLukGjkJCfauAIZdlYBPjb6KMZ2TaFNtW9R08-1792013793-1.2.1.1-IGQbnzduO4U.e32v9cTJqBJln2esrDAq0DA3581SvuriGN58safMZo9jz2p76dLByVTv0tCflVDjnvMHh89ys_bw4O7nRzxPXvQ4AC.LbnN31UkjyJrIci_WmUVszq6tQHFlN2KayiPLifoSo27Go4dOIUwo.i0ZTI5mBAwom8MgKlyFTLLhbNm_ZFKrPP0.R28GYhBSz.pZgH4ARlnAWrqhgqB0DseWCCV3fBQRHZ02h5McJp_ZqhD8ScNezHdHluvs12y0XBCOvF39qFdAL80OHuYhgXzYxex.LK61MjMQxqZeSX3NoW1XKSOm7VwnTca47ney_CxouXIrnm7B6YeuZGoURzmhmfUp5pzwVVxuBJf2mHTe9Bo_ViF.El61Ucut.VfaU44hb0rzX.rSL8_.MRlPGAS1BxQI9GXZgo8uWsiWaSIcDEmSRruGs8.xw.I6Gh1sa.tvmwDeFLIdtsaW8O1dMd0WgAQkSWpmQlV2PjK4lkae64KrzPj2eRAD0BvRP5CuD.vMbFsUlBmT6A",
    "XSRF-TOKEN": "eyJpdiI6InZBUGJoZ0ppdnpVUWVZdnNMQ3hlUXc9PSIsInZhbHVlIjoiRllmMGVJK3VNYVJSckFuVzNibkdxMndvYndQamJXd21DdGh0dFpQelU4d0xCT3ZGWHdlUUhKMzRLWmNDWm5BNmViVDFYem5xNnRwN0lsWHVtRWxMck96aTgvUHNKUjYxRDlPSWJsTC81bytYZk5oY04yMTN5NG1KVTMrR2JjSGEiLCJtYWMiOiJiNmMyN2Q0ODA0MDIyNTFkNTA3MGJiM2QyN2YyMTAzN2QyZTAyOGE4ZDEyMTBjMWE0OWJkOWE2ZGQ3MTk2MjM1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImNLaGdjME5aOXRyWUpFandEZkhmcGc9PSIsInZhbHVlIjoiMktHN2tHVkFtdi80eFBxZHE4OGVWcUV6SjljSEVhck9jOU1uMDV4YmoxZTA4RVdVQ1NaaWhaeVIwOEtvVG9TYnVSSS93ZDhwWW01d0g4Qy9KYmNVR2duSTd3ZFJsb1VQTzUvUVJGZERJL1A4amFiVnBpQ1NRTHNwbThFNXRHVXIiLCJtYWMiOiIyNjQ2MWZjYWZmODE1ZmU3MjI1MTE4NTM1NjUyNWI0YjA4MjhhNmRhOWY0YmRlNDE3NGM3Mzc2MjkwNDNmNWVjIiwidGFnIjoiIn0%3D",
}

