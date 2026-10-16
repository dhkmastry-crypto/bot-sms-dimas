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
    "cf_clearance": "9RanN5qEtpBu5lzzPO31_ly5.dGfesc2x65Bbvf9.4E-1792145246-1.2.1.1-KDv5nLJDPvhdDBKegU_aGz_5iRa9EHU_XS_26vCfDHmiM9bazQFvbbdJ_B2FdqhhYpjxZgf0FeFU26hHFuZRRUo1lxXSRJd8TK5mEeYK1VSUW7A0Bb96tvLTPzKt75H2G4ke7IbIoGmtgdiHTOhzxJVJyvoKO2RgsprJmATvAJRnZNP2uEjV06QRwY2q.MQ4wdS39EDiOLTGAFZlYl3BnZKwK.C.15ibU93LBVl2YGEkjLnTxBZarHT7pWPEFOa1_MyKIaAD8JsMzGQDKJsbbYgVxkvki7VYNsdrouogfMe8r54CbAPFYacsRG0XsDhc.s4UsUbKKjp1iViUhuiifgMLKjTJBtB_2aLXwlThE3awTNvEfIWVzmM1l.Q7aqFnlUuW7pcXj2XNuJZhmmQAFL55FZmE.ZbEOx5VxJ8i.JJZ9PHuhQhNL2jLDLpj4O9SkxwuxwRyOTPllNabA3xTKCxykQbaYx26j9gOQ4DPd43qvblj7CY.S_df3azXe5aZUdhT2Wvpef4Q_74AO9OCLw",
    "XSRF-TOKEN": "eyJpdiI6IlJzeGVxR1NnMmZKWlNNclc5MzNtK0E9PSIsInZhbHVlIjoiTmI5NmVOSldFRmgxaW4xRXpELysxQmRyU1BSd28xaS82ZUdmM0J3b09ZSHZ1SXluTzBIQTJWZU5QYU5WdmY4ZXlBSFBvZHAycmE4cEtnWktzd3pEZG9Wck1HelFHOTN3bG5yRjVmcG9uYWJvSm1FWWdtNFBPbHp2cTRneUlPYlUiLCJtYWMiOiJmYjE3ZDYwMTM3MWY1NDE2NzQwZWYwODFhNTdmYTVkNmEyOTY2MzFjNzJmOWNhMjM5ODk4MDAyNjc4MTdhZWFlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkpLYzcwR0tRVHhpbVk5V0tjbXlCb2c9PSIsInZhbHVlIjoiL2s3anZNSXZ0RGpFTFNKMWVOU0dTNVhVSUtVd21hc0xxMnZoMGxkeE9JQUJLcmU3M3MxT3BDSVFNTVZUZ0gycUVhNGMyQ0R1NGpXTnJCcVY0YVVzeWtZTDNmVHZlWlVlbmRmcTNkbWdqaUQzUHdmd0hjWGVpcEl1Y28xY3BDV0QiLCJtYWMiOiIxMzk2MmMzMWVkNWEzYzgxYjhkZmExZjg1Y2U1MTRiYzFjNjMwODc0MWQxMTU3MDhkNjQ2M2YzZDIwZTM3YWEyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "qH1OsUm9bi17sVByJOKMV4ATaCndHlbPOvJDpHdDPpM-1792145257-1.2.1.1-dUqYHA1qu6Hz8N0O1vFDzOp6nGhimloaUBMux5ZTwiZVXq9BPAaPUB8B85PvtsV1vRGaT9V3QZEZYJ_oqg8nRebnxGKTwJJplXYq.OZt5n2jGRkgkbe1GqoCED82TiZ3O9JqQRJ9nUCrYhjMBm.OMDYLeXN_kkR6h3OEIMUpSt7yLRSTYjOp_gq4.HKg0.bvz1Fydi0wwq4CYKHPmz10ysa4AbNVj8.17xiwJAO3TV6_NZ0GXLH532zLjxdn1IVuRS1aW7HI5LUJOBrqxk7APONrpUGgp2iclYz1c.741uXbmbq012NjygJ90wS_012C02g4wv29TZdfLNwlSFS4EL.H65BeV1xMLFvPbte87AjWyGZHEoGRMZBW1LlE3dq8LvUqq2SwkFIRVCPaBaySZdc59b9ZgwQKa2EAj_QagMk6XB1csTUC.DHfX8tXdtDSxMw8c9daQf8wJo4v1ptyzHWmI5QkP2clDW97ZbCVXdYr0sbd1J2JSbTBNbIshJTtHOOhKQMzJqG_QL_l1ddZqA",
    "XSRF-TOKEN": "eyJpdiI6Iit5SnFiL1Y0a2dpUjU1TzVhSlVBNlE9PSIsInZhbHVlIjoiYThVeW9yUHhVTTVRak4wV0QzRFRETk5CeHIydFdtVlJxSGl0c0dSMUhsU1lZdXIxY003OXNVaFluN0ttS3NnY2hxTFI0SmZQSHh1dzZ4SDYvbGFLZXdsVmhCbm5XNHcvZFNUdXAyWjJST2JaV05XckJvMGhnYkMrZ0xJQ2FpY0siLCJtYWMiOiIxNWM0YmJkZjE4MjQ0YWUzMGM5NjViMmMxMmU3YzI3NDBhYTcwYjUxZWRkZWQ0N2UzMmY1NzY5YzI5NTY0NDZjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjRqK0ptdVo3aWFnM3hHb0ZzWmdNV1E9PSIsInZhbHVlIjoid3ZZUk9SWk10d1BuRnNndHkwTmM2UE1aTWg4MXVBdUVtOHkxWlBZeG85cEpSWUh6WjNhN2VqWGJGTnRBdFJHeHJ0YnhIR0RiQXJzVTJRL3dsRlJsQ0ZrY2VRWXpBbm5KYXdYZi9uNVZMelo2b3FRY2pNckZsL3RvVjNyN2ZTOVoiLCJtYWMiOiIyNTY4MjVkZmE0YTI0NTRiY2Q0ODVhMzdiZGE4MGUyNTQxMjc1OTU1MjNiODVhOWM5YWE4MmFiNzA2M2IxOGI5IiwidGFnIjoiIn0%3D",
}

