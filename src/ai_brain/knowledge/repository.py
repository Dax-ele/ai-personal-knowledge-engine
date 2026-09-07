import json
from pathlib import Path

from ai_brain.documents.models import Document
from ai_brain.knowledge.models import DocumentEmbedding


class KnowledgeRepository:

    def __init__(
        self,
        file_path="data/knowledge_base.json"
    ):
        self.file_path = Path(file_path)

    def load(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        result = []

        for item in data:
            document = Document(
                id=item["id"],
                title=item["title"],
                content=item["content"]
            )

            result.append(
                DocumentEmbedding(
                    document=document,
                    embedding=item["embedding"]
                )
            )

        return result
    
    def save(self, items):

        data = []

        for item in items:

            data.append({
                "id": item.document.id,
                "title": item.document.title,
                "content": item.document.content,
                "embedding": item.embedding
            })


        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )


