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
    "cf_clearance": "0rqz_LGVPZp1os__qxhkDt24nlb0dcVZoYirzOGaqoE-1791896377-1.2.1.1-UsLOdFgPfQ1JmOZkolSCGJi7TI0_mpcS1RZvxvBY_kZqhC13dZIWAFesOtQc27IIMhUh42FUHmiQc8OTfqj6n.wQgIBSv_R9xAQTpage1n5xwanWml.Oeommr6GbEHvwYJlUrwdVuw42s6xFVZiYInYs3HMEMtMSkAqKwLwf24XrmJY1EBvCAqwDeYqJbi_keXMQJqDCdmMmFKGEbvhHbr8S4mpOy0OAwi74rWmq4Shb3xzSrfi9XoLSQA8UYtlZokP05G91PiVoDlhNfS2T_3hg.YW8TXDj9bJN9qLze4XNjE7uTuXOec_KtqOpSBi4AnFin60QoFOawuudMJFMCf0LgDoU21H.W1n5CdBHTPNIzH84WA3Xo2loHLtbAQu4FXA2mojzkYLtbIES7_8z3jY1OpmAX8Y4P.PSegplsJht0UqqNA.aB6aQsdFHniaGqQC.vbJMlrr3XS9lS8bqHn71QnSlXe3_xl.zEjfQ3dtaYuZujV215mvmT_l2i4m4wc28QSQaLNybhUb0IeFjYA",
    "XSRF-TOKEN": "eyJpdiI6IjV1R2hseXFxdHoxeFJMY0lZU2RwU3c9PSIsInZhbHVlIjoiWHN6cXdBbWNmOHJCL01LamhsdVRIVEFxMUtTcExlcDZ1dnRlaUx4Vkp0bjRpaFc2cThNeVkvVWkvbE5VVjNPQTlHdHhJNllUdU9qc01oNFlBdEh2eW9WVjF0MVh5MDRpZDZBMFJteWdGZnJNVVV3OTdjU1pkM2Z2OXVjODZWWVEiLCJtYWMiOiJlNDhjODJkNDZhMjA1MGZjYWUzYmM3ZGE1NzY5ZjM1MTFkNDg4Yjk5MjcxNTRhOWE2ZGE2YTNkZDZiNDY5ZjlkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlQxMnFSYjlldnhlWDZMUE9tcU1IRGc9PSIsInZhbHVlIjoicDBkdHBoZ2lBamtRcGFBZjAwendMVmpxNEl6bU1qa01IQ1pma2NSL2lrQ2tReGdmc2s0MWJGWXN0RDdrTFVpcEJaaU1iNjBiYUkwSUtuRHZJN1dwMU5IMGpwdkR6bSsvMVpsTUVEcHJPSDJZMUtDZDNvQTh6TUlhRnpSUlo1ZnEiLCJtYWMiOiIyZjMxYWQwMTkzOTBhNGVjOTY0MmM0ZDQzNDc2MGVmMDlkYTY1N2Q0NTEwMmIyNzI2NGE1NWJiYzY4YjA1YmY1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "d9hpJIzGTtnlFyOfUIev8Ms75QTPAisZnczsE7wAoSo-1791895754-1.2.1.1-fS.K_69EMAVvPzh1DF30oM5xH1yhfDgtaxvhTXkby.6zzGYwiis6OJ34wzHs8nJJahorTlwBhBwbuHfrjgZOuvHvkGmeKiuqUEH3VTz5IbxEigC4l1SxXn5PUKzCI0u4S18PsLk_1TYH5cx1UCImJlX8QSx63Ing_ZnMO1eSpkRMHoYyAPzq1djnMUJ0wFKDpn._qPMR0XqLTN.0Ah.5MAZ1KQJ1p1IPZwawXaw.ZfRu7lCHQ35bYxpqXEnxEMT_qyg8ZY_lcVlmYGN5948hQpUWGTVeEXRG_21pZv_OIvevFX15jOnJyhcYRlRmKNPuEYxKx_SFbd887DIl1NaCNez9yJbBdlgediOVWndRJV_6k4db0XzTTTgFNcPEKSyk78vZD2OhMPTdaYixyZda0ui7.0Eg37aDifS2pqCTTi7hX0zh1YaGFyBIFpP3x9amq_WRYyuefX704M4rlTAGtm8SsisYWJqzgxQlAWBRwmswBzd5hv.YFNxf9O7.0u47.iX.gI204fJSlyBvXnl_ZA",
    "XSRF-TOKEN": "eyJpdiI6Ikc1aTQ4dlk0TjdZMXQ1cmhSN2sxSmc9PSIsInZhbHVlIjoiKzdRSEpRTldYR3M3dTJLc2liaElQYnI3K2lkdnNZTHh1T0FsTksxekJ0NnNaenlXVTJkenZ3bFRRS0xnWDJGNTFIM0dNdGVqQ3hnTkZpMTZmRnlkNERwQ1RxbTFtelRSYnh6RmFDcVBZVzBtaEFlNkVLWmc4Q1ZrWmxEUWErZFIiLCJtYWMiOiI4MzAzODBlZmRmOGUyZTVmYWQyMmVhZmZmNjQyNjIwOTQ5NjBlZTc5YTRlNDRkNjhlZTA2OTM0MGNjMTcyNjc2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxzRjVxTEt5cFpXU0YxRHBWMm1GWHc9PSIsInZhbHVlIjoiZE9CeFhMN3JTQlk4US9xUlZ0SVBwYkFZNzhoU2hudXRCY1ViVER1UkFVU3Y5VDNkN0ZtLy80TkN1b1NubUYyTXc0RGdIMVhmZmsyOXdYZG0wN2xvNjcvUWJoQ3JRT0hYVVlWY3loanRGWlZzck1GMlFFOC9CK3REay9zcVNzM3oiLCJtYWMiOiIyNjY1NzIyYmU4ZTRjYTQxZTFlZWRiYjI4YjRjNjc4NDUyYWQ0NWMxZjA2MzBiYjcxNjYxNDZmOWU4NWMyNmY2IiwidGFnIjoiIn0%3D",
}

