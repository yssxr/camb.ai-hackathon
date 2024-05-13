import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")


BASE_URL = "https://client.camb.ai"

headers = {
    "Accept": "application/json",
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# characters = [{"name": "Chani", "id": 9014, "text": "Hi! I am Chani from Dune and welcome to CAMB AI Hackathon!"}, {"name": "Paul", "id": 9015, "text": "Hi! I am Paul from Dune and welcome to CAMB AI Hackathon!"}]
# characters = [{"name": "Logan", "id": 8777, "text": "Her memory held catalogs of names and cross-indexed details. She could rattle off the major weakness of every known enemy, the potential dispositions of opposing forces, battle plans of their military leaders, the tooling and production capacities of basic industries."},
#               {"name": "Paul", "id": 9028, "text": "Why now?"}]
characters = [{"name": "Logan", "id": 8777, "text": "Paul Wondered"}]

for character in characters:
    url = "https://client.camb.ai/apis/tts"
    payload = {
        "text": character["text"],
        "voice_id": character["id"],  # voice_id
        "language": 1,  
        "gender": 1,    
        "age": 0        
    }
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    task_id = response_data['task_id']
    print("task_id: ", task_id)

    while True:

        url = "https://client.camb.ai/apis/tts/"+task_id

        response = requests.request("GET", url, headers=headers)
        status = response.json()["status"]
        print(f"Polling: {status}")
        time.sleep(5)
        if status == "SUCCESS":
            run_id = response.json()["run_id"]
            break

    print(f"Run ID: {run_id}")
    url = f"https://client.camb.ai/apis/tts_result/{run_id}"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    with open("saved_stream"+str(character["id"])+".wav", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

