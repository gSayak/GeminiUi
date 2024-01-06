import streamlit as st
import google.generativeai as genai
# from dotenv import load_dotenv  
# import pathlib
# import os


def get_answer(query):
    secret_api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=secret_api_key)    
    result_container = st.empty()

    error = """
    # The execution was blocked due to safety concerns regarding the prompt.

    """
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    result_container.text("Generating content...")
    
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content(query)
    except Exception as e:
        result_container.error(f"Error: {e}")
        st.write(error)
    with result_container:
        st.write(response.text)


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
        get_answer(query)

if __name__ == "__main__":
    main()