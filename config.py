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
    "cf_chl_rc_ni": "1",
    "cf_clearance": "TKyHak31wQ42cLXPqwu1jsLaarvPxEUWkDpQlN1Vytw-1792010205-1.2.1.1-dnlt1uTBBLttKWXxrV9rceePt1EEGBK7WXi6QNtYkwRdJ89kdO.Z.T28HP7Ra1GmNL1P06JhRh5_7bwcWqd6xJxf0U3j4Wv2RIWPRkjnBDgums1Uae5G6hDlq7ESW.BLgJGSY.9CaFbnIl6zm3sgRU6eVqHiApsmuO9zdocv9IP9_FrJ4MXGzVzdS7Df.GFr44OECSTstl7RDkddWGP_EgjINnsARAC2CbYwLsrZPVyBwAmIedbudrB5YhFdeb8SFSjDxgt6LJHoTAc5RAOqvcGXu9QAiad3XhrUXF7bmlbKnnyeaTHWdg.R3KALOoyrpoVp6ry8IO.YFyjoT2TXebvnb4TefBYe1p6QmrKAFDN9U6n72sxs2oD.gWL56GQKsgdGySaZR.HRsogjH2tcAJqyzTAQo5WeL1oI1rfPNh6m4Xm9ZQ4He3bC4BYlJWcsaIPzAykwqvshTVZW3JEI0Ozol.BearHd45S1vrZ__TMd67R3XWMtU.2DNxD5T1pCCUat3_4mwGhPpCAxJv.SCQ",
    "XSRF-TOKEN": "eyJpdiI6InNjQlFMd0RsWEdwUmNzaXhVdEVUdFE9PSIsInZhbHVlIjoiVVgvZXc4azNESmVwNFlyd0o3by9UVldQUXVETmJubHUrVU9QN1E1THFQUXFuNVdVOGxtRVNNZkJNMzlEZFhjVlpacjl2VEY2ajdwRFk2RzRZNHZmbVN3QkpISVE4YWZ2OFQ5cml5VjdhSUd4K3I3K28xNlpwelNuVWltUEdXYVEiLCJtYWMiOiI4YjRhN2YzNjYyMWVjODIxOTc3Mzg4MzBjMjU1ZTU5NDYwOWU3MzZjYjJkNmNjMzY5NzRhNjExNzAyZWM0YTIyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InJDV1MwUGRmYzI5RWU3aHNoTmpCemc9PSIsInZhbHVlIjoiNHdSTzExNzlIZ2tTVVF2djlob0lxMkVnaHE5dDJnbTM1MEpUU3ZmVlpjUDVTV0NNZ2t4cTVsZEd3eTd5UTVSaDljRUE4SzQrdVVjdjBnQ0t6YTJ2ZVhUYkRYMTF2V1dkNDZlNDFmc0xrb2FlOXBiTWE4UzBNMmdYbGdwVHF6K2QiLCJtYWMiOiJhMTk2MjNmYTNmY2MwYjMyZmY1NmZkYWYyMzk2MDBiMzQ2ZDA4Y2E1ZTMzNTVjMmQyMDg5MzRkN2E0YTE4ODNiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "VaNCDCzkq4OqOQavoEDcAJ6gowUjYdwXDjW2pV0_2pI-1792011978-1.2.1.1-8S0rjPnSxuPJEdc4g6t_bjniy166FuY88rnu1o82F0ZrDr7VDhgK55oNJL09bRwSVMqxUeEDVFkgviXwX.ARbNK6tO5kR.VhfNcuqHBh2KWzDOXb6VKXOdmnUIh_0pITagucJF_GYxbmm_d0pIzt4mjnhQLOlKK5dDx9kI.pvHlp..SyLaQqDHKZVCBPBAGOSYQ8SuQ1D2a5YEMqNfH1X2cabyx7GcucJIeq5vtHFmIaSXLHHAzq7ZHloXepDt7a0.UDy.h53W1I0s6h0ROEqcpNVCzuBUsPTsJxdPWf0p1lDi5_mLWRzmRanKirwYnDMpHigaZvH8mt5PR3blHkFww2Do3BtKEwdRvwV_A6U70pEiM3qDZHDUH6NH2k_qdchOepxqb.QhqBcew4w4CANPd4u7mbU3X6eWha5bGGWXUuOBrs6glmW5WJ9zAfyACT6r9vb0moUlsI.nkc4NbMhCVBTI8j2I.HC..U2RCLacnlBgokE6otwy7tT0g1ywjLGVSDzzd8NRlLNYSRmVTvRw",
    "XSRF-TOKEN": "eyJpdiI6Im8xK3lzbUc0cjVvZzBraW5pekQyUVE9PSIsInZhbHVlIjoiRWhoOWZaODVuR2xQc0pMT1c5WFRqZXVOamlCQkx1eWpXSjhHNGVUbERhOHAyN0t1bjZ5azE1dWdNcy9NL1lZbGllY0Y0UzBsMklqYjAxNEdrNTNOL3VpNklHbmJqUVdBNTZrU0RFYlpPQUVaV3luMTVScXlIQjl5OHUrVXFnd3YiLCJtYWMiOiI2MzA2YzdjYzYzNmYzOGQyOGNhMzFkZDUxOWU0MzU2YjVhYThmMGEyZjIwMGNiNmVhMmNiN2RhYzljNGRhMTEwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkYzWGpYY3htbEJHNTlJclVXWjdOV1E9PSIsInZhbHVlIjoiS3A1M0Vjc0JsczJycG5NYXBDL1NxRHl4RGJaZmVyeDk3WXlUSytaUi9KQjJJMjBvR25hZ21mSkttWm52MmhJSkgwYTUxQWpqUDRnQk1OWXFNTDgvd25UYTB0aHgrUnhJOXVQZjA4RXdMVkRhamxMbmFCSEdJODFvdGJLZDFtZFIiLCJtYWMiOiJjMWVlYzVhMzNkNDI3YjA3MGQxMzUyZjgzYTYwMGM5MzRmNzM2NjZjOWFiNDlmZWJhYzFhZGU1OTQwMTUyOWVlIiwidGFnIjoiIn0%3D",
}

