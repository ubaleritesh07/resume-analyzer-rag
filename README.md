![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![RAG](https://img.shields.io/badge/RAG-LLM%20Pipeline-purple)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)
![LLM](https://img.shields.io/badge/LLM-Llama-blue)


📄 AI Resume Analyzer (RAG + LLM)

This project is an AI-powered Resume Analyzer that allows users to upload a resume (PDF) and ask questions about it. The system uses a Retrieval-Augmented Generation (RAG) pipeline to analyze the resume and generate intelligent answers.
The application extracts text from the uploaded resume, converts it into embeddings, stores them in a vector database, and retrieves the most relevant information to answer user queries using a Large Language Model.
This project demonstrates how modern AI systems combine embeddings, vector search, and LLMs to build intelligent document-based applications.

🚀 Features

1.Upload resume in PDF format
2.Extract text automatically from resume
3.Convert resume text into embeddings
4.Store embeddings in FAISS vector database
5.Retrieve relevant resume information using semantic search
6.Ask questions about the candidate
7.AI-generated answers based on resume content
8.Chat-style interface using Streamlit
9.FastAPI backend for API handling
10.Uses Groq LLM for fast responses

🧠 System Architecture

User Upload Resume
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
(Sentence Transformers)
        ↓
Vector Database
(FAISS)
        ↓
User Question
        ↓
Question Embedding
        ↓
Similarity Search
        ↓
Retrieve Relevant Chunks
        ↓
Send Context + Question to LLM
        ↓
AI Generated Answer


🛠 Tech Stack

Backend
  1.Python
  2.FastAPI
  3.Groq API
  5.FAISS (Vector Database)
  6.Sentence Transformers
  7.PyPDF

Frontend
  1.Streamlit
  2.Requests

AI / ML
  1.Embeddings (Sentence Transformers)
  2.Vector Search (FAISS)
  3.Retrieval-Augmented Generation (RAG)
  4.Large Language Model (Llama via Groq)



📂 Project Structure
resume-analyzer-llm
│
├── backend
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── vector_store.py
│
├── frontend
│   ├── app.py
│
└── README.md


⚙️ Installation

Clone the repository
git clone https://github.com/ubaleritesh07/resume-analyzer-llm.git

Navigate to the project folder
cd resume-analyzer-llm


📦 Install Dependencies

Install backend dependencies
pip install fastapi uvicorn groq pypdf python-multipart sentence-transformers faiss-cpu

Install frontend dependencies
pip install streamlit requests.


🔑 Setup API Key

Create a free API key from:
https://console.groq.com

Add the API key in rag_pipeline.py
client = Groq(api_key="YOUR_API_KEY")


▶️ Run Backend
cd backend
uvicorn main:app --reload

Backend runs on:
http://127.0.0.1:8000


▶️ Run Frontend

Open another terminal and run:
cd frontend
streamlit run app.py

Frontend runs on:
http://localhost:8501


💬 Example Questions

1.Users can ask questions such as:
2.What skills are mentioned in this resume?
3.What technologies does this candidate know?
4.What is the candidate’s experience?
5.Is this candidate suitable for a Machine Learning role?

📈 Future Improvements

1.Resume vs Job Description matching
2.Candidate skill extraction
3.Candidate scoring system
4.Multi-resume ranking
5.Chat history memory
6.Deployment using Docker and cloud services


👨‍💻 Author

Ritesh Ubale
B.Tech Student | AI & Machine Learning Enthusiast
