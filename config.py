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
    "cf_clearance": "hezox4jgW8C7vwfRR_STzgIDyD_4CuKEEbqB9uOyLWY-1791876473-1.2.1.1-UuEZ4irzo..GWjyFS9ZsfERLOl_m58hNlGZRfAXuXzgF2H7NdQsGQ14iEVcmp1r71BoJqF6kEyZbQpNJ79EP0hR9nwDobKJB54BcEUkcI111_zpXJzH4lZr4Faj3e_hQIUPwRdqCeCwnBrcHT5B_FukzHul2oFjcPbbf77WoI3ik3PyDAxADRVl1Yk1RJv_ehpUJakrt_4LILcwtBh8Xs9TwHMG5.DkhTbb5OuqcHQQGdTno49_tE_9L_H5Kok_qEmf_OmZ0s89wnV4CtPGxM3JNYmnVkb9GF1yEWGCkTxmuKfOafWbSXyh01Ia44NfJx_qxkuaaV7PN6ynF.DxPkV6fGmaT35M2nD_f7CAQKRXZgfDIjznHit3Qa8JaL7EFIllxpLeGh1J8B4A2XSO9UEL9oYAa5XMDRdotO.EnM9XDQvuWipMpgax9bbucJBQruig9AI8ge2UzQemDQTYNKSbT1T36GUNDyZ2unQ_4VXIjcva4.69hpsHB9H7ptD1_tOPBdzTSMetsi_i1sFG7MA",
    "XSRF-TOKEN": "eyJpdiI6IkRoTkdIdjFpWk5NNE5pdmJ2dXBJOHc9PSIsInZhbHVlIjoiRmFpWVRMS3NXYTlrbHI2cTgzT0xmR1NRSzF5R3ZkbWoyem84WVA4VWd1S2dpekFKUjR2SkNpaloweGZFdWViUE1rUmNBblIrM0VZT2dDTFlUaHpRckpSdmhCVi9RMVZrRlV3NG5wcEppNmg3eE5XdGJxTkFQOWVIRW5zelJXdE4iLCJtYWMiOiIxZDA5MjQ3NGJmNWM0NjU3MzA2ZjUwYjAzNDhkMTZmYjUyOWVhOTkzZmM1ZmZhZDMzNWVmNGIwNDU0NDlmNDUxIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Im9ISTYzYTZBOWNyMGF4RTh4cnB1aGc9PSIsInZhbHVlIjoiSGt3NlVMUXk2WUFuQVl0M1RWUm5ueWZGRHFicjU0c3dKUyszamRnMWxGcnRialQ4Nk8xV2M1SDlLSjI4VDRwM1hURU5rVlRkc3FteFBhRHZ3VEhKOS9wQzZaYVNOZzRmSXNDQmQza28xRWFXbHZLZjRhOFFhRDMrOGtCTFBlQ3ciLCJtYWMiOiIwYTNlYTI2Zjc4Mzc3NDkyNjBjMjM4OGYzNGY5YWJhMWI3NjNiMGYyNTE1Y2FhNzVmNjUwZmUxOWNmY2I1OWMwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "DToueYjQvTdSUZoPuRkT8xdDe4lteMdVOkCX_Jd1W0k-1791875860-1.2.1.1-Sl9_vp3CDdP86zXoflJnL1LDzYm5.08nQOSz7_ZLnWUiITDTqBcJqmobvZMk0FVJlxQ8w8SEs53NQfJFmUbXN_97_qf9r3kl3VQZWq4.IvpzsPAv.vhFlkBTTfN6cCZHhgnNNwtkbeQ9StScrVxGgzxJIUJ8RNoAwoUNVCjc8v9ElJAySqyZfCUuvLZ9ULqf0bOCgwo5jPzBBa0NI_jZO4gmy4J0HSd_rCB9rURKBFKCxBe7UmjqXMUgMqJ1PqSy8ejuBM6un0eF_nYoH7p1aLONifoKu3kJickvPwwqASTUzKDJgZwSU3AGCNbx.78yM3aLoGwvJ9vXWI4InfGI56Ka1zaHHLVV4QDP0OHhM1SW8ka0GXVPdphk3IPCR4d5shhQ3241gv8.A0977XTeIv1VDB1Lb4GcM3zhTaSOtXpLyHM4lZx6M7tavtEaHhdhn2WDarP1MskMHqoLio5Vdcrkb7DNOvLvDhIof2GoFQCim6bjSy1WqRNMQQVEPW_IM0Dmj0JrBXIAM.Xqz5cKsw",
    "XSRF-TOKEN": "eyJpdiI6InJMcERDcU1oK0lXSG9VQU41R0t4aGc9PSIsInZhbHVlIjoiWFB4cTg0VUp1RFM2K3VObHlIMHZVWTRqbUZjcGttUU9odnRoTGI4SDd0ZmlFVnBOTGZqZk9IdFc1ci9iUFBRNWc2ZDRtNUtpc1dOcXZ2MkJUUXViUS83cGkyd05hazluenZIbGpYTy9rTExOeGU4dVBNYXNSODFVdVpVS2hHRjciLCJtYWMiOiIxMDRhY2JkZGQ1ZjVlYTAyYjMxMmRiZWRjY2E1NDU0MmJhZjY2YzE2NDljMWE1YWQwZGJmYzNhZTk4YzgyNWJmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkJPWGp1eXVWUmFIOXBPb0xXZ1g3Q2c9PSIsInZhbHVlIjoiT3N2UllQYnIrdUpYKzlWaWlUNVY3NW5RS1IzaWNqdUN5S2FwK1FFUWhIZFRYMHRMTk96YzdablJLL2pONHpvYm1SVmhwSUtpN0E4eEJiRnpkY2ZHNjFyR1ZscjdXeU81b2doSkRjRmFIY3MzV1dyYUNFTFVVS0lVTTlkL243cDYiLCJtYWMiOiI0NmE2ZGY1NGEzMzMxOTJjNWMzZTUyMDEzZjU3OTFkYjUzMWMxZGU2OGI2NzAzNGJlOWI5ZWQ4MDliZmIyY2MzIiwidGFnIjoiIn0%3D",
}

