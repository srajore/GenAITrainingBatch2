from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI

from dotenv import load_dotenv


def main():
  
  load_dotenv(".env",override=True)

  prompt=PromptTemplate.from_template("Tell me key achivments of {name} in 4 bulleted points")

  llm=OpenAI()

  chain=prompt|llm

  response=chain.invoke({"name":"Rohit Sharma"})

  print(response)


if __name__=="__main__":
  main()