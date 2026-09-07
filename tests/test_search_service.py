from ai_brain.search.service import SearchService


def test_search_returns_only_relevant_documents():
    service = SearchService()

    results = service.search("Come funziona Python?")

    assert len(results) > 0
    assert results[0].document.id == "python"

    for result in results:
        assert result.score >= 0.5
def test_search_discards_low_similarity_documents():
    service = SearchService()

    results = service.search("Qual è la capitale del Giappone?")

    assert len(results) == 0