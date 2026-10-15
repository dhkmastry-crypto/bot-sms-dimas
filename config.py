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
    "cf_clearance": "33vYFHU6WF9hjtFfv13TvlqLhpVpncpotikRz2d6Olg-1792024672-1.2.1.1-4JLwcDM_oJEg2rmPHzopQ4Ac0fkWQLSWp0pIwTODLYDuPgI.CS13e7QBzpjKeCwUOA3HzUXcAmIO4smZHZQuW1yqMqlkCg3CzmFARjP80BZcRXBZRXWMXwynRI_RrvVyvzBsu3Z8voOvOLJGhwwHCTMNBBuitdK1eHL_FxzjeQebgz5fY8ACIhj_bCVg99NFTLN6izPBj_uXmr7XflScDOrXp1lmUI4n.cNRLMSMssTz2REbDszQH4nOtG8ugflzymTzTGPur3EzA9M3VY6EGW2O__d3xlABjltov2y1P92IVxPRjL5W_93eHOCwrxIe6xxq.lIT_Prl8LYa4arNa_rdDxxRSiZPhX7KFk5oSBv39oaZZH8okx3NJ6c5KYqo_UOmAoGebGkW3QIfKviaFM7Pl2qf7AcguXCIQbP5.nGHdNxgszQmPoN96SXbsJ04Q2CE6n72Q5lDszsNCpdqHPPJ6GObXNnvY9G8KAshxOb4lKmAyy35fe.ahxguNGWYRcTaUyqAoz9lfuN5LQta.w",
    "XSRF-TOKEN": "eyJpdiI6IlpJV1liV094TldiMGNGSzh3ek16ekE9PSIsInZhbHVlIjoid0JFWnRFYkZDZFNVOTJtWkxrRHFPMzlIZkllTDZzUE1yUEM0S0FHZFd5ZHV1S2t0MURRWGVSdXNxRXhZNE9LYjh3RHRRTWtBd3ViRFBENUFpanp3Q1huN2hqb2JRVEJsRkZnZDg1S01QTXJ0bnN6NU84N2VwdzBURXhlV3h2ZmQiLCJtYWMiOiJkZWQ1Y2NiZTZjOTE4ZGYyZTUzNjU5ZDJkNjgxOTkzMjE5MjJhYjU4ZDNlZDZkZTAyNGM5YjgwM2UyNGJkNzVhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjVXU054ODJyVGIzRklPNTg2eXFkTWc9PSIsInZhbHVlIjoia2dUWkNtdzBMeUtDL0lkZVFvTFd2czEwSFRhMlpXUS9vU21JN1A5TmRLRWZxbHl0YmFoWEtLdlBBaENhTk5aa01uUVpwYXlGbE16V2RVTTMxZ1FJK1NtdFg3UlJQZ2ZpaFpBRzNnY3F5MW9ZZWZPWUkyQVhPdFBwcVk3S2taZ1IiLCJtYWMiOiI3YTU3YjczYzFmZmY3YzljODQ2MGI4MDFlY2U0OGE0OWVkYjYyOGNiMDlhMjVkMDNhZjNkMGFlYWE5NTFhNzEzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "2c8olPt53fyDH4eWw4HUiAux78hU2tL8nnddUo7gC6Q-1792024662-1.2.1.1-.tzT99UecwNYTrPx7yn0ThSsL0szhGApzRaZcvDCDCyGOKiiGDNGMXYCJmHeZ.9DWgtHSvKDssX_HS4MWGOl837Z5En.SQJL3_F7GxpiDP3dWa2dWzdGtOaQkYu_yA2oRiQeVsFtol7WKASh9VO4nyoj6DBaZk0yfrF6pCIpA0TK3xx.B6hRhhMiWDefebjgLT_gycmRNy4RFDpza3QvCBUjh2GFEy3dC9bN9.CwO.DNjaHmEkXat3UOYCWGTkRUt2s.8ZigzJcxkJ9Q3N2sZTgFoeo5Uzop8uAGDcVmLFV759.g_GjLKBQfZUYrLA7Js4GFOGH.XM8Knx_fPjA4b0REIu8mb8tfnjrOhaxNMMwgyaJ4HGu7JhDw.ok.uqyOgtrMSXBdpfV4zGhGNEYfirv9llIjXfprTuGS34RENHPgQmuWXy0yDKFOSg8owMUYfuPw7__8EbqTxR1OeXPckMNIkYYDvcQmVh.wX95GYsQAzjqF.XzaMGL_fF5.GkGXCd4V44t7F3RInE8xz.bfuQ",
    "XSRF-TOKEN": "eyJpdiI6Im5xamg1dVFmTzY0UEtiVTlUN0dMWEE9PSIsInZhbHVlIjoiWHF4VWNvV0lob2h4Vy85bVZWbXQvVDhEM21HSUNCeVdlSTlhOUlSbmtldXZpR1lXUVJIZGhUclhIa2lLZlV3anpUNXpEdnFXQTdWc0d4UTl3NUVFWGF0OGFpMjY2TC9pQWJ3MmZJYytVL2NweVlkN21LWTFuSHRaYWFHMmlHd0IiLCJtYWMiOiJjZDY3ODY1NTc2ZGQxZTY1MGRiYzllYjE5OGU1N2YwN2I1NjYyZDQ4ZDZjMzc3YTNmOTZkMzgzYzA0MmY3NDMxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InVyUjREeGFZNFQya0ZnMmZEenhUNkE9PSIsInZhbHVlIjoiN1oxTUNUZVdrWkFrYTFidDl4c05jVUF0WW5CSlN5VWh3aEE4SERDdndUWHQ3c3pTNmc2RDBld0YrUVpVejlFSnpiTnBDNU8wZ1lRVG15MEpYRjZoRFFFUllzUUtDQ0hqdFZKcldLT2NGNjlvSUF1NFBOcFg5TWNvb2JZRlNVRzUiLCJtYWMiOiIwMTEzMjVlMzVlNmRiNTRhMDk5Nzc1ZWYwOTEyNTNhMDNhZGMxODRlZTU3MzQxOTgyNjE4MzJiYjk2NGNlYWY3IiwidGFnIjoiIn0%3D",
}

