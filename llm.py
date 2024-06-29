import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

def generate_response(prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
    )
    response = chat_completion.to_dict()
    return response["choices"][0]["message"]["content"]