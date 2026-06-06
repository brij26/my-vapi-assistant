from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_chroma import Chroma

# =========================
# LOAD EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# LOAD VECTOR DB
# =========================

db = Chroma(
    persist_directory="vectordb",
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": 4}
)

# =========================
# RETRIEVE CONTEXT
# =========================

def retrieve_context(query):

    docs = retriever.invoke(query)

    context = "\n\n".join([
        doc.page_content
        for doc in docs
    ])

    return context