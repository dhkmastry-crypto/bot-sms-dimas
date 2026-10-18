import subprocess
import json

ps_cmd = 'Get-CimInstance Win32_Process -Filter "Name = \'msedge.exe\'" | Select-Object ProcessId, ParentProcessId, CommandLine | ConvertTo-Json'
out = subprocess.check_output(["powershell", "-NoProfile", "-Command", ps_cmd], text=True)
data = json.loads(out)
if isinstance(data, dict):
    data = [data]
for d in data[:15]:
    ppid = d.get('ParentProcessId')
    pid = d.get('ProcessId')
    cl = d.get('CommandLine') or ''
    # Find parent name
    pname = ""
    try:
        p_out = subprocess.check_output(["powershell", "-NoProfile", "-Command", f'(Get-Process -Id {ppid} -ErrorAction SilentlyContinue).ProcessName'], text=True).strip()
        pname = p_out
    except Exception:
        pass
    print(f"Edge PID {pid} -> Parent {ppid} ({pname}): {cl[:90]}")
