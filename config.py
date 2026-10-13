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
    "cf_clearance": "9jhYsJyONM7Qm3JH48OTLyjlTY8hR3uXub8wEhsAQ.o-1791858392-1.2.1.1-ptBXMEwEjnIWcRjOwBGZXtykDCJ_Iec193BsQ5fT7kTM7SAJIgupMF0MZYfG1FfDg8UEE60V3LwecYgdp8UALd9C5fiQjgnQn8gPMJyBwcVcFS2lxy2djjVUN7xPSa4cxNMBxk_Dgt69xp.MA1ByjKwbPv3MDLJ2_Po.rljIUb5sWesUw5c4fUhuslj8pjpQNOQUCzPcL2JqFA6NR1mRvUKSznvr4KH4OESwI91NYVk.O397.qRbtNAht9TUW1k3EukEkY6xlTncttiaAIx7drSeq8XbO6CAyMdrg9Clkj8wSh5c0ngI.CX9SLp0W_RP1vAkZPlY2g5cWg.glfJFoVXwCk4U0W80lqv4ByaXePB.eS2o6wjyALA7z0vYgTYW8TgPnYX1zbSproIWO4URoYrrPIJsnyFVmpOZUpU37bivcbbdoFPKmXZ6pgWCAqYRCBAuILYjCH6VvbWQZRvBDUcQ5IouFTFqkWVUAdp0j3KDnkEbvdCJqhNXu9fxkKfA6Nhl3SlDUJc9FanBWeszdA",
    "XSRF-TOKEN": "eyJpdiI6IlN0WjlrSVVBNHpQamk3SjFBTVpLNXc9PSIsInZhbHVlIjoiK21NM1hlUkNiZ0o2Ty9mS21ZaUJ4THM3TTZYYk9yMnA5N0VRM0VNeFRRK2RyQnlucHdKQWF5YVJkTGEwUmlkM1B3RWNLckdGY2pRUEpMd3dUSWNLYk1lZDZKa0NHMGx1Y2xoOHR0cStIQXo5OTlGZmlrTkM0SGxhalNFdVdZa0giLCJtYWMiOiIzYmZlZjE5ZjEyOWRjZjhkNmE4NTA5NjA3NDg0YmE1YzRmNGE5YWIxNWYwNGViZmY5N2E5OTZhYTdkZjQwOWE5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjR1T0xQakg4R3ZMUGJtWXZrQk85T1E9PSIsInZhbHVlIjoiQllSODFsVzg0U1Y3NjgxUUNSNUFTM0hHR1haTnRibUZ3VFlXNUxXS3RyMkFTT29GWHNzMVpoT3VlcWx4dUpKbXVYZkxRc1gyV3RJTloybGFSVERIRkswS0RXZWQ3VVJtVVNlcVZxQ3dZeUdyVVFibFZXRjk1ODhwY3Fta0I5bTgiLCJtYWMiOiI1YmE2NTYzNTM3YzdmYzMyNWVjNjY5Y2Y3OTJhYzE2ZTAyMWE2OTAxMzAyNmRhZWM1ZTc3YmE1ZjYzZjM2ZjhjIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "Mdt6PeAwuiD6cNwx7_msKFyi3qsKumk7oquGGfTYhKs-1791857762-1.2.1.1-9bowht3mLn2ctb7s40YMIRhggYnZzKDZXAJCyCBXXQMZun3AxV2fpNGYTA5thLWjzRMka4kG42Fz3iBdh3fVPGcRvTbaY_PU1x_.NANDDnUoKC0.snl3XOJiRHoIw5X2b2YbZ2oFwqRv_8HwPipnwpRexgEYXfu2GgeqgfvLzVEU8VQGvj.C8VGGm2HgLOYLhqkhIots0Dn78tiavHt93xHwzfojQybGBoNxdBg_iOUYupy6N6dLrZrFLhAuIgXt0puW3fxE29H71.GsyuGIQrXI3wsFoKDSqW1S_ZUvDc1SMcWqqZC1hfQSxd1nI.Xq77x0h3ak6hEC1ckL2IJ921IAjPXrsf.foIPt.jvLzdkRM.J3dpjKqMn.CrPt1QmoogUFu3wg9WFywWl7DTG7gBYBGn72aYykhKQbbYTR4edGV9_lKB0GPHkvzsgZmCvc8.3okql5Y2KU0cJWR8xWl7zsv3Kewz0ykWrsMBrnkL9WvLKmt16WkuNO.MKi_5E1HJQP_PLmwEKE1FfSyODTuw",
    "XSRF-TOKEN": "eyJpdiI6IjlyZE9RQWdUVlR2c0wwU0tIR1UvMHc9PSIsInZhbHVlIjoiZlNSOUV0aW5tWGp5NEdNd3VLUlNiMUhoUWxMb1J5OXlnQnNtTlQ0eXRRdk15ZTVNdTZJNTZ4Uy9iaE9STUFyRGN4TGNnektBV3cyR2I1Z2lRcktLYXRISmNIQ2pzeXZQSVZFU3o4Vk5uNFplUDRlM3FjM2xNVEdkMGRrOFpUam8iLCJtYWMiOiI2ZTdiZDBlMjEwZDczNDBiODJmOTMyMTZkNzU4N2VkZWQ0OWYyOWFmYTIxOTY2ZmIxODc4ZmRiMWI5YWRhN2MyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlJjV3Foa3ZpVlljSmlHT2prZS9WaFE9PSIsInZhbHVlIjoidUtYRWlJMk9KM1FFeUR2UDY4QUJTYVRNa0RGNnJJR3pIU0pUdFBHbUhWTlc5SE0wcEU4REtSdTdQQlRkTGplWXRkSjRqViszVnRuMDZOSGxhYk5BQ1dWOU5JVWVjVkNiOU1HaFZJdEMzdG5ObGR3VWE5M1pkN0MvV2o5RlM3L3QiLCJtYWMiOiJjNjVlNDM0ZDA3ZDVhMTNhMGU4ODJiYWUyN2I2M2QxNjM1YjliMjA0YzJjNjdmN2JlZmNhOGViYTZhYjg5NzRiIiwidGFnIjoiIn0%3D",
}

