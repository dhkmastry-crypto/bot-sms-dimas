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
#  COOKIES IVASMS (dari browser)
# ────────────────────────────────────────────

COOKIES = {
    "_fbp": "fb.1.1791750688792.297447955592323031",
    "cf_clearance": "5CdaZAdzIbVeCpKAr_vgzttxdQiWsuvv6cfFNDrAK_Y-1791851164-1.2.1.1-3vTZORuGmzUkPucsnNyBEPHeEMPat9.HtaB96R3xB0VNY2KogGLlyA05fJusTaXZW8JIawFCFtHACvJs0cCIWjbAGY2C77vLGw44HC3pBXZEoErYbQZEYAjRkXsQzG57ceuVRvrHYGc1rILC9sKj.xDb9hMcFRHPYFDqCDEGwhKItebS4Y9bLsrjkLwNSGeTcMoXQKvgBduZKlqVjMEuP9QCfmNynWdr1oFhNbJdvtKKCJCoh2amjRMVbMQMw6AWU_eu8AkBkFtujdDHd_mFp1.zB5_qqbJSien__WdX..6CnEuLMMum9H1bS5rK0biISiaUUW5JGlDOrEdcxhBQYJ8IWow6BjyA9uthlxeB3N1plsJsQhUOw_RWxewWdBJehH1V.xzm7OS_g2gUFBi0h7kZ1p0b62Ivvzy4yydZS7ifGTuA7Uay_q5XYuGJOcuL3cOgWJxCNlTwXGNVDMkRYr7GVqTk14TcUvNJ9FvKwdZhRJIYEj4K562p0kbgS5F6ZdE6wLsGoAOZDP5EzPndMw",
    "XSRF-TOKEN": "eyJpdiI6IjBmY0JZNUw1cnJCSW15N2hLSFhBVkE9PSIsInZhbHVlIjoiaC9iS2l2UjhzaWRSUTJEMUFzaGplZGREL3hRYjRieTYzeW93dERid1dyVmRLVFVwN1VqNS8wbzJ3RVNlaE51V25BcE54NllYcUNWTnN0RnAyS3VkeUMzdEJIQ0l0d2dyeExsNmsrd2Z0UnpoSGpTd040aTJPbTdHZVRxM3o0N1ciLCJtYWMiOiJhYjA1MmU2ZWFkM2I4NzIzZmMzMWUwNmU4NDJkYzYxNTVkNmE3YmQ1YzE1MjE4MmQyZmU1ODdkOTE5ZGJkYzI2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVvejY4S0Rjb01BNFVWbmVTUnFISHc9PSIsInZhbHVlIjoiOHZpOGo3NGsya05aZHNVaWNJa1MwKy85R0NFdWJNYU5zUDBVV3lEbGRsbnJ6Ykg0Wnh6cTN4WGpMbFdta3BSK2hhV0RITHpTQXJPTEZ2R3hTZk9hNitnQi8xb2c5SFZCaTI1SUt0YXJkdkI3VS8rcUFSellqbERQS0hPL01RUUkiLCJtYWMiOiJjOWMzYmFjZjJhN2I4MjVjZjQ0YWRlNmQ0NDA5MmEwYTBkZDI4OTIxYmIwM2FkNzNmNzVlYjFkYjNiYTZlYTdmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "F9MG9n6YcnZvXidCPg5f_MJIyH3MHwprc.ws5yjsnNs-1791852325-1.2.1.1-A0CtYkjOlMBB56eRjRssPeh4p9ZlovFeHQXkwJd5TnFK5VI9GCmoWnT.jXqjT_T2CsVKIOUTyZbczaC8IrD4HxEQz_o7cL_VmsRiFh0gJJzfmt451ziS9OzYcQsr4BQj0qm7FmuSpCG.7TphC2cbeoUf3Zda4DsS6h.HuhABsmrCBgl1O7PyjzJnZAdkzyvopLBz1D4WDrEKD8q5fq94ju.aid7HYhJ6vBPIydECg9E1Vni.Oz3j3haD0zrV7x7.NLFTHzw48szZFLZoRBIndKQuyo6Pp45ezMBECHzBD8Ubw57_OFh_KW41rP2.q8Tr3Ks4r.ZYSZPzxdgrJ2KdqlLu5QcXyt22dcb2H1fsk6hFbLirvLkZgdZLD3FFEDTXjYEIgLJ3V4GclbTMI_UmAVPIwTtxEMVCb2uAge6fn_vy67oLBjXwO0K22WqMPOwj4WFqeDnBExvbum1ajSKxmQR2sbrNZgiogvvPAlMOe7YlR1GhjuqCd3xmAGErJh2smmMXn1Y4CtxdA1.cU6ESfA",
    "XSRF-TOKEN": "eyJpdiI6IlV6UjlnUVpKZTIyZTNTV2xtRnpRYWc9PSIsInZhbHVlIjoidTlVQVp5N3FVZ2xsc1VVV3V0Qnc3RFN4RC9RUmc4STBtM0tKdmF6OVp1K3ZoM1ZtU3lpODVidTlDMnRFMlpvL1UxTmNHV2tZcExBdkdSVU5sYWpzU00yb2pzNnBjRmoybkRoNkt1akplSW5oNWpLVnR1bDZ4d1pySmdzTnlyblEiLCJtYWMiOiIyZjc0MjQ0ZTg3MzVhMzkxNjgzMTFmNjNiZDhiNWU4OGQ5NDhkNDRiMTEwZmVlNzMwMmQ0ZjUxMzQxYzNkYmRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IncwTE15NUpaRENQYWFyOHQ1MlkzMHc9PSIsInZhbHVlIjoicTFmREdEd3oyNW9aekIwRHRieG9HUlQzYzJoR2VVMS92Vjl2WURKYmxncE5mc0FuYkJrbG54eVoyeUZ1bFpqRWZ6WVBKaXlUSHNJVHFFSEkxKzVST04rKzgwcTkwYjE1dnh1UjllN2NMTllKb2Z2YXUrODBMYy9tc2NQY201T0kiLCJtYWMiOiJhODdmZjAxZWM2M2ZlZDRhNjI1NmMxNTExNjA1NzRlYmM2N2IxZGI2MDFmMDMwNzUwMmJhNzY2NDMzOGRkZTZiIiwidGFnIjoiIn0%3D",
}

