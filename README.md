# AI Personal Knowledge Engine

An AI-powered personal knowledge assistant for organizing, searching and understanding personal knowledge using **embeddings, semantic search, RAG and local LLMs**.

The project is built incrementally to explore the fundamentals of modern AI Engineering, from embeddings and vector search to Retrieval-Augmented Generation and LLM orchestration.

## Goal

Build a personal AI assistant capable of:

* ingesting documents, notes and code
* converting knowledge into vector embeddings
* performing semantic search
* retrieving relevant information
* generating answers using retrieved context
* running LLMs locally

## Architecture

The current system follows a simple RAG pipeline:

```text
Documents
    ↓
Document Loader
    ↓
Embeddings
    ↓
Vector Search
    ↓
Relevant Documents
    ↓
LLM
    ↓
Answer
```

The project currently contains both a **manual implementation** of the RAG pipeline and an experimental **LangChain implementation**.

The manual implementation is intentionally kept to understand the underlying concepts before relying on higher-level frameworks.

## Technologies

* **Python**
* **FastAPI**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Sentence Transformers**
* **FAISS**
* **LangChain**
* **Ollama**
* **Qwen 2.5 3B**
* **Jupyter Notebook**

## Current Features

### Document ingestion

Markdown documents can be loaded into the knowledge base.

### Embeddings

Documents and queries are converted into vector representations using Sentence Transformers.

Current embedding model:

```text
all-MiniLM-L6-v2
```

### Semantic Search

The system compares query embeddings with document embeddings and ranks documents according to semantic similarity.

The current implementation uses cosine similarity with Scikit-learn.

### Knowledge Base

Document embeddings can be persisted locally in:

```text
data/knowledge_base.json
```

### RAG

The system retrieves relevant documents and provides them as context to a local LLM.

If no sufficiently relevant information is found, the system avoids sending the question to the LLM.

### Local LLM

The project currently uses:

```text
Ollama
└── Qwen 2.5 3B
```

This allows the project to run without relying on paid external LLM APIs.

### FastAPI API

The RAG system is exposed through a simple API.

Current endpoint:

```text
POST /ask
```

Example request:

```json
{
  "question": "Come funziona Python?"
}
```

## LangChain

LangChain is currently being introduced as a second implementation of parts of the RAG pipeline.

The goal is not simply to use the framework, but to understand what abstractions it provides compared to the manual implementation.

Current exploration includes:

```text
Embeddings
    ↓
Vector Store
    ↓
Retriever
```

LangGraph and more advanced agentic workflows will be introduced later only if they provide a real benefit to the project.

## Project Structure

```text
ai-personal-knowledge-engine/
│
├── data/
│   ├── documents/
│   └── knowledge_base.json
│
├── docs/
│
├── notebooks/
│
├── src/
│   └── ai_brain/
│       ├── documents/
│       ├── embeddings/
│       ├── knowledge/
│       ├── search/
│       ├── llm/
│       └── rag/
│
├── tests/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Roadmap

* [x] Project setup
* [x] Document loading
* [x] Embedding generation
* [x] Semantic search
* [x] Knowledge base persistence
* [x] Local LLM integration
* [x] Manual RAG pipeline
* [x] FastAPI `/ask` endpoint
* [x] Initial LangChain integration
* [ ] Configure cosine similarity correctly in the LangChain/FAISS pipeline
* [ ] Compare manual RAG vs LangChain RAG
* [ ] Improve document chunking
* [ ] Improve retrieval quality
* [ ] Add evaluation of retrieval results
* [ ] Explore LangGraph
* [ ] Add a simple frontend
* [ ] Improve deployment and production architecture

## Status

🚧 **Work in progress**

This project is being developed incrementally as a practical exploration of AI Engineering concepts.
