import numpy as np
from core.embedder import get_embedding
from core.embedder import client

def retrieve(query, index, chunks):
    query_embedding = np.array(
        [get_embedding(query)],
        dtype = 'float32'
    )
    distances , indices = index.search(
        query_embedding, k =3
    )
    retrieved= []
    for idx in indices[0]:
        retrieved.append(chunks[idx])
    return '\n'.join(retrieved)

def ask_gemini(question, context):
    prompt = f'''
    You are a research paper assistant. Answer only using the provided context chunks.
If the answer isn't in the context, say so clearly. Always mention which section of the paper your answer comes from.
    
    Research paper context:
    {context}
    
    Question:
    {question}
    '''
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt
    )
    return response.text