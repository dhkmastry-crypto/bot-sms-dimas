#!/usr/bin/env python3
"""
Comprehensive Test Suite for OTP IVA SMS Project
Tests all modules, imports, and core functions after Elite SMS removal.
"""

import os
import sys
import traceback

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level from scratch/ to project root
PROJECT_DIR = os.path.dirname(BASE_DIR)
os.chdir(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)

passed = 0
failed = 0
errors = []

def test(name, func):
    global passed, failed, errors
    try:
        result = func()
        if result is True or result is None:
            print(f"  \u2705 {name}")
            passed += 1
        else:
            print(f"  \u274c {name} -> {result}")
            failed += 1
            errors.append((name, str(result)))
    except Exception as e:
        tb = traceback.format_exc()
        print(f"  \u274c {name} -> {e}")
        failed += 1
        errors.append((name, tb))


print("=" * 60)
print("\U0001f9ea OTP IVA SMS - COMPREHENSIVE TEST SUITE")
print("=" * 60)

# 1. CONFIG
print("\n\U0001f4cb [1/10] Testing config.py...")

def test_config_import():
    import config
    return True

def test_config_values():
    import config
    assert config.BOT_TOKEN, "BOT_TOKEN kosong"
    assert config.GROUP_CHAT_ID, "GROUP_CHAT_ID kosong"
    assert config.IVASMS_URL, "IVASMS_URL kosong"
    assert config.POLL_INTERVAL > 0, "POLL_INTERVAL invalid"
    return True

def test_config_no_elite():
    import config
    has_elite = hasattr(config, 'ELITE_SMS_ENABLED')
    if has_elite:
        return "ELITE_SMS_ENABLED masih ada di config.py!"
    return True

def test_config_augestel():
    import config
    assert hasattr(config, 'AUGESTEL_ENABLED'), "AUGESTEL_ENABLED tidak ada"
    assert hasattr(config, 'AUGESTEL_URL'), "AUGESTEL_URL tidak ada"
    assert hasattr(config, 'AUGESTEL_API_KEY'), "AUGESTEL_API_KEY tidak ada"
    return True

test("Import config", test_config_import)
test("Config values valid", test_config_values)
test("Elite SMS removed from config", test_config_no_elite)
test("Augestel config present", test_config_augestel)

# 2. IVASMS SCRAPER
print("\n\U0001f4cb [2/10] Testing ivasms_scraper.py...")

def test_ivasms_import():
    from ivasms_scraper import IVASMSClient, get_country_from_phone, mask_phone_number, detect_platform, extract_otp, COUNTRY_FLAGS
    return True

def test_country_detection():
    from ivasms_scraper import get_country_from_phone
    cc, flag = get_country_from_phone("+6281234567890")
    assert cc == "ID", f"Expected ID, got {cc}"
    cc2, flag2 = get_country_from_phone("263799991419")
    assert cc2 == "ZW", f"Expected ZW, got {cc2}"
    return True

def test_mask_phone():
    from ivasms_scraper import mask_phone_number
    result = mask_phone_number("263799991419")
    assert "2637" in result and "1419" in result, f"Masking failed: {result}"
    return True

def test_detect_platform():
    from ivasms_scraper import detect_platform
    p, e = detect_platform("WhatsApp verification code")
    assert p == "WhatsApp", f"Expected WhatsApp, got {p}"
    p2, e2 = detect_platform("Your Telegram code is")
    assert p2 == "Telegram", f"Expected Telegram, got {p2}"
    return True

def test_extract_otp():
    from ivasms_scraper import extract_otp
    otp1 = extract_otp("Your verification code is 385954")
    assert otp1 == "385954", f"Expected 385954, got {otp1}"
    otp2 = extract_otp("Your WhatsApp code: 195-127")
    assert otp2 == "195127", f"Expected 195127, got {otp2}"
    otp3 = extract_otp("Kode OTP Anda: 7823")
    assert otp3 == "7823", f"Expected 7823, got {otp3}"
    return True

test("Import ivasms_scraper", test_ivasms_import)
test("Country detection from phone", test_country_detection)
test("Phone masking", test_mask_phone)
test("Platform detection", test_detect_platform)
test("OTP extraction", test_extract_otp)

# 3. AUGESTEL CLIENT
print("\n\U0001f4cb [3/10] Testing augestel_client.py...")

def test_augestel_import():
    from augestel_client import AugestelClient
    return True

