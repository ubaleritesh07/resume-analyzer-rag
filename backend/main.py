from fastapi import FastAPI, UploadFile, File
import shutil
from pypdf import PdfReader
from vector_store import create_vector_store, search_chunks
from rag_pipeline import ask_llm

app = FastAPI()

resume_text = ""

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    global resume_text

    file_path = "resume.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    resume_text = text

    create_vector_store(resume_text)

    return {"message": "Resume uploaded and indexed successfully"}

@app.get("/chat")
def chat(question: str):

    if resume_text == "":
        return {"response": "Please upload a resume first."}

    context = search_chunks(question)

    answer = ask_llm(context, question)

    return {"response": answer}