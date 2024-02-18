from dotenv import load_dotenv
load_dotenv()  # loading all the environmental variables

import streamlit as st
from os import getenv  # Importing the getenv function from the os module
import google.generativeai as genai

genai.configure(api_key=getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get response

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="Q&A DEMO") 
st.header('Ask me anything')
input_text = st.text_input("Input: ", key="input")

submit_button = st.button("Generate")

# When submit is clicked
if submit_button:
    response_text = get_gemini_response(input_text)
    st.subheader("The response is")
    st.write(response_text)
