from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
chunks = []

def create_vector_store(text):

    global index, chunks

    chunk_size = 300
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))


def search_chunks(question, k=3):

    question_embedding = model.encode([question])

    distances, indices = index.search(np.array(question_embedding), k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return "\n".join(results)