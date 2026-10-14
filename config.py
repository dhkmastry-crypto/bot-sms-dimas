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
    "cf_clearance": "ZqrDakkr1NrP7C6jLDihuj8qIZC8hnryFIbg5pDxeFk-1791978312-1.2.1.1-0XUNKSwByIGm9CnYOyDQkYpZWT1znwxSlr.uUCjy5.qwKJrA3lbzVLPQBOME6IciFjZal.XLJVVYBNYyjCLnttKPvZmIDgAk7E1vaZ8IvgPQDVyOdRxA1Fss17baTjxIk.xdKB6q68mI20xeKca7sqw40MDzswV8h5zsIM5bWZbJ5UNhErBJadKclC3Kn0RuKGnmUT7TUNLlE_OH7NPtpsmmDWyFM61cmKWoXf6h1efMzcfk6vvlxD6A3hJGX.PUozfHA5T02YQzMt7HS3Hq8itZEpI_lkDYaM9zWaC0d6YtYydLXK9KbnLEcnlgIQRwnNYGg.umu5OpAJJB.7HTJF0BSBOTkG193f4G3N3yM_QSShLzuF691efQYHUGt2DI5nQK1wnLbxrlAxIpG6EPiJxtPXVZsL0oChihkkZppygpI.80s2kK5dDi0uGRwhrvo72fh4cM1zwyfxlK7qKnnHzK2rtECA7iOsdhi.3l4cGGMVdUSTVDaDwPRMDGuRmUnrAW9JNpYuVPFL0GSZQmig",
    "XSRF-TOKEN": "eyJpdiI6IjZKRitZVnNlZWh6UWo5TzZJYi9hOEE9PSIsInZhbHVlIjoiMjBnRlhRdmFkN1U5QVJNaUtOZnppWXhmRHRNN1pmZUNxV2NibXVGb3o0REhiay96Z3R2WmFRN1NhaFkxWWRoSXdQcWxaYkx3U3pUejRsZWtNZkEvMExrRGZkcnJTdjhPdWRtdnhxNm80WnNPemVpck5xVXo5Y09XVUM3K2FBL0QiLCJtYWMiOiJiMjViYmUzZWY1NGY2OWU4ZTk0MjZjNGZlZjI4ZWI4NzdkY2M4ODAzMDk0N2VjZTUzZjZiNDY0ZGRmMmQ0OGJjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjBEZ1p1OGljME52ZGQzTmE3NEUyM2c9PSIsInZhbHVlIjoieVNld05xTzJBcUtPYitpanNUZkljTjFaOUxhb3FUTHc0dVRIb3dMdGNYMWViTXNJZ1dXZFArbVpBaFVnWFZqQjU0NkszZ2R0VUlwUVRWeGNTZnZEUnE5V1ZFbVhXWS9NNTArcDZFWTZKWWhER0NwOCsvdzZpRzdtalYwMGZVQ3kiLCJtYWMiOiI2NWY5NTZhYzgyNjdjYzlmZGM2NGJhYzZmMmE3NWE1NmI0MmUxMTYyOWEzYWJiMmY3NDI3YzIzYzRlNmMxYmU5IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "eyBRyMHlY9aHiflv5uD4SFFDnzBh9IgAVknsdYh9vac-1791976616-1.2.1.1-ifJopEH4jpLqUnMTIL7ZTdV1THDNiyqOImtQzT5yq8o4kObYHWetxvj7sjVG5EzxiGnT7xgtetHTiWFn9sJ0VRioXDvhsdMQGLOsXSZDvqqPXRCi9Idfy.gkqvCSTxnCQ0hpwDOkiwQAxcjANrEvq1ULDO2TmowjrfQJUPjlx0QJXB2aErTeeePbF5TIkt884uV4ggzdypzJeOBZ.vaJRKZw8zV1pqRu3g4XFUDp0yN1lRJIYCmLX2An8SP6cKO0EsoQsSUvhU9tZWX9PmzFm_nxCiOaQGepZmkUcOFtNj.BPwrOpScHjAtGmztz..WhNhu8xgFCXVk_8pVKL0VilHF1cc5CWLXqLHCzmwxYtgEa2w4TdOKp4b80vJhojHLu4msVwiLbLaXDqw6tiWALudOUehD8RekVNqPorrcrMqqGszn_9gSlJ0XuXRBZQ2BjqR3CTBzEe7O5wjkWNQsaDXocLnIPmWk4PECSSK6vgZxjGJVBP3a4e_VMhM_vBqlX92Tq0pxIe1AMvLOM.CwQ4w",
    "XSRF-TOKEN": "eyJpdiI6IjhGbHhqTjZhbzZKb1Y1UnpiNHhTdHc9PSIsInZhbHVlIjoiclVGSU5jZzhuV295eC9sT2tUL2dJNjRhYytycWhWN2VVSjdHcTZLd0s4K3cxNk1NenZaTHZ2eDBzYkozRE1pSm5MeTgwcGhmblIvdDFvUXpsN2hCaFY4cDFQVjVoRkM2WEE0U09DcU10VllrWWZuRWtZQUVZdjl0TnBydWJ1aysiLCJtYWMiOiJhZjZjMjAzOWEyNzI4OGJjNmQ4MjllZDExMTAwMDg1NGRjN2ZkZjgxYmU1OTM0YzUzNTI1NGU5ZWVmOTI0MTQyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImdjeXZSc21TaXhaWG1OOWlpV1ozOVE9PSIsInZhbHVlIjoiS1dBRW1UeEVLK05xSHFkTkk3aUMxd1dPbHl2TXE1MkRtODZkaGFETWpJaWRsWmxuVTk1SWFBRE5ZYWR5emFFck1WRE5Gb1J6OUR4ZGxGcVlIc2xvdUVQWnhPaVdKdlpBSk8vYzN5UGt1NnNPY2xsOElpUE5XSjB0eHJmVmtlYWgiLCJtYWMiOiJjMTc1OWYxNDJlOTAzMTczNmNjMDRhYzZkYjc0MDc0NjE4M2Q5MTdkM2JjOTgwY2FkOGEyMWYyYzBmMTc4YTllIiwidGFnIjoiIn0%3D",
}

