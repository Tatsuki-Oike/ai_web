import requests

API_URL = "http://127.0.0.1:5000/api/segmentation"
FILE = {'image': open('./images/cat.jpg', 'rb')}

# POST
response = requests.post(API_URL, files=FILE)
print(f"\nPOST URL: {response.url}")
print(f"status: {response}")
