import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv('.env')
genai.configure(api_key=os.environ['GENAI_API_KEY'])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def get_model_response(question:str) -> str:
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config
    )
    chat_session = model.start_chat(
        history=[]
    )
    response = chat_session.send_message(question)
    return response.text

st.set_page_config(page_title='Q&A Done')
st.header('smart chatbot project using gemini 2 API')

input = st.text_input('chat', key='chat')
response = get_model_response(f'you are smart and helpful AI please translate to arabic: {input}')
submit = st.button('send')

if submit:
    st.header('Anser:')
    st.write(response)