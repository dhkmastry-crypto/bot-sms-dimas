import os

log_path = "bot.log"
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    clean_lines = [l for l in lines if "│ werkzeug │" not in l and "Browser/Cookie Guardian" not in l]
    removed = len(lines) - len(clean_lines)
    
    with open(log_path, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)
        
    print(f"Cleaned {removed} spam lines from bot.log! Remaining lines: {len(clean_lines)}")
