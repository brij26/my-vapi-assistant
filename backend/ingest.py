from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

import os

# =========================
# LOAD ALL PDFS
# =========================

documents = []

# Resume
resume_loader = PyPDFLoader(
    "data/Resume_Brij_Patel.pdf"
)

documents.extend(
    resume_loader.load()
)

# GitHub PDFs
github_docs_path = "data/github_docs"

for file in os.listdir(github_docs_path):

    if file.endswith(".pdf"):

        path = os.path.join(
            github_docs_path,
            file
        )

        loader = PyPDFLoader(path)

        documents.extend(
            loader.load()
        )

# =========================
# SPLIT TEXT
# =========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(
    documents
)

# =========================
# EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# CREATE VECTOR DB
# =========================

db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="vectordb"
)

db.persist()

print("Vector Database Created Successfully")