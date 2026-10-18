import requests

session = requests.Session()
session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

eval_js = """
async () => {
    try {
        const r = await fetch('/Switchfy/assets/js/baa2ff34e904/clients-live-sms');
        const text = await r.text();
        return {
            text: text.slice(0, 3000)
        };
    } catch(e) {
        return { error: e.toString() };
    }
}
"""

res = session.post("http://localhost:5000/api/augestel/pool/eval/1", json={"script": eval_js})
res_data = res.json().get("result", {}).get("text", "")
print(res_data[:2000])
