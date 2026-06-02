import chromadb

client = chromadb.PersistentClient(
    path="src/storage/chroma"
)

collection = client.get_or_create_collection(
    name="documents"
)