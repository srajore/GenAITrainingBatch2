
#from langchain_community.llms import OpenAI

from langchain_openai import OpenAI


llm=OpenAI(api_key="",model_name="gpt-3.5-turbo-instruct") 

prompt="What is Generative AI ?"

print(llm.invoke(prompt))





