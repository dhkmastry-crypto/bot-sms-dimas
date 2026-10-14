import urllib.request
import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: python bring_account.py <nomor_akun_1_sampai_16>")
        print("Contoh: python bring_account.py 10")
        return

    idx = int(sys.argv[1])
    action = sys.argv[2] if len(sys.argv) > 2 else "show"

    endpoint = f"http://localhost:5000/api/augestel/pool/{action}/{idx}"
    req = urllib.request.Request(
        endpoint,
        headers={"X-Internal-Token": "bot-internal-secret"},
        data=b"{}",
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("=" * 60)
            if data.get("success"):
                print(f"🎉 BERHASIL: {data.get('message')}")
            else:
                print(f"⚠️ PERHATIAN: {data.get('message')}")
            print("=" * 60)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
