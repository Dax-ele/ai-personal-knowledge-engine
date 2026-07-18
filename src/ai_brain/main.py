from fastapi import FastAPI


app = FastAPI(
    title="AI Personal Knowledge Engine",
    description="An AI system for managing and querying personal knowledge",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Personal Knowledge Engine is running"
    }