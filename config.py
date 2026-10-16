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
    "cf_clearance": "ZsuFfJ03ZDFHDqiCtOPVBk8AWmU4nXM9cF5d5VZhvY0-1792138012-1.2.1.1-vGJM1Lk_OYlWDflwN66AX2Cp5fCxKpCik9qPVLhlHp7vSa8B4fnqfpPb22.gURMZn2GcQ0VGJR.9tbKx3851IqiwsJL7i4OCDz4gdbk.I6uNF9rtriWuAGIfKLGdb2IJV8tDJNYlcquvUT2SAgpMivWVzKcDFFqnNDkjT5rtA7bkOciT_JKxmCYak6S2so5mrbAKioTvDENP0HUlcXOlVqwiJS8up9V42Pb_Z1bTZ3EAeuQ1OIPj2F6NGB6DT4LJij_JOjYergzuQoKzsrS9EAkWGbSmmCabXrlwuLviqbcz5qdkMhT1yTrcpxuqUrYHXZUypAYTm9BQjGcU.V5zmhOIygeMe00zg3aWQz9uq1ARfdieXwjg6DwnnK1xs7wnXWj0y88p6yhdPjh.l.BwjqBSoiGK73T0Sqxhew1ExUWmAr81PfythbRbVy6Ugswth0iUvdqF.PaUCzNlGiKfxew02Ek3SjdzVI54B16HNSPCBCO2s6oF2SC8uwk_m6hWGADZDcG9KI9GWDB9JuL6YQ",
    "XSRF-TOKEN": "eyJpdiI6IlJjS3BoWlNubnZRdXlFajBML2IyRWc9PSIsInZhbHVlIjoicEVXQ01TVzRSa0JlNjcyYXV4WU10ZDltSUpmbzBoTkxhRTNrWlQwVGR4blM4QWJwb29SNnQyNmN1R25hQ0wybmVEVVhXbUJma2U1TWNiWFJjVFZDR3VQS2lqVThzK0JqcTlSR1lNWnJwTzZMM1A5cWtyc0syVk5DZ2pqRlM0WGQiLCJtYWMiOiIyN2NmOGFlMjlhZmI1ZTY3OWI2Nzk4MjQwYjNkNThhN2U0Yzk5ODVhNDRkOTMyNjYxYjdhY2ZkMzk3MmYyZGNmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Imh5L0VWekpvOUtyUzlFclFxWEFkMXc9PSIsInZhbHVlIjoiQTZNRTJqY1ZCeGR4U3FpRTVzdDdwMVlBb2pQcWFaRDBsUktjMWRoajhvbDY1VHUwbFI4SHEvNFhGQzZxSDYzbHBDNXZoZ1QycjFCL1dyMnhkNEVaWXFYd2d6bXZPTWVpcDludDJPZVp3ODh4dCtVajF5L0IxWm1BTmliNDhZa2kiLCJtYWMiOiJhNDM2N2JiNDhjY2QxMzZlZmFlMjMwMTM5NzM5YzU1MjYyMzM2NmZlODA2MTI0M2E4YjgxYmM5YWE3ZDQxODRhIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "0Yr6GVgkBvkl56iSnM0XuN70TglUKkrD1uDuhTV8LdM-1792138023-1.2.1.1-JSESNymGpjNByQ_5shqzpdglm5cP33L_VcSZ4YYpu5ddI9MUN7kE1BOzR_hb58AfobElCDVoRxsPw9N0OwxpohRXB4Cjaf9Z7kwpAqRTscXE8aJJ2ZyLNF4.FkNFvFulG88uFjJdNq9SBA_5IlFdxIlUUgWxJbAKVHiEvmcZEh0cDAnDVTRfZySXdzPr18o0WdP6L.EOfITgFNKPbmnnj4VHt6TTwP4.om9dHmgKr5F1d6lxolTSiOMZAJfGR1WyLHPlKZ2Kn9hp1OZbH5eUeIk2uPSoNgus4i.W25aERNt0DSgiiUsNiTdXtXE5sSFXMKNhJJIF9SlcqbKpGtcnH1BHYLdQbIbVgtInakAuktjLI57OGVRXpz6ve5Y0Qe2ckvyG7wZ8f3O0N1es_RQewdszVXdfFiTzyEGfGhGYYXvKXZgjfTcbiPuEgIXhQay63SZzy8RC.kaBdOJ1gK4vy5eme7Ym0gXOaeMTP2m84z8NCbyZy07h9PsNKTKCNFsLPM98Br8YjG0w798ep6xNZg",
    "XSRF-TOKEN": "eyJpdiI6ImlLNXdjcU1WT3Z2K0RheHdKVEs4WVE9PSIsInZhbHVlIjoiVjNPeUEyclFtK28yQTdXNEEwMDd2aThWTnlNczIybGlBZWp6TGR4Rjh4RW5hZm1XQ0ZBN2oxR0tLWFl0Um85WHFFczVJby9JR1J3UlQ3N2FieHZwb0NFQnhjS0pzMmNoVStCZmRScFVMSWJKSTlJN2E0TmZwYU4rQTlOQ0cwQ3AiLCJtYWMiOiI5MTJiOTYzZjY3MGE1OGViZTRhMzVkYWQzNWVjMmRlOTI4Y2I5YmJkMDY3MDcwYTRlZWJkMDEwNWUyNGNiMWVkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im4vMXJnaXQxVVNDZ0M0R1htSHp0Q2c9PSIsInZhbHVlIjoidHpNeDVYYzdKQ1FUL05ub09HSjJxdTI2d1l6RzZGUXZ4N2hwUVoxRlRTNGdPcDJvVm5KUVhHdVZlZDBpNHowOVE5NTltRE8vNVp4cFZvSHFKazQyd3FZRVFWdzNGTDJUczJiR3BxSVdFNEI0bStEYmlZeCtLV3RndmNObG1pQksiLCJtYWMiOiI2NWViZDZjMWE4NzEzN2I0MThiMmZmMTY5MTI2N2FhOGJhYzI2ZDAzMTUxMWRjYzU5ZDdlNjhhOGZlOTllYjlkIiwidGFnIjoiIn0%3D",
}

