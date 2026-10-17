import subprocess

def check_all_msedge():
    out = subprocess.check_output('wmic process where "name=\'msedge.exe\'" get ProcessId,CommandLine', shell=True, text=True)
    lines = [l.strip() for l in out.splitlines() if l.strip() and not l.startswith("CommandLine")]
    personal = []
    bot_edge = []
    other = []
    for l in lines:
        if "browser_profile_augestel" in l or "browser_profile_ivasms" in l or "OTP IVA SMS" in l:
            bot_edge.append(l)
        elif "edge" in l.lower():
            personal.append(l)
        else:
            other.append(l)
            
    print(f"Total msedge processes: {len(lines)}")
    print(f"Bot/OTP SMS Edge processes: {len(bot_edge)}")
    print(f"Other Edge processes: {len(personal)}")
    if personal:
        for p in personal[:5]:
            print("Personal Edge sample:", p[:100])

if __name__ == '__main__':
    check_all_msedge()
