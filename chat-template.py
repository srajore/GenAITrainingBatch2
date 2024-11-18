from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import OpenAI

from dotenv import load_dotenv


def main():
  
  load_dotenv(".env",override=True)

  prompt=ChatPromptTemplate.from_template("Tell me key achivments of {name} in 4 bulleted points")

  llm=OpenAI()

  chain=prompt|llm

  response=chain.invoke({"name":"Mahatma Gandhi"})

  print(response)


if __name__=="__main__":
  main()