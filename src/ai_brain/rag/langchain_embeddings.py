import numpy as np

from langchain_core.embeddings import Embeddings

from ai_brain.embeddings.service import EmbeddingService


class LangChainEmbeddingAdapter(Embeddings):
    def __init__(self):
        self.embedding_service = EmbeddingService()

    def embed_documents(self, texts):
        # Generiamo gli embeddings dei documenti
        embeddings = self.embedding_service.encode(texts)

        # Normalizziamo i vettori per renderli confrontabili tramite cosine similarity
        embeddings = embeddings / np.linalg.norm(
            embeddings,
            axis=1,
            keepdims=True
        )

        return [
            embedding.tolist()
            for embedding in embeddings
        ]

    def embed_query(self, text):
        # Generiamo l'embedding della query
        embedding = self.embedding_service.encode([text])[0]

        # Normalizziamo il vettore della query
        embedding = embedding / np.linalg.norm(embedding)

        return embedding.tolist()