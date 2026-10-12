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
    "cf_clearance": "8AyaP6tTTbl6zuP4TDTojLwDyMYkR6Ev4zgc_PDBYsY-1791829446-1.2.1.1-SpkMsihvHH_eNQviXds2U0GSdT6erBSiLSDc.Ukx8wa7WaSDixIVdeVuUHritW3oUgJmIG.iZ.1dalpShVIpDSg5dAXyRdtig8Sf69s7bOJiv9u_LTW4rtvXv_s4AYiP9z7m.kfkku8LCrB.bjv9o9.itDVKzP3pVspvTSghutKVvikDCIeRYyk8lxJ6ulxzKo9WfM7vGCvzYtMCSQ1LnvNt8Qf6dt0_tXH7CzRayG_l.PSwuGU5rKzV_Z3KeiDWU2Ln3zQ7XLn4EVjmE6WXtRboAankkSNlPHGqEqqr4vVZMjvbHgsTipcM0t4iFMZsrh1XZmybur0TuIvq.UaJV5njqj2g.WsDMO2QtS.tlmdw0I3xGmbIZHGRomkF1mGF17N3A4656epmdZHyV39hwFJB0doju1EkUi0.3GHUEcp9GDqVCGenh4dadC.aTcWhUBwBSMLvLu.fMn7j8YlEt0sgqGu7rqK4a4sqQp4B6YRKqtDXicuuFXTN.H1eNIz.WdU7iMsrKgcpoN33HV3jzg",
    "XSRF-TOKEN": "eyJpdiI6IkJEaW5ESVBVNVNPK3kwUnpiaVU0UlE9PSIsInZhbHVlIjoiM3JJeFkxRXRGc0x4ZmlaS0Q0eExOWHQ0MmJzSy9vVEd1RS9QdjdxdExob09mQ2JyTEZpUnNpeHc4YlpGZytqdjNaMWJhY2dTcGp6YVdOYkpwdFJOazJDVXlQVXRBbDdoZHdNdUFWUkZJTzZjb3JJWVo0Rmw5ZjhhUWYrcjJKc1UiLCJtYWMiOiJjYTRmMDRjOThmZGQxYzY4YmRiZmNhZTE5ZTAzYjUxMDQ0NzQyZjcwNDQ1NDc4OWE3NDUyNmMzZjYzNTRkMzczIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFpNU5wVjhDL1BTS1NuZEcrSjdmdlE9PSIsInZhbHVlIjoiWFlCZ2JFWmQxeGtnVy83TjNuL2xKUG1LSjFJQzJVR0F3UlY2MUEwanFOOG90MDJoM0ZHZUR3aFE3THNyRXBtWGFXVVRZZXhwdkxheEF4NEFrRzE3bGVZcHppVGlLbjRDNHBuaC92M3BaNHVhU0JkMXVJb0xmRUkwRnQzUFZjYkQiLCJtYWMiOiI4NzlhM2YwMjU3ZDdjMzhiMTM0MWY0NmEyZmJkZDhhYTVlYmU2NzJiMDZmMzE1NDkyNTJiM2RkNjk1MjJhYjU0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "kiBRHFoZlm2_c3OtiVHCpElUaaf_Kn_YTFjUGrps_Yg-1791828609-1.2.1.1-jpE6MXJsMBHJp6jEgL6bO7nGc5OZsNTlac88XKXmNvMDdoRBVnGMo.ueKIhyG0TnXolPmbLYwmvj4SJ95azD3nU5dFyl9JDemKxWW.ZC8bOGs9qwnltOf4d0RKcS6hd3250ZmJvfL2dXjXUUP9pBQHW2mdHLqXzBIj_o_U.3GJa7WexqPqEkbm2hcryDBrczoc8ptYCtEO4o3XMrxQ1pmxv_JjGUH48bgJbyVXLqiMbArYRIHCbx5kvPWbK39yfiFm6MCqig8.vCXsmHaOsZibgzAf1e9JRv86L6M49ehG4q9jYt5J5xr1Avd34EvhhaUbUXWcbr8wyMVwFAsR7APhEveUOZ1t0D4vhoBwkWOgAjRPT34wpDF4EwXGYMMBUOej8yreXS22QqfdpKkK0q5i0BVZGKkok7iwX2WvQHhx3pVZNZvWZaWS.bshayJQoSZJKlVdSywcKEEw8oX_cFQR49BnmAKv31pu9JhR0yEez9fbi4BbXdZpKx3Udf8WkxKY5OMMp9QoZBUQFmSFyUrw",
    "XSRF-TOKEN": "eyJpdiI6InN5L1dGdjNjaDNlaFczclpyVzNBOVE9PSIsInZhbHVlIjoiWHF2SFovQUhwMS9zMGZKVTZLMXd4MFBxS3FlSXJqUlZjRHRsQjJiTkx3OTA4bHJPL0tKS085bG9mTCttVnZ0ZFFKWmhpUDBORnl5cmN6Y1oxeHNOS25OaGtYNmZycURKZk1TaGlZaDJsQnN4OG43enVpanE1R09BTEc4YXk3V2UiLCJtYWMiOiIyZTFmODQzNDRlYTY3MzJiOTU1OGZhZGNkNTk1YTkyZjliN2YxYTVjYjZlOTM1N2UyMmFhMWQ4MzFlYzM4MDExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImRxeDBCdUtlU2IyOTdCWG9XZG1NWnc9PSIsInZhbHVlIjoiTHl0Y3JJQ0RMK3pYc2QzbkxRbVdwYlJBODlCdTdPVDFQQlpmQlFQTVk3Zkdha2U0bUFBTTRvQmhSdFpwM0kwMzR5N0JpVThHdnRXUnVlRzVBRkVsQ3FvRGI1M2xiZjlYelBzV0poR3RVb3NOSWY3eWdNRjl5YWUxRnk2V2FqWEgiLCJtYWMiOiIyNzIzNDQ4OGJjMzQxMTlhMjEwODY2OWEwMDMyMGE3NmZlMjg1Y2I0YTZmNzc0NGNhNGExNDMyZjY5NzFhODAxIiwidGFnIjoiIn0%3D",
}

