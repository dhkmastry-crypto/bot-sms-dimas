import os
import shutil
import sqlite3

def check(name, path):
    full_path = os.path.expandvars(path)
    if not os.path.exists(full_path):
        print(f"{name}: Not found")
        return
    temp = f"temp_{name}.sqlite"
    shutil.copy2(full_path, temp)
    conn = sqlite3.connect(temp)
    c = conn.cursor()
    c.execute("SELECT host_key, name FROM cookies WHERE host_key LIKE '%augestel%'")
    rows = c.fetchall()
    print(f"{name} Augestel cookies:", rows)
    conn.close()
    if os.path.exists(temp):
        os.remove(temp)

check("Edge", r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Network\Cookies")
check("Chrome", r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies")
