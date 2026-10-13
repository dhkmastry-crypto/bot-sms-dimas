import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\35d45fd1-15e5-4968-aa0d-e8b840ddc054\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line_idx, line in enumerate(f):
        if line_idx == 107:
            data = json.loads(line)
            print("Step 107 type:", data.get('type'))
            print("Step 107 tool_calls:", data.get('tool_calls'))
            print("Step 107 content preview:\n", str(data.get('content'))[:1000])
        elif line_idx == 106:
            data = json.loads(line)
            print("Step 106 type:", data.get('type'))
            print("Step 106 tool_calls:", data.get('tool_calls'))
