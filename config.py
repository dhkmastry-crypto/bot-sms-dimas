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
    "cf_clearance": "9QRzv8r4Clcv4NBvNs3n_fbdxrMVKzxAXo38LO9RNFc-1792067341-1.2.1.1-2OOlvVrDMxQeNacmKjSDYm_rS8UDTPRsLdzZ_i8wSENV6Xcx9aMF2C0P9iAYY2qo.Vit4_XUUnH2oKf6iAelgD2TIQzzqxQ4QY_sB8KuVLRo84s6w3YrHlaw8rv_bFamc.uBYXaem6GlKhT3zCRQHuLFBk3t3dyHL1M6uhUmdWoHgkT5qXgo6051aRu1U.anuW1bECskF._wzO17m85ofnvBrz5cHwr76IogspkaIKK.3XqMdhCpR9bp3LaXQ3Jzm1R.wVV3RdRA5p.FKuQT9V4U98faIRgqAGs64VPbQcSCzixLSEU235P5Dvf5L4IHMBKAgQtJtrRbI4.zgRJAqWIR0MKGTrGYKYOXdQ6M9gbbkQF4ptt_EbrrVRmPF57puw_FQIAaJcf1Kl3g0VCcns9MNWdeP2fFivqG4yadajpd_.u2s79NPxa1I1ISIIS5TwbHEGL2pi1IvB1A4urxr9OL.za6kZMY9EKoVYNIw962u9n3GKOL11yEqVw82g1tvtyMDNhZ61AgGMIBZeMAUg",
    "XSRF-TOKEN": "eyJpdiI6IjV2Ry9raW9jRC9DL3l6RG9Wak1rS2c9PSIsInZhbHVlIjoiT3pyeTZlREcwMEVVSC90cTlJaHNDcHZoQlgxVzlvdTZIZGE4WUcya001dzVNS1Zhc09kNlhqWU1uQWREaDRZVTFneGtYWnJhTS80dFFDZG1LTzRzRXRwK09yNWxKdVZBVGRPdUF4L3IxcWVYRXZXSUl6ajhhT1VweHEwblVnbXkiLCJtYWMiOiI1YzMzMDljNzIxY2E2ZTFmNTJkYjUzYzdhODU0NzI3MzNkY2M0OTRiNDUwZWZjOGU5ZTY5OTdjNzVkOWE5MWFjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkNCaDBFSjE5UTVXUWJNMFl3WTBpRXc9PSIsInZhbHVlIjoiVXlDUjZxUGNzS1Z4NU1tak14QXpDT2lBcnBPL00vQnlzMTNUbU1tdnc1V1hqQ2ZXUkNBdDlTUTlrUW9CV1BicEpaOVM5QTVBZkFFNVFHbEMvYkxBdzJTZnhQUThzZ2Y4M0hYQmwvbktrWnFNRHBHSUUwZ2ZZZUh1SUc0TlpVYjgiLCJtYWMiOiIwN2RjNTgzZTEzNDE1MmZjN2MyZTFkYmE0NGVhOTQ5MmUzMDE5Mjk3OTFiMTQwYjUyMGZhNzdmYTE4N2U0OWI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "KH.0gQ4jJYkHICPLIgprDFtx5k_lv_hDUT9B8T_vyz0-1792069105-1.2.1.1-Xswy3sVteR6cBxtYnKQv8jUh_IIqcFKBLGHdjXeXF2FoBnrT6B4lMD0LayltY4Z4.TllDPR1POdtGzA5ODeCIIQAhUkxZ9qnIfiUaq1rD5xmLOiaWdf5hD4op6h9g5m_FiWo3JAR6z31JpEDVB3cAMSwkPlDSPXmgTrv9LlWk0cSgQ4c5DPsvrIhUUrU9Kw9eQPJClSReYEB6c2TksBpDxxqJt5qQDKp088Ei2_g1_bVDo3eJT7DIEI.Tbq7pqur6yKVzjM2wrRgAblmjGxwxHrKpx5yqIQ8E1nYCVFqB.8MgOZIn2t6BKb.4JGK6FCn5VRPeHJhZVgacFuxT7ObGOH4L7cGNes_.hbDwj1SzOXyg62b5sfGqYmBo3JXsWpRMYAzhZnS.Gv.ElHWq5bzd6eMZXxtscOfnGJLZmN2cejvKvbmbjdBpcvOrYB33r5WhiB64l9txiA2AFC04MH9UYbK.n2Lfj.k8lV46ErxTbB0VchNgREHTEhjnZLm7oKYrVEoG69qx9Uu7ObyT3i5hg",
    "XSRF-TOKEN": "eyJpdiI6InprVGsyUVE4dkMycXZCMWxEN25LUHc9PSIsInZhbHVlIjoidVNZekVJWTFiYWxidjl0Q3ZPMlRPNGhwWm1jU1lSWk5Jc3AvUWdNaUpHTis1YXhlUnRUZEQ3MFJyVFJZQ0l2b3RTTnY1Y2l4ZkpxMzlCL1ZhNkcwTWpaaU5wZlhqWkhpRW50MEZqNjAzcTZBRm0zMlUzc0EwZTBFVXMzNHBoc2oiLCJtYWMiOiJkYzYyNzE3MzE5N2I1ODc1MTU5NjIxYjI5NTU4NjYyZTliNzc5OTA4YTVhYzZlMDJjOTAwMDhhOTZkOGNjZTk3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlQxL0RJM2hONVFGenBoSzRDelhJQnc9PSIsInZhbHVlIjoiV0g5bnZVaHpIeW1HYUFHajM1US82VG1VcERYVzdBdk0yY1VEV0tmQWJaTHgrVGVxMGFuVFV3UUduV2haQ0pZcWo1cFYrejRxemJDUHY2ZHFOVGxGdjBaOGN3QitQdnBmcHdNdkdDUmlRYjlCMGY1czBQREcvM2JYREdWNDlQdkIiLCJtYWMiOiJmMTJhZjgwODUwMGM2ZjFhYzE1NGVlODM5Nzk5MmZmNDFiNGRlZTQ0ZTI1OWZjMWI1YzIyMDY2Y2RjMjk1YzVmIiwidGFnIjoiIn0%3D",
}

