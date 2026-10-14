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
    "cf_clearance": "VYoxNOk2PymheiZ9G7_IrG12R_pWeszKkWTBN.BHdBQ-1791981977-1.2.1.1-fCP7h61tcHM4yEP2hE2yNR_46rJUVfDJl16JoUglPCJoncwFABFBgvmTwHDeEw9Pj7HAj9Z10pTRUySX2eTP0CwtycE5SpUZh0tPehV4_JLv8wm59scUWTSqCPH7hVV11pvgKJyQ9TwuFs45F8kZNbUesV.jIFMP9T3kbdMTHLkRcZaTHOq0F01FB0q8YhWuh5n.fRv4wnG.bL9.l899OsDhjRn2IrLHLX_QaAl.NEpphe1_2Z36jsRR9ciNUOkEt2fgcDzmAcnQJKSs7svSZGuJte4E_wXIlOcLlqkZokgSRB8uLhGobO93fLOh9yLkU7iabVEvYL_849gljGYooiStGrUUN7ikWM90m1CimbrFnw9UduvjCbs_3HgA7nQVsu4Lxp1HPOxcEIVpfEbB1GvDjZZgQKDiq4SlL3BqfvyRSufNF._SBUz62bKQoy.dmDSUq5nJZvCKPJ1Sfhh2xBNYQZJNuBbks36UB.wiGSqh2ufrtNmh2709W8Ybd3B8RIZ9U.DxJsCi0t_RXIATpA",
    "XSRF-TOKEN": "eyJpdiI6ImZLNHptNHJSam5NUGFSUnBYTUlMWUE9PSIsInZhbHVlIjoieS9Xa0ZWOFZRc1FzOVNJRkM5Tkoyc0FwREE5TTU2M3J5MnFmUWw1Q0hwemVERENwb2xoaWRVU1B1RXlvb0h5NHFLVCtaZFdqT0FHb1NhSWJGYVUwaXhhWWdCc2xRZU1tTDR6UzYvTElPVHBLTnk2c21lUk9ld3hXVmxtV055UTgiLCJtYWMiOiI2MGE1NDA2ZWM1ODQ2ZjkzYjg0MTgwNzlmZDBlZTllOThlNjE0OTcwMzIwMmE4MTI4NmI0NmEyM2ExMTRkNDM1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ii8rMlRrY0c1MzQreHdxb0xoaFdWNHc9PSIsInZhbHVlIjoidERmRC9JUndrWnMwbGVFd0taNnY3WE9vN2c4ZXVvd2ZTZDhaTEhBY1ZjTHBUSTdIQnh0SlFMSkMyT2J5MlVMSlNpNEhyVmhONmNXZDNRaisxNGh5TXkrdUtPYTAyUzdYV1FrcWR5WFJiU0VhMXVhNWd6Skp3Wmo3TGZ1bHVPOWgiLCJtYWMiOiI1OWJmNDY2NDJlYjE2YmM5MGZhZTkxM2MzODBiZGMyYWE1YTI0ZTg3N2UzMjM3MGU2ZTY2YWM5MzAwZDJiODg3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "4FF_23_5zFZh4xmv3AQSlLz2o3Fp7DvHUKD._iWPdRo-1791982042-1.2.1.1-msPHBX8C3pR.rnMJYxN6A6FviQL_MMA0gs19cSl2qjtmXYArnfJdZvmIX6YRZwgds3h0HHSc2Bx7v_SLFGVCUELk4hCKaAaM1JTdXMw0RKBzlUTipAiu0UgAzW6VLPia8fpqlzRVjWeSoVyhU49z6zS8WCNdLgormiusWqSsiX1qZrROm7e0mqYHAH3B3umnAR9am_2YUfpmH6rMCOx_ohnL8BG9ImyIapfzkLIa...e6M.lD798niRS7LyBd_eTfuA4EXPFVTFx1k5YdujsnrsWCPU9XkpBOHBoBLzW5DVup5CDf5EmSH2dXDBwwJB68hFyefWY2bm6FqsbH6LejoNNeKJaeS12sE02q6I8PMqmNw.Q2HwvNfqf8YWvPyK7xiF.MeMGDw1F2PH713dIG3LKug6RD7FanU3E8ywPKLtFhkN6w.6QEpAPCvCYnWpN3zj3NDgx7onpRKAsiD989_pI63DikyHd.45RJRPgDfzuSfiO3IG3bK2F20HkIdm7euP_ZScTAtUaf7D4KPSHmg",
    "XSRF-TOKEN": "eyJpdiI6IityUmxGcDY3UUxEVXg4V1ZvVEtBc0E9PSIsInZhbHVlIjoieE9TR1BQQjU4SVhyWThDbW94aFNkRE1iWHZTdTFtc1k0YllHRURITlBYVE1DanlubzNDUWZOMWxndWdtelpYbjI4YUpEUXVhTEE4ZjJlMGIrcHc4a0hXTWNvQWhNZU44SkVUS2JicXNsenNXWU51Z0JBNlYxdE1wUWVmV3pCYVEiLCJtYWMiOiI4NGYyNmRlOTZhN2E5NTA1NGI3OTNhYTdhYmExMGUxYTYzYmFlZTdhYTFiYjNhZmJkZDc0YjRhNjk4YjVjMWFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InBGMjhXR0tBblgvMS9zYjArbC9TZkE9PSIsInZhbHVlIjoiSzRJdHBoUEswRVlkQUNaaHdpOHEyZXF5RDFuSFljcEthUWl3cUJJVzZJOWFsMmZuRzFpOU5jYlhheTdvbHFJb2dKT1MyeGtOQ3NqSXdSTlk2bmhQclYrNTFmL3lBeWF2S2x1T3lhUExJcVppUmp5eXdGdGhFN3JENWlHaUlzdlAiLCJtYWMiOiJjYTJkNzQ2Mjc3YWQ5ZGJmOTE2OTg2OWFkZTMyMzdmM2M3NTZmNjYxMTE3ODg1MjE3ZDA0MTI0NWM0ZjFiMzliIiwidGFnIjoiIn0%3D",
}

