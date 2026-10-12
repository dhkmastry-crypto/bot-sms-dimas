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
    "cf_clearance": "_bmW_60LWeliLg5QEeaolddJdzHoaxEvo1DWMjf.oNE-1791831259-1.2.1.1-gYpDZ02RyAB3JyRAW1KFrwnuuUp74CFlsnfSkdkgXeniH4pDKN9HihkhtypJ42mfV3p8eYnUl8pA88Nuzi9TwvL.rZYRyM_1R5P5D9DltKz0YmbTYHxbddFH6O4H4WrIACyPO46Kgk5t2HMRT0IZLZlCZsGKNDvZ2CzFMazJkcO.cjiRrWKA8dHt..FJ51h_.cDMaP7QehmC8wVnFcxFaGMgnhDN1GFIw5FvPVS_r_lPTZ.0RuKUp2Wf.D5Z9rvOAYqOwYQYCMSpRTB4S5LRZbXNuSRxKgvAs4zMVGUhmKzq8QEOCHOqKOm0N_ftbxm_EYrABr8Bg5uYhgIOxiHP1z2TYZex9NsHwPt1LShdTsvUtVa3qLL0GjcxuIz7yWHiNWTKbpwawG52c9.uvXayGgXz17.hiA0JH39aeELZEoWHC2sUtSNurgkmyR5Su5RWI.eh6TO5pGT7p06zFgST3DPs63DkwsFP6bulP09bQ2V77UFKiaNnVf81WYZ.Lyuo__F8_JtFOWMBaY2t7517qw",
    "XSRF-TOKEN": "eyJpdiI6IlZUVDVxVEJ6STJaVGxzR29xT1Q3RWc9PSIsInZhbHVlIjoiTWVXQ25IZ3BXeHJWVG50b2J6Y3dtejNGakZMQnFCcmFSdHBzTjF3bVJOYTdmTUFxSVc3alhpSXgwbXJTVHFuMTZCMG9uVUF2b3lFaVAwcnJxTmt6c0JPeUo3RVZyUDRISldKVW5YUDgyRkdzTXNrcnJuMTlIOE5IaEJBZDhodEgiLCJtYWMiOiI2MDlhZDlmZDk0ZWY1YzUxNWY4MjAwNzNjZTVjMzVjMjkxYzM0ZGU3Y2VhZTk2N2FjNjc4YTRlYjI3NTg2MTMyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InlwQWdNRGdpTm1MT1RMSHVGMGtqQmc9PSIsInZhbHVlIjoiYmE1aGNrT2c4T3RMU3ZObk9UUDhwZ1Jpa1VtWFpHMUdybmcybUVIaFlVd3hnbWN0aEpSVU54dWEwN3hDcnNGYmdwclZIUDZmMmY5MEF0ekFQWmJoZk5vbWZBL04ybHJpSnBtbXVQeFBRL2tVeUFzaWY1R0xKWSs1WUtQS0RmQWIiLCJtYWMiOiIyYWFlZGI5ZDIwOTA0ODBkMjQ2MGVkNWJkODQwMjY1YjM5NmZmZjI5NDlhNzJhY2NlOWFkM2M4ZGZjYTljM2Y3IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "MUUuLlvV7hx9LYSRr3AbdMCWtby8FxWH.0BQyeN.Mnw-1791830415-1.2.1.1-7t8emWuHFIO7g.NYk1FAcgkwj2L_8duALzSuWi9fzuY9wLZ7_dwUWYQExhRMN6yNxtslyF3bYWjrRw9OTE2lSauzRknCTJ1XNs372KIvirDeYDVgmZUNFZd3b0WuLQk5H1WQqBuN9Ik75n9UUb799NZoMY1ONd2h1Mz067iKOgINNpOZeP_TEo1yDTXGfxiMq7z2doysRr..Y1OzIeT6P7Z_6X2nj5ivYylP7WidnwN3SX0ZgZlLanQ5zSFDtj7W3IKzqHOF6ZxZIairOKphdImzzLu6pf2.t1ZvdBC5VALn86VasQJrdpolOgPA98qca1FFwkvlTYE3b1g_6YAk8vwvqnNsCQnLOcFcHok3f7Lf2tKR2oS9GPjyCs4PJlm7l0hMotdIq3pganXLDXXyR.LD540hNr0Grz2RSrYi37ZmN4w4q9WRP1Ae6mx8r21HRDhck5GCojOBbi_31fGyrTm9.SdAqsu0AL3nurFkz.y2ctZpgmaMvg03h6YoNNbnF6J55GKVM3ODr6KWVFGVYg",
    "XSRF-TOKEN": "eyJpdiI6IjBDRG8yM3lsSGc0Uy9oeTI5V2pVNFE9PSIsInZhbHVlIjoiTlZBZlVjZXpuV3hxeThjWFJsTlc3MDFSek5OSXF4TGxabU8ydU9CWjk1U2tpWUxnYm1TOXpoTTlKb2RrNkFielA5eXo1VVR4RUlzR0dYc1hDVHU0d0xEZkR0OUpuaFk1Vm5VOXg4aW9Oc0lVREhhYlJ1YVF3ZTV1ZXVaTWg4Z0YiLCJtYWMiOiJiMmQ3MWE2YmM1MzA5NGQ3N2I3OTAwNzM4NGJlZTdlNDQ5OTA3NmEyNWNlNTk0NzkwZGZlZDcyOTI5ZWMxMGZmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InlEUXYxMFRDOGxzTmlHNzBDbGlzenc9PSIsInZhbHVlIjoiQ0lCd0RBakpzRGV0NkhONGFoSW9ibW8xK1UyR25BemErRVFDcFB5OFpJR1RHcXlwdGNvcHh3cmIrUnFMNVZEVWIwSDZ1dFdkYnV5T0RYODNlZmZ5THRucTJ1Ykx4bkFIbTR2NmJsTzRSU2NXOFdPOE9STmJISEVUNlVLZituWk4iLCJtYWMiOiIwNDU3MTA5MmNkZmUxNzliNjhkZTI5NmZkNzdmYjk0NmU4NjZlMzZkMmQwNTk5MjI5MWI4NWEzZTFlZTRiMzM5IiwidGFnIjoiIn0%3D",
}

