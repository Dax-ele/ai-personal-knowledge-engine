from langchain_core.embeddings import Embeddings

from ai_brain.embeddings.service import EmbeddingService


class LangChainEmbeddingAdapter(Embeddings):
    def __init__(self):
        self.embedding_service = EmbeddingService()

    def embed_documents(self, texts):
        embeddings = self.embedding_service.encode(texts)

        return [
            embedding.tolist()
            for embedding in embeddings
        ]

    def embed_query(self, text):
        embedding = self.embedding_service.encode([text])[0]

        return embedding.tolist()