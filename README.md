# Local LLM Chat Application

A lightweight, locally-run chat application powered by Llama 3, integrated with Ollama, and featuring a clean, Grok-inspired interface built with Streamlit. This app allows you to interact with an AI assistant directly on your machine—no internet required after setup.

## Features
- **Local Execution**: Runs Llama 3 entirely on your computer using Ollama.
- **Grok-like Interface**: Minimalistic, conversational design with rounded message bubbles and a modern layout.
- **Chat History**: Persists during the session, displaying user and assistant messages.
- **File Upload**: Supports uploading and analyzing text files (.txt, .md, .pdf).
- **Customizable**: Easily tweak the model, tone, or styling to suit your needs.

## Dependencies
This project relies on the following software and Python packages:

### Software
- **Python**: Version 3.10 or higher ([Download](https://www.python.org/downloads/)).
- **Ollama**: For running Llama 3 locally ([Download](https://ollama.com/)).
- **Git**: Optional, for cloning the repository ([Download](https://git-scm.com/)).

### Python Packages
- **streamlit**: Web interface framework (`pip install streamlit`).
- **ollama**: Python client for Ollama (`pip install ollama`).
- **PyPDF2**: For extracting text from PDF files (`pip install PyPDF2`).

### Hardware Requirements
- **Minimum**: 8GB RAM, 5GB free disk space (for Llama 3 8B model).
- **Recommended**: 16GB+ RAM, GPU with CUDA support for faster inference.
## Set Up

Prepare your environment and project structure with these steps:

1. **Clone the Repository** (or create manually):
   ```bash
   git clone https://github.com/jlpnunes/llm-local-app.git
   cd llm-local-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Ollama**
   ```bash
   ollama --version
   ```

4. **Install Python Packages**
   ```bash
   pip install streamlit ollama
   ```

   ***Confirm instalation***
   ```bash
   pip list | grep -E "streamlit|ollama"
   ```

5. **Download the Llama 3 Model**
   ```bash
   ollama pull llama3:8b
   ```

6. **Start**

   ***Start the Ollama Server: Open a terminal and run***
   ```bash
   ollama serve
   ```

   ***Run the Application: In your project directory (with the virtual environment activated)***

   ```bash
   streamlit run app.py
   ```

   - A browser will open at http://localhost:8501.
   - If the port is in use, Streamlit will suggest an alternative (e.g., http://localhost:8502).

## Troubleshooting
- App Crashes: Check RAM usage (8GB min for 8B model). Close other apps or use a smaller model.
- No Response: Ensure the Ollama server is running (ollama serve).
- Slow Performance: Speed depends on your CPU/GPU. Enable GPU support in Ollama if available (see Ollama docs).
- Dependency Errors: Re-run pip install streamlit ollama or verify Python version compatibility.