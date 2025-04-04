import streamlit as st
import ollama
import PyPDF2
import os

# Set up the model
MODEL = "llama3:8b"

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your local AI assistant, running Llama 3. How can I help you today? You can type a message or upload a text file (e.g., .txt, .md, .pdf) to analyze."}
    ]

# Streamlit page configuration
st.set_page_config(page_title="Local LLM Chat", page_icon="🤖", layout="wide")

# Custom CSS to mimic Grok's clean, modern look
st.markdown("""
    <style>
    .main {background-color: #f5f5f5; padding: 20px;}
    .stTextInput > div > div > input {border-radius: 10px; padding: 10px;}
    .message {padding: 10px; margin: 5px; border-radius: 10px;}
    .user {background-color: #e0f7fa; text-align: right;}
    .assistant {background-color: #ffffff; text-align: left;}
    </style>
""", unsafe_allow_html=True)

# Display chat history
st.title("Local Chat with Llama 3")
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f'<div class="message user">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message assistant">{message["content"]}</div>', unsafe_allow_html=True)

# Input form with file upload
with st.form(key="input_form", clear_on_submit=True):
    user_input = st.text_input("Ask me anything:", key="user_input")
    uploaded_file = st.file_uploader("Or upload a file (.txt, .md, .pdf):", type=["txt", "md", "pdf"])
    submit_button = st.form_submit_button(label="Send")

# Function to extract text from uploaded file
def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    else:  # .txt or .md
        return file.read().decode("utf-8")

# Process user input or uploaded file
if submit_button:
    if uploaded_file:
        # Handle file upload
        file_content = extract_text_from_file(uploaded_file)
        st.session_state.messages.append({"role": "user", "content": f"Uploaded file: {uploaded_file.name}\nContent:\n{file_content}"})
        
        # Generate response from Llama 3 based on file content
        with st.spinner("Analyzing file..."):
            response = ollama.chat(
                model=MODEL,
                messages=[{"role": "user", "content": f"Analyze this file content:\n{file_content}"}]
            )
            assistant_response = response["message"]["content"]
        
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.rerun()

    elif user_input:
        # Handle text input
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate response from Llama 3
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model=MODEL,
                messages=[{"role": "user", "content": user_input}]
            )
            assistant_response = response["message"]["content"]
        
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.rerun()

# Footer
st.markdown("---")
st.write("Powered by Llama 3 via Ollama | Running locally on your machine")