# ═══════════════════════════════════════════════════════════════
#  OTP UTILS - Country Flags, Masking, Platform & OTP Extractor
# ═══════════════════════════════════════════════════════════════

import re

# ────────────────────────────────────────────
#  COUNTRY DATA - Kode negara + flag emoji
# ────────────────────────────────────────────
COUNTRY_FLAGS = {
    "AF": "🇦🇫", "AL": "🇦🇱", "DZ": "🇩🇿", "AO": "🇦🇴", "AR": "🇦🇷",
    "AM": "🇦🇲", "AU": "🇦🇺", "AT": "🇦🇹", "AZ": "🇦🇿", "BD": "🇧🇩",
    "BY": "🇧🇾", "BE": "🇧🇪", "BJ": "🇧🇯", "BO": "🇧🇴", "BA": "🇧🇦",
    "BW": "🇧🇼", "BR": "🇧🇷", "BN": "🇧🇳", "BG": "🇧🇬", "BF": "🇧🇫",
    "BI": "🇧🇮", "KH": "🇰🇭", "CM": "🇨🇲", "CA": "🇨🇦", "CV": "🇨🇻",
    "CF": "🇨🇫", "TD": "🇹🇩", "CL": "🇨🇱", "CN": "🇨🇳", "CO": "🇨🇴",
    "KM": "🇰🇲", "CG": "🇨🇬", "CD": "🇨🇩", "CR": "🇨🇷", "CI": "🇨🇮",
    "HR": "🇭🇷", "CU": "🇨🇺", "CY": "🇨🇾", "CZ": "🇨🇿", "DK": "🇩🇰",
    "DJ": "🇩🇯", "DO": "🇩🇴", "EC": "🇪🇨", "EG": "🇪🇬", "SV": "🇸🇻",
    "GQ": "🇬🇶", "ER": "🇪🇷", "EE": "🇪🇪", "ET": "🇪🇹", "FJ": "🇫🇯",
    "FI": "🇫🇮", "FR": "🇫🇷", "GA": "🇬🇦", "GM": "🇬🇲", "GE": "🇬🇪",
    "DE": "🇩🇪", "GH": "🇬🇭", "GR": "🇬🇷", "GT": "🇬🇹", "GN": "🇬🇳",
    "GW": "🇬🇼", "GY": "🇬🇾", "HT": "🇭🇹", "HN": "🇭🇳", "HK": "🇭🇰",
    "HU": "🇭🇺", "IS": "🇮🇸", "IN": "🇮🇳", "ID": "🇮🇩", "IR": "🇮🇷",
    "IQ": "🇮🇶", "IE": "🇮🇪", "IL": "🇮🇱", "IT": "🇮🇹", "JM": "🇯🇲",
    "JP": "🇯🇵", "JO": "🇯🇴", "KZ": "🇰🇿", "KE": "🇰🇪", "KR": "🇰🇷",
    "KW": "🇰🇼", "KG": "🇰🇬", "LA": "🇱🇦", "LV": "🇱🇻", "LB": "🇱🇧",
    "LS": "🇱🇸", "LR": "🇱🇷", "LY": "🇱🇾", "LT": "🇱🇹", "LU": "🇱🇺",
    "MO": "🇲🇴", "MK": "🇲🇰", "MG": "🇲🇬", "MW": "🇲🇼", "MY": "🇲🇾",
    "MV": "🇲🇻", "ML": "🇲🇱", "MT": "🇲🇹", "MR": "🇲🇷", "MU": "🇲🇺",
    "MX": "🇲🇽", "MD": "🇲🇩", "MN": "🇲🇳", "ME": "🇲🇪", "MA": "🇲🇦",
    "MZ": "🇲🇿", "MM": "🇲🇲", "NA": "🇳🇦", "NP": "🇳🇵", "NL": "🇳🇱",
    "NZ": "🇳🇿", "NI": "🇳🇮", "NE": "🇳🇪", "NG": "🇳🇬", "NO": "🇳🇴",
    "OM": "🇴🇲", "PK": "🇵🇰", "PS": "🇵🇸", "PA": "🇵🇦", "PG": "🇵🇬",
    "PY": "🇵🇾", "PE": "🇵🇪", "PH": "🇵🇭", "PL": "🇵🇱", "PT": "🇵🇹",
    "PR": "🇵🇷", "QA": "🇶🇦", "RO": "🇷🇴", "RU": "🇷🇺", "RW": "🇷🇼",
    "SA": "🇸🇦", "SN": "🇸🇳", "RS": "🇷🇸", "SC": "🇸🇨", "SL": "🇸🇱",
    "SG": "🇸🇬", "SK": "🇸🇰", "SI": "🇸🇮", "SO": "🇸🇴", "ZA": "🇿🇦",
    "SS": "🇸🇸", "ES": "🇪🇸", "LK": "🇱🇰", "SD": "🇸🇩", "SR": "🇸🇷",
    "SZ": "🇸🇿", "SE": "🇸🇪", "CH": "🇨🇭", "SY": "🇸🇾", "TW": "🇹🇼",
    "TJ": "🇹🇯", "TZ": "🇹🇿", "TH": "🇹🇭", "TL": "🇹🇱", "TG": "🇹🇬",
    "TT": "🇹🇹", "TN": "🇹🇳", "TR": "🇹🇷", "TM": "🇹🇲", "UG": "🇺🇬",
    "UA": "🇺🇦", "AE": "🇦🇪", "GB": "🇬🇧", "US": "🇺🇸", "UY": "🇺🇾",
    "UZ": "🇺🇿", "VE": "🇻🇪", "VN": "🇻🇳", "YE": "🇾🇪", "ZM": "🇿🇲",
    "ZW": "🇿🇼", "ML": "🇲🇱",
}

