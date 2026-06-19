import streamlit as st 
from core.pdf_parser import extract_text
from core.chunker import chunk_text
from core.embedder import get_embedding
from core.qa_chain import retrieve, ask_gemini
from core.vector_store import create_vector_store



st.set_page_config(page_title= 'ResearchPilot AI')

st.title('Research paper RAG')

#Pdf Upload
uploaded_file = st.file_uploader('Upload PDF', type = 'pdf')
if uploaded_file:
    with open('research.pdf', 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.success('Research Paper submitted!')
    text =extract_text('research.pdf')
    chunks= chunk_text(text)
    index, chunks = create_vector_store(chunks)
    
# Question box
question = st.text_input('Ask anything about the research paper')

if question:
    context = retrieve(question, index,chunks)
    answer = ask_gemini(question,context)