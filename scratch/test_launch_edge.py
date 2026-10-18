import os
import subprocess
import time

BASE_DIR = r"C:\Users\ADMIN\Downloads\OTP IVA SMS"
idx = 1
prof_dir = os.path.join(BASE_DIR, f"browser_profile_augestel_{idx}")
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Kill any processes locking this profile
cmd_kill = (
    f'Get-CimInstance Win32_Process | '
    f'Where-Object {{ $_.Name -eq "msedge.exe" -and $_.CommandLine -like "*browser_profile_augestel_{idx}*" }} | '
    f'ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}'
)
subprocess.run(["powershell", "-NoProfile", "-Command", cmd_kill], capture_output=True)

for lk in ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]:
    p = os.path.join(prof_dir, lk)
    if os.path.exists(p):
        try:
            os.remove(p)
        except Exception:
            pass

cmd = [
    "cmd.exe", "/c", "start", '""',
    edge_exe,
    f'--user-data-dir="{prof_dir}"',
    "--window-position=100,80",
    "--window-size=1280,850",
    "--no-first-run",
    "--no-default-browser-check",
    "https://augestel.com/Switchfy/client/numbers"
]

subprocess.Popen(cmd)
print("Launched Edge via start!")
