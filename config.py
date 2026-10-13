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
    "cf_clearance": "VY2EnFPaeap_FDPgWe2n06OjxHKzOeScfaRRedICipM-1791885520-1.2.1.1-wrvIXEIIQYZmwZRJBdP2HKBzGBxyAGUdJ9rot0cvJYRdC76JWq57HdyXRE4LpJgXpgbfY5K0Wv4E1x_NeybCjlPhnhwleUlGZr2xBUffqH9iUu_RTaas5t7N9DgSnhMWF_ZBQ78GJt.J17X3gVvwqi52LWCNjU8QYbzrL0YL65WyXHgnrIH7Jt3ce57EYXsqiKzYJNaPaXG6gUm3_zsfYmVyVtLG55r7IzgXewbtaxWel4C3rgPgxruwv2LaAAHwFp0hs3ExWqtHNudK6G4KWwvkFUC5LvSGiu5kw6aZy220c18xFZHBLn8z6urfcz_VuCOeUOLySwM9w5i9bf.1a7qYPFyifrYCTgxMjl45imYNuxAPNUuO1P_bh600vv8teLCqahCgHPRHQG8isMDONwzIUZ8HrIunpMBT8Wyco5WLQ2Bq0oOq1Ydlv4U2mxrfYATk6a5jhzcGKdK.jEP50LjaMyemK2fWHGc7nm5TkPSjK.V5F.1ZVsdpJT5JO6DMY2kg_STm28VRoZ0c0gWqgA",
    "XSRF-TOKEN": "eyJpdiI6InNGMmxVdnNnaFhGRmZPZVM2R3JKOFE9PSIsInZhbHVlIjoiRmVsMEhITXVuek5UV1NvRHRmZ01KNk9LU1Q3NkdOTitlaFFaYndpU1pHclF1RjdOamNDQzg0MVZ4Y1NqaTd2MldUMStsU3BzT1d1d2V1enRlU3VqbVVGS2I5ZjRXTGFaR1FKckFpb3ZYTVB5YXhBblpxRHdKdkh3Q2swRTZwT0kiLCJtYWMiOiJkNzQxMzdmMDRiMDNhYzVhZGRmMmZkZDY1YjY3ZDY1NmYyM2JhMDE3NjNmM2YwYzZjM2Y2ZjVlNDJlMjNkZjBmIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IklqaGlsZFNSU1llUUhZMERmTVhhdXc9PSIsInZhbHVlIjoiZ3dJbkhPUHJ4Ny9CWkY5QUhmM203UHI4Uit0Zmg2MkNXRHZmRmlwcjUvWUd5UE13aHRFZFE3azBnM3o2WTlNTnpZV21PMzRLMVBIM0t0NDlVNVRPSnRMRmlJeElBa3pVM3JTZjNHZjdqblJSamV6T3NsVEExWW1ndHBZNFlhN3IiLCJtYWMiOiJhMjMyMWE5ODljZjA4ZmQ4YzRlYmJhNjU5ZTJhM2ZlMDNhN2FiYWFjMWE3ZTgwYzY5OWVlNmFjYTdhNTEwMDQyIiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "O3_0zXIHniMIvc52PRoe3furf1B03wxz0aRgLN68OSA-1791886702-1.2.1.1-fa.QZHkNRETk5qMoERvQNi.Ge1cWe27VAJuNbnVPEo4rCnh.xYQs0GdB8C8WKzGzak_37Pm0K3GS2HMX_fLhsS18jhweFLBU82nzxVGb2Oq5Teb7KibU0fxYig70Xcka369XWoDBYAk1292s_vH1GXSXGG9y7PhpWIxifZD7Tx5MCQZhSkElm79iQAq0iohJAyv.maR7gnuU92OMlK8vFMbA1Jq2V5_NNLeK_szt.eKqXSfrDiipBS9jW32P7PtlnNSQw8qjrFn4lhT9vIf0APXPq3eRvbnaW5_9JrjNVhTFou3mwqvPMRG0ryzYI0PQzpIaUd.CaV90l4oKpuF2qROLZObCd_nAnNZDP.L3s2FZj_HSxi7lEm4FBYBrtAvqafqfRFqosiVYSXJouYZTM10FZF9Lizm3edOWPWN1ZyqVya3HLx2UIOhRDDbiEH6ArKExcaD.9wucicfVpj7UEtDA5_ZZ4ZXf6OvQ.2JaekNMCA7zg8QpaasPGI7Wq7zO0tBOwTkcAdw8jYhbMhGgoA",
    "XSRF-TOKEN": "eyJpdiI6Ik5rWCtTaDc3MHMzQ0hTYk1ZSzYzQ2c9PSIsInZhbHVlIjoiYi82bzRWRHRLbm9VL0Qza0ZZZXFESkZMRDJMOG5aZnNwTFdzaGdhZG03NjRWak96THRUQXJvYUZhTGJCaG5IQXFEeXlWTGpXdFIva255U21xOUsxVHI0VHFnWDJ0TE5BWkxEQy8xbU44TmgzaE5rSmxCYytMM1pPOG1xY3NwSGUiLCJtYWMiOiJlZjRkNDkyNjA4NGQ3NjU2ZWJlNjA3NDlhOTdkOTVhY2JhMjg0MWE3Y2QxMDQ0MjkxMTVmYjkwYjY5MmY4NDU5IiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ilpoa0dFdmdOdklEL2lQbkRmQmpDd1E9PSIsInZhbHVlIjoicjdJendqTlo3N3hpVnlISStoSmM0c0VpTzlwRzE3Y2h4VWVnWHhqRHZCSnkwWWhCYmhqMG1jMDZCc0tSNGp0VUkrVnBWT0FyOSt6d0Q1NkREd1I5SCtEVDJiTjZtaFNCQi9kbHg3WmdHbXRTZFVRRERlODVEeFRXVFl4S29BZEYiLCJtYWMiOiJjZjY2M2NmNjI3OGE0ZjgwMDI1YmI1MTA4ODRmOTc5OGU3M2IzYWU2Y2Q0OTBmOTdjYTdmZjljYzJjMjIzYWZjIiwidGFnIjoiIn0%3D",
}

