import streamlit as st
from qa_engine import ask_question

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="FYP Research Assistant",
    page_icon="📊",
    layout="wide"
)

# ------------------ SIDEBAR ------------------
st.sidebar.markdown("## 🧩 Project Overview")
st.sidebar.markdown("""
**FYP Research Paper Assistant**

This system retrieves information **strictly from uploaded research papers**
using a document-grounded question answering pipeline.
""")

st.sidebar.markdown("### 👤 Developed By")
st.sidebar.markdown("**Usama**")

st.sidebar.markdown("### ⚠️ Scope")
st.sidebar.markdown(
    "Only questions related to the research papers are answered."
)

# ------------------ MAIN HEADER ------------------
st.markdown("# 📊 FYP Research Assistant")
st.markdown(
    "Use this system to retrieve key details, contributions, "
    "and results from research papers."
)

st.markdown("---")

# ------------------ INPUT ------------------
query_category = st.selectbox(
    "🧠 Query Category",
    [
        "Overview",
        "Method Used",
        "Key Contribution",
        "Results & Evaluation",
        "Limitations / Future Work"
    ]
)

user_question = st.text_input(
    "📌 Enter your question",
    placeholder="e.g. What is the main contribution of the proposed method?"
)

# ------------------ PROCESS BUTTON ------------------
if st.button("Process Query"):
    if user_question.strip():

        final_query = f"{query_category}: {user_question}"

        with st.spinner("Processing research papers..."):
            answer = ask_question(final_query)

        st.success("Answer retrieved successfully")

        st.markdown("### 🧠 Retrieved Insight")
        st.markdown(
            f"""
            <div style="
                background-color:#1f2937;
                padding:20px;
                border-left:6px solid #22c55e;
                border-radius:8px;
                font-size:16px;">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a valid question.")
