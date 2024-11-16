# make sure to install `langchain` and `langchain-mistralai` in your Python environment

import os
from langchain_mistralai import ChatMistralAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
# Langchain settings
load_dotenv(".env")
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "app"

# Initialize the LLM
api_key = os.getenv("API_KEY")
mistral_model = "open-mixtral-8x22b"
llm = ChatMistralAI(model=mistral_model, temperature=0, api_key=api_key,token_limit=2000,random_seed=0)


#sreamlit framework
st.title("Chatbot(MistralAI)")
input_text = st.text_input("Feel free to ask me anything")
output = llm.invoke([("user", input_text)])

# parse the output
parser = StrOutputParser()
result = parser.invoke((output))

# output
st.write(result)