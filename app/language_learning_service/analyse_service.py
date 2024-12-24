import os
from openai import OpenAI

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(base_url="https://api.x.ai/v1", api_key=XAI_API_KEY)

prompt = ("I need to identify news to know if its a terror attack or not. I need the info to come back in the same structure every time including city, country,"
          "perpetrator, date, description, attack weapon, total wounded and total killed. and start the message with TERROR and then the schema without extra words"
          "for unknown info the value should be Unknown or -1, date format = yyyy-MM-dd"
          " if not just send me back FALSE")


def analyze_news(text: str):
    completion = client.chat.completions.create(
    model="grok-2-1212",
    messages=[
        {
            "role": "system",
            "content": prompt,
        },
        {
            "role": "user",
            "content": text,
        },
    ],
)
    if completion.usage:
        return completion.choices[0].message.content
    else:
        print("Something went wrong.")