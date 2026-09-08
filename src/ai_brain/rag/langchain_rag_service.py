from ai_brain.llm.service import LLMService
from ai_brain.rag.langchain_service import LangChainService


class LangChainRAGService:
    def __init__(self):
        # Creiamo il servizio che gestisce vector store e Retriever
        self.langchain_service = LangChainService()

        # Manteniamo il nostro LLMService per utilizzare Ollama
        self.llm_service = LLMService()

        # Creiamo il vector store una volta sola
        self.vector_store = self.langchain_service.create_vector_store()

        # Creiamo il Retriever con una soglia di similarità
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5
            }
        )

    def answer(self, question):
        # Recuperiamo i documenti rilevanti
        documents = self.retriever.invoke(question)

        # Se non troviamo documenti sufficientemente simili,
        # evitiamo di interrogare il modello.
        if not documents:
            return (
                "Non ho trovato informazioni sufficienti "
                "nella knowledge base.",
                []
            )

        # Costruiamo il contesto usando il contenuto dei documenti
        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = f"""
Sei un assistente che risponde esclusivamente usando le informazioni
presenti nel CONTEXTO.

Regole:
1. Usa solo informazioni presenti nel CONTEXTO.
2. Non usare conoscenze esterne o informazioni apprese dal modello.
3. Non fare supposizioni o deduzioni non supportate dal CONTEXTO.
4. Se il CONTEXTO non contiene una risposta sufficiente, rispondi
   esattamente:
   "Non ho trovato informazioni sufficienti nella knowledge base."

CONTEXTO:
{context}

DOMANDA:
{question}

RISPOSTA:
"""

        # Inviamo il prompt al nostro LLM locale
        answer = self.llm_service.generate(prompt)

        return answer, documents


if __name__ == "__main__":
    service = LangChainRAGService()

    # Testiamo una domanda presente nella knowledge base
    answer, documents = service.answer(
        "Qual è la capitale del Giappone?"
    )

    print("RISPOSTA:")
    print(answer)

    print("\nDOCUMENTI UTILIZZATI:")

    for document in documents:
        print(
            document.metadata["title"]
        )