import subprocess

def check_edge():
    try:
        out = subprocess.check_output('wmic process where "name=\'msedge.exe\'" get ProcessId,CommandLine', shell=True, text=True)
        lines = [line.strip() for line in out.splitlines() if line.strip()]
        print(f"Total msedge lines: {len(lines)}")
        for l in lines[:10]:
            print(l[:120])
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    check_edge()
