import requests

API_URL = "http://127.0.0.1:5000/api/translation"
DATA = {"input_text": "こんにちは、元気ですか？"}

# POST
response = requests.post(API_URL, json=DATA)
print(f"\nPOST URL: {response.url}")
print(f"response:\n{response.json()}")
