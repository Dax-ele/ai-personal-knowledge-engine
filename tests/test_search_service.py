from ai_brain.search.service import SearchService


def test_search_returns_most_relevant_document():
    service = SearchService()

    results = service.search("Come funziona Python?")

    assert len(results) > 0
    assert results[0].document.id == "python"
    assert results[0].score > results[1].score