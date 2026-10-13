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
    "cf_clearance": "Lhu7xQ9Py5xPh5wHT1mYwxeExkq6JO.Km2lilxHID.Y-1791852975-1.2.1.1-V95H1jkn6vBQINPVOKxbC8usy_vEZY0jOGnt8riTw5F1kiUwvPg_RwGKn0Hesgid3m55qpLDvl2s6pV0h2VNXCAN5jdEGCkIblFkCtrbgNhDlv71begG2HKk4r8VZD7r1CobWUtu.dqGYpARLo3EW.2YqZhZIqp8jn.fMUcz93YS4._BLiBHDdPs4fFFZeHnkZh1S9bTBqsw0oMwbUb_TwlSlOsX1ZSO8Ui.pmdbd8sYDzmw5PpAySaQAQWuXNXnX4r3_oYqDkJlQnmcBDOrGK9NgSuXKr7sJjVqcrSlSOx2IUZo_cSv48uQpfy9sewk1uP_YPHWzE85sdHNxG4uDhzXB9gGxJ4DoMcFXYsmI4ku6oT2GH0ojL.RtdzY5VtPxZb8yEMauYp2eY4ECIN.QGgi96s.n8tAeX3VAZavUedKDl7KVvcT7Lk_luG5sd7DTtv4ivVEBbnYpC5kR0EgAMJSacgsusNuKHwWAYcro3TtXS_D_SA8vx6mxqb4POYGqE13si5m48q9Rys.DX4oqw",
    "XSRF-TOKEN": "eyJpdiI6ImpkTlFCM2JuZi9GQTZBNXVGTEFaTFE9PSIsInZhbHVlIjoiTDJTWjB3ZEVpalM5cEY3T051eGNHRzlhc3ZneFJyeWVqTHJOdUtCdlVIZWNSYlVvZ1RqdU5wZVk2OTRUOVVBVDVzK0h0bUE4NTBic1RYYS8xYVhydVMvYURHS3ZzWkRKTGFiam9tcDFEMzNSOVFBTFBnVTh4bU9vOGxRT0ZtZjciLCJtYWMiOiIyYWZkM2MxMjdlMWJjN2MwYjUxZGNjMjY1YWRjNjllOGFiMGNkZWZlZTA1MjNlMzc1ZjU5ZDRmZGUyNGVlMzc1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImtuZnBscU5vMjU5VS9LNE9FMmM4Ync9PSIsInZhbHVlIjoiY0cyNjhwKzVMYkRRYW10alJ0NGpVc0p0YzZzbVROUXRPbHFjcnFXeUpIR2RCTzBteTgraXRKeURjUkxoME1Odmx2L3pyS1R5ekN5YWhTOXJYL2VIQnpZL1JoTHhkS3dNcDBZK2c4V3Q2NG9yeEFLK3I5OXVpanhDd2J4Ykg1bWwiLCJtYWMiOiIwYzdmNDEzNmQ1MWRjYmJlZWUxOTE2OWRhMWM0ZDNjNzlhOTBkZDQ5ODhiODg3MWQ1MzcxNzAyYWQ0MDU2NDhmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "F9MG9n6YcnZvXidCPg5f_MJIyH3MHwprc.ws5yjsnNs-1791852325-1.2.1.1-A0CtYkjOlMBB56eRjRssPeh4p9ZlovFeHQXkwJd5TnFK5VI9GCmoWnT.jXqjT_T2CsVKIOUTyZbczaC8IrD4HxEQz_o7cL_VmsRiFh0gJJzfmt451ziS9OzYcQsr4BQj0qm7FmuSpCG.7TphC2cbeoUf3Zda4DsS6h.HuhABsmrCBgl1O7PyjzJnZAdkzyvopLBz1D4WDrEKD8q5fq94ju.aid7HYhJ6vBPIydECg9E1Vni.Oz3j3haD0zrV7x7.NLFTHzw48szZFLZoRBIndKQuyo6Pp45ezMBECHzBD8Ubw57_OFh_KW41rP2.q8Tr3Ks4r.ZYSZPzxdgrJ2KdqlLu5QcXyt22dcb2H1fsk6hFbLirvLkZgdZLD3FFEDTXjYEIgLJ3V4GclbTMI_UmAVPIwTtxEMVCb2uAge6fn_vy67oLBjXwO0K22WqMPOwj4WFqeDnBExvbum1ajSKxmQR2sbrNZgiogvvPAlMOe7YlR1GhjuqCd3xmAGErJh2smmMXn1Y4CtxdA1.cU6ESfA",
    "XSRF-TOKEN": "eyJpdiI6IlV6UjlnUVpKZTIyZTNTV2xtRnpRYWc9PSIsInZhbHVlIjoidTlVQVp5N3FVZ2xsc1VVV3V0Qnc3RFN4RC9RUmc4STBtM0tKdmF6OVp1K3ZoM1ZtU3lpODVidTlDMnRFMlpvL1UxTmNHV2tZcExBdkdSVU5sYWpzU00yb2pzNnBjRmoybkRoNkt1akplSW5oNWpLVnR1bDZ4d1pySmdzTnlyblEiLCJtYWMiOiIyZjc0MjQ0ZTg3MzVhMzkxNjgzMTFmNjNiZDhiNWU4OGQ5NDhkNDRiMTEwZmVlNzMwMmQ0ZjUxMzQxYzNkYmRmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IncwTE15NUpaRENQYWFyOHQ1MlkzMHc9PSIsInZhbHVlIjoicTFmREdEd3oyNW9aekIwRHRieG9HUlQzYzJoR2VVMS92Vjl2WURKYmxncE5mc0FuYkJrbG54eVoyeUZ1bFpqRWZ6WVBKaXlUSHNJVHFFSEkxKzVST04rKzgwcTkwYjE1dnh1UjllN2NMTllKb2Z2YXUrODBMYy9tc2NQY201T0kiLCJtYWMiOiJhODdmZjAxZWM2M2ZlZDRhNjI1NmMxNTExNjA1NzRlYmM2N2IxZGI2MDFmMDMwNzUwMmJhNzY2NDMzOGRkZTZiIiwidGFnIjoiIn0%3D",
}

