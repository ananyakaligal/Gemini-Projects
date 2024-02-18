# Q&A Chatbot
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## Initialize our Streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input_text = st.text_input("Input: ", key="input")

submit_button = st.button("Ask the question")

## If the ask button is clicked
if submit_button:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.write("_" * 80)
    
    st.write(chat.history)
