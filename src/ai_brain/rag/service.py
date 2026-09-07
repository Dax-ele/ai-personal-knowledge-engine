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

        return self.llm_service.generate(prompt)

if __name__ == "__main__":
    service = RAGService()

    answer = service.answer(
        "Qual è la capitale del Giappone?"
    )

    print(answer)