import subprocess

out = subprocess.check_output('wmic process where "name like \'%edge%\'" get processid,commandline', shell=True, text=True)
found = set()
for line in out.splitlines():
    if "browser_profile_augestel" in line:
        for idx in range(1, 17):
            if f"browser_profile_augestel_{idx} " in line or f"browser_profile_augestel_{idx}\\" in line or f"browser_profile_augestel_{idx}\"" in line:
                found.add(idx)
print(f"Edge active for profiles: {sorted(list(found))}")
