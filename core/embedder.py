from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="qwen3-embedding:latest" 
)

def get_embedding(text):
    return embeddings.embed_query(text)

# Ollama Embedding