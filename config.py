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
    "cf_clearance": "6StHcnxCM3Gp5o_wzkdbPoxcfYRUQkJefldKXXnqEsg-1792054694-1.2.1.1-jCMOHBeLAzRLi5OQjHVAgGJnU1.EKR5y01IfPU1U9Z_l6TGIQLItY_0vsVNp4bNOwjDuQHcd3Hx8.EttfTZpAcCG9d34XuPRjJ2.xnOUsJnYg_ygHCS_RFsrJg9l7och6tyNx54H18Dgnp6REMtKnbwJhQr1rDzPVTIUSFEG7xE77t0wnBWRPFfoBRNUAFnNVqCeQaF6X28Mkai46ivEVsTkMIEjx_9VR1PW8pFzj1kuuTF0MZc3Ggr9YQWMRlinqBb8mOiNKAIFTyBZZn5Pwhl.f3Q4pdLjgcdg0QPPBk9LLz3zxxMODgG3YqZHWFlJLaC79hatD3MDZbfs9jnNMYUyyGSeRe39s9oGbrvZh71MHTLNZA9.DCUaJMoqifJ2wcqzj6hSA5pDhTJ8IRDI8sE3xv0qwyzvKEUiiu74xocHa8m5eOIjYIMlQs6rjnmDQZETlcow4iVbdAd0YRaOHYYaJjdIhQjiMDrpKh9ORA32j07E9DseWN3BgDZgbIplkIAKLXk9kIKO_ovX5lnQZg",
    "XSRF-TOKEN": "eyJpdiI6Ik1OWGJBREEyMDNBWFVvaGFYemJiOVE9PSIsInZhbHVlIjoiQWVEd2JkVUZld2VKVnJlR2dxWHVqZ01GbkxHbUNKUEd5V3dBQ0xrUW9XWDlrZGhMalBmMi92dm1UN0FENFJPZGJHa3pJR2FndTIvR0lkRUphanNEbHorekFFTlN4TU5RZzE2TEpmcUN1YmFNdVgreWRVSjVIaGNaOFd2RHdrdTMiLCJtYWMiOiI0YzBlNGE5YmM3NmYyNGExYmRiMDA0Y2RhNzcxZDQ4NmI0Y2U2MWY2ZGQ0ZmI0MWE2M2UwNzlhNTcwNmI4NjU3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImZGem04OGRlQU4vb25qdEtxT3p5QWc9PSIsInZhbHVlIjoiNUxXc3VlWmovUTRsVWIzcFVMeXNmZ2pjN1oyQ1BPT2ptYnlGQWNzazdwR2tRM3oySTU2OWdVMmZjbkxXOWthbGZrdXhnZlRFK2pkUWcvMDFSL1lpSjJyQlRHVGxjWkkxallDeEN5Zkh0WjdsTjBsZ0d4Q1oxQkkrNnR2d0ltczkiLCJtYWMiOiIwNTk4OGQxYzFkMzA0YWQyOTEwMzc5Yjc3NWY5YWJiMWQ0MzM4MDYxNDZjZmNiYWY4YTFiNTY2YjZmY2ZhMzI4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "JgCifKtqWRTKQUIjmthGXHG_GgVoMpZ3z_Frce4pLno-1792054652-1.2.1.1-hFn87kwpEFylEqyPYy.0eNfhMwv7CeaT5GofS4aUttcC9QBuS0WYV_FbXhR6Bp9x1rMfwG02CvJ7u2uM84k_nnk9MxK51gYraCuq.NILMswplcuzNVTlPzygyFXJlME5AWXyQwGczDMLUpYEAo0dM9HdPHZibL0NggkOnLqE3Pbmoeb6IKVBC7CwI6x7YuAnMdpmw.atuAzOji64ljeRdtzTTANqySvr_67o6AdL3Ea19CmEwtXpxavkzol8yj4DQqyLK68Xd1YEDZAhp4g_BOrZ5ZCpnRnezQhra4N1ixFF82Zg9jmxr5Kal.sAFNO9d4Yqvwtw_Dum3Noz3Z3m0ZmdlabL6cOHVzRr5Sj83FIDbVlFfbS.ZXa5KSpc0Zv9x1biDqLBDxFWsVp5mUhW87NyYPFDlJMi9XVOVywYparrw3h8a5Q7L0xpbP_hhmVbMlx1mh7ZX_a5yBQ9ATg0RvWmqeB1SY4BIl0b7RFGffRE5Z2Msuf69b2aXVPEuJ2elroMlRiwC2o.F06Nh2_x4w",
    "XSRF-TOKEN": "eyJpdiI6Im1jMHE2SHc5bzJTUVJhQWlKbGlCanc9PSIsInZhbHVlIjoidGt0Y1RVTkpCSWVXZWtIV0hQMnAwTEdWMnRjSDRDV2pJM0E1b3BjUEFRYzkwM3hHSHhtaVBUMFdGT0REcFFWUzRWQmdFL1AxeVhHWUNublNNaWgyS0NYMU5xYUNMdDRBaXp4NFNkbTVwR3BTZmZieXFFYjN2WDhra05UVGNBamYiLCJtYWMiOiI2MWVmMGU2NjFmY2M4ZjUyN2MxZTZhN2JiZmU5NGJmMjY2NDIwMmZmOWFjMjlkY2ViNWExNDM5YTY0MTc4ZWZlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjkzaUVMNE83MTFEVnpVN2JNeTlnV3c9PSIsInZhbHVlIjoiRTkxd0F1UkFwcXppS3I0TTh1UXBrVkhDdXBhbDE3bU95L20vL0tVUzQzNDBOTjlmZmFqYlJhbm1yUE1BSkZVVVNTOTJvR2hVeGxHU3pFM3NQRkxlTVBmWnlJU1NFL2pWVHlGeFVra3FrdmljcjZjRU04ZXVVT3o3cGxLTktxUXoiLCJtYWMiOiJmNjI3ZWJjMGY4ZWI2OGJlZjZmZWQ4YjNiMzg5ZWNmZjRlOWFlMjQzNGUyNTRlM2Y4NzJhMmE0MmMxYzlkMzI4IiwidGFnIjoiIn0%3D",
}

