import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

base_url_secure = "https://api-7.whoop.com"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
data = {
    "username": os.getenv('whoop_email'),
    "password": os.getenv('whoop_pswd'),
    "grant_type": "password",
    "issueRefresh": True
    }

response = requests.post('https://api-7.whoop.com/oauth/token', headers=headers, data=json.dumps(data))


print(response.json())