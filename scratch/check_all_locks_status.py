import os
import glob

base = r"c:\Users\ADMIN\Downloads\OTP IVA SMS"
locked = []
free = []

for idx in range(1, 35):
    prof = os.path.join(base, f"browser_profile_augestel_{idx}")
    lk = os.path.join(prof, "lockfile")
    if os.path.exists(lk):
        try:
            os.remove(lk)
            free.append(idx)
        except Exception:
            locked.append(idx)
    else:
        free.append(idx)

print(f"Total free profiles: {len(free)}")
print(f"Total locked profiles: {len(locked)} -> {locked}")
