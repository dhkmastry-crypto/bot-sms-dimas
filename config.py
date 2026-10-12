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
    "cf_clearance": "OngsWMoayXcSAE2gJQUU1yJtAA5ma_DXO0ks5iWu4G0-1791843150-1.2.1.1-fXuYvEcd5ZX8qoC0qhuN.voN0v3JOsqFCgr7fSvUqXam6Tz2Yuvwtu7luTIsSyZPK_6q9O.jAdUXuUpveE9nwPbv5vclXuWGtHe2VccEgBbwDtDz8oJUE51ZRt4CYZpa3On3YK9naQPE4NyKi7c0mv6AObZ7UWO1amKmduK2yik4DDtr8VxGXIYPlL6HFXKMb27WGuAZyZ9XFd7r78Vn6dwaXPT.TE06wbfwcYUYLtUVj5V5t8XmwWLOmZS11UKU.6Yvhn7HgV4zp7s0jd0pt7ZPq2uGMjPCZYcB_4CL1CtX9IZGxva55LlORsQETyviLeyiDFSSVHg15ll8U.GUD28IMklST1MylvD751obNQNdlVwWaC4dNL7wg8eF5qSKQjPSGoGUI0ot6Mqzvh4UXVPsB__BmWHrGhpiaBbkz3DcDWQp5hekMpjdD0.tC.qqMbT1cf1ow2GwyfwfllaQZbrKY6CBSO545WJGmwGrjKMRWWRoRIqJU6HIHV.91A5NV2.6LnZp6G9Dn8G0T_DnUw",
    "XSRF-TOKEN": "eyJpdiI6IkVta0pZZGxOUUl5WW9kaDV0SGVLTFE9PSIsInZhbHVlIjoiYmZVRHBpZkFnNnluNWFDbDZmQmFrTzE0ek14ZFM2NDdnZDAydCtrZVRhZ29qTHpDWXhFSW8yTmNQd0xUQW9LV2czOGhKdlJzVFJVUTRoT3ZERWdxZHFiUk1lZllSTHhaYzgxUW90eTlwcnJneEdjaHl4WkZrRXdyQzIvMGNheEUiLCJtYWMiOiJkN2EyMzMyYjNmMThjNTQ3ZDRhODJlM2I3YmU1ZmY2MDMwMDUzN2FkNjA3N2U2MDQ0ODJkM2JiMmViZWFkNWI5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im1xbWRHU1k2SktPMFdxTTdJakdNUkE9PSIsInZhbHVlIjoiS2ViQ2dxamhaZUpBQ2RIMzVmdXpJUDFsQ0F3MW1aM1o1RFEvaDlGUzg2U0VJcjMweVV4SDVhbytORFZsL3pSRUMyUmJFMjZrbm1lR3BIV2VnK3BSaHhRditkRDdIWTFNTDU5ZzNZaE05TDFUQVdLdncyTHNwK2RmSWZRc3lpakUiLCJtYWMiOiJlNjA5ZGY3OTU2Y2RiZGEzMDVhMzZlZjhhYjhmMmJhMmFkMzkxYjUxZmZmOWNlNzBiYmFmZWYzMDM3MjEwNTU1IiwidGFnIjoiIn0%3D",
}

