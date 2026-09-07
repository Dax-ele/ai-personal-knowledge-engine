from ai_brain.llm.service import LLMService
from ai_brain.search.service import SearchService


class RAGService:
    def __init__(self):
        self.search_service = SearchService()
        self.llm_service = LLMService()

    def answer(self, question, top_k=3):
        results = self.search_service.search(
            question,
            top_k=top_k
        )
        if not results:
            return (
            "Non ho trovato informazioni sufficienti nella knowledge base.",[]
            )
        context = "\n\n".join(
            result.document.content
            for result in results
        )

        prompt = f"""
Usa esclusivamente il contesto seguente per rispondere alla domanda.

CONTESTO:
{context}

DOMANDA:
{question}

Se il contesto non contiene informazioni sufficienti,
dillo esplicitamente senza inventare informazioni.
"""

        answer = self.llm_service.generate(prompt)

        return answer, results