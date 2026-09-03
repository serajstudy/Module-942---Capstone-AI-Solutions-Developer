# CAP 942 Implementation Plan

# Study Abroad AI Assistant

## 1. Project Title

Study Abroad AI Assistant

---

## 2. Project Summary

Study Abroad AI Assistant is a small AI application that helps students ask common questions about studying abroad.

The application will accept a student's question and use an open-source Large Language Model (LLM) running locally through Ollama to generate a helpful response.

The first version will focus on simple questions about studying in the USA, Canada, UK, and Australia.

### Value Proposition

The application gives students a simple place to ask study-abroad questions and receive an AI-generated response.

---

# 3. Problem Statement

Students who want to study abroad have many questions about:

- Countries
- Universities
- Tuition fees
- Living costs
- Student visas
- Scholarships
- Work opportunities
- Required documents
- Post-graduation options
- Consultancy services

Finding and understanding this information can be difficult and time-consuming.

The Study Abroad AI Assistant will provide a simple conversational interface where students can ask questions and receive an AI-generated answer.

### Intended Users

The application is intended for:

- International students
- Students planning to study abroad
- Students comparing countries
- Students researching universities
- Students learning about the application process

---

# 4. CAP 942 Requirement Alignment

| CAP 942 Requirement | How This Project Meets It | Evidence |
|---|---|---|
| Use one open-source LLM | Use an open-source LLM through Ollama | Working LLM response |
| Accept user input | Student enters a question in Streamlit | Question input box |
| Produce LLM-generated output | Ollama sends the question to the LLM | AI-generated answer |
| Run as an application | Use a Streamlit web application | Running Streamlit app |
| Prompt engineering | Create instructions for the LLM | Prompt template |
| End-to-end functionality | User question goes through the application and produces an answer | Live demonstration |
| Documentation | Create README and project documentation | Documentation files |
| Workflow diagram | Create a diagram showing the application flow | Workflow diagram |
| Testing | Test realistic student questions | Testing checklist |
| GitHub | Upload project and instructions | GitHub repository |
| Presentation | Demonstrate the application in 5–10 minutes | Final presentation |

---

# 5. Project Scope

## Minimum Viable Product (MVP)

The MVP will include:

1. A Streamlit web interface
2. A text input area for student questions
3. Python application logic
4. Connection to Ollama
5. One open-source LLM
6. Prompt instructions
7. AI-generated response
8. Basic error handling
9. Basic testing

### Example Questions

- Which country is best for international students?
- How much does studying in the USA cost?
- What is an F-1 visa?
- Can international students work in Canada?
- What documents are required to study in the UK?
- Can students work while studying in Australia?
- Can I get a scholarship?

---

## Outside Initial Scope

The first version will NOT include:

- Real-time immigration advice
- Real-time university application systems
- Payment systems
- User accounts
- Complex databases
- Custom machine learning models
- Training an LLM
- Paid APIs
- Complex authentication

---

## Optional Enhancements

Only after the MVP works correctly, possible enhancements include:

- PDF document Q&A
- RAG
- ChromaDB
- FAISS
- Conversation memory
- More countries
- University information
- Document retrieval

These features are optional.

The MVP must be completed and tested first.

---

# 6. Recommended Technology Stack

## Programming Language

Python

### Why?

Python is recommended by CAP 942 and is beginner-friendly for AI application development.

---

## LLM Runner

Ollama

### Why?

Ollama allows an open-source LLM to run locally on the computer.

This means the project does not require a paid AI API.

---

## LLM

A small open-source LLM will be selected for the project.

The initial model should be suitable for a computer with approximately 16 GB RAM.

A smaller model can be used if the computer has performance limitations.

---

## User Interface

Streamlit

### Why?

Streamlit allows us to create a simple web interface using Python.

The student will be able to enter a question and see the AI response.

---

## Python Project Management

uv

### Why?

uv will be used to manage the Python project and dependencies.

---

## Development Environment

- Windows
- Visual Studio Code
- Git
- GitHub
- Terminal

---

## Database

No database will be required for the initial MVP.

A database will only be added if retrieval, document Q&A, or memory is added later.

---

# 7. Application Workflow

The basic application workflow will be:

```text
Student
   |
   v
Enter Question
   |
   v
Streamlit Interface
   |
   v
Python Application
   |
   v
Prompt
   |
   v
Ollama
   |
   v
Open-Source LLM
   |
   v
Generated Answer
   |
   v
Streamlit
   |
   v
Student sees Answer




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