from pathlib import Path

from ai_brain.documents.models import Document

class DocumentLoader:

    def __init__(self, documents_path: str = "data/documents"):
        self.documents_path = Path(documents_path)

    def load(self):

        documents = []

        for file in self.documents_path.glob("*.md"):

            content = file.read_text(
                encoding="utf-8"
            )

            document = Document(
                id=file.stem,
                title=file.stem.replace("_", " ").title(),
                content=content
            )

            documents.append(document)

        return documents

if __name__ == "__main__":

    loader = DocumentLoader()

    documents = loader.load()

    print(f"Trovati {len(documents)} documenti\n")

    for document in documents:

        print(document)

        print("-" * 40)