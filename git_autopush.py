# ═══════════════════════════════════════════════════════════════
#  AUTO GIT PUSH DAEMON
#  ─────────────────────────────────────────────────────────────
#  Mendeteksi perubahan file kode secara otomatis, melakukan
#  git add, commit timestamp, dan push ke repository GitHub.
# ═══════════════════════════════════════════════════════════════

import os
import sys
import time
import subprocess
import logging
from datetime import datetime

os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ [AUTOPUSH] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("git_autopush")

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# File / folder yang diabaikan dari deteksi perubahan (hanya runtime noise)
IGNORED_PATTERNS = [
    ".git",
    "__pycache__",
    ".log",
    ".session",
    "status.json",
    "ivasms_accounts.json",
    "browser_profile",
    "debug_",
    "test_",
    ".tmp",
]


def check_git_status():
    """Periksa apakah ada perubahan file yang belum ter-commit."""
    try:
        res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=DIR_PATH,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if res.returncode != 0:
            return []
        
        lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]
        relevant_changes = []
        for line in lines:
            # line format: " M path/to/file" or "?? newfile"
            file_part = line[2:].strip().replace('"', '')
            if any(ign in file_part for ign in IGNORED_PATTERNS):
                continue
            relevant_changes.append(file_part)
        return relevant_changes
    except Exception as e:
        logger.error(f"Error checking git status: {e}")
        return []


def push_changes(changed_files):
    """Lakukan git add, commit, dan push."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = ", ".join(changed_files[:3])
    if len(changed_files) > 3:
        summary += f" (+{len(changed_files) - 3} lainnya)"
    
    commit_msg = f"auto-update: {summary} [{timestamp}]"
    logger.info(f"🚀 Perubahan terdeteksi: {len(changed_files)} file ({summary})")
    logger.info(f"📝 Melakukan git commit: '{commit_msg}'...")

    try:
        # 1. Git Add
        add_res = subprocess.run(["git", "add", "-A"], cwd=DIR_PATH, capture_output=True, text=True, timeout=15)
        if add_res.returncode != 0:
            logger.error(f"❌ Git add failed: {add_res.stderr.strip()}")
            return False

        # 2. Git Commit
        commit_res = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=DIR_PATH,
            capture_output=True,
            text=True,
            timeout=15,
        )
        if commit_res.returncode != 0:
            # Tidak ada perubahan atau gagal
            logger.warning(f"⚠️ Commit returned: {commit_res.stdout.strip() or commit_res.stderr.strip()}")
            return False

        logger.info("✅ Commit berhasil.")

        # 3. Git Push
        logger.info("📤 Mendorong (push) ke GitHub origin main...")
        push_res = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=DIR_PATH,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if push_res.returncode == 0:
            logger.info("🎉 Berhasil auto-push ke GitHub!")
            return True
        else:
            logger.error(f"❌ Git push failed: {push_res.stderr.strip()}")
            return False

    except Exception as e:
        logger.error(f"❌ Exception saat auto-push: {e}")
        return False


def run_watcher(check_interval=15, debounce_seconds=5):
    """Loop memantau perubahan file."""
    logger.info("👀 Auto Push Daemon berjalan (Interval cek: %ds)...", check_interval)
    last_detected_time = 0
    pending_files = []

    while True:
        try:
            changed = check_git_status()
            if changed:
                now = time.time()
                # Jika baru pertama kali terdeteksi atau ada perubahan baru
                if not pending_files:
                    logger.info("🔍 Menemukan perubahan kode, menunggu stabil (%ds debounce)...", debounce_seconds)
                    last_detected_time = now
                    pending_files = changed
                else:
                    pending_files = list(set(pending_files + changed))

                # Jika sudah melewati debounce delay
                if now - last_detected_time >= debounce_seconds:
                    push_changes(pending_files)
                    pending_files = []
                    last_detected_time = 0
            else:
                pending_files = []

            time.sleep(check_interval)

        except KeyboardInterrupt:
            logger.info("🛑 Auto Push Daemon dihentikan.")
            break
        except Exception as e:
            logger.error(f"Error loop: {e}")
            time.sleep(check_interval)


if __name__ == "__main__":
    interval = 15
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except Exception:
            pass
    run_watcher(check_interval=interval)
