CAP 942 AI Application Development Capstone

PROJECT IDEA:

Study Abroad AI Assistant

I want to build a small AI application that helps students ask common questions about studying abroad.

The application will accept a student's question and use an open-source Large Language Model (LLM) running locally through Ollama to generate a helpful response.

The first version will focus on simple questions about studying in the USA, Canada, UK, and Australia.

The application should be simple and beginner-friendly. The main goal is to make a working AI application that meets the CAP 942 requirements.

MY CURRENT EXPERIENCE LEVEL:

Beginner

I know some Python and basic programming concepts, but I am still learning AI application development, LLMs, Ollama, Streamlit, APIs, and prompt engineering.

PREFERRED APPLICATION FORMAT:

Streamlit

I want to use Streamlit because it is simple for building a small Python web application.

AVAILABLE COMPUTER OR DEVELOPMENT ENVIRONMENT:

Windows computer
Visual Studio Code
Python
Terminal
Git
GitHub
Ollama

Use uv for Python project and dependency management.

CAPSTONE REQUIREMENTS:

The CAP 942 capstone requires me to build a small but functional AI application using an existing open-source LLM.

I do NOT need to train a machine learning or deep learning model.

The project should:

- Use at least one open-source LLM
- Accept user input
- Produce LLM-generated output
- Run as a Python script, Jupyter/Colab notebook, Streamlit app, Flask app, or FastAPI app
- Run without paid APIs
- Demonstrate prompt engineering
- Have a clear problem to solve
- Work from beginning to end
- Include documentation
- Include a workflow diagram
- Include testing
- Be uploaded to GitHub
- Include a 5–10 minute final presentation

Recommended tools include:

- Python
- Ollama
- Hugging Face
- LangChain
- GPT4All
- Llama.cpp
- Streamlit
- Flask
- FastAPI
- SentenceTransformers
- pypdf
- ChromaDB
- FAISS

For this project, I want to keep the first version simple.

I plan to use:

- Python
- Ollama
- One small open-source LLM
- Streamlit
- uv
- Git
- GitHub

A database is not required for the first version.

Optional features such as RAG, PDF document Q&A, ChromaDB, FAISS, conversation memory, or multiple tools should only be considered after the basic application works.

The capstone requires these deliverables:

1. Project Proposal

The proposal should include:

- Problem statement
- Why the project matters
- Tools/frameworks
- Expected output or user interaction

2. Working AI Application

The application must:

- Use an open-source LLM
- Accept user input
- Generate an AI response
- Run without paid APIs
- Work end-to-end

3. Data or Input Sources

Only required if the project uses a dataset or external data source.

A simple LLM application without a dataset may skip this section.

4. Final Presentation

The presentation should be 5–10 minutes and explain:

- What the application does
- The problem it solves
- User input
- LLM interaction
- Output
- Tools used
- Challenges
- Lessons learned
- Next steps
- Application workflow

The final documentation should include:

- Application overview
- Purpose
- Problem being solved
- Intended users
- Technical workflow diagram
- Tools and libraries
- LLM selected
- Application architecture
- Data flow
- Features
- How the LLM is used
- Challenges
- Lessons learned

The project should be submitted through Canvas as a ZIP file or GitHub link.

The project should follow the naming convention:

FirstName_LastName_CapstoneAI

GOAL:

Create an implementation plan for my Study Abroad AI Assistant.

The plan should be a learning roadmap that helps me build the application one step at a time.

Please make the plan simple and easy for a beginner to understand.

Do NOT create the complete capstone application for me.

Do NOT give me a complete main.py or app.py.

Do NOT give me a complete finished repository.

Do NOT give me large blocks of code that I can submit without understanding.

Do NOT use paid APIs.

Do NOT train a machine learning or deep learning model.

The plan should teach me what I need to learn and what I need to build myself.

If my project idea is too large, reduce it to a realistic MVP and clearly separate:

- Required MVP features
- Optional features

Please create the following sections in my implementation plan:

1. Project Title

2. Project Summary

Explain:
- What the application does
- Who it helps
- Why it is useful

3. Problem Statement

