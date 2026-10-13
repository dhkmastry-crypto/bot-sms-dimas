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
    "cf_clearance": "4ztRWIY6lF_Tk2TWLLqHJy9Vjq7ctQRwnMh3t4AwpBM-1791871043-1.2.1.1-s1dviQBzPHvHwkq6F.LygJdo.28VecV2YXFxPcL4t9dLDTykn2PPR2zddMnumx2l5PEdjno1Voj2YTnj4MTBdkvwhUnI7UMa4HbfWmFW9xKH8bhbMZij3ltjnPlQ2jlP5NSWO9bAhDOEflOatkz.wLa0SP4tk_BIs__AnePjdGXtBD1ZgizJBcnPxCpnfDV_7RO3LRbOuEJCBgqBcXjeSBNNQIvBR07wc7dObEDixCOUOZDpPkA7iC0dgEc0mnFeOtzZz8ACGYctwnMCck6vikk8b8UHUP_YGUPUKXhXPPA7vq6VddBZM6_o9JcofMkOtjvguKOZghm.MthvCxmyurteXJFVNAyfOlT8erPRt8Z8ZCqXcaQh6CSEbzPX2amZj9_okBU7tU39xEZkrEaBedFSedQ6uL3vOOu8yd_udTw1aL9DmZcKiaSysUo57iNpz2QGshxS8SyV1z2I0NAMMRxmo_shsFb5xyVtCSDAGDcQNdYaC7qxVPZ4h2zW3xk2asqHkOKv61760Zy02Fxb6w",
    "XSRF-TOKEN": "eyJpdiI6InI0Zk00bzhvU2dwUjBNYkpubk9PcFE9PSIsInZhbHVlIjoiMkNDaERHeFg3Z2dDWUwyWDdaeHRYczhwTXRWNHBrZ0hmSkN1T296VGhWRlBuM08vajdPNzhGU094WUF2dkhJOFRMZW1lSktFOGhEZ09WTmRveGQ2UW4vbS9Uem5seUpkRTNQV0djKzZsQXdsL1RKNDVjdm1NWWZVdWdqdmlYWlgiLCJtYWMiOiJlMGU0ZGFiOGU1ODEyMjdkYjA0MDU3ZTkwYTEzNjBlYWYwYzVhZGFhMTVlZTBhZmQ0NTNmYjM2ZWNhZDNhZTFhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkRVbCtydXJXYXRkWDNqbDlGU3pPbkE9PSIsInZhbHVlIjoiUTBaMjJRVFZOUkRXSUFMc0dBRVhTbG95Rk5qYlJuajVIR21US1BvOG1nYzB6ejF1WXkxSVZtTmVzQXcxK2c5TjNmOS9UbzRpeS9EV2tVQXM2WGlZWVJTNXE4dG9jUWpycTFUSEpYWTJpQjVJUUtIc1VhdGZWOWlJZjNNTnlrN3oiLCJtYWMiOiIwYzU3OWVlMDUwMDFkNmNiZGY2ZjdlYmJhNjdlYTRlZmVjOGNjM2Y5YjVlN2VmZDdjNjk3ZjEzZGIyYmRhMzM1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "j.DGWTtdGOjjF.sXcEUvOUuhy2WKUtIE1XfICPuXia8-1791872241-1.2.1.1-t.4xkvpxtcZOZr09zb6dh6BS2uHEnno3bfBsTEv4q38P.DDkdihaqv8WdSDAoKf6UP8JJhqGBatmWER8oHJKNkP_XKeRha9ko4v0gj3vnmejvxLknGzH0K4oKtjLcf_V3UFvuuQOwlepRCq6206RjKiF4s3um_3E8a7q.QpEosR_.fn.Mou9O413VzfkMgdXNaYqAClWhxiaHHmm7FnLDnJHylcZs9RoznGAjRLxToTQxaI4JfdgByqYB4mDso1rkAnv8RUCtlvitJ_PR5u7Qo0wB4.ZbjVyfQzx14CEVaVGbz_zWy_85pMWkfK4P6jVTqriBwyMz3mqZZ3QTCbBqEisCrH9vMxAIgSfmFJcC7QMsu_hgQJn1ufv4XRFH.2O0FcJzcCrLXpBgc5ltQ0R66NDafqnPTNCoqRKXEthQ8xYUE8TMASMYyfzChEtu2bJjNvJbRUU3zVJA6gylHR2A7_ib_e69QINfwZXc4Oj.foJusR1dL.YTRvvQijjvVEcwS92qcctW_N38zKbKaFULA",
    "XSRF-TOKEN": "eyJpdiI6IitVU0dkckFSRnUyejNSdndmMWpVQ2c9PSIsInZhbHVlIjoiUkZWZUZ6ZUFSdlVhR2orR2dUa2EvZFdDM2pTeUI5dVBFWHhoZVcxdUQ2Y3RhT1lqcXExY3ZCalNTWjBGZ1RneVk2MWltNExCZTNKRUJsYnZ2TXVNNHI0NGwrQ2xGUUx0emI2czFSMHMzeFlWYklNUmE2cG8zamxXbkZHZncxMVMiLCJtYWMiOiI1NTk3NmU1MGY3NzM1OTZhZDZiMWE4N2E4YWNkMzFlYzBmZDA1MWE1OWIzYmIyNzUyYTY3NzdhOTExNjM3NGJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImZ4dy9teDhaSHBTRldidVBmOUE0VVE9PSIsInZhbHVlIjoibHJLWFVTT2hEOW9mUmRoVkxlL0VJMFpUOHpBdHhXMmhObjRHSDhYUHRySmNoUEZXOGJNU2p3U2ptZVhZMExjWHNJcGpwUHlZZlVnZ1pIYmJJcVYxVVdMS2RPTGJZNXNsSWFLbThoa3VzTlNiZWpJeWRIckJZb01ydVpPdzBOUW4iLCJtYWMiOiIwNjE1MzJmNWU5OTU4NDUyNjc3YTFlNmI2YjhlNDEwY2Q2ZGFmNGJiZjFkZTcxOWExMzY4MmJmZGI2ZTVhMWVhIiwidGFnIjoiIn0%3D",
}

