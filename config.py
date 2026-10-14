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
    "cf_clearance": "QHHCRIDicbYIwfZM.Yb6HobYDl1zXUtjSEYnwDh0nMo-1791991095-1.2.1.1-P6kgr9dxv67lAVp0ZmCLV.lu7OFjBeeyZcKGnS823RAC3gQ7D7gApqs9gT29pqfpH9lGykwfJb_H8abQc1K_pl46KGMAIfVlRAOi8h2R9nMEk0JFtGsAIz7MATwhotLJY.QyxM1nn5u.ozUv7kRAh0UB5tNH44Z7Hps0q8mVoXCPxilMGtgRVP1YNuuXQpRXuDMeKpAWCgzo7Z2c04.39..q5XAyXejrREaHP8OgF8X9eB.5WyfsfunfrK8ACT8xSzXBFzrIRuoKgL3guA3abRigrif.tm92..n_vpisU0KSwSfMTaOIIoy2RaGLgsUfmydsXEcAHSn7NH2i.xtIM7binIkd1RXi_qCMPrTepguy.tgaL3n0C8yF.BrJDYOiH9XdEu7wreGfWfh3hOuU6cvHFXodxGvl2VhcT2tpY39WhZXRbD_FmFXJa2._6VuUDDpYru5ryDT3bxRyMAOomQbvdVkyCbyG94RWVfPfUcwmxQdVlT7Ml20osATo9BHkaQmMwCdJT_tUBWekcqT7qg",
    "XSRF-TOKEN": "eyJpdiI6IjhjVzkvOTF5Uk01ZTltdTZBYlFFcnc9PSIsInZhbHVlIjoibkt3NCszc3M4VFkxdGMrM1hqQ0J4WVVQeHl2V0lQdWtOcUo4NjU5clZ6MGJVcGt5VDFLQ00zU3IzOVZueVRWc0l3TFJnRm43OTlJN2EwWEdqemthSHV1SFB4Y3B3eDU2a1kwNnRkcC93U0RzZmtlMFphdkZqbkhROVEwbG9vQ3giLCJtYWMiOiI4MTkyYzczZTY5NGVmZTllMTJmODMzNTQ2NWYxZTU1NTVhZDJlODNkMjUzM2U4MDIxOGRlMWVlOTc2N2ZlN2YxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkphY09SZ3dYa3JjbUI1VTJ5NmJqSkE9PSIsInZhbHVlIjoiTEkxVFNOa29oeFlLSnBOSjRWYzI5Q1NqK3h3ZWluZ056Mm1LampxSTg0dnJtakUrd0taT2hjZGVhYlN3R3dmVU9OZFVEeWFGY2h5a2tBb0lHZGlTZ2FLTVBiMTlPWU1aSS9PVUpCaEtGcEQvMjVyWXA3YjFzMDVoZ3dtNmpuRXgiLCJtYWMiOiI5M2E0NGU3ZTI5NzVjZTAwYzNiNjBkMmRlZjkyNWQ2MjFiZGVkYzFhZTU1NzQ0NjgzNjYxOTkwYTczZjczNTY4IiwidGFnIjoiIn0%3D",
}

