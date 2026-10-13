import cloudscraper

scraper = cloudscraper.create_scraper()
res = scraper.post("https://augestel.com/Switchfy/login", data={"email": "test", "password": "test"})
print("Status:", res.status_code)
print("Retry-After:", res.headers.get("Retry-After"))
