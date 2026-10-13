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
    "cf_clearance": "VzUc6bcAzPVLoo8MM8Bn4APJxD73Y0pBQAaYhadiVG0-1791925840-1.2.1.1-MFc4kGpUJaW6T8cGNuFBoQc2iAv2bqo9o.bMneeWAz3bsFBBkc51CBzV82a9Kj1gHWUqMmTZgIfIUoZFN9K6qceAwCAljsNuv97CiGQ1ViSD7xhg9WAcMWjfMWhhW8fE2yioWdgH3I69XS3lRuyLAZBDbhNoJ2bmGGe5dWH0G3fzmz0Bo4u.l.mGIXK.8CHlgwTiYDm.SI4SH9Ph6UlJSkyR25ec3Spjkshyz4crzGeoVf.nBhkvdyEJulBzxIv7FAWvqDcoXyGBkwY0UVAAFkxduxUN3h7schnruCMHR32Hd3SsMANmOHf99WSqDS715QDLYC636fJqhDxvY.JSl_idzIrRl7hznDMIx0lEly_4FViJgogCSOrxJ58.PrWNMOWbMzaY_O0k5lg13pzfBELHH7SFfD4mfEEbgddMqVZuKAZIeDVzEZjqc2ZiJeS89IF2E26OgIu.ueWjR7RT6ci0b0YaVTgCIDeEtO_HzYrImdtfb2YqEToaDdz08FLm1Uid88dfByk_l49CeGgafw",
    "XSRF-TOKEN": "eyJpdiI6IjNpSXRzZFRDSTRPblJ6aTNqSzJjenc9PSIsInZhbHVlIjoiMzRpRmJ0WW9IeVh3bFlqM21VL1hTbXRPMzg2b1ZPY2s2OXhIcWw0WTFZaXJkdjI4c2x6WThwVUl4Z3lnTlJhOHNwb29hQ1NmdUswSUdueWJDdExxV1ZOVkVVdzZGREYwYkN3bDJYWmZvdDJPVm1BTTZSNlRiczNNdTVOTk80OUsiLCJtYWMiOiI3MjUyNGNmYWVkNTgxZTAyZWVjYTc1MmM4NzZhMDc5ZTEwNjA3YTkwM2YxZGU1ZWE1MTg1MmE3YTk1NGMzYjk0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlR1NDNoT3ZCcG5KTFB4ZDcxOUVCL3c9PSIsInZhbHVlIjoiRjFDL2dCSjJEVGFUcTV0WGgwU090MUMzQ0lHRlQ5djRUalFBVWhOZ1J1aW1SWVhQaitoeXBpMFdLSDI1WWhvdmdOYS9kMG1kNDFiSlVVSG83MkNzS0xVS00yeVM5VVdaV3JUZVNiRnpZclo0R2Y4Nk56UDhYd3ZXcTY4aEt2TlkiLCJtYWMiOiIyNzVlZDdiMGZiYTc3NzkyYzY1ZWQ0ZjIzNDQ3ODczZGE5ZTAzN2VlMzk4YWFkNDIxMzgzZDA4ZjNkNzkyN2I0IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "s1kcbGpX6CzZLCuBRo1U_yHmHSBIf5fcMciNE8ggfpY-1791924037-1.2.1.1-cBENExUQopZExZkmiX7p5rBqMyaVZVxZMpPhCKhQLfrVbz8clqSY0x2lu0kN4MLmoxnBQtCOyr_8imdmhb.xHMAc.ZquJCqK.WqFrw1juif.86Yeoh5.RmWdrbDvJtULvxYri1bCuE0.6R8XTDFm6LKG7SiqltLEgvUroTJaVgsxE_DSTHPYXu97KtZixceN9XJrTNUOz.UUyTxRYFdoYf.VtogbnVvYPsPJ8KfUyrhuFw_59.zJxyJ6gIwiWJPd2juAC1cxe1w.FLp6aHFP9y9OYemZnZpQ0c2d.Ox9X_yb3FPuGORTGeuu4uKHPJwJIy9NkyMoMZyLs4_y_8eKAo7pjARfstd0dgWkHO1lzH99lkuzikc1RDxFY_flBmyqXGjFgqE6HsXo3x.WiM_dgJRFnw2OOeZEprd0rwH0tlJLcN.oEr_p4bn5YUqC5xwRWNOej8A2nhDuIYt3zYjUiAOr.q7DORDWfFG3lvv2ijJdBuRNXt4VZH7x5d4qX1RsMBCr2qjm.gKbB_tYbwzgDg",
    "XSRF-TOKEN": "eyJpdiI6Ikt3ZUdaQ0hoZWdzbzRMSC9sRXI1OEE9PSIsInZhbHVlIjoiM0VQR1h4WFJIYitreUNoZUMwZjdjWlh0M1JmQ0VIWFI1aEQzZ2hFQnMwS1lWTXF4cTh6emRTY2ZsSWZ0QndCei8vbllFc3l2WWRkNXZ0TEZZWEdhRXJwQVNhRithM3Y3cml1alFGeVkrekNwN1lUS3ZHVXhNdmR6WTQva2VxZkUiLCJtYWMiOiI1NGY4ZjNkOGI0N2ZjYTY4ZDU5Y2M2ZGJmZDNiMTc1NmFjODgxMGMwMDJkZGNlNmFmNDY3NGE4YjVkMGU2ZTY2IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6ImsxUXdGbnhXMTBPdDlHYllMcnJiRmc9PSIsInZhbHVlIjoiUXF1WXpPdmRPOVZ4ajhiZk45ZkxiZUhHV0QzMk14WWE5QjRmTFZTejhNZ1hTam1PZEtXRkl4SVJsanloM2NKUWI0WHZiTXNBQ1NVanFaTnFFT3EvVTVTb1p2ekhGZncxN3Rkb0NZem9xZEIva1N6Y1IwT2ZCaVcxNENoZGZCK0kiLCJtYWMiOiJlN2RmM2NkZDhkOGM0ODFiYzRjMWFlYzc0NjA3Njg2NDM5MWIyYmIzYzc4ZTgyODcxZjQ2YjE5NmYwMWE0MGU4IiwidGFnIjoiIn0%3D",
}

