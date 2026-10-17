import requests
import json

session = requests.Session()
session.post("http://localhost:5000/login", data={"username": "admin", "password": "admin123"})

# Let's inspect via an ad-hoc test script running in python
# Wait, can we import get_browser_pool? No, get_browser_pool is inside admin_server process.
# But admin_server has python routes!
