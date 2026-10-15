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
    "cf_clearance": "V3yQlP0hfW8HgwxHLCzyi89bhJWSHbbUhDQONaj_hx4-1792087225-1.2.1.1-jJDPnpEHc5rV8hKMLAeqtOWBpBnS.k7leSMA8j70OOqNh97GS2CYt3qd87ZX8DQP8vZ24FsxhehAsVRQKSw2l2pe42hlcbXtZH.mV1IGu6PgZ8y.EW9_kO5346tNzFmUf37aXpArbGs_rCav6XmgiHE9267vAq4ptxHmRHo8WGbFvcfLxFe817RLlNY1wHZv5iQgP6IglqE2srLEy5eP2WgTx.Lkfh.meRMiasgEybLvJ68jZwXPXvK4HZMcpf4H1nUePWnIxAdECFSbV16vNcz3X9CTlVbnMNhp8zRuhZYHHxLrcgZPFodR3ZmJXC_QIz158i7GjBl7_zm60779O16u_7bIr9JFSb2oe5p_FFos_K1Lh._t0.2CzQACSBu_L9ax8Oy7UFidqPBhzYuVporMtjKdN9a2zmYGurr4FOFPnfPOYRkaobBnTR028N3SwpKNZ4kfhCehKeFl2A1LUGF06F8E0gSW1fEojTOT4whPd0ZPG3Bx0czgCfFBowp6e3wBB9t4oy62tuE.fH4i4Q",
    "XSRF-TOKEN": "eyJpdiI6Ikt2YkJOSXVINndXMDV4L0RvcGZEeFE9PSIsInZhbHVlIjoiUXI0aTNqSU5GQUJINFNHYVhmL21OVDZYdXlzdHk0M3F4ZjZqUWpyamdQU1Z3T1J2SVVFZFJKQldKSmk5N29qeWtXM1Q2b1pCV29wcVp2Q0pDVjZNbnBqdjRmNWsyWWhXZXRLZjgzVVFkN3I5SzNIMmRvbXFsVVBscVNDbTAxaE0iLCJtYWMiOiIzOGI3MzFmYjlkODcyOTc3MDEwY2IzNWEzN2E4NGI5ZjQzYWMwODgwYWQ2OTVlZTM0MmYyZDFjOTQ0MjZjM2RjIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6Ik1yWU4raVV4akwzT0R5ODM0b3FOaXc9PSIsInZhbHVlIjoiUTVMUnZFMWJWSStEaHVDc1lIMHUvTGV3NklHOEtpZWx3KzRncU80TEw5T05rbktBNmdDN2RnUEhqU3VIR2UveE9Eakdod3NqQmZ1THlBd0F5V3VxL0QvRDVMTGFQUnp3djRYczZmSmwxVEw0SE1GemU4SnE1Z1grTXZ4VGl4RjUiLCJtYWMiOiI1ZjM5YjdkM2I3YWU3NDY4MWVkMmM3ZTI3NjAxZGE0ZDRmYmQ4MTFlYmJiODhlMjdmOTgxOTM2ZjJhZGI3OWU1IiwidGFnIjoiIn0%3D",
}

COOKIES_2 = {
    "_fbp": "fb.1.1791826808610.852005192451035990",
    "cf_clearance": "nX9Bb1sj9WQeLq0Ah1Eb8du1lWGnXMZ.KxU.PiynBm0-1792088996-1.2.1.1-zsLgZ5aUegsdAv9aLtImTT2Wb2SGJZMerQC256jBZDYdl.3IBrIP7zeoksnRVv_1aahlixe8TjGZrqMjZES3lenxugfZBlxGzGHPnKwsBDh5RvMrYFpZol5nmiDkiuFfssZXZ3bg9aX0Ik2EhmUlQFMgYoKVBTgfj0ii1.wzesz0L1j_iEzd7ls4rJ4Pvd.SxNmbq3KipRv5gkEJ4QFBrfDwkLKJPupCaNLTlpt9.55TZLWCfMcpKKt80w0gK8c6_UDlBhCAWvQffiMJyjw78aaOsq.vxMdBtFQC8imk5agkeshd6ZgZRw0ckRG0w3JIfgjxfi.md0CAvpm5Z6hy7BabJbs2EqnQh.fvBHD22mvVyIAirbBFN9xE9S5d1UHiDD._mHTmgxa8hftk2e6t0iLSWmCYLT4AIO.k7x0ixFQvS957T7z2OeoBc1VcOLX4.60zcFwnZHYqYOGC4zS5YtRPOs.fZTRUNHlRrFzjPZeyTuyEcTM7rb4i0LlhRIdkXtBHa8LPtczVxbyXOQy8bA",
    "XSRF-TOKEN": "eyJpdiI6IjZBck00bzliZ3ZySWhRR2pJUjRjaVE9PSIsInZhbHVlIjoiK0srZmtRb3RXOHJ6T2Q5cHpxc1E0ODNKVTRGeGxuWERYcHFzRzFTOWFNUXRUNkFRVmoyaXJWT0U1Z01mQnpreXhSa1NYVDRwQUVPZGRzbjFQY3RIMlRQWStaVUhwYjBIRUY1dUdjUGVBc1ZpSktweWZienR4WkcyTDNvTm1uWjkiLCJtYWMiOiI3ZWM3ODk2NjZkOWQ2ZDc1NGZhNmY4Mjk0YzFhMDE1M2NmZWYwOTM5NzcwYmRlMjg2MTJhYzc1ZTQzMjNhZDEzIiwidGFnIjoiIn0%3D",
    "ivas_sms_session": "eyJpdiI6IjFPSU5mdDU3SThIWUZYdVNoM09ZT1E9PSIsInZhbHVlIjoiLzUvYkFjU3o3cU5TOCtsY1lLMjBHQnNVYnNsWkVDMFAyRGhWWXh5bXNScy9zcjJuY0RUVUw0bjkzQkFpOXZXTlpSSGwyWEJpZHdBNXRoamlJSm5vdE1KcTR0K292aGVPbEFWL25CaGxRS1dFQWlMVDd3c3JoR25KSWppYkR1bUsiLCJtYWMiOiI2YTBkOTVhNDZlYWFkNzk4ZDY1M2M2MjE0OTkwYWUwOGUwYjY3OGM5NzQ2NzEwNGM4MDgxODUyNTdiNGJlMjVhIiwidGFnIjoiIn0%3D",
}

