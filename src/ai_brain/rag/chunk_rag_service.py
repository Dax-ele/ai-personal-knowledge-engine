from ai_brain.llm.service import LLMService
from ai_brain.search.chunk_service import ChunkSearchService


class ChunkRAGService:
    def __init__(self):
        # Servizio che cerca informazioni nei chunk
        self.search_service = ChunkSearchService()

        # Modello LLM locale
        self.llm_service = LLMService()

    def answer(self, question):
        # Cerchiamo i chunk più rilevanti
        results = self.search_service.search(
            question,
            top_k=3,
            score_threshold=0.5
        )

        # Se non troviamo informazioni sufficientemente rilevanti,
        # evitiamo di interrogare il modello.
        if not results:
            return (
                "Non ho trovato informazioni sufficienti "
                "nella knowledge base.",
                []
            )

        # Costruiamo il contesto usando i chunk trovati
        context = "\n\n".join(
            result.chunk.content
            for result in results
        )

        # Costruiamo il prompt per il modello
        prompt = f"""
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

RISPOSTA:
"""

        # Inviamo il prompt al modello locale
        answer = self.llm_service.generate(prompt)

        return answer, results


if __name__ == "__main__":
    service = ChunkRAGService()

    # Testiamo una domanda sulla knowledge base
    answer, results = service.answer(
        "Qual è la capitale del Giappone?"
    )

    print("RISPOSTA:")
    print(answer)

    print("\nCHUNK UTILIZZATI:")

    for result in results:
        print(
            f"- {result.chunk.chunk_id} "
            f"(score={result.score:.3f})"
        )