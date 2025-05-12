import streamlit as st
from pdf_loader import extract_text_from_pdfs
from qa_chain_local import LocalPDFQA

st.set_page_config(page_title="Chat with PDFs (Free Version)", layout="wide")
st.title("📄 Chat with Multiple PDFs (Offline & Free)")

uploaded_files = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Reading and embedding..."):
        text = extract_text_from_pdfs(uploaded_files)
        qa = LocalPDFQA()
        qa.split_text(text)
        qa.build_vector_index()
    st.success("Ready! Ask a question below.")

    query = st.text_input("💬 Ask your question")
    if query:
        with st.spinner("Generating answer..."):
            answer = qa.query(query)
            st.write("📘 **Answer:**", answer)
