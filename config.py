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
    "cf_clearance": "awrUAO2StZqHRmeVDgrn7By00WtqLJjNDOF8AQzT_p8-1792012011-1.2.1.1-p_gfUhxZlVLgtmGRF8DriKFBu.40KsMKaEdakXFwnB0bJXQcIgoYo2oPXgUftxxsQQuS11.B_nipnsp6.EQs0yUyzFaunLJNu8cQO9yRWBIlp9uFdJX2wq6eRqTcZVgb0g.OpkJctysmW3dWBQZH8SeIkOV8xQVpxtwIh903unziDSNBpu7NO4Jc1LYzRQnp3ovgwqg8Omf2J.M4ubQo9vfMCncaqFGTwwIi8.2yCATCFFi5wn9QorUTE3nwvXKv5EEzsfd2kuMAHFPru1mWDSKUVL2Slo1GhLPdJBC8kMLjRMsuFhJnDdEqztc8LkT0HSmx6up9gNZwL.dqTcnC.gHF49KpjqK2lvETkFID.I1yl2PwdIUiFPymdPD6RUpWe1WDECOQeMERXNFI0fQh1lHdWPGcl0Mm57TXqvUD2NrAvMrEkGt4zK2wHo3hhdgwgFIFUkMKPD.cdfU3iOGKbFcraFEI7reZ9kAiZB_1491KW_276aI0AdZX1RD6bTsTEnxWf63uM6uas7YWaSQjMA",
    "XSRF-TOKEN": "eyJpdiI6ImY1R0lLL29pdmw0U2VRWFhRRzJ5VHc9PSIsInZhbHVlIjoidXREQXdiSFF3N1dMQmVCdmxzekU4NjFIYVZnSEpPK0E2dkpqQUFmSjhHeTlHS0ZjWk9BbUhLM0ErV21va28wNldLdDQ5dStRR3o1RGhsL0dwRnlyVTl1S1lhM09ya0pHNStHZUlVbTUvT3gzakNHcjRWUjZYWDlEMlhzbEJ4U2UiLCJtYWMiOiI1ZDUyODFiYTgyYzE5OTUxODQ1MTQyZTAyN2JmNmM1NWJhYTQ1OWJiOWZhNTRhNTU1Y2YzOGVkMzU1M2MxMGFkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlR3aFNGdzd5S21WdHNtOXNsNWdtbEE9PSIsInZhbHVlIjoiR1BGV1hIZmFWczNPNFdrQ0NjcXBPY0lGNExsWVJMQjZtWGp1cVhCcmc5ZTlLWkYvMkxpemlsQ2VUc3ROMThzT1dCbjVjTlhNeTYvMHgxanQ2aWRsWFpyUVByT0xZT2RueWNOeEtBejl1azBwSnNyWnozQTAyOGFnN1I2OWZhQnciLCJtYWMiOiJhZDUyZDAxYjJmNDkyYmY3YjMxYTczOTZhN2QwZmE1ODg0ODRiNTczMjY3M2RhOWNlMjU0OTYwMzJkZDE1ZGU4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "VaNCDCzkq4OqOQavoEDcAJ6gowUjYdwXDjW2pV0_2pI-1792011978-1.2.1.1-8S0rjPnSxuPJEdc4g6t_bjniy166FuY88rnu1o82F0ZrDr7VDhgK55oNJL09bRwSVMqxUeEDVFkgviXwX.ARbNK6tO5kR.VhfNcuqHBh2KWzDOXb6VKXOdmnUIh_0pITagucJF_GYxbmm_d0pIzt4mjnhQLOlKK5dDx9kI.pvHlp..SyLaQqDHKZVCBPBAGOSYQ8SuQ1D2a5YEMqNfH1X2cabyx7GcucJIeq5vtHFmIaSXLHHAzq7ZHloXepDt7a0.UDy.h53W1I0s6h0ROEqcpNVCzuBUsPTsJxdPWf0p1lDi5_mLWRzmRanKirwYnDMpHigaZvH8mt5PR3blHkFww2Do3BtKEwdRvwV_A6U70pEiM3qDZHDUH6NH2k_qdchOepxqb.QhqBcew4w4CANPd4u7mbU3X6eWha5bGGWXUuOBrs6glmW5WJ9zAfyACT6r9vb0moUlsI.nkc4NbMhCVBTI8j2I.HC..U2RCLacnlBgokE6otwy7tT0g1ywjLGVSDzzd8NRlLNYSRmVTvRw",
    "XSRF-TOKEN": "eyJpdiI6Im8xK3lzbUc0cjVvZzBraW5pekQyUVE9PSIsInZhbHVlIjoiRWhoOWZaODVuR2xQc0pMT1c5WFRqZXVOamlCQkx1eWpXSjhHNGVUbERhOHAyN0t1bjZ5azE1dWdNcy9NL1lZbGllY0Y0UzBsMklqYjAxNEdrNTNOL3VpNklHbmJqUVdBNTZrU0RFYlpPQUVaV3luMTVScXlIQjl5OHUrVXFnd3YiLCJtYWMiOiI2MzA2YzdjYzYzNmYzOGQyOGNhMzFkZDUxOWU0MzU2YjVhYThmMGEyZjIwMGNiNmVhMmNiN2RhYzljNGRhMTEwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkYzWGpYY3htbEJHNTlJclVXWjdOV1E9PSIsInZhbHVlIjoiS3A1M0Vjc0JsczJycG5NYXBDL1NxRHl4RGJaZmVyeDk3WXlUSytaUi9KQjJJMjBvR25hZ21mSkttWm52MmhJSkgwYTUxQWpqUDRnQk1OWXFNTDgvd25UYTB0aHgrUnhJOXVQZjA4RXdMVkRhamxMbmFCSEdJODFvdGJLZDFtZFIiLCJtYWMiOiJjMWVlYzVhMzNkNDI3YjA3MGQxMzUyZjgzYTYwMGM5MzRmNzM2NjZjOWFiNDlmZWJhYzFhZGU1OTQwMTUyOWVlIiwidGFnIjoiIn0%3D",
}

