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
    "cf_clearance": "_.yHtUAoNgzDg8eGj0xPYt5.Tynaib6ewdMGNz3QmJE-1791992831-1.2.1.1-FBUxQ3IUJhwpMLX4zrd2rT.pjBGqQ6f_oib_c_NOyb_7vZTQZIqGoAa_YCZZ6V.lNR8DM5xeqmhGVBbqbDd3.7HhIEMh4k1H3LKk6i7wTZruAiT7jUCkyVOJNZHVtxbU75P9Cddpl76d7OO3KdnbpEzlixsPRBeny_RYbo8.F48pnJVsa.RgqvkF8hFefMTYQut3fT9Fb_nW7Lw5DSeiOnexZUuj__8zMRBeJpiF73UccmLkES623pdgaxpgh8iKClR4BETYx1rAPjszhhTTpWI91zlQ5M0ZlnihANP9Ry2od7R8.GJURyIu0SsVCLusZN0p1ATWrlUknhFKgl3jwiH7ASxC.Lt5p0v0wgaCq7vysENPqDtaVLFZML8X0RCWK.MeuR8EaWw.2j.LTY1zXqucmZICQXx7_iFqcZwhQqM.9IbzM72Ryxo94PvyJ4O662f96T1xirQGUTQ264e.B6sstJtAs8un8JXl8DQrHNOzVjSqQNyE4V71V0bazhVMWQ8nhQBvrQu9HzNKY1NNbg",
    "XSRF-TOKEN": "eyJpdiI6InpkZ0RoTFRnTEovU2NCbG9OdW1SUEE9PSIsInZhbHVlIjoiVTRZck5TSUg5V0FiTnpMekpLNk1OMVB5OFYxeEZuUjRLMXpLVTBFekJhOGRSeWRIWkl5QlZ3NTdsWStSTzV0QU8ySmdlSDE5M2hieVFKWVdZZTNLdWZZOVNmcElUR3ZJU0JJUTVQVFVxeDllQVlMQXUvNm43dmlJZTFHWlJrUE0iLCJtYWMiOiIwZjZlMjg5MTM2MjRmMjQyY2E3ZTlhZDU3ZjkzOGZkYjIzNWIyYzQwNGE5MzZjN2QxN2JiMmI1YzU5ODU0Y2RjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1NMDJEQmtJVTB4dzJ1Q1NVSUI0cUE9PSIsInZhbHVlIjoiSjllcmkrY21qajNER0xZVmF3emhnN2FiSTFGUEs0SENjOVZrbnZJVmp0OHVMWklFWmN4YTZxS3d1N05nNUpDRCt1WUNscVlPaTlHTE1reThOY3lwSVdCdnREaW1aaXQwY2h2T2h3UFVQK3hHcU9vQVNaYzNnMG1DZXI2U2FYZVoiLCJtYWMiOiI4NzZkZWVhNDJhY2UyMzg2NTk0NjNlZjhhMzVlNTQ2ZGZkNDQxMzEwNDk0OTFkY2E4NWQ4ZmNkZTJmYzg4MzFlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "rKsdBclKgLVLMvuN.pjrrefMGcSf_d.3YH_jaxTTb0o-1791992946-1.2.1.1-q7QhcHp6ZBt8DKVpuoRfxhqH1KniTEeZVvIyfItUksvVLE8G53RQvTykNRdrDmxA6WzzKVc99YW2b8b4O24qpzQ0ug2isDS5WUSgz24VFLbcKDGQFBC2Vta74Bj_Tc8RuzABxQYJhPvqoSP4Zl7T5E9pEY8qp7_tCXNb1OjHzF71uA4XVSMChugjjwwN5rWNES.m5qEuLSOvJRwSzkVwS5sMWsGBlQAj1E1rH07vlj36yhL1QQ7ltf9SeVSZBLkyrJhfkPd3UMOc2CVukekWResx7o3YjPsxvrqHczvueaBgaekEn6Kxj6WdRbgz3bZKQOsbw9KyZBFLjRk_cuzHQGIWbx4IiEGBLDjBNVvKITejSqPNcE4kqWaKibgLl9ihl5b5pnX23PO9rv_vnSlUuEIiXphF4Ijw6KShCW8B3tLCJf4tenVykOCfd4TIfhkm0EFbE_48qKrzR.ZNpmDyzcFTYxOGzgUtknc.lZRY0Zjre9.taCVqVs5RMka8qs.zo7DCfZYatB1PbmwZM_JidQ",
    "XSRF-TOKEN": "eyJpdiI6IkUrOVoreVBYT1hmbzQyUDNOU1FTNFE9PSIsInZhbHVlIjoiOHowUFg1OWJNV1FLSU5Icmo0QnYrSmFzTjJCZGZHRVc3OE1FT0J3K3RtcnRST1Y5eTN3OGRjdmpXMk5PNTJLdlJqNHhoUGE3aTNiRHJNS3ZQTlRiUTJ4L0xWM1p3S1Y0OEt2VlA3SDF0YlhuYmtzbWg1d2tOcVM2aEIwVEVRNWYiLCJtYWMiOiJhNGYxYjRmMDUxYjUwZjc5NTVkMzYxMWFmN2UzMWIxNjc3MjcwYzAzMzczYzBjMDE0ZTIxYTE1NzQ4ODJmNGM4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImFzdFhkYS9XV3gvUEhLa3Y2UVl4WGc9PSIsInZhbHVlIjoiSGZXc3crWmxCUjd3QXplNEp4bzJSTGk2ckFpc1ZaOWxlUU1QNmU4T0w5enpIWnpwYzh5UGVTUDlkZWl6YlJXTk1mM0kwQy9BR0c5WEgyNmNqRk85UHBzRU9WNHkwN01rekUrbWplT0V0QkFyWTRQbDc5S1NOekpHblhiZENnWTUiLCJtYWMiOiI1YWI1NGY5Y2MzZGUxYWNjNDZiNzg5Y2QyYmRkNGNhNGQwYjZiOTAxMmRkNDZkNzc4MDAxM2I2ZTliZGY2NzA1IiwidGFnIjoiIn0%3D",
}

