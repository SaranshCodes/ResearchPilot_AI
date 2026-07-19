import streamlit as st 
import os
from core.pdf_parser import extract_text
from core.chunker import chunk_text
from core.embedder import get_embedding
from core.qa_chain import retrieve
from core.llm import ask_gemini
from core.vector_store import create_vector_store, load_vector_store


os.makedirs("uploads", exist_ok=True)
os.makedirs("indexes", exist_ok=True)
st.set_page_config(page_title= 'ResearchPilot AI')

st.title('Research paper RAG')

#Pdf Upload
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    pdf_name = uploaded_file.name.replace(".pdf", "")
    pdf_path = os.path.join('uploads',uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Research Paper Submitted!")

    pages = extract_text("research.pdf")

    all_chunks = []
    chunk_id = 0

    for page in pages:

        page_chunks = chunk_text(page["text"])

        for chunk in page_chunks:

            all_chunks.append({
                "text": chunk,
                "page": page["page"],
                "chunk_id": chunk_id
            })

            chunk_id += 1

    index_data = load_vector_store(pdf_name)

    if index_data:
        index, chunks = index_data

    else:
        index, chunks = create_vector_store(
            all_chunks,
            pdf_name
        )
# Question box
question = st.text_input('Ask anything about the research paper')

if question:
    context, pages = retrieve(question, index, chunks)
    answer = ask_gemini(question, context)
    st.write(answer)
    st.write(f'Sources: Pages {pages}')