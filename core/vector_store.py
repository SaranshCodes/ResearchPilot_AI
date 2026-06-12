import faiss
import numpy as np
from core.embedder import get_embedding

def create_vector_store(chunks):
    embeddings=[]
    for chunk in chunks:
        embeddings.append(get_embedding(chunk))
    embeddings = np.array(
        embeddings, dtype = 'float32'
    )
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, chunks