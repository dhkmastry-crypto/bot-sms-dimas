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
    "cf_clearance": "Ln3US27GP1Sl8Os.TJrhQqU76_QpJIyJDiKPGgNXcUk-1792007112-1.2.1.1-h4aWk15A.urIoh.nnSc9xFhJjst6dbgFKNS0wtJHsq9CSc9JRIUhF_OXluaRNH_PLLPhoS5Trroezx2LfRLTmO2W9TuaPWKLcVQrmmcVQhqtrZXOrntzMJh78v2bAy3evzPFDiB9Rm.qmJMATHy1VogE8XBN5imPfeCrJlTW4UFKKIyw51kpH94B1awC8RdVbEYncWNLKA2Nmm4swu2xJqx05a_fsZ8uEj3RBQlDlLC4MPNl.izMaZdnQY3pkSrHCQCqS0u8HttqO9Ml64LYybnBWO3rQhGOy_eQVu9wI45W.pTN6n5zKfu5FxAsv5u0c81eqz2P6V.zg0Bt_jh7FYUnqR7crUsyo29k2WQVGOzDOrbcbjIAvnF_u8gw7f9NNNNPaZewETojkPbHN7.hQ27zjwS2BFwP09bB9mNSnJ6whUZr6yTqQg25jBauf.8Z9VQpDtMMYVBoy6Lyq7.Pm3eVSjiPrdYsvOx4lA9VeZTFg9Rdv.1ZIfMtRuuNLWY0Rox74LSWqjD5ubsk0PFebQ",
    "cf_chl_rc_ni": "1",
    "XSRF-TOKEN": "eyJpdiI6ImtHcW56a29Dc0tITzZDS3k3NlRxYWc9PSIsInZhbHVlIjoiRDFRNU1LaGtSdWFJQ0VuWEs4U2RVTC91cjBzQXhDNVhsUGZpeEhyZmlyVVIxSFhNbmtheWh5UFJUMGs1V0wrU3czWkxRbHpTajVjUmd1a2NzaHFwdXlQVVRldCswZXB5QXhjc3h5S2FWMzdVRUpMc0N6Qm44Y1k4YzBzZFQvVG0iLCJtYWMiOiJhZjU3YjZhYjA4MjMxNmVhZWM0YjFjZTc5YmNmODMxNTBmNmZkZTVmZmVmM2U3NWNiMDE4MmNkYjA4OTI2NWUwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFVYTlrRXY2VnVnSzBVYnBzQTdEaUE9PSIsInZhbHVlIjoiWTNmWGozb0tBMnAxN1ptcTg1WXZoenRUTkFLNTl1bUJmams2dndBTi9HcTlHWWdzSnVzTmsxbDFpSVdZS05CaklqZUk4OWpGWnBhT0lkTjB0OUEvNUY2cGZCKzB4aWNuZHRLM0dMbXhCVkhOaXVMMDhPMmxYQUdMMVBVV2p0T00iLCJtYWMiOiJkZWFhY2RkM2U2MzM4N2I3NzMyZTAwNTViMDc4NjVhODA3MDQ3YTc3MzAyMTQ2NzE2YjVkYTY3YTkwYzkzMDAxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "3rO1qcn4JQB2oKFvXsnHI0vCCwIz7d3cGQoWekzfKLM-1792007407-1.2.1.1-AsH0TagBsg88i7BtNAyEHWR.Pxi.AVhP9hdnlySDpqXW3RI4tbCGP_RCgJPkxpt_jphxgJpKywt9i8AsSco.vLmjzNstamoJi1ppHwWFaYpXDANWrfeVHKItYddo3ozGCIAbS9t1JJ3_n_eWZgwQb51bgY8f.sFn6uh1ZwncReMZdwLbtDnVPwm8mq41kgwoOVr61tQrO5yTPaCznrqWQEQT09IkmdUw9Fqu7DdizKcBiIiK37zOURzqczrtvcbdqXfOa79KBvAvCHnZR_ZFH0t6884PACtdU15d8hNDRH5pfrNZ1OI7RCbuuOdZAqzmCSoJloeyPYUHeahLITb5yx4..CTeNmq5J4c9Khv7s0Ga8jQLQTS6OsBgeq.p7M7gIZn35UAZlFBmpJ1XnpiK7MM4VGnsdPKVBuv0fFMSNBq_2xSt4WLfyfwRun92j.TPCDCksiwUfjcwvtfaxI7PNLkkHaPju_qIcYWVqobz9vUP7vBp_468HOFZ5l4BeRn3m6rprw44NKPj6YDCWz15Hg",
    "cf_chl_rc_ni": "1",
    "XSRF-TOKEN": "eyJpdiI6Ik1OdWtuMEF2UTBJSmpPaUladDFpdEE9PSIsInZhbHVlIjoiMElma3J2YVFDYlBDaU5MZXJ4eWhDSEIwN2ZzSnJCM2ZqZC9iVHVrSFcxdlVkeG0rUHpKb1FNQXozY1BSRis0bGVLT0JZdUM1M0dMT25hNXhEd2JRdDFvSmJLVENzZUVJM1gySXY4emYzZWg2cTlBRXVJQkpiK3l5RGN3ZkxrZGkiLCJtYWMiOiJiYTcxZDIyNmVhZjJiNzhiMzFlMDIxN2YxYTVlYTM5NGMxYjJkZDg0ZTYzMjYxMDAzZmU4NzNmOTczNjJkMjQ0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkZzZTVTQ2hzZVRlamt6K3dFZnpHV2c9PSIsInZhbHVlIjoiS1NNY2pjUTl4MGZqaDFxalZyMityRjNjamNObnk1Q08rdldaS0hMS29iM0NCN0R4U0NOOHpnV014Z2NUTWhwZmVBQ09HQlhLVy96dzZUV1BMZ1E4eTlBMjBkRlc1a1dDM04vVGcvNUlSaUFRS255S2NmVmxzYkVkUEZQd01LMjgiLCJtYWMiOiI5NzUyYzZkMmFiNDNlMmRlMWZkYzZiOWU4NWM2MDZhYjVlZWNmZTc4YWM5MDY3ZWFmOWQ5NjdjMmMwODY2MmY1IiwidGFnIjoiIn0%3D",
}

