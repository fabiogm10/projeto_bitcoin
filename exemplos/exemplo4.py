import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual a capital da frança?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

