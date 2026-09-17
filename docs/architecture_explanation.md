# 🎓 Study Abroad AI Assistant — System Architecture Explanation

## CAP 942 Presentation Notes

>

---

# Opening — Explain the Diagram

“This diagram shows how my **Study Abroad AI Assistant** works from beginning to end.

The student enters a study-abroad question, the application validates it, builds a prompt, sends that prompt to my local **Llama 3.2:3b** model through **Ollama**, receives the generated response, and displays the answer back to the student.”

---

# STEP 1 — Student 👤

### What happens?

First, the student opens my **Study Abroad AI Assistant** and enters a study-abroad question.

### Example question

```text
What documents do I typically need to study in Canada?
```

### 

> “The student is the starting point of the workflow. The goal is to make it easy for a student to ask a study-abroad question in plain English.”

---

# STEP 2 — Streamlit UI 🖥️ — `app.py`

### What happens?

The question goes to my **Streamlit user interface**.

The main application file is:

```text
app.py
```

The `app.py` file controls the web interface.

It is responsible for:

- collecting the student's question
- handling the Ask button
- displaying the AI response

### How I start the application

In the VS Code terminal, I use:

```bash
uv run streamlit run app.py
```

### 

> “The application is built with Streamlit. I run it from the VS Code terminal using `uv run streamlit run app.py`. The `app.py` file is the entry point of my application. It creates the user interface, receives the student's question, and displays the final response.”

### Important code idea

`app.py` connects the different parts of the application:

```text
Student question
       ↓
Input validation
       ↓
Prompt building
       ↓
Ollama model
       ↓
AI response
       ↓
Streamlit display
```

---

# STEP 3 — Input Validation ✅ — `utils.py`

### What happens?

Before sending anything to the AI model, my application checks whether the student entered a valid question.

This validation is handled by:

```text
utils.py
```

### Main validation code

```python
def is_valid_question(text: str) -> bool:
    """Check whether the student entered a question."""

    cleaned = text.strip()

    return len(cleaned) > 0
```

### What does this code do?

```python
cleaned = text.strip()
```

This removes extra spaces from the beginning and end.

Then:

```python
return len(cleaned) > 0
```

checks whether something is actually left.

### Example

Valid:

```text
What documents do I need to study in Canada?
```

Invalid:

```text

```

or:

```text

```

### 

> “Before calling the AI model, I validate the user's input. The `utils.py` file checks whether the question is empty. If the input is empty, the application shows a validation message and does not make an unnecessary LLM call.”

---

# STEP 4 — Prompt Builder 📄 — `prompts.py`

### What happens?

If the question is valid, the application moves to the prompt-building step.

This is handled by:

```text
prompts.py
```

The `prompts.py` file contains my **system instructions**.

It combines:

```text
System instructions
        +
Student question
        ↓
Final prompt
```

### Main code structure

```python
SYSTEM_PROMPT = """
You are a helpful Study Abroad AI Assistant.

You help prospective international students with general questions about:

- study destinations
- tuition and general costs
- scholarships
- student visas
- required documents
- application processes
- work opportunities
"""
```

Then the prompt-building function:

```python
def build_prompt(user_question: str) -> str:
    """Create the prompt that will be sent to the LLM."""

    return f"""
{SYSTEM_PROMPT}

Student question:
{user_question}
"""
```

### What does this mean?

The application takes the student's question and adds the system instructions.

For example:

```text
System instructions
        +
"What documents do I typically need to study in Canada?"
        ↓
Final prompt
```

### 

> “The `prompts.py` file is my prompt layer. It contains the system prompt and a function called `build_prompt`. The function combines my system instructions with the student's question. The system prompt keeps the AI focused on study-abroad topics.”

---

# STEP 5 — Ollama + Llama 3.2:3b 🤖 — `llm_helper.py`

### What happens?

The completed prompt is sent to **Ollama**.

Ollama runs my open-source:

```text
Llama 3.2:3b
```

model locally on my computer.

The Python communication with Ollama is handled by:

```text
llm_helper.py
```

---

## Main code

