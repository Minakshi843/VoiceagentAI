import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Folder where vector DB will be stored after creation
VECTOR_DB_PATH = "vector_store"

# Your PDF files inside knowledge_base/
PDF_FILES = [
    "knowledge_base/SIZE24 – COMPREHENSIVE FAQ.pdf",
    "knowledge_base/Size24_FAQ_Updated.pdf",
    "knowledge_base/Size24_Full_Detailed_Document.pdf",
]


def build_vector_database():
    """
    Loads all PDFs → Splits them → Creates embeddings → Saves FAISS vector DB.
    Run this once before running agent.
    """
    docs = []

    # Load all PDF files
    for file in PDF_FILES:
        loader = PyPDFLoader(file)
        docs.extend(loader.load())

    # Split into chunks for better search
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
    )
    chunks = splitter.split_documents(docs)

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    # Create FAISS vector store
    vector_db = FAISS.from_documents(chunks, embeddings)

    # Save database locally
    vector_db.save_local(VECTOR_DB_PATH)

    print("Vector database created successfully.")


def get_retriever():
    """
    Loads stored FAISS vector DB and returns retriever.
    This is used by your agent when answering queries.
    """
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTOR_DB_PATH, embeddings)

    # Return retriever that retrieves top 3 relevant chunks
    return db.as_retriever(search_kwargs={"k": 3})
