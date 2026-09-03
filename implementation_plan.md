# Study Abroad AI Assistant

## Project Description

Study Abroad AI Assistant is a small AI application that helps students ask common questions about studying abroad.

The user enters a question, and the application uses an open-source Large Language Model (LLM) through Ollama to generate a response.

The first version will focus on general study-abroad questions about countries such as the USA, Canada, UK, Australia, and other countries.

## Problem

Students often have questions about studying abroad, such as:

- Study destinations
- Tuition costs
- Scholarships
- Student visas
- Required documents
- Work opportunities
- Application processes

Finding and understanding this information can be difficult.

This application provides a simple way for students to ask questions and receive an AI-generated response.

## Features

- Ask study-abroad questions
- Generate AI responses
- Simple Streamlit interface
- Uses an open-source LLM
- Runs locally with Ollama
- Basic error handling

## Technologies

- Python
- Ollama
- Open-source LLM
- Streamlit
- uv
- Git
- GitHub

## How It Works

User
→ Streamlit
→ Python
→ Prompt
→ Ollama
→ Open-source LLM
→ AI Response
→ User

## Installation

1. Install Python.
2. Install uv.
3. Install Ollama.
4. Download a suitable open-source LLM.
5. Clone this GitHub repository.
6. Install the project dependencies.

## Run the Application

Run the Streamlit application from the terminal.

The exact command will be added after the application is completed.

## Example Questions

- What is an F-1 visa?
- What are some popular countries for international students?
- What documents may students need when applying to study abroad?
- Can international students work while studying?
- What are some common scholarship options?

## Limitations

This application provides general AI-generated information.

It is not an official government, university, immigration, or legal service.

Users should verify important information with official sources.

## Testing

The application will be tested using realistic study-abroad questions.

Testing will also include:

- Empty input
- Invalid input
- Ollama unavailable
- LLM model unavailable
- Normal questions

## Future Improvements

After the MVP is working, possible improvements may include:

- RAG
- PDF document Q&A
- ChromaDB or FAISS
- Conversation memory
- More study-abroad information

These features are optional.

## Project Status

CAP 942 Capstone Project

Current stage:

Implementation planning and project setup.

## Author

Seraj Ali







study-abroad-ai-assistant/
│
├── .env
├── .gitignore
├── .venv/
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
├── implementation_plan.md   
└── uv.lock


### **<! # 1. Initialize Git
git init

# 2. Check Git status
git status

# 3. Add all project files
git add .

# 4. Check what will be committed
git status

# 5. Create your first commit
git commit -m "Initial CAP 942 project setup"

# 6. Connect local project to GitHub
git remote add origin https://github.com/serajstudy/Module-942---Capstone-AI-Solutions-Developer.git

# 7. Check the GitHub connection
git remote -v

# 8. Push your project to GitHub
git push -u origin master

#  After you make changes later


# Use this simple command cycle:

git add .

git commit -m "Initial CAP 942 project setup"

git push -u origin master



 >**

