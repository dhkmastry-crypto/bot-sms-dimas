import subprocess
import json

for name in ['node.exe', 'msedge.exe', 'chrome.exe']:
    try:
        ps_cmd = f"Get-CimInstance Win32_Process -Filter \"Name = '{name}'\" | Select-Object ProcessId, CommandLine | ConvertTo-Json"
        out = subprocess.check_output(["powershell", "-NoProfile", "-Command", ps_cmd], text=True)
        data = json.loads(out)
        if isinstance(data, dict):
            data = [data]
        print(f"=== {name} ({len(data)}) ===")
        for d in data:
            cl = d.get('CommandLine') or ''
            print(f"  PID {d.get('ProcessId')}: {cl[:100]}")
    except Exception as e:
        print(f"=== {name} (0 or err): {e}")
