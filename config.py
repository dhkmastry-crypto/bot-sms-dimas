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
    "cf_clearance": "54nIgN5MG5MNOKD_W0rK56n17Y7x5nObsNye52qT3Xo-1792112628-1.2.1.1-MXh.Pd9JlgkAt12ekaUrkGkNPaW6APyxb58sCCisNKmTGjeD2v4szDU_Yp9bmIuxbNZtiBQmfmSo0Pm4Bop3deramq7L4TkE2wzTHdTQ7C8Ql6TF.Om6kYfKhtBzaBWlXbjJZvq1jX_nRx_0F0Olk38I8i5yz.dyWOqMVxD4sq75FuwcAwRQXpw0xKUFgxnKgJnK.YwefHrPYPuSjGTnU0hL48K9QT0tPqVlXWWoz68izNh5_TCYqjKrkqLW.tpWH8K0S0j97oY5EJPoCSQRVbEdxUapE3m6eqH2P5AWc5_8PMzm9Y4fXE3_gaefMIe3I5.wj.Mbek0Hj0NjVpJ90EiHUfQryTSLoh0NXPCPMS66UChGXH3L9W6.9FsJtYvGfrLPZyEGff6nN62nTP2kDwzVwdgiOk8..7r0EpkaLc5SnB_6voYL3J7YOxdLiyUu.n..TKkeQLSwf4lqaSj8KMzNRTN0_uLN_LJHw5gqkHQ2fdRiWq4QwZhIcV6VigzQtWlEzioj7fIddRJfoZLQQA",
    "XSRF-TOKEN": "eyJpdiI6InMxUTJTUG5EWUJwUHNFa0NsMmlsYnc9PSIsInZhbHVlIjoiVVZTK2JyM25QQnJYMkRvVzdST0JjYnppaFNYTnp0MFhXZWxWTmk5QS9VWGVxejVYOHRqaUhoNGxvM1B1MmxocGI0SnRROHRZR1FNQjdMa2x1bURCcGFhdmhvUjJ2R0hZcWc4eEVsOHBEd21oRVJoRERRVG53d0w2eTBjQm40MVUiLCJtYWMiOiIyYmM0NjM3NTZjNTk0OTFmYTQ2NTEyYWEzYzA3ZTY3ODJjNzM1Yjg5YWVhNDkyNWMzZTNlNjUyZjU1ZDQ0ZDUxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlBZNlZxY2RuYTg1SXd1alIxVHV5eEE9PSIsInZhbHVlIjoiR1M2VHFxWVNaOHJKV08vMnVQVm0xSWRnTDNDcmJkTDNkRjlVTWc3anZubHhMTllUaDRFUjFVT290QjdteXBRRU9xbDREWTJ0ZS9Xd1llQkJBb1ZoUEs4WUp6SjN5anhjRHdSNk54Wk9EUVBBNTZOdGFtWFl4RnU2RjF3cnNQQloiLCJtYWMiOiI0YjE0NWMxZjAxOTAxMjI4ZWRmOTVhMTljYzlmNTI1ZmEyNGI0MDcwNTBkZDQ4ZGI2MWUxOTNkZmY3ZDhmYWFiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "GVDMkM9v8TALz4Jqs_ySh.b5mplO9qF7eNuajkSUM48-1792112638-1.2.1.1-DuOcX8tSlLIkJdvZ7bPzUaNvsDRanqD8PDm0pGUcGymf8kSPntU3CLu3Df0JX3OnxAb6nrstUyjy55l77DSVwgZLsEaHHb4611GTVxdJJPTFOQkyXLlstMFBgboedox0lx43k.rP_VcCPDJRfcl4WHsxDQ1rqmHx2vb01dfW7gQmtID6ePIXRqFQwNbPrTz04PWU1LDIXsGi.ZttoF2Y8kEqCUnPb_lDBki3R_CaI1UiEy6iHZqu4smbUq81oxXNT72G.PL7Vxi.Y99cUKP.71QWyeT7TfGG3niKavxGXWD87iqgE5wNDfIelQOcToYZmojUUVsKKWl4Gs3.kYMBSdjkbRSUdruJSUraUJqgO_wg7P9pen.wqCLBg1vPlcJ5Qlp6bU5LEYmt7BQO0YmZelzhqikXB8B5J0xe_jnJ0z.w6q1eB4xqjf4jmLp40o.muXL5gEZ4p5tdR2nGciiFl2.Lw5hVwIE1hSS6jMUBIQPRhnvnQ_bwK.lYgsaSym2Hn_YLN3PfOD10rcFIp1nv6w",
    "XSRF-TOKEN": "eyJpdiI6ImZVMFlnUFRYOG83dmV4VEZXYkpCeWc9PSIsInZhbHVlIjoiNjh6VTRWOWx2TjQzeTdHTG03eUh1NDllQXluSzAwK25uSkNFNWlBMlhKTlRzKzBjdk50TDhnc3Y0cVB6R1Z2UEs2cW15cFpGNGdOZXkvYld4aTM1WUFmejhlSEpXUTQ4TWg3NDRsemhWMXkxcWgrdmk0YkQ5WkNSR0N4bFpmQjIiLCJtYWMiOiI1ODZkZmM3MGZlOTA5MjljMjEyZTFmMGQxNGU4OGE5OGFhZDVmNmE2YWI3OWM4NjVhMWVkZmYwOTIyMGY1NjI3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjNtMnhtWHNTdlY3Y01OOENyNG13Z0E9PSIsInZhbHVlIjoid3BteEVyaUE4OCtEaE92azhGb3k2WSthR3hkUXFRNEVXOXdXR1d6eStXSzRzcnhyeCtzbEpiSTBIelN4VStVbENaYVgwZURucm90WjdHWVlXVi9aTTFHTkd1SlV2NmxFaDc1M2o5RjFod1pYS0YxMTNzUTdUQUJjbVdTblJyTFMiLCJtYWMiOiI4YzBjNzAzNTBmMGZmNTY5MDgyZTJhZWVjY2MzZWRlMWFlMGQ4NmUzOWVjMGNhYTlmZGZlNmRhZTliYzI0YWQ5IiwidGFnIjoiIn0%3D",
}

