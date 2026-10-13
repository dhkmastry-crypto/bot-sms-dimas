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
    "cf_clearance": "jHEzxsFqAWKhAFL8XB_Ju5qQAu.zzlfRCzf8dw5CQS0-1791914973-1.2.1.1-ovbc9IPzy1PQFW0dPDacJjkOEsgALlx.JoW5goBxk20rS_uC78sUBwu13iYanzQTFoRtOMZ1T7S4GTf47qMBKGueoqvlAZpunw6H_gKJ4jeOocM96LKMjFxFh.Ixg0rpp7sk689lu5zHAlUbOktYpVIpR8uaWY6ELDJv5LsOwlgOKrKCbzqh8zLpFxXc8tGbNTERF0xVxgnmi8hireS1tIrMOyXh.jU44i3vade.UR2laisCFGHQ1nYpTOV7iMYs4U0gjIKak.cAGxPF85989.ajSxF89B8jhZZx53nRy2nz7.4bLaHftMPEhFkoWcJ7TCO4qsDj_d_EU4fMRlfnkli5LKBjvCM1HcZTPyiR5NmE2U5Zlm2ITn2kBukMaVhz1H4NBEy86UWaVDvmU_85tSwP.Exmnd76tuA5hbCR20PE7hVHI_AwhGyXi6kv2VKbgL_Sf.q_QDhZVEPb725klF_Dve9gD1wikSGcIbq3ZSQkCVxeM6JcVaoTFPV3qYGNCAjegaIAH0cwIB9NLBn8bQ",
    "XSRF-TOKEN": "eyJpdiI6IjViV29Xb28yRlRyYjZHekNRQ1RWSmc9PSIsInZhbHVlIjoiSGM2dEw5Q24vdmoyQVlYZXY1T0RYZHNMaTRqME5SbTVNbEhobE0xZVo1dW9WMU9wQThPalRtdVVEckY4eERKVU5EYkN5ckVoYlJHMWRmdXFKeFBKNmFCQjlzWWlGMlVqTXBFZ3RKckhQT1Z6elp6K1I1elVhalI2c3hHaHg2bTgiLCJtYWMiOiIxMTM4NjdhODM4MjQ4OGVlZTA4YmRiMTQyYjJjYmQwM2ZhMGExNzU5MzYyOTg5MGY3MGYxM2U0YzVjOTM1MzdhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImJ4WlE3R0M4TWc1Um94cTN1VGRvTHc9PSIsInZhbHVlIjoiTHNvb1JDVVJVMm13Qk50R2VKUkFYTE1YcFZTQ0ZCY2VrRnhYa1AwMkVFOEczbmljZTU1T25wUHBub2szNE1VTktWTUtHRGdwV1V4MTZaVHFTV1NmMExTaTN4eFF1bDRRVEE5dzJCMEZuQW8wd29nOXZveUI5OTdRZkVXVThTZ0EiLCJtYWMiOiJkMWFlMTJmMDcxNDg2NjEyMGQ0N2I3OTdkYWUzMTE1Mjg5MTgzNGE1M2IzMzg1Mzg2NmQ3NGU0ODJkMjg5MTc1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "_kpwD_Wh3kANo9jqliv8Q0rgQmWEyPURWxTxkwmzRCg-1791914984-1.2.1.1-wWiYGBcNH60.6fWpd2u3XjATMad9_efk_RcJHlrAzXkBeqVSQO9yqgZ5Z.MCr_w_5WoqsUg25yvH_ksZ.YR4Ko2C_meOuwhZH24Ih0cZkd2xQl7DRaMfeCBy8YjAglGTyEFWKNmqDbVJY1X9qxgzDrBAR07jdQVvY12.Bl8kSaBYmTluJprdBbFDWo7m_WdSkhtTMpPDTvSi7rIrc8HgQ4LDCugPwmMzc76ai5vQ1ZdfOx9vvXE1x2Mv7bHFANuA.Ir_ypTj7BldJOIZVeVu6DtIrEVMP._bk6o_NMFZe6cCdNns8W7_QUqtFvBlTpcK7_mCmq_vs1S9C7MY7f2VoLqURvyQ67DD3buU6rOC46NFjdacG_INqL8fygAC37t97IETyN9ZMEgAPbsBZ.fBJ9d4S0RGahYbL7JbTzdcPQDxeCbYf2Uk_HP7EkQrRN_cw33Hh1c4ZIs4YlJeFlkF4HjTQHlKjBPi1ycN9UH02LUOyc4lt0B_ufY7swypeZLYE6kDvdQMaeiXQ09.K7Upxw",
    "XSRF-TOKEN": "eyJpdiI6IlBTb3JqZnlaaXhoUGdIeHV1RzRzWmc9PSIsInZhbHVlIjoiMVF0Z1hmWm9rUmREdENUUWp2cXVBQSs2OXJPUnNLMnBJMk9jK3BBSzlhYkZRa0JaL0hZWXZSUnczMFhlNXNaRDVTZTJ6aDhMY0R2ZDF2WUJMa3JUSW9JcjI2TjlKRWVpZ0MrZG8wMllRNjg4WHc4MXN0U0tDRm4rV3BycXVPeEkiLCJtYWMiOiI5ZjYxMmVjOWY0YTU4ZjUwZGZiNDRkMGFiYzEwMmJlZjk5ODlkMGVmOWFjZWRmYTY3NTkxMDJjMzJhOWU3OTNiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik45amk2R1lhNlIxQnRlSFJRQ1N1L2c9PSIsInZhbHVlIjoiVFZ6eUt6RHhhOEwybStWekxQa055UnZueEVoaW5OYThRVEROUHE5dVNvTkRqcW5VVHdOaE11UHc0ZjF3UC9PRUhWbDVYMW9GajF6cE9yN1o5bU11cENyc0VIcWVORC9HK3AwZFpiL0sxUkhsK0JBV0dyb09MSW1aT0NEb1VwL0siLCJtYWMiOiI1ZDJiNzE1ODM3ZGE4ZjE0ZGM0MDRmYWQ0Yjc2ODJlMjIwMzhkMDMzNGMxMWRhZTE0ZmI5MjExNjVmZDRjMDlkIiwidGFnIjoiIn0%3D",
}

