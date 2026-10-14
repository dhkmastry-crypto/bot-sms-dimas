import sqlite3
import os
import shutil

cookie_file = os.path.abspath('browser_profile_augestel_1/Default/Network/Cookies')
if os.path.exists(cookie_file):
    shutil.copyfile(cookie_file, 'scratch/temp_cookies.db')
    conn = sqlite3.connect('scratch/temp_cookies.db')
    cur = conn.cursor()
    cur.execute("SELECT host_key, name, path, expires_utc FROM cookies WHERE host_key LIKE '%augestel%'")
    rows = cur.fetchall()
    print('Cookies for augestel in profile 1:')
    for r in rows:
        print(' ', r)
    conn.close()
    try:
        os.remove('scratch/temp_cookies.db')
    except Exception:
        pass
else:
    print('Cookie file not found at:', cookie_file)
