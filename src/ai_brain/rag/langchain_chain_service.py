from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from ai_brain.rag.langchain_service import LangChainService


class LangChainChainService:
    def __init__(self):
        # Creiamo il servizio che gestisce il vector store
        self.langchain_service = LangChainService()

        # Creiamo il modello LLM locale tramite Ollama
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0
        )

        # Creiamo il prompt template
        self.prompt = ChatPromptTemplate.from_template(
            """
Sei un assistente che risponde esclusivamente usando
le informazioni presenti nel contesto.

Regole:
1. Usa solo informazioni presenti nel contesto.
2. Non usare conoscenze esterne.
3. Non inventare informazioni.
4. Se il contesto non contiene una risposta sufficiente,
   rispondi esattamente:
   "Non ho trovato informazioni sufficienti nella knowledge base."

CONTESTO:
{context}

DOMANDA:
{question}
"""
        )

        # Parser che trasforma l'output del modello
        # in una semplice stringa Python
        self.output_parser = StrOutputParser()

        # Costruiamo la chain LangChain.
        # L'output di ogni componente passa al successivo.
        self.chain = (
            self.prompt
            | self.llm
            | self.output_parser
        )

        # Creiamo il vector store una sola volta
        self.vector_store = (
            self.langchain_service.create_vector_store()
        )

        # Creiamo il retriever con una soglia di similarità
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
        # non interroghiamo il modello.
        if not documents:
            return (
                "Non ho trovato informazioni sufficienti "
                "nella knowledge base.",
                []
            )

        # Creiamo il contesto concatenando i documenti
        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        # Eseguiamo la chain passando domanda e contesto
        answer = self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return answer, documents


if __name__ == "__main__":
    service = LangChainChainService()

    # Testiamo una domanda presente nella knowledge base
    answer, documents = service.answer(
        "Come funziona Python?"
    )

    print("RISPOSTA:")
    print(answer)

    print("\nDOCUMENTI UTILIZZATI:")

    for document in documents:
        print(
            document.metadata["title"]
        )