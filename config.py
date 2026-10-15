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
    "cf_clearance": "_Gep77.lxjdfyEQANvN_ENWRSNi.cO.oaXsLwDIU30Q-1792047468-1.2.1.1-37Zcw.O5iipIUXGhmDPp82lS_bCmJP1a1ASqsUkzB9.kf_P53v.Glpz93xdiWYLWmJW9IWFyZaMiePY1O.X6ZORekO3T_XybUL2kVoxMCaO9FnOVa09MrvpP6cfeiY3lnkXbYJSAQY375kDmSXGfPJZvsDLXZM7lcqjevE2LJupvPwhwYAyp2zFit67w5q6tpxtZUL4vPXYQj5uyDT74kcL9PBXTxF6il4q5XvShtuWCGbEht5IU5mcmTTW0V2vefP.DVqQ06G_QUByJG7z3qZneuOxPR.lBASXDRLuqk4P7Qdg_IoqlxNkckBAME6uLxAzHudxTqKM8oyrEHFee0mggO1ban1dpTR7Zthnu2kRb62WmIiq4TIHSGOTKQM.my9orbzXdiKXXEQiCZFNBiP2dXqB1qCquG_3aqleqn1arHcnzsbfA8BHHCEQalwwQ1KhSHCSuj7KoKSbStb9zJ7zLD3P8sQCEPgNfSb08rz31iTW01TpDfcyjKTejFyMJDT52PNJq7ea3iE4Q0R1mGQ",
    "XSRF-TOKEN": "eyJpdiI6ImZZdHNSRFdZV1NwZVJtY1dHbzBXa3c9PSIsInZhbHVlIjoiWlR1dlh5eWN2Q2liQ2VENHhwV3FXM0FHaUQyV1hJRHN4SDVWbjRlVld6OUZSOHhTaDhOUWVLSUZuN2N4aGJRcmRvMlpiOElMbWxpOElPbmJXVVBjQUI4ZUtES3hMS0V5cmVWaHdSQy9ST29NVFJNYjZtYXUweklXZFNLTnRhMkciLCJtYWMiOiJhNjRjYzhlNThmODk1MGIyZDg0NzdjNGM1NmFkNDAzMTg0YWYyZTcyZTdjOTM4ODE5NmQ2YzU0ODQwYjMyOGE3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlFLdWRGbithZ1JlNldrQXEvaGplTGc9PSIsInZhbHVlIjoidnJJMzUrK0VuY1VXN2NnWXIzMkhRYkdhUXpXMVJPMDJTM0VYUy9nMWQ1QTdNWkV0M0pNN3ZRYWNvclMrZFhkNUtVRG9PbytvRU9yTjJnVVNNbXRudldHQVdqakJucWp3Nm1FVWZ1RmZQUkpmS2VJUFlFdmJqMWxDRW5zQ2JmVlMiLCJtYWMiOiJlNGM0ZTY4NTI2MzE1NThjMjYwNWJkZDhkMjZlNzdmM2RkYThmNWQ3Yzc2MzExNjljODhkNzVkYjk2MDQ4MjRmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "kFe6f33.klbTmhaa0tuURKbbjM6YGGsEdGDQt7NY.ew-1792047425-1.2.1.1-oOIab3nVSheZUQtkxXvVLLoADyKtP_PPy5Y2wjOdvLmqjhrIKXWTqPpBylWg2kjFNxaX9v_2xhY1uvKKbzG6E0I6n_6R.dxhXWjzQAkZSxBHm8aPb4cGArBMrkWJpwfXY1WpAE5oDn59x21YfOsaHIvMkXnt3AKVdAEleftZGkpinug2FXdp8bQCxa2nhWUNKhyrs6d1K5OXT2LUBncS9VKuoixtjxTCmtAvEpGnt1ln97JTfGiK8GQF2hSh_TsYrRO8o3T8vE0nUVd4BXSriAxYVcukK_EA4R4RvtCWcxuQb8YJT7cpsbDfxQGGPMVqPfwptMXtWp_7HvenS.dabBbSGD4Xd7DFEWOk4EBGytHjI9cBn6ZboPJs0rDHaTeqABqyXLydPlSky6GT44XGGOReEAdqNpAdfi5oPLlmAC.UsK50cXkRIid9BS599MKj_q1VVwhBPWdoRai33zPThf7UyIiY5r8zkB7Z4QrSLEAHix1c5WyMgalz.Xd7kKk1EFxgVrriQMALtQiZH_L31Q",
    "XSRF-TOKEN": "eyJpdiI6InBNTlJmNW9nNk1jNVJ1Y2REeHhZV2c9PSIsInZhbHVlIjoiTU9rdXIwZkwxRGp1SW5KZDhDczFESTVpZ3lYUnorTUEreWNUOFArYU8ySU9iY3FBTlRWUXFkejF6RG9XcjZhcXI3RmgrVXBrdDk5N3FTRjREZ3NJU0JrcHZFN1FkakVGK2xCNE16ZDlqYk0wVXc2QnZhRGYvTldjY2ZNQVMzV2giLCJtYWMiOiJiMzlmNDM1ZDkyZDNjNDk4YjY4MDNjYmUxZTJmZWY0NjM1NGYxODJlZDY4NzJiM2M1NWQ1MjYyNGNhODlkZWZiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1Tam0vWmk5Uzg4bnN0djVZaEZ1L3c9PSIsInZhbHVlIjoieEV0cmVEVjVGTEtDQVFIa3BEaXJRV2tSL3dmUFBrTFhPbHEzQ0JBRjdjeWw2TFBpOWdOWnY2Snk0ZEFPNXpXWjBCYkloOVpVaTcrSzdJVE5laldoRkxYUlBRZ2NOZ1hoRnpsczNXWTg0TkZqdWVkTnYxS2cwREZzcHc1U0FBNDUiLCJtYWMiOiI3ZDEyYmM3N2JlZmZmMDVhZDFhZjdhZWViMmE5M2NiZWQwNzI5OWYxNjgwM2Y4YTgwYTg0YmFiOTRiNzAxYzcxIiwidGFnIjoiIn0%3D",
}

