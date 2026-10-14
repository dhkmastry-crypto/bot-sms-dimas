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
    "cf_clearance": "SDVjHE_bP3.jFqRbCQS18I2N33m9cYREDPQBhjVDm40-1791976508-1.2.1.1-9lZOSWLIYpIOYhuZMNTpnI7rYxw_WBJ0na4XxHy6bDPqF2HiRkv8YNdkDgdXVseyE4fnlFUj7DGmTTfX0EHvTLK6XwrkaYCSriYmehJpLrwAcJPou8HZx.9dH9l5jCCxmizET_5nB.K7l3ONFYh00DIz6t5ksu6CjoUcXTGFg3Ra5AiBWWRhdCdlm.P.UicMEjm4T75VrcdufbM.wGsyrD555JtF1s8M.k7tT9HnSyQnWtQeAVoGtjkyh2xV9XUZGiTae8NWOFWvHiTiPmtJvyreW7krL1Z.a77T0M9ccfBLOrgY1HWQpv1QyUK3I5nCiT46lZIGlPsATqtSkFseyTZf.f1BrS_0ft4szzLF43xRPJ3w1HdHNo8VeG9aaW7WsR4bZSi.ymeg6hOK4_DGhVGcqywJRCnsjCFEsiAHVmXHL9gc05jEsHW3CgRa1ft7Mcmn9P0E8kx1z85r6RL8ZB2X1utxobuL8WoJYrsYnEirOhJsehIYGQK8c8RcpYQaRNOXlpiYvlR_LGP1xrf.Cw",
    "XSRF-TOKEN": "eyJpdiI6IkE4MUp2dEdObWFicjFCaXNCVDNjemc9PSIsInZhbHVlIjoiaFlYdGNDU0R2cU9hT0kraVpvTWJBQ0FjR2lqL2lLT25jdWFibnlsOWlqeGY3bDdOR0hXWWVCbllhd0c4S3lvck1ESVkvcjJrM3ZsWW5HaCtSdHc0WFR1Y0xtNEp0R2pNai8xOCttaWhBZXlMZWNVRyt2NEJtNE16RDlNV3dmck0iLCJtYWMiOiJiOWMyNWVmODY4M2ExYzY3NWQ5OThmNzkxNTFkOTdjMzdmOTU5NzEzYjE2ZWVkZDBjNmIyNDFkZTg2ZDc1NWQ4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFYbnZVNnEvbkgxSVFkTDRsazRZc1E9PSIsInZhbHVlIjoib1JnQlZSby95V1RKM05GbUF1SERJWU1WbnR2TDhsdElqQm1oSUE0bWpEWktHUWtyS0Ftc3o5Ri9ZQWc5VVUyNHlBdC9iWG02WFQ4Zlowd2s1TWNrV1dtUVY0cERDa20rbHVqZXV3WTdpdnk4d0VNTGJMSnRkT3daRUxkQnNYRlgiLCJtYWMiOiJlYmQzNTM5ZGNjNDJjN2IzNzJmZDc3OWU0N2E1M2E0OTMxODJkZjA1YWVjZjE0NzVlZDMxNjA4MTI3MjY2ZTdlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "egPQiywgpYcJwzT2YPEDKplOwQRmfRYKzHxF2dTidgY-1791974811-1.2.1.1-C1V8AenrCEsyxGU7sXyF9OT58p1BzEMl0PKB0NfqeIkXPfb1YipFHRLgzUEiXfFkj4p96Gd2yqutZdjKgkUyyjxOYBzEbB307BoiktpMkwF7Fy1hLnmucA_LXEQRHwmspwZq5aABBwICM.DdryhIb1YMS_RVOpXY3tharLXoBeVhtNGc1ZpzDLnGiffxeodlUhIhYIVnY2OH9sTvgyJXR1_GCqf2P8JxX.U_gWzNFkI25jlBqL0gwEmJ_.7jzSUD9jOOZ8ee22551oh7UJPPHMQaJ9UyQr2LKD5GLWazBSsrt7L9WfnX00ssP5dXut1oDPLRUGPlr3Abrcm97s3hZ84aCe.9Sh6U0oYfbBUm33U2Jhbkumoyr1m4zwWz2zBwPcJLstWFgcaGKgoFBWHn9Jbewh5RUdbSWMBF5.K96lGLZ_r9xd_eViQj2PyYrdoXF4MvDCgB77uzNZ9ISbEmYU05VPbhwnUELjEscQ6hS2p9TkQrEsKWNsih7GsAtkmjg3hZ61Bp.WU44HXRVkzJPg",
    "XSRF-TOKEN": "eyJpdiI6Ik45RmpGUjh5Y21JL2FhWnNla1N2Smc9PSIsInZhbHVlIjoiUEZRalVpWkV1d2hTUzdWMDNVUDUvOXdyK0c3VDc2SElXM1pHWmxjd3o1cGtRVW0wUVJNcitwYnc1RmR2cXJJQXdXNVNzR1k2YzlpcnYvMjNaSlA1U1g3QlBFSTE4M05OR1RFTjNjelFpZnRlc2FzYWZPbjFrV2RTazd5TDBoZWEiLCJtYWMiOiI2MGU0MTg3ZTFiMWFiOWE2NDcyY2ZlZWIyYmE5NzZjZDFkMjhlMzUwOTY4NjgzYmYyNzcwY2NhYmNjZjZiZDgxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjQyMXRvQlByeGkrM1UrSWJzOXI1c3c9PSIsInZhbHVlIjoiS0NBRENGOVRRUk4vbklSM2N1RjJGeExRdnNzT1N5RjRpV3k3R2pmT3ZWNU1DdXZYU3l5SHdVL3NTM0lLZGx2UHNXbVB3VlRaTnNzSGkzMXRzVWtJZ3RrbkdvaE51aGttbHBVLzExV0FIbGNQYUtMbGdNL0FKMjVOdHQwT0lWQWYiLCJtYWMiOiI2MmVhYmIxNWRkOGJkMGZlZTg3MzhkNTg5ODUwYmViNzc0OTc0MzY2MDlhNjU3MWU5MmJhMDhjOGM3ODExZjJlIiwidGFnIjoiIn0%3D",
}

