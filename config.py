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
    "cf_clearance": "ic.zIPffM4Is24ZMWoGse80PIW7vfyGMwW6ZqkzOumk-1792052882-1.2.1.1-wOLp3pVte_TNUbbu0aiea_SB_bcnYuzXWGCzMm1nxFaT9TS._vlmyqI5.5JzTMmNGg2V2TGKPKuCgzEgwzZOXhJcAEBo_CO.t2aaj2kivshaBQNthaXeXIcQAEEFXBBdtve3rTmC8tvSVWxwPpqK3NbtJ_uLTAe6PPCd36VmEfrIXubcd_ATfwTTCTvbwRLomN63micaXEgTheNnuv6k52aHW4mj88Jh.mdhMkM39tbdLqWu89_Imrzn7ftqMuNvPe3y5LwVdhNRLVpRBlihMeh5WC78qranuO4ADQZbD7j9vblrhwuo337Uqz8Q6yEnETyYFiMz3r2qtSPhSC9hfxcMMKHyuykocqkwJCB.fXx6xUuddP2ezqA_svqRlbDBJDAvAkHFCIy9zJYk7O9IIrAjIIL3I8cnoYxq0xLAr2.AeO1VoUN04X4zJ9Uu4evlhtHB8t4bj9PXKmreN2nphEh39YOkC0fkppi5RCdhOsxFFjTyn58T8rwb3bQHGHhGTs7_.F4mMsMzgrvJyZy7EA",
    "XSRF-TOKEN": "eyJpdiI6Imo2WDBtR1J1WFRjTHo3Q0gyYVpuOWc9PSIsInZhbHVlIjoibm5DOUJJZjdrZ3ZGbk9saVlZMUduUGFSY3ppc0ZqWUd6dmhscitPU2NDdzhBOU5aQm1RTFJ2VlJvcTVlL24rMWdWOFZmRVFXamkxb2swT0tKVFh1UklZWE0yMllpYTBIZ1NXb0s1SzlleFJGUUJIelExSkxGOTRneW9KTnVNajQiLCJtYWMiOiI4YjYwZGNhZTk4OWZhZjgyYmY4ZTNiNTAxMmEzOGZiOGU0ZjAwNDBiNGY3NDY5N2YzZjMwYTY2NmE5MmQwNTA1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilk3TUNzbzNjSG5vUVlqZTdCR09UWnc9PSIsInZhbHVlIjoiV2VRbDZBM1BVTGVOZ3NqMzVxOTNHZUYyZkVYZW5sbW1OY3praFhDUlNTdGl2VHNwTXJKVUxNRkJyM0xGYW5CWllHV3ZQdVQ2K2Rjb0NBUDZXcFlybkRDazhBL1VnM1AwUmlJQmF6ZWlmblJ0RlY4L2VCb2cvcExzODVuMWhISG8iLCJtYWMiOiJhYWE1NmM0YzliNzAzMjFhZDY5ZWNjNzY2MTU5YjM1OWY4NTI0NWYyM2ZkNTAyZWUyYTJjYmM0ZDQ3ODBhODlmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Wsx3.purbWm3lqmaQHz5fO9hqQYc3Dt8DA0a2ApBWP4-1792052841-1.2.1.1-FJCo656EOY9OCY09zVLshjIapTU69TqCexEVYGKkwhaJf5ZBV8RcDuTg6_R4YTwRHW2kV.jAf900iHdGwynFP5u.Mak0CK9LuZmj45Cp8.d.xF.bI9etPyLMbJhnn2l8NVG_XOrvah0RBQ.Fr0ZErEq4KQ9tj2LiRnv6gay_hrorDRwLzN8NtoN79wdHJpPiMVvouWkIn8Q6hWlqfHwOks96EUp9xkfqBi9oPonX_Tt7I8qylm7f8qsRJAlfkyqlWKSBInpnQVXMUtKgN2MqEviA1cq58TEmtgGDhAwlKiN4iLYAB7UUuIv0jDc1BI_hIJb.OO4dSNXGCQVxJx2yKwHshQYpIRYNsPhpUz43ln_NGYe1iUs3LukAK2jy0.eyfZ4f8PG1asvVxaeRvzAADLx0T07FTbQlmmIcrY68B_uA_ex0duC3bQi2gHu2g0KbkWxrHNFSPCLYpZ3QjRVSFVxFdrRlEmlytdi7YgKnPIfplhJGbJNVkZtZCk6hSPhN9NoSYjLo08z9C4WACDgPtg",
    "XSRF-TOKEN": "eyJpdiI6IndJNS9BY2tOM0dPTUwxWTU5Ri9TN2c9PSIsInZhbHVlIjoiL3JUSnZNdjVaMFFpdGszL0M5ek1Fa0tYOWorTFNrZkFxZFRqWEVtZ0gxSCs1Nmd1V3Jwemd2MmJ2MFhaNUw5L3p4eXNtZk5iNys1aS9rdXlBRlZIUkhWR3htbmVGWkhXNFVqRXhEWkRLaFZKREhLUGZteWxNelF1VzAvQ2dNcUMiLCJtYWMiOiI3YmFhMTA5MzNiNTUyZTVkZGI1MjQ1ZGQxYzY4YTlhNWU1NDhkYmZhYjMzNzg5MTc5YmU1ZDJhOGRjODkxMGI0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxrdmZ3WFdoM0dSd0EySzVOUjhJVmc9PSIsInZhbHVlIjoiMEgzbEo1Sm9yTXFUU01hYWplaHEzOGxoRzBBeGtkZTZxc2sxL2lsQzdWN3N1Zm1FUGxrdjV0cUxhWDFaQWRBcmlLOEZDTEU3dnFnb2dxMk5iNWlRNGVUVkE5ZHBzWlN6bDlpVTllS3A2WDlJY25yQXFuczNzUXJaVUpMSU5GM0QiLCJtYWMiOiJlODExNWEyZWMxYmM5YTk4ZDk5NTNhOGI4MTUxNThiZjhjMWFhYTU4ZjQ1MzY2OGIyMjA4MWUyNzhkODU5OWE1IiwidGFnIjoiIn0%3D",
}

