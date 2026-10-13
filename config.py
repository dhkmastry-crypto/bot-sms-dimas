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
    "cf_clearance": "7C5kud7CbfkUtScgm3ANpLCfLmnjI7YkDrH0SNmV.r0-1791874659-1.2.1.1-UKBW46Hi9TMIicMeVjnyh9OmDriTvCvsaytqDw.ahV9uZVRh5KNoHhzfxYRSCKDm1DPZRfSPg_kWC_RxkJ0occnYD66H1ddwxxcHIS92iqDpJnGluDluTMnnv05aWAsOhZ48Vc615y7dxPPB3bFNNb64kHL7qX32p6CybsJNkwWHk.WTSIbvjvTuCF1lWEw1uJa0RoP_og6lvYOXbPp2IS0IIwkO6lwRg5k2_TGZjNOXMVKsIV8jHsO2pqyyNLG6JIZnQ9078ye7QmkvFr3CpzzGOpM2J5jiNuyIp85KFvJEoFRN4TDQGkSWyS7wDNpgNqhyLpMh2CoCGatjT8VgHlts9HPsI1r2cUjVYvC_57cz6slY.ufqXLHE6Q0kdQDN1wkR7_DszFuE5gSB76f7BMv.1pni4Zck3u9QBZXmfC_LzSFxzrQ_n897KJePLw_vS73dWvvmRyoZdcWK_Q7mSKSwoEki.6q5swCC2RDaW5F6Ty2dpYx4ud.L8Hi1ZQ06rJLN6tAc64zXJsij55i3hw",
    "XSRF-TOKEN": "eyJpdiI6Imxaa1ZZQ2dvYXZ6R0c1MXlJSlRrd1E9PSIsInZhbHVlIjoib0VlMm5KTnV1VFdsaFI3dkVZVThvWkxWeTNEZlM1bDAzQmt2WFh3UnY2dFovdERuTW1wcmlMNXZ0UWJxRjg3YnoyQXBFQ3FXMGNsRitPYzl2RzM1eGtOR1FxZW13Z1lXNUlZUitOVFJjVHY3WUVHWXY3ZkV0Y0xYTGpXNnQ2M0IiLCJtYWMiOiJhYzJjMTkwODI0YzkzNWQ0OWIxNTJlNzZjMWQ1YTU3NmMyMjkwOTVmOWE2YjYxODY3ZTk5YzZhZTI5ZDA5MGRhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InMvUkR4Z3Arc0ZGUzB4a0V0MFI0VEE9PSIsInZhbHVlIjoiWHk4S2ZrMnY3UGFkT1JaVHRUakM1SXNOOXlWdElxdnVmUFJaVUp5ZUZlZnVLTXV6c09rRnZsWDBTYUQySFZ1QkF5eExRYVNmQVVlQUtSZ0dNaVlld0tWb2tQbEx4cmxWSGM3S3dwekIzVXNxMUlLVUFHY05PL0xUZjhtb29ZQlEiLCJtYWMiOiJhYWU3ZTI2YjVmZDI0OWEzNmJiNGY0ZDVjNjBiYmVhYjUxZTJmMzM1MzhiNmMwOGZkZjI0YzRlNTZmNTZmYmM1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "DToueYjQvTdSUZoPuRkT8xdDe4lteMdVOkCX_Jd1W0k-1791875860-1.2.1.1-Sl9_vp3CDdP86zXoflJnL1LDzYm5.08nQOSz7_ZLnWUiITDTqBcJqmobvZMk0FVJlxQ8w8SEs53NQfJFmUbXN_97_qf9r3kl3VQZWq4.IvpzsPAv.vhFlkBTTfN6cCZHhgnNNwtkbeQ9StScrVxGgzxJIUJ8RNoAwoUNVCjc8v9ElJAySqyZfCUuvLZ9ULqf0bOCgwo5jPzBBa0NI_jZO4gmy4J0HSd_rCB9rURKBFKCxBe7UmjqXMUgMqJ1PqSy8ejuBM6un0eF_nYoH7p1aLONifoKu3kJickvPwwqASTUzKDJgZwSU3AGCNbx.78yM3aLoGwvJ9vXWI4InfGI56Ka1zaHHLVV4QDP0OHhM1SW8ka0GXVPdphk3IPCR4d5shhQ3241gv8.A0977XTeIv1VDB1Lb4GcM3zhTaSOtXpLyHM4lZx6M7tavtEaHhdhn2WDarP1MskMHqoLio5Vdcrkb7DNOvLvDhIof2GoFQCim6bjSy1WqRNMQQVEPW_IM0Dmj0JrBXIAM.Xqz5cKsw",
    "XSRF-TOKEN": "eyJpdiI6InJMcERDcU1oK0lXSG9VQU41R0t4aGc9PSIsInZhbHVlIjoiWFB4cTg0VUp1RFM2K3VObHlIMHZVWTRqbUZjcGttUU9odnRoTGI4SDd0ZmlFVnBOTGZqZk9IdFc1ci9iUFBRNWc2ZDRtNUtpc1dOcXZ2MkJUUXViUS83cGkyd05hazluenZIbGpYTy9rTExOeGU4dVBNYXNSODFVdVpVS2hHRjciLCJtYWMiOiIxMDRhY2JkZGQ1ZjVlYTAyYjMxMmRiZWRjY2E1NDU0MmJhZjY2YzE2NDljMWE1YWQwZGJmYzNhZTk4YzgyNWJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJPWGp1eXVWUmFIOXBPb0xXZ1g3Q2c9PSIsInZhbHVlIjoiT3N2UllQYnIrdUpYKzlWaWlUNVY3NW5RS1IzaWNqdUN5S2FwK1FFUWhIZFRYMHRMTk96YzdablJLL2pONHpvYm1SVmhwSUtpN0E4eEJiRnpkY2ZHNjFyR1ZscjdXeU81b2doSkRjRmFIY3MzV1dyYUNFTFVVS0lVTTlkL243cDYiLCJtYWMiOiI0NmE2ZGY1NGEzMzMxOTJjNWMzZTUyMDEzZjU3OTFkYjUzMWMxZGU2OGI2NzAzNGJlOWI5ZWQ4MDliZmIyY2MzIiwidGFnIjoiIn0%3D",
}

