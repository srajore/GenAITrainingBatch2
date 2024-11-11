
#from langchain_community.llms import OpenAI

from langchain_openai import OpenAI


llm=OpenAI(api_key="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",model_name="gpt-3.5-turbo-instruct")

prompt="What is Generative AI ?"

print(llm.invoke(prompt))





