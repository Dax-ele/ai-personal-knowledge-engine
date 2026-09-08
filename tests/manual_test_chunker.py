from ai_brain.documents.chunker import DocumentChunker
from ai_brain.documents.loader import DocumentLoader


loader = DocumentLoader()

# Carichiamo i documenti originali
documents = loader.load()

# Creiamo il chunker
chunker = DocumentChunker(
    chunk_size=100,
    chunk_overlap=20
)

# Prendiamo il primo documento
document = documents[0]

# Dividiamo il documento
chunks = chunker.split(document)

print(f"Documento: {document.title}")
print(f"Numero chunk: {len(chunks)}")

for chunk in chunks:
    print("\n---")
    print(f"Document ID: {chunk.document_id}")
    print(f"Chunk ID: {chunk.chunk_id}")
    print(f"Chunk index: {chunk.chunk_index}")
    print(f"Title: {chunk.title}")
    print(f"Content:\n{chunk.content}")