```python
import ollama


def ask_model(prompt: str, model_name: str) -> str:
    """Send a prompt to the Ollama model and return the answer."""

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"].strip()
```

---

## Explain the code step by step

### 1. Import Ollama

```python
import ollama
```

> “First, I import the Ollama Python package so my Python application can communicate with the local Ollama service.”

### 2. Create the function

```python
def ask_model(prompt: str, model_name: str) -> str:
```

> “I created an `ask_model` function. It receives the final prompt and the model name.”

### 3. Call the model

```python
response = ollama.chat(
    model=model_name,
```

> “The `ollama.chat` function sends the prompt to the selected local model.”

### 4. Send the prompt

```python
messages=[
    {
        "role": "user",
        "content": prompt,
    }
]
```

> “The student's prompt is sent as a user message.”

### 5. Return the answer

```python
return response["message"]["content"].strip()
```

> “The model returns a response. I extract the generated message and use `strip()` to remove unnecessary spaces.”

---

## 

> “This is the main AI part of my project. Ollama runs the open-source Llama 3.2:3b model locally. Because the model runs locally, my project does not require a paid external AI API.”

---

# STEP 6 — AI Response 💬

### What happens?

The **Llama 3.2:3b** model processes the prompt and generates an answer.

For example, if the student asks:

```text
What documents do I typically need to study in Canada?
```

the model generates a general response about documents that students may typically need.

### 

> “The Llama 3.2:3b model processes the prompt and generates the answer. The response is then returned from Ollama to my Python application.”

---

# STEP 7 — Response Returns to Streamlit 🔄

### What happens?

After the model generates the answer, the response returns to the Python application.

Then:

```text
Streamlit UI
```

displays the answer on the screen.

### 

> “After the model generates the response, the response is returned to my Python application. Streamlit then displays the AI-generated answer so the student can read it.”

---

# 🔄 COMPLETE FLOW

```text
Student
   ↓
Streamlit UI — app.py
   ↓
Input Validation — utils.py
   ↓
Prompt Builder — prompts.py
   ↓
Ollama
   ↓
Llama 3.2:3b
   ↓
AI-generated response
   ↓
Streamlit UI
   ↓
Student sees the answer
```

---

# 🧠 One-Line Memory Formula

Remember this during your presentation:

```text
STUDENT
→ STREAMLIT
→ VALIDATION
→ PROMPT
→ OLLAMA / LLAMA
→ RESPONSE
→ STREAMLIT
→ STUDENT
```

---

# 📁 HOW THE FILES WORK TOGETHER

| File | Responsibility |
|---|---|
| `app.py` | Streamlit user interface and application entry point |
| `utils.py` | Input validation |
| `prompts.py` | System prompt and prompt building |
| `llm_helper.py` | Ollama and Llama 3.2:3b communication |
| `tests/test_prompts.py` | Automated tests |
| `pyproject.toml` | Project dependencies and configuration |
| `README.md` | Project documentation |
| `docs/workflow_diagram.png` | Workflow diagram |

---

# 🧩 WHY I SEPARATED THE CODE

### 

> “I separated the application into different files so each part has a clear responsibility. This makes the project easier to understand, test, maintain, and explain.”

The responsibilities are:

```text
app.py
    ↓
User interface

utils.py
    ↓
Input validation

prompts.py
    ↓
Prompt engineering

llm_helper.py
    ↓
Ollama + Llama model communication

tests/
    ↓
Testing

README.md
    ↓
Documentation
```

---

# 🚫 IMPORTANT DESIGN DECISION — NO RAG / NO DATABASE

### 

> “My MVP does not use RAG or a database. The application does not search the internet or retrieve information from a document database.”

The model generates the answer from its existing training knowledge.

```text
Student Question
       ↓
System Prompt
       ↓
Llama 3.2:3b
       ↓
Generated Answer
```

There is no:

```text
Database
RAG
Vector Database
Live Web Search
```

---

# ⚠️ LIMITATION

### 

> “Because my MVP does not retrieve live information, information such as current visa requirements, fees, deadlines, tuition, or other time-sensitive information may not always be current.”

Therefore:

> “My application provides general educational guidance only. Users should verify important information with official government, embassy, or university sources.”

