AI Personal Knowledge Engine — Project Recap
Obiettivo del progetto

Realizzare un Second Brain personale basato su AI, con l'obiettivo di imparare in modo pratico le tecnologie più richieste per il ruolo di AI Engineer.

Il progetto sarà sviluppato in maniera incrementale, comprendendo i concetti fondamentali invece di utilizzare framework che nascondono la complessità.

Obiettivi finali:

organizzare documenti e conoscenza personale;
ricerca semantica;
gestione degli embeddings;
Vector Database;
Retrieval Augmented Generation (RAG);
API REST con FastAPI;
interfaccia utente.
Setup completato
Repository GitHub

Repository creata:

ai-personal-knowledge-engine

Repository inizializzata con:

README
LICENSE
.gitignore
Struttura del progetto
ai-personal-knowledge-engine/

├── docs/
├── notebooks/
├── src/
│   └── ai_brain/
│       ├── __init__.py
│       ├── main.py
│       └── embeddings/
│           ├── __init__.py
│           └── service.py
│
├── tests/
│
├── requirements.txt
├── pyproject.toml
└── README.md
Ambiente Python

Creazione virtual environment

python -m venv .venv

Attivazione

Windows

.venv\Scripts\activate

Verifica

python --version

Verifica ambiente

where python

Il percorso deve puntare a:

.venv\Scripts\python.exe
Gestione dipendenze

Installazione librerie

pip install fastapi uvicorn
pip install pytest
pip install python-dotenv
pip install jupyter notebook
pip install numpy pandas scikit-learn sentence-transformers

Aggiornamento requirements

pip freeze > requirements.txt

Visualizzare librerie installate

pip list
Configurazione progetto Python

Creato

pyproject.toml

Installazione package locale

pip install -e .

Questo permette import del tipo

from ai_brain.main import app

senza modificare il PYTHONPATH.

Backend

Creato backend FastAPI.

Avvio

uvicorn ai_brain.main:app --reload

Indirizzi

http://127.0.0.1:8000

Swagger

http://127.0.0.1:8000/docs
Testing

Creati test automatici.

Esecuzione

pytest

Risultato

2 passed
Git

Controllo modifiche

git status

Aggiunta file

git add .

Commit

git commit -m "messaggio"

Invio su GitHub

git push

Storico

git log --oneline

Differenze

git diff
Primo notebook AI

Creato

notebooks/01_embeddings.ipynb

Obiettivo

Comprendere il funzionamento degli embeddings.

Librerie utilizzate

NumPy
Pandas
Sentence Transformers
Scikit-learn

Modello utilizzato

all-MiniLM-L6-v2
Primo esperimento

Trasformazione di tre frasi in embeddings.

Output ottenuto

(3, 384)

Interpretazione

3 frasi
ogni frase è rappresentata da un vettore di 384 dimensioni
Similarità semantica

Utilizzo di

cosine_similarity()

per confrontare il significato delle frasi.

Concetto fondamentale imparato

Testo

↓

Embedding

↓

Vettore numerico

↓

Confronto matematico

Questa è la base di:

Semantic Search
Vector Database
RAG
Primo componente del progetto

Creato

EmbeddingService

File

src/ai_brain/embeddings/service.py

Responsabilità

caricare il modello;
generare embeddings;
calcolare la similarità.

In questo modo il notebook rimane un ambiente di sperimentazione, mentre il codice riutilizzabile vive in src/.

Cosa ho imparato
Python
Virtual Environment
struttura professionale con src
package Python
testing con pytest
Backend
FastAPI
organizzazione del progetto
API REST
AI
Sentence Transformers
Embeddings
Cosine Similarity
rappresentazione vettoriale del testo
Software Engineering
separazione tra prototipo e codice di produzione;
test automatici;
Git workflow.
Roadmap del progetto
Sprint 1 (in corso)
✅ setup del progetto
✅ notebook embeddings
✅ EmbeddingService
⏳ rifinitura del servizio
Sprint 2

Document Loader

Obiettivo

Leggere documenti reali.

Supporto a:

TXT
Markdown
PDF

Creare il componente

DocumentLoader
Sprint 3

Vector Database

Introduzione di:

ChromaDB oppure FAISS

Obiettivo

Memorizzare e recuperare embeddings.

Sprint 4

Semantic Search

Creare un motore di ricerca sui documenti.

Workflow

Domanda

↓

Embedding

↓

Vector Search

↓

Documenti più rilevanti
Sprint 5

RAG

Integrare un LLM.

Workflow

Domanda

↓

Retrieval

↓

LLM

↓

Risposta
Sprint 6

Backend completo

API come:

POST /documents

POST /search

POST /ask
Sprint 7

Interfaccia utente

Probabilmente Streamlit.

Filosofia del progetto

L'obiettivo non è costruire un chatbot.

L'obiettivo è comprendere e implementare uno per uno tutti i componenti di un moderno sistema AI:

Documenti

↓

Embeddings

↓

Vector Database

↓

Semantic Search

↓

Retrieval

↓

LLM

↓

Applicazione
La mia valutazione

Ti faccio anche un feedback sul percorso fin qui.

Secondo me hai affrontato la parte più difficile del progetto: impostare basi solide. Molti iniziano direttamente con LangChain o con un tutorial, ottenendo qualcosa che funziona ma senza capire davvero come è costruito.

Noi abbiamo fatto il contrario: abbiamo costruito un progetto che cresce in modo professionale, con Git, test, struttura src, notebook per la sperimentazione e componenti riutilizzabili. È un approccio più lento all'inizio, ma tra qualche mese farà una differenza enorme nel tuo portfolio e nella tua preparazione per un ruolo da AI Engineer.

La prossima volta inizieremo a lavorare con documenti reali. Da lì il progetto smetterà di essere un esercizio sugli embeddings e inizierà a diventare il tuo vero AI Personal Knowledge Engine.