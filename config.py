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
    "cf_clearance": "vFIP90xy235KCh7rZv9GsPutcUJ6kNx0kZx_dayToCE-1792015629-1.2.1.1-mSHP8rHhlPljjWIzbUvZYqpoK8_Fn4UWICUygBF2l1QmqXCnwh91N7lgEUPUgnixxrF3uBCikDztI.DtYUD2COMk5YWWnragalpYXujWqCI.8aLwDz88hy4t36jrjl4PO0WgomRDmUEu6Canl_udYRkI_hXxUolu.pV93tC64kxE50o1YxRPdXXaa3dFznfO4W6aJhzgD6j5_sr3NgXxRRzkQtflX31LHa68L7hH_Cqpwt4K3oJYs8d79dmEePigzQFDDoAtxuzqzENLnqIQcgq4kldOteAqpCrL9KwcLZJiulo8SPOGcrWt8.OFpG5JGpDWAQyEv4RMta.KFOjemRI27EksaRCqgpjdhbDcFpPYSKRXPgd02eIb484xr8Enir_DsWok_SDCkGdrHdaxfqX4_OPULdrsSY.QD.rWu7bXwbV3CBadAoHCyLyQLDghT5Fltyyb9cjk_TF0pYWJqUJceLSGeKfz.BrKVIMzLbsErLUoMyeMgXh6UL2bhUfmwV5qk5XuJXTO3mO240NCqw",
    "XSRF-TOKEN": "eyJpdiI6IkZPVHRxVmlibVc4bEJWc0ZHQmFKa0E9PSIsInZhbHVlIjoiU0pqU1A3YnhCK2hRMjJ5YzYyOTVja2doR0pIVWlHVGNLNmNpaThqZHpJaWFCbCtkNjZXanMrU3lmaU5ZUVMraTZxbUhwRm1yK29aVytncG9xRTlkbGtzckt3Q3pRdnJmTENYcVE1UThPUVZlK3JkSzRCZk9CZnkzaFZtQ1QwbWoiLCJtYWMiOiI3MjQ0ZGY5NmU0OWEwN2VlOGVlYjIxMzk1NDQ2Zjg2YjE5MmM4OWRmZDIwZmQ0ZWVmZDdjMTEwY2NjZmE4NDAwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjgxNVJ5QXozallvaU1WcHplN0ZLVWc9PSIsInZhbHVlIjoiZWRQa2M5cFIwNnlLeS83aUJNdEIxZkZ1ZTNRZ3d0WEMxQ1MwTTJNeXlxTHpGbENrREpKcy9PYktaOStyZDdSYW5aNEpZTC9pL0hnRDZ1a0NaaTdjcG84MVhnZE5kaitzQlA3cTcyMnZMd3JTc3FLdDdJTDdDUUFIRlIyaXFpenkiLCJtYWMiOiIyOGY1ZmFhNTYxMDE3NzRiMGMyMGJjNzkxOTdkNGY4NDdhZGI2YzE4Njc0M2Q3ZDQzZDc1ZmFjYzI2MzEyMDI4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "C_R.jA2EjAclSvcw83GSRxLQ5ZWdm.rxTM77z_xbpVs-1792015606-1.2.1.1-Z81_30TJvWGELKrWkWE.RQn3vaLbOxv1VHaIcvqHm9zYXAv7vnx.Dhy2mDG9GETS8gUsIj5XWUVuEEDC8f4iGOL1xWQ5vliRkTCAOP4KyDe4Opbr9NWJ_tFyRq1IPUN_ASoVDrYccvbrbHy.FXU5kiEFe_.SAw5wE6.Jq07ftYSBl.ybIIIICnfeIJN3PJNNe6JW6fykvXyPmVGRAL.iXwKo0_Q.xo7.n6YL4Dwrs_iR_NkIvz2ZqByeoCXGacN5.BLsixblew6tgzikuIA.DjuhqGPOJznF3lQQCPHbfbiYtVX_cABn91eelEwK2XBbfeJ135OfWOPrm.BiTaim.Sn4IEK4HNWrViDxxgYNkVRm8QAvGbsQoDVfFWEmtRDULTyBatK27Yyqi_vYwiktefbvJH4c6BR.KletcIUIpJ7EQlFhKaG2dUpE3I6g90Glr90.rLMo07LInDAkHoXIGdkS4k_MAFbhwiZG9MUsZcv4XhMhZf8.YEPZ.KvhLyyexHd30MZs4bJz.rRySUuAAQ",
    "XSRF-TOKEN": "eyJpdiI6Im1ub1o5NHoyWkpwUDVEYVJ5VjNDV0E9PSIsInZhbHVlIjoiOGlMbU1qS2hDZ2tLTUwxU3ZUdXIxZHYrTHNuNE55NzZzZ29rcDFNbWdtM0dXV1hHMFlQVVBIRzQ4OWJaMzVrbTJobElQOWNTZDU5ZzBnUGJHVXFxL3Y5ZVRITk9YWExSSW9wekZQU3ZOMFJQVDdFK3hEOHE2UGFKWjA4NGxGaWwiLCJtYWMiOiJiNjUzZTE1ZTJkODA2MWE0NmUyY2U5ZDYwZmYyOTRlMTQ3MjE3ZjVjNTBmZGM4NjRhZDI0ZTA1ZjI3NjFkM2E1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkY0M0VqNmdIUGFYeDFScWVVTVJKc3c9PSIsInZhbHVlIjoidnhJY0s2UXZpamJyM0x3MWM1QlNwYkN5aDd1QnNueFB4Qmh3RWwzS3Q0Vmc0dzExai9NaTN3eEhxeVB4R0REbUlSNmtSOW4wdWNSNnJIeUVjanVZUENEQ1dRalB5dlBSZDl4djVPSS9JMVV5R29NR2hvNHNWNy9qb3NtTWRpRkYiLCJtYWMiOiI1NjhmNjgzMDlhMDc4MTdhODRiZTg1NDExMzgwNWY4ODRlYmMyZGVjNGI0ZDMzODE1N2M2NThmYTZlODJjNjFjIiwidGFnIjoiIn0%3D",
}

