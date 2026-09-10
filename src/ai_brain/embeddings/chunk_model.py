from dataclasses import dataclass

from ai_brain.documents.chunk_models import DocumentChunk


@dataclass
class ChunkEmbedding:
    # Chunk a cui appartiene l'embedding
    chunk: DocumentChunk

    # Vettore numerico generato dal modello di embedding
    embedding: list[float]