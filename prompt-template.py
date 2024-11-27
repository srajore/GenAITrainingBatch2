from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI

from dotenv import load_dotenv

import streamlit as st 


def main():

  st.title("Prompt Template Demo !")

  user_input= st.text_input("Please enter your name")
  
  load_dotenv(".env",override=True)

  prompt=PromptTemplate.from_template("Tell me key achivments of {name} in 4 bulleted points")

  llm=OpenAI()

  chain=prompt|llm

  response=chain.invoke({"name": user_input})

  print(response)


if __name__=="__main__":
  main()