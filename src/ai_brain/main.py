from fastapi import FastAPI
from pydantic import BaseModel

from ai_brain.rag.service import RAGService


app = FastAPI(
    title="AI Personal Knowledge Engine",
    description="An AI system for managing and querying personal knowledge",
    version="0.1.0"
)


rag_service = RAGService()


class AskRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Personal Knowledge Engine is running"
    }


@app.post("/ask")
def ask(request: AskRequest):
    answer, results = rag_service.answer(request.question)
    
    return {
        "answer": answer,
        "sources": [
            {
                "title": result.document.title,
                "score": result.score
            }
            for result in results
        ]
    }