import streamlit as st
import google.generativeai as genai
# from dotenv import load_dotenv  
# import pathlib
# import os


def get_answer(query):
    secret_api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=secret_api_key)    
    # env_path = pathlib.Path('.') / '.local.env'
    # load_dotenv(dotenv_path=env_path)
    # GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    # genai.configure(api_key=GOOGLE_API_KEY)

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)

    return response.text


def main():
    st.set_page_config(page_title="GeminiUse", page_icon="📖", layout = 'wide',)
    st.header("Google Gemini")
    st.sidebar.title("Gemini")
    with st.sidebar:
        with open('sidebar.txt') as fb:
            text = fb.read()
        st.write(text)
    query = st.text_input("Enter your query here")
    if query:
        answer = get_answer(query)
        st.write(answer)

if __name__ == "__main__":
    main()