---

# 🧪 TESTING

The automated test command is:

```bash
uv run pytest
```

The completed automated tests verify:

- prompt building
- valid question input
- empty input
- spaces-only input

The test result was:

```text
4 passed
```

### 

> “I also created automated tests for the prompt-building and input-validation functions. My pytest test suite passed four tests.”

---

# 🚀 LIVE DEMO — Flow
## Step 1 — Open VS Code terminal

Run:

```bash
uv run streamlit run app.py
```

## Step 2 — Open the Streamlit application

The application opens in the browser.

## Step 3 — Enter a question

Example:

```text
What documents do I typically need to study in Canada?
```

## Step 4 — Click the Ask button

The application sends the question through the workflow:

```text
Question
   ↓
Validation
   ↓
Prompt
   ↓
Ollama
   ↓
Llama 3.2:3b
   ↓
Response
```

## Step 5 — Show the response

Explain:

> “This is the response generated by my local open-source Llama model.”

## Step 6 — Demonstrate validation

Leave the question empty and click Ask.

Explain:

> “The application validates the input and prevents an empty question from being sent to the model.”

## Step 7 — Show the project files

Show:

```text
app.py
llm_helper.py
prompts.py
utils.py
pyproject.toml
README.md
docs/
tests/
```

## Step 8 — Show testing

Run:

```bash
uv run pytest
```

Show:

```text
4 passed
```

---

# 🎤 FINAL 30-SECOND EXPLANATION

> “So, in simple terms, the student asks a question, Streamlit receives it, the application validates the input, `prompts.py` builds the prompt, `llm_helper.py` sends it to my local Llama 3.2:3b model through Ollama, the model generates a response, and Streamlit displays that response back to the student.
>
> The architecture is intentionally simple because this is my CAP 942 MVP. I focused on building one complete working AI application rather than adding unnecessary features.”

---

# ⭐ FINAL MEMORY LINE

```text
Student
↓
Streamlit — app.py
↓
Validation — utils.py
↓
Prompt — prompts.py
↓
Ollama
↓
Llama 3.2:3b
↓
AI Response
↓
Streamlit
↓
Student
```



CAP 942 — Streamlit Application Manual Testing

Run the Streamlit application:
uv run streamlit run app.py

Test #1 — Ask a Study-Abroad Question
1. Open the Streamlit application in the browser.
2. Enter:
   What documents do I need to study in Canada?
3. Click "🚀 Ask AI Assistant".
4. Expected result: The application displays an AI-generated answer about documents commonly needed to study in Canada.

Test #2 — Ask a Scholarship Question
1. Enter:
   How do scholarships for international students usually work?
2. Click "🚀 Ask AI Assistant".
3. Expected result: The application displays an AI-generated answer explaining scholarships for international students.

Test #3 — Empty Question
1. Do not type anything in the question box.
2. Click "🚀 Ask AI Assistant".
3. Expected result:
   Please enter a question before clicking Ask.

Test #4 — Off-Topic Question
1. Enter:
   Write me a poem about cats.
2. Click "🚀 Ask AI Assistant".
3. Expected result: The AI politely explains that it is focused on study-abroad questions rather than unrelated topics.

Manual Testing Summary:
✓ Streamlit application opens successfully.
✓ Study-abroad questions receive AI-generated answers.
✓ Scholarship questions receive AI-generated answers.
✓ Empty input is validated correctly.
✓ Off-topic questions are handled by the study-abroad system prompt.
✓ The application works end-to-end with the local Ollama/Llama model.




MVP includes:

✅ User enters a question
✅ Question validation
✅ Study-abroad prompt
✅ Local open-source LLM
✅ AI-generated answer
✅ Streamlit interface
✅ Basic error handling



“So, in simple terms, the student asks a question, Streamlit receives it, the application validates the input, `prompts.py` builds the prompt, `llm_helper.py` sends it to my local Llama 3.2:3b model through Ollama, the model generates a response, and Streamlit displays that response back to the student.
>
> The architecture is intentionally simple because this is my CAP 942 MVP. I focused on building one complete working AI application rather than adding unnecessary features.”
