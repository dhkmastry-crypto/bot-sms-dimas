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
    "cf_clearance": "EgJmj9J18Zar9tMMfMWzZ_C3gGTYp8j3HK1AtCoSfZE-1791929464-1.2.1.1-ikKhu7xjLh4m4BjbpwHwGjA.7X.5jMGzPiDsOiG2gXfxEIrCCPXk0s1VP00qtYs4SwXGT26ZrOvf1z4PrE_rzisuQcUZWb5lVWe5vAG4nPnROikbBMIMi4weYxncIrPqNoZXPNV.D_jpr7Ws1awFGu3sPfwJZTB4qGXrXd4iEDJclqVheykiUG3ogq3w8Faf0Mav2euAI1adojh8Rl_zD8gKVtLCl.9MSjVRrP3d75YhNVjy0wRLjnBTwrc.P9iFeupymR5vKRgiuFIeFZXtXiiM99_prgmqwDkaydxPMwcUZ.dqcfgJ1uE3.YNvmcUvJgZ.ZxPBJwPWF9b4CJLmJLafRMCTM3KPOyyF6XWT_2S5MAbcQOk22jtW0LBpju.yr528d7Vh2Y.uSdKVhbCBq3tw0Fc9VJxK.RsvuoDw0oI.HWQOKgfQvEznsEJTmKwItUJ7QVGKzXaUaRu3Tec9ui18KopsrprllxaGNeXh.cABt8Ay9nXoiXEgWB9.u_BCstJ4z1SaXA0DBVCA84F5oQ",
    "XSRF-TOKEN": "eyJpdiI6IjkwbjlPczEvRVB5WkQ5LzdSaTl4MXc9PSIsInZhbHVlIjoid1dxWDhoZmZQUGhSSG9hejB4TTFWMmFSUitXdk8zVVNCZldacTROcHhxdnZ4Q2o1anNTSTF6MEU2WXZ3OHBNK3RnZmxxOGw1MDBiSUVpdlN5UXFVS2lmRTFvUkMzeHZUMW9Qa2NzbGVXYmgzQ1ByUUpvVEZmbEI3MEh1Vi9OWE4iLCJtYWMiOiI2ZGQ5Y2M3ODA5Mzk0NTFkZTA3ZGRiZWUyYzk0NjcxN2I3MmNiMTM1MDM1Zjc2NmM1ODc5MjllMjFiMjhjMzFmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlRuK2RJZ2N5bXQvRldpbE9XcEk0OUE9PSIsInZhbHVlIjoiZWVscE1ZckpETE91UGorTWxPZ0p2L0pTeVpRVDdJV1hkaXpjbTEraEhob01kUlV4ZHNxOGVoRXVYek5yY0UxZ0wxelpTZmYyMlRPTVRpcHJMdWtneW5NcTk2bDlEN2h1d296UW9RUlNJSlRhdDVwU1J4M1JWcHVrWWVqRm04d2wiLCJtYWMiOiJiZDRhYzU0MDAwNGQ5NGUyMjZiNGJkMjZkYzAyNjZhMGNjMWY1OTk5ODAxNjVlZjQ1ZTIyZDBmYTVkMTIzZTRjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "WmqD1AQoqzcjRpv9c_RKQYVhl7s1ZJbPIKYjoarPHEE-1791929464-1.2.1.1-amQ4nqq_kYs_f_cZN1S5op1ze3q7gAXuXOs8F3YSgTDEVQuIGLJG.sWtAYDzQGpm.BPdvfxRfTleTs2qAW5BG5P2Wb63u5pzdMYsNCl77wDJQUJyn6VBHZK7gpfxQ2Q8Q7K7pX3p1.ZtD77qMKboAueoYD50s8gKIzc9Zmkut1.jQhHOom_6iLuUtGM2YbAv.xosCfG0oZp.gQ88o33qtIDYJ.DiVHswCTk_L6m1QMMu.G0PUVqaLi3MeUWjqj.75F26cHCmiW6WihBAIrsllyPlb0Qt3md7kx0SCbuPmJGqSlecoOeU.NLlct6ycPrdB31C4NHHC7feTVUL8wt0CB3pBR9cxGYaTWsap5NUxqNSop6PwM1jRJX2a_QgYLIp1Qj7HFdNbl2_bQJH_ya59VALS.WzlRxctnyE4vodWyp_w3mBypMmHQ9yCnNAKjqjq6HT67YmCAJpHSxBgs57keALB5UQMOQWtRIwWUwqG4n76oT1UPMml4QrwBsi3ztzZhSMTVVCY6ypBffS1ItLNw",
    "XSRF-TOKEN": "eyJpdiI6IlJ0amU4YVp5VFNPV1hYTEZYU3Qvenc9PSIsInZhbHVlIjoidXl4VTBUQWxlNFd0WitDUjZmNytCRzVsZ1YvYUpkckRVT0x1TFVYZ3UvS2dnL3VHbHRxMmZrVEZFR1Z0dHBlWnBIaCsybktIVzZ4T1JpUC9rM1Y2aVdsY3ZXY2hOSGFHR2xDK0NRU1VlSDcvWXl1U2FXMEZ5ME5iTWZ0and0Zk0iLCJtYWMiOiI4YmJhZWM1YmJkYjE1MTk3YTc2Nzc4MzMzYmY5ZWUxMWYzMWIyMzM0Mzc4YWUzODMxNmEwMDM2NzZmYjY0M2E1IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkdoWGFZYklHaFpLbnlkRmpLenFpNFE9PSIsInZhbHVlIjoiUlYyY1NpSzRLanFTSW1ua2dRYm9CenNHdkE4blFpcG5YSmhPQVdtelBTV3AyMVZjMG5DYkFpdXNBMUF3bU55LzVJUGp4YXBaNlNEWHcrbkFSU3lmOEtWN0RiRWQwUS9Xb2NFakgrTFhqZEdYbm1VRzI1cVdkVFR4NXVHWjlMaFEiLCJtYWMiOiI0OGU3ZWRkMzEyYTU5NzljNmMxNDY3ZmRhODIzNTk5MWE3MDA2OGY5MWNmMTk0NjUzZGNjMzc2NWY1MDkzNzM3IiwidGFnIjoiIn0%3D",
}

