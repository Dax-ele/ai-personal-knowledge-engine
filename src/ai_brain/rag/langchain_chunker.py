from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from ai_brain.documents.loader import DocumentLoader


class LangChainChunker:
    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=50
    ):
        # Carichiamo i documenti Markdown
        self.loader = DocumentLoader()

        # Creiamo lo splitter LangChain
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(self):
        # Carichiamo i documenti originali
        documents = self.loader.load()

        chunks = []

        for document in documents:
            # Convertiamo il documento nel formato
            # atteso dallo splitter
            split_chunks = self.splitter.create_documents(
                [document.content],
                metadatas=[
                    {
                        "document_id": document.id,
                        "title": document.title
                    }
                ]
            )

            chunks.extend(split_chunks)

        return chunks