
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from pypdf import PdfReader
from langchain_core.output_parsers import StrOutputParser



#Create a streamlit application
st.set_page_config(page_title="PDF reader")
st.title("PDF reader")

#Upload Files
files = st.file_uploader("Upload Your Files", type = "pdf", accept_multiple_files= True)
if st.button("read PDFs"):
    with st.spinner("reading on PDFs"):
        for i, file in enumerate(files):
            #Read the first page of the document
            reader = PdfReader(file)
            number_of_pages = len(reader.pages)
            first_page = reader.pages[0]
            raw_text = first_page.extract_text()
            
            st.subheader(f"PDF: {i + 1}")
            st.text(raw_text)
            