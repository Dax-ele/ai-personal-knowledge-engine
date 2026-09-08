from dataclasses import dataclass


@dataclass
class DocumentChunk:
    # ID del documento originale
    document_id: str

    # ID univoco del chunk
    chunk_id: str

    # Posizione del chunk all'interno del documento
    chunk_index: int

    # Testo contenuto nel chunk
    content: str

    # Titolo del documento originale
    title: str