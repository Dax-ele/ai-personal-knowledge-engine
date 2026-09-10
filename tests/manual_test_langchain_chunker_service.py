from ai_brain.rag.langchain_chunker import LangChainChunker


chunker = LangChainChunker(
    chunk_size=100,
    chunk_overlap=20
)

# Creiamo i chunk di tutti i documenti
chunks = chunker.split_documents()

print(f"Numero totale chunk: {len(chunks)}")

for chunk in chunks:
    print("\n---")
    print(f"Document ID: {chunk.metadata['document_id']}")
    print(f"Title: {chunk.metadata['title']}")
    print(f"Content:\n{chunk.page_content}")