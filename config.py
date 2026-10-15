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
    "cf_clearance": "rwSxhlb3d7mK.h0LzOjMjnqyQx4vT384d2D9.HHLh7c-1792049271-1.2.1.1-bb.5AL5ZfNYFIz57rDZHmJruj4t2XhcermvV6AoATvYBPanp2y8u71knDWc_9uf5tEgHa6Wj.CIGFzLEgSDWrT1Bax3XrgnIx_xIqt.bUifgrAyelWN3HyNNAAKSHKy9kfpgYdhiSsbb5ZEM7HroGluw8oFh7HD.VKIGeW7HMwdZ8ec3XIEl14Hb_bzsuDy4tDLSo6f13FLgDR8Q.Nqssks3OW7Zi.cvyzbQOtiGIhRi2Bby1TazC.D_vNZMUpOjlKunHsZhZbaI6UVejaY1zmj9f73D2Iwc2AItrdpCIc_TtWpzaIGlnr3bnznurz.D06R6g45FT5_QTN5KO39N_3OdFjTIb0YqW5nhSWGN_nfLh_GlEWWplmTGVRzp..kLGDpmt5dbf2cM_g2DTH4LV89pya_m8LqfWcb6lCvxgKgMO3Ea.x0zGZzmT2fzjViZLU1ywsyfrAkMrCQu._YRhVUTDKjX.rVTLGME68RQSmuN9SQ4HYL9xt3is_PIab12M6ZFpuLdEy6CKwumWH6LIw",
    "XSRF-TOKEN": "eyJpdiI6Imh4ZWNGZDd2dlRXdDNyTDMvbklUQVE9PSIsInZhbHVlIjoiVkttaVI0VW9lS1dqeEh1R1pLNDRhYzVva0czZlg5aGxEOEJLMnBEYjM2WTYzaERBUGtUR3VkaU0weVhXeENPODZSOEwxdG9IdVJNRlAxcXBSWFVoQ3d0bXgxMm5SdlBZWDlTUXZEY2E0bitmZ1lYaXlKcWk5MGZqSTZONnU1NkciLCJtYWMiOiI0MmQ4NDVkM2IzY2QwNDU0NjhjZGY1MTRlNzEwYTZhNDgzNzViNzBlZmJiYTg2MGQzOTNmZTU3MmZkMmI3ODJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVLVEdHazNNM1pEL3V1OHArZmZ6YUE9PSIsInZhbHVlIjoiOWNrdG9yOVlsNTN4Q2JSQ1VHK0ppNmt4a2ViSlhCTDBFSVNrbXNSckYxZmVMenA0RlIzK00wMWpBbWZTcDVPUDgvOVlkMEdvTXcwd1U4RFRVdmo5bkw3N3hnUG16WnRLRkFHWkh4ZWYwR2o0alBXWHdiNUNWbzkyNWgvZGhQY1MiLCJtYWMiOiI2NzQyOWM0ZTk2NmU3NmYwODRiNjFmNjUzYTllOGU1MTA3N2ExNTk0ZjNmNjU5OTAxOGE5OTllNWU4ZDdhYzBjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "blq7NsG4WbNLbCJEa1299LEaevtFE7IX3j5v1cNFnsg-1792051037-1.2.1.1-MBt6dZWzM8l3qNr4gCup.qhDXcc1J71jphD5aULRAOJNCqpiMBaHcmaKapnXvUTbvotRUQf5GoJqZOhmBglxn8Bdt6PQqC0MC46FWwQOob4x49rvursp8SdbGeP.d7PSeN09h9NjjBnk_KK8TxHYfnHDYVXiqwPkN1yB1y5h.BRr0xgpUhyuyGpYehSGxLFO.CoiXa_hj32r0.0qfvSQ7SODM78JOkLjdwU0TlE.yFZhUrL652stT38.ZOdrwM_6S0kY6sDwDUPkS3Fo0pSdhoWoeFm5ocl.lQFi13E0y2iEk5sNqaV14eShCx0.tvkriRR6izJ.RA_wgZzlRrPK.XfzCydZfLpfif_Rn139c_8of1gklFjHPn6dxdA9Mr4ZArMgfEnWprzynPOpvALVCE6yd7Z95oJ2G_cfUR0PfHxMOOeyYefGYqKqguCSgEr7kEK9KrMSf4bdfWWl8sdh3ZLCrOvvZw6IDBnD7ajvHmkm95OlfF8lyXVdCNlV6muV2lVRGscMa6NkH8XAU1nI8A",
    "XSRF-TOKEN": "eyJpdiI6IlZtOXdOZHNFWkJWVy80a3hLd0s3M2c9PSIsInZhbHVlIjoib3hzR2o1UXNyV0V1RFNmMUlSYThvTlYwN2V2ZFpEY0tVUU54Q2c3QlNFaU51bjNOZ3ZudHFrSU9ZOWE5MGJTNUVXa1FKV2dERlBXYmliZEd2ejZNZGJrR2V1MjZhSmhMOHEybFV0V3JsazRPZ3lpSkJNN0g4RG9LOUhSZXF1WkciLCJtYWMiOiJhYmZhY2IwMWI0NWVhNzgzNmJmMWM2NTYwMThkOTYzMTZjY2VlMjBkMDVmM2NiYzBmMTY1NjBiN2M2NzAxODhmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InNTT2R6Q1Q5WS83OUNYSlNWUW9GRHc9PSIsInZhbHVlIjoiR3JFSVQrYkFYdFlvOTJlcjlEVDVhWEl0WHZHaWUzVXZ5bW8yOXJYZGVidnlvb3ZZZXNGYUYxc1ZMVjRhUGs3WU1BR042WSt4dnJBVDRhYUVjSmV3WVQ2MGZKUElXNm82UzhacUlxQUViQWZJM2pIQng4Nzh1cFY2RmFHZ0VCVWsiLCJtYWMiOiIyM2NjMjM0MmVlMWI5OTA3NTIzNTU2ZDYwYjhlMzJlMTdiNzI4M2VjZGM3YmYzZWUwYzJhZGQxZGRiNWZjMjczIiwidGFnIjoiIn0%3D",
}

