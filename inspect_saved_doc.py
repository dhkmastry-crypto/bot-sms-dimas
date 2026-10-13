import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('saved_profile_doc.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("HTML length:", len(text))
# Find generateApiKey, regenerateApiKey, deleteApiKey
for word in ['generateApiKey', 'regenerateApiKey', 'deleteApiKey']:
    for m in re.finditer(re.escape(word), text):
        idx = m.start()
        print(f"=== Found {word} at {idx} ===")
        print(text[max(0, idx-100):min(len(text), idx+600)])
        print("-" * 50)

# Check all script tags
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Total inline scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    if any(w in s for w in ['apiKey', 'generate', 'regenerate', 'api/key', 'liveHistory']):
        print(f"--- Script #{i} snippet ---")
        for line in s.splitlines():
            if any(w in line for w in ['apiKey', 'generate', 'regenerate', 'api/key', 'post', 'ajax', 'fetch']):
                print(" ", line.strip()[:140])
