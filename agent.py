import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def get_reply(text):
    res=client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a kirana shop voice assistant in India. The user speaks mixed Telugu + Hindi + slang. Always interpret meaning correctly and respond ONLY in simple Telugu."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return res.choices[0].message.content