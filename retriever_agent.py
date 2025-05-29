from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
data_chunks = []

def build_index(texts):
    global data_chunks
    data_chunks = texts
    embeddings = model.encode(texts)
    index.add(np.array(embeddings))

def retrieve(query, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [data_chunks[i] for i in I[0]]