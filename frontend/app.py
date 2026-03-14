import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer Chatbot")
st.write("Upload a resume and ask questions about the candidate.")

# Sidebar
st.sidebar.header("Upload Resume")

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {"file": uploaded_file}

    response = requests.post(
        "http://127.0.0.1:8000/upload_resume",
        files=files
    )

    if response.status_code == 200:
        st.sidebar.success("Resume uploaded successfully!")

# Chat section
st.subheader("💬 Ask Questions About the Resume")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask something about the resume...")

if question:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing resume..."):

            response = requests.get(
                "http://127.0.0.1:8000/chat",
                params={"question": question}
            )

            if response.status_code == 200:
                answer = response.json()["response"]
            else:
                answer = "Error connecting to backend."

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )