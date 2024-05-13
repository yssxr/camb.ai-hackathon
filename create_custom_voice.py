import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

files = {'file': open('enhanced_timotee.wav', 'rb')}
data = {
    'voice_name': 'Paul',
    'gender': 1,
    'age': 30
}
response = requests.post(
    "https://client.camb.ai/apis/create_custom_voice",
    files=files,
    data=data,
    headers={
        "x-api-key": API_KEY
    }
)
print(response.json())