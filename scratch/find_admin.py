import subprocess

out = subprocess.check_output('wmic process where "name like \'%python%\'" get processid,commandline', shell=True, text=True)
for line in out.splitlines():
    if "admin_server.py" in line:
        parts = line.strip().split()
        pid = parts[-1]
        print(f"Admin Server PID: {pid}")
