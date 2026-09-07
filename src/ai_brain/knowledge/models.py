from dataclasses import dataclass

from ai_brain.documents.models import Document


@dataclass
class DocumentEmbedding:
    document: Document
    embedding: list[float]