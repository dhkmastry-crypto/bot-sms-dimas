import subprocess

out = subprocess.check_output(['wmic', 'process', 'get', 'ProcessId,CommandLine']).decode('utf-8', errors='ignore')
for line in out.splitlines():
    if 'admin_server.py' in line or 'watchdog.py' in line:
        print(line.strip())
