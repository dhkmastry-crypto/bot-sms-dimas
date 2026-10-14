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
    "cf_clearance": "zCEkk7rayWaGXyrb7.vOrXavm_8vtvrGNT2UPnvc02M-1792017440-1.2.1.1-GAxTybDJ7Z7s81y27ko1PJTjx1HFVwJbe2Sd.f16RTnpf_lbXlCN5lQw2k7mGdynUxlktw61kHM3y8rFvfiIYWOsfi2ojQfTlgOBdJlmh.125GulW3x7.TUvKl5oV80XHOYtspIYaI1eVKFWP38zul43RU5o3RUDrCkM8TOPiWt8Ng_qVmcIFb5g5JwKjWcEb4gaW9ulxMfTIz9ubG7EhkMnK6Cjso2z6NwmAWV2sZr1fYH4EVQKq1KBJDhiNKmv7s5IfWS6fA2loPkz3J_xbucSImn5aK5NEjpg2DLr7vA6BE5zorUJNeI4DEFlc76j7iBb.j2snCapa730SgztH2UdgSTDMhlX2oSLuWrRx8TIBGk8SfDpJehdupAZL3FMj5x7CmYe2LOhHazHtNR51_FdlFgwxqrzdvpRCzfxh.uahi52XvNTEx2pT5PUfDpRfEfPvcJ8FALbjhiZ6GPkttFOuarxa6taXnxUi.ulTlhX1jUQR_xtvZ.zNiub3XgNwczVoy5O0D0D_hC1_mgZFg",
    "XSRF-TOKEN": "eyJpdiI6ImRMUGE5S2lWT3N3M3FMMXZlUVEwUmc9PSIsInZhbHVlIjoiREFwSGdxRTk4OTdEKzN5TkFFKzNqSGUxZWhIbzdCN2J3TEF2WUJqZ2tUd3FXSmg4R2o5bWR1cEQ2TWwzNDdyaGdLWEVsTnEwZUttQVJsL25xYVRwc3JHSzNrWjNicjBNQ2tFZjJFVnVBNzZQVGhLSkx4SFZlUFMya2ZXTVVxWVUiLCJtYWMiOiJkZmY3MzBlOGViM2ZjZjcxZTYzYjFmY2JiZWJhNDhmY2M4MmJkZjA3ZDlkZjBjYjIzNzNjMTc0OGMwNzMzOTg4IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im5DMmprWmlUbEk1b0w0NWs4T0RaS3c9PSIsInZhbHVlIjoiUHMzSEVLK2dSTDd1OHdmdytZenpTUDhObmUxVTZXYUNGSytKencyOGNiQUJKVzdKQWhWWlJNSDZmM3lJelBYLzloeHJUbmJhclhRNnI2LzkwZDdVOGtYM1VvZ1BkSzIxODl1U1JxVlBrWW1jMkNSNFJRZnIrR2t4dnhsU045S3QiLCJtYWMiOiIwYzQwMjM1MTAzNjA1OTRkZmY4ZjI0ZjQxYmE0MjE3NmFkMmFmMGI2NTZhZWFjZTM5NjIyNDJmNTFjMjBhZjU4IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "_upA8vNXt2hlhD04WkZ55bJFl7NvzhVGgnWSpvyQh_o-1792017420-1.2.1.1-n9y8Dr1H27BxEvtlXHm7XuRQVLS_TsTukDpOSyOi5MC664uplp_bUePBBpkmaxKIHuECXbCxuudVGBLbfMfMmzdKDa2vNdvbBCCygszFMGbxZHHTUtb20cj9DbNWFMi219vDEwwjhdr7yqdCLcwn8XdhpNhZfXdiQccBYSaUSDGifAftNWE0z4vI1j1L4rm_oW9wqI36lARRtYy3JtTKUS3p4sHPNQt8Onmz8Of6K4CGqBITOie2dezmtGAD7R5MhkbgsLCEqY_zHTbRFSWojpZT7gfRecCpUuYPcvqJPw0sRIrfl97pvpU8kXm5LiDkJ1LXYXKdgJI0.A5H2y5GcN7nofhQ3ssSXzjwSVBw2Ka9XvcOs0TBCYahUY3wuNxzl5PSYjSaDrJFHPgkZQL_5CdJbMMzAhyJbnA0U1WuPfZ6eWqG1Mn4fZAjM0QeUnTtjVRIbXHeyDOwHb2kHjTWW_ci1ZosmnzHAatCtFdpXu6oCLAnHPJOH2JN1nDpGDwbtEkcX6gqGmCRTDBKsyPjww",
    "XSRF-TOKEN": "eyJpdiI6IlZUKytObE5vR0pOV0dvS09zOHBzVHc9PSIsInZhbHVlIjoiTGdzOVduc2dETXhsc0JGRGZWRlZpclhtK1JVR0hIa0w5b3JiUkI4cWU4V2RGSE9TTHI1ckUzOGJnc2hicHdJRVlDektST0FkZUh0UHdCNXliRUU4bmNrSHJqMlZXbmsweitKT2xwK2N0eVEvL1Q0SzlVTExEUlFkK20wZTM4dDkiLCJtYWMiOiJjZGRkMGMyN2Q0ZWRkNWUwYzIwN2M0M2U4MzI5YzU5OWQ2OTliNjJmMzk0MTNkMzkxNjZjYTAwN2ExYzYwYjVhIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkViNnY3SDRRNEtGNHdnTzBsdGY2UGc9PSIsInZhbHVlIjoiNkgweG9jNmx3NXFoRGRwcllSUGU2R0lSdmNGMy90eW1zdEVFdytuQTUzbkM2eFpBUGtZeHdDQnpNYWhwZTcxdFZwenNjTTN6eGs1anFRU2k1VEV1STk2KzdFblhaVEYxbWw1VWl4Q0RKK1VDNDFkUVFRVDJINmFtRXkrVWNtNW8iLCJtYWMiOiIzZTNiYjcxYTRmYmQ0ZmU0MTE4OGMxODA3ZWU4NWU5ZmYzOTY1MTdlNzBhYzU4YWQwM2VkNTdlNGRjMmY0MTVhIiwidGFnIjoiIn0%3D",
}

