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
    "cf_clearance": "z8cNVJ4aTLKT_thitqcy1h3ywIa871pHBUGyGcSGois-1791987467-1.2.1.1-p7nq6TQaXF0zwrBJEBnnvIueJagcMrJNLVsZAxtkXLInhkGBdcVrRm1Ypi.FDHmjSvJdhUZfV0oQYZ2VXUybkoh5uAsxRt4wzn7j37qpOVDFRyIPbXR5wIEmNkMNabOc8nWaYgRyZMjtwLMZDSb_ndkwtzrrxMRqxPIoglaQIRSr2ErR4gruKPiRk8BX6TOAjCxkJ_q1E.ACQ1OnIg7rr1okrtD8tG7SSzhrwbRF2bGAt.DYzk5GXeLCAtiRpXX_YkmSZsc5009bi4.XqxlZLXw2XiI4ENI72CiuQO6gAvxoLx0O1QTf_7d4Ke1nK5wxxVoj6vug8epV8V7gV20i5asXuMw_8U3HqMrrcdlv8Kug502B4Vv71ATLFbQoxm3Fg7lYI5dmiGM8QiAmfBt25BrTMWFvtgm1BfhSuyGhQTJzRsoeMMfm1xDcZ9et7ZA_8KtKCo.WQlkVIzx96pMZe73iZjY2P5mAKhqAiknsC5Z3GxSZBd6jROrQhJivQYYuBzyXJqoC_WxXuXYSUcALBg",
    "XSRF-TOKEN": "eyJpdiI6IktoeWhwZnQ0U29PWnpYU2sybXVIQVE9PSIsInZhbHVlIjoiN3E0amVob3RkNzBFQ3NvQXVBWDNkVTVaRWpZWmM3STdicllIRjdud1FZaXJjUnlGdlQ3c251cnJ3a3g1Z1g3VmY4bllTYUpGZWJVcDNmUjEvSjk5MmZ5SVdjYmRlZHVMeVlCOEQrNllZRUFYZlhZNkpmWHRZbWJVeTRDTUt6RVQiLCJtYWMiOiIwMWNiNjcwMDM4Yzg2YmViMjY4MjdiNmU2M2VjNTAwZDQ4YTc1NTkyZGQxNDc4MzM5MDVkY2QzYjZlZjBmNTE4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkVMdXNpVkQvL1l4L3AwK2ZiVkY5OWc9PSIsInZhbHVlIjoiazhEQktnMHRzOHBMbFppNzhVeWdXSGE4dHg0bGNwUFBGUTlwclZzRTF4aDRqMUxoVXdGMzE3M0FJclJxZCtRRVo5akMwSnU2Rmp2UVVvT01SYk1jR0RIOE91NUNyRk5FZFNVMGdWNjhBa1hkMTFMQkVsdFBqaUtleU9QTTlVWW4iLCJtYWMiOiIzYTk2NWJhZmExMzRlZmQ5MGIzOThiMjAwMTY0MzAxYWE2N2Q3NzE1Yjg1ZTEwOTFlNmMxOWI3ZWFkOTgxNDBiIiwidGFnIjoiIn0%3D",
}

