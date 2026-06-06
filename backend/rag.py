from langchain_openai import OpenAIEmbeddings

from langchain_pinecone import PineconeVectorStore

import os

from dotenv import load_dotenv

load_dotenv()

# =========================
# EMBEDDINGS
# =========================

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# =========================
# VECTOR STORE
# =========================

vectorstore = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX"),
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

# =========================
# RETRIEVE
# =========================

def retrieve_context(query):

    docs = retriever.invoke(query)

    context = "\n\n".join([
        doc.page_content
        for doc in docs
    ])

    return context