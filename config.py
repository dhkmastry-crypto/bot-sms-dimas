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
    "cf_clearance": "JgCifKtqWRTKQUIjmthGXHG_GgVoMpZ3z_Frce4pLno-1792054652-1.2.1.1-hFn87kwpEFylEqyPYy.0eNfhMwv7CeaT5GofS4aUttcC9QBuS0WYV_FbXhR6Bp9x1rMfwG02CvJ7u2uM84k_nnk9MxK51gYraCuq.NILMswplcuzNVTlPzygyFXJlME5AWXyQwGczDMLUpYEAo0dM9HdPHZibL0NggkOnLqE3Pbmoeb6IKVBC7CwI6x7YuAnMdpmw.atuAzOji64ljeRdtzTTANqySvr_67o6AdL3Ea19CmEwtXpxavkzol8yj4DQqyLK68Xd1YEDZAhp4g_BOrZ5ZCpnRnezQhra4N1ixFF82Zg9jmxr5Kal.sAFNO9d4Yqvwtw_Dum3Noz3Z3m0ZmdlabL6cOHVzRr5Sj83FIDbVlFfbS.ZXa5KSpc0Zv9x1biDqLBDxFWsVp5mUhW87NyYPFDlJMi9XVOVywYparrw3h8a5Q7L0xpbP_hhmVbMlx1mh7ZX_a5yBQ9ATg0RvWmqeB1SY4BIl0b7RFGffRE5Z2Msuf69b2aXVPEuJ2elroMlRiwC2o.F06Nh2_x4w",
    "XSRF-TOKEN": "eyJpdiI6Im1jMHE2SHc5bzJTUVJhQWlKbGlCanc9PSIsInZhbHVlIjoidGt0Y1RVTkpCSWVXZWtIV0hQMnAwTEdWMnRjSDRDV2pJM0E1b3BjUEFRYzkwM3hHSHhtaVBUMFdGT0REcFFWUzRWQmdFL1AxeVhHWUNublNNaWgyS0NYMU5xYUNMdDRBaXp4NFNkbTVwR3BTZmZieXFFYjN2WDhra05UVGNBamYiLCJtYWMiOiI2MWVmMGU2NjFmY2M4ZjUyN2MxZTZhN2JiZmU5NGJmMjY2NDIwMmZmOWFjMjlkY2ViNWExNDM5YTY0MTc4ZWZlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjkzaUVMNE83MTFEVnpVN2JNeTlnV3c9PSIsInZhbHVlIjoiRTkxd0F1UkFwcXppS3I0TTh1UXBrVkhDdXBhbDE3bU95L20vL0tVUzQzNDBOTjlmZmFqYlJhbm1yUE1BSkZVVVNTOTJvR2hVeGxHU3pFM3NQRkxlTVBmWnlJU1NFL2pWVHlGeFVra3FrdmljcjZjRU04ZXVVT3o3cGxLTktxUXoiLCJtYWMiOiJmNjI3ZWJjMGY4ZWI2OGJlZjZmZWQ4YjNiMzg5ZWNmZjRlOWFlMjQzNGUyNTRlM2Y4NzJhMmE0MmMxYzlkMzI4IiwidGFnIjoiIn0%3D",
}

