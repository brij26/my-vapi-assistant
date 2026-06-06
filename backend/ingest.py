from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_openai import (
    OpenAIEmbeddings
)

from langchain_pinecone import (
    PineconeVectorStore
)

import os

from dotenv import load_dotenv

load_dotenv()

# =========================
# LOAD DOCUMENTS
# =========================

documents = []

# =========================
# LOAD RESUME
# =========================

resume_path = "data/resume.pdf"

resume_loader = PyPDFLoader(
    resume_path
)

resume_docs = resume_loader.load()

documents.extend(resume_docs)

# =========================
# LOAD GITHUB DOCS
# =========================

github_docs_path = "data/github_docs"

for file in os.listdir(github_docs_path):

    if file.endswith(".pdf"):

        path = os.path.join(
            github_docs_path,
            file
        )

        github_loader = PyPDFLoader(path)

        github_docs = github_loader.load()

        documents.extend(github_docs)

# =========================
# SPLIT
# =========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(
    documents
)

# =========================
# OPENAI EMBEDDINGS
# =========================

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# =========================
# PINECONE STORE
# =========================

vectorstore = PineconeVectorStore.from_documents(
    docs,
    embedding=embeddings,
    index_name=os.getenv("PINECONE_INDEX")
)

print("Pinecone Upload Successful")