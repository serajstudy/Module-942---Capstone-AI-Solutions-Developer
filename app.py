import streamlit as st

from prompts import build_prompt
from llm_helper import ask_model
from utils import is_valid_question


MODEL_NAME = "llama3.2:3b"


# -----------------------------
# Page settings
# -----------------------------

st.set_page_config(
    page_title="Study Abroad AI Assistant",
    page_icon="🎓",
    layout="wide",
)


# -----------------------------
# Custom CSS
# -----------------------------

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background-color: #fff8f8;
    }

    /* Header */
    .header {
        background: linear-gradient(135deg, #b5121b, #d71920);
        padding: 28px;
        border-radius: 0 0 20px 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .header h1 {
        margin: 0;
        font-size: 38px;
        font-weight: 800;
    }

    .header p {
        margin-top: 8px;
        font-size: 18px;
    }

    /* Logo circle */
    .logo {
        width: 70px;
        height: 70px;
        background-color: #ffd447;
        color: #b5121b;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 42px;
        font-weight: 900;
        margin-bottom: 10px;
    }

    /* Information cards */
    .card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #f0d0d0;
    margin-bottom: 20px;
    box-shadow: 0 3px 10px rgba(181, 18, 27, 0.08);

    height: 170px;
    box-sizing: border-box;
}

.stColumn {
    display: flex;
}

    .card h3 {
        color: #b5121b;
        margin-top: 0;
    }

    .card p {
        color: #444444;
        font-size: 16px;
    }

    /* Ask button */
    .stButton > button {
        background-color: #b5121b;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 17px;
        font-weight: 700;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #d71920;
        color: #ffd447;
    }

    /* Text area */
    textarea {
        border: 2px solid #d71920 !important;
        border-radius: 10px !important;
    }

    /* Answer box */
    .answer-box {
        background-color: white;
        border-left: 7px solid #ffd447;
        padding: 22px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 3px 10px rgba(181, 18, 27, 0.10);
    }

    .answer-title {
        color: #b5121b;
        font-size: 24px;
        font-weight: 800;
    }

    /* Footer */
    .footer {
        background-color: #b5121b;
        color: white;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        margin-top: 40px;
    }

    .footer strong {
        color: #ffd447;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="header">
        <div class="logo">B</div>
        <h1>Study Abroad AI Assistant</h1>
        <p> Educational Consultancy and Services</p>
        <p>Guidance to Quality Education</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Introduction cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>🎓 Study Destinations</h3>
            <p>
            Get general guidance about studying in countries
            such as Canada, USA, UK, Australia and other Countries.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>📚 Applications</h3>
            <p>
            Ask about common application steps,
            required documents and study options.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>💰 Scholarships</h3>
            <p>
            Learn about general scholarship categories,
            tuition and financial planning.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# AI question section
# -----------------------------

st.markdown(
    """
    <div class="card">
        <h3>🤖 Ask the Study Abroad AI</h3>
        <p>
        Type your study-abroad question below.
        Your question is answered by a local open-source AI model.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


question = st.text_area(
    "Your question",
    placeholder="Example: What documents do I need to study in Canada?",
    height=130,
)


# -----------------------------
# Ask AI
# -----------------------------

if st.button("🚀 Ask AI Assistant"):

    if not is_valid_question(question):

        st.error("Please enter a question before clicking Ask.")

    else:

        prompt = build_prompt(question)

        with st.spinner("🤖 AI is thinking..."):

            try:

                answer = ask_model(prompt, MODEL_NAME)

                st.markdown(
                    """
                    <div class="answer-box">
                        <div class="answer-title">
                            🤖 AI Answer
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.write(answer)

            except Exception:

                st.error(
                    "Sorry, I couldn't reach the AI model. "
                    "Please make sure Ollama is running and "
                    "llama3.2:3b is installed."
                )


# -----------------------------
# Disclaimer
# -----------------------------

st.warning(
    "⚠️ General guidance only. "
    "Always verify visa requirements, deadlines, fees, "
    "admission requirements and other important information "
    "with the official government, embassy or university source."
)


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">
        <strong> Educational Consultancy and Services</strong><br>
        Study Abroad AI Assistant<br>
        Powered by a local open-source LLM with Ollama
    </div>
    """,
    unsafe_allow_html=True,
)