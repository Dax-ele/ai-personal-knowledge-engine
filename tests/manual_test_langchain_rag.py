from ai_brain.rag.langchain_rag_service import LangChainRAGService


service = LangChainRAGService()

# Poniamo una domanda al nostro RAG
answer, documents = service.answer(
    "Qual è il ruolo di Java nello sviluppo backend?"
)

print("RISPOSTA:")
print(answer)

print("\nFONTI:")

for document in documents:
    print("\n---")
    print(f"Document ID: {document.metadata['document_id']}")
    print(f"Title: {document.metadata['title']}")
    print(f"Content:\n{document.page_content}")