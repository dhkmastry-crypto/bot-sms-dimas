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
    "cf_clearance": "hEPveNB5ijXLWqB_xs57w9wUYbiWtJZUL5.p0B5k7.U-1791936712-1.2.1.1-K2rxsrBdSkpsaxZgzT3xy_ru3Ec9D10WwhFAGAaB8_bdPpq7_Vkmg1Wz7ovI8lgLGmYUL65qJLYK3sR2lgWIWtcA.icPJV83e_VlDgLI8dWgPw6dVSNkg.IYya2CngnaD4PMzFV0huj_oAukT16Bl42K_7UF9Sjukr28RcAG9Vl0vRIw0cuECF_90DKSjAsSXCNHSKz3SbxnbxUgB5QIPhw3TuTyQT.TS3rxwQmz5ZN3nRhHpL4oKt0xEf43AJkDw0vkfYUVvvB9UvMLcxez2PnNchbA7NsxH4b8nnB4Lh5HQ6SGkcCpF2ckgXA.sFcIBHOD54LA4sqLFOf2ziUtaRkJrotGNoD1U5aopqtLX2IRJmPlIX9jRsSIN1VHHrqxKWZnct9s62v4vOQjtHcj7c1HMa58WESIs8K_ZZb4pK92NDpcY3bo5ghEjuEe4ALgi6iyqPKFQfEnPjVl9VCCv7CWF5ZMKhhyOSMOHUC14qgdbils4RsUMs3DIlJq4e.ltPtyRfHxFWDRXDtrY7JPOQ",
    "XSRF-TOKEN": "eyJpdiI6InUremZJZ3d3Zldpckg4QVFmRFAvRFE9PSIsInZhbHVlIjoiaHp4TTFVR20wbVQ3NnY5NGlvcTgrVUJ4VmhWMlNoK3lFeXJ0ZzRoS1pZaUVWTllQb1FaTmlKTlI2UVEwTE52cGFBNnF6b1hEUWF4RTVzWm9sQWJuc3VKbXovNXZhTGE2bHh6WURLVm5nMGRZNzFaaGtMNFNHT3hWME9HWFdpbnYiLCJtYWMiOiJiZWE1ODQ2ZGFjOGQ1OTZlMjJlNjllYzhmZTZmMzRjZTMxZWZhYjE5OWI5NGNkMjZjZjJjYTM2YzAwNWY4MTUzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InNEWHQxTmk2ZHVSVTd4NThaZ3lvcnc9PSIsInZhbHVlIjoiMWJPQ3hIaTRPcnduU0Q0aVFqNngzMlFIUkpQZUFGOERMdVNIbWpUV010cytpanlieDlaL1VWRjQ1c0FTQlRSVHhrc0VWRVJSSHI1Nk5HVzVvNmU5bStndGEzUzdnRXN3dkMrbmRwSWpvYmRyUVM0ek9RNEVlK1hyS1gwSnN5a1AiLCJtYWMiOiI5Yzc0ZTlkNzYwZDJlZTlhNTRlMGI0MTU2MmI5MzdkMzU4ZjM3MDhmODkyOWRmNmZiOTBjYTI4MDNlYzZlMzQzIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "nOLG7vpWDse9ESCk7e0OeR7yLtnoofQmUNdmLobQazI-1791938508-1.2.1.1-IWZq6tTZuQelyRm2ZJgY2hZFsTE4F4H7aL62O2T3hN2TGfxgKBZOqXypAPOvWNslc..E.rfv.kEZjtL10zUOYGchbAN33APLyc46VbEkN2fk7b8LX.2LtpqIhBydZ6U4Gb64t5pMPZIEfPJo36z.uuEKVlRXIcdT1U_dxBW_S8FtQAtLcjY8bImQhnvu.C.yAuCvgFu_IMsJ8adNW_B1IWmi_WNF67IV8WBMyJVpiJ_sSZ7plqIytTIoSwY4ZsLQQ2CApJGv5k06s7q2_5m2XFbVbPUFJ8Aa7CpExnJVcElJyawROOmdU._OdVeymoTsHaT0S2fRMqo8tuvb7HjF2iz1jFRwAVKgaMFqmnDpT_YQWWdY9nexkuuvkfPB9sMbxAAeTnou8JZyN6eMwLqwQUBpi7iaFmkIOXg.ig6fsZTO3lbf96pt8lzkkRrXJdIoY6UqcvDj_bVKarQ92tEMaZUS.K66ImqjH63nT3ATcgvQn4amv7gLbEDEiEtWEpndxAoEeoqilz1nzBbtTADoAw",
    "XSRF-TOKEN": "eyJpdiI6InRJdHgyb3hTb1NVNVovMlg2d0RkRGc9PSIsInZhbHVlIjoieW82bVdhVEhJMzNxVThQS2phRS94QUZKdXNldnhqZUticmxDZFJIeWxoemZmMVIyUEd5ME9VYjlBaVRITm5NeWMwTjJDeGs0OXcxT3lMcWRSTmdlSTFNUmV5OXREcXYzQ1FadWp0Y1FGUHlXT3R0Rk1NRVZwTGNjQ2o2YXJ6Q24iLCJtYWMiOiJmNWMxYjZjZTYyZjg4ZGQwZmEyOWNlZWI5ZTgxMzFhN2NiNzg0ZDU1YWRlZjU0NzljYzM0ZWJjYzUxZDAyYmE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImN6cXRuVk5adHh3enRxck1YQTRZcVE9PSIsInZhbHVlIjoiVUVWbEtvY0MrNHdlVlBtS010Tk5INDUyWkZSQjRKZXpqendqMjlSalY5MU5qVmRXYlhHSzd1ZlcvelNyNDV5RXVBSHRKaENZaUh2YUNkWnZINm1QVUhxT3ZpRmtzVkxXdm5DS0FKbFo5NHgvNXJCOUlNQ0NjK3pUUEthK0VNUDYiLCJtYWMiOiI0MTdhNWQ2OWQ0NTg1ODE3MDA5OWUwMjgxMzhkMmMzMmVkZjkxMzU5NDA0YmMyZWU5ODgyZjcyMTNjMWRhZGE2IiwidGFnIjoiIn0%3D",
}

