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
    "cf_clearance": "MUItf25vP35feGGx_eRCF0nGHsCOqCeY6QoZaLr93I0-1792125318-1.2.1.1-l.SuLwfzyYOLt1WKoG8fJCuv9gbb8zV4JGKOHiTZzOeiSPoVO1fLkKAdNenuVgonpMCe1PLO0z7KxK9u6IBsgX.re.G7PiifS0a18tuVsv3ewozaqZ04h5C6iRG0a9XPUJIoIAe7q2BlZQGttLlZPmFd_WfWPgN6vOag6IzFxQozYqKPpbH1ZA2HqX2uOHs0aTLb3D9cFPt5Ia2C9dSFdC3b2N1CSRamQn7R0if4oURkuUnIyTyfxlgf8LKHoObRV7WSrGWMXkD1cGoAvvRGe12WNMzgaXO5k3CzEmsHHZ_UeQvlRlglvHzJOMdoqkcZcj2RqAp26xu8mWJTpJ.yoFPTxMc3h_uKo4ZeQ72vtIOlxmH7gmlg0x2qk0ltrU3nQF7H_AONYCExthDQyt8K8C1yqKTFRLAvhAJIjrEC5Y9Pzmrn.lGs2JEzFEJztACfyZ3KvIr_h4fy7K5ssJeTvMzbzDU3bUTR.xHZn_Eo5s0MjRHBfIBCTvoD83QvRs_JGre0ma2rIoXsyMTYg7iQDQ",
    "XSRF-TOKEN": "eyJpdiI6IkhGQlhYYW1yMWJTcXBQNXQwemNkTXc9PSIsInZhbHVlIjoidVJXUGxFV051ajFPM1hFWFdnYnN0b3JlekVDUVprbDR5dkZxZTVZR0lEVVlKc3VMMGhib1U0K2t3TjBYSEpVNytJYVNIRWdwN1lLc045OWYzN0ZCRjk5c3YzVlVhVXIzMXhSNk1uSzlBcTRyaThKeEhWTk9LaGRibk5tbVZ3ZlUiLCJtYWMiOiI2YjM2ZWFlY2ViMjgzNTBjYTY0YTg4OTFiYTI2MWEwOGYxYzdlZmFhZjM0NzAyYTgxYjRlY2JjNTRkODcwY2ExIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IlV5cUt2RjRJaEY2NEtKYjFOa0Z6b2c9PSIsInZhbHVlIjoiM0wvTmk0bEp2N1h4ekNZd082ak4vU1BWNm1adHBQU3dRaEUxK1U4N0EvZTIxMU45QTZ0REZleFVaUG8wdlR6ZlRSTW0xeGxLREdXTFZWTTR0azMrYlcyd0NzRmJPMGtvekYrcUREMHZRZlAvSHVocW5GazF5YS9RbkNXOUNiTEwiLCJtYWMiOiIyZDkxNzg2ZWEwNzBhNTM0OWFiMGQ2MDYxNmE0NDczNTE3ZjZiZDhlY2ZhMzAzYWVkOTc1YThlMmEyYTgyZDEwIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "TeGi3OE9fFSXF6UuUIrl1FP2cRGqUmGRUhz.HXob5I0-1792125308-1.2.1.1-O3mSqRoDIPVujW.mplF8Yom2MVQieWzZWLL8sfK7rC4msnBVhON1SQ_o4Uq.z1m3AF0yhqYiT_nnIujS1OTc.sewSgcEPSiX74D53c82FWyK7xeuwFsCoy_RMfJTgqnIp5lDkmnBFq3RrwRl2eVNvKDnwujMUUl5iG9hA1qAXkFEaGjChe8YK9S.x6vjoNPWSDBeevYnBMKY8qQYvhV7V8kU2SwyNKjhFPP53KIok3s17y2gINmMLglLwmwSIMkKzZlIdJZNg5wBRWcG3g.5S.buZVtrFISfeBSHTjRWZicnkoqVDeaZHLJ47EtI4dkDQ56olMWuNUktljtpyj3lM6.ENZqdAy89ZI6gkoH.mewKCJg97VodxCqdL.nMPIvIxwjnGQnyFztJHMU2zi1SSlGNoo7r.E3jRC0YJOnujiP2zLktOY1ec86Q9cYny4Lq4EXJrNlTviLVPsUKtmrEvZ4wzH8l1YOT5pZN8yTuzsYL5dN898h5KWhDosY4njnIA74l1cUTKz2dX0Vuvh4snw",
    "XSRF-TOKEN": "eyJpdiI6IkxCTWw2RnpOWjJ1c1hiR244UzNSMmc9PSIsInZhbHVlIjoiYk5vRldFczB5T3Fib29naWU0MGIybVhSNWI3SFdQdkF2KzMvVEtscmxrMXIvK1EwREROaTlqRCtVNUZRVExJNW83VU1UYXkwd0cwKzBFby9sYjUvWThMQjVuQmIrWFBZY0dSc1c3Sys5U1VvaFdSVVliaW85b0xnWGp3cERNSmYiLCJtYWMiOiJkYWM3ZWYxOTQ1ZmZmMDIyNzgwNGE1ZjYwMTU4YmUzYmI5ZmI1ZTBmZmExNTAyZWRlM2UxYzViZjhjMmFiODY0IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IkxqRWJEa1JTRUN4a1NVN0JFbFNxaVE9PSIsInZhbHVlIjoiUUVuMU50SHRmODM4UFVPK2NDMnp2Uk1tTk1CNFRFY0FWVGRDRHkrVGNsVnJyMVNWU1htUXY5bzdSSDRLTlltYytVaFNkTWFUdndNRFZTTlByY3o1dTF3TS9kV1F3ckJQT215cWZ2aThDdThZa1M3d2hLZ21xWHlBckE1MUtIbGkiLCJtYWMiOiJlMmQwNDM1YzlmMjNjZTE4ZGM4NzRkZmM0Y2UzZmY3MjI0ZDM2MTZmNzBkYTcxMGI5MmFmZDM1OTk4OGM3MzEyIiwidGFnIjoiIn0%3D",
}

