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
    "cf_clearance": "kMM9OLtQFhoT32oyFJ49mrBj8ybbGkAeSBu6xGCKIp4-1792119901-1.2.1.1-AeW47NH6Fls.GJtpcV.z.cLKRBTfrOPB4T0Pb5x.ax0tNUlY0gWJer2CC4.SGOMBODZitXrAd5aT35_KsmT5mvgGtkC329p3Y2.Bc3WIIz9Y_RNfckW0F8PPSQBPWe9tXk2ToWQI2fEyKIKk8_O9zvRw8CVe9nhQeVIYmWEGsDDNpH24N_O.zydar4YioPy0VuRDzj5H2EqIycbYM7Gv6eKUUMBClfTsN40J8DMh1LUmSJFKN1fgBYNWBd0tlaURWZeyikGROGlGuEuk3x15IdjQfdGAIifDVCjcCIMxI7cJos5nxNdsOiFzcNDjH9PbnJonNPxpzM.3kqJXRBVnvhQK4McUtu11sejK0.SJOV1luLPZePEVX9qht5rvelOuN95ScbnH97VB2t371_fJ.VI2O5Wfra14XNEwP_zHjarnWqza_wT6m.b_83hUti3pGBf98Hn_7HtDqi3Kl4Nx2Nexw1YG.R4djKLGI92fGiLTo4h8YmiX6hENuIMfmHax9KnWT7Hxir6uNekqHlhicA",
    "XSRF-TOKEN": "eyJpdiI6IkI5RTZVdXZwa2MzM3kvQ2Q1UzhmN1E9PSIsInZhbHVlIjoiYUsyditEY1NaQ0xwU0s3TXBqUzdKdE5VcytqRE1hYk9ma3pidUdtV0piRzlSZ0g0eEt5elFlT2drb2VKMzNWMUROWW1xdXNmbUc5QnRWNGxaMzlETlJTQ1RzT3pGODZVN09ZOXN4MDJCcHRpUHdQL2kzTWxXMFl3RnlzcUVhNHciLCJtYWMiOiJjYmM5ZjdiODVkYzMxMmYzY2U5NzhhZWVkZDg3ZTdiYjcyYmUxNWVhYWEwZTA2YjQzMGUwMzlmMDAxNWQ1MjdkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjZYcmN2R1h0VHk1ZjlTbUlKYkkyNGc9PSIsInZhbHVlIjoibkNGOS9ZRHQvQmw5YWVXNmtldTJxcWNIQldCNEFrTXpqVmdyL1RIQkEzZkdQUmRXNmVEKytLNG0wQzB3cmNCL2xHQkgwQ1pYbWsyb1dhUHZhNlFqU2RCd1BOdWZHRnRidk5GdEpmZDJMK3c4TXhRN3QyMGljT3N1Y3Y3Rk5DbGciLCJtYWMiOiIwMWZlNWZiYjA2ZjUyYWM3N2FhMjk4YmFhZGEwYjAwYTZiYTJiMThlZmU5YjA1NDgxNTI3NzBhNDE2NzEyMzA1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "mVKH1fD1ClwsQZH3Z2uq0ZnMR1tAhPxEk.JZX_6hAhI-1792121684-1.2.1.1-Hq4tcAeQ.yuyqHc6RPEJkRnHKLJBG5L5xKEr00P01a9pzmRRwr.sGphB2aDIpzTJ3IUoPeeLMiASHln8A3wcnh86HgHRnifssFDPgO2JlJVVhzX_Lk_vvUjh880_In39auSmm8mmmr80zoiAJ3vMDjypI.WBERqd4pZy6mrjuQPyJlxUC8cqvjBA4NQvKbN5ApSTP0RH5eo8PHNbL17kUHIatTsHhaGnouP6Vmu0h4_yHTJajTzwt9TVdfrU6uaGLeUSC1M4ZoqxYxORLM5.vedSb6PI59czJIK2pI_zkeiBDn_3_UPW58RZLEKwncRkBhH8GUg8b2cMUaxscqeSOcyzHCn6rvpBooCjH8.haX7c3030WkQtuUyJj6kHZP0CkURNXGb801c90.sggeXjs5WwSoGn0DGY1cs3EcSUt_CBJfrl08lh9nFA3OK.2vu6UI2EmCDAdIK475umOO6slDE0H00dTIactz3RY2oX5YSFZ82u0xxT5oBddYW6RdwmlxBwTmHh6FaVVBNPK0FugA",
    "XSRF-TOKEN": "eyJpdiI6Ii90VTFIRW9JYnVhWktodEI3ZUVtL3c9PSIsInZhbHVlIjoieGVqWGhoZjBRZlpnOVNWOWg2VUlTTjNmNnpQMlFnNmpCTGJuZys5c2xBUEZKWjQ1WDIyQWU1bTdia3VYdVZDUVNrUUlKUDdJb1FPSHZGd2hyaHhrakQvZDJ3V1F4cTJDUDU5TEM4MFFVemZxSzlrL1dCWDF0SjZuejREWGtnckMiLCJtYWMiOiJkYzA3NjEwNjJkNGJhZjdhOWY2YWRmYjE5YzUzMGVmYTU3MmY2YTI0MDZiZTdlYzczOTgyZmJkOWNjNTNmNjk5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IitUQnd3d1NDdWdyUXppMlppRTBEM0E9PSIsInZhbHVlIjoiY1NkT0dzTUtkUHpUQURpd29Id0FqaDU5cGNDdXpTbjM0WFdiVmRsc0ZZT3NUMzQ4UjZNM2IwcERIL0RneGE5M3d6Vm9lemIzRXFZUGNJeXQvRmVqbTVIQk02Y29IZlN1SHpqY3pPbFpzWk5TdEN0c29nZjZXeTdZSlpJalRjeU0iLCJtYWMiOiJhZTMwY2M3ODIyZmZiMjliYWY2ODU5NjlhYjc1ODMxNjkzYzFmZWFhZmQyY2MwODI5Y2U5NDk0NmExMjRkY2VkIiwidGFnIjoiIn0%3D",
}

