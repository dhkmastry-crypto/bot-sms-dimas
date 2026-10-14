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
    "cf_clearance": "yRE2rnzd2QsRmyHYUBF.roICpdxPHoDPr2LmoDlKtuo-1791987402-1.2.1.1-NeCvFHjiIHr7Cf13hhGYf70neAREAiPy3.OUQ0YIKhI98GmKRJx3S0clolZ5vMbZa2iF0c.jHZcZPsuZhmqS2g9zQ9YvzQ.Ef0zj.6LI5uHi3rccAUHdTBYy5moACvV.nwnn0fVz6Rc7kxOnsxf_v5FJFttEl7SpOheblSJtqAbbBGrWkOpFRETGsi4gjRrRm7ikMScvSvZpCfyAUcAxm0Z14rD.MgqOKe4GUkqUCvtQ58tP1uuMn0Md3a.PbaLlcqHZms7FyQAOfKrpYNdy41OkF__nQTHPyNocRWoneevkgqohYnVJ8nkog1GzsisG8.4XGrSRKFwyPNYUIyFte4zu_rXaUvfLR8A2qfoP5zSiCLKR.wCGnuUmuuNH.D2mYSnbjN0vO4l_AIlEBjYJqTXXFFWk6P1_8ko.k7vQWZLzX.JIwlu0E.Ot2119H6SGA9E5rvXM.U3sxweDa3JM_HdkD0tHlhMh0Vms7GYNv.JBEzCwdReQeDGe6Ntg8KZ4.r9Kgb7TZOtAzYZoEEbJfw",
    "XSRF-TOKEN": "eyJpdiI6InFoNGdxQk51Uy9IR0lPT0VhVGpHa3c9PSIsInZhbHVlIjoiRFh4ajlyT2htdVZkSXFYc0xXSTlIdzlJdmhSTmZYaW5zYWVnQi9CVnYvRm5Od1FnN3JyQ0oxRFNRSklIeGt2Wm5meS9BelcreGNFV0ZZUFNQaWRlSnNSUG95NGFGRWtGZjh3a0dRc1EvYWxNa2daeDBITFltTVJRaGkyTUNaNmIiLCJtYWMiOiI2YzMzZTdjY2JlMzQ4ZDMxZjQ3ODE5MThhMGQ4ZGE5ZWQ3YWZkMzAzNDcwNmZjODM2YjM5MTBjOWMwMTM4YThjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik1lNEFlSjFTT0VsRFhqdExURjRLM0E9PSIsInZhbHVlIjoibkdwY3FHOEZja2JBb2NNR29ZcXMybHBLZHhObFIrL25EY2ZsU2RBRjNxeGRObjFGVmpxQTlBaEVacndCQWJxTjREWlk5UFlqdDc0THlOeGY1TEhqUWVRWWRXRC81b0l1ZkVLY0hZMHgwdDQ1UkVMbU54WUNESmMwZlhYNEVaa3oiLCJtYWMiOiIzOGU2ZmU5MTY2NmNiZjVkNWVjOTQwOGJlNDBkZTU5YmQ4ODk3MTc5MTk5ZmJjMGJlYzYwZjAwZjJlN2RkNDA0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "z8cNVJ4aTLKT_thitqcy1h3ywIa871pHBUGyGcSGois-1791987467-1.2.1.1-p7nq6TQaXF0zwrBJEBnnvIueJagcMrJNLVsZAxtkXLInhkGBdcVrRm1Ypi.FDHmjSvJdhUZfV0oQYZ2VXUybkoh5uAsxRt4wzn7j37qpOVDFRyIPbXR5wIEmNkMNabOc8nWaYgRyZMjtwLMZDSb_ndkwtzrrxMRqxPIoglaQIRSr2ErR4gruKPiRk8BX6TOAjCxkJ_q1E.ACQ1OnIg7rr1okrtD8tG7SSzhrwbRF2bGAt.DYzk5GXeLCAtiRpXX_YkmSZsc5009bi4.XqxlZLXw2XiI4ENI72CiuQO6gAvxoLx0O1QTf_7d4Ke1nK5wxxVoj6vug8epV8V7gV20i5asXuMw_8U3HqMrrcdlv8Kug502B4Vv71ATLFbQoxm3Fg7lYI5dmiGM8QiAmfBt25BrTMWFvtgm1BfhSuyGhQTJzRsoeMMfm1xDcZ9et7ZA_8KtKCo.WQlkVIzx96pMZe73iZjY2P5mAKhqAiknsC5Z3GxSZBd6jROrQhJivQYYuBzyXJqoC_WxXuXYSUcALBg",
    "XSRF-TOKEN": "eyJpdiI6IktoeWhwZnQ0U29PWnpYU2sybXVIQVE9PSIsInZhbHVlIjoiN3E0amVob3RkNzBFQ3NvQXVBWDNkVTVaRWpZWmM3STdicllIRjdud1FZaXJjUnlGdlQ3c251cnJ3a3g1Z1g3VmY4bllTYUpGZWJVcDNmUjEvSjk5MmZ5SVdjYmRlZHVMeVlCOEQrNllZRUFYZlhZNkpmWHRZbWJVeTRDTUt6RVQiLCJtYWMiOiIwMWNiNjcwMDM4Yzg2YmViMjY4MjdiNmU2M2VjNTAwZDQ4YTc1NTkyZGQxNDc4MzM5MDVkY2QzYjZlZjBmNTE4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVMdXNpVkQvL1l4L3AwK2ZiVkY5OWc9PSIsInZhbHVlIjoiazhEQktnMHRzOHBMbFppNzhVeWdXSGE4dHg0bGNwUFBGUTlwclZzRTF4aDRqMUxoVXdGMzE3M0FJclJxZCtRRVo5akMwSnU2Rmp2UVVvT01SYk1jR0RIOE91NUNyRk5FZFNVMGdWNjhBa1hkMTFMQkVsdFBqaUtleU9QTTlVWW4iLCJtYWMiOiIzYTk2NWJhZmExMzRlZmQ5MGIzOThiMjAwMTY0MzAxYWE2N2Q3NzE1Yjg1ZTEwOTFlNmMxOWI3ZWFkOTgxNDBiIiwidGFnIjoiIn0%3D",
}

