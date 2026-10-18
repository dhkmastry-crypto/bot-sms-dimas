import subprocess

try:
    out = subprocess.check_output('wmic process where "name=\'python.exe\'" get ProcessId,CommandLine', shell=True).decode('utf-8', 'ignore')
    for line in out.splitlines():
        if line.strip() and "CommandLine" not in line:
            print(line.strip())
except Exception as e:
    print("Error:", e)
