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
        const parser = new DOMParser();
        const doc = parser.parseFromString(text, 'text/html');
        
        // Find scripts, datatables, websockets, or endpoints
        const scripts = Array.from(doc.querySelectorAll('script')).map(s => s.src || s.innerText.slice(0, 300));
        const tables = Array.from(doc.querySelectorAll('table')).map(t => ({ id: t.id, class: t.className }));
        
        return {
            status: r.status,
            url: r.url,
            title: doc.title,
            tables: tables,
            scripts: scripts.slice(0, 10),
            sampleText: doc.body ? doc.body.innerText.slice(0, 500) : ""
        };
    } catch(e) {
        return { error: e.toString() };
    }
}
"""

res = session.post("http://localhost:5000/api/augestel/pool/eval/1", json={"script": eval_js})
print(json.dumps(res.json(), indent=2))