def test_augestel_init():
    from augestel_client import AugestelClient
    client = AugestelClient(api_key="test_key", email="test@test.com")
    assert client.api_key == "test_key"
    assert client.email == "test@test.com"
    assert client.seen_ids == set()
    return True

def test_augestel_cooldown():
    from augestel_client import AugestelClient
    cd = AugestelClient.get_remaining_cooldown()
    assert isinstance(cd, int), f"Expected int, got {type(cd)}"
    return True

test("Import augestel_client", test_augestel_import)
test("AugestelClient initialization", test_augestel_init)
test("Cooldown mechanism", test_augestel_cooldown)

# 4. OTP DEDUP
print("\n\U0001f4cb [4/10] Testing otp_dedup.py...")

def test_dedup_import():
    from otp_dedup import is_duplicate_and_claim, get_dedup_key, normalize_phone_digits, normalize_otp_code, claim_earnings_once
    return True

def test_dedup_normalize():
    from otp_dedup import normalize_phone_digits, normalize_otp_code
    assert normalize_phone_digits("+62 812-3456-7890") == "6281234567890"
    assert normalize_otp_code("385-954") == "385954"
    assert normalize_otp_code("  1234  ") == "1234"
    return True

def test_dedup_key():
    from otp_dedup import get_dedup_key
    k1 = get_dedup_key("+6281234567890", "385954")
    assert k1.startswith("otp_"), f"Expected otp_ prefix, got {k1}"
    k2 = get_dedup_key("+6281234567890", "", "Some random message")
    assert k2.startswith("msg_"), f"Expected msg_ prefix, got {k2}"
    return True

def test_dedup_logic():
    from otp_dedup import is_duplicate_and_claim
    import time
    unique_phone = f"999{int(time.time())}777"
    unique_otp = f"{int(time.time()) % 1000000:06d}"
    is_dup = is_duplicate_and_claim(unique_phone, unique_otp, source="TEST")
    assert is_dup == False, "First claim should return False (fresh)"
    is_dup2 = is_duplicate_and_claim(unique_phone, unique_otp, source="TEST2")
    assert is_dup2 == True, "Second claim should return True (duplicate)"
    return True

test("Import otp_dedup", test_dedup_import)
test("Phone/OTP normalization", test_dedup_normalize)
test("Dedup key generation", test_dedup_key)
test("Dedup claim logic", test_dedup_logic)

# 5. COOKIE SYNC
print("\n\U0001f4cb [5/10] Testing cookie_sync.py...")

def test_cookie_sync_import():
    from cookie_sync import get_fresh_cookies_from_browser
    return True

test("Import cookie_sync", test_cookie_sync_import)

# 6. TELEGRAM FILE SENDER
print("\n\U0001f4cb [6/10] Testing telegram_file_sender.py...")

def test_file_sender_import():
    from telegram_file_sender import (
        get_owner_chat_id, set_owner_chat_id, get_bot_token,
        send_telegram_document, export_and_send_augestel_numbers_txt
    )
    return True

def test_file_sender_config_read():
    from telegram_file_sender import get_bot_token, get_owner_chat_id
    token = get_bot_token()
    assert token, "BOT_TOKEN tidak terbaca dari config"
    return True

test("Import telegram_file_sender", test_file_sender_import)
test("Config read from file_sender", test_file_sender_config_read)

# 7. BOT.PY (Syntax & Import Check)
print("\n\U0001f4cb [7/10] Testing bot.py (syntax & imports)...")

def test_bot_syntax():
    bot_path = os.path.join(PROJECT_DIR, "bot.py")
    with open(bot_path, "r", encoding="utf-8") as f:
        source = f.read()
    compile(source, bot_path, "exec")
    return True

def test_bot_no_elite_refs():
    bot_path = os.path.join(PROJECT_DIR, "bot.py")
    with open(bot_path, "r", encoding="utf-8") as f:
        content = f.read()
    elite_refs = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'elite' in line.lower() and not line.strip().startswith('#'):
            elite_refs.append(f"  Line {i}: {line.strip()}")
    if elite_refs:
        return f"Found Elite refs:\n" + "\n".join(elite_refs)
    return True

def test_bot_import():
    import importlib
    import config
    from ivasms_scraper import IVASMSClient
    from augestel_client import AugestelClient
    from cookie_sync import get_fresh_cookies_from_browser
    from otp_dedup import is_duplicate_and_claim
    from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler
    return True

test("bot.py syntax check", test_bot_syntax)
test("bot.py no Elite SMS references", test_bot_no_elite_refs)
test("bot.py dependency imports", test_bot_import)

