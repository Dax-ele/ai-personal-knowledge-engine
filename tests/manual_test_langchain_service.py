from ai_brain.rag.langchain_service import LangChainService


service = LangChainService()

# Creiamo il vector store usando i chunk
vector_store = service.create_vector_store()

# Recuperiamo i chunk più simili alla query
results = vector_store.similarity_search_with_score(
    "Come funziona Java?",
    k=3
)

print(f"Numero risultati: {len(results)}")

for document, score in results:
    print("\n---")
    print(f"Score: {score}")
    print(f"Document ID: {document.metadata['document_id']}")
    print(f"Title: {document.metadata['title']}")
    print(f"Content:\n{document.page_content}")