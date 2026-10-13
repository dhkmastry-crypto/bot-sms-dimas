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
    "cf_clearance": "L4aC9YZupxxdcUH2daSf9p68DiCzy26KjqXti3frcHo-1791862003-1.2.1.1-GwDrZxTp6rMFZ05NzD6DwvVi5WBSHIliWLDSKuKElc767aYJhPf0dxJ8mgJMewUt8XslWJX3mMTNf6s6ek82hJu3Yg8BOKITSrbFx1.k4VMrKiAaGZiAd8OSztSU0VYe3WxoWBISBBa2eOy.WFwu9M047kzfBq4B5dt8EUXDszBe7NSpJpWeBxbGA6zbRqVB_ncU1a8Iya5VC6CeyFeiPmWc.6H_ECPwBlBwIB5bM16Qq5FcrxbfFrpvkEHh716Z_7io0LWkB43IowiSsTtq7lpthfw6m_A01DKrjwOq5b6ww1UapKz7xNsrM0kHGenszp9zSm6ub5dx9edqhH9i_dDitsmYTPn0qdc3jCP01zLN2R2mrfgL2BhS8ACntCvJhj1Bs3_WmeEaf.fUdWop5Vj6GvYWnJ_4gv_JED7FTLSnyjw_mb3VvNMQVB0HwAGSY1QBgPEMojPCXIyIA4eNjxQjerxWZ1ehcGDZ5.YotVBYUQp5hae0Q9S6BzTLF1.J.Wkip1FADw13y5Z.yBT6_A",
    "XSRF-TOKEN": "eyJpdiI6IkpXTW1OeEtwSk9iVkhPczl6YktBa3c9PSIsInZhbHVlIjoiWFBiTXVkOHpFb2hpVlJaYWZ4VzUveEpBVklObVpwTW1OSCtsVVJPL2grYnRuSGJKMmE0VEJGNU9meWFPbWhUMGRlZkVicUdwVDZialNNdlo0SUJhdDBRNW1RTnJ2YU9KQ3JobHFQUUNRaTZzT3BZTGhUQ1ViMTRFQXFnRkswL0UiLCJtYWMiOiI1ZDczY2IzZmVkZDk1ODMwNGFlOTI4YTJkYWU2ZWMxOWNmNmNjNDBiYzM3Zjc5M2E2ZjRjMTM5ZmJmODY3Yjk4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IldQSkliRUMxYWtvVVdObmtXZGZNMHc9PSIsInZhbHVlIjoicUZNRlpqVkp3cTY3VmliWmQ1ay9LeGtSZjVnOWJ6VWRNT3FyaEo2OUpkRkJyTGpoZkFwRkdkd0lRQTRNVlBYTXBoVVE4aUdsNUV4Y20zcnVTRDRCMjhvTjdOdHZHTXdUbzNUUDNUanFOTUQyakdKUUY0NGtRYXFZbzFpWWs0ZzEiLCJtYWMiOiIwYzEwMmY1ZWRhYmFjZjg0NjRlMTg3NTg1MGU5YTE2NmU5YTkyMDc0MjI0YTdjYjAyZjI0NDQ5ZmZiZDk0NzBjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Knu._1SkRxgpQ1FnwrOeEyVPc82sNI5EklC3XXx..T8-1791861383-1.2.1.1-l7_qvMAfw8Pgxz3u5dpq6TK.LVVyCeOKRYNQpVvqWGoAb7Ij6Qga8ruFrGlWZ.vX5.Y5uZUiL6CC7uVX.JlAMvMGh0xOzLQTCm2riRK8n6frVnLb7ArbcElu2J0gmuO1grSJJdSsbEzb4A6MVx3sVXo0vHBO1abhYbBeu8nMymIL3Ukik5ycmMCKc6C04vXnXt8kZ4KRn9q_9v7NCIoELEE0IxNG59BDJszWj8usZjTigu0WsdJ9GyoLNVTWexereruBsY06YivC1b1F.MhvnfUuFLXdXFHQVOVAdfDJ19LatMeeNytHo9liOCHBl1RrZFMYFTIpTCuk.C7q2389zSqpdcRY5QKwP.lwLQc9nO6_KSh5rkvaX5lYBCH9FGeVjGK3Vgn3FtGTIzOGimCZoap8FYtvRFG6XgiFYVqjlLL5TpDcZHojsCaF7m81a.EDv30Wue4hPHm_MNH6cBlrg8Ru.fosWurh3etpv_9Wj8cqqT8IQKpvgn.AEon_21XJN5.JajYve94KURlWN1cNkA",
    "XSRF-TOKEN": "eyJpdiI6Ik56bkpCZDFJWHpaSFAxVUVhNHE1ZlE9PSIsInZhbHVlIjoicGxLby9aVGZVM1ViSGxsNVBEbFpHMVNyNXBnTEJHY2dRU3FXTER6bS83VDdsVmJSRXpLL1RnNERITEVncnkvZVNrZFI4QU83SThQc0lxR0JDMkRvcFVWeGt2MVkxeHpVZW9vb2ludUQwSzc1M0IxTVB5STAwTFdTNkxJNXNGTEciLCJtYWMiOiJlOTYzZWI5MjhhZjdjMDk2YzM1NGQyZGMzNGFlYjkyZmRhNzZkMmE1M2U0YjE2OTExOTU0Njk5ZmI2NmVlOTMwIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlRJZ2krVHRLL1NjczlBZnpreGhlbHc9PSIsInZhbHVlIjoiOUhUaG51Mkp5VTF0Y0JXM0cvMkZZOEdFK21WMmhsalg1RCtGRHU1bmRGcXBGUloxWFdBcDB3NjdkVVpZRWJuOThweE5lS1lvSG5jWkhCSjNXa0N1eXZENFJucVdmQU0xd2s4QzNwUWJ6UWVoRGVGWkpFVTR0VW5QNGxlNDMyQXIiLCJtYWMiOiI4YWUzZjc5Njk2NTVlZDg1MGQ1NGQzZjgwNmExNTMzZWEyZjg0Njc4YzQ0YWFiNzIwYmZjNTdiY2FkYzZkOTU1IiwidGFnIjoiIn0%3D",
}

