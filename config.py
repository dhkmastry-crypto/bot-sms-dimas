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
    "cf_clearance": "omC_X1_pYm_pTWoS5ziL3c6gQcJYd7QAObfvDYhAF1s-1792028298-1.2.1.1-mU.sAABkFawbftbo94fTe2UUFie6tK1LDxwr7fT3oiWxIhxJWEl..kCIo_zTQTtIbvBVSeoYW4kFbuR77ttyG3TVQIFEWvcGrH7uC4WVNHxKJpZc65zuFTFrK83.WM0egSQSTrAYSHC8g8aeCV2IPzVX26f_138FA67LtDKwQ.NbQzKzx2si4LGrFS5fevDQgMb1UVSZLVrT5sJgWL9vfTS3Dgl.BY.QzfZego0cUVOU7j4GR1mSevKfuQ_W5xarTiLjZKkSI7s3OPtk5I3NafTiEVtejKX5hcmFT0dBb8LsURCwqJ.5FP8WgUCvs_jy.B50QAEjwktUsWMTKbsoqWmG_3zCWJpXAIh2jHCdc85ZCPrlst3gc21PazdFAlCEsphUswZNMx502e56zL8zu6Pt3Q4yR08NW3NcRFmO9DKOG.fXpdHgd4V56O2.lAfA9hQd5JsVRlGqOhvda.SGHdsWEp6QkSK0fcen9haJc4jb.yaXWMNihwgkQnlkT2DyxiDqqC68VXqk_wSrt9GK1g",
    "XSRF-TOKEN": "eyJpdiI6IkI1YmcyQmRHSkgrTGNwREoxanRSalE9PSIsInZhbHVlIjoiQzRkcW5lZW5JWGxSYXJoQTd3RzluL1FzRWo2bng5VjZUdmZCUEdrRDFseTlkQ09scG1DL3VNMGRNS3NhZmoyRUlvd0FUTndvVVlNcUJST0VpUFQ4Rm00Y2VNaGQ1N2svSmNNM1dNbGRXejJDR2hBbUsyUStsYUNxOW1pa3dYUW4iLCJtYWMiOiIyNzE5MWU2MWViNjFmMjJmYWYxNWJjZjM1MzYyMTA2OTQwNTdiMTE4MzFiYjdjYjVmM2Q4ZDU0MDE1YWZkNTZjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjlZc25xcGFVN2oweG1SRVBaUk9BMVE9PSIsInZhbHVlIjoidWcwTFI0K1U2OEZHNEZwYmhad0NSOCs3SU00MiszbEhPVkV5dTdFVWdWaWZoRjNINUtseGpLSjJsajdjSjBoUm9VUHJoeWhTQkg0THV0cjJnVm5leFo4YUkrOXIzcFloRk5KekdjcDUrSHhtZzhDVnFlZDZIUU5pMjYxNVNMdFciLCJtYWMiOiIyYzNkNTdiMWZiODllYjA1MjQxMzFhZWZlOTdiYTNiOWRmMmIxOWZhMGI1ZTJmYWEwZDBmYmZjNzA5MjQzODJiIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "amH5FdEfhUdJQlliv_97VLZh5eNM1b2BvGbzaL.HD5k-1792028288-1.2.1.1-wYV2S94tH7_QQBCM.GdYSCwu7HqZnkPb7iEeqNy0EZ4b_KgYoiYc8iVZWxWyaQLF4bc.0BfhTXAWtBamFpCxm8OMGiDvbeKdBkgIO1fuGTVA5PnlAD.8ISERahnvZPmEmilHZXGYMxoJ61V.otujPwuyQ9QxKTvRbOkysokmqIv6yzsnBETY3i2zZzTdl7kVT9yTfA8VCvNdX3nSVpSve0IGpWFOUQV_iXrXegrCis4v7usNS9Jbu79j.bQQ3mCfW42UmZQafawg6l7yyy2r9HDfIotJwUyWsddS_jQ3D.YgG3axojG75kSJbmBaQqoqw4HMK1k4hndIKpQ6VztnU07ZEn5wUzleNg5.DOAdJCOweGcpXcsK5x.Qoyt7C7rlqeM2WY.Iwi4mW2J97poqJW5ZwVlmq4Jit25Izo1IouYql_Fxd94Qh863sLCwpRDMsK3zARIFoJftEcKqP88bjczonEhHJvFzDEsytYuAbxwCml_N0q6YzsIQYmX5rtXVXR3ZDce.wr.1gT3F7IR2rw",
    "XSRF-TOKEN": "eyJpdiI6ImRJQ0l4blN3VUlURU1RMUdDbktGUmc9PSIsInZhbHVlIjoicFRMamFGLzc2R3RQR05QRjNaMmVVYVY0d1BJd0R2OHhRbGM4dThDYm1pTEI0Rm8vQmx0djVrKzh1bE5Oa0QzeEhDcURjQ0VxMFNWUk55OE1iS2w5RFArNkp6UGZrOGFKRGdCT0ZCZFdKSjgwL1hwR3RJb2FsQkI5MXY1Q0gyYjMiLCJtYWMiOiJhMzZkMGZjZmJiODNlOTZmNTNmYTIzNjY0NzlmMTBlMWJkNGRkNDQzNzA0MzlmZDcxYzUwNDhjOWM3ZTIxYjg2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjYxUnlIS3JyS2ZrdW9VQStoTUo5Mnc9PSIsInZhbHVlIjoiNWRiSytWdjlvbElkdDN5em53M0pVd3ZYZ2pBdHZiOXZiRDRES1dpSEd3S09mN251ZFdNSlJiaS9vUEV3Zmd0V21yRnlqRTVjQ015QVY3VnpWNTdENWJpYjVZTnNid3NBQ3A3WjdQU3BGVHBPTnVoVFRuTFpkREFkaTRJZzFKRWwiLCJtYWMiOiI0Y2QzMzgzNGNiYTA0NTczM2RjZjZkYTY3NmJiYzRhOWVmNjhhOGU1ZTQ0N2UxOWNjNzNlMGZhZjlhMzlhZmY4IiwidGFnIjoiIn0%3D",
}