# 8. ADMIN SERVER (Syntax & Import Check)
print("\n\U0001f4cb [8/10] Testing admin_server.py (syntax & imports)...")

def test_admin_syntax():
    admin_path = os.path.join(PROJECT_DIR, "admin_server.py")
    with open(admin_path, "r", encoding="utf-8") as f:
        source = f.read()
    compile(source, admin_path, "exec")
    return True

def test_admin_no_elite_refs():
    admin_path = os.path.join(PROJECT_DIR, "admin_server.py")
    with open(admin_path, "r", encoding="utf-8") as f:
        content = f.read()
    elite_refs = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'elite' in line.lower() and not line.strip().startswith('#'):
            elite_refs.append(f"  Line {i}: {line.strip()}")
    if elite_refs:
        return f"Found Elite refs:\n" + "\n".join(elite_refs)
    return True

test("admin_server.py syntax check", test_admin_syntax)
test("admin_server.py no Elite SMS references", test_admin_no_elite_refs)

# 9. AUGESTEL BROWSER POOL
print("\n\U0001f4cb [9/10] Testing augestel_browser_pool.py...")

def test_browser_pool_syntax():
    pool_path = os.path.join(PROJECT_DIR, "augestel_browser_pool.py")
    with open(pool_path, "r", encoding="utf-8") as f:
        source = f.read()
    compile(source, pool_path, "exec")
    return True

test("augestel_browser_pool.py syntax check", test_browser_pool_syntax)

# 10. UTILITY SCRIPTS
print("\n\U0001f4cb [10/10] Testing utility scripts...")

util_scripts = [
    "watchdog.py",
    "git_autopush.py",
    "auto_add_numbers.py",
    "auto_add_augestel.py",
    "numbers_service.py",
    "setup_all_augestel_webhooks.py",
    "sync_all_augestel_numbers.py",
    "login_helper_gui.py",
    "batch_login_augestel.py",
    "get_chat_id.py",
    "detect_group_id.py",
    "check_status.py",
    "set_webhook_single.py",
    "set_webhook_acc1.py",
]

for script in util_scripts:
    def make_test(s):
        def t():
            fpath = os.path.join(PROJECT_DIR, s)
            if not os.path.exists(fpath):
                return f"File not found: {s}"
            with open(fpath, "r", encoding="utf-8") as f:
                source = f.read()
            compile(source, fpath, "exec")
            return True
        return t
    test(f"{script} syntax", make_test(script))

def test_elite_file_deleted():
    fpath = os.path.join(PROJECT_DIR, "elite_sms_client.py")
    if os.path.exists(fpath):
        return "elite_sms_client.py masih ada! Seharusnya sudah dihapus."
    return True

test("elite_sms_client.py deleted", test_elite_file_deleted)

# DATA FILES CHECK
print("\n\U0001f4cb [BONUS] Testing data files...")

def test_augestel_accounts_json():
    import json
    fpath = os.path.join(PROJECT_DIR, "augestel_accounts.json")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list), "Should be a list"
    assert len(data) > 0, "Should have accounts"
    for i, acc in enumerate(data):
        assert "email" in acc, f"Account {i} missing email"
        assert "api_key" in acc, f"Account {i} missing api_key"
    return True

def test_requirements():
    fpath = os.path.join(PROJECT_DIR, "requirements.txt")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    assert "python-telegram-bot" in content, "Missing python-telegram-bot"
    assert "flask" in content, "Missing flask"
    assert "requests" in content, "Missing requests"
    return True

def test_templates_exist():
    assert os.path.exists(os.path.join(PROJECT_DIR, "templates", "admin.html")), "admin.html missing"
    assert os.path.exists(os.path.join(PROJECT_DIR, "templates", "login.html")), "login.html missing"
    return True

test("augestel_accounts.json valid", test_augestel_accounts_json)
test("requirements.txt valid", test_requirements)
test("Templates exist", test_templates_exist)

# RESULTS
print("\n" + "=" * 60)
print(f"\U0001f4ca RESULTS: {passed} passed, {failed} failed, {passed + failed} total")
print("=" * 60)

if errors:
    print("\n\u274c FAILED TESTS DETAIL:")
    for name, tb in errors:
        print(f"\n{'_' * 40}")
        print(f"  Test: {name}")
        print(f"  Error:\n{tb}")

if failed == 0:
    print("\n\U0001f389 ALL TESTS PASSED! Project is clean and working.")
else:
    print(f"\n\u26a0\ufe0f {failed} test(s) need attention. See details above.")
