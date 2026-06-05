from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from src.core.embeddings import embeddings

def ingest():

    with open(
        "data/docs/notes.txt",
        "r"
    ) as file:

        text = file.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs = splitter.create_documents([text])

    Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="chroma_db"
    )

    print("Chunks Stored")