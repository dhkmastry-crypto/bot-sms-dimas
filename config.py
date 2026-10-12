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
    "cf_clearance": "H6Xlbjl6gmTrTDa2uTPFr3oIK0aS1f8QXC3lRq9eyX4-1791845733-1.2.1.1-8wJ3nPjP76.M0UvQ5jlZIuIpoNcWLpbzGJXT8csncwyDLykmqHkaeNlMF5YKLy2Or_ScQ7Mn1AGF0s4Kv5C3SlkJJWJ_SYmsbVn32MP87I5OsKdGDC.9kE4TnyQmsRcsz8lZfPOMPSOM6mpERq._LolHfDLE.gNWWAK9UWbTvkEzHhr4bUXm_NXvP4ILQRBcO3nA4cdsD0NEycE1gORDNtYO.40rRzLEXtxakbrkb.Og6Ed2dlYTypBU2_wM09OqmD5pWWIh3db_EDqkpCSBLauGj4rfqQgTz1T4uaK4I15xaJDK5byYN9noCGKC04KB0wQpEt5acReRmaD3BsjAEXN3vVLWkYcI_hhpYBo4m33t0L2drg33ELTbZl4M5RWPC1VlSEIoyUnJho72fuu3qHvXZR2XFtzV0fYVQCOiI_KyjHbzkdY7a48jQmuXYsgQzLvqlCcnV_.AR4Y027LYljJ_ySZnGVXgQXpLy68kKlbEqzfvvrLXvZa6XfZc3zf3wZltff1aXkyJ7KkQ5pNe0w",
    "XSRF-TOKEN": "eyJpdiI6IlVGWG5yOXZvSXQyTmRidkoxQWxxVXc9PSIsInZhbHVlIjoiWExWSjJGWGpzdUlxMy9EdHY3cnNtUmZQM3pOZDRNS3pOdW0vZXV0bmJHVG95aTdlVEcxVmFOSklNaFdWdjltYmVrM0trTFV2N0NwVi8vNGUvNVlVZ0tlcFJjQ3QrRzZGUXF1bGRlYnZKUzhKSGErQ0kyNlZyUVNOeURDWk5IUHgiLCJtYWMiOiI4ZTU1YTJlYzNhMTZkNGUwNGNiYzY1YmJmYTljOGZkMGZiZGRhMzM5ODkxMGNhZTE5YjljMmJkNTFkMWI2MTU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJicWo1RjU2UEFuSitQUHl4aCtZTHc9PSIsInZhbHVlIjoiQUx5SERMeUxwcFhyV2M5LzdNRFMrMU5wSmV2VS9GZXpGdVNYSFlnaUFBZGVxWC9BeFpMTW9Wb3QrMTBvWXpQbXpVSDIzdElaUlozWHBhQmlQUlRER1FrVmNjM3oxM3hKYjF0eFhXSlRNMVJWWDRnWUpGMGFpbjh2STMwc2NCL3IiLCJtYWMiOiJmYWIzNDFiOTVjMTEyMTAwZmE3ZDUxYjhlNmU5MDlhMGNlZGIwZjhlYzVjYWEzYzFkZWQwOGQ0NDU4OTc4NmRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": ".VFA4ph23icSYdH8OYjwr6rIcQYdfMFCRkvaPGo1aHQ-1791844965-1.2.1.1-h1ZRGEXTODGdXPUWvFLa8KYzEBmmUh74cNjPO.z.y1b2ZMnUefqITmCPVymcIPmmDI6hci_zSEIiu0THB_thWpdW0ZcCXHoiMfL_uSTdc_BqSUBlZKRSeKkJFOECLqlIBsHitErePCf1JBRFn5n8yDXc9WA3uGJCy2nOHuMGm248pdMuPKoXGsixfDTCmVZtNtwZ5B6SDH1GNpY2OGhfbKEGBcSTYyEiT3RaJyfvRB.4yADQ1B39obeYOm2REs3YSvUW7ASFCQZQc2NJtIzzmfduTWEmGqXe2bv8enIk30Vhg6wCcoHgBLgN1nVj1HZ5yArrzyyudSDdyNcgMuXzcoNV6Sgnc1E1JB0grxm8OE1M0So_0p.S4T8KGErl9d27WWYhNIHoUcndevyi.oMBQJxIxCAYmJin1OHkSJZ0GlsZnam1RdtX4caPASa21SBkAJQq9Gg1Y.JUDhgWrZxO9frPRnn1XWxcUOYFBfIHc556YxFe_qLoZPx3CGM2M5CNcJESte34s5zo6RBNCqye4A",
    "XSRF-TOKEN": "eyJpdiI6IlczL0FHTFc2NC9qUHluR2xrQjFTSWc9PSIsInZhbHVlIjoid1NGdCtiRnBvVFlWZERmV1pqOERuWmhFeFEyOFZvN2EvM2hXeWRRbmxEYnc2TUxua1EwUUR4TGxrQ2FiMEJHemxHRlhSMnVMNUFFSTRjOEFWcWZMZ21wUEtvRTYxZGFPTXdwZC9ldmcvVVpMd1FiK2JjWVEwZzcyQ2tEanRRK0siLCJtYWMiOiJmM2M2ZTY1MmY1ZGIyMzI1ZTRjZmNkNmU1ZTRjMDI2MjQxYzhkOWRiMzg0ZWVjMTU5OWZmOTA5ZjUxMDY5MjgyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InNrSUthdndOQlVlU25ZdHRTc0pWeHc9PSIsInZhbHVlIjoiaTBCdDZwaGc4MmdLRmNhYlNnNU5zY3ZFNHpDeWdad1pnNXRnTDJsUUY3SmJTek1OUEEycEFsRXZGUTFKQ0JPeHVEQnVZekVBVjRhcDZubTBwWHRmV0c4SWhUQTBwbEFwT0NrYzBpS0N2YWwwZjZodVlYMHMyNVdYVStiVW1LZEUiLCJtYWMiOiI2N2NjOWRmY2M5YjA0OGI2ZmMxMzM2OTlhOTJiNDEyOGUzYWZhNjQzMDMzODUzZGM1ZmYwMjA0ZDE0ZWQ0MjBjIiwidGFnIjoiIn0%3D",
}

