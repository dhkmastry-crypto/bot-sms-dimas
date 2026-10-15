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
    "cf_clearance": "_Gep77.lxjdfyEQANvN_ENWRSNi.cO.oaXsLwDIU30Q-1792047468-1.2.1.1-37Zcw.O5iipIUXGhmDPp82lS_bCmJP1a1ASqsUkzB9.kf_P53v.Glpz93xdiWYLWmJW9IWFyZaMiePY1O.X6ZORekO3T_XybUL2kVoxMCaO9FnOVa09MrvpP6cfeiY3lnkXbYJSAQY375kDmSXGfPJZvsDLXZM7lcqjevE2LJupvPwhwYAyp2zFit67w5q6tpxtZUL4vPXYQj5uyDT74kcL9PBXTxF6il4q5XvShtuWCGbEht5IU5mcmTTW0V2vefP.DVqQ06G_QUByJG7z3qZneuOxPR.lBASXDRLuqk4P7Qdg_IoqlxNkckBAME6uLxAzHudxTqKM8oyrEHFee0mggO1ban1dpTR7Zthnu2kRb62WmIiq4TIHSGOTKQM.my9orbzXdiKXXEQiCZFNBiP2dXqB1qCquG_3aqleqn1arHcnzsbfA8BHHCEQalwwQ1KhSHCSuj7KoKSbStb9zJ7zLD3P8sQCEPgNfSb08rz31iTW01TpDfcyjKTejFyMJDT52PNJq7ea3iE4Q0R1mGQ",
    "XSRF-TOKEN": "eyJpdiI6ImZZdHNSRFdZV1NwZVJtY1dHbzBXa3c9PSIsInZhbHVlIjoiWlR1dlh5eWN2Q2liQ2VENHhwV3FXM0FHaUQyV1hJRHN4SDVWbjRlVld6OUZSOHhTaDhOUWVLSUZuN2N4aGJRcmRvMlpiOElMbWxpOElPbmJXVVBjQUI4ZUtES3hMS0V5cmVWaHdSQy9ST29NVFJNYjZtYXUweklXZFNLTnRhMkciLCJtYWMiOiJhNjRjYzhlNThmODk1MGIyZDg0NzdjNGM1NmFkNDAzMTg0YWYyZTcyZTdjOTM4ODE5NmQ2YzU0ODQwYjMyOGE3IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlFLdWRGbithZ1JlNldrQXEvaGplTGc9PSIsInZhbHVlIjoidnJJMzUrK0VuY1VXN2NnWXIzMkhRYkdhUXpXMVJPMDJTM0VYUy9nMWQ1QTdNWkV0M0pNN3ZRYWNvclMrZFhkNUtVRG9PbytvRU9yTjJnVVNNbXRudldHQVdqakJucWp3Nm1FVWZ1RmZQUkpmS2VJUFlFdmJqMWxDRW5zQ2JmVlMiLCJtYWMiOiJlNGM0ZTY4NTI2MzE1NThjMjYwNWJkZDhkMjZlNzdmM2RkYThmNWQ3Yzc2MzExNjljODhkNzVkYjk2MDQ4MjRmIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "8K_l_RDgKqgYoq5_DRh8K1tcKBTwoVQiFu53_hpUvts-1792049230-1.2.1.1-TOD34Z9fjO9G3.3VWibVFl7iVXvsa.9GJsxsG7OrQl8Mvlie5R1afLSK.3jylx.DeaBWCrH2RyvIwlXNKzGpeuojTpd.ibFyQ4I8nwzfxxwmoqA_9nxteZ1BjORSDFnNMPKRfPPDZ17ZUbfz3y7.mN69sH25aU3y3HrFls7c0ekic7pWrxSykHPQjvWEUdjPkqIrGMYazHN2cIZthG2cidxFHHGz2.hiqX4NSkrE95UDaFllkh6yvtwNgT34POh206IkFjOPQ9FPc1GduyqCZhE4rNJQGgxBZW4VCaesjgh.XLEtj5abZjzCv.bi7p.C9DwUmCP1MdsvfSSYknVQM.WjRkj.bsgnwNao32.D6mAyrrNSKQmRKUaF.Qr_vIu9To6XvASm2Z3WFzWvs0pFO1pJxzAwHnK4cMwb0Q.Hwz4IEF7XF9HACoXTPabwCDsaK9aRGuU69DHlvAdW4Gh7zPou2bFNzGBm5UlcwRUtgbbPWDl3TAKwMW4X6NVs15ukilJ7D5t93w9xQUZDEMv96Q",
    "XSRF-TOKEN": "eyJpdiI6IkRjc1ZleVZ4NmV6SEYvVVVLS1BmSkE9PSIsInZhbHVlIjoiOEhVT1FjVHQ4SkRZVU5pS2RFVW93M2psamQvT09kWWNtdHdTT3pUQmR3Y0l4SWg0alZyeGVLZEdrVXZBbGd0UlZFNlVDaTJDVGZlNlcyQUdsczgzcHM3Uzl3SC8xY0NKd0YvWmtMUldVM3hrcHZSVjUvVU5PQTdoZTB1Vk83bmciLCJtYWMiOiIwMDRlZTdhOWI1ZGIzZjVkOGNiYmUzOTRjMTdjYjE2ZDNkZmEyMGEwYTUyMjIwMDQ2NTRkYzQ4Y2VjNzBkZTViIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik9qVFB1Rlc4eHNScVdSbnkrcmVwK3c9PSIsInZhbHVlIjoiOFJNTVA0VmZSdVpGT1QyM2xGSXhQMDlBR0g0ZDNFcFlVSWFpMWZ1UG1BL1lvVlo0K0hsWnNZTzIxazRqbjQ2d1NqTjB3Q0xmRnRxSkk4Q0xCOER3ZU9hamtodW9wNDdkb1JCd2dUeWl5Qm4vcDBHVXFFM08xeFE3OVBzUDVIenMiLCJtYWMiOiIxNTFlMTFlN2I2NDIxY2QwYzNiNjUyMTBmMDc4NDNjZTE5MzU5MGJhY2IyZmMzNjYzMTVhZTVlMDRkYWY4NjIyIiwidGFnIjoiIn0%3D",
}

