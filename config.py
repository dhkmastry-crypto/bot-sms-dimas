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
    "cf_clearance": "pJ_H0amrkLCkVNR071kBwZgoFGtoGdR48JhNzAoTlW8-1792105349-1.2.1.1-sX427xYmNZArjsYrjKFYv2PULgPC8dgtx51sJsjDyNcrCxaKfxxWj9S0vi35K4esu0L5HsbUBi2.MjyQVzdm_93dyUg__GwlHNiahH6lyryiknt9A0Yl1zFzwubP5csC1cQYYO3kYREUuTkSkn273hanHsfF5ar1_D1ZLxnQfOqfhYdE8eaw.Poc4VTj_MjtZ0Jj9v8vVvvUgo0TrWIWKKv9xki6tnvYLIxRvb53VbY9Zfpu9TYes6kwgRqQ8sueQJkFXdrsG4wcsVP24FgbrszEEuKaAlqjJDihpQRN_2NsOi8e32QTl2sldny.gciEiTKlB4xsdgBRE5ZzM2StD2E9DR63dBrG5N0By0JxNUm_MeE9D7Us7Pmvxm.JIvoc6I8FZAStktDYBZxYzWEGPAq_8qJSmFBpfFor_3pDVW35eGi0uTjX19cOnJNQFQSHmacTkg8I7CINhn1AR.zkiX.0SWBtTvA6SKae0D1b8zgZJTujjB.3oji_ufJm9Dau_BjXhL2hlCIR3PipdVnOBA",
    "XSRF-TOKEN": "eyJpdiI6IkNMOXZoR3JUMXg4L014aUpFUHAwUHc9PSIsInZhbHVlIjoieXJKVVZoNDh2dGxTUHVQUHB0Wlh2V2l1enpiK2hZNUdFZlErNjhPTXNyeE1vYnpvS2tueGhSelRVc0ZnYmtlTEQrWGFrbGZsVXozYTBrWTMrN0VxZG9kcU5VTEhTcjNxQWZpZXFNcTZZSE5nejBNdlhIeEsxMjQwQW1PRUZBeVEiLCJtYWMiOiJmZThmMDFjZDhiZWVjNTc0MmU3YTM4ZTNlMjcxNmI2NWNiZDNhYjhhMTM2NzQyOWE5YjkyNjhhMjBlN2YzZDcwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlhFK1FNaWtOVWtWQk5LY1pzNEV2OFE9PSIsInZhbHVlIjoiNGQzTVBIQnZmdnhrRG14S01HQVJVQm54VDhBNGhrOVNoZWRURG5ZQWRuUklsWFBRRlBLSGkvVkJTUUxzMGJBMVUwQlRyZkVjYldTdDg3TGxTMVhCMHFGVCtuWHVKWE84L3BMSXZuOERxNitiZHA2WDNLSVJGZERiMEl0WE9GRCsiLCJtYWMiOiJkMmIwYmQ0Y2VjNzQ3YWNhNDNkYTgxMzc3ZDIwOTk0Zjk0ODc0MDVkN2ZiZmU3NjQ5MWI3ZTM1OWNjNjYxNDJkIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "sGH5Tj.TotWo8LnQOfFfmti.un5oBXZ0XNWIDphZDDk-1792105392-1.2.1.1-jE4SY89UnXw_z_kMdSDDEEijeWfz3tyKvoTJDmbh2X.0XbXoqlev186Z0IdP.PGhAiLF_rGP9Vxnal7dUkUGybQJl3AAe7FFlsg5whqKaJwsLXmipvghqpF6clUnWfgjFoAJC8GeHQphSiR6EGZFqamSvRNbQfNI53dF5jHSskccUN29MIomm7za7y3KnlduHShWA.4EA6EBywoP_NsC8R8iXLjQUg3Ji41zEmFItqtJoFzDrK623tbR15QQyjBgO96nnuu5eXRtWILo2T0gVDN7KRMYLnfoAxcxH3IDIUTbRHku01UuwDR7Z2uggC2E5SiZbmgi_yyNndZNXi0baggfZYmNWddag1Ho6GOWKGDqQIGp.eBr2Mbg_OxpVssW7uhsvHcmVo7I1qcldOxphw3LhsaG5k_GbDCTI705umkmvvKJ7aIlm7dFKpTZ6.hKTwyXXK1IKeSkarABmT26_ERFNywLp7.mS6UvTibb1oeVgmRj9d5T8LVqEZEaBKEz76Du13.GDzEjRtFGmzDMsw",
    "XSRF-TOKEN": "eyJpdiI6InR4K1F3b3JzbFlvMkVJZE8ydE0wZHc9PSIsInZhbHVlIjoiQU9YZlRYRExFckZhRk1iV2s1cEhLUnVVL2l1Qit2WHcwd3h2NFhZYnY3VHpsRmRudHUvbFN0VkxsSTJxd2NDdktKbFJUWC9uRkw5U2MyLzZ2VlV0U3JOYTlicWNGLzBublU2N2czRlU1Z3dYOUtmWlFMNlVtTDBwcDA5cTU4ajgiLCJtYWMiOiJhOGQyZDQ4MDExMzVmNWVhOGMzYTQ0NGMyMDZjM2NhM2Q1N2E2NmU2MTk4MWI5OWZhMjlkYzNiM2YxN2YyMzJlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRadGVVbWNJZmpXQ3UwbjJBSit1ZGc9PSIsInZhbHVlIjoibDF2ZFVXQXhDS1kvaTFDMDk3cEFIcXZqc2dKV2RDc3JIMHhFL000UXpWZWhBem5raUFwWHhicmswSzJKK2lTRWRmYkhrd3hPV2JyTzFsYVFrYVJUdHFCelpCeldGZjBOZ05RVUxkbjFWVHlET3B0SnZDVkplS3huRjRpUzNHS2UiLCJtYWMiOiJmMjRlZGFkMmFhNTg0ZWM3Mzg3YmFiZWU3ZjliMWMyNDU5NWUxYzNkOGFiMTliMWJiNzAwNjA5MTQwZmI0NjA5IiwidGFnIjoiIn0%3D",
}

