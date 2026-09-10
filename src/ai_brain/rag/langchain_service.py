import faiss
import numpy as np

from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from ai_brain.rag.langchain_chunker import LangChainChunker
from ai_brain.rag.langchain_embeddings import LangChainEmbeddingAdapter


class LangChainService:
    def __init__(self):
        # Servizio che divide i documenti in chunk
        self.chunker = LangChainChunker(
            chunk_size=500,
            chunk_overlap=50
        )

        # Adapter che collega il nostro embedding service a LangChain
        self.embeddings = LangChainEmbeddingAdapter()

    def load_chunks(self):
        # Carichiamo tutti i chunk creati da LangChain
        return self.chunker.split_documents()

    def create_vector_store(self):
        # Recuperiamo i chunk da indicizzare
        documents = self.load_chunks()

        # Calcoliamo gli embeddings dei chunk
        embeddings = self.embeddings.embed_documents(
            [
                document.page_content
                for document in documents
            ]
        )

        # Convertiamo gli embeddings in una matrice NumPy float32
        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        # Creiamo un indice FAISS basato sull'Inner Product.
        # Con vettori normalizzati equivale alla cosine similarity.
        index = faiss.IndexFlatIP(
            vectors.shape[1]
        )

        # Inseriamo gli embeddings nell'indice FAISS
        index.add(vectors)

        # Associamo ogni ID FAISS al relativo chunk
        docstore = InMemoryDocstore({
            str(i): document
            for i, document in enumerate(documents)
        })

        # Creiamo la mappa tra indice FAISS e docstore
        index_to_docstore_id = {
            i: str(i)
            for i in range(len(documents))
        }

        # Creiamo il vector store LangChain
        return FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore=docstore,
            index_to_docstore_id=index_to_docstore_id,
            relevance_score_fn=lambda score: float(score)
        )