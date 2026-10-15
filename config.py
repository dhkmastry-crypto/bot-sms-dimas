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
    "cf_clearance": "Xc4q4bQNqkFddJtJUfnoYo1UeWjUOhJtAqsMvsqDZCw-1792030111-1.2.1.1-VdSTI446BGj.7FQdDMM1h9EAkCKoAAm_UH7r1Rto.4HS_0pPL567ckyXWCaS9A3aN5ITSGAN0ob46l_jRc5t6mr.A8BjdZJ_FXdmY6FbYSM7Kgnv3RHkEJ9rvoarmsC2u4sBaYHQ_clbnPCETaZRaD8EsuoBUeTJfDDP5P3NNfZ9eO0QxSoHu3mypX77r3lEuNjJ4.F8VdvEk32tANxlk4Lf_Az394VAp39bFblzKiw1jCeaOr1Hhkvfja9jCdTfnP4Qasov25XlSfIoGwD_qhdri9y2hi85iflim1ies1WEfQAY5_vCVQQwZIFapF47WVvELRLa0H4mbEfe0Xo_3yMjqNvqjrrqYuueOYpm4zXbYO5Gmf_NkrVSlZ_O0CJokaTWLvc9sD2u04XfMikMmKIT.0qnmxWN7dxBI_SNy3.9wHrRuRS.2VIU_Cw3C35934eiLMdje0dLUEJMGOozE7oRvI25Ua6fijaX_dD0pi7.XqhnUEJUuGQuqLEBtnwI_yu8h3WTELIB1rEJ0i5WbQ",
    "XSRF-TOKEN": "eyJpdiI6IkZSazhBTUEvckNWQmdlVXJoSjZVNlE9PSIsInZhbHVlIjoiMjc4WFYrR0ltYjMxYTJseTNyMGczK3k5OHJQdnBvdXhkWng0MzNxVm5uR2ptUnRSblB0b0lTVnp1WnlsQys1Wk14endNRThGY3Q2YjMydmtkRlNkaXIvU243VTlqNmQrSE9lcElHUDN3OEV4VVlBZTQvM3MybTdSSmtKRDRxZFAiLCJtYWMiOiI5NmNlODZlOWQwZDNjZDA5ZWEyZmViNzQ0NGVhNTFhNTI5ODg0MTM5MmVkOTE2NWVmYzhmY2M2Mjc5OTM0YWQ3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZUWXgxVzZnWGZjWGdHQ0dIRDNGeEE9PSIsInZhbHVlIjoiNmt0dzF3cU5PSkdKVXNYN3BacE1jQmpnQTJidnpHN25maTY0amtwMG4ra3o4dFVWM3lUK2xXT1FnQ2JIc0ZwSEkzeWEreUpmVTlTTmlmNFNad2FDcHg0SUJFUjB2TlAzQjJoKzltcE9WaHVPcTRtMlBTMStBNy8xTjM4U2R0RWkiLCJtYWMiOiJjMGQwZDRlN2RhZTlkNWZiMjVjYTk2MDU3ODAwNjAyMWVmNmFhY2FhYmIwNWMxOWFmNjRhNjgwNGQ2Zjg2OTdlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "t..5ii9F5radichgCJnXwR8PaJH7P4wC5V5p02.6izA-1792030101-1.2.1.1-_1l32cl1p0JU34VYmER5pi1ovdji4xFS9B.sz49As5OiJV0_l0m1I2UCw6Q3OxaXP4KLGclHAYSA7sYG3tBBblOAlqu7TY8O3HLMQedzw8G2u__P.Hs653kVpLsG5.qzjQs8d3LIB_U1MefGKdMl8G7XXsmjH28OdUuuvENqeyW0FUZzDX.KUS_k54tjJD0asFViD16IKLVnbfJTPSB_6orMfyUnu0qpWF40t5IGyOjqXHf0br_4Ux_64LtNpgp7znN83JCYp.AjQHqKlD.J4Z5Yoqqzd93VbbfG_6F5Kk2B56luP4yuE7SgJSI9pBhHPATueCf8qLiortXZVAShdLwiDoEP.sqC2ntVZErM3CB34otcOvjcWG18CmlgtdWU0.zbFKShn8f2XgUai0.QAfcVS1.y_a2fyvoWT_rL6ikvJqYryaY9GJpO3wtUR48CSTxc2eEsSNmnWN98AOdW3bAoER8G5VC1rsAjfsv4_vk7.nDm_dh8bdvGGDJg3.YfWe0u8SywzfvNv.Iv7ad03w",
    "XSRF-TOKEN": "eyJpdiI6InFCdVJ1am1Ed291VmFsd2RyUytncnc9PSIsInZhbHVlIjoiaVlXdzVBRWRya1Z4UllOZVFpcHNuYk80NzRUeVBKUVFNbzVxVUgwdmU5MXRpQXF0VUV4MEVtMW00ZG9EbDc1cmttS3RZVTVCQ3A4RWY5aUtUVzBDR1hmVjJJYjhNLzkvTXdMQnMxQnk0a2c4eWRNUUk0SVJYRDJ1V0c4SXdiUzIiLCJtYWMiOiJlZjAyNTNkNzIyYzNiOTQzNWZlMWM3ODU5MTJmODdmYzYyZDVkODEyY2RkMDczYTdhZjI1ZDIzMWNiOTU4ZGJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik1wamlqc1ZmdGdXQmJGTmpnc0kwT1E9PSIsInZhbHVlIjoiOUhXL2RIMkVjd1ptT1E4UmM5WEtvWjlSZFpXYkRXRW01Nm5jeTk0K05BcU5ZWWw0Y2pScFRtY3NNNjlzaXp1WWRlZ01Hb0JaTDNHY2Y1cW5oQ3owL21lTnNPYTAzQ2hDK25KQXd1czJzbnozcXpKLzd1VEZuNHJRVXMwQlFOZVQiLCJtYWMiOiI4MjY5NWEyMTA0MTM1MzVhMjkxMmY5NmZmYzEzNmRiNzAxMGFhODMyZTM3MTZlYTIyNTBhOTU1Y2Y3NzM3NWZjIiwidGFnIjoiIn0%3D",
}

