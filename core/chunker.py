def chunk_text(text, chunk_size=500, chunk_overlap=100):
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be non-negative")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be less than chunk_size")
        
    chunks = []
    if not text:
        return chunks
        
    step = chunk_size - chunk_overlap
    for i in range(0, len(text), step):
        chunks.append(text[i:i+chunk_size])
        if i + chunk_size >= len(text):
            break
    return chunks