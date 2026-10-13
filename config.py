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
    "cf_clearance": "uRoFpUZ4N0U.48knIlDVf38wdfFaJEJkfigotOQUwJg-1791877664-1.2.1.1-UMCJmIlWPg7jjd._KfATDA9AHna55gD.yhw4F.EA0tPnBR6hWum.CoUp8OnDAGjiCQQq8xgETxVcn79S5Kd1FA8M7qFlr7mEmeTuT8fsmUyq6ZUoX.k0vR3W6d9_jpLhFECPK_Q4fxtGSOW25GxMK3i3qHDtZSXOJehzGF__1EBrgvVwKt_wukYy9mFOpMixGrNpeLUT_MNTgylvmm2WA0RP5Ru9tiiR3n864bANsuIfbCQxv.Ia96ik2N_QyXDi__nYCJJx44Js_7sl5yL5lZakarN3jvl_mhP0nG8iCVk4_yIBBmT10S.Qoz01bBztUBowtxW61MbpoSDPRH9eLsaP3J3keXgt0RezgLoiFsb4R9ARz8jn6yhDyWt89.wJTTBSCpIOxmnhKWH9MEQCIC5LGoxpbq7XkUbNEgNkzIyQPCyAiLMIao9ZIkbTPA.riaT8nxyfl.gE78sLGH_pNrbL92.Jn4Bg68nsDDixecIQk4AqERJvomcV5Xth7bY7zT6x4gpAJYH9I18C3GI8XQ",
    "XSRF-TOKEN": "eyJpdiI6Ink2TjdudTdGTTI2OTFCQ0FDMm51aVE9PSIsInZhbHVlIjoidEp6WFg1bjhTaUlDL3M3WkVyOEFFZW93d3RPQnY5MFkwL21iMTFUMVlrRFk4aDhQZVc4RXdYdzIxVm1mc0lLMWZNbmE2SlpUWlFUb1R4aWpYeEt0UkpFR3Z5YUIvOGNTMUcwM1dRVkJUZlo0U2ZzZlZJaVlDWnpvTFpib0MrMTAiLCJtYWMiOiI1MDg4Zjg3MzdlNGVmNDk5ZmFkZWJmZDkyYmIyMzAyOWU1OGVhOWY5MTk0ZWQ4ZjViMjUzYWE2YThlYTVhMDMyIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6InRNTkppSXgxdm9NZDltOE83REErYkE9PSIsInZhbHVlIjoiZ292ZzdrR0EvdmZEUkdvTi9ORnFBT1NHMWhsbHUyY3ZPd05kbjIwUFQ3dFNSNTRvOWozZnNIeEVCblRocmlTbmRpd0tzKzVmWFZrZThiM0FvVHZYYk9DWjJDMXd6eks0WGxnV2hrVUV6UllHSWd0MG1RS2s2UlVubnYrajNvYWUiLCJtYWMiOiI4OGYzMzRjMDc0MTE3OGY1ZjAxZGYzYTNjNWM4OGRiY2ZkODRlZDQyN2EyYzQxOTJlYmIwMWQ2ZTg3YWY5MDJlIiwidGFnIjoiIn0%3D",
}

