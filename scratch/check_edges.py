import subprocess
import re

try:
    cmd = ["powershell", "-NoProfile", "-Command", "Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'msedge.exe' } | Select-Object ProcessId, CommandLine | ConvertTo-Json"]
    out = subprocess.check_output(cmd, text=True, errors='replace')
    import json
    data = json.loads(out)
    if isinstance(data, dict):
        data = [data]
    print(f"Total msedge processes: {len(data)}")
    augestel_procs = []
    other_procs = []
    for p in data:
        cl = p.get("CommandLine") or ""
        m = re.search(r"browser_profile_augestel_(\d+)", cl)
        if m:
            augestel_procs.append((p.get("ProcessId"), m.group(0)))
        else:
            other_procs.append((p.get("ProcessId"), cl[:60]))
    print(f"Augestel msedge processes: {len(augestel_procs)}")
    print(f"Other msedge processes: {len(other_procs)}")
    profiles = sorted(list(set(x[1] for x in augestel_procs)))
    print(f"Active profiles: {profiles}")
except Exception as e:
    print(f"Error: {e}")
