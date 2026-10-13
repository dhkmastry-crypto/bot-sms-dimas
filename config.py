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
    "cf_clearance": "D7rPF9arZwwakaHLCJLkXxVpHFhqFkf4FX9ZQdKLro0-1791911345-1.2.1.1-HpMJ.iIZzAV02pMjeWNpX3XygftYib4SKg.MBC6_NbzyURikruJhiNigMhlZ925SO2O1SuQVPa4M2nWxszy8X3WnrN2I1UnDmn8I8BNQ6NxcohrhaalVowf43tb_uqRtc6JRiNjxVlmeEmVGzyCNYBLKd22U2Ip7IrOAtwC1B.R4AGrGpx4VJ_Ngz_.SxQLiYrA10HAyUhPXOsQ2ORRiUvFyLkYYd_MSaWQxsWqQpZoKUP9mt6u5FIhfMyIlJSyzw3_Xe5lRDxpLDyOu6IIx7miwmhCOg3G6M1ZIa1WcvgmfGWUCLG5N0sRUzDtmnC6y27A7YZmEboWod5EgUp3Rms.F_TXVIt3WWYBqvDYQS0gfc4_dnBP83b5PEtHRRsx8AHL8FOIyP.1YFRyLOBYDPvt8o6lXvKJhOR6xYIwoGD.F43xCY85d1Pb8Iqe1x4PR7ytLHA5S7cUmfXErZSWR9AsqatS59pesNEFHs5zhNh8wwiZ0AT9.SSXODMBIoU081oxz6o_fMDlG_Tv33qTibw",
    "XSRF-TOKEN": "eyJpdiI6ImwrbGc5VTJ3M1RlNEN3aWI1RHI3Mmc9PSIsInZhbHVlIjoiTEJUSTVlVHNaSmFNNDlpNzJpNXNPTkYvNHhOaktGN1dTMkNjUGNCZUlNNVFJUVZ5VTg5RjdkeEh2SWMyeHJscFM2UnNEVGhRMTRCejBBWDdxeGNBcCtmUnd2LzRVVm44ZmEzTUg4WWNyS0hGanpGYTBIZmhTcy8wb3ZUVWhMTHMiLCJtYWMiOiIzYWQ4Y2RkNGE2NDY3Y2YxY2UyYmY2NDlmZWU2MmYxNDYwNmYzYzAyZjhkOTlhNzQ4NDliMjRhYmUzZjdlYWVjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRsTVhGbUxjQ0FQb1pEd0hDalU4REE9PSIsInZhbHVlIjoiZUZneGVYZkNielhYMSt4UWxLOWFsNnlGL2s3bjRENHJNTjU5TVpvMmNzQ0x6dHpyK1FUZlFLV1lFOUplM2MzQVhMWWlYSm1kLzlud2haN3FQc1REM1pWaGd4VmU4NnNrWnZ5VWVJR3gwY05sbHRwZnVpenpqZmpIWkdHcG9xOUUiLCJtYWMiOiJiMjdhZjA2M2EwNGI5MWJlZmQ5MTAzZWUwYjVkZGYwZjllZTE1ZmVhYWE5NTQ3ZmRmZjg1OGU5MTBjYzY4MGQ4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "8IlnEbJfU_4Ib_fT_4AHY_U9uGsB1pdkBceV05QlCno-1791911367-1.2.1.1-kLinjeAGDbm555mDuwuCwAEJ.ZnfQ2kCHkSgIIN1VKloPYbXNw1pfwO63NLnDj1v8MwlPK7soZ.By8vekUmSDC4gpQ_tDjeWxJpmrXviNpCHtJ9NB7BQfDBblHi5G7wBSASUt_wBMMEv46p3ivvVH4dbsTcgFS9Yq_r4DcPqucVgnqgVdz.QhT0W50gmQqV.sQvvrVZhpBmNUBBK402e_1ksuNoMCRk8QXwlJJFLqURGR6Ctw6EuwPIne.pu4594QSN7hT5s6wfOCEcB4DsM4Vo6O38.q8Eywe1IWDimXZsYLrSmYkMptx_KtZYmhZ3SJ0a4uOwCn9Sw5wbGSyszzV_GKat9nzTwJuB246qqiI006FWlrM1qVbQSxEFUMSp__QqJv3wA10IDyoY2qm04d12Si5k6y7P4MvOtMBjcyVZSqkuNO2cRtYK4xHLTi02L7yEqA1zSdXTbpq2E4oawCKxLsvqgESMypx8Zn0iQcWPh7UftIPSMjPqluD0rQUQeCrVj3dMVj.CAyHQjK2s4ew",
    "XSRF-TOKEN": "eyJpdiI6Indtb095VUtoVHphbGt0NHZkajlTdlE9PSIsInZhbHVlIjoiaEZ6SkxkRFQ1YTBjTzJjWXVpbnhSbmtpSHF4czl5Rkd2eHVVOVpLTVhMY01HZitod1JYOXRzYmNRQ0dhRWJ2UEhJYWZ0SEVPemVLY1NINkY1Y2ZHdUErNmoyRTByQ08zd1hIaW5wREFwREsyYTQyWnNvUFBabDJyR05LK3E5OXYiLCJtYWMiOiJjNGU2YWU5M2Y1MjYwMjljODg2YzIyMzJiYWQ3YjJjMDJhYjY3NDhlMDE5MTFiMGQzMTE3MTMzY2M3ZTI5YmJhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik1wcEdXQzh6KzFaUmhHMlZCV0puUlE9PSIsInZhbHVlIjoiTkJVcUU2WjkzcHExNlUzUGI1bjBCaHJxenhGd2c2OXZqTDBEazR5ZHJDUVZCcFI4eFlBQ0JybUh1UWdneU1OcXNOcXV1cmc4d2pKMk5Uc09VcGdSSEkrVDRhZUlrcDkxclV1RUU4VnZ1UWQ3NkpXZDhkZUJHVDkxQUhYc0ZnalEiLCJtYWMiOiIzNDUwMjEwOTg2NDUyODQ5MmFmZjg3NDI3ZjQwNDkzNTk3ZDA0NTZkZmE5ZDQ0YmY5ZGQyYzZkMGZjYzBiNDk0IiwidGFnIjoiIn0%3D",
}

