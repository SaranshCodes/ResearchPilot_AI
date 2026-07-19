from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="qwen3-embedding:latest"
)

vector = embeddings.embed_query(
    "What is Retrieval Augmented Generation?"
)

print(type(vector))
print(len(vector))
print(vector[:5])