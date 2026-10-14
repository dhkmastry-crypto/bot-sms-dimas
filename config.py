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
    "cf_chl_rc_ni": "1",
    "cf_clearance": "F_LPxz9x8rJ.w1IXi.vh.QueaiYDXFTgYBaqlj6ud2g-1792008392-1.2.1.1-C4rY5EO9rxUntMtkE6JEU7vKa2U2PVZVvSHDgV61U31C1I2G3fH.Y52PZV7PYdXhdyDSLirVio2s_RjKSBOh4sLir.qxix5vCSHbwSFNoMm7GKKYWK6vLYoNfvkU2uy9g0NibKZm3noMHwc_i59bav3mFZgWu0O0RwEPpKzEE2vR5DFc5JJx8yx_NCIcMIqO9pFFS7HTIMVUNx2Jm69vrsUaO7puYNHhpQI1UdVZb8KCu33ut9426EEULR2nHpuhNutpqLDFGIBpb0JLeUDEJBIWhYfDmEspZQrj5.WNJzjP1Qg9Cp2Gu_IyR8dNOUOBXu86YCZ95XY5WZhxqMV04lsFwvog5HQn57yRnldSS0McGwuskq5h4bvwYHThL9GfKkQsHQl1qyaMAQuiZC6wl8F8YnFs1XSo1DHkaIH_pRIGflNZFmu.OPKdffxUwWjSbzqtWnN9PFzKNM6qpkLD2j8HtCJPJsjEcD28RAzSs7CZEC546Aggn66Qg4_UIoi8Oo18twMdal13aGX50lshDg",
    "XSRF-TOKEN": "eyJpdiI6Ii9TSzR3NkVjWGpPTHdCVnY2Ulh5aXc9PSIsInZhbHVlIjoiS3hTZFFONzhMTjJybWlJV1piWnBkTEtscm5DNklGOC9KdUdpMXFsUlUrd2ZLbXNHbWFaMkxhYmZJckhIL3VDb1JiUkQwUE1vekx0N3BLS2VnenNsUGpsMlozMmZVNjN5Z3RGNjl4cU9kdDg2UGIyRldGVnJCZ2h3YkhNQXNFUDciLCJtYWMiOiIxODMwY2EwN2I2ZGY4OTlhMTdlNzlhNWU1MDNmMzZiYWRiZTcxYWJhNzU1MzMwMGQ3NjM3ZTQzMTI1ZDk5ZjdiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InFqYnJwV1NwOVptb0dsTWZETkR2eGc9PSIsInZhbHVlIjoiSEpvZjNmYzRocHpTZzltM3k5TGZ0MStRTURETHhMdUswQnZLNi9UZ0JoWlhzRDNwUTNqMzdVVW1rVmk5NTBrUlBQSENIVk5Pa1N2Z0RvY1hkakV1dHZhODRYV0wxMVlQZzlOQ09QUzZPRVpPV0RjOEFoakVzQTFFYnRGWkxxbUoiLCJtYWMiOiJkOTcwNmQ5NDY5ODNjMzhhNjE4YTg4ZjA1MWI3NWU3ODRiNjVmN2NiMTYwMzBjMzc5NDAxMzg4OGY5ZTM1MmI0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_chl_rc_ni": "1",
    "cf_clearance": "lFosJK9GXnrMVl7KT.2vQ6RG4bTgFSsUUTi5OaCbdKE-1792008362-1.2.1.1-MjiJdSGP_nin_I8poPcZgc7QRZgO1QKDSgq7Exhwbu134GUmukLH9_vPxc40et3DNO16uZAC3Tlehgdl1z8wU.V1wotbt8ahXy27Ti2gLPhIG40kKpzyIZmAltZllrGlZ5_bCydyJnhOY_lpZ.wWgw6eBx47YLQZDQJxwWObysZJyn8WF7Pd3IZ.h.6rB5zl754rmZTab13RxVc2bjJcTogJSCBbuLAsjnwZiC5Zc9BCgVpz9hb9ntp3f74v10Csk_74Hdd06KucFzsMRieQvIopTUhVlIJ88EJChQl3TS4rmHWpEyYKwV4WmlNorZpf5REqQWDF9nwoUUJaw_J_xlo1AXLod0uP27bzwOaJeh7JUOSsT3lEBRuWUSrTovGC4mVsZx2XmZe7iXH6s6y0h1.1Ib3fSCJJsWjPSBs5xwCak5NG6zG.MeOt1CeYqwQ.um18oMhVc_9N2yHt1Wavu5Y3pIb0dqIUZXfFro9PL9DTMFG12_7CwaBvMUEEkIuvFIz7pYOEUQ.xBJsL8KExzQ",
    "XSRF-TOKEN": "eyJpdiI6IlNIeVhVSEFuclZjbWJQVnFYMmU0dEE9PSIsInZhbHVlIjoicmxvRjcwY2ZmSitpaHp2T1RIbC9MZFRVUXlhRjlKN3pRU1c0OWNjQW5JVHZreWIxYXduTmplaVhSTTdRbHdPY2NPbDZtTDFRelorNDlxQ0U2Vm9ObEZDTjZHUk9GamZBWU1MeU5KYmZTUkJaSUxGV2lPaFh1TWVGait4QmV1YXAiLCJtYWMiOiIwMTkyZTI3MGI0N2YwMDdiYjAzOGY2MzI3ZWFhMDBiZDIzNDllZTE3MWY5YzY1NmNjYTExYjMwNWViMjdlZDliIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImpEVktsMXB5TldsbVdQWS9XbXk4Snc9PSIsInZhbHVlIjoiRnd4OVhrNHI5eHkvbDBLWHFiUXRoVTkrMzNJYVd2VFNyK3RCbzViQlUvcFJSbkdLWGN2dkM5eHpzZWw0VkZzdmJ3SGxVWXhWWEV2WWZNdHJ1NHRyVTc1S2dwSFJlTzlqS1phWktSc3NpbHFoeVlObVNVLzQ2UGlTdENGbG9qZEgiLCJtYWMiOiI1YTI5MjY4N2Y0NWI1OTc5MWU4ODRjMjcyMzk2OWE2Y2FkMDJhODQ4Njc0MTQ3MzNmYTgyMTA2MDNkZTM4MjUyIiwidGFnIjoiIn0%3D",
}

