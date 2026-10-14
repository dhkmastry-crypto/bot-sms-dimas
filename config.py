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
    "cf_clearance": "Tgd4JJvTloFyf94Zkm7Elit3PEsJb5Ii0F3lwZTuNA8-1791963840-1.2.1.1-nVgEKDL.9voltloSZW.ETDp05KuvrZQfK.uHqWHJrYI3m2ujcQbQqaAl8upriICWWr27Yik0VfldU.T1p263AvrPS_Uz_GwjumE.kVvv6CQfF_m0PZjRkJYG2Hg_y76L480WaQ0KVAnpdPynUiBjLRSONkVwLrp5hRKDF2xV2Q4myfO_MhXij_X_dxEzArKij5mQOeE.2guT3sY302r0rR84CEFMVpBSddpnbKe7juuK031xAIaYHY4B6imE80Txl1U33cpReLGhtkrXL0HdlT4exQVy8yaoELINhBn2wZ39KFrvhKyOAgKLIt5xBY4fmePg7LOSgZvKL1_vhM6q.lTmvhYPpuvg4cbgoF4y0mlz6uRzgkEiO5QbReoSVqS8AUPOsTUijJhPg3tziLt0YuGOsB5BP3XyHihsEH2TzuVkZOHlaoopw3rDE.OiGV03S6Fw_8V7TOEQGmAOQnV9MRgCGwFpsfUG69hdoqGN7znvYf9zZ7CxtJvmM8ia25fYhfLiKZW31bpjygmsCA0sFw",
    "XSRF-TOKEN": "eyJpdiI6Ii94NS91MFU3akp4eFNGNDlRdzdUeEE9PSIsInZhbHVlIjoiVzg5eTNkemR5d000c3dzSFhnRDJLVU5Oc2ptUmw2TzRwWi92MjlXWjBDSWFsbThHbUZCLzFTcDB6TWxIcEJDRU5vek5JTXc0ZlZLTDQwbDE3YlVJNzVGMTN3MVhUMzZKSFh2YkhxcTFEaFZidmhkRGlxbURJWFZqbTIySkM2Ry8iLCJtYWMiOiI1Mzk5NDNmZDU2NTYwNGU5Nzc1NDA2NmNlNTQ1NjgyYjA3YmNhOGY5YWI2MjhmYmQ1YTUwY2ZjZjliOWFmMjgzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkkvTjdzQUlUYXYza1kxZ1UvMzVLSmc9PSIsInZhbHVlIjoiMzdnU3hTbDd0bUt6NERJK0lMYldFMHcrZVRUMzdjTWUvSEdBV1FSdm9haVR5OGlFTnZWY09LZWdWcGpOdXUxcDIwNGd6QlNBcTFLSHhRWTFQb2hsNUdmUHZvbjJlZWYwTml1UThZYTV1VC9xeWlJdUJSV3o1eitFMEpuNk94L1giLCJtYWMiOiJjNDgwZjI5MDlmOTQxZWFjOGFmNzUwOGY4ZjFiYWE2MzQ3N2FlMTA0OTFkODI0ZDIzODA5MGQxNThhZmJmODYxIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "o7qjGwRca92LXRKzH_LPc0yw3DeDf0mlMqvRB1zJzj8-1791963937-1.2.1.1-EHIj6vjwcFiuvsWRw8pDBIWUl3h4bvbBS2zREAZ1c4BTV9ryCBkbhxcDVYygJD2JTPR14UA2SX_84q8czpN9xhrTOkXxQsO5b3LD1nXLTuLr36DO7ukL63sAnPNRkmR2U5WJlh_ZOcSQ3mFe_LIWwqZt4ifstSp.kRj70RMTnA9uOIlh63WhoaVc63i4QVI0nZ6Qcdi0DShT5C3i_mKmBb7ebWeyGCRhgS5jgrRUXbnd40kA3dFKMwMFyKj0HYXArqgEdHf_P3hqAUA1ugDdAg18CJGKKQdhy7mJRiOJTIi_u5wcJvraZe.HqW0zZGLRaphuTy.QEkRMkTWLtta.XJblcnnRG47gNKQzUFEbyarf9Zmv9delqabLb5xGqJKt0yjClnXLAxBko6XBzv56OkJsu_lR_PygA2_PnlfKCXYBiW6gd37Pxm8f6F2s.4Op4BL3CjUMsjd28K8ZNUJM4Xw2mM0RrBHHJT2JQDNPiomTps4Z3giCZTgfWAHdOUPX2HldzGsMdXyxQJJh5jY3jA",
    "XSRF-TOKEN": "eyJpdiI6Im1Pb1hUV3JOSkY3ZVZSNWpyNzdhNmc9PSIsInZhbHVlIjoiWWtBZTdsZXpKQkNPTjhjUHdaSkYzbml5V1VjdFNNU0MzeE1UTFl1RFVLVzBMa2crWEpSZUtySlAvNklEdW4wNjloM2hNNk8vVllvcENxajJXMzlRQmdTaHZpSGFYQ2J0RzlGRloxWUVielVvM3kwWnlxWlluYkhvU28rYUs4UXciLCJtYWMiOiJlNDBlNmIxMmI4NjAwNTg2NjYxNjc0ZjhkOTNhM2RhZDViODc3MTZiODIwNDcyNzYzZGZhN2NhY2UyNzZlNThiIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9DUHBYMjdsRzJ5UCt1d0wyY3JRQXc9PSIsInZhbHVlIjoiZFcvWGw0NCtXRW9Xa2lBSlZEdUNhV0hTdG5yMjBmNDZNOGNQemUxYUkxeDN6YnkzYlVQSjFyMGRWaFBuVFFhVTc4b2o5b3FUZXJIdnM1K1pUUWt3YVNKdFYrQ3ZkaENseXozdlhMVWdqL3Z3Tjg0OVRQVFhRNDFqSnhqSXM5bTIiLCJtYWMiOiJjOTMyY2U0MjM3ZDQ2OGMwNWI5ZTI2MmZjODY5MmI1OGJmODQyNmY0OGMyNTM4MWQxODY3MGZmZGRhZWVjNDMzIiwidGFnIjoiIn0%3D",
}

