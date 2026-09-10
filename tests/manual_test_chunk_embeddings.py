from ai_brain.documents.chunker import DocumentChunker
from ai_brain.documents.loader import DocumentLoader
from ai_brain.embeddings.chunk_service import ChunkEmbeddingService


loader = DocumentLoader()

# Carichiamo i documenti originali
documents = loader.load()

# Creiamo il chunker
chunker = DocumentChunker(
    chunk_size=100,
    chunk_overlap=20
)

# Creiamo il servizio di embedding
embedding_service = ChunkEmbeddingService()

# Prendiamo il documento Java
document = next(
    document
    for document in documents
    if document.id == "java"
)

# Dividiamo il documento in chunk
chunks = chunker.split(document)

# Generiamo gli embeddings dei chunk
chunk_embeddings = embedding_service.encode(chunks)

print(f"Documento: {document.title}")
print(f"Numero chunk: {len(chunk_embeddings)}")

for item in chunk_embeddings:
    print("\n---")
    print(f"Chunk ID: {item.chunk.chunk_id}")
    print(f"Embedding dimension: {len(item.embedding)}")
    print(f"Primi 5 valori: {item.embedding[:5]}")