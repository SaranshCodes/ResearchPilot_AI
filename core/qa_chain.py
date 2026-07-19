import numpy as np
from core.embedder import get_embedding
from core.llm import ask_gemini

def retrieve(query, index, chunks):
    query_embedding = np.array(
        [get_embedding(query)],
        dtype = 'float32'
    )
    distances, indices =index.search(
        query_embedding, k=5
    )
    retrieved = []
    for idx in indices[0]:
        retrieved.append(chunks[idx])
    
    context ='\n\n'.join(chunk['text'] for chunk in retrieved)
    pages = sorted(set(chunk['page'] for chunk in retrieved))
    return context, pages


# Retrieval logic