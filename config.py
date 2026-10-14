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
    "cf_clearance": "Eixb2yHes1ecDp.HDLUMHL3qyNl1DCe4cpIuKekBHn8-1791967459-1.2.1.1-jsM2bPV1eMEkndkIVd9zVSo3OuGMr8gvxMIStskQNCd6JpDX8GlwBckFe1mTid5_O8vFRu_HpV6_2hTPKFVYjmsZv.LWcFszhiCO65wG9oNApfCA1k0Tj1lSNBYwFDCRIjTkDSxMM7JGPpF_wITdffwIEACWzUXzauWEwu.e3u5VZXbHsag0IcGWpOLYsm6sVfZ3cUHAJRNqSJ2TGPYOpt90hNYO.Wd5W5djMXdW4naHifL1p_Sa4z1VuJj98DETlEhowSeZfTWCk2XowFYLZDn854yhR3Y34DglKr9ERe8_TUoZZ.5JSJsodgEXpnbS_ocr4FEke3BbX5qUGuejY7Nlm4QEJPVNQqJLIpxlrRpB05NNj6fY7tyMP9QAWE5ejSU9xYOmxM0qCOYCOAlWjhdWrYnYT0HPGjJtIoA7nNTy469ULLU3PydWn3OZV06Z8XGXIMxSVozF0hQiVcA.WfpZ83IGKYZ3Pzsztil8QwYtOcJEjvdGvmmIX107H_skRNj2aZOzXA8x9j0.vOqzFQ",
    "XSRF-TOKEN": "eyJpdiI6InBiTzNtenZUYVp5MjY4WDdneHkzL2c9PSIsInZhbHVlIjoiUC9mb3VMV0pGalp1WG5mTWh5MWdOQy9ybjRPa1JMUEtDS3BLek9sdWJkZ2dCRTFibHQ2Zk9DaWp1WTZrWlFtVjBrWFR1dkY2OEQ0MXcxL0xweVZrMTIvVEE4ZXkvaGduaXhHa3lOZjFJb3QzbHdjSjRQdE91c2JCZDA0TUVsRG4iLCJtYWMiOiJhYjIxOWYwMGZmM2JmNzNiYWM1MzA1N2E5NTA5YjA2ZWI2ZDc3OTNjNmFhYjA1NDBkMDVlYzdkNzcxMGNmMjEwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhVaUhxajNnQzlpeHVFMVpaUjBlT2c9PSIsInZhbHVlIjoiMHNydG5WeTNwTUFrVGNMT2c4UHRObDU4ZndxS1BaVCtnQzI3b0Uxd3p4QVVrVVh0dVU4YkZCaVNJVUhEVFB5WWNJbTY4THJqeDZUTGNieGVkSFB2YXFiN0lYdWxkR0laQU1ERnc2ak1HYVVyb3FMdlF5dXZhNTN5cjNPZTVqeCsiLCJtYWMiOiJlMzY3ODgyNGZlODhiMTM5MGUwYjEyZDcwNDRkNWI1MGY1YTZlZDA5YjYwOTRlMGYxNDA2MmFhZTE5Mjk5YTE1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "76TwewydF3SsGzmntWA08fChj8Ic4p4B8OalGT3JUdo-1791965751-1.2.1.1-u_0Mi4kD7yW.BxJeR5Kl4NHwUDRlL8UJsOUJAPs8M3cUGDasfVNU5NXRoMV6J6tvVKM7ZTwPT9t8smVAjZUB6ZRAE9kI_HkLs_bca3ILCfF5o2KioHs8SdzHQTnTT9qPD12TGpofhVCIjJNTsX5VSSd0k6OzW.ppu7vTtfyRvyFvpDVrgT.cWBo.F7FIICR9o2pFVQfZvqjWLbXRucbZkwnl.eAmkCfV4t9fqvnWPCVETaQDTWCKeaf72.5PDIo4gUFy0qkkl4kn_Hr_hYZMdsbwhtx51vyFraLnNqm4nIxX8FqUEUYha840WM0yMRTnbcFEgKLpo5JYpgMugddZvscNLLNA7laqZnf91_TOVpcfZzBSbp.oPBdTXah9xKe6ttJRrRD7_Mcx2XI8HMb7Ix0FAB1WWY_MG.KdPCrWh2SEUM7XrMA.GuLOlU5jWABLajd3AT8PlqTU1e4oQ5YqRwU_A8dfBDbOxYQByp3zlkn5ik4opkkhKadVbReT.Aiu6Z7T3ssiV81GaurtSvbHaw",
    "XSRF-TOKEN": "eyJpdiI6IjdQcy9tbGhWTDZsNFNKYU1zcnlNM2c9PSIsInZhbHVlIjoiZ2pxZW83d0pSZ3FleExhelZlbDByS0lNSWhxMVJsMmorMmRXT3lyUENnR3BXM0JkdVU1NE9HZGNXS2ZmSWUxWEJqcDQzcEZiMmdLUkVrb0tJQlJPL0VpTCtwdDNET2hhY0pUY3lQcnU5MFNRaDdycGh2V0VjYVVJU2JtdmhXS04iLCJtYWMiOiJjZGQyODRjMjdhOThjMDRkMTFjMmQ1MmJhMjg0NDQzM2RiNTVmZjRjMzMyZTMwMTk3MDY2MzYyNDI5OTM5YzQwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdvQ2dLa1UwRlJMTDdha1M2V1JsQ1E9PSIsInZhbHVlIjoidDhiTkxBL3pFTkJCWmdpSzRkZk16cUZZeHp0VWY1UUoxN251bkYwU2FxcWV6MVVlTUlWOXBCdTJFV2J4VWdNL2J0by9VelBmTlEyaDZRbUE0bEE4UElnTVNraS9TaWRkR2lIcURKc3AvVWNIKzBDL0xFd3VHOXRnNVpmQTgxS1kiLCJtYWMiOiI4NjhmYzNmZTU0NTk4ODBiZWNhOWMyYjFiNjJhOWRiZGIzYjNkZmQzY2E5OTgwODhjNGI3NmUzZWZmMTI4OWIzIiwidGFnIjoiIn0%3D",
}

