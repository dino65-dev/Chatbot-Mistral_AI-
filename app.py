# make sure to install `langchain` and `langchain-mistralai` in your Python environment

import os
from langchain_mistralai import ChatMistralAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

# Initialize session state
if 'result' not in st.session_state:
    st.session_state.result = None

# Langchain settings
load_dotenv(".env")
os.environ["LANGCHAIN_PROJECT"] = "mistral_app"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# Initialize the LLM
@st.cache_resource
def initialize_llm():
    api_key = os.getenv("API_KEY")
    mistral_model = "open-mixtral-8x22b"
    return ChatMistralAI(
        model=mistral_model, 
        temperature=0, 
        api_key=api_key,
        token_limit=2000,
        random_seed=0
    )

llm = initialize_llm()
parser = StrOutputParser()

#streamlit framework
st.title("Chatbot(MistralAI)")
input_text = st.text_input("Feel free to ask me anything")

# Only make API call when submit button is pressed
if st.button("Submit") and input_text:
    with st.spinner("Thinking..."):
        output = llm.invoke([("user", input_text)])
        st.session_state.result = parser.invoke(output)

# Display results
if input_text:
    st.write("You said: " + input_text)
if st.session_state.result:
    st.write(st.session_state.result)