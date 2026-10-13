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
    "cf_clearance": "7jTG4.55WhDoxkyV3iqN1cwAwJAsIKJRVKz.DgLk0HI-1791922215-1.2.1.1-wcn7XqA.D38.DX.2TcKUWf7DDuES22qvzNT9p4qFJnEQ8KrPHcukmhTsVbU.cqq2Q46E7U0MoP2V.kofczNGTO3fnnB2GutByHMMDQrt78uFlpdQqFlJ9X51dNZljY_XogCg2tLZvqkCmD6Ith6durcIsOk01WJ10ztPYXcRWMt.pTF5HKWSfHJjEPEVTM4mMHOmgaAxZzw85xsJpbHEaFY.28io785HRdc2428bKwWr1FcwTq1.FrXE5UHkhR_xVXvLvXl4NDsMHHkw7WCzIFDta8.NuQ5H6WjFRYpd7nD8K9UBdqwSyWsp0zoX6yjrbgnngzAwlP2GVFAdfOAaEQ7_225EcFMNxaApkuRUnKC_IPbJgargNdigyUAlEHflsXVslHoFCm_0DSTDCyATPHUlbFNTQFXNyqZHjy69mOeIoPH_ec9KpGKjShjo8lZVa5b3.F6xrtzYj6vc5mS5oCZ66f4.Tgr8sfE6ovRFpLetjz5EaaIc80L7l5gp1oJya9ObMQXYeoQKBfGK.ui9.g",
    "XSRF-TOKEN": "eyJpdiI6IkFBZ3V5djZpQTVtSmRoUXJTaTM4TEE9PSIsInZhbHVlIjoiN3o3bm1RdTRrekd3VEwwTjZGcmdCR2hFV2VORmpZcHJGQVcyaDVsQWhGN3NXV1gycUFMZUFHNlJNRGRtV2NuRzR2dDZqQnc3WDNtVERuTDFNTnVLUzhVRmcxM0Z6VnNsTHRONUp2dW9JdXBUN0pUK08yV0hDcHVWZXA3RWhjaTciLCJtYWMiOiI4NTE0ZmVjYWZjOWRjZmI3NmRlYWRjOWZmODJlZjc2YTBjMGU1YTZmY2JiZTU1NGYzMWJkZjk3ZTU3ZGFmYjAzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRjWHp1dzFoTzIxM0FzcTc1b0xpRWc9PSIsInZhbHVlIjoiWmd2Y1hFUmZkV3N4eERvMCs1c1p1OW1xWGNCYTRWM1BCaFFBZDByN3d4akwwQzBaWHNkYkRmMXFURkhGTElQV0JLUTVrVkVLMzU0emtDbHRSMzYxaUFNMnVxOENSM0M1aXpLWGRrMjlMbExBRWVWZXZYT2tvajE2a1pGcVlsTFEiLCJtYWMiOiJlZWQyNTYxOGQ5ZTkyZTFjNmJiNmU0MmI1NDgxMzZlNTUwOTliYWQyYTg4ZTk4ZDVmMWYzYmM5ZjlkNTAxZDIzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "U26F0239qo.uFR_Otu9xTvfBSmphxAI22zsYbfUPufQ-1791922227-1.2.1.1-0ZICuUkH1CDkRzMb5SXlpI.CA2hb.qAkH2zT475q.LruRcfZU5Y_hKYF43LCrNBg3AyOpd1MpA3XC47C.73YFFM_4wdatQRbkmtsJm9Kssa0nbacZCu0nLyEVDdgtXSgHnioTpB5wp6thL4SF9ZjY0LB9sYnm4VoMsyBUn6FnO_pfL8r9jL0CbMF0J6P962jM5kZYl8HLRhIxqyKMFbK1_zVN0ZzPUQn3J56uGiD_HFKRTvUKsK3TZMJtSTrLZp_IPVO5Lg8qX.XNzxOpxFsE5UZ18Y6dMI6W9RNYbVRr4Q6S5xRvxCYLubRqP3H2nIvsZpp5EzIB9QR6brrI2J_sBatgTQb9Sd.6M.b_swqO2TCXkMZd7msS7tTTTAUBDOyQG37xNqhcX3vjzqmgDhMJxB8.l34b27XGdWw8L8DSY_Wv9ntXXqWA2LHShkjf8d1K2Xot6irLMRhXZQNbSMnOVqjt8_2i5x7mH_AEfLEmQtUf7jSs3FoKOKq9quRQwYf9wS7e5lj5oymMwBg8mHX2Q",
    "XSRF-TOKEN": "eyJpdiI6IjFLZ1Q1QkZhS0phM0RUdHR4bjVyOVE9PSIsInZhbHVlIjoiTTlMRDFCa01WQ2lxSGxnekdPWGNzRjJvb1NnR25jQ1MzWU1DUFFJdXpCNHhTUmx3MUZoQnNVWnU4YW1NdnN1c3hSeHoxZ1MxSHhYcCtnNzhvaDN2QUdqNGxVTURRSkVUU0k4Rko5VkNRVnF2TmRHKzV1Z0tEOE95UWNFaGtyZDYiLCJtYWMiOiIwMjNmNmQyOTc5MTU1ZWI0OTM0MzQ5NzgxZDEwZmNmMTBhNDc5NjRiZDJlN2I0ODE1Mjc3YjM5NTdmMDE1YTJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZvenNaekZQY0k3bGlmazlhbDhZL3c9PSIsInZhbHVlIjoiRm0ydVdYcDVaL25qdHhSQmxjUXRYOVVEOEVyZlNjejN1cDBHWWNEbGdQckt6Q1IzS2pCRWE3MnB2ZTcvZFlVYWJvcXFuc3FUNytwcUZHK0NMSXZCUGlwcU5CTHNyVUJWbzQycWxTb202TExTSmduTnFhZksxZnZyVEFZV21RWGEiLCJtYWMiOiI0MmYzNzZhMTQ5ZDM3MWNmOTkzMzBlNzIxZDMzNGQ5ZTc5MmFhMTg1ODFhZTBlZTE4ZDI4NTYwMDg4ZTcyZTQ4IiwidGFnIjoiIn0%3D",
}

