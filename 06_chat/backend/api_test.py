import requests

API_URL = "http://127.0.0.1:5000/api/chat"
DATA = {"input_text": "Hello. How are you?"}

# POST
response = requests.post(API_URL, json=DATA)
print(f"\nPOST URL: {response.url}")
print(f"response:\n{response.json()}")
