import requests
import os
from dotenv import load_dotenv

load_dotenv()

def speech_to_text(file_path):
    url="https://api.deepgram.com/v1/listen?model=nova-3&language=te"

    headers={
        "Authorization":f'Token {os.getenv("DEEPGRAM_API_KEY")}',
        "Content-Type":"audio/wav",
        "Deepgram-Options":"tier=enhanced"
    }

    with open(file_path,"rb") as f:
        audio=f.read()

    res=requests.post(url,headers=headers,data=audio)
    data=res.json()

    print("Deepgram API Response:", data)

    text=data["results"]["channels"][0]["alternatives"][0]["transcript"]
    return text

def normalize_text(text):
    prompt=f"Convert this to proper Telugu meaning (ignore Hindi mistakes): {text}"
    return prompt