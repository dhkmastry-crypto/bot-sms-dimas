import requests
import json

session = requests.Session()
session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

eval_js = """
async () => {
    try {
        const r = await fetch('/Switchfy/client/live-sms', {
            headers: { 'Accept': 'text/html' }
        });
        const text = await r.text();
        
        // Find all URLs mentioned in the HTML / JS
        const matches = text.match(/\/Switchfy\/[a-zA-Z0-9_\-\/]+/g) || [];
        const unique = Array.from(new Set(matches));
        
        // Find all script tags content
        const parser = new DOMParser();
        const doc = parser.parseFromString(text, 'text/html');
        const scriptTexts = Array.from(doc.querySelectorAll('script')).map(s => s.innerText).filter(t => t.length > 50);
        
        return {
            endpoints: unique,
            scriptSnippets: scriptTexts.map(s => s.slice(0, 500))
        };
    } catch(e) {
        return { error: e.toString() };
    }
}
"""

res = session.post("http://localhost:5000/api/augestel/pool/eval/1", json={"script": eval_js})
print(json.dumps(res.json(), indent=2))
