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
    "cf_clearance": "KMN.agw6xFMgm_61vcqiCDr9xf9yY2fF3WDioKE79IU-1791890321-1.2.1.1-2gMB9QnMO7xufr4yPBRJfj.VmfXMMLGs1..QI9m4o3mI4z9iqfoMuoZoRRfxBhtO53mXk.fjcSmJ8fh2oBU7nNDtLKTfHj9Ipb_FlwBRDjnD0ZdZFXQA_D9pR679clMYB_5_tiJvIQvGSIy6aneBrfkE0Th.eavxovOSbVWmDblu7B93GaqLj.WRX.7b33zjU3cxEnjtp0qPZrQj78TS2yVct5EzoOIxd_ypHHipuKKsz4baQNY.bQ3SdBCArXxeod3wc9zyMdTwchIgegG.tTSxr4UzkJRMlFI_TqBSOodxWgqn_kEi6JOxoc7wYJK9UBpgy5jEk3YplAlIGxRuLKLkPo88MU0pbUMr7EcTYyXFN9BPF2wlRoMSGBTk3HLG9bCQIkd9zxXScuUnzCTYfE_hCFIxLpDIStIKCTcB3.8DdOqiW15zonaRn4SSP5YUdQvXsC_RAa.0FefO8BPFaQ5SL9oPAfNXt1aU9.emjfCssFjcvmkVuzjJE4hyc43Caqcy4KwYiPTQ_eaPDnYElw",
    "XSRF-TOKEN": "eyJpdiI6ImtIbElKaWozNDQ1enlZV1JSZHJWSHc9PSIsInZhbHVlIjoiZGE0VTZRbmM4S0FiQk5VSHlPTEZYc2VscmFHTStDOHM3WW1CbmNrVEpuUlFtVm5FMXRrUEFNaExpNS92azNvVld2UWQxWlErcnFLMEFIWXI2V3pEVHdGODBSbmx6dU0xM01VQ09wSkc4WG5UK2xIcUFXYVMvWHJabHppWVJycG0iLCJtYWMiOiI4NTVmODFiNjJlYmQyM2Q4YmExNTQwNGYwMDk1MWM4OGZiNDI1ODAwNjViNDNhZDY2Y2FmOTk5MTA4NWJmM2I0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ild3bEpuWWhrYXloMFMzZmFncnU5dXc9PSIsInZhbHVlIjoiZEloS1RUaU83UXVmMWZnSVY4V0M1R0JFdlFwQ0ZWdkFoTDJFMFVRVlpuYi9naDBKa2VnWWl4NHBmWEd1dG9EYUlUYmpwaDlXaTF2MmhmTFllakRiYy9RUGo4aDhObHR1UzkveFBSdmpReUZvZkk3azNVTnVTOUtsYlRpakV1YlIiLCJtYWMiOiI1YmZiNWFhNTNmMjMwNGM2MjUzZDU4NTVhYzVmY2U0ODNiNWM2ZjI5NTJmOGM4ODgzZmQxM2YyMDc5MDBjNzdlIiwidGFnIjoiIn0%3D",
}

