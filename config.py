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
    "cf_clearance": "JCQJh_9j.k7IoYB3r52XwymD07yHMAsKhC7PRPuPGFs-1791865620-1.2.1.1-AlIggXlu6gdOUsKF0JrG98eYlHDPGydwBiJk_yxBgUvARYNxS1GYG1lp71tllwVodGlIZzr5ls7vv_kO9Tr9pVRgoAYx9LJJYfak_o6XhOtm7bZT6BjKooLScdSvCH7bMpJAqUkWvyaMN.F4QJyl.33KSlaJo1zTs_Q1O3Vzn.S9XE5X062p1noBG6Nrqn48k8GH68ny44Hq47CFLShZAqJhybjF.juhXkcWHJ5b4Gcvvrybmj0Q5Vf7UpMMRJeey0msXg_dBt._MsH3XU33b2yOpr89am5OI77D2yP_Y1z1ssfPDlQXpci18bYi2A5mpd3LdGyMhyMcbDZmwBQak1effeABvUTXPesvAfMec2.j_FjYjYWFPYe0NJtRDWtSMRHJD0BETPxpctMBHiSjMs.HLYFT2jrOZlHzkHIYmXsIvxSdt1D38TUq24g_6Q3pzAlglqaZ6Y7taQwYSMIJ6VxjuctTk_rw5NJdIouBRP_M1b1TzJqZZEg.tmcTrjzboDu0OiYrV.6_rbzukH4jpA",
    "XSRF-TOKEN": "eyJpdiI6ImgvMk9McHRpaXRKcWJFdjFQWmg3dEE9PSIsInZhbHVlIjoidG5OU1dvTkdWMS8vMnV2dnRDNjJ4NGhGTDExYlJhRTAzTFFveWkxYWVCVlJNMGIwSzRmVHA2d2tOVW0relJlVUR3M3Fva0QrODZ3YmdMMDFldDg4UFBxMUowakxGN25OUWNFRTNRNFlLd1F6UmRXVEEyTm9GdHdKTjNoMmJjZzIiLCJtYWMiOiI4N2ZjZGNhNmZjNDMwMDdjZWY3ZWRhZDc5MDRmNjE4YWFjMzk3NDljZGY2ZmFjZjc4NWFmMzEzMzNmYzk2Njg5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkFKRkV0cnFiV0Vnbk9DZjhLL3JjM2c9PSIsInZhbHVlIjoiME9IWnpKVnZZWUptRXJkNEhXZ3kwZlR6K2xvWHRiNUhlM1lNaG8xRVhqbjRUVTE2c3JDYnF5eFdGSXF6em1ha1Q5T2sxbmQwbnRhT3lNUXFnOEpqYVpBMHQwZEkwbFpmQ2VmTWMzdmJyd0t4eVlsc2dBVENPS2kydHRZVkNRd1UiLCJtYWMiOiI5MmU3OWExNjVmNmE1MDYwNzMyMTU4OTA4OGFlNTVhZGU3YmUzMjlhZWRhNDZmMGU0MTZjMzFiZTE1YzUyZGM3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "IuCqRKlhoO.oGse9K3HCWlalNc0JqAg4bLM_posuDbY-1791865007-1.2.1.1-eyb5sycVMITiJo52et0OJGh2GpPeT2UsLH4Gj7V29k0Ry79dSkTicSragW7SQyTUhupkTRppwCUQbJTwcGek5nRdvrXAoW2yCwyM7B10CcB6y_gltaXAh.hTvtzNlvYeT13vYitFCoxxTU4SY3XH888wC57xMFSgatILLqEN3CYVbkVltaS85oTfuv6zgqYzTC7035ZkMXGT984yxJVcabOws6MOuL1Lequ5PEN3xL.AqhG3JOC7HH0ZPsoUZEYi9biTPLHlx1EUtq3VOx.9z.96faccCzsc5dg5JgCVItPquR9S7APOw7J3RSxZm.sHKuzNr2zvjan545cENfIwRmNI.NlGjUQk6TMlj3E9uUmMGuj_1zMipjHG3RHetYSURzXXImStsnSTM138e5QR4PwV7lG6zNfmTsZ3xDoeJCuqcbRpNyP44PQxMwr0mFNJ.BpeE5dSicsuOaOfVtQdRfVyA7xDpoQ_78bzbfyGctEDx18d9frPzzPnWIOo2snuNnZTv0lLlA13iXOW0bYntQ",
    "XSRF-TOKEN": "eyJpdiI6InFPaDhlZG4ybVNPU29hbEJwUjRmVkE9PSIsInZhbHVlIjoiY3pPa1NhNUZ5ZENSU0Vrb3NsTUV6ZUlycFpYRjBEbWlPVjBiOGNVcHpyc1lNS0kxTHNMb3pPNUxmdlhYVm0xNWRmTmUxRXVSTDZIUjZhQXA1MllWbXB2RG0vK0oxU0JubFUrMWRITXNZTzRUb3I0ZlhZcFIySTdLaHM5Wm54TjAiLCJtYWMiOiI5NmQ2NGYyZjljNDc3ZTM2YTcxMjk3NTQ0MGIwNzQ2YzhkYWZjMGM2NzIzMTlmY2E0YmMyYmRhZmQ2NjZjNTU5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkQ3bmNIM0pRclVyR0NuVWdNeEtnZEE9PSIsInZhbHVlIjoiS2tROEUyd25qMVBrdlZSek5KRlovV2JaSm5DMGh4S0ZOcTRsa1FSTkVjMHRmenFWeXo4dkdiMnNza0lXQ2JvblIyV2c3czg2OFJDVzAzaVp5c1RndGRhSXgxalcwYnpuUmdmZUcxdUdvMHdpUG5PUkM3ME13am9TRVYwWElXVzEiLCJtYWMiOiJjZDgxNzQ2MDIwYmZjNzA4MzhlNGMxYTZkYzBhY2QzNTQzYzZjZWU4YjE5NDMyZmVlMGFkZjM0ZDJkNTE4MWE0IiwidGFnIjoiIn0%3D",
}

