import json
import re

path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\35d45fd1-15e5-4968-aa0d-e8b840ddc054\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line_idx, line in enumerate(f):
        if line_idx == 107:
            data = json.loads(line)
            content = str(data.get('content', ''))
            print("Content length:", len(content))
            # search for regenerate or delete or generate in content
            for w in ['regenerate', 'delete', 'generate', 'api/key', 'Switchfy/api']:
                matches = [m.start() for m in re.finditer(re.escape(w), content, re.I)]
                print(f"Word '{w}' matches count:", len(matches))
                for m in matches[:5]:
                    print(f"  [{w}]:", content[max(0, m-50):min(len(content), m+150)].replace('\n', ' '))
            break
