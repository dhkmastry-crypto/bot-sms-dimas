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
    "cf_clearance": "rZflQVQmhoP9lvywdZW_wjcrSpq81akQV_CC8XfDBBM-1791991021-1.2.1.1-79jhcS3xJKa53SpAMRvjWFIm3MW17poFuNEF3.QxCZ7Z8F1aMpXx_5EloGK1d8oCDOIJew9SBLNiwwU0zzACz1XaK1XhTI30Tm1BmH2Rsc_ql79946U0T_juCRS_uMuEr4_xMY1bNkaZDojKnmFw0irwjcq.pZolOb.WEKEHxAdppDs.LozTjBH.ySRKNTfCVAC5O6WXT3RzjyP.Tx1A9wVPsIHC1oCwW03_WE8O1oWcl59AILwkChrleTU12puTaFgroqTciKk8nPDjrqaAkRL3mYy2LED6giowwfbq7Kl0TGvNLZ661GaToQoZauoVo.IqmyA.MeCU4UOM14t3cPD6d.ilT7TmvZVyRVCFAQhuxFf4cCyGADHdRfpMHkEX8GVRtTfpdwf6e14V7ExF6CN3D7deD.K3rBCp64VJPpQVPM87g5Ez_uHKIqoU50drbVBAJ6ZPRiMtIGrvMldP5erGqGDalR5EclbZThqKEOga76IiR85.CRJOmva1PDLyVTXzgfvvzgybWrRy1oPl6g",
    "XSRF-TOKEN": "eyJpdiI6Ik13SDJ4UUhPSUkzN1hZQ0JYOTZKQmc9PSIsInZhbHVlIjoiT0pMQW1ZTHpmcFpyODR0QU5QSWo4RVltWDVKdm9ML0JaMGxMMTJPbGpiUVJGYU85MmQwN0NnOW8rcnU4ZTZLYndrSm9oeUZYbGVFZDA0VTBIalFFbXM4YWE1SFFjdFU1bGFrV0MzR3FLWURCWWt4WU9sNlg1cENKVUxOQ3BkWUMiLCJtYWMiOiI2MmM0YzM0MmEwMzRkOGM1MzYxYjEzYWM3ZGEzZDc0YTc3MDZjNWU3MzU0MjJiNzU0MDM3NGIxNjllYzViY2RjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVDbTdkYlpJb2hxL0tMaEJtL2gxc0E9PSIsInZhbHVlIjoibWhocWI4QjJmblRjeHJEcnhxL2tVMTVOK3Z0OElQaE1WZWZVWHdCYUFPdWdORWR1bERHdmxiMnBjT2I3TXhQTnBIb3poTDN2QXlqUm1EU2hYNnJ2Q3lzTVRxOU1vQ2ZhenYreWdGUU9zeWNJaEFwa2d3d3JhRHJMNVhSVEZJdmciLCJtYWMiOiJkNmRjYWUzZDRkOTcyZTNjZmY5NjQ5NGNmN2ZlMWE2NTBmNzI0MWU1YTcyNTBkNjZmZGFlYjAzMDM2Mjg0ZDFlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "QHHCRIDicbYIwfZM.Yb6HobYDl1zXUtjSEYnwDh0nMo-1791991095-1.2.1.1-P6kgr9dxv67lAVp0ZmCLV.lu7OFjBeeyZcKGnS823RAC3gQ7D7gApqs9gT29pqfpH9lGykwfJb_H8abQc1K_pl46KGMAIfVlRAOi8h2R9nMEk0JFtGsAIz7MATwhotLJY.QyxM1nn5u.ozUv7kRAh0UB5tNH44Z7Hps0q8mVoXCPxilMGtgRVP1YNuuXQpRXuDMeKpAWCgzo7Z2c04.39..q5XAyXejrREaHP8OgF8X9eB.5WyfsfunfrK8ACT8xSzXBFzrIRuoKgL3guA3abRigrif.tm92..n_vpisU0KSwSfMTaOIIoy2RaGLgsUfmydsXEcAHSn7NH2i.xtIM7binIkd1RXi_qCMPrTepguy.tgaL3n0C8yF.BrJDYOiH9XdEu7wreGfWfh3hOuU6cvHFXodxGvl2VhcT2tpY39WhZXRbD_FmFXJa2._6VuUDDpYru5ryDT3bxRyMAOomQbvdVkyCbyG94RWVfPfUcwmxQdVlT7Ml20osATo9BHkaQmMwCdJT_tUBWekcqT7qg",
    "XSRF-TOKEN": "eyJpdiI6IjhjVzkvOTF5Uk01ZTltdTZBYlFFcnc9PSIsInZhbHVlIjoibkt3NCszc3M4VFkxdGMrM1hqQ0J4WVVQeHl2V0lQdWtOcUo4NjU5clZ6MGJVcGt5VDFLQ00zU3IzOVZueVRWc0l3TFJnRm43OTlJN2EwWEdqemthSHV1SFB4Y3B3eDU2a1kwNnRkcC93U0RzZmtlMFphdkZqbkhROVEwbG9vQ3giLCJtYWMiOiI4MTkyYzczZTY5NGVmZTllMTJmODMzNTQ2NWYxZTU1NTVhZDJlODNkMjUzM2U4MDIxOGRlMWVlOTc2N2ZlN2YxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkphY09SZ3dYa3JjbUI1VTJ5NmJqSkE9PSIsInZhbHVlIjoiTEkxVFNOa29oeFlLSnBOSjRWYzI5Q1NqK3h3ZWluZ056Mm1LampxSTg0dnJtakUrd0taT2hjZGVhYlN3R3dmVU9OZFVEeWFGY2h5a2tBb0lHZGlTZ2FLTVBiMTlPWU1aSS9PVUpCaEtGcEQvMjVyWXA3YjFzMDVoZ3dtNmpuRXgiLCJtYWMiOiI5M2E0NGU3ZTI5NzVjZTAwYzNiNjBkMmRlZjkyNWQ2MjFiZGVkYzFhZTU1NzQ0NjgzNjYxOTkwYTczZjczNTY4IiwidGFnIjoiIn0%3D",
}