# Prefix -> Country Code
PHONE_PREFIX_TO_COUNTRY = {
    "+1": "US", "+7": "RU", "+20": "EG", "+27": "ZA", "+30": "GR",
    "+31": "NL", "+32": "BE", "+33": "FR", "+34": "ES", "+36": "HU",
    "+39": "IT", "+40": "RO", "+41": "CH", "+43": "AT", "+44": "GB",
    "+45": "DK", "+46": "SE", "+47": "NO", "+48": "PL", "+49": "DE",
    "+51": "PE", "+52": "MX", "+53": "CU", "+54": "AR", "+55": "BR",
    "+56": "CL", "+57": "CO", "+58": "VE", "+60": "MY", "+61": "AU",
    "+62": "ID", "+63": "PH", "+64": "NZ", "+65": "SG", "+66": "TH",
    "+81": "JP", "+82": "KR", "+84": "VN", "+86": "CN", "+90": "TR",
    "+91": "IN", "+92": "PK", "+93": "AF", "+94": "LK", "+95": "MM",
    "+98": "IR", "+211": "SS", "+212": "MA", "+213": "DZ", "+216": "TN",
    "+218": "LY", "+220": "GM", "+221": "SN", "+222": "MR", "+223": "ML",
    "+224": "GN", "+225": "CI", "+226": "BF", "+227": "NE", "+228": "TG",
    "+229": "BJ", "+230": "MU", "+231": "LR", "+232": "SL", "+233": "GH",
    "+234": "NG", "+235": "TD", "+236": "CF", "+237": "CM", "+238": "CV",
    "+239": "ST", "+240": "GQ", "+241": "GA", "+242": "CG", "+243": "CD",
    "+244": "AO", "+245": "GW", "+248": "SC", "+249": "SD", "+250": "RW",
    "+251": "ET", "+252": "SO", "+253": "DJ", "+254": "KE", "+255": "TZ",
    "+256": "UG", "+257": "BI", "+258": "MZ", "+260": "ZM", "+261": "MG",
    "+262": "RE", "+263": "ZW", "+265": "MW", "+266": "LS", "+267": "BW",
    "+268": "SZ", "+269": "KM", "+290": "SH", "+291": "ER",
    "+350": "GI", "+351": "PT", "+352": "LU", "+353": "IE", "+354": "IS",
    "+355": "AL", "+356": "MT", "+357": "CY", "+358": "FI",
    "+370": "LT", "+371": "LV", "+372": "EE", "+373": "MD",
    "+374": "AM", "+375": "BY", "+376": "AD", "+380": "UA", "+381": "RS",
    "+382": "ME", "+383": "XK", "+385": "HR", "+386": "SI", "+387": "BA",
    "+389": "MK", "+420": "CZ", "+421": "SK", "+855": "KH", "+856": "LA",
    "+880": "BD", "+960": "MV", "+961": "LB", "+962": "JO", "+963": "SY",
    "+964": "IQ", "+965": "KW", "+966": "SA", "+967": "YE", "+968": "OM",
    "+970": "PS", "+971": "AE", "+972": "IL", "+973": "BH", "+974": "QA",
    "+975": "BT", "+976": "MN", "+977": "NP", "+992": "TJ", "+993": "TM",
    "+994": "AZ", "+995": "GE", "+996": "KG", "+998": "UZ",
}

