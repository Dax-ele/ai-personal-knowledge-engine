from ai_brain.search.chunk_service import ChunkSearchService


service = ChunkSearchService()

# Cerchiamo informazioni relative a Java
results = service.search(
    "Come funziona Java?"
)

for result in results:
    print("\n---")
    print(f"Chunk: {result.chunk.chunk_id}")
    print(f"Score: {result.score}")
    print(f"Content:\n{result.chunk.content}")