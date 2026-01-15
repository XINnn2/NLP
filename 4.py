import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

st.title("Text Chunking using NLTK Sentence Tokenizer")

pdf_file = st.file_uploader("Upload PDF File", type="pdf")

if pdf_file is not None:
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    sentences = sent_tokenize(text)

    st.subheader("Sample Extracted Sentences (Index 58–68)")
    for i, sentence in enumerate(sentences[58:68], start=58):
        st.write(f"{i}: {sentence}")
