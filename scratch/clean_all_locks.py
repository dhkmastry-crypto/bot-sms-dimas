import os
import glob

base_dir = r"c:\Users\ADMIN\Downloads\OTP IVA SMS"
lock_names = ["lockfile", "SingletonLock", "SingletonSocket", "SingletonCookie"]

deleted = []
errors = []

for prof_dir in glob.glob(os.path.join(base_dir, "browser_profile_*")):
    if os.path.isdir(prof_dir):
        for name in lock_names:
            p = os.path.join(prof_dir, name)
            if os.path.exists(p):
                try:
                    os.remove(p)
                    deleted.append(p)
                except Exception as e:
                    errors.append((p, str(e)))

print(f"Deleted {len(deleted)} lock files.")
if deleted:
    for d in deleted[:10]:
        print("  Deleted:", d)
if errors:
    print(f"Errors deleting {len(errors)} locks:")
    for err in errors:
        print("  Error:", err)
