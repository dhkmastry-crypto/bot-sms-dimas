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
    "cf_clearance": "r5FEMz1nKj1bXrl3k6gQVfK63_aDtLLmYxobX5KCI_8-1791980119-1.2.1.1-hE_xIsENTPs5rpeHmtx46xvZ6pK3HWSnTNNZIb5Gsm2fl.L9NYECIgkj7m3diF9KXYVkLlIQskFHQsax4xI4sAYtRfUvTk20Z2B.T5axW3Hmq7RUbpWmCEO1OhN5GlATpvze0_aPbuXKXDSNV7o0JNn0MgZfSwL0WNDcUH5nPqa.AUG2Mwgx1i9vpLdWhArFDAKIOTfCYpLZL.mbnKd.lq8cnVr_10eFxiJ6Ew1oRlFZXuUBgqyslNvlfvHMPUQtBx.Ywqt.suItaIbthxTzCc_JVDM1h2kjaEQ7SOm6feQKaAF.zfLdVY27RcxGSIci4QA9WCm1leRP8rloXdrnQSNv_Q0jekVMD7u8AONIXml_FTxWBNWVvCYdc7su7H.utQLhZc8cQ5qhPLJoEmdYm75PEyq2ZpNTtLC5pzKuSYXq_KDMc1PMXIceEULpqoVvVzJ4NYXE2t4HyJ.RNwZXxIrVA4p7XWTOpZf27FHgGA2KD38AjITJGEZfZRgCEJHmD0upzTpFbwKTPHhHmef5vA",
    "XSRF-TOKEN": "eyJpdiI6IjloejJrOTJoTWFJc3JFQk1hQTk1dmc9PSIsInZhbHVlIjoiYjNpNUVHSzJLSncwVjRZTnlGNk1zNk00M1FsZjA4cnVhVWZYdWZUNlkycDlRVGJ1K1ljbEszR0VGc0R0SG5HcCtoaUg2Z0dkYm5keVJFRUtOdEExVHRFSk1hK0ZzRjdrZnRqZHNoTUZ5ZzRoendPUTdOWXAzU0xjSStycmYyanoiLCJtYWMiOiJmYjM2MTYxYTVhM2U3MmYxMDQwZDQyMjI2ZjM3MWIxMzNkMzVkOTg5MmZiN2U1MzVmOWU5NzdmZWNhMmM2MDdmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjIxSm9nRERSbVE3WW5pNDFmbUxrbnc9PSIsInZhbHVlIjoid1lONlhnMEVJZy9rb1BlTjhhZC9MVW41V2x6OU1yZU03dVVCR3VydVFMUFlDS0E4STJRMUNVSmdIekEzc2VDWHUrUEVCZ2hwdXFDTWZ1R3lPK0JEUzVJbWxReGJCdE9tMHdVbnNKU3FqSnJNTFZHWXJvTzNvYUFXUkRIaHAwRVIiLCJtYWMiOiIyOTY5MzVmMmU0OGE3N2NiNWQ2ZWVkMGRhMGViYjM2ZGM1ZjQ5M2Q5MDE1NjY1NDAyNTc2MmYwNDUxZmQ1ZmI4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "tozchuVwYF5TkOYytHvne3J8EaATgS02hSdn9h8vECQ-1791980228-1.2.1.1-i18HmiPFpNDu6nPD7HPc39ChExa3y6xl7togATfMHvTdgD6NqeN3qbcbbjZ8SHC24EoqTI.nezj1ojbthpCi52jrg2BJzmLIrSf_3zgSXGTGz5ewjM0pjroIykUftD_j5omXPfI1srjjx1GmMOnkSzluVWBgZsg23UcEYuqnXxNBND2hyZSGeLUBtqQwFzMcQLA9m8XKHghbfDYYy_Ml2CAexqmMvvs_9y4.bikPSPuviHPKuv_NxejRgjVk22o5lJH1ryq_xKVsc08x1UCErH04qQ2_wOLOmGxa1HYWJjS1_jj4VryF1BkhKCi3e2LURhrUh1Pjfp3gkjrulQqC.n0HtVJoFDC36xtkPKxfTSga4nMUGUrBZauEz48pJb.JDktAcsKW418SOiqI_sKtgfcfvJBvGc3OQ35O.daXnM.SeeHBbtV._YeNh5_szpM7MkZEamQTezpNfVQKP4bGFMuUF_PJI4kpolsP9dA1AAT_Su041Cvku8JQ77vgaicChcEQ3aotvmT9aM2JobUg3g",
    "XSRF-TOKEN": "eyJpdiI6InhGakI3b3puTmQvRDZaNmxSZXYwNGc9PSIsInZhbHVlIjoiT2Q2L01CUDVKVWgyUkdUdFlhbUlZdGZzT0djL2doaUoxd1paZ0R4MHJKYzNPT0JiSFJ2M0w1RnNDR1JBOFY4L2tzYkhPN3RPSWZ6T1hLTHdZMzdSZm5hc0U1bGxSMUhlYTlISGR5MkZyU2IvSW1IdllDN3RzWE5IVnN4b2tzUkkiLCJtYWMiOiI0MzdiYzU3YzI2ZTk0Zjc4Yjg2MmE0ZjkyZTEwNGEyZThiZGNlNmJhZjNhZjJlM2EzYTQ4ZjkwZjIzYjQzNTIxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjIvN0VCYlVpZTVNS2I5TEtsWDZSMWc9PSIsInZhbHVlIjoidU0yeFNKQ1ZSSlJaNGhyNXhFa25aZyttUE9vVnQ4V2hzWVdNRG5sdEloTlZMakJCQytqOEU4cU5tei8wNkpWbk9RMEw5VmVIaWNmSlBTRWZSWlJsU3VFdnJrbXRrdk11U1l2bWpPZ1ZCbFNRTkRuSjFhRkhSMkx0VFJ6M0YwdmsiLCJtYWMiOiIxYzM2NjZmNTdmODVkMDMzMmI0ZDMxZDEyNzk1NDQzNDg0MmJlYzQxY2U2MGYzMmFhYTdiZDFhZjI2MWYwYTQzIiwidGFnIjoiIn0%3D",
}

