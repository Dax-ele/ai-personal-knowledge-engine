from sklearn.metrics.pairwise import cosine_similarity

from ai_brain.embeddings.service import EmbeddingService
from ai_brain.knowledge.repository import KnowledgeRepository
from dataclasses import dataclass

from ai_brain.documents.models import Document
from ai_brain.embeddings.service import EmbeddingService
from ai_brain.knowledge.repository import KnowledgeRepository
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class SearchResult:
    document: Document
    score: float

class SearchService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.repository = KnowledgeRepository()

    def search(self, query, top_k=3,score_threshold=0.5):
        items = self.repository.load()

        query_embedding = self.embedding_service.encode([query])

        document_embeddings = [
            item.embedding
            for item in items
        ]

        similarities = cosine_similarity(
            query_embedding,
            document_embeddings
        )[0]

        results = []

        for item, score in zip(items, similarities):
            score = float(score)

            if score >= score_threshold:
                results.append(
                    SearchResult(
                        document=item.document,
                        score=float(score)
                    )
                )

        results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return results[:top_k]
