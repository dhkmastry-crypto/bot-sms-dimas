import json

path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\35d45fd1-15e5-4968-aa0d-e8b840ddc054\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line_idx, line in enumerate(f):
        if line_idx == 1276:
            data = json.loads(line)
            content = str(data.get('content', ''))
            idx = content.find('regenerateApiKey()')
            if idx != -1:
                print(content[idx:idx+4000])
            break
