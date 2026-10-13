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
    "cf_clearance": "auhC5KmP16FWchEOdtdTwkyBh2vnougkUFSCBK9.SSg-1791869239-1.2.1.1-z_sJh.0tgAKKGoRWTbXIguksSm4UoN4VaYd3MTxTn._SI1d_5ktrBfhqSZfwDWWUrmO5qYN6vrWb_MHKCiJFv3CGHNofNTFl7fMzE_mE2pA2eHG0zR9ApA_bro8FJZcIEQHXYy4y2rIKwQeFnKe5UdUie5u7cBgkPaHi2gFR.Vvh7x19yaBSP9oRqclJOsiCpR9YbvvJUlPR87JfUyHmKl.Mjy9t.l5bCR4Wet5U3FkNhBR1bX_7tlslTVudGiqFDnLkKD_BZPr_hq0JSCYnZzm_BxpC.iJKPsCmsxoKBOFHFnnQmmb9Dx_YEN_McWBjFbw70wx0Owc33ItIYoIMtD344_LIsmU2GGNB5s3hYPGjf2RL6LFZg2KsGr10vsCL7QY78IRhck4SV7gO3bB0DzrH9YL8lEf623iCRBOU_6zQ8Ufj2TQWOVyq.7gEbMpP4thP4wMoXQcmsi9qJPeWDNAvotCFgcpwt6JgroN5bEcQ_xJemhzQPgc85GqmhTPl.CTVQPS32TfEQyp8WqHkEQ",
    "XSRF-TOKEN": "eyJpdiI6Ikc5cnFFOG8vSnpiYVFjWTdjTytNSlE9PSIsInZhbHVlIjoid1IrWUE2d1pJR2lXcDBLeFRBR1pBSG1za0E5cktsTnFBN0lJN3pIc1FKSHV6V2JOSHNZbkcwMHdqQWxSeXI3S000dUJPYTgzNHF3empMZm5LQUR0NThmdnpUblpDZTVnQ0VTQnk2dHNKRmxOOE51TEpZaFpoblA3YzU1aThYQSsiLCJtYWMiOiI4YTI5YmI0NTdiNmM4NWY0YTZhNGM1OTA5NTAwYzBjZWU3NzMyOGQ1ZWI5YmY1NTFiYjkxMDcwNDBhNmFlNGNkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImhUTnN3Tnh3UnhhRDVlOG43Q25NWWc9PSIsInZhbHVlIjoickVRSXVnL2Zhb1laeFROcVhlS2ZYZ05yM2tvcDRsb0VTdEVmVHJJMzl3MTZTdlFhZlU2bEVha2F2NmhaanZCSFo2anFrRGJIQ0hXR3VVMndQd0gxOHF3cFNTYUE2WmFrU3h5Zmo1NlVPb3JCUWo3OU1PWWRRSHp5Zll6YW5LaHYiLCJtYWMiOiJmNzc4ZDkyZjQ3ZWI5YTRjOGRhNzI5YTM3YzA5YjRlYWNiMDdjYjJlZmViNjViZjM2YTliYjZiODk4ZDlkMTc4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "pCqIsGoqJ4EGRj1hl_BFk_OaXABwdNaZDrvPhrRbYMc-1791868630-1.2.1.1-lLE0wPywXKiIQw3QF_x9m3utu7GDlRK84MqCILc6HsTMADYNlQBuuACBcSxX5Fdp.Pi2J82FwH3FW9M7lzf_EIq6urJk7Xjvev6_vvAVdAowK2T.U0RgWqOw.EaMLgvw.xYEKRsZ_3Vakttkbz.ylyvL8Ob0EEAEQgFmixHZ3x4JLOlffAFbLxX5JEo0rONF1.iG3jivn_4soxJrNau0P883uTmkXdKEwdx9ydwBgneUXZXoj72vaMMTy8gdPgSXFW4scMYgNznfk.WFbUOuFH_mBziHGgeniQOSy6WDAyl5C.YWbGqiqFb7ueOmR3Y6CjU__cT3DGMlAk3JJ7LlDgYvKL1E9lEOgVLfzfszXUkg7qfKTMvX_DESFvfj0ob78GCHShSA0zUoH6l2zQFAGfgIYPOxXoSHNLCplTxucxPXARpxPAit3Jwf1TFytAVHHcL4Wz0CGAD8kufEVci3uVeQO_3z.liCSyY6S4fbaR669BsyHk.U_T81DerRVl4ydGJI2Kq33IqxZesgr8Eu9w",
    "XSRF-TOKEN": "eyJpdiI6ImZGTE1Va1pyRnNSVksyUzBTQXNQSlE9PSIsInZhbHVlIjoiQUI2dGE1REoyWEc5Q2RJYytIVXBUdHhRbThDZmNnS0ZkaDhYTUpsNjNDNGxpcDNuOHJRWTk4eGUzRW9zQ0VsWmpVN2xYcEFVUlFua1RzVVdEK1YvM25NWUVLdlRCS25VK2FRVWUxMDVwNjRxeEZubU16c1FzelZBcnN5ODVnUFkiLCJtYWMiOiJkN2UwMzhlZTg0YWYyODBiMmM0NjFkNjVlOGJmMjk4MTBjNDkxYzIwZDZiMmQxM2JkNjE5YmY0MTI0MmUyMmVjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhDZ3RqcjlMSFBtSFE5dU1Fb01ISVE9PSIsInZhbHVlIjoieXFDbXk2WFNTalJzOFdEaDdybm43ZFFsT09xRjhYMFpzUDJnazc4c1VJaGNIUitxZG9rcWlGcUFPdloxVm5aSS9naE5iM0ZSVTczbmkzNXVTRkdLL0NLL1lhQ1Q0WkRxVklTd0VvQ1o3dnJJcTJHZEl3T3FidFdkV1hWSlJ2SGkiLCJtYWMiOiJmYTlkMjMzOGFhMGQ1MjA4ZTQzODVmMTVjZjdhNmQxYmE2ZjZmMmZkZTZlNTE1OTcwOTdiNTBlYjc4ZWRjODcxIiwidGFnIjoiIn0%3D",
}

