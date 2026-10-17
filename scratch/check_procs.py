import subprocess

def list_procs():
    try:
        out = subprocess.check_output('wmic process where "name=\'python.exe\'" get ProcessId,CommandLine', shell=True, text=True)
        print("PYTHON PROCESSES:")
        print(out)
    except Exception as e:
        print("Error wmic python:", e)

    try:
        out2 = subprocess.check_output('powershell -Command "(Get-Process msedge -ErrorAction SilentlyContinue).Count"', shell=True, text=True)
        print("MSEDGE PROCESS COUNT:", out2.strip())
    except Exception as e:
        print("Error edge count:", e)

if __name__ == '__main__':
    list_procs()
