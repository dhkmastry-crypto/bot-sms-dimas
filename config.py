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
    "cf_clearance": "XLSpYcT3QTefzIQS.YC5swPV7nU6gjsO9af_1cT_NMg-1791989216-1.2.1.1-cRsK_s.qFqheXtbg0B9xICnp0.BKj0MECh3B4eFLscdawnvothpmaPepX7_OpyaJloUiOy.c1y9HCsQ_uAMBcHgC80FRakVh4YUSMDxBgElTxkNsnJvkZ9QX_aKY9.IYgDDEpqznBO9egn1Ow4begBwTNLDkwlyUXGH6DgewAt2FMBzsiXQ09VI9YB7nF_TqOFpWOeMw16N1o5Hf25C5yRKsEO3I_EgL.S7LQBEXgruPiRAD7pJCn.pbh_bMgipJoiMXYED2ZPWljo7J7fwHvH6ibt4yp_ctcKaKz8p5Nqfvej9vtkIjNmKU9W7CUHzvv4tdhY_fM9cKPQQ3CDPQoBxEdBjafsdr8TrXyqegR4y_oKKy2AZJtBy01B0koVdUo3V_x1o52OpNCEk2HhQhYfojuhDhuIIUO_BwMpNHGWzyDAH09gJn0879WJ69O2L2lu7DWzgIMv.Un3MJG0tTBcImBmUq6VEszVtFq4F.RHhXkiDkCzsdTc0LDsAQ6Jly9NXmGXKO7.oinqdVndljpw",
    "XSRF-TOKEN": "eyJpdiI6IlhXMXhSakdHcHZyUmNQUzdudXozL3c9PSIsInZhbHVlIjoiWVpWeERBcGtONFovWG1XTktBdStsMGI0Z2lqQnlVRUJNYW56a3UxOC8vTERjbVV5aTNRV2N5azZ0eU44VDVta2dlY3VDVXE0MDRTazNMNTJ2VkpwK0lRTUNvNFRsRWd6TGM0YWpGOUxjVWVSVzBYSFdtQ0d0SkdCM0c4V0hvRmEiLCJtYWMiOiJmYjcyZTFmNTdmZjhhOWViYjQ0YTM1MTAyYTI1Zjg3MjM4ZmVjODEyZmZkMGM3NmJkYWZjODQ2Y2Q5YTU5NjRjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imk1UmY1TGtzZDdDWHh1WmJBR1g0M2c9PSIsInZhbHVlIjoieWNpczQ0V25BMEJkZXhraktwTEJGelFieGlVOTNiY0dranJPWWRGZlZNUUJuZTZUakRKcUViRDZielJPbUoxY2N4a1BISisrZFNxb25SclpOWTBTNnh3Zk9RVEpQUnBHYWZoODdYVGgxK09kSTZiTGxjVnM0VWZMb1l2R3dvUUEiLCJtYWMiOiIxNjhiN2M1MzJlNTI5NmFlNjIyNjFhYzM5YWQxNjY2Njc0NWY0NmE1MmNlMzU0ZmU5OGFjZGE4MDc0NWRlYjY1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "W7Lr8_jrm9tLWLOVcaytvVT4JB2oXqLtY8xsEv.MtdQ-1791989281-1.2.1.1-A2wkNZbTVXWOggk07KPalxReM8XmDgN0q.piVNabgLv8iVpL4GtXqqRRZjBtix4ncJABT25QmR_BQRfelyjBgI6WG08L9074iBXI4Hl_c0q.k9NnMCX1Q4Qep7cUTomvMOwLGVRpewHSY1mB0kixWz5.jByYtSHWmH2Dxu_ry3JptvVHPgi5rRhyXSO6p9L8vkm998jS.Po2LIgwRjRG9TJkHS5YHpn8cOuaP0iRQ5BeAvqp1EBsf40T2bjl57dPpb3O61oLZ2SL6pNvCQhVUtSU7oENMI2o4sdbObDxrXgH6QIPJEF6GzVvvmDOCjpGQDx9P.GdUYL.pUNL0XzZ3YznQioyzBJxKsNqVnmOSzeciGXMHVabAQ3nOc3dC5oaED40mvgOeHaZRPLYcmYbnUh41cvRFP7ne7hlUmP2PuhToATyv4b1DdILYD0pHAGejapEU5itIjFNRTjDApdRNj899pVbmwUM2OB3Xxmv1FUvsjJlOVbv6eNx2vFt0Oa6zDp1ChMFgqKyAn1Jvt.xqA",
    "XSRF-TOKEN": "eyJpdiI6ImRzMnF5akpoejNqZE9nR1VKRHpjMkE9PSIsInZhbHVlIjoiT0VoZUZza2RZQkUvaFBxRXY5WTRMejgwVWFWVXdRTVo0Q3Y1bXljbGpmREQwbDhMNU4wdFNwTnZEZ2NwdUIwQ3dwaWd2UndhNWFTVHpFb3RDRThoT2FWM01UWUdPMCtGc21SWTBuYXREZnNubzJvVzVyakV1cVAybnkzblVEUS8iLCJtYWMiOiIyMmNkNzlmYTk1OTU5NTA2NjUxOTA3NGYwNjJmNWZhMWZiODc4ZjM1YzczMzc3YmVlZjJhZWViMmM1ZDc3MTRlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjE1KzhVMWgveG5KSERFd1RpeWdlcUE9PSIsInZhbHVlIjoiVW9iOUxBOVFoSHNXOFdjNzBTdjRxa09sejNTTGlmNnNaM0k0c01ucHUzNGpYaDJRK1JBd3ZsS0FidmxVakhpczB6UmVJZi9BVG51MkpDQVVwUjE0c1B1YThMeUJWT04zVFZWS2RIRHQyVjdQSldhZEdITUhQY1ppdXNERnR3QzgiLCJtYWMiOiIwMjQ5MjYwNTQzNmY3ZDM2NTQxY2IzYmU2ZGJhMjA3N2M4NzBiM2ExNDJjNmZkMDZlNGMwOThkZmNkN2ExYmVlIiwidGFnIjoiIn0%3D",
}

