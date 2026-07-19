import faiss
import pickle
import numpy as np
import os

from core.embedder import get_embedding

def create_vector_store(chunks, pdf_name):
    embeddings = []
    for chunk in chunks:
        embeddings.append(get_embedding(chunk['text']))
    embeddings = np.array(embeddings, dtype= np.float32)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Saving Faiss index
    faiss.write_index(index, f'indexes/{pdf_name}.faiss')
    
    # Save Chunks
    
    with open(f'indexes/{pdf_name}.pkl', "wb") as f:
        pickle.dump(chunks, f)
    return index, chunks

def load_vector_store(pdf_name):
    
    faiss_path = f"indexes/{pdf_name}.faiss"
    chunk_path = f"indexes/{pdf_name}.pkl"
    
    if not os.path.exists(faiss_path):
        return None
    
    index =faiss.read_index(faiss_path)
    with open(chunk_path,'rb') as f:
        chunks =pickle.load(f)
    return index, chunks