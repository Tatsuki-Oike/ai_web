import requests

API_URL = "http://127.0.0.1:5000/api/image_generation"
DATA = {
        "prompt": "a cute magical flying robot, fantasy art drawn, high quality, highly detailed",
        "steps": 3,
        "size": 256,
    }

# POST
response = requests.post(API_URL, json=DATA)
print(f"\nPOST URL: {response.url}")
print(f"status: {response}")
