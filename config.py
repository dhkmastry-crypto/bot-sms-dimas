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
    "cf_clearance": ".V3phxPiQQoBEnLiPQdoq8vPKnDGP0Mg8dQCvQBQqeE-1791867434-1.2.1.1-O3Iz6U1yB7.XSHFewpp5AzmaqQRti8nQXo6HMTQjtfOAehRdaA_TVqKYlRW5qedGwBsoZ9TgRy62lIV91SiIIXVy2GMv71z0eIRRgBL13_yExTCL6IdKEnc3hOflSVRZcNrlNsc8Bnwr.qXY_6ZzoZ4iFgseWLnH06HoLvFgAryloVUY6L_eVm3fLogRzF9L0XY3AQzn1RiGYdRBR5XOGq0Kft9m2M3fjvRdcGdiCizPYKfaWmUzIPiyarOQ.Ov7.yckeVD3.PzpjJH_Ea_TVuRaKKORqdM7lLxcJylTzHlZs45jpprLFDGe3b1Wu3UWWc8EIFxc5v33MjIG44r0TqJE4dt4IaxaHl2ahAjHaMp0rG1CU6S079504CrQwNh1txb891KXZxBqoZMegdqsVb8lODfOMLZsKKN0hRu70d7DX47t2LhNzvFZVI5RPHX6R4Ze7Bi3V3AAFQDepdrsYpJ14dBhmFwo.eH4kXBXi6uGOTcfuwjyk_fXadV1FU22TMlT2KQUFgLNFgulMjvPnQ",
    "XSRF-TOKEN": "eyJpdiI6IjRjd3g4YW0zcGhwS21udzg5MHNMVHc9PSIsInZhbHVlIjoiTHZTaUNKRDlnWUhQUTR3MkJiSTJJaFU5bzM5OGczRG0wWitaYUZBRmFOK1ptc2ZmeHV5VGJCWXpkaHhOTzk3Q05qR250cnFmRVk5V0xqQUN4WnFQeUVtTWtrWm03aVNMQkxkN3pVR0liTCtuc3Q1Z2hCanVPUng3b2FodC9tcWkiLCJtYWMiOiI4ODM0NTkxZWVjYjJhMzg3ZTg2YWE5NDE0MmNmZDNiODAwNDlmMWJjYWQ3OTM0NDlkNTk4M2VmYzBjYzVlMmRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImtyMkpHYW94TjdaQWE1TC9HelBEcFE9PSIsInZhbHVlIjoiZjJqQzUzc0VwMXVCL1FhY3hLb2VhbDNLWDdLSUtVS05HS2c0b3EyRXlzTmdsWGkwT1d3T2FETEN3Y0lRNGl3MVdteURoN0Fqc1FRWlMvbnMvYkhEdGRYd3IxRXVWUmZZNS9reXBEWno3d0NmV0ZMaTJpaDdhaklJVjFlNjByOVYiLCJtYWMiOiIyYWRkODc0NDNmYzU5MTUyN2M5Y2ZhZmZmODBmY2JlZDA2NTMwOTE4MmI4M2IxOTkzNjY4ZTU4ODRmNmFiZTQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "pCqIsGoqJ4EGRj1hl_BFk_OaXABwdNaZDrvPhrRbYMc-1791868630-1.2.1.1-lLE0wPywXKiIQw3QF_x9m3utu7GDlRK84MqCILc6HsTMADYNlQBuuACBcSxX5Fdp.Pi2J82FwH3FW9M7lzf_EIq6urJk7Xjvev6_vvAVdAowK2T.U0RgWqOw.EaMLgvw.xYEKRsZ_3Vakttkbz.ylyvL8Ob0EEAEQgFmixHZ3x4JLOlffAFbLxX5JEo0rONF1.iG3jivn_4soxJrNau0P883uTmkXdKEwdx9ydwBgneUXZXoj72vaMMTy8gdPgSXFW4scMYgNznfk.WFbUOuFH_mBziHGgeniQOSy6WDAyl5C.YWbGqiqFb7ueOmR3Y6CjU__cT3DGMlAk3JJ7LlDgYvKL1E9lEOgVLfzfszXUkg7qfKTMvX_DESFvfj0ob78GCHShSA0zUoH6l2zQFAGfgIYPOxXoSHNLCplTxucxPXARpxPAit3Jwf1TFytAVHHcL4Wz0CGAD8kufEVci3uVeQO_3z.liCSyY6S4fbaR669BsyHk.U_T81DerRVl4ydGJI2Kq33IqxZesgr8Eu9w",
    "XSRF-TOKEN": "eyJpdiI6ImZGTE1Va1pyRnNSVksyUzBTQXNQSlE9PSIsInZhbHVlIjoiQUI2dGE1REoyWEc5Q2RJYytIVXBUdHhRbThDZmNnS0ZkaDhYTUpsNjNDNGxpcDNuOHJRWTk4eGUzRW9zQ0VsWmpVN2xYcEFVUlFua1RzVVdEK1YvM25NWUVLdlRCS25VK2FRVWUxMDVwNjRxeEZubU16c1FzelZBcnN5ODVnUFkiLCJtYWMiOiJkN2UwMzhlZTg0YWYyODBiMmM0NjFkNjVlOGJmMjk4MTBjNDkxYzIwZDZiMmQxM2JkNjE5YmY0MTI0MmUyMmVjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhDZ3RqcjlMSFBtSFE5dU1Fb01ISVE9PSIsInZhbHVlIjoieXFDbXk2WFNTalJzOFdEaDdybm43ZFFsT09xRjhYMFpzUDJnazc4c1VJaGNIUitxZG9rcWlGcUFPdloxVm5aSS9naE5iM0ZSVTczbmkzNXVTRkdLL0NLL1lhQ1Q0WkRxVklTd0VvQ1o3dnJJcTJHZEl3T3FidFdkV1hWSlJ2SGkiLCJtYWMiOiJmYTlkMjMzOGFhMGQ1MjA4ZTQzODVmMTVjZjdhNmQxYmE2ZjZmMmZkZTZlNTE1OTcwOTdiNTBlYjc4ZWRjODcxIiwidGFnIjoiIn0%3D",
}