COUNTRY_NAME_TO_CODE = {
    "GERMANY": "DE", "FRANCE": "FR", "SPAIN": "ES", "ITALY": "IT",
    "UNITED KINGDOM": "GB", "UK": "GB", "UNITED STATES": "US", "USA": "US",
    "BRAZIL": "BR", "INDIA": "IN", "INDONESIA": "ID", "JAPAN": "JP",
    "SOUTH KOREA": "KR", "KOREA": "KR", "CHINA": "CN", "RUSSIA": "RU",
    "TURKEY": "TR", "NIGERIA": "NG", "EGYPT": "EG", "SOUTH AFRICA": "ZA",
    "KENYA": "KE", "GHANA": "GH", "CAMEROON": "CM", "SENEGAL": "SN",
    "MALI": "ML", "CAMBODIA": "KH", "THAILAND": "TH", "VIETNAM": "VN",
    "MALAYSIA": "MY", "PHILIPPINES": "PH", "SINGAPORE": "SG", "MYANMAR": "MM",
    "PAKISTAN": "PK", "BANGLADESH": "BD", "NEPAL": "NP", "MEXICO": "MX",
    "ARGENTINA": "AR", "COLOMBIA": "CO", "CHILE": "CL", "PERU": "PE",
}


def get_country_from_phone(phone_number: str) -> tuple:
    """Deteksi kode negara dari nomor telepon. Returns (country_code, flag_emoji)."""
    phone = (phone_number or "").strip()
    if not phone.startswith("+"):
        phone = "+" + phone

    for length in [5, 4, 3, 2]:
        prefix = phone[:length]
        if prefix in PHONE_PREFIX_TO_COUNTRY:
            cc = PHONE_PREFIX_TO_COUNTRY[prefix]
            flag = COUNTRY_FLAGS.get(cc, "🏳️")
            return cc, flag

    return "??", "🏳️"


def get_country_from_range_name(range_name: str) -> tuple:
    """Parse country dari range name seperti 'GERMANY 1100' -> ('DE', '🇩🇪')."""
    if not range_name:
        return "??", "🏳️"
    name_clean = re.sub(r'\s*\d+\s*$', '', range_name.strip()).upper()
    if name_clean in COUNTRY_NAME_TO_CODE:
        cc = COUNTRY_NAME_TO_CODE[name_clean]
        return cc, COUNTRY_FLAGS.get(cc, "🏳️")
    if name_clean in COUNTRY_FLAGS:
        return name_clean, COUNTRY_FLAGS[name_clean]
    return "??", "🏳️"


def mask_phone_number(phone: str, sensor_text: str = None) -> str:
    """
    Format nomor telepon: 4 angka pertama dan 4 angka terakhir.
    Contoh: 263799991419 -> 2637 ~ 1419 (atau custom sensor)
    """
    clean = (phone or "").strip()
    prefix = "+" if clean.startswith("+") else ""
    digits = clean.lstrip("+")
    sep = f" {sensor_text} " if sensor_text else " ~ "
    if len(digits) <= 8:
        return clean
    first_4 = digits[:4]
    last_4 = digits[-4:]
    return f"{prefix}{first_4}{sep}{last_4}"


