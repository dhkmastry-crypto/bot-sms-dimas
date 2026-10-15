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
    "cf_clearance": "D95n2RNIt5T9W8nVzY_raazzn_WNdBUWz6QW5Qp_Vz4-1792096290-1.2.1.1-dfRv0Al3MBsALW3pBFLnIA2IZc8QnSyrCBd6zPCN7ZDhWsHN0VsnCUUQku7h6KZpqsmCxKyvtBzRcHI89NfMITV2dAiZcgV1vFOvdEEfSky85qu5DG8uR2r4qTgk2M1sxjvM.Is08b92fUWy3hawPS2fWWpxdTHRD27WLSITjs9HFcC1B9xJRacPzQWbs0FBZ3FIcduVKqGh1xZ5KmCK2DurKcYIRA49h30AQCa2ejzNjxvdsSWCq6BwjrZlVYn5xe_LNdc6dJYzJwscL8ODw4RNu.ZLI5rNOrHF06czmWMgOHjOUoLj5_GocEvBjM7FCUCnTJShPDwt3kUYLv7s1a6mByy8hiqNd5lPDdlnErFd.7uiyIqhV9tYuCrHOg7ajAzodrkGw60vvzPpyQm4CGhwGfu1ABIWitzInt3a9L2Jz6amVQxBsLdOEsPG6plK663gAh7C2eWeyYV98KDSFupajHx3oN..oGRHbEip2UqYmxN05v3fHvWCeyn08byafhnci8qrUfHz5nh_h206sg",
    "XSRF-TOKEN": "eyJpdiI6IlpGMUtGUmp1Uk9Nd25Zbno3TzNZa1E9PSIsInZhbHVlIjoiZm5ab3NhTXNXNVpLamNKSDdOLy90VkE2TjBUWmQwUnFRdkNRQXRVSkpmVkYzQUFzMUlzRXVUanlEU3NMbC9hZC8xMnk5aU85b3EyY0ZvbzFPL3hvc2ZrSEozTEFtUXpDWEVKMGtEdWZmRzhNaXhUYWt2a01vc2xkRVdiUlVja3oiLCJtYWMiOiI5M2M4MDUwMGNkY2YyNGYxMzY5OTcyMmE1YmYyOGNiZDhiNGY2ZGJkNjMwMTEyNjJkOTM4Y2NkOTMzNzkwMGU2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlBBY3UrWnkvSTZySnV5MEVzSlBJOFE9PSIsInZhbHVlIjoiOWk1VEtlQkpQTnBqNW9pbjllT0xpa1RhRzNDTDZOalBCejJyZVVPZHhRY0Fsa1Y2bFF3aFN1bS9tNDVpNlpSQ1BKa2VMRlpaS25pZHA0QVorMGlUSno4NVVqQ3RYNUpFb3BnQ3kvSkw3Mml1UUlETmo5NHpJbEtGS3pFMG1NV0MiLCJtYWMiOiI0ZGMxZGZkOTA2Yjg1Mzc3YTA0Yzg3Mzk1OTdmZWFkYjk3ZjVlODk1MWEyZWJiOTEyMDdjMzFjOTU3NmI3NDRiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "VD0ZdV2crS9N1nbTRGQkwnbk.NtFi3x4IMxLE6.lPh0-1792096290-1.2.1.1-PDzYRTsdspmZAsrUvWxaG3xBoFeVMiJTUG_KsVmSeI_.ut7EQaAi1OCtRCLaswuyhK6jGW7t2JtPNwSvt5EK5wpKKCYnImGcIauYpjvvD9btXy11mDH.A7rUO8A1opgCVlsxFk9kkq8_h_MsMgN5P96Ml1WtXkw0NcTPygkcH46Md3MaBOt9rFFiLypmOxCsmBjIqpn3CmJ27HEGY97zddjwRxzx8KB.Cl1RHPi5_sfv8G4k6A453lRrPGfSIdvl8qBAIUpTc.2rufZSFqtiWQKGbjVmmcBypIbfaYEWjdukFpqZMsgAFZbbj9HGraYm767QuZe2zEBxVfMhU_CLynmon80pmYGRK8E0SJNKpCp6N_bdeXg3WEOptpr6KPsXCTs7I8.MKVYrNzTuNs9UfN42ej8Si3XXntxGwSOR6vUg09CaowK1qjgyOdNrZ9vdL8cEpDWyuCotNh591oXgLt.vwuRP.7d6mdwVS3QeC77plEW1G6IDUDbBFvOcAPtfPNrQkTJNRV3ctmUjU1RxXA",
    "XSRF-TOKEN": "eyJpdiI6ImtYYkZuTWk5dU1helE4VVVBM3BnTWc9PSIsInZhbHVlIjoic25kSkF3NllNK3ZRVjlkeTM1Z1hjN0FoeFZoMEMwaFhPRTRlL0lJbnNtUmxaUFFsd1JLdS9tdDBHR1JlbUoxdGx4S29pYUt2OCtHZFBlbXFidUxSdmp6MWt5YVRIai9tRXZvZ2kvL3Z3TnFTSnpXUGZjRGhwbzU2L0gxUU5XZFYiLCJtYWMiOiJjOWFlY2IzZGZhYzAwNzA4ZDEwYTc1Yzc5OGY0N2M0NjViMmZkNjY2NWNhNGVlMTRiZjFiMDE2M2VhYTY5ZjgxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IklpNmRUWDJmNHZuRzFmdE9rSk1TRHc9PSIsInZhbHVlIjoiVUg0ZXZhNWhNQlBCV2ZRbitWN0hzaUtiYzdEenRnRWJqSXVmUEpoZDkvMEc3NGNsMEU0dUcrcXlyaGZERUxKaHAxRzNXZGIwYU1TU0Z3S2N6REhYM2JBR1d0bmN4K0xWbURSakYyNXNIQlpmWmFZd0JTTHZFYVordEVNN3hXQnoiLCJtYWMiOiI0YjkzYTQ1NGY3OGI4MzJiZmU4NjI4MmM0YmZjOGEzOGQxN2E3MzVlMTdkNGZiY2I2ZWJkNTllMWNlZmI4ZTI5IiwidGFnIjoiIn0%3D",
}

