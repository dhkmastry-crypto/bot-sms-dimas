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
    "cf_clearance": "rWk_ig8WW26gYnzhjDGKmDftOtb8RZKyDz5qXQ1U7y0-1791913159-1.2.1.1-KKxqDlOsUSuVy7Lnvdv8LB_idQ_wz8J2dLiH3TbQZ6j9ohdTZuLMpvyaL8HvxHTkrAwAx12CjY9aQuAxOwcIziyZHE8qgR7phuxEmmcB4L.YGlubASon34tjMNS0TWVXJz1OS8jmTk_lrnowlBpeZsPyt8rjbtSJOa4mENcjVHPuIho76b0xs3ec6npiKHu.4wJRgBo3PWKycNW72G4nQ6LV4g1fxdWPH2BIIO95Txi.8neXiH_Di953LztAi.0D2US41hAZjVEZQoPkiyXq3YEuhhkC_RW5fs4r1K.7vrOZErSZUkWprU7GVh4TNPD4.rq3gV7sJluQa2xzJf.tU._0uIONMY_tYEuCFst9QLFZRQJRpVj5wF1Qd_bl2GwcB13HyLHMWTSEgRyim6qC5quOjrG.sWGQ8GxGCEh6pN8kNh1L8LtmtB9KQmMTUoPLUbnlCLk6HRKWJNzzi1HdAEc8zEVsGK5Ig0wtQAxrVmkg2T75suT78sRLuW4enZGj_s2OLZ9Ejtz9Gbi8AwyFcg",
    "XSRF-TOKEN": "eyJpdiI6InhxMndCSDZXUGo2V2l1MGoxQk52Tnc9PSIsInZhbHVlIjoiUGdNdzlueFNqcGZpMzNiclhmWW5oZ3JuUTRUdW4zSzRmaURoYWZya1dibmlKTHNVUGttWmFGZzV6dXplczdKcXZtNHd0UW1Fb1l4SWhoM2V2ZzVuWGZyMHZOWW5oNVg3cmxUVXZVN0lqdEtPYWR6aGtNbytlUXVGU0JPUXZwbGciLCJtYWMiOiIwYThmYTNmNGY3ODgxYTliZDczZjExYmNmNmQyNTdmMjE4ODk1OWM0MjE1NmJmZDJiMjZiODQxNzg5N2Y0NzUwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImwycmtOb1VVU2ZudzR5NGkrcEpweFE9PSIsInZhbHVlIjoiby9kbjUwZXl3ZDVPME9mcnVIUWZIVHFXQ2crc25xQ0dnWDFZRjJTZ2wxRGdoRUdxVG5GMnRiMXVCWjRJcW9SQ3N5WFh3eUUzQStBcEFqRUNVK1BFVjFkVjhBUnVQQVd3TFJTOERlbnRidmtPeGMxT1dGb0NPTzBFMm5WTG1UUG8iLCJtYWMiOiIzOWM1MmUxYWY1YmNlMjE2YjRjODhlNmUyNTE5MjM4Njc5OGU3ODdkYzljNmMyYjBmZjJlYTgzN2QxZWUxNTAyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "7or4BAs3PuWLbF3AOvx8y.Pc5BZ96_AeZv90udu868Y-1791913180-1.2.1.1-AzYpMxmbkqbeHfX6v7Am6nuftQMGJJs1eugQkEHdzO.hQa7YtBXx3HhZj3A.dxVYEe7TxOQ0AU5NatGu5bnGP69gd8txUISqaJxHUzdkCpmHPUpi9co4YHbjVLkSURNK7WCa5jKUOsutLyA9rFfQGieCAjDpqQBNNwVlT5ovU6MluhNwVTLCalqUs7_gTRN_QfR7_pJr.x2I6jo2c4K4mBgxEI3RgLBgnoiOidkRTBUHLFD8ne2hhE2vNsJO7v.5G3nAYaBHotb60u.OGsiWLdz3hXVqRDeA4iPngMSSsP56_tgNf7RHmq6O1jo8.iwfwBYsURxTAUAcqcVS.oCmUj.gLSMAxbzbExNePg6o0vXgtyJ1_HF8nrGFjZIiKuMIaKgnGU7vG7m3TFk53L88z4BKze4VqksF78ZqpXYeJlTMzR.Md8zHQc6vZAbxmxjFPO6QZA.hMSthIXFBo.bW8Xy0CaRccc4.9.4nt34nfO45WdGdBEAC_K90_7yY.Docde42jHjSb8fu2a9RCOOhmA",
    "XSRF-TOKEN": "eyJpdiI6IlpHWE0vNWEzTitxSzRBdFJPRkpKOUE9PSIsInZhbHVlIjoidUxjTnEvQTJWT1Rmb2FDT0E2UURsYTl1UWdON014UUxlY2lMWmxjTFBza1ZUaDJHd1pRYU5ITU10VXFaVGUzWXEzeEhLMUNIeXpLa2JWZENJME9DS2dUYTVicTlRR29BYWpUN3M2ODU4TGFuMkd3NnhJMDJvMGlWU3RYUVhEWTgiLCJtYWMiOiJhMzcwZTNkMzdkMWU4YTkxOGRhMTdlYjcwOThiM2I5OTU0ZTViOTQyYzI5MDJlZjA1MTMxMWUwOWViZTAyMGQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkhMWG5HM2pRREEvaDFaV3BoUytFWWc9PSIsInZhbHVlIjoieEV2VGUyTEU4Lzh0U1pQcVpqRjg0NGdCUVdraFZkVDBvWWFqOFg2U2lLQ01BWnZhc2pCY0RYOTlRdlViV291dDl3R1JqMW1rck5zaTB4V1IxSkVhekVDUDZsVEhjVnlUZnNRc0JhR2xnNTJ3RE9ZS09nb25GSGt6YUpNTWY3VXkiLCJtYWMiOiIzOGFlNWRmNzllMTc5YTVmNWY1YzBmMDQ5M2M0NmNmNDYzYTI3NWE2M2MwMTcyMGE3OTM3NTJiNWVlZWFhYTU5IiwidGFnIjoiIn0%3D",
}

