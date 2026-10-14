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
    "cf_clearance": "kAOCi0h3BXlKQMM6G5hrNc9YraX8jUBSCa2tUev2dQ4-1791951177-1.2.1.1-MbHjjfq__sEKmbBxn.l0X3VCginX59WH7rwKKbNFF26B8gGvrXLvkQmo8Vi.XIFAjnbN3HedqLmcXKxB1c0BUHjP7BQ0s4n63yTXc4tJQgwSo.Qcbe2CWkbaW3v5FJzYRX1qw4GKjsOw9IlqJh2qa5p.E.tGgV5AmkOP8.9UfCsDkaO0DMQoYOm5FEAmplRVtj6TyPszyTKIMddqTniwWL0UVTZwhhk42YwtRI29QuPKAcRC2xR1DuNQtUDkKUl6IDBxeYeE6Jg2BbqxM4GyqKK1F.ziu6KKncFp5PsJc8I_veFoozK3U9HA5tG_s3FIBDqUNegGZw7cNme_v2src5X9GS0l2djiXYTFmP9zzDcuyiU0gr9V2S8qlRbc6RZqtt8Jtg3tjh39JEoq.5J.iR6QrtWm22kjplRjUcxkcdLFrf6IbjW6VdizKPkQmSA.caK9NiA7Di48fJSlKi5MNd5pXB5sCYSU3smlmcYgUwucj0aZuTSOi2V5asp266P40YVPMTu.Sb3x4P3nwUX_Jw",
    "XSRF-TOKEN": "eyJpdiI6IkZVOWhFb2NXeEZSQjBpdFhTSmVwNkE9PSIsInZhbHVlIjoiYXY0WndVN0ZTNFRBZEFwUUVtNWE2YUt4VEJ0M2ZHNTNIVXRFSzl3MlY2WXlRZ2diT2pVU1Z5T3pLVFhCRlZCTmFseVRsdGU3dzNqUzJNTTh6N3FYTDNjVUtRc0l4RVI3eFdqQ3NCYWo3K2V0aEF1VmNuODVKR1k2dDJxKzFsNEwiLCJtYWMiOiIwYzcwM2NjOGYwMDI4Y2M0Zjc1MTgyOTY4ZjQ4NGQwNjNhYTljNDA0ZjQ5ZWE1NjkyMGQ3MTg3MDg0NWYyODVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhFY1NiUFQ4TnR2dlhmdXM0b2gzU1E9PSIsInZhbHVlIjoibWpwbEs3WTcwdmRCbEx4MTdkL0EyeGlhM2lvSjQ2NGxhand6R3JSazM1d29qNk0weHNMdURrczlqZngxS2wrUUk3V1RjMUJYTUVhdnhmd1Z4NlN4MDAwM0laRlQ1Wm9INUl2VWRQUWMyZkhla2FWSGpEellWVUtCRkpBZ2g2OCsiLCJtYWMiOiIxZTAwODI5OGRjYjQ3NDMyNjI2M2JmYWRkMDU0OWYyNmU1YzAyY2FkZTQ1MWQxZmFlMDg4YjBkNzNiOWJmYTE0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "5MbmIjrjtIFMZZcy3w9xtNq2rG0eQhFMRXd4blh0F8w-1791949459-1.2.1.1-koEGeD1g65E03OnWjApjz1Un6ktCYUbpCqHv9mdZMPsPKvlBozIT9esKnGvFia75ZAOcXi7H95Ld3nX1kCwi0wHaCUnw2b._WNB4Of72X3c0EqrQ3_MxuNoqZbPld9xPsZz9MJupMLAWE00ixINkMhHmTu30LTp_4R7mQ2jv2u3wXaTasmCdXh5XJfKJXEbEuAv5GCrYew6gUSeefRQQPXEVGMel.QYva4DCRQV2kfMhCGSgXotknIgTZKantGdSIGcY_Q8fTCLesB_AOFWPcIWh6.euMyB5d3e70aMUQK24AjVlKIER8N6JWQU5QKYn_0WbM_g8iE_wot.l3VUXyHqAtHw_uT7i6CusK.pMJ86aFHoJZk66pGyPPD5GDhOCoWbjXreRRHwxwAJlJmA7a7YWUG4M8BjnqPGDd6uIMQU8z9zmxA0gx3tpEaPp8VfCV4QC2n2N.2Ct9W5iv4yioEHYRZtm.PsT0SCybWvjU1SDNk37lCVUn4uqhs8mMLY6GaLaPGG0JloYSyAg.m8wcg",
    "XSRF-TOKEN": "eyJpdiI6InNhK3ZwZytoYm5tYWx5QUFPTEF2VUE9PSIsInZhbHVlIjoiWFhHMnRpU3psdE5LZjZEMW9mUWp4WjY5SlZpZFFzbTdEYXJ5Ni9BaW82SXlSRTdTMFJ5bFl3N3poSEVoTlorYUZjS3k2aldXSzZWb3BvYktxRzFweXUxR3ptb3d2TkQxa0xLV1pMMUNCS2xuWUQ1c1ZZOXZrSTg0MUxtQTM4T1IiLCJtYWMiOiI1MzY1ZmUwZjhmMjVkYjFjNDY0YmY2NTkyNmQ3ZDBlMjNkODhmN2I1NzE1MDg2NGQyMmM1ZDgzNmI5Njg5MDIyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1GREJ5NmpMa1QxS01nekZ0ZWlLSkE9PSIsInZhbHVlIjoiREM4Y0tWL002YXdwdEdrTlZMRVREdk5MQWxuL0hiOGdZRE8vci9QRWJvdml6a2JGSUpJSFUvRFB2TEw0TVlZcHcxN2JkM0hOeW15YkswUldYaWR2MWRUbnAxQzAvUk9EZCtDSkxINGVGNVkveThSMlc0Q2hGRCtoUlpPUGl2R0siLCJtYWMiOiIyMzAyMjM4YjBmNDczNDkzYzZjNGJkZWU1Zjg4ZGIyMDNmY2JhMWRkYWUyNzA3Y2E0NDE5MzRlMzdmYTZlZTVlIiwidGFnIjoiIn0%3D",
}

