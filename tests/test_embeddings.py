from ai_brain.embeddings.service import EmbeddingService


def test_embedding_creation():

    service = EmbeddingService()

    embeddings = service.encode(
        [
            "Python è un linguaggio di programmazione"
        ]
    )

    assert embeddings.shape[0] == 1


def test_similarity():

    service = EmbeddingService()

    score = service.similarity(
        "Python è un linguaggio di programmazione",
        "Java è usato nello sviluppo software"
    )

    assert score > 0