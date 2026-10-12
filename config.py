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
    "cf_clearance": "AyBlHq7OetYbS2tgB5hNOYIXxQgb4PClRFSAhe5mrcE-1791843924-1.2.1.1-gAKk5lL3viSjp7pRbKoNtNn4Qlnc5fvBnjY6VAxT2oq5A.KLrqBKK0TtB4.X7kP8haxyFKrj28U4WHDk35XYcaKy2jPsKKILFnL03tR0tG03ooCU1bnTZwVcYiZsc4hh0gT_vunhVYjJBh_abjHr2OLgX4P1mVdJY3IMb4XVcTA_O3tVrhhbjg6hD7dIe3CEU7NgctuDEqscztI5cyYW3wnhJeFFO6QCjg.GIg_W2K9uzxcMSxrZ6MLpHJFPfzrKj._bPvN5h6JOa__VGXktc4QLZe9P.Ol7Hsrsdg77ZyhbbetypaVm2dTIm6icHjQVwQveIDLkUoJc4uelGc1s2sS4l1p2Iv1UN.abjzp8GyuI0nPrvnmfBBoAOU7vS_mvK1RmNUTLxtwxBIRETkTMf9rMhalXy_vU9qNArWmJr0XxgmXkXIcM8PGZHfnzqAd8eX_6bvz27g473pHDKIe9uz2pnKkrpZYrUlG_5cDUMpPzL7pY6BK85iT.V3eh.wjhC.JbVY0xb_Z5iqELwluJvQ",
    "XSRF-TOKEN": "eyJpdiI6IkcycHloaWZmQWw5V09Kb01XUU5weHc9PSIsInZhbHVlIjoiVHpFSDBTOWw1YlU5bkw4QXVBKzhkKzJkbmREdDVuWFQxMEJQL29zUEVsSFNobm1YWHRaRkZzQkx4dXlaaVdSdVd0eXg2WGtHQlYvSFF5M1ZkVDI5WDZlVUtXd1RCSGdmTitZYmxoUDZKRTdCRTRlZC8vd0kyc3N0UDZKVDlVTmIiLCJtYWMiOiI3NzJmOTIwNGRlZGJlMjZhZDQwZDVjOWZiNzM0Nzk1YWM4NTFiZTJkMDUxZTk2Y2UxZjE2NjlhYzZhYWIxMTY4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlFhMzRPYXZLWGlmR0Q5Ym9RWjRkUVE9PSIsInZhbHVlIjoiZHhHZXlFblg5YWJJQjh2M0wyYU5YQ1NoZnYyNzBqMTl1aVB0aFJRSFAzNlZEc09SYU9Rd09LaFVSbmV6VkEyTFp0dXhjeWlIZVZPY0EveHVocXR4ZU1VM2Z5REdJM2h4LzFjOVdmMGRRVUhGOTloc042M2krUXl4YlNIZDJCbVEiLCJtYWMiOiI1N2FkZDg2M2FiMGE0YTAxMTRhMDQ3ZWUwNDgwYTlkMjE0NjE1ZDg1ZWIxMGMyMzg0NTg1MDQ1ZTJiMDI0MTRiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "OngsWMoayXcSAE2gJQUU1yJtAA5ma_DXO0ks5iWu4G0-1791843150-1.2.1.1-fXuYvEcd5ZX8qoC0qhuN.voN0v3JOsqFCgr7fSvUqXam6Tz2Yuvwtu7luTIsSyZPK_6q9O.jAdUXuUpveE9nwPbv5vclXuWGtHe2VccEgBbwDtDz8oJUE51ZRt4CYZpa3On3YK9naQPE4NyKi7c0mv6AObZ7UWO1amKmduK2yik4DDtr8VxGXIYPlL6HFXKMb27WGuAZyZ9XFd7r78Vn6dwaXPT.TE06wbfwcYUYLtUVj5V5t8XmwWLOmZS11UKU.6Yvhn7HgV4zp7s0jd0pt7ZPq2uGMjPCZYcB_4CL1CtX9IZGxva55LlORsQETyviLeyiDFSSVHg15ll8U.GUD28IMklST1MylvD751obNQNdlVwWaC4dNL7wg8eF5qSKQjPSGoGUI0ot6Mqzvh4UXVPsB__BmWHrGhpiaBbkz3DcDWQp5hekMpjdD0.tC.qqMbT1cf1ow2GwyfwfllaQZbrKY6CBSO545WJGmwGrjKMRWWRoRIqJU6HIHV.91A5NV2.6LnZp6G9Dn8G0T_DnUw",
    "XSRF-TOKEN": "eyJpdiI6IkVta0pZZGxOUUl5WW9kaDV0SGVLTFE9PSIsInZhbHVlIjoiYmZVRHBpZkFnNnluNWFDbDZmQmFrTzE0ek14ZFM2NDdnZDAydCtrZVRhZ29qTHpDWXhFSW8yTmNQd0xUQW9LV2czOGhKdlJzVFJVUTRoT3ZERWdxZHFiUk1lZllSTHhaYzgxUW90eTlwcnJneEdjaHl4WkZrRXdyQzIvMGNheEUiLCJtYWMiOiJkN2EyMzMyYjNmMThjNTQ3ZDRhODJlM2I3YmU1ZmY2MDMwMDUzN2FkNjA3N2U2MDQ0ODJkM2JiMmViZWFkNWI5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1xbWRHU1k2SktPMFdxTTdJakdNUkE9PSIsInZhbHVlIjoiS2ViQ2dxamhaZUpBQ2RIMzVmdXpJUDFsQ0F3MW1aM1o1RFEvaDlGUzg2U0VJcjMweVV4SDVhbytORFZsL3pSRUMyUmJFMjZrbm1lR3BIV2VnK3BSaHhRditkRDdIWTFNTDU5ZzNZaE05TDFUQVdLdncyTHNwK2RmSWZRc3lpakUiLCJtYWMiOiJlNjA5ZGY3OTU2Y2RiZGEzMDVhMzZlZjhhYjhmMmJhMmFkMzkxYjUxZmZmOWNlNzBiYmFmZWYzMDM3MjEwNTU1IiwidGFnIjoiIn0%3D",
}