def detect_platform(sender_or_message: str) -> tuple:
    """Deteksi platform OTP. Returns (platform_name, emoji)."""
    text_lower = (sender_or_message or "").lower()

    platform_map = {
        "whatsapp": ("WhatsApp", "🟢"),
        "wa ": ("WhatsApp", "🟢"),
        "telegram": ("Telegram", "🔵"),
        "facebook": ("Facebook", "🔵"),
        "fb ": ("Facebook", "🔵"),
        "instagram": ("Instagram", "🟣"),
        "tiktok": ("TikTok", "⚫"),
        "twitter": ("Twitter", "🐦"),
        "x.com": ("Twitter/X", "🐦"),
        "google": ("Google", "🔴"),
        "gmail": ("Google", "🔴"),
        "yahoo": ("Yahoo", "🟣"),
        "microsoft": ("Microsoft", "🔷"),
        "apple": ("Apple", "🍎"),
        "icloud": ("Apple", "🍎"),
        "snapchat": ("Snapchat", "👻"),
        "discord": ("Discord", "💜"),
        "signal": ("Signal", "💬"),
        "viber": ("Viber", "💜"),
        "line": ("LINE", "💚"),
        "wechat": ("WeChat", "💚"),
        "uber": ("Uber", "⬛"),
        "grab": ("Grab", "💚"),
        "gojek": ("Gojek", "💚"),
        "shopee": ("Shopee", "🟠"),
        "lazada": ("Lazada", "🔵"),
        "tokopedia": ("Tokopedia", "💚"),
        "paypal": ("PayPal", "🔵"),
        "binance": ("Binance", "🟡"),
        "amazon": ("Amazon", "📦"),
        "netflix": ("Netflix", "🔴"),
        "spotify": ("Spotify", "💚"),
    }

    for keyword, (name, emoji) in platform_map.items():
        if keyword in text_lower:
            return name, emoji

    return "SMS", "📱"


def extract_otp(message_text: str) -> str:
    """Ekstrak kode OTP dari teks pesan SMS."""
    if not message_text:
        return "N/A"

    # 1. Format dengan tanda hubung / spasi (contoh WhatsApp: 195-127 atau 195 127)
    wa_match = re.search(r'(?:code|kode|otp|pin|clave|código)[\s\w]*?[:\s]+(\d{3}[\-\s]\d{3})', message_text, re.IGNORECASE)
    if wa_match:
        return wa_match.group(1).replace("-", "").replace(" ", "")

    # Pola 3 digit - 3 digit berdiri sendiri di pesan (contoh: 195-127)
    dash_match = re.search(r'(?:^|[^\d])(\d{3}[\-]\d{3})(?:[^\d]|$)', message_text)
    if dash_match:
        return dash_match.group(1).replace("-", "")

    # 2. Pola kata kunci umum diikuti angka 4-8 digit
    patterns = [
        r'(?:code|kode|otp|pin|verify|verification|verifikasi|clave|código)[\s\w]*?[:\-\s]+(\d{4,8})',
        r'(\d{4,8})\s*(?:is your|adalah|code|kode|otp|es tu)',
        r'(?:^|\s)(\d{6})(?:\s|$|\.|,)',   # 6 digit standalone
        r'(?:^|\s)(\d{4})(?:\s|$|\.|,)',   # 4 digit standalone
        r'(?:^|\s)(\d{5})(?:\s|$|\.|,)',   # 5 digit standalone
        r'(?:^|\s)(\d{8})(?:\s|$|\.|,)',   # 8 digit standalone
    ]

    for pattern in patterns:
        match = re.search(pattern, message_text, re.IGNORECASE)
        if match:
            return match.group(1)

    numbers = re.findall(r'\d{4,8}', message_text)
    if numbers:
        return numbers[0]

    return "N/A"
