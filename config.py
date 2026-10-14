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
    "cf_clearance": "1K2IqiRo5zVjzJUfKCWBPMPIwiHJO7Zsd_Y6uGItJXw-1792006587-1.2.1.1-P8iuBsDPfmlkQq9oaQCrJ42voVPoslix3bdUkXu8BB0kKkO.lLn_S2D1Jl14apZ5bn3ghiVjKcrPhlwQRTQIHH_JlZuuAT9Vv3HWIOBi5rCrgis.isTBjnIMDsstQju4C3B0_WfwtyWLOKc.qxeY9exo9aVa6xYqbCZuRYcsddH.ZjrECs85HctE6P4E86Qi5XzSuLZhA2JeV0sbF95sGnVvbF9BXB1veJGwaCGaC8Sbp.xIIgtB0_ToI0MxXUmXhrJ_cE8Efu5ADjt.HcMuyc9LL6T12vNx8HbAJ7_tgR44fRSB6XXP_vT_unGytkzTEbHxXnkdPAlBQfNs5zQxMh1GdmRcCNBRju8uqZJbLkX6HmoHASkLftx3GGPt9FXXvMZk400QdufuvVhUBqxMdafZhTRfI6uhgnU4vDLA1x7JBAyUMsPx9rQgr_Ni9w8E6BcIlzJEshKzdlSIeTwE7mZi2SebK6BzQqBk8H_SDdd6eCGUW6kOpiCZuPcJpruBMmpj_6A4H5frrzDdpZJz2Q",
    "XSRF-TOKEN": "eyJpdiI6IkxrVkEwNG5ZZ3lhYlZvbFVqSWdEU1E9PSIsInZhbHVlIjoiM1liK1pqMU1ROUJKYlV5TWM1eEszcGdwNWpsb01qN0FsWEVudGN6ZTM4TVArWEZWdFRZSTZKMjdqWTh2MDRXSTVXd2Z1TjFkQkRMMy9SMFJuenhwOWlSalhMSVRRb3F4SERNL0t3ZXYyVHBXbXMwQzByOGVxTjBNVHkySzQzYVYiLCJtYWMiOiIyZjEyOWE1ZDRiNDZjZDkwOWFmMWFiODI5ODBkZDJiNWIyNTgwY2E2ZWY4ZDhiNmZhMjYyYjVlZGIyMzgxYWJkIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InhocDRpeTdzczdEeG5DUzRsZWJJUFE9PSIsInZhbHVlIjoiSUo3SWVKNVdsazJoQUxYN0IrcDlNcWsxcUR0aFdFOU8wNm5pc29uVG05REk3cldsRVBzZGo0UjBoMVNwTFpVZHBnNVY3NjdaSEVaY1FBWHBBWGQ4U3h4dUJXbU9GWkdQYzY3enJxb0ZMVzJWWHplRGEwSWJJVjUrUzlQdjZKRlYiLCJtYWMiOiJlYzg1MGU3YTRiOWQ4MzIxMGZkMmQ4ZjU3YTUzNjI2ODJkYzI4NWQ1YzRiMGE4NDc5OWNjNjJlNjI1ZWZhZmU1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "156hPmBE81pesehyZTO9o.qUbAynd.iwYkUBKMW3FsU-1792006554-1.2.1.1-f6TNYhV9JN1b3VcxvIi4z7ckWI5ucSfSB.kI30wyt4Br1g7SNYYEC4tr8L.bawj_jzNXiUHtnKetpLehqfT7LpSnur_kAlwq2u32zI.wwoa0y.6DapyOSFrth5_XirBiIqyW3AYuDuN7K4pNKw0VrXTnN3bjusg9iUmhwPS17o08XW9.niL7Rk7dc8MS.7med3FpHfy2O06O6cn_cwRRjqJwkpCoK...7wIaptcmcZtP_wYYcSizAKTvQqRhBS2XUKJ6xh_6bBhI6AS1zIi4EBhJtFXvr32kKuf0zEyBmfbJNdzp9w6_7TK7McxOtMV.EkTJvznOhm3Hotc7uBFCIR.kzLb7lbk.czp_j1u19vbhDjOqIbc7nuHAC8gmANm_B4TUBaIvLY30k0YsRr4TXvS.2v7bwfER68iKDKDL7LAjqbk.VHCkRzVsfy1lQJNssOsaZEPV0AN_ogYjiwoeoMQoiDYDZ6bR.KMTnm2fFwvS7I7Gc0sq.XO6qcM1aKx5nqAubpM3rl2_C5Rj7CYn.g",
    "XSRF-TOKEN": "eyJpdiI6ImMycTVPdDM0MzRrMkZXdXBIMmhPTkE9PSIsInZhbHVlIjoiT1Q5S1d0Z1NRTUk2ZzR2SEdFTHFMOTg4VFp3eU10L2tXelNmV1o2NTM3LzBwY3dSeExxaDlTakg5ODQ4WjliSmxlMVRNeTRZbndiWjFQMDk5anlFeVhvZkYwMkRwWGlpS1YzNWZEaUw5KzVHanNvWTl2YjduNTh6M1BJbjRUN2UiLCJtYWMiOiIzNmQzMDgyZGM0ZDVlYjAxZjRlM2ZhYTA0OThmOWM4MzNkYzQ5NmE3MWYzOThhMGE3ZjZlMTI3NWI2ODQxMWVjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImpLWHNFbUZjdm8rZmlkNEZleDN5ZWc9PSIsInZhbHVlIjoiekYwVDZvbGhPVERMcE4vM3hQaDhWdjF0OHNPNWhWSEZhNXF6czJSaVIzMm92MEd4RnBzSzl3UnBldHI2N3BhQU1FUWhpN0hEeXQzTCt1RmYvdGM0UHJ0dkVFRUlRUzRmVU5EYlRuby9TeVhxWDd0YmRKVGcwVlUwSzBUM0ZnNnoiLCJtYWMiOiI1NzQyNGUxNzM1NjczNTIxZjMxZmFkYWJlMGQ5NGI0ZmI5YTA3NTFhYjhjMGM5ZTQzZTU5N2FkOWQyOWIyYTJjIiwidGFnIjoiIn0%3D",
}

