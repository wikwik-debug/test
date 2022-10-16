import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")

header = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

r = requests.get("https://api.spotify.com/v1/users/ozigk9d0w2wxro185kog2sqgy", headers=header)


data = r.json()

for key, value in data.items():
    print(f"{key}: {value}")