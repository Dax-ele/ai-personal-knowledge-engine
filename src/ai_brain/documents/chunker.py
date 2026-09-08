from ai_brain.documents.chunk_models import DocumentChunk
from ai_brain.documents.models import Document


class DocumentChunker:
    def __init__(self, chunk_size=500, chunk_overlap=50):
        # Numero massimo di caratteri per chunk
        self.chunk_size = chunk_size

        # Numero di caratteri condivisi tra chunk consecutivi
        self.chunk_overlap = chunk_overlap

        # L'overlap deve essere più piccolo della dimensione del chunk
        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap deve essere minore di chunk_size"
            )

    def split(self, document: Document):
        # Contenuto del documento originale
        text = document.content

        chunks = []

        # Posizione iniziale del chunk corrente
        start = 0

        # Indice progressivo dei chunk
        chunk_index = 0

        while start < len(text):
            # Calcoliamo la posizione finale del chunk
            end = start + self.chunk_size

            # Estraiamo il contenuto
            chunk_content = text[start:end]

            # Creiamo il chunk con i metadata del documento originale
            chunk = DocumentChunk(
                document_id=document.id,
                chunk_id=f"{document.id}_chunk_{chunk_index}",
                chunk_index=chunk_index,
                content=chunk_content,
                title=document.title
            )

            chunks.append(chunk)

            # Passiamo al chunk successivo mantenendo l'overlap
            start = end - self.chunk_overlap

            chunk_index += 1

        return chunks