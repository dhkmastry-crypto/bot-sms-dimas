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
    "cf_clearance": "VkJAy8COjRbX5gMehh8yup_rz.3ngI0UzPp5Q_samX8-1791949373-1.2.1.1-0MGzLqZ4AUANU3FWXwg1K3Lyj6hotLma46tn1uNcwNxkOKF.JitB1BGqXo.JaBnj4xH7MpCm5uBTISFsxy3B9aUJs9avK2pa7isi_vO1c07.gyMcVlsVeAB3.AaktMmfHqSUbGv3EwzHnCmdwPjHIvl.gk_ndyep9TzQHXavcjVSzXirPu9SvU_QJ_Qmpgfk6OZyocejWPb5EGkhLGe66XksyEiHoN.4nwtdKTo346PTwV.6rDpb8QtDMP_54gtxZQtiL_r9nCmg1AnL9VqHE6Pj62Vp.wNYZEq7VMYS4MDCZ9.N4CjrMXPWVM07MWw1yblQTiaz3JAlP3zlpql62eMjpdt_eygqyy_tnbfX8ecjF66htkTGxdVHdmylI57dWnM51PcX5Vd_fHow3v7NtRMohGGU8c4mEj9Z2wBGfQDwsqTxXobHszESBzFKMVH0EN1yJ31t2MWODDpa9Vgpee9.VQF8UUlC7leNRdWJ7gxnq2PWJwzxP4GHJgmf0_sUGTwGD0RuB0HjnFi6O7oPNQ",
    "XSRF-TOKEN": "eyJpdiI6IlRRQlh0ZzdOZzhNSUsyRkFoemZGUWc9PSIsInZhbHVlIjoieWdhNk03SldJcHVaZXZHWk1mYUpjMXhMQVJzZ1hieU5tTnF3ekFyb2NXQ1RIRGQrM0xRUmNHd3JuUlNST1RNeWxYRjBwSy9qb1M5WlovcXBuRG1KNG9uSnJLRDUydG9zSTl6WWJ2VFBrK2JncWx5WFY0S01CWE1DMDNiZE5YMlQiLCJtYWMiOiI0NWIzNTljZWRkMDZhMzMyZjY5YjFlOTlkYjU3OTdiYjU2NWI4NzYwY2M5Zjg3MDMwZDg2ODE1NWFkMTdmYmJiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImN1NjR0MDVpU2xFYlk3VHNNaHhtdlE9PSIsInZhbHVlIjoiMC9vZldKSTB1T1B1T1hZak1kL21FTjZ1TWNQMjVsS0NVK0FiRHVwR0ZFbWEwRnFOQmNONkxhZnZzMVRiWlkxbUZtdkUxblduM0VhS3dYZzJta1hGMEZUdi9hRE1FdktSYW14WUJpbEdrT09BT2JieDVnTlVRY3JIUVlmTmhZVFgiLCJtYWMiOiJjNDRiNWVjYjMwNDBlNzhhZjMyY2Y2NjM5YWQ0MjFiYWU3ZjgxYzc0NWUwNjBjZGFiZDlhMWI3MjQ4NTM1MGZmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "5MbmIjrjtIFMZZcy3w9xtNq2rG0eQhFMRXd4blh0F8w-1791949459-1.2.1.1-koEGeD1g65E03OnWjApjz1Un6ktCYUbpCqHv9mdZMPsPKvlBozIT9esKnGvFia75ZAOcXi7H95Ld3nX1kCwi0wHaCUnw2b._WNB4Of72X3c0EqrQ3_MxuNoqZbPld9xPsZz9MJupMLAWE00ixINkMhHmTu30LTp_4R7mQ2jv2u3wXaTasmCdXh5XJfKJXEbEuAv5GCrYew6gUSeefRQQPXEVGMel.QYva4DCRQV2kfMhCGSgXotknIgTZKantGdSIGcY_Q8fTCLesB_AOFWPcIWh6.euMyB5d3e70aMUQK24AjVlKIER8N6JWQU5QKYn_0WbM_g8iE_wot.l3VUXyHqAtHw_uT7i6CusK.pMJ86aFHoJZk66pGyPPD5GDhOCoWbjXreRRHwxwAJlJmA7a7YWUG4M8BjnqPGDd6uIMQU8z9zmxA0gx3tpEaPp8VfCV4QC2n2N.2Ct9W5iv4yioEHYRZtm.PsT0SCybWvjU1SDNk37lCVUn4uqhs8mMLY6GaLaPGG0JloYSyAg.m8wcg",
    "XSRF-TOKEN": "eyJpdiI6InNhK3ZwZytoYm5tYWx5QUFPTEF2VUE9PSIsInZhbHVlIjoiWFhHMnRpU3psdE5LZjZEMW9mUWp4WjY5SlZpZFFzbTdEYXJ5Ni9BaW82SXlSRTdTMFJ5bFl3N3poSEVoTlorYUZjS3k2aldXSzZWb3BvYktxRzFweXUxR3ptb3d2TkQxa0xLV1pMMUNCS2xuWUQ1c1ZZOXZrSTg0MUxtQTM4T1IiLCJtYWMiOiI1MzY1ZmUwZjhmMjVkYjFjNDY0YmY2NTkyNmQ3ZDBlMjNkODhmN2I1NzE1MDg2NGQyMmM1ZDgzNmI5Njg5MDIyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1GREJ5NmpMa1QxS01nekZ0ZWlLSkE9PSIsInZhbHVlIjoiREM4Y0tWL002YXdwdEdrTlZMRVREdk5MQWxuL0hiOGdZRE8vci9QRWJvdml6a2JGSUpJSFUvRFB2TEw0TVlZcHcxN2JkM0hOeW15YkswUldYaWR2MWRUbnAxQzAvUk9EZCtDSkxINGVGNVkveThSMlc0Q2hGRCtoUlpPUGl2R0siLCJtYWMiOiIyMzAyMjM4YjBmNDczNDkzYzZjNGJkZWU1Zjg4ZGIyMDNmY2JhMWRkYWUyNzA3Y2E0NDE5MzRlMzdmYTZlZTVlIiwidGFnIjoiIn0%3D",
}

