from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(".env",override=True)

openai_client=OpenAI()

available_models=openai_client.models.list()

print(available_models)

