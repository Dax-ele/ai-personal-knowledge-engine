from langchain_core.documents import Document as LangChainDocument
from langchain_community.vectorstores import FAISS

from ai_brain.documents.loader import DocumentLoader
from ai_brain.rag.langchain_embeddings import LangChainEmbeddingAdapter


class LangChainService:
    def __init__(self):
        self.loader = DocumentLoader()
        self.embeddings = LangChainEmbeddingAdapter()

    def load_documents(self):
        documents = self.loader.load()

        return [
            LangChainDocument(
                page_content=document.content,
                metadata={
                    "id": document.id,
                    "title": document.title
                }
            )
            for document in documents
        ]

    def create_vector_store(self):
        documents = self.load_documents()

        # Calcoliamo gli embeddings dei nostri documenti
        embeddings = self.embeddings.embed_documents(
            [document.page_content for document in documents]
        )

        # Creiamo il vector store partendo dai vettori già calcolati
        return FAISS.from_embeddings(
            text_embeddings=[
                (document.page_content, embedding)
                for document, embedding in zip(documents, embeddings)
            ],
            embedding=self.embeddings,
            metadatas=[
                document.metadata
                for document in documents
            ]
        )

if __name__ == "__main__":
    service = LangChainService()

    # Creiamo il vector store con i nostri documenti
    vector_store = service.create_vector_store()

    # Chiediamo a FAISS anche il punteggio di distanza
    results = vector_store.similarity_search_with_score(
        "Come funziona Python?",
        k=3
    )

    # Stampiamo documento e score per capire la metrica utilizzata
    for document, score in results:
        print(
            document.metadata["title"],
            score
        )