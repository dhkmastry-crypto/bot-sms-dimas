import json

path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\35d45fd1-15e5-4968-aa0d-e8b840ddc054\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line_idx, line in enumerate(f):
        if 'Script attrs:' in line:
            data = json.loads(line)
            content = str(data.get('content', ''))
            print(f"Step {data.get('step_index')}:")
            print(content)
            print("="*60)
