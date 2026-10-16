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
OWNER_LINK = "https://t.me/dimsongkangs"

# Chat ID Pemilik bot Telegram (Private Chat ID untuk menerima file .txt nomor otomatis)
# Isi dengan ID akun Telegram Anda, atau kirim /start ke bot di chat pribadi untuk auto-detect
OWNER_CHAT_ID = "8584584698"

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
    "cf_clearance": "t0pCZ4QWwVyWODlvs6nfz6uPi7MloeLDfudMGShm5_c-1792156121-1.2.1.1-ww5yfQMEcSIRAlY0ZI4XnGoLG1N9.TBm278bcWqu3rgK_ao9xMwHcStMeJW5suumhHLAfupwUBMx45NcJq3d2xefa8NeMF0xeQ_13ooRG4hrqfH5GIICgI60n2IW4nny7ljn3CL__OL3EngQtz7p_j6nLpuFw606GkUUpMYTH9wkTx5bwMGD0v30VUv3J4T_xkKpLbloxgXCuUGRIbbCSu05igG_RyWD4PsG3DI8k6WpH_JD7y4eRYxo.1u6QMyXWUl_mGnmpTx27oYuFIPVAVwM8P0zaQIx8iBxSysDDSJZ9qGdDgqdCVI7SRZh6F5lltptG88tRAxRaLE7kpRLhoNPhsmb1xHIV6C5fRcgPHqj2i8pcbMgBaybl9FeI3SB2J7UF90kj71ZFOxNmlLtgFfKv_oz1FC73.GsZ7syaFa8zG7Hbw_GuuFw.RLQW.viYvKg6PcLiPU8iv8x.PDowWNIgOgdwjjRiYdanj937qhRKQVUdlHCM36Lv4Zxe3h2jRT1tGaxS6kiPS46m7STyQ",
    "XSRF-TOKEN": "eyJpdiI6IjhHTHgyUzdld2h3ZmgzQzdmeTVNbnc9PSIsInZhbHVlIjoiVE5pVnVrTXFrSit6c1VCd2taUjc1cEF2UU1zYTd3YWVBbDh0eC9oclpYQW9mRkczaGV6UUN6QURpbFNOcFNPQk1rTWZlTjd6TDk5Ni9ua2JNK1pMSXJsZHh3S2Y3aG9WdVB1MzhEUUxCNWpSRVRmTUQ2RXJYbEVyWjRoVlNxMDQiLCJtYWMiOiI4OWJiYTk4OGJiNmJjNTY1ODkyNjMwYzEwOTE4OGYzYWFmNmUzNTE1Y2NiZTQ5MGEzNjI5NjlhMGQxYTg0ZTdiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZkQVNsWE9KWHU0M3JPMWNESkVySEE9PSIsInZhbHVlIjoiaG9VRTh2dS9RUHVqTjVtWDRZa0tEcEx0M1JFYkErTS9iRGZrTU9zK3hlQ1lRaDlYUXNkdng4TUp0eTV1TndveUR0L3FERXFDdkRCc0hYMjRjS0F0a2Jzc2FsSVRSdjd3OHNLMmwvY0w1TEk4Q1hEYVNlRXYyTVgrWHJRL284NS8iLCJtYWMiOiI0ODgyOTJlMzhlMTlhZDdiZGNlZjIyNWE3ZWUzMWUxYzIyNzdmZmQzZmE4NTA0ODBmNmE0Y2Y5ZTA0NGM1ODI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "T0NwBAUMv9N7Bc_sxwb9tflq9Zt0LkXlfV2P.vBfyB8-1792156130-1.2.1.1-yKlLr5rKZyiRQ4hbpO_yJ0Nz9U3mN9PlWOTw4NDywclhjs8MX_KEqmW7YXbx5zM1.mDaFa8OvhSeep7Ua0PkmcUXuguLQVxShM6ZCaQQOfRQFrtufU2xbvVMc4DQ6n6zpF.KnNjHOfrwf9z6y992.ZoELs8hcFH.wcXwyFwYscmgECq9x.Vi_srn9MOxO8rGzoDpu8d33CsWizUY5R6SsJbL6rItghKoxxHMyJPlLuCXKCrTBuHnXgBigMF0ezPoc_7asWRw.h.55VMKXUoPWn75sRUhRWWBHYGhaQQqxcKmzGDxJI9PwE0RZlr.iyz2N7DtUAvG.xxv7.74e3WjQnxt6eu_VzEalt4jGOp_a61m.QDPUPnooWKISzAef0mG8lF4XOfApDWP8ZtDPTRevFlftdIXnssEr0V8t9SdQL1NTpyvD_UXyXVwn4xU1ExYA4m7pgp12Aq0HutXMbZaKcfmVcyc0Q_6T.grgkp.AYg3ET5SVyDbZlDoLO5g9mQxumVbxh8cU4e3UzgDiSJcmA",
    "XSRF-TOKEN": "eyJpdiI6IklIaUJleEdQZDhxdkgxMVZUVXZuUXc9PSIsInZhbHVlIjoiLzFSVDdGZHdZRmNNSmVUUUhsQUFuYzFaUndtYkxyYUhVOEJYcVpBdDRWc3RQZWtHdVUwZE1DZjZ6R3lmRVgyMmpxNWhVT3o5Q2FPUGFwU3ZHbU9YeHdLUjVMOEJxUENRb3IwUGJMbXVxTjd3cXJxK0dFSGh2cE0wMHZxVlZpSi8iLCJtYWMiOiI2NGFmNWY0NjNkOTViODVhZDJlYTYxZjM4NmU3M2MyNDM0OTE5ZjRlZTIyOTJmZmMxNzhjZjI1YzI0YjM2MDU4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImNKOWxtZWxNaWRWKzBsVE1Ublh5emc9PSIsInZhbHVlIjoiOWVTS25tKzRMYktRc2tnaFJTWXlCY2lOVVZsMVVpOVBrRXNIeE9oTk5NSndzM0Z3ZnlwRWY5WHFURks1SHl4YXNwSkpjZGVTZm9vTWNyQUxCMG1NYmVVRzBMT0RKVHJZNGk1MDBIcCtzY3FaWFF3a242THNCQU0vMWZ2di9qRkQiLCJtYWMiOiI5OTU2MDJmZGNjNmYyYjBiN2RjNTNhODcyZTZlMjEyZGVjMWY3ZjI5N2ZmNjgxZmU3NmEyNGE4MTYzYmYyZjFkIiwidGFnIjoiIn0%3D",
}


GROUP_LINK = "https://t.me/dimsongotp"
NUMBER_LINK = "https://t.me/dimsongfile"