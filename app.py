import streamlit as st

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

This system is designed to extract **relevant information directly from FYP research papers**  
using a document-grounded question answering pipeline.

### 🛠️ System Capabilities
- Semantic document retrieval
- Research-paper grounded responses
- Offline vector database
- Free and deployable system

⚠️ Only uploaded research papers are used for responses.
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👤 Developed By")
st.sidebar.markdown("""
**Usama**  
Final Year Project
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📁 Data Scope")
st.sidebar.markdown("""
- Selected FYP research papers  
- Preprocessed and indexed documents  
- No external knowledge sources
""")

# ------------------ MAIN HEADER ------------------
st.markdown("""
# 📊 FYP Research Assistant  
### Structured Question Answering from Research Papers
""")

st.markdown(
    "Use this system to retrieve **key details, contributions, and results** "
    "from your research papers in a structured manner."
)

st.markdown("---")

# ------------------ QUESTION TYPE ------------------
col1, col2 = st.columns([2, 5])

with col1:
    q_type = st.selectbox(
        "🧠 Query Category",
        [
            "Overview",
            "Method Used",
            "Key Contribution",
            "Results & Evaluation",
            "Limitations / Future Scope"
        ]
    )

with col2:
    user_question = st.text_input(
        "📌 Enter your question",
        placeholder="e.g. What improvement does the proposed method provide?"
    )

# ------------------ ASK BUTTON ------------------
if st.button("Process Query"):
    if user_question.strip():
        with st.spinner("Processing documents..."):
            final_query = f"{q_type}: {user_question}"
            answer = ask_question(final_query)

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

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:#9ca3af;font-size:13px;">
    🚀 FYP Research Assistant | Developed by <b>Usama</b> | Streamlit Deployment
    </div>
    """,
    unsafe_allow_html=True
)