Explain:
- What problem I am solving
- Why the problem matters
- Who will use the application

4. CAP 942 Requirement Alignment

Create a simple table with:

- CAP 942 requirement
- How my project meets the requirement
- Evidence I can show

5. Project Scope

Explain:

- MVP features
- Features I should not build initially
- Optional enhancements

Keep the MVP small.

6. Recommended Technology Stack

Explain in simple language:

- Python
- Ollama
- Open-source LLM
- Streamlit
- uv
- Git
- GitHub

Explain why each one is being used.

Also explain computer/RAM requirements and what smaller model I can use if needed.

7. Application Workflow

Explain the complete flow:

User
→ Streamlit
→ Python
→ Prompt
→ Ollama
→ Open-source LLM
→ AI response
→ Streamlit
→ User

Include a simple Mermaid workflow diagram.

Clearly show where the LLM is used.

8. Application Architecture

Explain the main parts of the application and what each part does.

Keep this beginner-friendly.

9. Proposed Project Structure

Show a simple folder and file structure.

For example:

study-abroad-ai-assistant/
├── main.py
├── README.md
├── implementation_plan.md
├── pyproject.toml
├── .gitignore
└── uv.lock

Explain what each file is for.

Do not write the completed files.

10. Step-by-Step Development Milestones

Break the project into small steps.

For every milestone explain:

- What I need to learn
- What I need to do
- Small coding exercise
- Testing checkpoint
- Acceptance criteria
- Common mistakes
- What I need to build myself
- How I know it works

Start with the smallest working component.

Do not tell me to build everything at once.

11. Guided Code Examples

Give only 3–5 short code examples.

Each example should:

- Be about one concept
- Be approximately 25 lines or less
- Have comments
- Include a TODO
- Be easy for a beginner
- Not be connected into a complete application

Examples can include:

- Getting user input
- Validating input
- Creating a Python function
- Calling Ollama
- Processing a response
- Basic error handling

After each example, explain what the code does and give me a small practice task.

12. Prompt Engineering Plan

Explain:

- What prompt engineering means
- Why my application needs a good prompt
- What instructions I should give the LLM
- What information the user provides
- What the expected answer should look like
- How to reduce incorrect or unsupported answers

Give me one simple prompt template using placeholders.

13. Testing Plan

Create a simple testing plan.

Include at least five realistic questions.

For each test explain:

- Input
- Expected behavior
- What I should check

Also include:

- Empty input test
- Invalid input test
- Ollama unavailable test
- Model unavailable test

Explain a simple way to check whether the AI answer is useful.

14. Privacy, Security, Accessibility, and Responsible AI

Explain in simple language:

- What information I should not collect
- What I should not put on GitHub
- Basic security
- Accessibility
- Limitations of an AI assistant
- Why immigration/legal information should be verified with official sources

The application should not claim to be a lawyer, government agency, university, or official immigration service.

15. Documentation and GitHub Plan

Explain what I should put in README.md.

Include:

- Project description
- Problem
- Features
- Technologies
- Installation
- Ollama setup
- Model setup
- How to run
- Example questions
- Example output
- Testing
- Limitations
- Future improvements

Also give me a simple GitHub checklist.

16. Presentation Plan

Create a simple 5–10 minute presentation plan.

Explain what I should say about:

- Problem
- Solution
- Technology
- Workflow
- Demo
- Challenges
- Lessons learned
- Future improvements

17. Suggested Timeline

Create a simple development schedule.

I want to:

1. Understand the project
2. Set up Python and uv
3. Set up Ollama
4. Test the LLM
5. Build the Streamlit interface
6. Connect Streamlit to Ollama
7. Improve the prompt
8. Add error handling
9. Test the MVP
10. Write documentation
11. Upload to GitHub
12. Prepare the presentation

Make sure I finish and test the MVP before working on optional enhancements.

18. Definition of Done

Create a final checklist that covers:

- Proposal
- Working application
- Open-source LLM
- User input
- AI-generated output
- Prompt engineering
- Testing
- Documentation
- Workflow diagram
- GitHub
- Presentation
- CAP 942 requirements




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

