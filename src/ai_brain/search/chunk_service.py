from dataclasses import dataclass

from sklearn.metrics.pairwise import cosine_similarity

from ai_brain.documents.chunk_models import DocumentChunk
from ai_brain.documents.chunker import DocumentChunker
from ai_brain.documents.loader import DocumentLoader
from ai_brain.embeddings.chunk_service import ChunkEmbeddingService


@dataclass
class ChunkSearchResult:
    # Chunk trovato dalla ricerca
    chunk: DocumentChunk

    # Similarità tra query e chunk
    score: float


class ChunkSearchService:
    def __init__(self):
        # Carichiamo i documenti originali
        self.loader = DocumentLoader()

        # Dividiamo i documenti in chunk
        self.chunker = DocumentChunker(
            chunk_size=500,
            chunk_overlap=50
        )

        # Servizio che genera gli embeddings dei chunk
        self.embedding_service = ChunkEmbeddingService()

    def search(
        self,
        query,
        top_k=3,
        score_threshold=0.5
    ):
        # Carichiamo i documenti
        documents = self.loader.load()

        # Creiamo tutti i chunk
        chunks = []

        for document in documents:
            chunks.extend(
                self.chunker.split(document)
            )

        # Generiamo gli embeddings dei chunk
        chunk_embeddings = self.embedding_service.encode(
            chunks
        )

        # Generiamo l'embedding della query
        query_embedding = (
            self.embedding_service
            .embedding_service
            .encode([query])
        )

        # Estraiamo i vettori dei chunk
        document_embeddings = [
            item.embedding
            for item in chunk_embeddings
        ]

        # Calcoliamo la cosine similarity
        similarities = cosine_similarity(
            query_embedding,
            document_embeddings
        )[0]

        results = []

        for item, score in zip(
            chunk_embeddings,
            similarities
        ):
            score = float(score)

            # Scartiamo i chunk poco rilevanti
            if score >= score_threshold:
                results.append(
                    ChunkSearchResult(
                        chunk=item.chunk,
                        score=score
                    )
                )

        # Ordiniamo dal chunk più rilevante
        results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return results[:top_k]