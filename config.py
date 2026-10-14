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
    "cf_clearance": "4Ce8FaPH8W3JXmkb77_TEBBQwMv_VOOlnxrTj1CIIqw-1791960220-1.2.1.1-y0s1tbksD.dMMmreHBd.SmWnZbUS7Qx3Qw6IM9QIqnSIphhQiL06TlM4v24fy7Nxm0pgjZ7u9RDj.xvSbkk3dVTIuj6ROpI8yqG0MU4Dju13g.IQzP_ArCuXSTU6y6sQYLaTpOk_d9SWP8dBbtc9OqB9l8imoNWQSyyI70CfBg80nzERZuyoLWibww7f3SKKF7UKjZvoyUtPHNOdQK0hW3i6R9_8ASKmGhQPdwwMHTUO001Q.2p2ylJQN9FlOyFavAMKMwGxh6wWUTbKNIokW3VERq2JdY6m60T10fPoVpTL0pYGmxdxvvDw_x2h2UZAMJVbO3d2hWU5W1dwTbGZqaIgvgJtYbltLKoAoogvre7IncP36Bwrkhs9phOZnW2b6VGuS4T0Cc8iqYA2BAkfiAJgf4QfXK0lXxKQxjQ_rE08JUMWj6J.S7H8Vz5EFROAbMZILqtV1.OL2NOWmGWCDTY1Bdsm0JoVmxO0f6GLmLo.oGio8NPZWPbb15JgnBWMnJEyhYZGrHscB24lVi_5gg",
    "XSRF-TOKEN": "eyJpdiI6IncwVm9vUy96WHBNR2pTVFo0SEo1Z3c9PSIsInZhbHVlIjoiajNqWWx1eXVUeEgrUnFhcUFLdTZWMnNUWkFxMWtjYjJQNURPZXVrMnVpOFgwOSt6MWxkeEl0eXJwbnZUNXplRnpNcGtEY05uVGluTzNSQ2dIazhiU3NkUEVCY1hXTzFkSWd0d2w4bFZ5OUZZckVIblhDRk13ZnZaemliWmg3ZjMiLCJtYWMiOiIxODFiMWJhNjA0ZTdjMmVlYTczMDlmNGUxNzUyN2MyNjE5NzJjYTEzMDhmYTVjN2UzNmNkMDhjN2Q4ZjMwOGExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRsc2FTOTA1NkpWZGhFR3dqMW9UMnc9PSIsInZhbHVlIjoiNWlHUlFKbXJQaGJNN2NrUFIrS0VwdUJKK3NJYjk5Q1prRnJiTEIwaWxCalhkbEJrSWhGbithdm9IN2pGcVR1T3JXMnhQS21zL0FwK3JIaGRPYWk0dGh5Y0pxZndCdGxNK3BmQ01pMGdXOG5LSFFyV0I5K25nR014Mlo5OU8wUUkiLCJtYWMiOiI5MWFkN2UwNTNkMWRmNGFmZmYxMmY1YzQwYzI4MGQyOTVmZTllYzlhZDg1M2Y0NTdkYzFjMmU1YTkwZDUwMGM3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "nWcG98x3x6.0V_GW5fnkHivH6d1vTdi_shV4u2G1BCQ-1791960318-1.2.1.1-F9Sq1A_loF7gr3V0SaxHfImUfq_xSvMjoZHSBZuvQMzLmdygGaY2Zthpq4wUQuq.YiFYFBI.UHeYNBK2Fah.7MTBg5T91G4.D74TRQyBkcSOhlKsRq0GOEL.9g8AYK4Z4jIF6aFtJ350c4xiFQvW5ZZ2oxNtbB5_agmitLpBsHNZrp1CYzwUufnw4Tv3GOUnsUWQhvN2O685tn6y.h3bCJIcerH7zPOkoPIBhTgM47LAj2gPo9MjwMqrBj.zIngqDfM2NClO_ZRJUM6gL8t4hFhQqwC1DR5rHJvWoSOLi0xq8Ym3VOcZuWqcej3SzvuZL43BT3z_9TpBgHLeHcvm3ae.d6q2oZmuP7VCFUcEvsSDIJEaPHLI_jA2aArSru9B4N9awDwoBhkFzpaGW0plvLVruRGPky..RjwEHycfJzx.62pLd0E26VVuRrxm_tVJ549PyQ25H16pVRA6r6Jv6Jzn7e4zZEg72v6Fj8LJ6uY9ZzwlK8RZv1YJT..1CnjkMRf.u0hQNFOgameO1uVl1Q",
    "XSRF-TOKEN": "eyJpdiI6ImRMMVRGazdyUTQyejFXV25QSU9sYnc9PSIsInZhbHVlIjoiZkhYR2tEQ0FQNjZQRGdURTNLeWQ5RGQ4MVhjblp0VzZQYm54QVYyb2J1UFpRYmUvOE05SzRsWXNxV0Yzd1R0VktvUjZOeVRaRGxwa3oyTDZyV3hkVXoxWnpsUWoxakczUEJkWHBaYmdPWm9vQmQ0aDRrMU40VTEzbGhYdmtJN2wiLCJtYWMiOiIwY2Y2NDI3YjExOWNjZDQ2YzAwODBiYzY1NjkwOWU5YTlmNGFmODFmY2FiNzlkZjg3YTVjZTBiYzhjYWQ3OTUxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImVPYnNtYlk2T2xlQi9Jc20xVkMvcFE9PSIsInZhbHVlIjoiR1dUV3E3cisxT1QrcXRXcDVQRVQ3aFBDdUxtY1hkMHA3UUFzTnppTU1qKzJ0T2taQzMwSnZLTVZzYmRvbnZ6VTJxT0hvSTBhdWdtb1E1VDM1RXRDT2xZc0pZRmR2VlgvejRLZnkybE1TTXpsdXNsRkZhcjQ2QnEvVG1vVWVJNmsiLCJtYWMiOiI0MmIwMTU5NmFjNGY2NWMwODk5MGU4ODgwOWEwNTFkZDhkZmM3MTJiNjkyN2VlZjk1ZmE5Y2FjYmU2YWY3NTliIiwidGFnIjoiIn0%3D",
}

