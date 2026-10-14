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
    "cf_chl_rc_ni": "1",
    "cf_clearance": "tygeW5B6zwHBXF4h3fZ0J2Vk4mowtR0HKiW.QnTL3.8-1792010173-1.2.1.1-3APM5ubQOYgWYHbPqCfdFaPUP7oobH.8NIVDCvktswaRCZpjvCa6U5S_FY0JMUt9FMn.wzIOUv02FByKD_uo4AKVT1S9TFSMuhagr12T2LtkelDuka1216qnKBr2w_8aFPLCbIedSXe0FlzQ5uoabAVx1T3QySzUtcgkD9h9bIq4kiZLSTnTxz6dLO6ETjDTH4bfQcMXUMo8VZO_qR_YWulcQhXSSy9EcyiKVI0NkOMOuZ68ejZV_l0Hp8JU2M3xel9UEVpxDhF_EZEcMHJhnHUHNduBi8m_fHnKXv_erILxaQaEdBfOQ7rtzEHsIsSVLU.GLCiAsHwBnsS7Qx8Cl4NVhVjlOgwLD7vVvLrUgIICtFrWogKgxGVRxUQ7l44HHA7h0QBYs06vcJYQTl2o1n3rFE4Qhn2eZZdnt2kKibGpMqID5DzLvCOowaz8FSHV.X_pMRENYXQFvukTz9Ak1Rg_RZifvGosIAYGMDuEgVTRE4yTuKVlt.hwFftjzUeRaOobK5TjQijP_jPxJfWVIw",
    "XSRF-TOKEN": "eyJpdiI6ImppeE16Y21NVWMxbmdqdTltcHFnT0E9PSIsInZhbHVlIjoiQmpXVVdKanZjSy9UcW1VVGJDV1hHVTVYQ1p3Q3ZNSVpDWjUrRmZjaStnWk8rSTUyaWhac3N4bEhXR3JKN1VyK3hIVG9XUlJhQUxFUXhBMDRPcE8vQytOanQ5YjVkWDZJSVEzeWYrWGVzaktOTjdDWHZnU2hsVUo0NXFtOUZ0YVMiLCJtYWMiOiIyMmExYTA0Njc0NmRmM2M2NDk5NDE4MTBlNjBkMDczNWQ1MTRjYmEzN2FhNzk4MDdjZTA4NTM0M2M2YTAzZDM0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlJsa1pSL3E0NmV0V0FZL3JkQVVQRlE9PSIsInZhbHVlIjoiMzk0ZzBBZFB1bUdMRlExWDY4SFVXVFF6RmNzS2E3cU1qbU94NC9oc2hwTCtTRGxqMW4xSDIwdmJYSjhZRWpNTm1BZUZnSENGbVFqN25hVzZOc3U1R1pCcjdGYk5FRmpiZUFpTEJjS0E3ZmRBaVM1cWI1TUxFRHdyV2JSbDBQa0QiLCJtYWMiOiIyZTlhMmY0NTdhMTBlNWZmNzRkODMyNDA3ZTE5ZGQ1YjE2MDU2NmFiNjEzMmMwMDc4OWI2OWJkYjFiOGZiMGE2IiwidGFnIjoiIn0%3D",
}

