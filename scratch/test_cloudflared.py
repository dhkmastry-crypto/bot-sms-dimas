import subprocess
import re
import time
import os

exe = os.path.abspath("cloudflared/cloudflared.exe")
cmd = [exe, "tunnel", "--url", "http://localhost:5000"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

url = None
start = time.time()
while time.time() - start < 15:
    line = p.stdout.readline()
    if not line:
        continue
    print("LOG:", line.strip())
    m = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
    if m:
        url = m.group(0)
        print("FOUND URL:", url)
        break

print("Result URL:", url)
p.terminate()
