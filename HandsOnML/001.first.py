# Get Keys : dotenv
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": "당신은 유능한 비서입니다."},
        {"role": "user", "content": "50대의 남성에게 저녁 12시가 다되어 가는데 적절한 칵테일을 추천해줘"},
    ],
)