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
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "1S7fw1s_iBlfZ.iji0Ou71_JV5r1mjeWgkiU7qG.lSU-1791889144-1.2.1.1-LHkaRQWcY35yo2UeIg5nEKn2SLzRW.te_6Hqa9kBoyxLWWkflwXWNUMzDnsCHp98v9fs.tGVboJfu_.EHbUOPD95brFn81_ua.jdxAfTTmbursVajWdMlliIHYtqkivqP6z.VjznwfcenDWh.iHasB2HY8d8s1.AusOx49zGxlE7s8yrJsTI5bbgDs5LiKiY.O2aiPYYMuISNvh.nishsHImlqXwFGw.ehSxK3N7d7DZxlolps2mM9qs9fLhZOvUE5ftlV0ajNDo81AU1JKJXJ1qJbrfskz5VcKt7SZ5ly4fPQv8MCb1Drv69WK6gGMIZ97k2Iv33YEzVX9UxFcAmlktNfv2A9D8BdAh_CskOCxayPYuBxzI7RPJeR88H0wT3VumwA.WZonz.rrIxRVZbf2CW4xdbN1g9DbhGa8YDkTnonXc8mmoJlbzd3ZBUr3mO_dcf0cTKilf1ucOwEbhcHk5pW.pFmRCzWyykpk7Xdd.MddU162SEyhUzf_Bjf13Fp.XnlCbQb4wvkMG49_AxA",
    "XSRF-TOKEN": "eyJpdiI6IlloVlpZSVh4V1EvcXpsNG1TWEowc2c9PSIsInZhbHVlIjoibHlSTFBmSHlyUUJJTVIwRldOWFRlRTc2VEpJUkZGMS9nSUlPZVQ3Ynl4aktyM2VQYnRISE5WUUZackhTbjdFM3dwQUxOVUxzVEk4RmtUbm5DWjh0dEZrRjlzZmxKclZabTVIcU44R2kwSlo3NGJXZmpQQjhsYnRzR2M5UFFlNlUiLCJtYWMiOiI0ODdlNDZjMDk1YTg1OGYwM2I4MmI5YjdlNzcwYjNlN2EzNmMyOWExM2NiNzJmNjA0ZWJiN2VhM2FiOGZiNWEwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImhHcjhqcXhqNmpKdlNIUWRhUmpvZ2c9PSIsInZhbHVlIjoiWEtEWDJiTVRaMm1QSytFU3A2NG53NXVaMk0vT3RJc2VFaG1wUGtQR2pDbmlnSE56NW9YRmRNeUFzL0JZSWZvb3BSOHhxeTBhUlpkWXRUZkFCanVLYmFEd1FKcGZOUW10TmUrZjlLT1I1c0pTSWVad0U0ZDFoSUpvcTBrZ2daWjEiLCJtYWMiOiI2MDEwYmRjNjhmNjU4MGE3M2ZjMjA2OWMyYTIwYmYyZDRhYjI3YTA4MGI2ZTQ0NmY3NThmYjExZDc2MDlmZjk5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "0ULjaQ1M.RMEZzgaPkAema7N_k.yhqFNAawOdu1Ey9M-1791888517-1.2.1.1-NnwwuQiinUyaDDxiISgaBEOtjxr91JeJ4IE9g4XffJuqH5_04JxYYUZuj4cxWwdxKBgvFLQAbm03q8BJ9iKpZnSlrcjT522sDkxU64Uj_8SPiE_4YufR8NpTByAc6E5Y0YL2qD7X7RzRCYdltBTWAkV6SVN2ImxYBeib1mPbAo9QDP5haRH_xG.YQNTSJBXW57oI.pnLYZEXleNnpbo3LRlawMIhWGPep1nYyTbZ8z2ba4Hl_jaC5qQGUl8aXaRUF6OdncBG3ApJKOAlWXB5DSnx6SBmjVdBwUCynQh06urOyOyIhao7S5ZLhTeHQgtyMndSfFvX5QI.1t_fzj7mYYMvAMS7jOzOyyRfFgbimHAR1E.F.z5IjYbXHvtzD3ddTXg..x65Y5hZx674iO.UfiEbvknJHbWTk8BEse09UzJcuU19BhnBxqWEdGLeSBdPiUMmdBG69w60UR8kggmkdMvdnroH477kscQwu8jY3Wkw7rS7nARD2To40fTeM43bxNsDecy5NKDkgG6rSwTYcQ",
    "XSRF-TOKEN": "eyJpdiI6ImdDQ25JVmk1VW1wVncySlZIT0Vhd3c9PSIsInZhbHVlIjoiV2QwNjBQK2ZCeGdGaDBWSlR2REQweHZ3anIvUGhXSTB6ZG9LeU53REpQNnFmbHJXV25ic09Jb0MzMTBxeUh0dTd0ajNzS1Y1VkMxSjhoZjMxcURqSWZYaUpiWnAvRVRNb0NsUFlVVXBoVHRuemt6eDNEYW1QblhNcWUyVEpPWmsiLCJtYWMiOiJiMTM3OTBiMzhlYmU2ZmQyY2VjMmEyNjFlODIyYjJkMjIwZTE0MTk2YWUyNDk1MTVkNmViMzUzNDE1NTk1MzEyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhYYS9qbG5yUGt3Unp5UHdUVFJ2VkE9PSIsInZhbHVlIjoiYXRTN1ZZSGUvOUNqM1hZY3pzOGMwSXl4cWY3cnR3NWR2R0dJWDZnZ1pQUUxPN1ZMam9MNG5jVjhLRkhpNHE4N1NZSGNYc2JCanFwZE1seC9qUlJSa3g0SUgzODZXMGU4NWZ5Rm9uekwvUlgyb2x2WThieUtaMlgza3VyT01wM0IiLCJtYWMiOiI2ZTI1MjNjYjZmYWYzNGRiNDEwYjQ2ZWZkMWJlNmI3NjkyMjQzODAwYjBhYjMxZmE3ZDg1ZThkMWZjZjZhMmEwIiwidGFnIjoiIn0%3D",
}

