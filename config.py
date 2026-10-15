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
    "cf_clearance": "yXKDHv7iynixpu9BG_futkQmew8sNfkMKNXJMDXYUis-1792076375-1.2.1.1-JccJf9BynNQ6NYfZ_1FKmgwAkXohZYX9zEL000AO3aEAhWO_sv5HpWOia300Q5agoRXcFipP5r0p1e4MMMIpYRd3lH.3JRHzsJCd.6QFemaWN17u6QkE8udoJILvZoad3BkIi3ieRf2oHLO_gdjWvqHRY.ij.Crfq6SJS.OWkSzTIeoPbdPzKZx7XdEHY3x3MdyJffgMW4HoIW2YNOJogiH4htfn4Ol_SRq4orrWiqd.guqnEWO0aBlfKTWpoK4fTmrbPswado7WbSaGDjPQdTcut9C0kH.GbYPqWLD0vZfLvB8QkFxQ7LUkQ38DGcq.ci9IQDeupTEtzEa58s1g7rb0wclawPfIWI_E2Io.0IQnEpyCsdPelvXwnLKm3Z.3PjkFh.JpifvGElsNfFnEvTVrNWypxKQeaYMVxEFKb05G1CJgGIdFwSS_vYps7pf_rcTzGoGD7KdkfkAfqm2Ps5dNZjv2g73jSYV5TXHEnVaMkZRcDJbuOJO3t9SHgDlufdv_k1iYoRngmAIPxM9g2w",
    "XSRF-TOKEN": "eyJpdiI6InhYM0JTOW1UYTNsY0NGZ0dLUW5OTFE9PSIsInZhbHVlIjoidUN4eE52bDVQc004akhTSEgzbE9UMUN5MmJYVWkzRzB5dnFOWTB5M2dVZlFkQUR0aDFpeXFrNTlITkNzVTVYa0x4UXlaKzlqVUIwQThMb2lEcmxkajdpVWg1all0SGVmQ215ODVGUGw5OGJUWXRZcmcwUG9vY0tOMWJHRUNMMGoiLCJtYWMiOiIyMGUyMWUxZTdkMDg2YzFkOTc2NTI1MTRhNTNmN2RhZTdmMjFlNDBhYzM1MTkwZWY1NGZmZWFkYzA4MDNmOTFkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlNYUVVoK2ZGUWg4NHRMejJBNk1yeXc9PSIsInZhbHVlIjoiKzFGbzQ3RTBNRTZLUWxnZXJHVm1aaHFORmZ6TFhjSlFySzFlZHlmVFEzaFFlcmphbUpNbmRFbHE1Q3VzRTNYK1N3c3pTVXcrd0ZIL2lsQXJQRWR5elljOXRQeU5VaGw4L29xSmIzeFZEMkpDdm5YdXdVOGd1VlFVWVZMdi91aGgiLCJtYWMiOiJlZTcxOTRkNWU4YmUyODIzNzdmMWM5ZWU1MmE1ZWQyZDE5ZmZmMmYxNDJjMmRiZmIwZTJiNmVhMTEzZjZmZDdlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4Psh0XCDRid.Uuw801JNQ6nI2NyYAmRmCZE1nsSujgw-1792076330-1.2.1.1-C4MH_JHds_bJYmbNmK3AYI6dmx_ZR6frHtpGU_Y1j8.TwxFARLRoYZdT5fegnFeFEH_iL9H7sbly5jyFCYLlPlT0GvpX8.pe2sxqyifHFmXsdI0tVzQo26Mpg93pqllabtKjBbXewUvSnwL67CtrRvC1yhdvF98vQy3WT0TVXZJ1c8OeGQhtJoZOEf.WwlyLj6F_rHeoB0M4FvXpL9wydXQzXkYJAVT5yE8CEAX2HB12u_K25uqaCrY3RzeGd0NccLNi2wN6OIey9cNwxHucTZodU82191bqYyThWiKZ0L9nueGwUulhrUiZtySgwhu5XddfUSTYFHPrWSocrEgM89tCne_EJT_UbYW1gCRBG8B9Jts6lqxwksmPFg6JZFvrer5qXk4u.7vZGuG3CdG5sVT2i6lAKU2FpjLd7QpFz0hYfBs6QyaYNm_hCtmuinWR78jQLCZsIxq_4eG0ayldGUfPGj6SzNysewttxiDGthRLDbaCxDZy.oTCgjxEn6qYnArZOdgj9w24h6l3oYS6iA",
    "XSRF-TOKEN": "eyJpdiI6ImhEeHJoRWhtMkRvbU1qeDl3R24yV3c9PSIsInZhbHVlIjoiY1lIVmhnd3czdDM0MzJmeldxTUlSb00zcjNua09IMXVTNEM1Q2krQ2ZBWkdDYWhPVEtFUDJJWUNSR3BWdjQzR1QrYWYyMlViRVpieDMzNEZYMFhiU0hvcHBzVzlFUmUyVURPcE5SSDl6c3pYSUxZQ01IZVhSaXlseDkzM0t5aVgiLCJtYWMiOiIyOTkzOGE1OWU4NzcwNWVmMTgxNzAwZDU3MzA2Mzk2NjEyZDM2MTk5NDAwMDJhYmM1ZmI4NDVmOTBmZDRiYjIwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldpanZudDNPeFBCTnhRVHdPbjVnMkE9PSIsInZhbHVlIjoiMEpnWHlNcWRMRjllV1EwUkVFY28rNXk1ZFFyQXZjSHRmZXhKbXM5RWxoUnZibWVyN21LQ3Awd0sxNkdZTTk1ZElsOUUrTnpKaFl5ckt6U1VRcXllZE1reFljMTYvaU9GMzlPbWljSFFQa0pubjBQUXFqeTRhS2RQOVRLVWozYUoiLCJtYWMiOiI0ZWU3MWM3ZDJhMWVlNWNjYWZmZDg2ODhjN2IyNGFhNjUzYTgxOTA0NWJhYWQyM2ExOWQ1MTA4ZDEwMmY3NmQwIiwidGFnIjoiIn0%3D",
}

