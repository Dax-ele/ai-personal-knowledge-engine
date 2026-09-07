from ai_brain.documents.loader import DocumentLoader
from ai_brain.embeddings.service import EmbeddingService
from ai_brain.knowledge.models import DocumentEmbedding
from ai_brain.knowledge.repository import KnowledgeRepository


class KnowledgeService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.embedding_service = EmbeddingService()

        self.repository = KnowledgeRepository()


    def build_knowledge_base(self):

        documents = self.loader.load()


        texts = [
            document.content
            for document in documents
        ]


        embeddings = self.embedding_service.encode(
            texts
        )


        document_embeddings = []


        for document, embedding in zip(
            documents,
            embeddings
        ):

            document_embeddings.append(
                DocumentEmbedding(
                    document=document,
                    embedding=embedding.tolist()
                )
            )

        print("Sto salvando la knowledge base...")
        self.repository.save(
            document_embeddings
        )
        print("Salvataggio completato.")

        return document_embeddings



if __name__ == "__main__":

    service = KnowledgeService()

    result = service.build_knowledge_base()


    print(
        f"Creati {len(result)} embeddings"
    )