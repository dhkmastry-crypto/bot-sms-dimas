import subprocess
import glob
import os
import sys

def kill_augestel_edges():
    cmd = '''Get-CimInstance Win32_Process | Where-Object { $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel*" } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }'''
    p = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True)
    print("PowerShell output:", p.stdout, p.stderr)

def clean_locks():
    base_dir = r"c:\Users\ADMIN\Downloads\OTP IVA SMS"
    lock_names = ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]
    cnt = 0
    for prof_dir in glob.glob(os.path.join(base_dir, "browser_profile_*")):
        if os.path.isdir(prof_dir):
            for name in lock_names:
                lk = os.path.join(prof_dir, name)
                if os.path.exists(lk):
                    try:
                        os.remove(lk)
                        cnt += 1
                    except Exception:
                        pass
    print(f"Cleaned {cnt} lock files.")

if __name__ == "__main__":
    kill_augestel_edges()
    import time
    time.sleep(2)
    clean_locks()
    # Check remaining
    cmd_check = '''(Get-CimInstance Win32_Process | Where-Object { $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel*" }).Count'''
    p_chk = subprocess.run(["powershell", "-NoProfile", "-Command", cmd_check], capture_output=True, text=True)
    print("Remaining augestel msedge processes:", p_chk.stdout.strip())
