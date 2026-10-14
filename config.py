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
    "cf_clearance": "EXRJ2TKgxO4n8tjtnWLE5UR6G8H2Xp364DnaZGD4qrs-1791994639-1.2.1.1-3mzUpn0HHYg4o_226ylvik_vWJbx8WSBYq7QrG23JOIXrH2W85atUUQEFdSB2kc_tFIHf0R42FKtT0a3.M72NCLM9wGVaKIc8Qa9j40YYmpO2oBM_tTzQBgK0oUY0NB1F.Sv2mDqnbzMgC8XS.387AJiXZZk5ATFHWtcYNuCnlyi71gJ9d7LlN2UeqqAYK_XHab0RZdL03mK3g0zsns3FtQIdj9QDKR7oOpdd6HdD.U5uo9.5YHnYXWZGDSDb7LIxdwCmAcmsXQ4Bvz53V7ClcIui6gzmrW2e3v8sj7T8SiJ5_e85TYNto5MkuoBfEnuMlK8_sBoVwOGcl7PbfKQ1OGAOR.u0m8IbaQsuADcykxhc3FpCLn139uYYSUErreBuVhSh0IKpjWORl9r5197NCnFPAQacK20D10oVsW8NFiz2tWO9FWMEjJ0ycN7UvXxDXg.OSSVZL8w2Jo1CL6mhePszvA2WKNfMwQ34QZCxM1VF8aLmHDHfhNPhZko5jf3AiL8LFzcH8K5Gp1XhG06lw",
    "XSRF-TOKEN": "eyJpdiI6Imxyd1lwMHFIY0w0NWpWZWF2NE5qUkE9PSIsInZhbHVlIjoiM2oyOEhoNkpMTGY5SWExcGJQZ0FIRWZvNkw4TjhHaWRJZ0k0TkFDUjVaQnFvdVU3UGh3YUQ0YW5YYnB2YjkyamczQnVDU3d3c1pOVVlSWWw5MzF3Q1BXRVZsWXlKYmJ0bjRjUC9EeElPUExGSEQ1Tms4UERPZEZWT1lHSVgveXgiLCJtYWMiOiI2ZGUxZTUzMDMxODA0ZjRlZjY1N2FlMTQ5YWI5NTE5NjNlMDQ1ODk0ZTEwOTI2NDE4M2E0MTkwNzgzNWRhOTYxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlVpeENoRGh5ZmNXMS9JZjlZODU2UUE9PSIsInZhbHVlIjoiM0tFRnVLRlgxY0ZjaEZLSnRieGRwNlBzcGpDdXFFdGF6L2hnTEwwaUc0SE44UDhYOHJ3RktOUnF6ZDhHeVFIeWxIWUVlREE2b2tYYkRFVEYxdWtFMnB5ZmVHOVdPU21rZjJpYWIrSGxPSzNiekZEcUxrNVB1a3hYaDlvUlZsLzAiLCJtYWMiOiI3NzNiMzAyZDYwZmIxZjljNWYzYmM0NzhhMmMzMDE1ODdjMTk0Y2UyMWJiMmQ5NTAxZTcxYjczNDcwMzlmYzhiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "rKsdBclKgLVLMvuN.pjrrefMGcSf_d.3YH_jaxTTb0o-1791992946-1.2.1.1-q7QhcHp6ZBt8DKVpuoRfxhqH1KniTEeZVvIyfItUksvVLE8G53RQvTykNRdrDmxA6WzzKVc99YW2b8b4O24qpzQ0ug2isDS5WUSgz24VFLbcKDGQFBC2Vta74Bj_Tc8RuzABxQYJhPvqoSP4Zl7T5E9pEY8qp7_tCXNb1OjHzF71uA4XVSMChugjjwwN5rWNES.m5qEuLSOvJRwSzkVwS5sMWsGBlQAj1E1rH07vlj36yhL1QQ7ltf9SeVSZBLkyrJhfkPd3UMOc2CVukekWResx7o3YjPsxvrqHczvueaBgaekEn6Kxj6WdRbgz3bZKQOsbw9KyZBFLjRk_cuzHQGIWbx4IiEGBLDjBNVvKITejSqPNcE4kqWaKibgLl9ihl5b5pnX23PO9rv_vnSlUuEIiXphF4Ijw6KShCW8B3tLCJf4tenVykOCfd4TIfhkm0EFbE_48qKrzR.ZNpmDyzcFTYxOGzgUtknc.lZRY0Zjre9.taCVqVs5RMka8qs.zo7DCfZYatB1PbmwZM_JidQ",
    "XSRF-TOKEN": "eyJpdiI6IkUrOVoreVBYT1hmbzQyUDNOU1FTNFE9PSIsInZhbHVlIjoiOHowUFg1OWJNV1FLSU5Icmo0QnYrSmFzTjJCZGZHRVc3OE1FT0J3K3RtcnRST1Y5eTN3OGRjdmpXMk5PNTJLdlJqNHhoUGE3aTNiRHJNS3ZQTlRiUTJ4L0xWM1p3S1Y0OEt2VlA3SDF0YlhuYmtzbWg1d2tOcVM2aEIwVEVRNWYiLCJtYWMiOiJhNGYxYjRmMDUxYjUwZjc5NTVkMzYxMWFmN2UzMWIxNjc3MjcwYzAzMzczYzBjMDE0ZTIxYTE1NzQ4ODJmNGM4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImFzdFhkYS9XV3gvUEhLa3Y2UVl4WGc9PSIsInZhbHVlIjoiSGZXc3crWmxCUjd3QXplNEp4bzJSTGk2ckFpc1ZaOWxlUU1QNmU4T0w5enpIWnpwYzh5UGVTUDlkZWl6YlJXTk1mM0kwQy9BR0c5WEgyNmNqRk85UHBzRU9WNHkwN01rekUrbWplT0V0QkFyWTRQbDc5S1NOekpHblhiZENnWTUiLCJtYWMiOiI1YWI1NGY5Y2MzZGUxYWNjNDZiNzg5Y2QyYmRkNGNhNGQwYjZiOTAxMmRkNDZkNzc4MDAxM2I2ZTliZGY2NzA1IiwidGFnIjoiIn0%3D",
}

