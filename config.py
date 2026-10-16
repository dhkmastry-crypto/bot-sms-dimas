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
    "cf_clearance": "Ad0VZ6GbgWPYVw0Uxsx6WDhOZSVoDVLV.QmLUr2wh8w-1792143433-1.2.1.1-UeRaS1JImM0eRJDEYGLpDD2uperN5CsMeN3Fm73J0_kwq0mhfHYVidvzPAm59SMM6IKAIln4M9i666hHGvFZv0yKfo.EPHEtSY6YqANQVPglm_5hk5K09Q_YeRQItA7IzNZtdQOroEsKzzZoRVicZnlkFv1TgDwyoDSZ1NxeeKzeb1gRAjekkFJiNfGTN4.6Hr0EyHYuDa2U_hEmXH4lmdqQWq837FwxSIOR0bmTDMmN_.dpOd4Xc49fEWSHpsktkiSV9lv7IVMRGoX9EyivjQvRq3Zv50dvDr1sjyStkRSD6l8nu6Tmk_pOTu18PZlfE8TZLn1M30153q3CR0bPqbL.jc1.C6TwrIfsKyqdtiw8adLcIO0JjbTTvxMcgZQ1Go3Zyek6aIUmg81GQBRpCOr0ps.vCdgpFL4QlgTdcrTaQEstD.fuSbC3eI.fSwpE8BRNLXDpAgQnlT1nJ8aw1HjJh2DwJNvrfzroSyGz0HAnMjIh7KLGOQebTY_jR.oBQLtgEovnk8NZuFZbOW92Pg",
    "XSRF-TOKEN": "eyJpdiI6IjV5VXI0ckgreDI3azdZdmNjWmI4VFE9PSIsInZhbHVlIjoiejNiUXNvOEhFUUErVlRTc3liblVHanJCL3VsRHhBM3p0dGNUOTJqMFovcFE0NHQ1M0ZCaG9tNiswSmNjcHBsbFg1Uzg0amFsYkJvYkhWNXBWMXpFNStLU2ZkTTB2UUoxRm1OYkJScE5iS1N3Y0dnYVhpUWdjaE5ScUpleHRYSlIiLCJtYWMiOiIwMTk3YjhiMWFmM2RiMzUyYmNlNGVlMDNmMmU0NWQ1Yzk5NTE5MjViY2IxMGI1NDcyNzg4MThlM2ViMTNiMmFiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjNiNWswRXViaTBrY1lBLzRsa25jdmc9PSIsInZhbHVlIjoiWWpjazh5RWZKKzFyUTBwbHh3Vy9zbXJPQ1Z5bFYyMWhDWDFSN3RreGpCTFFHSitUeHVkU0VvbVNlcHN2RG5pUGVQTDRmeTg5RVVZSGNyWVRWbUZOczdOZG0vclpUcXlHdzAxc1BuTHl2U2w3Y3FaSGgyeEVsWFBlYkRCVW53VDIiLCJtYWMiOiJjM2M4ODkzOWQ3ZWY1NjA3NmQ1OGY1MTUwZWNkM2U1M2ExMjhhYmI4YjRhN2VlMzY5NzU2NjljZWNjYjU0MzYxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "8t9ug0qy6PwZzkM8TpbbUODNgCsc91adUBOpBGhFE7g-1792143444-1.2.1.1-P_wiLgguboFpdu8UvjP85UT0uYMaPLRDcF6kq44EzyqaR5H.ubg4tAm6U1w9FkwSiXNev6qz5F_irC7qYTbxyM_gZahR1IetbApL336ejuGE9z6LhoBZ7t28_YoTpLNoslm5IVdYaUlVVLhlbBB_Ld322dJhttactbUxkOlOckBgYzu.253xQ2ZmLruT856PVhqtBmPjbdWa5UEG1SDRrXPOQy734PIReFevwqXg3pBs2eu4cQg3NpJ1ZT1dIh2VOUIrknnClZCOf0ZR55ugNfyRxg_2FV5P2kQ6gwFXKrxNb9KDI4r1iVxC7wtQdrWhEdOJs9kt_21TnJVKcPM_xcPCfj8YSzMJgHBZdE0yei5HV_Kjphl8F0AOYbzSqeeMTj7xFbBricHJ_h_CaPNEBhiBZrnrBq2RIMb0QRbUw4Nq_ZAQ2Fg10dSpp3JgwcVi9gISX6DeWEavYBD.JseHOqiszaxyWXwKOlolKS97GdahI8p4hGqyniudDVdXtl4vrqV2zTogRmMe5uAw4WyVrg",
    "XSRF-TOKEN": "eyJpdiI6InFBT2pieFZXNlJ5Q05RbVRrc21TWWc9PSIsInZhbHVlIjoiY2NpejEzVGQ2YmgxcXU5ZS9IM2VYV2ErR3NYMEt1TWJ5c2FzUUI2TGU3Q0VBcmFna1BVWHp1WDBJYk02SnErQThpRlp2ME1RRVE5WnpDUjJDb2xtS3NxZXNIMlYxMmpiTXRiZU9YczJLcUEvUTRyWnZia1VGMFZJeHFpUnNzZCsiLCJtYWMiOiI0MzAxMmU5NzE4NTA0MjU0Njc1YzM4YTZjN2JhNzdlOGI4ZTEzM2FhZGQ4MjBiNjdlM2ZmZDdkZjAyNjkxOTNjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJiSmp1Y1Z5a1VVWldyTHlNREVUdEE9PSIsInZhbHVlIjoiVFE4ZWc0NTY4Um5XRHg1LzNsRmZjbys1SFI1T3VHU21nd0dlYzhNYXdGK3czaHpFV1Eza1o5MllCWFJ1S3ZDZ3hrVHVPZG5QbHZaRWE2bE9xcjA0ZlhEN0loMFpqS240VE9maDd5eUVwcmVHcWxkcUU4NFo1eHk3NW1oQmtMNXIiLCJtYWMiOiJiNzQ0ZDgzNTQyOTVhMDMzMWYwNmNiNzRmZjdkYzBkYTA1MzBhOGNjYjlhYjUxZWJiZjU4MzgxMWZlZjU4OGJiIiwidGFnIjoiIn0%3D",
}

