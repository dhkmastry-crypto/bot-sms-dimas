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
    "cf_clearance": "x9rPemld57jb3LIgfr9i72wqmITzNxXnZqxgsowybJk-1791842119-1.2.1.1-wIUYYdS0H1uAx9l2HF1YJGYzLUzeks7WaKKsRkNLStHG8YmPYIEVtvdd.VgVIEgJPLMY.DEP7YvGskkD8v5hk2QZvPLxuqZN5ACGMaLzq4NAZdwb.IZXUF.eBwBz78nAaw0RpvJzCT16I0yCAApEPn18SHOLCXJ7.mKfSc.cI0rEniLTUAic8CaykfYxdxgN35t1rFnQkJz.MgPzJ7MR2WZNf9MIcmliwKRnxHSbDDK1LEMbUMlvAX91FQZTbJDs5au86VEtm9_IX0JgpkvyV1i08YsJrD7PtWPHbagaKRO2OmVm7ZfVMbh_ZU2FZb8LcgypoOBAntTLGRHFK_g.os7CqNHmz7JJ.E_wTUf2rP40XgBXb_UH0_R5bFilSkh3LU0lsfJDmQ4N5vLLta0UGCubjlD7hgsHDIgvkbuV6JehbUongNV.Cc8tnkthM2Rz3EwLS7cUDzdVY8E1oQfGRYA2zqbqbfHEaEf_ZirdhCjLW4y611NVFv_8Vgx.iPUMQz1ckBNdHqJFLTeX.nl8QQ",
    "XSRF-TOKEN": "eyJpdiI6IldkakRGNkErczgxU1h1bU5Xb1BGamc9PSIsInZhbHVlIjoiOTVDSWNpQU5sWUlUYWNDL0gwenYyT3JCVkpkRW94YXVIbVd5OEdBUUxleEp3M0NyM0FLeG95MzQyR3ZZRmhmaVh6SUtxOW1NVEJLaHR6aTZwSlR0b0g2MHMydExOb0s2L1BodWxjTndSQ3NTbG00dWQxSkFvV1VoMExqTVdkcDUiLCJtYWMiOiI4OTFlMjUwYTQyYTYyMTVmMDQ3ODM1YWE2YThmODQ4ODc1MDU1NzkxMDQ5NzgzMTZhMTA5NzA3Mzg4NGQ0OGEzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjhuS29MME5GdThQVkFydU1FVVQycEE9PSIsInZhbHVlIjoieTJ1N2FvZjlLV25WVTFUeUFMeGgxTVRlVDZYRWlpQS8yRmZ5TjVSUnBpMUpSZGV3RTljUnNqZkppZXhmdm5iZklCR3VPY1BERjQ0M2k0ak5ldDdGekg1UVBnWi93TGhoSGxVa1FESWprdnRZK3pBazdLWUZ3Y3FHMDJrZktxd1oiLCJtYWMiOiI2YTFlZmEzNjkyNzE5ZTNlYmRmNjEyZWRlOWY0NTcwY2NlNjllZGUxODU4ZGE0YWZhNWNlNjk3ZmZmNDA2OTFlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "HF6EaIiStFe5zUW9gfkf9nnmSf54NQY9Puuxl6lxqQI-1791841285-1.2.1.1-2b4I4Zk2l0qffOLslLLDqZhVGdEW_Lw7zt0PwlhtNOkJEbr7GB75aFQAH85PJF_6oMb3mktMCyGGtwY4KPUMhEodmXlJAdTGxBRwy22CFxQl4jITfhkMOv70skPGhqrGVqz0QhGgLZ9THkbJJzFIs3wjyvWHeRmgZI2HVDLPzqdE6c3ecDw7T23T8AaLqDS_vO3ZmmwwSiE3HJZ9Fbu3hBijSwDcAG4N944hDWgRL1NZyrCAoMpRd6w0zyNqTIdLtDscYe2d0rxr..ops9sgWaglCfQR_yFvYLJBCoBdwgmziPrvXq0fe5Nj33nzVC7n_5gs8ubT_EGU10WQjND.Dg3iKeboOzZak3eAB41ddP3sZwvgP8R7._3XGNt3ASnC3TfOG_DyBG9FIi_NP8.wIb0q11MGSXIXxI34FL7rExh49Q1Rmcmkf7l9QTnuwD2jN9hbztoWkPnCZEpHdzN2HphHQPfqsjG1WA9OYPRtXzS8EPrS3EkZlsBmgvu.C_IEr5B5RCByhv2I_S2TuXT2Bg",
    "XSRF-TOKEN": "eyJpdiI6Imh2aDNFV1lZMFBrTFpxTytKWThsQWc9PSIsInZhbHVlIjoiQ2crSmFDamg5Z1d1N0V0NGpiVTltWDM4VDk0MXVrUUorbXI5UW9jQ1ZneHk1d3lPT3pWampPYm1OMllId3U1b2ZkM3VjK2Mxb2hQZnNyU2lkZkRnMngzNWZJOXl6bjdTWHFQWmhVdjl6N0FZZ3lwQzBzTS9aNEtjMzVGaVd1am4iLCJtYWMiOiJlOGRjOTg3MzJmOTEyNWY4ZTVlODI5YTcyZjMxYjM5ODFlZmE1YjdhNjU2Y2YzYTllYTA3ZDY4MzgxODM5NTUxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InlMcDJZdUVxazZLeDRZck9lOUlya2c9PSIsInZhbHVlIjoibWNOQWd1OW1zQVBDVEY2Z014alJzTnlqNkI5dkZJZUVWUHpvaHc3eDVWNnBYK1FTMXdQTm43cldOd2xaRjN2RFFBdmlKUGdWWUlvWnZ6UTAwYnQ3N2xkQmxIY1B3bEY0Vk1nM2o1My9PY3NWOE1Wa2N5Yy80OTc3anNwdm42dHYiLCJtYWMiOiI0NzUxOGVjMWNjZTc4OGMzZGM5Y2MxMjVhYWNiZmZiNzFjZjI5ZTE4MGY2MzA0OWY3ODUxNzk3MzVjOTE3ZTIxIiwidGFnIjoiIn0%3D",
}

