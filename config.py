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
    "cf_clearance": "156hPmBE81pesehyZTO9o.qUbAynd.iwYkUBKMW3FsU-1792006554-1.2.1.1-f6TNYhV9JN1b3VcxvIi4z7ckWI5ucSfSB.kI30wyt4Br1g7SNYYEC4tr8L.bawj_jzNXiUHtnKetpLehqfT7LpSnur_kAlwq2u32zI.wwoa0y.6DapyOSFrth5_XirBiIqyW3AYuDuN7K4pNKw0VrXTnN3bjusg9iUmhwPS17o08XW9.niL7Rk7dc8MS.7med3FpHfy2O06O6cn_cwRRjqJwkpCoK...7wIaptcmcZtP_wYYcSizAKTvQqRhBS2XUKJ6xh_6bBhI6AS1zIi4EBhJtFXvr32kKuf0zEyBmfbJNdzp9w6_7TK7McxOtMV.EkTJvznOhm3Hotc7uBFCIR.kzLb7lbk.czp_j1u19vbhDjOqIbc7nuHAC8gmANm_B4TUBaIvLY30k0YsRr4TXvS.2v7bwfER68iKDKDL7LAjqbk.VHCkRzVsfy1lQJNssOsaZEPV0AN_ogYjiwoeoMQoiDYDZ6bR.KMTnm2fFwvS7I7Gc0sq.XO6qcM1aKx5nqAubpM3rl2_C5Rj7CYn.g",
    "XSRF-TOKEN": "eyJpdiI6InVlcVZzbDVGOU82OFpUbFU0c01OWkE9PSIsInZhbHVlIjoidzQxMFJRZFVLQmJ1Tm1zTXVjV1RsNnpDVXRjRmo4N1ZWVEVWdk9RMXZjTURGQU4xRDN3b1RSbEFERnhXVUdlNERKM2VQM3BrU21kKzgwT3lKeGF6VmF0azdHS2M4L212K2NxRkpFMXkzTnlvODRIQlJUYUFxcmM3cUVLR0VFdnoiLCJtYWMiOiI3NDQzZjBjN2U3YjI5ODk5ODc5MzFhNTExNmI0NTdlMzc0ODRjN2U5ZmE2ZTkwYjQ1MmEyZmU4MDlkNjljZjBiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9PcDBtM2NqVHl0bWhZbXRySzhWMGc9PSIsInZhbHVlIjoiOFhkNWlpVUdxL0ZVNlZkaXl6d3Vta2tNQlpkdG9NYVVYVnZQMjBnMkRGc2E5SmFSTkFEZWxiT3FNTE5CUENCT3JlbTBJeU03YmlmTEhrRVVoUW9FUXBQWHJaTGZ3QjBxT0ZNblhVTnVJYm1idW93YUVkV0JDQXdvY3hrVGtTbkwiLCJtYWMiOiJiN2RhZWI3YTZlM2QyNjc5ODBhMzY3Nzk1MTAxMGUyZTgyYzUyYzdhNmQ4NmM2MWZkODk3OTQyMzU3NWJiNGI3IiwidGFnIjoiIn0%3D",
}

