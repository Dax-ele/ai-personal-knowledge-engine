import faiss
import numpy as np

from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document as LangChainDocument

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
    
       # Convertiamo gli embeddings in una matrice NumPy float32
       vectors = np.array(
           embeddings,
           dtype="float32"
       )
    
       # Creiamo un indice FAISS basato sull'Inner Product.
       # Con vettori normalizzati, equivale alla cosine similarity.
       index = faiss.IndexFlatIP(
           vectors.shape[1]
       )
    
       # Inseriamo gli embeddings nell'indice.
       index.add(vectors)
    
       # Creiamo il docstore che associa gli ID FAISS ai documenti.
       docstore = InMemoryDocstore({
           str(i): document
           for i, document in enumerate(documents)
       })
    
       # Creiamo la mappa tra gli ID FAISS e i documenti.
       index_to_docstore_id = {
           i: str(i)
           for i in range(len(documents))
       }
    
       # Creiamo il vector store LangChain.
       # Lo score di FAISS viene usato direttamente come relevance score.
       return FAISS(
           embedding_function=self.embeddings,
           index=index,
           docstore=docstore,
           index_to_docstore_id=index_to_docstore_id,
           relevance_score_fn=lambda score: float(score)
       )


if __name__ == "__main__":
    service = LangChainService()

    # Creiamo il vector store con i nostri documenti
    vector_store = service.create_vector_store()

    # Recuperiamo anche il relevance score calcolato da LangChain
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.5
        }
    )
    
    results = retriever.invoke(
        "Come funziona Python?"
    )
    
    for document in results:
        print(document.metadata["title"])