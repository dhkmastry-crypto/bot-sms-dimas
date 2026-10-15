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
    "cf_clearance": "3KZsdhM.fuEDpLym9yh5nI0KDg.YGkVq39kLd8BDySA-1792035551-1.2.1.1-Ed_qWd.UL3kBJZRSgArARHK3JAyeUOZxYxrkgyeLEiYYMSQqdIRaGz80idkdHKYZVNqWuaVzK8Fb6Op0sRbvezGBAa4UkSZH7QFQilVwapt6TNOQ81RJfG50aGkM63gcPkSc4iqjfgaz3CFGb1GiPPsbGahoy14MpsVWJJYa3RqBgKPuS2K85RCFfJo5WXaomsgQJt0TQfHkGnK9OKOsTEHwTqevL3mFclrj_7R4Z2R59xdLDVszvR7ZTP6GmGGrw4FepRoZ4gjLmEt.7Pgar4CK.AjUKM8vNZhefh6Fhx9a0jf0E0npZUDVweYgOM4Fzgsmfv3MUO_Y7xXey9zk7g60MsfDSpE.jzV.AmHjTcp6OG2mybgj0PzqByNXEV47t4Oi3qSs9uORr_n5ul3zp71S0KjBo7dBzEY2WTTQbCNI567AxCHNl0LiJ7_ioDtsaIojB.yZRs.8D4wR9mg4HYWDw_Iwwhn0atRSu_9R8Sary7dCVR9KvdtwRJjSGlo8WM38ldL5kQWKBmEkiMmf7w",
    "XSRF-TOKEN": "eyJpdiI6IjVCSUtPTnBJSkFCSkZ6cmNoVldGaFE9PSIsInZhbHVlIjoiMVJaZWo0UXlubldKQk9nWnBxNElxRjlKZGxCd0xQZmNXMGJNdjdOSlFTcS9CblV5b1laaWVBTFp6VU5yaDZjMzR1Vi9zUmFMMVhYZktFdFVsaHRNc3ZSQXVpV0owaXF2MnhuMWo3NVUxTnpSNFZwbVZTbVppV1ZBU3FhRVdKRmEiLCJtYWMiOiJhYmUzNzUwZWRiZTBkNzc1OTE1NzRiMzc1NzM5NjRiMmE0YTNhZWJhMTBlMzc5MmVlYjMyYmI2MDQ3YjI1Mjk4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik94WlhQTDhSZEluZUp5enlQSUIxNnc9PSIsInZhbHVlIjoiYlNDcHB5cjBsL1pacFJTY2hxbHZOb2NXZTBDWG9VNkxtL0NYL2I0Vk0ybmpBdWpPMWltZ0JkcTJQMEZCQytRRG1lQThQdVN0VXZUc2Z2VzlEUkV1MnUyVHBDNmlQaFJvWjBkUjBwUGhwcEpBRGx6KytvN0dKUmZRV2F3c2VkRXEiLCJtYWMiOiJhMDJjZDIxMjE4ZDUwM2Y2NTE1MWUxYWUwYmJhMWIyOTFhM2JmZjQ2NmI1ZTE3ZGRiMTRlMzc2NWIxYmRmNjdlIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "hCUj5nwR1I8KZi9BXD9ypSFKwC7iFU.yVNa1egp0kd8-1792035542-1.2.1.1-7zWFDat8fDLAv8Cv9JXgwFBDyRVkBp1fNBICEHVPSA4TA7aws7wf0USWLA91ZxRBiWzMFmi5gmKloqOn8DOLN4wNvGAGOxVI5lXyyyJUwoNZVtNQBI1C5Mc.WgV3SMyXz1ELnzTKFb_rOM2_UkGHLBHBV5uqpnRlGkAuWNScWVCmAklilaMKYF2oadYrBz3qCsaAwWwl_6huAVOs8ZJrMAWO9OokZTmeSNrn7jakydYaSFQ10gsc2DwWHazC0pyLNOFRYl1xykxm2J6YqK5mZRaE3RnpO.VeZC6V9m06uZnhHDME_VBS4sU6iQTALqGk2WrdubkltFX2lUOESZLpHupt8uhbAnQW4D6jke1pZdDju5uokGHAd1X1Cy6gOjvsEati5A28v0l9RoXbxzQjDkbKzc0.8QK_vMahiEd8xl2UNIRB8v11NkwkZpseeeoB8LqL9noWLGgY20TFY_lzWp1_ZzGtPHDNBVVz3qyNkKVRqyCNT94hOGdGdAG17o7Y2SgRIHx63kbOcNXVyiccAg",
    "XSRF-TOKEN": "eyJpdiI6InRjMDVTTU80RDQ5aVA4RTMwanV5QkE9PSIsInZhbHVlIjoiUzRHektTZlh3c25RQVY5bXdqcUtpVjh4NXZKdzJYeVdReDhCVjVJZVRtU3B1Wkc3Y1RaUkVJd2FpRGl6dCtFb1I5dFJSd1ZOcXA4c2dUSGZWa1N3cmdYd1BqSkQ5VU9qeWFtNVc1K3dIR1F3bWZjQjIxTGtzVGV1NFgzeWtZMmIiLCJtYWMiOiI0ZTgxYjkwMWIwYzkwYmI2MGE4Yjk2Y2FhNzE0NjExZTY3YzhlNGFkMTJkYWRjMTkyOTI0MDkzODVjMDYyOThlIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImpNRGFUSkx3N1l5SzVKTEdPRXpCQ3c9PSIsInZhbHVlIjoiV1VYVjRoWlBhandsM2ZLSkNLMHFkbWx2akhLUktqRThXNVE1ZkM5SitNazkwczhPUktUbXo4dWhvdkpQM3h2SkRhUE52RmlqVjdUM21Ycm1NdWRVdzRHUE1saWdTbzlGNUpwS3pJVjc0RnVsd0NWY1pZQkhONWdFQkRmUis2TEEiLCJtYWMiOiI2NjM2YTNhMjA1ZTYzNjAxMDQwMWVjZDMwYTA4ZTQ5ZGIxMGQxZTY1ZWE2MjY2MjBjYjRhMzY4ODg4NWQ0ZTQxIiwidGFnIjoiIn0%3D",
}

