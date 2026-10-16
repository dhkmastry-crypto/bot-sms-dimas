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
    "cf_clearance": "hkr.7Y6Xz4Qk3z4BPFR0R6XfV6sHMFasON4jahtwVLA-1792136198-1.2.1.1-hWhsLK1k3g.u0QruzJCLr4jby0E2qvMCSWLxZW..Gfec3ZbTi1UK12N1.2fX6vvR7daicGrz65bFsMFiJ21iNhWwgOAPGYAqthJkbaxvUIbPS45SyhQKK5QMprCI4NAGR4S9nwCamD9y8W3Ol8BB0d9zhgAXyl_Rg6H4G72xIzIx.UyGxS5RXT0oki0UNoAvAP1eI5UQrdR8j5NNIqgGyEwsxDle47Og0ka8pGBXHuM._y.LmGm_PGx60JXARcmKh4UWKHn7r_xAtayGsoTRqf7BqijK8M0zAwIhBGq8Mb6L7DAqzkgvq9dLqRYBpH3k3cWJr_IYTohvWhmMf1R7aPI1ElWalMIBzFWzrc62bIfz15.aYZ98wOP4m9Eom5jfK8p8Zrjl80M71zZoF29mY..ygGjQd49TEjczfWJmDD8DVpzUJ2XBBK1v4R9zlxQvIOmvdInXXHHrgkHwOL1WJABpA9Q_J.liAlKh8yYwnHK65ENAyk5z85QjcNX9g3UE5INaZ0tO7RfRAtQ2cioUpw",
    "XSRF-TOKEN": "eyJpdiI6IjY4Kzdhb2ZBa0NaWXVYM1BJN0djOGc9PSIsInZhbHVlIjoiMUtYMmtzdW1jcldqM1BuRFJsWU42T1F2TURKOFhELzcvM1M0REM3M2lkcDhORmg5ZmFoYTMrdXNwTnlQN080QUZyTDh1dGQxdVpNb0tJZWhpSzlLMVMvNmV6bUJkRXRWRnlCU2NuMHVzbE5KcUNGNTlYZ1lrcXJWQm5aVjM5RFEiLCJtYWMiOiIxMDA0OWQyMWJiZGFiMmFhNjY1MTdlNzVmYzhhNGFmODg1ZTk5MTk4ODc3ZjNmMzQ4YmZiMmY0N2JiZjEwY2Q4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InVSL2pJSVZyemJoRjFyMEdSeFBGelE9PSIsInZhbHVlIjoiL1Azd2g5K20rRUF0RFRmWEpxK213L2NnL25malRMRU5hMURzZmxLSDVaQ2w3YU1GZUROZW1sdEI2SlJiMTMrYTFPeVY3Q3RDTFJqTHMwNCtvN0lXc0ZZc1hjK2tqZTEwdGZJSG12QnNlb0JYYnFRVmMxd0xCSWsrMGdsZllkNmUiLCJtYWMiOiI3NjU3MmEyZDBkMzk2MzBmNWUyZWRkOGVhOTcxMGE0MDgyYzZjNjg1NjI1NGU3ZWI4MDE3Yzk3ZTZhY2U3OWQ4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "6nd1ALmpbHvYDPLVjrNNtf0PrAX9WCGpQthqM91MuHw-1792136209-1.2.1.1-JdGx_NsTEuHy2ffag..0s1gv2jQ3zuJlXgIP5SD10WUDh2oX.vbX3aD8...kjRzvT5EdleQi9p.FQD4h2QNKN8kKZrRetcxE0UMXXhX2Ew.VRrV6AH428q0Xp3Yr_V0.ZsZoqg9urSrePSts4xxcvBECqqWmO7avPiVAnk0RIkl56xSG9xUpUfNuAXUko2L2GctWXuLrIzwTh6Fn7e7yzar_wzFqhFuEleEfa2i_MhzSPO73TknnMUa5cP41CiDVyEZO_U_Rente_TGlVQ4B4g3mwSioDc6vVWppylLv3iyLVTc6fsAMQsZLQZmC5io7ZAhTy6EEtk5AY.p6E9OiwO2lrfEsWB9ysWlukeIZelEBuQl3ezWPgMtwoOCH09aSfcfE0pPvKS9kU8JqWHiJZAEFfRwpEAAOZPRuXrY6XfY4xpzLdmc3r1FXQ2k6_JHcpQwejksVxiwY2r6FTbyXl147M_6In.GiBg8cjaGX1bEc_2quwD2FRjecYZRYE_Js5ivwlWoz1UQEtfT2FFB3mA",
    "XSRF-TOKEN": "eyJpdiI6IlhXREFCVk54cWRYcHpObTZtY0NyS0E9PSIsInZhbHVlIjoiUExuR0FlWnRiWnJJREZkNGk5ME83Q1lLTlFRT1lSaEtqWVAzYmFNQ2puRHNabjJqT09BM0dBYVpFdjBjSVQ4TlphdUt0OFlVeTMyWisvMXZ1eXJmR1ltVFlsdklMRVNEK2ttblhSZ1Ziak9la01ZOEg4Wm5mMHZkY0lLZkFEbngiLCJtYWMiOiI2YmYwNWU5MTI5NGNlNWNkYjFkMDdmZTI1M2RlOTc0YmFjZTcwYWZmMDMzNTQ1YjRkMDYxZGMwYjI2YjA0ZGY5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IndTOWdISG1ZL0hnaFBDVGMra2pMTkE9PSIsInZhbHVlIjoiUEEraVhJYndxUmNHbkF2N3EzM0diN1Y3V1BTeXY4bHZ4WnIxd2xNM0hyZExweXNicHpFaDg0UXYyU1krWk4zN3VNaTRGakF0ZDBaTGYwRUlYMDNTTTdDQnB4ZVRHU1FBQ2VwNzl2SXdNNHE2a0ZGak9TaXRsVWNtVndBcjg2Wi8iLCJtYWMiOiIwMDdmNTE3NjU4M2NjZTQ2ZWI4YWUwYmM4NTM2ODQ0ZDQwMTI1Njg2MDQ3ZTQ0NmI5MjMxMmIzOGM5ZmY5NjQ0IiwidGFnIjoiIn0%3D",
}

