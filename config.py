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
    "cf_clearance": "4teh8T_8fDRP34E6Ahvmra8OOYi0dmYUd1o_mHksvOc-1791958413-1.2.1.1-bdeFCF.zwqst4QvEiIQzFlz.ZyZlAPqpFLSSusO8RRSnd5ugPvtPEr55dPNMUFhnotmbMFnVlRi58ndaW1k8AHTBet3JHrvgqWHYvYLPauivrj3B6T05t91_9yY_v6TM8N4GeW1OVX8EHeCHKDbXwVljgsdPotsozFfNwI7Gg9cO_g9GM1RQj0I22HlCc.DjWdWLaJjt7lUovhQqs1zbbhqFIn0iPoRLuXzPoeRw1z5YEHLgmjsglL2f166GJ3kHFj73y0laNXadSIfARq29l4ktjN_21jKCasMdiV_oiJamtB9o97_gZkHhkrSLHOhl2.FEixaxM7qP5cUBrJr.a2HPxLeM5BtOjEyZLu8X2dFBIdVYWdCpOhw86LLjAfzf7gwGlIBdMpW_DCIzW7VELmzS8lCi4mpYzRV5y3j4Ua6E9_nmnG6izdmfFPPnWvGTOZUxj6letmb.LVMwrvNCm0DEU0fdSwJ7getwy4AEDwFqP3ZQsEvmAxFbjfkl81k1NDc2kXI1X54Ta359vOntzA",
    "XSRF-TOKEN": "eyJpdiI6IlkrU0syVnNIV2lXcXNZZHZ1YnFudkE9PSIsInZhbHVlIjoiTjF3WUYxK0dLMDl1YURMb2JueUZQcENRQWdTZkRSRjB6Z3RnT081aGVpS1o2c2UyTEVkbE52RS9FVFdhcHBpOSt2QW1idTFncnBKa0FoZC9rK0gwQ21EVTBYOStaSTdMbFgzVVM4bTYwYWdpUnJTOXFkaFFldmxncmNDczY0ZzYiLCJtYWMiOiI3MTZkZWZmYTEwZjc5NDhiNDQ0OTgzZjI0NWY5MTJmODAzYWNkMmI4ZjIzOGM3ZDU4YWIyOTU4MDcyNTgyOGRkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZJMTJtVm9Dd05sSzQvVTF0anFuZlE9PSIsInZhbHVlIjoiakRVUi93VnVvRDQyUW5LWWtYVnllT2NmNndGRnBpVTBaZE04Mm5pRXU4RDNBM3NMdzhvM002dkJVRkU1NGhOVkhMN0k1MVkweXVYY01hbm1vekZTVDVUTmNGZnN1KzNwSUVEakdaL2lsK1VVQUNEeFNqSyt1cXdEdU5tNU9iWXkiLCJtYWMiOiI3OWViMzc1OGI2MjgwMDg1NjE0NGVlMmI4ZTUwNjZkMjIxZTAxNDBmYTcwNjUzNTBmYTE0MDZkYTE1YjNhM2Y3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "9n8l1OTgB01qyxgqoWF65F2Bbf680TvofVqpR2Wbpq8-1791956697-1.2.1.1-zGe96Dw07yff5NtYSfHgNDadUvVS_jRzJKvCDuV33e3zXad4KWCJCOYUAuDsIxSaVojeKkrqIVnzyPum6S5Md45IoU_C_QyCGvhoWV7KaiQjWciosvHJrtmx1I_Hgwfj90ysTEFzO49GltfFPFoHZlwxzD51JUWPahOA1SghdMeNf_T90APtoAyDHRCeEFDTPvw5eQOUuwZFf1cd80BGVTW68uUmfNSN_o.jgxkEvAhArXcbqcTDiqvX2vb7I71j19HMwKcWGvLDcoA51HuT.0ePKQoC7bdi2AJ_S0AaIukfeCjLCLoqBBn7VW4F1mPIdStKQQY5oTqik7jDNaZNlh20qGVXc2uV18sU6yFfW11cF4k4FK320tsz.AS5kIo0lK_GSSUMI1GCIUQMahJM50sHiABseq4A7dBnE8AMPq8uBE5KMKv.cD0UVB.Wmyn2atdM.xRnhq0OQF_76Nq2uBy9yk5MAIy_Xm_bPQUY2sHk3tU0UDVEdTxMlW47FGSyV4uVvt_fREspF_SqspeC6g",
    "XSRF-TOKEN": "eyJpdiI6IlFzN0UzWEVMVnpTNVc0WmJLYjViR0E9PSIsInZhbHVlIjoibXNNS2JBcndRL1hjUS9IY3NFVmlLdmhpSlBSTktyaEI1WmpLb05FK1VZdjlRZk0zNHhTcG1ta1lLeWUrVGREWUNXWUo4NCtjUGorMmpsMURwOGQzQyt3YXkwY1h0V2RuM3hIZ20vK1hWN2I2OXJvSGx4azFXWmZ1dVJqa2N0R0giLCJtYWMiOiIyODA0YzVhOGJiNTk0YTYyMmYyZWRkMGNiMDRmMzk5ODE4ZjBjMjczNTUxNzA1MTc4YmVkZWRlNWI1OTIzZTZhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBreUtEOVBHNi9IREYzN0h2T3VSTGc9PSIsInZhbHVlIjoiSUNwZ2lkcm8wME1wdXFlZGlMZXFzRVl4Y1R4RG5TS3Jla1Z2ejRjaUxMcVQ5bXJITFBIdnV4QUxsMDBCd01WSktLblh1eksxbWVJc2sxMm5yV3JEenM3eDFvaDBsTnVpK3pjODYwZHRoamhvak9XcFRRamw0QzFZaG1va01KSXkiLCJtYWMiOiIwYjZlNGY4ODNkZDgxYmNmZDYzMTg1ZGI3YWQ3MWMwMTJiMTJiYWM0ZGEyZmI4NmFhN2MwZjY5NTNlZGYyZmFlIiwidGFnIjoiIn0%3D",
}

