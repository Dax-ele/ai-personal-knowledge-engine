from ai_brain.documents.chunk_models import DocumentChunk
from ai_brain.embeddings.chunk_models import ChunkEmbedding
from ai_brain.embeddings.service import EmbeddingService


class ChunkEmbeddingService:
    def __init__(self):
        # Riutilizziamo il servizio di embedding già esistente
        self.embedding_service = EmbeddingService()

    def encode(self, chunks: list[DocumentChunk]):
        # Estraiamo il testo di ogni chunk
        texts = [
            chunk.content
            for chunk in chunks
        ]

        # Generiamo gli embeddings in un'unica operazione
        embeddings = self.embedding_service.encode(texts)

        # Associamo ogni embedding al relativo chunk
        return [
            ChunkEmbedding(
                chunk=chunk,
                embedding=embedding.tolist()
            )
            for chunk, embedding in zip(chunks, embeddings)
        ]