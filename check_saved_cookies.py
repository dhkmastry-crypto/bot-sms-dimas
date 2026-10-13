import sqlite3
import os

p = os.path.join("browser_profile_augestel_test", "Default", "Network", "Cookies")
if os.path.exists(p):
    conn = sqlite3.connect(p)
    c = conn.cursor()
    c.execute("SELECT host_key, name FROM cookies WHERE host_key LIKE '%augestel%'")
    rows = c.fetchall()
    print("Cookies in browser_profile_augestel_test:", len(rows))
    for r in rows:
        print(" ", r[0], r[1])
    conn.close()
else:
    print("Path not found:", p)
