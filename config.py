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
    "cf_clearance": "6jPULmWtpJdoh4Rj4O9pZeVIdQsdrnEUyA1cEzePfcE-1791890951-1.2.1.1-N5.PizMA97EcAvHnfrSdayhDHQNec5fd0TMUtGlQSafCr2vij57fa.lgh.juLNWUOsa63JWvpKGB.42wbGoP_quvdP._BbyT4FNCIpzAw0NZQlog01JtebxTqCuM7AL5Oc9aodDDODN8WUzDYnsyAtN12HT1mRCfxR0EFxGJSchYlt6Wan1dEXNyZWg45ZkCGFRtqdzI2s_u5anRFCont5BSAX9AevHwrQzMN3nZtz7sutvf2Lwrwe0X3gHPCYG7qhc6zfAO72PKBQyBowSgl9nmo1ludyTYQAHp3knnNpPMJhwJn523oM5h8TxNOrCov9aXzoQ4j2CYL01vl.tAxzgAGhgreLRTVPvPkIFwZv6id7AqIY36IMEHPuLAnMv8Ytb8.Vq3yHyr8dPF3uNho7Nn8BhTHyEmPL9Wb_voDyLJ820QcIDDv.F0_d9K8L6XLpjqXMqbp75qyDVa9P6xcEbT0ws_.gag8bQUdy8BwR5Ww9THeTmZkKLCgLhVjmnUiD8BjcUN2VyOyxPTVfoPxw",
    "XSRF-TOKEN": "eyJpdiI6ImVuQksxUHdPNkNPV05xWkpkbDBBY1E9PSIsInZhbHVlIjoiL2twNXNWdHNjM0JGMnBGbmhuL0xrNUhNQTVCVUdxZnlzYnNsVmRIL0hKcFhBM05CanJmWlF0ZDIvMk9uRTdOUjNvUy9ZSnpSeXd0dDBpRXZuWnlkN0o3Q2h3Rk9lS1EvZVM1bXdUc2twMlNjUzFxc24wZTZWQis5NDFmTEZjczgiLCJtYWMiOiI0YzdmYzBlN2NhZDQ2YTRkOWI3OWVmNDY5NjE2NWRlZmNhY2NlOWE3NjgwN2Y5ZTVhOTM5YWQ0YTY4NTdjMzVmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjJwZUF5TGoraW5pWmdyYytQUWRGVEE9PSIsInZhbHVlIjoiOURvaVVhTXpnRURISElEU2NSZlI5Z2JDUlJseStjVUZvLytuNzI2MmxMTmhqSTNEa2tZNklQVlJtNDlBSStyWFZYMzhjNS8wb0VzdUQyMUloQ3haTzc4bG1NN0VmZzRiUEdzdmJqbVFvS0tDUkdnT0Z4eVpnb0ljeXNRNG5TM2MiLCJtYWMiOiI3MWE0YTY1NmU2YmFhODAzNTUxZjcyYTJhYTU5MTU3MmU2Yjk2ZGQ0ZWFiNmFkNzZiNjIwZmM4MjdlYjdjZTYyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "CJEZED41xnxE55huz_9j_SvQlIpY4YY0kLnypu8mRYc-1791892133-1.2.1.1-r7yr7wBnmRLx1XlL1OU6lZHqx3.4Q2l4o_Hl1QyviX1hXiQ1DRuBvUe52SHalAkSdlVJcty7uCRXHjQuqIttMyYzdMUSUsca3nvgS9SQYh6mR2YBFc0hmoqRF1OhBFekubE0ShpeHCsZMZaewd4HJ28mw4PZrQTqhzkVxujqJW1ieN_Yuhp6idSvaQGmq_0.1bOICy1XIrpmRRCLYQQgO5TSaHY7Po.TJL0Otg1u0MG4Fv78IB856sXUpLZqLIoJT_Yx6_Ez0Y8DkeTOVnLoviayhFy1KY0fjRg6cz3pjsR1Tkn6AnuAkBufBZhMns81MEUSPUZk7XDoc1m4j0zKQ9xf2Lmsp.pRORXLB3ETj6C4vfL5ubXVtsNAcUXY.P5EKR3g5isMC9IUFw83ncDN7.QaJUhQJMobhquJSImg8tl5EpzsEYIS94aY3sVh0JMgB.DczpO9UPOmlIp0OnUtMQSXV8LM6g4UxGL8PHfjotf9qqnfNRJydx7j9JlydsZ5wLVNyh8db2yqkXyegTGwsQ",
    "XSRF-TOKEN": "eyJpdiI6Ik1rZEg2RmxUd1JveHoxa2xBQ2hHdFE9PSIsInZhbHVlIjoiR3ZwUnZWa052RFkxT2E0WnBzRndieTZyMS83UkxOeVovY254dk9XTnlIWDBlWEdSN3I5ZWhIc0Yzei9naE41WDhka1ovSUY1Q3VIUVJVSitpU3daWEw4bElHKzdqODZNZ2VacEtkMVFQYVBZS0JPTE1BLzBPbU9zY2F1c2FXT00iLCJtYWMiOiJlOWIxNjhlZTU1OTJiZmI5ODNmYmI2ODFiNjE2MGUyYTE4OWI2YmZmN2UxZDYwYjRjZWM5YThhNjI4OWVhNjE4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InZ1Z0JCaXNKWEE5bmg1ZGRGeGcraUE9PSIsInZhbHVlIjoiQ203NEE3TEJSanNNMzBDWG84cFRKSFlNM3pjclpoOU1LVUJTQm13NktUaWVjWE8ra3dNSTZxZkx0U2tpZG9sdDUzbTl2Z0x1dWFDK1dVUnRaTFB1WWFYcHBzTVAvMFlJaTczNFcxZCtNYWFjTzA4TDhTU0tPNXBsOXNDaUhhY0wiLCJtYWMiOiIyODVmZDlmM2EzOTBmYWVkZTFiZDdmOGYyOTkyZTExNTljNzkxOGQzYjYyYTVlMmY2YWFlYThmOTgwMWZhZTVhIiwidGFnIjoiIn0%3D",
}

