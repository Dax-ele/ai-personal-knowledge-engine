from ai_brain.documents.loader import DocumentLoader
from ai_brain.embeddings.service import EmbeddingService

class DocumentService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.embedding_service = EmbeddingService()

    def load_documents(self):

        return self.loader.load()

    def create_embeddings(self):

        documents = self.loader.load()

        contents = [
        doc.content
        for doc in documents
        ]

        embeddings = self.embedding_service.encode(
        contents
        )

        return documents, embeddings


if __name__ == "__main__":

    service = DocumentService()

    documents, embeddings = service.create_embeddings()

    print(f"Documenti: {len(documents)}")

    print(f"Embeddings: {embeddings.shape}")