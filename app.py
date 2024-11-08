from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(".env")



client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "user",
            "content": "could you please generate a code for me for addition of two numbers in Java while taking the input from the user"
        }
    ]
)

print(completion.choices[0].message.content)